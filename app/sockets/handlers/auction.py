import time
from flask_socketio import emit
from app.extensions import socketio
from app.sockets.sessions import get_session

ROUND_SECONDS, RESULT_SECONDS = 60, 2

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

def initialise_auction(session):
    if not session.get("auction"):
        session["auction"] = {"round_index":0, "round_progress":0, "current_item_pair":list(ITEM_PAIRS[0]),
            "votes":{}, "finished_players":set(), "budget":100, "purchased_items":[],
            "status":"waiting", "round_result":None, "ends_at":None, "timer_token":0}
    return session["auction"]

def _valid_player(session, payload):
    if not isinstance(payload, dict) or not payload.get("sessionCode"):
        return None
    player_id = payload.get("playerId")
    return player_id if player_id in session["players"] else None

def _player_ids(session):
    return set(session["players"])

def _state(session, player_id=None):
    auction = session["auction"]
    pair = ITEM_PAIRS[auction["round_index"]] if auction["round_index"] < len(ITEM_PAIRS) else ()
    state = {"phase":session["phase"], "round":auction["round_index"] + 1, "totalRounds":len(ITEM_PAIRS),
        "items":list(pair), "budget":auction["budget"], "purchasedItems":auction["purchased_items"],
        "voteCount":len(auction["votes"]), "playerCount":len(_player_ids(session)),
        "finishedCount":len(auction["finished_players"]), "status":auction["status"],
        "endsAt":auction["ends_at"], "roundResult":auction["round_result"]}
    if player_id:
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
    auction.update({"current_item_pair":list(ITEM_PAIRS[auction["round_index"]]),
        "round_progress":auction["round_index"], "votes":{}, "finished_players":set(), "status":"voting", "round_result":None,
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
    if auction["round_index"] == len(ITEM_PAIRS):
        auction["status"] = "complete"
        #expose the final inventory at session level for the mission phase, without making it depend on auction implementation details
        session["purchased_items"] = list(auction["purchased_items"])
        session["phase"] = "mission"
        broadcast_auction_state(session_code, session)
        socketio.emit("auction_complete", {"purchasedItems":auction["purchased_items"]}, room=session_code)
    else:
        _start_round(session_code, session)

def _resolve(session_code, session, reason):
    auction = session["auction"]
    if auction["status"] != "voting": return False
    pair = ITEM_PAIRS[auction["round_index"]]
    counts = {item["id"]:0 for item in pair} | {"skip":0}
    for choice in auction["votes"].values(): counts[choice] += 1
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
    if not session or not _valid_player(session, payload) or payload["playerId"] != session["host_id"] or session["phase"] != "start_game": return
    initialise_auction(session)
    session["phase"] = "auction"
    _start_round(code, session)
    emit("auction_started", room=code)

@socketio.on("auction_vote")
def auction_vote(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None; session = get_session(code)
    if not session or session.get("phase") != "auction": return
    player, auction = _valid_player(session, payload), session["auction"]
    choices = {item["id"] for item in ITEM_PAIRS[auction["round_index"]]}
    if not player or auction["status"] != "voting" or player in auction["finished_players"] or payload.get("itemId") not in choices: return
    auction["votes"][player] = payload["itemId"]
    broadcast_auction_state(code, session); emit_auction_state_to_player(session, player)

def _finish(code, session, player, skip=False):
    auction = session["auction"]
    if not player or auction["status"] != "voting" or player in auction["finished_players"]: return
    if skip: auction["votes"][player] = "skip"
    if player not in auction["votes"]: return
    auction["finished_players"].add(player)
    broadcast_auction_state(code, session); emit_auction_state_to_player(session, player)
    if auction["finished_players"] == _player_ids(session): _resolve(code, session, "all_finished")

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
    if player == session["host_id"] and auction["status"] == "voting" and auction["finished_players"] == _player_ids(session): _resolve(code, session, "host")
