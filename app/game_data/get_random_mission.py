import random
from mission_structs import missions_list as missions_list
from items import items_dict as items_dict
from challenges import challenges_dict as challenges_dict

# Some locations repeated more as they have more missions available at that location
possible_locations = ["Arctic Tundra", "Arctic Tundra", "Desert", "Desert", "Jungle", "Jungle", "City", "Ocean", "Volcano"]


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
    
    # Choose a challenge for each of the 6 challenges in teh mission
    challenge_nums = ["challenge_1", "challenge_2", "challenge_3", "challenge_4", "challenge_5", "challenge_6"]
    for challenge_num in challenge_nums:
        challenge_type = selected_mission_dict[challenge_num]

        # Add rest option, that catches if there is no option found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        challenge_options = []
        # Find all viable challenge options
        for challenge_name in challenges_dict[challenge_type]:
            challenge_dict = challenges_dict[challenge_type][challenge_name]
            if mission_location in challenge_dict["viable_locations"] and selected_mission_dict["mission_type"] in challenge_dict["viable_mission_types"]:
                challenge_options.append(challenge_dict)
                
        # Select a challenge
        selected_challenge_dict = challenge_options[random.randint(0, len(challenge_options)-1)]
        randomised_mission[challenge_num] = selected_challenge_dict
        

    return randomised_mission



# mission_dict = get_mission()
# print(mission_dict["location"])
# print(mission_dict["mission"])
# print()
# print(mission_dict["challenge_1"]["challenge_name"])
# print(mission_dict["challenge_2"]["challenge_name"])
# print(mission_dict["challenge_3"]["challenge_name"])
# print(mission_dict["challenge_4"]["challenge_name"])
# print(mission_dict["challenge_5"]["challenge_name"])
# print(mission_dict["challenge_6"]["challenge_name"])