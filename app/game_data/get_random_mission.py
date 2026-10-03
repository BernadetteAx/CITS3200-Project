import random
from app.game_data.mission_structs import missions_list
from app.game_data.challenges import challenges_dict
from app.game_data.mission_descriptions import get_mission_desc
from app.game_data.location_info import possible_locations
from app.game_data.location_info import location_info


def get_mission():

    randomised_mission = {}

    # Obtain a randomised mission location
    mission_location = possible_locations[random.randint(0, len(possible_locations)-1)]
    randomised_mission["location"] = mission_location

    # Find all possible missions that can take place in that location
    mission_options = []
    for mission in missions_list:
        if mission_location in mission["location_options"]:
            mission_options.append(mission)

    # Select a random mission from that list
    selected_mission_dict = mission_options[random.randint(0, len(mission_options)-1)]
    randomised_mission["mission"] = selected_mission_dict["mission_name"]

    descriptions = get_mission_desc(mission_location, selected_mission_dict["mission_name"])
    randomised_mission["mission_description"] = descriptions[0]

    for challenge_desc_name in descriptions[1]:
        randomised_mission[challenge_desc_name] = descriptions[1][challenge_desc_name]
    
    # Choose a challenge for each of the 6 challenges in the mission
    challenge_nums = ["challenge_1", "challenge_2", "challenge_3", "challenge_4", "challenge_5", "challenge_6"]
    for challenge_num in challenge_nums:
        challenge_type = selected_mission_dict[challenge_num]

        challenge_options = []
        # Find all viable challenge options
        for challenge_name in challenges_dict[challenge_type]:
            challenge_dict = challenges_dict[challenge_type][challenge_name]
            if mission_location in challenge_dict["viable_locations"] and selected_mission_dict["mission_type"] in challenge_dict["viable_mission_types"]:
                challenge_options.append(challenge_dict)
                
        # Select a challenge
        selected_challenge_dict = challenge_options[random.randint(0, len(challenge_options)-1)]
        randomised_mission[challenge_num] = {**selected_challenge_dict, "type": challenge_type}


    # Get the weights
        weight_nums = ["w1", "w2", "w3", "w4", "w5", "w6"]
        for weight_num in weight_nums:
            randomised_mission[weight_num] = selected_mission_dict[weight_num]

    
    return randomised_mission