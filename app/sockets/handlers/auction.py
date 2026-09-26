import time
import re
from random import sample, shuffle
from flask_socketio import emit
from app.extensions import socketio
from app.game_data.example_mission import example_mission
from app.game_data.items import items_dict
from app.sockets.handlers import mission
from app.sockets.sessions import get_session

ROUND_SECONDS, RESULT_SECONDS = 60, 2

#REVIEW ARE MISSIONS SUBMITTED
#prices and pairs are deliberately server-side. The browser may only select an id from the pair currently being auctioned.
#generated some for now until we get the missions file in
#make sure image sizes are consistent 
#use the 64px versions for the main auction cards, use 32px versions for the inventory hotbar
ITEM_PAIRS = [
    ({"id":"axe","name":"Axe","cost":20,"image":"axe-white-64.png","description":"Chops through obstacles and enemies with ease."},{"id":"water-bottle","name":"Water Bottle","cost":5,"image":"sport-bottle-white-64.png","description":"Keeps your team hydrated for the long haul."}),
    ({"id":"shovel","name":"Shovel","cost":15,"image":"shovel-32.png","description":"Useful for digging, clearing, and improvised defence."},{"id":"map","name":"Map","cost":10,"image":"icons8-map-64.png","description":"Helps the team find a safer route."}),
    ({"id":"toolkit","name":"Toolkit","cost":25,"image":"icons8-tools-64.png","description":"Repair equipment when the mission gets rough."},{"id":"gps","name":"GPS","cost":20,"image":"icons8-gps-signal-64.png","description":"Pinpoint your position when the route is unclear."}),
    ({"id":"tent","name":"Tent","cost":20,"image":"icons8-camping-tent-64.png","description":"A dependable shelter for an overnight stop."},{"id":"compass","name":"Compass","cost":10,"image":"icons8-compass-64.png","description":"A simple backup when technology fails."}),
    ({"id":"taser","name":"Taser","cost":30,"image":"icons8-taser-64.png","description":"Provides a non-lethal defensive option."},{"id":"fuel","name":"Fuel","cost":15,"image":"icons8-petrol-64.png","description":"Keep the vehicle moving when every kilometre matters."}),
    ({"id":"car","name":"Sedan","cost":35,"image":"icons8-sedan-64.png","description":"Carry the team and supplies across long distances."},{"id":"credit-card","name":"Credit Card","cost":15,"image":"icons8-credit-card-64.png","description":"An emergency resource for an unexpected problem."}),
    ({"id":"mountain-gear","name":"Mountain Gear","cost":25,"image":"icons8-mountain-64.png","description":"Makes difficult terrain considerably safer."},{"id":"food","name":"Food Supplies","cost":10,"image":"apple-64.png","description":"A small supply that keeps the team going."}),
    ({"id":"armor","name":"Armoured Boots","cost":20,"image":"icons8-armored-boot-64.png","description":"Protect your feet through hazardous ground."},{"id":"cat","name":"Cat","cost":5,"image":"cat-32.png","description":"Morale support for the journey ahead."}),
]

ITEM_IMAGES = {item["name"]: item for pair in ITEM_PAIRS for item in pair}


