from location_info import location_info

mission_desc_struc = {
    "Train Heist": 				"<opening_sentence_location>. \n\nYou were recently contacted by an unknown employer with a job for your team. A train job.\nWhilt your employer isn't exactly forthcoming with the details, you get the basics: \n\nYour employer is interested in getting their hands on a specific piece of cargo owned by a rival. They had been planning to steal it directly from the source, but a change of plans now means that the cargo is being transported via train to a new, more secure facility. This is your employer's last chance to get their hands on the goods.\n\nIt will be a challenging mission, but your team has a reputation for such things. You'll need to boost the goods whilst the train is in motion and deliver them to your employer.\n\nLet's see if you're up to the task.",
    "Artifact Heist": 			"<opening_sentence_location>. \n\nYour team has been hired to retrieve a very important artifact. The <artifact_desc>. \n\nThe <artifact_to_steal> was recently stolen by a powerful group of individuals. It is being held inside a fortified base deep in the <location_name>. Your job is to steal it back and return it to it's proper owners. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Jewel Heist": 				"<opening_sentence_location>. \n\nYour team has been tasked to steal a very valuable jewel. The <jewel_desc>. \n\nIt's being stored in a museum, but don't get your hopes up. The <jewel_to_steal> is only being held there because the place is armed to the teeth and very well fortified, despite it's innocuous facade. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Steal Enemy Information":	"<opening_sentence_location>. \n\nYour team has been recruited to steal vital enemy information in service of your government. \n\nYour team is being told as little as possible. It may be that your government doesn't exactly trust you, but with no one else up to the task, it falls to your team to complete the mission.\n\nWhat you do know is that you will need to break into a highly secure military complex located in the deepest section of the <location_name>, steal a number of files and bust back out.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Escape Enemy Base": 		"<opening_sentence_location>. \n\nA previous mission of yours went South. Your team wakes to find themselves locked inside a highly secure facility. Whatever they used to knock you out must have been pretty powerful, because no one on your team can recall who your captors are or how you wound up here. It's unclear what is to be done with you, but whatever it is, it can't be good.\n\nYour team will need to escape the facility, get in contact with someone who can rescue you and make a daring getaway.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Break Out Another Team": 	"<opening_sentence_location>. \n\nYour team has been put in charge of extracting another team after a mission. You're expected to meet them at a rendezvous point and give them a ride.\n\nIt's just hours from pickup and your team hasn't heard anything from them. You're starting to worry that something went wrong. Still, you have to make it to the rendezvous in case they make it, but you get the feeling that it won't be long before this mission goes off the rails.\n\nLet's see if you're up to the task.",
    "Extract Another Team": 	"<opening_sentence_location>. \n\nOne of your fellow teams has gone on a research mission. They travelled to the deep into the <location_name> to collect vital research samples. A violent storm passed through the area just days earlier and you have been unable to regain contact with them since. There's no telling what has become of them. Your team is going in to find them and get them out of there.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Rescue Stranded Teammate": "<opening_sentence_location>. \n\nYour team has been tasked with collecting research samples deep in the <location_name>. Yesterday morning, one of your teammates went out to collect fresh samples but by afternoon the weather had changed and there was a terrible storm. You haven't heard from your teammate since and are worried that they are stranded, or worse. It won't be long before they die of exposure. \n\nYour research base was also damaged in the storm and will need to be repaired. Your team will have to repair the base and rescue the lost teammate before it's too late.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Repair Research Base": 	"<opening_sentence_location>. \n\nYour team has been tasked with collecting research samples deep in the <location_name>. Last night there was a terrible storm that did significant damage to the base. Many vital systems are offline. Your team will need to work quickly to repair the base if you hold any hope of saving the research you have done. \n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
    "Get Rescued": 				"<opening_sentence_location>. \n\nIn the middle of one of your routine research trips, your team finds themselves caught out in a violent storm. You manage to find shelter, but after the storm subsides you return to your base to find it completely destroyed. Without the supplies from the base your team is now racing against the clock to get rescued before exposure claims them.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.", 
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

    return mission_desc

