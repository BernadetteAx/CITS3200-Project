from location_info import location_info

mission_desc_struc = {
    "Train Heist": 				"<opening_sentence_location>. \n\nYou were recently contacted by an unknown employer with a job for your team. A train job.\nWhilt your employer isn't exactly forthcoming with the details, you get the basics: \n\nYour employer is interested in getting their hands on a specific piece of cargo owned by a rival. They had been planning to steal it directly from the source, but a change of plans now means that the cargo is being transported via train to a new, more secure facility. This is your employer's last chance to get their hands on the goods.\n\nIt will be a challenging mission, but your team has a reputation for such things. You'll need to boost the goods whilst the train is in motion and deliver them to your employer.\n\nLet's see if you're up to the task.",
    "Artifact Heist": 			"<opening_sentence_location>. \n\nYour team has been hired to retrieve a very important artifact. The <artifact_desc>. \n\nThe <artifact_to_steal> was recently stolen by a powerful group of individuals. It is being held inside a fortified base deep in the <location_name>. Your job is to steal it back and return it to it's proper owners. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Jewel Heist": 				"<opening_sentence_location>. \n\nYour team has been tasked to steal a very valuable jewel. The <jewel_desc>. \n\nIt's being stored in a museum, but don't get your hopes up. The <jewel_to_steal> is only being held there because the place is armed to the teeth and very well fortified, despite it's innocuous facade. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Steal Enemy Information": 	"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Escape Enemy Base": 		"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Break Out Another Team": 	"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Extract Another Team": 	"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Rescue Stranded Teammate": "<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Repair Research Base": 	"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Get Rescued": 				"<opening_sentence_location>. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.", 
}


def get_mission_desc(location, mission):

    mission_desc = mission_desc_struc[mission]
    
    # Replace location desc
    mission_desc = mission_desc.replace("<opening_sentence_location>", location_info[location]["opening_sentence_location"])
    # Replace location name
    mission_desc = mission_desc.replace("<location_name>", location.lower())
        
        
    if mission == "Artifact Heist":
        mission_desc = mission_desc.replace("<artifact_desc>", location_info[location]["artifact_desc"])
        mission_desc = mission_desc.replace("<artifact_to_steal>", location_info[location]["artifact_to_steal"])
            
    elif mission == "Jewel Heist":
        mission_desc = mission_desc.replace("<jewel_desc>", location_info[location]["jewel_desc"])
        mission_desc = mission_desc.replace("<jewel_to_steal>", location_info[location]["jewel_to_steal"])
            
            
            
            
#     mission_desc = mission_desc.replace("<>", location_info[location][""])

    return mission_desc


# print(get_mission_desc("Jungle", "Train Heist"))
# print(get_mission_desc("City", "Train Heist"))

# print(get_mission_desc("Arctic Tundra", "Artifact Heist"))
# print(get_mission_desc("Desert", "Artifact Heist"))
# print(get_mission_desc("Jungle", "Artifact Heist"))
# print(get_mission_desc("City", "Artifact Heist"))

print(get_mission_desc("Arctic Tundra", "Jewel Heist"))