def _item_id(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _mission_item(name):
    item_data = items_dict.get(name)
    if item_data:
        return {
            "id": _item_id(name),
            "name": name,
            "cost": item_data.get("cost", 20),
            "image": item_data.get("image") or "icons8-idea-64.png",
            "hotbar_image": item_data.get("hotbar_image") or "icons8-idea-32.png",
            "description": item_data.get("desc", f"Useful for the {name.lower()} challenge."),
        }
    existing = ITEM_IMAGES.get(name)
    if existing:
        item = dict(existing)
        item.setdefault("hotbar_image", item["image"])
        return item
    return {
        "id": _item_id(name),
        "name": name,
        "cost": 20,
        "image": "icons8-idea-64.png",
        "hotbar_image": "icons8-idea-32.png",
        "description": f"Useful for the {name.lower()} challenge.",
    }


def _build_mission_item_pairs(generated_mission):
    challenge_item_names = [
        list(generated_mission[f"challenge_{index}"].get("items", {}))
        for index in range(1, 7)
    ]

    def select_unique_mission_items(index, used_item_ids):
        if index == len(challenge_item_names):
            return []
        available = [
            _mission_item(name)
            for name in challenge_item_names[index]
            if _mission_item(name)["id"] not in used_item_ids
        ]
        for item in available:
            selected = select_unique_mission_items(
                index + 1, used_item_ids | {item["id"]}
            )
            if selected is not None:
                return [item, *selected]
        return None

    mission_items = select_unique_mission_items(0, set())

    # Some missions use the same useful item for multiple challenges.
    # If unique items cannot be selected, use one useful item per challenge.
    if mission_items is None:
        mission_items = [
            _mission_item(item_names[0])
            for item_names in challenge_item_names
            if item_names
        ]

    random_items = [
        _mission_item(name)
        for name in items_dict
        if name not in {item["name"] for item in mission_items}
    ]
    pairs = []
    for mission_item in mission_items:
        random_item = sample(random_items, 1)[0]
        random_items.remove(random_item)
        pairs.append((mission_item, random_item))

    for _ in range(2):
        random_pair = sample(random_items, 2)
        pairs.append(tuple(random_pair))
        for item in random_pair:
            random_items.remove(item)

    #fully random challenge offer first then shuffling the completed auction rounds
    shuffle(pairs)
    return pairs

def initialise_auction(session, generated_mission=None):
    if not session.get("auction"):
        generated_mission = generated_mission or example_mission
        item_pairs = _build_mission_item_pairs(generated_mission)
        session["generated_mission"] = generated_mission
        session["auction"] = {"item_pairs": item_pairs, "round_index":0, "round_progress":0,
            "current_item_pair":list(item_pairs[0]),
            "selections":{}, "votes":{}, "finished_players":set(), "budget":1000, "purchased_items":[],
            "status":"waiting", "round_result":None, "ends_at":None, "timer_token":0}
    return session["auction"]

def _valid_player(session, payload):
    if not isinstance(payload, dict) or not payload.get("sessionCode"):
        return None
    player_id = payload.get("playerId")
    return player_id if player_id in session["players"] else None

def _player_ids(session):
    return set(session["players"])


def _connected_player_ids(session):
    return {
        player_id
        for player_id, player in session["players"].items()
        if player.get("connected")
    }


def _reevaluate_voting(
    session_code, session, reason, broadcast_if_incomplete=True
):
    auction = session.get("auction")
    if not auction or auction.get("status") != "voting":
        return False

    connected_players = _connected_player_ids(session)
    if connected_players and connected_players.issubset(
        auction["finished_players"]
    ):
        return _resolve(session_code, session, reason)

    if broadcast_if_incomplete:
        broadcast_auction_state(session_code, session)
    return False


def handle_player_disconnected(session_code, session):
    """Recheck an active vote without removing reconnectable player state."""
    _reevaluate_voting(session_code, session, "player_disconnected")


def handle_player_left(session_code, session, player_id):
    """Remove a departed player's round state and unblock remaining voters."""
    auction = session.get("auction")
    if not auction or auction.get("status") != "voting":
        return

    auction["votes"].pop(player_id, None)
    auction["finished_players"].discard(player_id)
    _reevaluate_voting(session_code, session, "player_left")


def _state(session, player_id=None):
    auction = session["auction"]
    connected_players = _connected_player_ids(session)
    item_pairs = auction["item_pairs"]
    pair = item_pairs[auction["round_index"]] if auction["round_index"] < len(item_pairs) else ()
    state = {"phase":session["phase"], "round":auction["round_index"] + 1, "totalRounds":len(item_pairs),
        "items":list(pair), "budget":auction["budget"], "purchasedItems":auction["purchased_items"],
        "voteCount":len(set(auction["votes"]) & connected_players), "playerCount":len(connected_players),
        "finishedCount":len(auction["finished_players"] & connected_players), "status":auction["status"],
        "endsAt":auction["ends_at"], "roundResult":auction["round_result"]}
    if player_id:
        state["mySelection"] = auction.get("selections", {}).get(player_id)
        state["myVote"] = auction["votes"].get(player_id)
    return state

def broadcast_auction_state(session_code, session):
    #individual votes remain anonymous and background tasks can broadcast too
    socketio.emit("auction_state", _state(session), room=session_code)

def emit_auction_state_to_player(session, player_id):
    emit("auction_state", _state(session, player_id))

def _timer(session_code, token):
    socketio.sleep(ROUND_SECONDS)
    session = get_session(session_code)
    if session and session.get("phase") == "auction":
        auction = session["auction"]
        if auction["status"] == "voting" and auction["timer_token"] == token:
            _resolve(session_code, session, "timer")

def _start_round(session_code, session):
    auction = session["auction"]
    auction.update({"current_item_pair":list(auction["item_pairs"][auction["round_index"]]),
        "round_progress":auction["round_index"], "selections":{}, "votes":{}, "finished_players":set(), "status":"voting", "round_result":None,
        "ends_at":time.time()+ROUND_SECONDS, "timer_token":auction["timer_token"]+1})
    broadcast_auction_state(session_code, session)
    socketio.start_background_task(_timer, session_code, auction["timer_token"])

def _advance(session_code, resolved_round):
    socketio.sleep(RESULT_SECONDS)
    session = get_session(session_code)
    if not session or session.get("phase") != "auction": return
    auction = session["auction"]
    if auction["status"] != "resolved" or auction["round_index"] != resolved_round: return
    auction["round_index"] += 1
    if auction["round_index"] == len(auction["item_pairs"]):
        auction["status"] = "complete"
        #expose the final inventory at session level for the mission phase, without making it depend on auction implementation details
        session["purchased_items"] = list(auction["purchased_items"])
        from app.sockets.handlers.mission import initialise_mission, broadcast_mission_state
        initialise_mission(session, session.get("generated_mission"))
        session["phase"] = "mission"
        broadcast_auction_state(session_code, session)
        broadcast_mission_state(session_code, session)
        socketio.emit("auction_complete", {"purchasedItems":auction["purchased_items"]}, room=session_code)
    else:
        _start_round(session_code, session)

def _resolve(session_code, session, reason):
    auction = session["auction"]
    if auction["status"] != "voting": return False
    pair = auction["item_pairs"][auction["round_index"]]
    counts = {item["id"]:0 for item in pair} | {"skip":0}
    connected_players = _connected_player_ids(session)
    for player_id, choice in auction["votes"].items():
        if player_id in connected_players:
            counts[choice] += 1
    highest = max(counts.values())
    winners = [choice for choice, count in counts.items() if count == highest]
    winner = winners[0] if len(winners) == 1 else None
    item = next((item for item in pair if item["id"] == winner), None)
    if item and item["cost"] <= auction["budget"]:
        auction["budget"] -= item["cost"]
        auction["purchased_items"].append(item)
        result = {"type":"purchase", "item":item, "reason":reason}
    elif item: result = {"type":"unaffordable", "item":item, "reason":reason}
    elif winner == "skip": result = {"type":"skip", "reason":reason}
    else: result = {"type":"tie", "reason":reason}
    auction.update({"status":"resolved", "ends_at":None, "round_result":result})
    broadcast_auction_state(session_code, session)
    socketio.start_background_task(_advance, session_code, auction["round_index"])
    return True

@socketio.on("begin_auction")
def begin_auction(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None
    session = get_session(code)
    if not session or not _valid_player(session, payload) or payload["playerId"] != session["host_id"] or session["phase"] != "mission_description": return
    initialise_auction(session, session.get("generated_mission"))
    session["phase"] = "auction"
    _start_round(code, session)
    emit("auction_started", room=code)

@socketio.on("auction_vote")
def auction_vote(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None; session = get_session(code)
    if not session or session.get("phase") != "auction": return
    player, auction = _valid_player(session, payload), session["auction"]
    choices = {item["id"] for item in auction["item_pairs"][auction["round_index"]]}
    if not player or auction["status"] != "voting" or payload.get("itemId") not in choices: return
    # Selections stay private until submitted, and may be changed while the
    # round remains open.
    auction["selections"][player] = payload["itemId"]
    emit_auction_state_to_player(session, player)

def _finish(code, session, player, skip=False):
    auction = session["auction"]
    if not player or auction["status"] != "voting": return
    if skip:
        auction["votes"][player] = "skip"
    elif player not in auction["selections"]:
        return
    else:
        #replaces the players vote with their most current one
        auction["votes"][player] = auction["selections"][player]
    auction["finished_players"].add(player)
    broadcast_auction_state(code, session); emit_auction_state_to_player(session, player)
    _reevaluate_voting(
        code, session, "all_finished", broadcast_if_incomplete=False
    )

@socketio.on("auction_skip")
def auction_skip(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None; session = get_session(code)
    if session and session.get("phase") == "auction": _finish(code, session, _valid_player(session, payload), True)

@socketio.on("auction_finish_voting")
def auction_finish_voting(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None; session = get_session(code)
    if session and session.get("phase") == "auction": _finish(code, session, _valid_player(session, payload))

@socketio.on("resolve_auction_round")
def resolve_auction_round(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None; session = get_session(code)
    if not session or session.get("phase") != "auction": return
    player, auction = _valid_player(session, payload), session["auction"]
    connected_players = _connected_player_ids(session)
    if player == session["host_id"] and auction["status"] == "voting" and connected_players and connected_players.issubset(auction["finished_players"]): _resolve(code, session, "host")
