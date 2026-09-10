""" THIS NEEDS TO BE REVIEWED AFTER THE MISSIONS ARE SUBMITTED
Authoritative Socket.IO state and actions for the mission phase
Angela have fun with this file some fake challenges are here for now
please make sure preoper missions and stuff are pulled from the correct spot later"""

import random

from flask import request
from flask_socketio import emit

from app.extensions import socketio
from app.sockets.sessions import get_session


# challenge data and the matching item stay on the server
#challenges are generated rn
possible_locations = [
    "Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano",
]


mission_structures = {

    "Train Heist": {
        "type": "Heist",
        "locations": {
            "Arctic Tundra": False,
            "Desert": False,
            "Jungle": True,
            "City": True,
            "Ocean": False,
            "Volcano": False,
        },
        "challenges": [
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Security Obstacle",
            "Steal",
            "Manmade Obstacle",
            "Security Obstacle",
            "Environmental Obstacle",
            "Getaway",
        ],
    },


    "Artifact Heist": {
        "type": "Heist",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": False,
            "Volcano": False,
        },
        "challenges": [
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Security Obstacle",
            "Steal",
            "Environmental Obstacle",
            "Security Obstacle",
            "Manmade Obstacle",
            "Getaway",
        ],
    },


    "Jewel Heist": {
        "type": "Heist",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": False,
            "Volcano": False,
        },
        "challenges": [
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Security Obstacle",
            "Steal",
            "Manmade Obstacle",
            "Security Obstacle",
            "Environmental Obstacle",
            "Getaway",
        ],
    },


    "Steal Enemy Information": {
        "type": "Heist",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": True,
            "Volcano": False,
        },
        "challenges": [
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Security Obstacle",
            "Steal",
            "Security Obstacle",
            "Manmade Obstacle",
            "Environmental Obstacle",
            "Getaway",
        ],
    },


    "Break Out Another Team": {
        "type": "Heist",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": False,
            "Volcano": False,
        },
        "challenges": [
            "Travel To Rendezvouz",
            "Manmade Obstacle",
            "Security Obstacle",
            "Contact Teammate/s",
            "Security Obstacle",
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Getaway",
        ],
    },


    "Escape Enemy Base": {
        "type": "Escape",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": False,
            "Volcano": False,
        },
        "challenges": [
            "Security Obstacle",
            "Manmade Obstacle",
            "Security Obstacle",
            "Getaway",
            "Contact Teammate/s",
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Travel To Rendezvouz",
        ],
    },


    "Extract Another Team": {
        "type": "Rescue Op",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": True,
            "Ocean": True,
            "Volcano": True,
        },
        "challenges": [
            "Contact Teammate/s",
            "Environmental Obstacle",
            "Travel To Rendezvouz",
            "Getaway",
            "Environmental Obstacle",
            "Manmade Obstacle",
            "Contact Teammate/s",
            "Find Shelter",
        ],
    },


    "Rescue Stranded Teammate": {
        "type": "Rescue Op",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": False,
            "City": False,
            "Ocean": True,
            "Volcano": True,
        },
        "challenges": [
            "System Failure",
            "Find Shelter",
            "Environmental Obstacle",
            "Contact Teammate/s",
            "Travel To Rendezvouz",
            "Environmental Obstacle",
            "Find Water",
            "Getaway",
        ],
    },


    "Repair Research Base": {
        "type": "Survival",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": False,
            "City": False,
            "Ocean": True,
            "Volcano": True,
        },
        "challenges": [
            "Environmental Obstacle",
            "System Failure",
            "Environmental Obstacle",
            "Make Repairs",
            "Environmental Obstacle",
            "Make Repairs",
            "System Failure",
            "Make Repairs",
        ],
    },


    "Get Rescued": {
        "type": "Survival",
        "locations": {
            "Arctic Tundra": True,
            "Desert": True,
            "Jungle": True,
            "City": False,
            "Ocean": True,
            "Volcano": True,
        },
        "challenges": [
            "Environmental Obstacle",
            "Find Water",
            "Environmental Obstacle",
            "Find Shelter",
            "Contact Teammate/s",
            "Environmental Obstacle",
            "Travel To Rendezvouz",
            "Getaway",
        ],
    },
}

location_challanges = {
    "Arctic Tundra": {
        "Environmental Obstacle":   ["Blizzard", "Temperature Drop", "Frozen Lake", "Ice Cliff", "Cliff", "Arctic Bear"],
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Fortefied Structure"],
        "Getaway":                  ["Land Based Getaway", "Snow Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through", "Get Past the Laser Grid"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it", "Retrieve the Item from the Laser Grid"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall"], 
        "System Failure":           ["Central Heating Offline", "Main Reactor Failure", "Communications System Failure"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Snow Based Travel", "Water Based Travel", "Air Based Travel"],
    },  

    "Desert": {
        "Environmental Obstacle":   ["Sand Storm", "Heat Wave", "Venemous Snake", "Sand Dunes", "Quick Sand", "Mirages", "Nest of Scorpions"],
        "Manmade Obstacle":         ["Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Fortefied Structure"],
        "Getaway":                  ["Land Based Getaway", "Sand Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through", "Get Past the Laser Grid"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it", "Retrieve the Item from the Laser Grid"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Solar Panels"], 
        "System Failure":           ["Cooling Offline", "Main Reactor Failure", "Communications System Failure"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Sand Based Travel", "Air Based Travel"],
    },  

    "Jungle": {
        "Environmental Obstacle":   ["Fire", "Flash Flood", "River", "Fallen Trees Block Path", "Quick Sand", "Cliff", "Cyclone", "Deadly Insects", "Crocodile", "Deadly Marshland Gases"],
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Fortefied Structure"],
        "Getaway":                  ["Land Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through", "Get Past the Laser Grid"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it", "Retrieve the Item from the Laser Grid"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall"], 
        "System Failure":           ["Main Reactor Failure", "Communications System Failure"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Water Based Travel", "Air Based Travel"],
    },   

    "City": {
        "Environmental Obstacle":   ["Sand Storm", "Blizzard", "Temperature Drop", "Fire", "Flash Flood", "River", "Fallen Trees Block Path", "Heat Wave", "Cyclone"],
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Traffic", "Building"],
        "Getaway":                  ["Land Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through", "Get Past the Laser Grid"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it", "Retrieve the Item from the Laser Grid"],
        "Make Repairs":             ["Repair Vehicle", "Repair Collapsed Wall", "Repair Solar Panels"], 
        "System Failure":           ["Central Heating Offline", "Cooling Offline", "Main Reactor Failure", "Communications System Failure"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Water Based Travel", "Air Based Travel"],
    },   

    "Ocean": {
        "Environmental Obstacle":   ["Cyclone", "Collosal Wave", "Shark Attack", "Underwater Earthquake", "Shallow Reef"],
        "Manmade Obstacle":         ["Blockade", "Sea Mines", "Ship Graveyard", "Pirates"],
        "Getaway":                  ["Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Distract Guards", "Find Another Entrance", "Sneak Through", "Get Past the Laser Grid"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it", "Retrieve the Item from the Laser Grid"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Exit Hatch", "Repair Solar Panels"], 
        "System Failure":           ["Central Heating Offline", "Main Reactor Failure", "Communications System Failure", "Air Recycling System Offline"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Water Based Travel", "Air Based Travel"],
    },

    "Volcano": {
        "Environmental Obstacle":   ["Earthquake", "Lava Spout", "Volcanic Gases", "Ash", "Rockfall", "Landslide", "Extreme Heat"],
        "Manmade Obstacle":         [],
        "Getaway":                  [],
        "Security Obstacle":        [],
        "Steal":                    [],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Exit Hatch", "Repair Rover"], 
        "System Failure":           ["Cooling Offline", "Geo-Thermal Reactor Failure", "Communications System Failure", "Air Recycling System Offline"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Air Based Travel"],
    },

}

challenge_success_items = {

    
    # ENVIRONMENTAL OBSTACLES

    "Blizzard": ["mountain-gear", "tent", "food"],
    "Temperature Drop": ["mountain-gear", "tent", "food"],
    "Frozen Lake": ["mountain-gear", "axe"],
    "Ice Cliff": ["mountain-gear", "axe"],
    "Cliff": ["mountain-gear", "axe"],
    "Arctic Bear": ["taser", "armor"],

    "Sand Storm": ["mountain-gear", "tent"],
    "Heat Wave": ["water-bottle", "tent"],
    "Venemous Snake": ["taser", "armor"],
    "Sand Dunes": ["shovel", "car"],
    "Quick Sand": ["shovel", "mountain-gear"],
    "Mirages": ["map", "gps", "compass"],
    "Nest of Scorpions": ["armor", "taser"],

    "Fire": ["water-bottle", "armor"],
    "Flash Flood": ["mountain-gear", "tent"],
    "River": ["mountain-gear", "map"],
    "Fallen Trees Block Path": ["axe", "shovel"],
    "Cyclone": ["tent", "mountain-gear"],
    "Deadly Insects": ["armor", "food"],
    "Crocodile": ["taser", "armor"],
    "Deadly Marshland Gases": ["armor", "mountain-gear"],

    "Collosal Wave": ["mountain-gear", "tent"],
    "Shark Attack": ["taser", "armor"],
    "Underwater Earthquake": ["mountain-gear", "tent"],
    "Shallow Reef": ["mountain-gear", "map"],

    "Earthquake": ["mountain-gear", "tent"],
    "Lava Spout": ["armor", "mountain-gear"],
    "Volcanic Gases": ["armor", "mountain-gear"],
    "Ash": ["armor", "mountain-gear"],
    "Rockfall": ["mountain-gear", "armor"],
    "Landslide": ["shovel", "mountain-gear"],
    "Extreme Heat": ["water-bottle", "armor"],


    
    # MANMADE OBSTACLES
    

    "Dam": ["toolkit", "axe"],
    "Giant Wall": ["axe", "mountain-gear"],
    "Checkpoint": ["credit-card", "taser"],
    "Blockade": ["car", "axe"],
    "Collapsed Bridge": ["mountain-gear", "shovel"],
    "Building": ["map", "gps"],
    "Fortefied Structure": ["axe", "taser"],
    "Traffic": ["car", "gps"],

    "Sea Mines": ["map", "gps"],
    "Ship Graveyard": ["map", "gps"],
    "Pirates": ["taser", "credit-card"],


    
    # SECURITY OBSTACLES
    
    "Deactivate Security Cameras": ["toolkit"],
    "Deactivate Alarms": ["toolkit"],
    "Distract Guards": ["taser", "credit-card"],
    "Find Another Entrance": ["map", "gps", "compass"],
    "Sneak Through": ["mountain-gear", "armor"],
    "Get Past the Laser Grid": ["toolkit"],
    
    # STEAL
    
    "Break into the Vault": ["toolkit", "axe"],
    "Open the crate": ["axe", "toolkit"],
    "Pickpocket it": ["armor", "credit-card"],
    "Retrieve the Item from the Laser Grid": ["toolkit"],

 
    # GETAWAY
    
    "Land Based Getaway": ["car", "fuel"],
    "Snow Based Getaway": ["car", "fuel", "mountain-gear"],
    "Sand Based Getaway": ["car", "fuel"],
    "Water Based Getaway": ["map", "gps"],
    "Air Based Getaway": ["gps", "map"],
    "Use Stealth": ["mountain-gear", "armor"],
    "Mislead Pursuers": ["map", "gps", "compass"],


    
    # REPAIRS 

    "Repair Vehicle": ["toolkit", "fuel"],
    "Repair Enviro-Dome": ["toolkit", "shovel"],
    "Repair Collapsed Wall": ["toolkit", "axe"],
    "Repair Solar Panels": ["toolkit"],
    "Repair Exit Hatch": ["toolkit"],
    "Repair Rover": ["toolkit", "fuel"],

    
    # SYSTEM FAILURE 

    "Central Heating Offline": ["toolkit", "fuel"],
    "Main Reactor Failure": ["toolkit"],
    "Communications System Failure": ["toolkit"],
    "Cooling Offline": ["toolkit", "water-bottle"],
    "Geo-Thermal Reactor Failure": ["toolkit"],
    "Air Recycling System Offline": ["toolkit"],
    
    # WATER / SHELTER
    
    "Find Water": ["water-bottle", "map", "gps"],
    "Find Civilization": ["map", "gps", "compass"],
    "Find Shelter": ["tent", "map"],  

    # TEAM CONTACT

    "Contact Stranded Teammate": ["map", "gps", "compass"],
    "Contact Rescue Team": ["map", "gps"],
    "Alert Another Team": ["map", "gps"],


    
    # TRAVEL
    

    "Land Based Travel": ["car", "fuel", "map"],
    "Snow Based Travel": ["car", "fuel", "mountain-gear"],
    "Sand Based Travel": ["car", "fuel", "map"],
    "Water Based Travel": ["map", "gps"],
    "Air Based Travel": ["map", "gps"],
}

def generate_mission():
    """Randomly generate a mission from the available mission and
    location challenge pools."""

    # 1. Pick a random location
    location = random.choice(possible_locations)

    # 2. Find missions that can happen at this location
    viable_missions = [
        mission_name
        for mission_name, mission in mission_structures.items()
        if mission["locations"].get(location, False)
    ]

    # 3. Randomly choose one viable mission
    mission_name = random.choice(viable_missions)
    mission_definition = mission_structures[mission_name]

    # 4. Generate the 8 challenges
    challenges = []

    for challenge_type in mission_definition["challenges"]:

        possible_challenges = location_challanges[location].get(
            challenge_type, []
        )

        if not possible_challenges:
            continue

        challenge_name = random.choice(possible_challenges)
        success_items = challenge_success_items.get(challenge_name, [])

        challenges.append({
            "id": challenge_name.lower().replace(" ", "-"),
            "name": challenge_name,
            "type": challenge_type,
            "location": location,
            "description": f"Your team encounters: {challenge_name}.",
            "success_items": success_items,
            })

    return {
        "location": location,
        "name": mission_name,
        "type": mission_definition["type"],
        "challenges": challenges,
    }

def initialise_mission(session):
    """Create mission state once, retaining the auction's team inventory."""
    if not session.get("mission"):
         generated = generate_mission()
         
         session["mission"] = {
            "name": generated["name"],
            "type": generated["type"],
            "location": generated["location"],

            "challenges": generated["challenges"],

            "current_challenge_index": 0,

            "inventory": [
                dict(item)
                for item in session.get("purchased_items", [])
            ],

            "used_items": [],
            "outcome_log": [],
            "score": 100,
            "penalties": 0,
            "status": "active",
            "outcome": None,
        }
         
    return session["mission"]


def _valid_player(session, payload):
    if not isinstance(payload, dict) or not payload.get("sessionCode"):
        return None
    player_id = payload.get("playerId")
    player = session["players"].get(player_id)
    #playerId must belong to the sending socket
    if not player or player.get("socket_id") != request.sid:
        return None
    return player_id


def _state(session):
    mission = session["mission"]
    index = mission["current_challenge_index"]
    current = mission["challenges"][index] if index < len(mission["challenges"]) else None
    used = set(mission["used_items"])
    inventory = [{**item, "used": item["id"] in used} for item in mission["inventory"]]
    return {"phase": session["phase"], "missionName": mission["name"], "missionType": mission["type"], "location": mission["location"], 
            "currentChallengeIndex": index, "totalChallenges": len(mission["challenges"]), "challenge": current, 
            "inventory": inventory,
            "usedItems": list(mission["used_items"]), "outcomeLog": list(mission["outcome_log"]),
            "score": mission["score"], "penalties": mission["penalties"], "status": mission["status"], "outcome": mission["outcome"]}


def broadcast_mission_state(session_code, session):
    socketio.emit("mission_state", _state(session), room=session_code)


def emit_mission_state_to_player(session):
    if session.get("mission"):
        emit("mission_state", _state(session))


def _action_session(payload):
    code = payload.get("sessionCode") if isinstance(payload, dict) else None
    session = get_session(code)
    if not session or session.get("phase") != "mission" or not session.get("mission"):
        return None, None, None
    player = _valid_player(session, payload)
    mission = session["mission"]
    # binding actions to the rendered challenge stops delayed duplicates from changing a later challenge
    if not player or payload.get("challengeIndex") != mission["current_challenge_index"]:
        return None, None, None
    return code, session, mission


def _resolve(code, session, mission, item=None):
    challenge = mission["challenges"][mission["current_challenge_index"]]
    if item:
        mission["used_items"].append(item["id"])
        successful = item["id"] in challenge["success_items"]
        title = "Obstacle Cleared" if successful else "A Costly Detour"
        description = f"The {item['name']} gets the team past the challenge." if successful else f"The {item['name']} was not enough; the team takes a longer route."
    else:
        successful, title, description = False, "Forced to Double Back", "No item was used, so the team took the longer route."
    penalty = 0 if successful else 10
    mission["penalties"] += penalty
    mission["score"] = max(0, mission["score"] - penalty)
    outcome = {"challengeId": challenge["id"], "challengeIndex": mission["current_challenge_index"], "item": item,
        "success": successful, "penalty": penalty, "title": title, "description": description}
    mission["outcome"] = outcome
    mission["outcome_log"].append(outcome)
    mission["status"] = "resolved"
    broadcast_mission_state(code, session)
    socketio.emit("mission_outcome", outcome, room=code)


@socketio.on("mission_use_item")
def mission_use_item(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "active": return
    item_id = payload.get("itemId")
    item = next((item for item in mission["inventory"] if item["id"] == item_id), None)
    if not item or item_id in mission["used_items"]: return
    _resolve(code, session, mission, item)


@socketio.on("mission_continue")
def mission_continue(payload):
    code, session, mission = _action_session(payload)
    if session and mission["status"] == "active": _resolve(code, session, mission)


@socketio.on("mission_advance")
def mission_advance(payload):
    code, session, mission = _action_session(payload)
    if not session or mission["status"] != "resolved": return
    mission["current_challenge_index"] += 1
    mission["outcome"] = None
    if mission["current_challenge_index"] >= len(mission["challenges"]):
        mission["status"] = "complete"
        session["mission_result"] = {"score": mission["score"], "penalties": mission["penalties"], "outcomes": list(mission["outcome_log"])}
        session["phase"] = "result_page"
        broadcast_mission_state(code, session)
        socketio.emit("mission_complete", session["mission_result"], room=code)
        return
    mission["status"] = "active"
    broadcast_mission_state(code, session)