from app.game_data.location_info import location_info

mission_desc_struc = {
"Train Heist": 				"<opening_sentence_location>. \n\nYou were recently contacted by an unknown employer with a job for your team. A train job.\nWhilt your employer isn't exactly forthcoming with the details, you get the basics: \n\nYour employer is interested in getting their hands on a specific piece of cargo owned by a rival. The cargo is being transported via train to a secure facility. This is your employer's last chance to get their hands on the goods.\n\nGeeting on and off the train's going to be tough, might mean that your team will have to face more than one environmentally posed challenge. Not only that, but your team will need to handle security, steal the goods and make a daring getaway.\n\nIt will be a challenging mission, but your team has a reputation for such things. \n\nLet's see if you're up to the task.",
"Artifact Heist": 			"<opening_sentence_location>. \n\nYour team has been hired to retrieve a very important artifact. The <artifact_desc>. \n\nThe <artifact_to_steal> was recently stolen by a powerful group of individuals. It is being held inside a fortified base deep in the <location_name>. Your job is to steal it back and return it to it's proper owners. \n\nThe facility your breaking into isn't exactly easy to access. Your team can expect to come up against more than a couple of obstacles, manmade and natural. Besides that, security is tight and stealing the <artifact_to_steal>, isn't the end of it. you'll still need to make a daring getaway.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Jewel Heist": 				"<opening_sentence_location>. \n\nYour team has been tasked to steal a very valuable jewel. The <jewel_desc>. \n\nIt's being stored in a museum, but don't get your hopes up. The <jewel_to_steal> is only being held there because the place is armed to the teeth and very well fortified, despite it's innocuous facade. \n\n The museum your breaking into isn't exactly easy to access. Your team can expect to come up against more than a couple of obstacles, both environmental and manmade. And stealing the <jewel_to_steal> won't be easy either, there will be security and even if you do succeed in getting the jewel, you'll need to make a daring getaway.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Steal Enemy Information":	"<opening_sentence_location>. \n\nYour team has been recruited to steal vital enemy information in service of your government. \n\nYour team is being told as little as possible, not even what your reward is. It may be that your government doesn't exactly trust you, but with no one else up to the task, it falls to your team to complete the mission.\n\nWhat you do know is that you will need to break into a highly secure military complex located in the deepest section of the <location_name>, steal a number of files and bust back out. It'll be fine. They showed you a blueprint after all.\n\n This base is nothing to sneeze at. They have multiple layers of security and the base isn't exactly easily accessible. Even after stealing the files, you'll have to get them back safely to your government before you'll get your elusive reward.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Escape Enemy Base": 		"<opening_sentence_location>. \n\nA previous mission of yours went South. Your team wakes to find themselves locked inside a highly secure facility. Whatever they used to knock you out must have been pretty powerful, because no one on your team can recall who your captors are or how you wound up here. It's unclear what is to be done with you, but whatever it is, it can't be good.\n\nYour team will need to escape the facility, get in contact with someone who can rescue you and make a daring getaway. And from the looks of it, getting out is going to be pretty tough with multiple layers of security.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Break Out Another Team": 	"<opening_sentence_location>. \n\nYour team has been put in charge of extracting another team after a mission. You're expected to meet them at a rendezvous point and give them a ride.\n\nIt's just hours from pickup and your team hasn't heard anything from them. You're starting to worry that something went wrong. Still, you have to make it to the rendezvous in case they make it, but you get the feeling that it won't be long before this mission goes off the rails.\n\nThe team you're picking up was returning from a hesit in a secure facility. If somethings gone wrong, you'll have to trek to the facility, get past security, and get in contact with them.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Extract Another Team": 	"<opening_sentence_location>. \n\nOne of your fellow teams has gone on a research mission. They travelled to the deep into the <location_name> to collect vital research samples. A violent storm passed through the area just days earlier and you have been unable to regain contact with them since. There's no telling what has become of them. Your team is going in to find them and get them out of there.\n\n Nature won't be on your side during this mission, your team should prepare accordingly. Besides that you'll need to figure out a way to find them, and get them to safety.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Rescue Stranded Teammate": "<opening_sentence_location>. \n\nYour team has been tasked with collecting research samples deep in the <location_name>. Yesterday morning, one of your teammates went out to collect fresh samples but by afternoon the weather had changed and there was a terrible storm. You haven't heard from your teammate since and are worried that they are stranded, or worse. It won't be long before they die of exposure. \n\nYour research base was also damaged in the storm and will need to be repaired. Your team will have to repair the base, find and rescue the lost teammate and get them to safety before it's too late.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Repair Research Base": 	"<opening_sentence_location>. \n\nYour team has been tasked with collecting research samples deep in the <location_name>. Last night there was a terrible storm that did significant damage to the base. Many vital systems are offline. Your team will need to work quickly to repair the base if you hold any hope of saving the research you have done. \n\nThis mission may be close to home, but don't expect that that will make it easy. The environment is still against you and you can expect a lot to go wrong. The damage from teh storm was pretty severe. Repairs are going to be extensive.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Get Rescued": 				"<opening_sentence_location>. \n\nIn the middle of one of your routine research trips, your team finds themselves caught out in a violent storm. You manage to find shelter, but after the storm subsides you return to your base to find it completely destroyed. Without the supplies from the base your team is now racing against the clock to get rescued before exposure claims them.\n\nThis is a survival situation in every form of the word. You'll need to brave the elements, find vital resources and find a way to get rescued.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.", 
"Deactivate Bomb": "<opening_sentence_location>. \n\nYour team has received urgent intelligence about a device hidden inside an enemy facility. Its countdown has already begun, and your team is the closest group capable of reaching it in time.\n\nGetting there won't be simple. You'll need to cross hostile terrain, overcome the facility's barriers and get past security before you can reach the device. Its safety controls have been damaged, so bring equipment that can help you restore them.\n\nOnce you've dealt with the device, you'll need to escape the facility and reach the extraction point. The enemy won't be pleased to discover why you're there.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Destroy Our Team's Information": "<opening_sentence_location>. \n\nThe enemy has obtained confidential information about your team. Names, safe houses and details of your next operation are sitting inside an archive at a heavily guarded base. If those records are shared, your entire organisation could be exposed.\n\nFortunately, intelligence confirms that the stolen information exists only as paper records. Your job is to infiltrate the base and destroy those records before the enemy can make copies.\n\nExpect environmental obstacles, fortified barriers and tight security. Reaching the archive is only half the mission. You'll still need to get back through security and make a daring getaway.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Smuggle Goods": "<opening_sentence_location>. \n\nYour team has been hired to transport a sealed shipment through enemy-controlled territory. The goods are already in your possession, and your employer has been very clear about one thing: don't open the containers.\n\nA fellow team is waiting at an initial rendezvous point to help coordinate your passage. You'll need to reach them and establish contact before continuing towards the delivery point.\n\nThe route crosses difficult terrain and several controlled access points. Your team will need to overcome physical barriers and get the shipment past security without attracting unwanted attention.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Answer a Distress Signal": "<opening_sentence_location>. \n\nYour team has picked up a broken distress signal from a teammate stationed at a remote research outpost. A severe storm has damaged the station, and the people inside are running out of options.\n\nYou'll need to establish contact and travel to their position. The surrounding environment won't make the journey easy, and reaching the outpost is only the beginning.\n\nVital systems are failing and parts of the station need repairs before its occupants can leave safely. Once you've helped them, you'll need to bring everyone to the agreed extraction point.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
"Deactivate Super Weapon": "<opening_sentence_location>. \n\nIntelligence has uncovered an enemy facility housing an experimental super weapon. Its first activation is imminent, and your team has been tasked with stopping it before the charging sequence finishes.\n\nThe facility is protected by difficult terrain, physical barriers and tight security. Your team will need to get inside and reach the emergency controls. Reports suggest the shutdown mechanism is damaged, so prepare to do more than press a button.\n\nAfter dealing with the weapon, you'll need to make a fast getaway and reach your extraction team. Expect the enemy to notice your interference.\n\nIt will be a challenging mission, but your team has a reputation for such things.\n\nLet's see if you're up to the task.",
}



challenge_desc_struc = {
    "Train Heist": 				{
        "mission_start_desc":    "Your team sets off in the early hours of the morning, eager to get the heist underway. There's a point along the track where the train will need to slow down. Your team intends to board the train at that point. You set off with high hopes, but it isn't long before you hit your first obstacle.", 
        "challenge_1_to_2_desc": "Having made it past that obstacle, your team is able to make it to entry point just in the nick of time. Your team leap onto the train one after the other. Now all you've got to do is get to the cargo. Pity it's got security.", 
        "challenge_2_to_3_desc": "Having made it past security, your team makes their way to the carriage that stores the cargo. Now all you have to do, is get it.", 
        "challenge_3_to_4_desc": "You've got the goods. Your team jump from the train, landing amoungst some vegetation. It won't be long before the theft is discovered. Time to make a hasty departure.", 
        "challenge_4_to_5_desc": "You've managed to get away, but you're not home free yet.", 
        "challenge_5_to_6_desc": "Time to get the goods to your mysterious employer.", 
        "mission_complete_desc": "Your team arrive at the rendezvous. It's all a bit cloak and dagger, but you makes the switch. Your employer seems very happy about their new purchase, and your team is happy to be walking around 12 million dollars richer." 
    },
    "Artifact Heist": 			{
        "mission_start_desc":    "Your team sets off in the early hours of the morning, eager to get the heist underway. You begin the trek towards the fortified base. You set off with high hopes, but it isn't long before you hit your first obstacle.", 
        "challenge_1_to_2_desc": "Having made it past that obstacle, your team continues their journey. Unfortunately, you don't get far before the world deals you another blow.", 
        "challenge_2_to_3_desc": "Having made it past that obstacle, your team has finally reached the base. Now, all you've got to do, is get past security.", 
        "challenge_3_to_4_desc": "With security out of the way, it's time to get your hands on the goods. You find the room where the <artifact_to_steal> is being held. Now all you have to do, is get it.", 
        "challenge_4_to_5_desc": "You've got it! But, with your hands on the <artifact_to_steal>, your mission just got a lot harder. It won't be long before they realise you've taken it. Your team make a hasty exist outside. You're about to start your getaway when you hit your next obstacle.", 
        "challenge_5_to_6_desc": "Time to go! With the delay from theobstacle, your team is now fighting time. Better make a quick getaway.", 
        "mission_complete_desc": "Your team makes a clean getaway. All that's left to do is return the <artifact_to_steal> to it proper owners (and maybe pick up a handsome reward for your troubles)."            
    },
    "Jewel Heist": 				{
        "mission_start_desc":    "Your team sets off in the early hours of the morning, eager to get the heist underway. The trek to the secluded museum is a long one. It isn't long before you hit your first obstacle.", 
        "challenge_1_to_2_desc": "Having made it past that obstacle, your team continues their journey. Unfortunately, on your way to the museum you hit another roadblock.", 
        "challenge_2_to_3_desc": "Having made it past that obstacle, your team has finally reaches the museum. It's armed to the teeth and has secutity to match.", 
        "challenge_3_to_4_desc": "With security dealt with your team is able to make their way to room that stores the <jewel_to_steal>. Now all you have to do, is get it.", 
        "challenge_4_to_5_desc": "Jewel in hand your team starts to make their depature. Unfortunately, you didn't count on this.", 
        "challenge_5_to_6_desc": "Having made it past, your team is going to have to make a hasty departure if they don't want to get caught.", 
        "mission_complete_desc": "Made it! Your team, now clear of any possible pursuers is able to enjoy their victory. You admire the <jewel_to_steal> as it glimmers in the light. You are all about to be very, very rich."
    },
    "Steal Enemy Information":	{
        "mission_start_desc":    "Your team sets off in the early hours of the morning, eager to get the mission underway. The base is a fair trek, and you'll need all your energy if you're to succeed. Unfortunately, it seems that fate doesn't share your goals.", 
        "challenge_1_to_2_desc": "Having made it past that obstacle, your team continues their journey. Unfortunately, you don't get far before you hit your next roadblock.", 
        "challenge_2_to_3_desc": "Having successfully made it past, your team is able to continue their journey. A few miles later your team reaches the base. Unsurprisingly the security is going to be a challenge.", 
        "challenge_3_to_4_desc": "With security out of the way, your team is going to need to move fast. You recall the blueprints and find your way to the room that stores the files.", 
        "challenge_4_to_5_desc": "With the files safely stored, your team is going to need to get out. Unfortunately, you haven't finished with their security yet.", 
        "challenge_5_to_6_desc": "You're out, but for how long? Better put some distance between you and this base.", 
        "mission_complete_desc": "Safe at last! As your team make their way to the rendezvous point they excitedly discuss their possible reward. Jewels? Money? Cars? When you arrive, there is, what appears to be, a secret service team waiting for you. Your team is nervous as you hand over the files. But then, you receive your illusive reward. Immunity for all previous crimes. That's certainly handy."
    },
    "Escape Enemy Base": 		{
        "mission_start_desc":    "Captured! How could this happen? Well, no time to dwell, you've got to get out of here. Your whole team is ready to spring into action. Only trouble is...how are you going to get past security?", 
        "challenge_1_to_2_desc": "Past security, your team hits their next roadblock.", 
        "challenge_2_to_3_desc": "You made it, but now you realise how much trouble you're in. How on Earth did you get wrapped up in this? More security. They must really want to keep you guys where you are.", 
        "challenge_3_to_4_desc": "With security out the way there's nothing to stop you. What are you waiting for? Go!", 
        "challenge_4_to_5_desc": "Well, now your out but, kinda in the middle of nowhere. The <location_name> sure isn't a picnic. Your going to need to find someone willing to get your team out of here.", 
        "challenge_5_to_6_desc": "Alright, you've got someone whose willing to pick you up. Now all you gotta do is get to them.", 
        "mission_complete_desc": "Finally safe at last. The rescue team you called, picked you up in an army helicopter and are taking you home. Now all that still troubles you is how you eneded up captured in the first place."
    },
    "Break Out Another Team": 	{
        "mission_start_desc":    "Your team's pretty worried. The group that your fetching are pros. Despite the fact that they haven't yet made contact, you'd still better make it to the rendezvous. Just in case they make it.",       
        "challenge_1_to_2_desc": "2 hours passed the rendezvous. Something has definitely gone wrong. They were breaking into a pretty secure facility. Your team makes a unanimous decision. You're going after them. Your team sets off determined to rescue their friends, but it isn't long before you hit your first challenge.", 
        "challenge_2_to_3_desc": "You made it. Your team takes just a moment to catch their breath and then they're off again. It isn't long before you reach the facility. This might be harder than you anticipated.", 
        "challenge_3_to_4_desc": "Made it past security. Your team fan out and serach the base. You quickly come upon the building where they are being held. Your not going to be able to bust em out, but they're a crafty crew. Your team knows that they can get themselves out as long as they know there's somewhere for them to go. You'll need to find a way to get in contact with them.", 
        "challenge_4_to_5_desc": "Well, that worked. As soon as the team knew there was someone who could give them a lift they sprung into action. They take down the door and a couple of guards. Quietly too. I said they were professionals. Now all you have to deal with is more security. Seems they really didn't want these guys getting out.", 
        "challenge_5_to_6_desc": "Time to go!", 
        "mission_complete_desc": "Not exactly the extraction you were expecting, but it'll do. Out of the reach of your pursuers, both teams make their way home."
    },
    "Extract Another Team": 	{
        "mission_start_desc":    "Your team is pretty worried. The <location_name> can be pretty harsh. You'll need to get to them fast. First order of buisness, getting in contact.", 
        "challenge_1_to_2_desc": "Well, you managed to get in contact. Now you've got to meet them. Your team set out but it isn't long before your team hits an obstacle.", 
        "challenge_2_to_3_desc": "Having made it past that obstacle, your team continues their journey. You'll need to make it to the agreed rendezvous point.", 
        "challenge_3_to_4_desc": "Arrive at the rendezvous and the other team is already waiting for you. They're in bad shape. You need to get them to safety. And quick. You get the sense that something else is going to go wrong very soon.", 
        "challenge_4_to_5_desc": "You make some serious progress, but it's not long before the hit an obstacle.", 
        "challenge_5_to_6_desc": "Having made it past that obstacle, your team is exhausted. You'll need to find shelter. The wheather is turning.", 
        "mission_complete_desc": "Safe, and able to recuperate. You team takes the opportunity to catch their breath and see to their friend's injuries. Your pretty close to home. with a small push, tomorrow, both teams, will be home free."            
    },
    "Rescue Stranded Teammate": {
        "mission_start_desc":    "The storm damaged your base. If you leave now, it won't be habitable by the time you return. You'd better fix it before you go after your friend.", 
        "challenge_1_to_2_desc": "With the base repaired, your team is now able to start the search for your lost teammate. You start following their usual movements, but it isn't long before the weather turns and your forced to find shelter.", 
        "challenge_2_to_3_desc": "Your team is able to catch their breath, but can't stay too long. You're on a timer. You head back out and get a lot further before your next obstacle.", 
        "challenge_3_to_4_desc": "Having cleared that obstacle your team is able to finish following the trail. You reach the research destination and there's evidence that your teammate was here recently. Now you just need a way of getting in contact with them.", 
        "challenge_4_to_5_desc": "They're hurt, and can't get far. They'll need you to come to them.", 
        "challenge_5_to_6_desc": "You arrive at the rendezvous and find your teammate. Their in a bad way and have a broken leg. You need to get them back to your base. Once again you find yourself facing another challenge.", 
        "mission_complete_desc": "Your team make it past the obstacle, injured friend and all. It's a hike back to the base, but fortunately it seems like the world has granted you safe passage back to the base. You are all so relieved when you see the glimmer of the envirodome on the distance. Home sweet home."            
    },
    "Repair Research Base": 	{
        "mission_start_desc":    "You survived the storm, but you're not out of the woods yet. Your team needs to retrieve the satellite disc that blew off the top of your base. You start to venture after it when you hit an obstacle.", 
        "challenge_1_to_2_desc": "You get past the obstacle, retrieve the satellite disc and make your way back to the base. Alarms blare, lights flash. Everything is in disarray.", 
        "challenge_2_to_3_desc": "You fix the system. But you soon realize your next problem. The water tank has also been ripped clean from the building. Better go after it. You don't get far before your next challenge.", 
        "challenge_3_to_4_desc": "You bring the water tank back and re-attach it. But that's not all that needs fixing.", 
        "challenge_4_to_5_desc": "With just a few more repairs to be made, you notice that one of your team is missing. They went out to fix the satellite disc back to the roof but are missing. You suspect that they took shelter in a cave nearby to get out of the elements. You make your way to the cabve, but not before hitting another obstacle.", 
        "challenge_5_to_6_desc": "Your friend is there, scared and exhausted. You bring them back to the base and finish securing the satellite disc to the roof. But while you're up there you notice something else that's broken.", 
        "mission_complete_desc": "Your team manage to get the base back into working order. It will take a while for permanent replacement parts, but until then you're safe. And, you even managed to salvage your research."
    },
    "Get Rescued": 				{
        "mission_start_desc":    "Your team knows they're in a secluded location. You'll have to travel quite a distance if you have any hope of getting in contact with a rescue team. Your team sets off and it isn't long before the environment throws them a challenge.", 
        "challenge_1_to_2_desc": "Having made it past that obstacle, your team finds themselves getting thirsty.", 
        "challenge_2_to_3_desc": "Your team continues making their way towards, what they hope, is civilization.", 
        "challenge_3_to_4_desc": "The weather takes a turn. Your team will need to find shelter.", 
        "challenge_4_to_5_desc": "Your team gathers their strength. You may have shelter but you still need to make it home. You'll need to contact a team to rescue you.", 
        "challenge_5_to_6_desc": "With a team contected, now all you have to do is make it to the pickup point.", 
        "mission_complete_desc": "Safe at last. Your team makes it to the rendezvous and finds themselves being wisked away home. Won't be long now."
    },
        "Deactivate Bomb": {
        "mission_start_desc": "Your team sets off towards the enemy facility. Every minute counts, but the surrounding terrain soon puts an obstacle in your path.",
        "challenge_1_to_2_desc": "Your team continues towards the facility. Before you can reach the entrance, a physical barrier blocks your approach.",
        "challenge_2_to_3_desc": "You reach the facility's entrance. The guards haven't abandoned their posts, even with an active device inside. You'll need to get past security.",
        "challenge_3_to_4_desc": "Your team reaches the room housing the device. The countdown is still running, and its damaged safety controls are your next problem.",
        "challenge_4_to_5_desc": "There's no more time to remain inside the facility. Your team turns towards the exit as enemy personnel begin searching the area. You need to get away.",
        "challenge_5_to_6_desc": "Your team leaves the immediate search area behind. The extraction crew is waiting at the agreed rendezvous. Now you need to reach them.",
        "mission_complete_desc": "Your team reaches the extraction point and boards the waiting transport. As the facility disappears into the distance, you report the outcome of the operation to command."
    },

    "Destroy Our Team's Information": {
        "mission_start_desc": "Your team sets off towards the enemy base, determined to protect your organisation's secrets. The journey begins with an obstacle in the surrounding terrain.",
        "challenge_1_to_2_desc": "Your team continues towards the base, but its outer defences present another barrier between you and the archive.",
        "challenge_2_to_3_desc": "You reach the guarded section of the base. The records are somewhere inside, but first you'll need to get past security.",
        "challenge_3_to_4_desc": "Your team locates the archive room. Inside are the stolen paper records. This is your opportunity to destroy the information before it can be copied.",
        "challenge_4_to_5_desc": "Your time in the archive is up. Your team heads for the exit, only to find another layer of security between you and freedom.",
        "challenge_5_to_6_desc": "Your team reaches the outside of the base. It won't take long for someone to investigate the archive. You need to make your getaway.",
        "mission_complete_desc": "Your team escapes the enemy's search area and contacts headquarters. It's time to report what happened to the records and assess whether any information remains exposed."
    },

    "Smuggle Goods": {
        "mission_start_desc": "With the sealed shipment secured, your team prepares to cross enemy-controlled territory. First, you need to travel to the initial rendezvous point.",
        "challenge_1_to_2_desc": "Your team reaches the meeting area, but your contacts are keeping their distance to avoid drawing attention. You'll need to signal your position.",
        "challenge_2_to_3_desc": "The rendezvous window closes, and your team continues along the delivery route with the shipment. Before long, the environment puts an obstacle in your path.",
        "challenge_3_to_4_desc": "Your team presses on towards the delivery point. Ahead, a physical barrier blocks the route through the controlled territory.",
        "challenge_4_to_5_desc": "You approach the final controlled section of the route. Security is watching the area, and your sealed cargo would certainly raise questions.",
        "challenge_5_to_6_desc": "Your team clears the security area with the shipment. All that remains is to travel to the final rendezvous and meet the buyer.",
        "mission_complete_desc": "Your team arrives at the delivery point and hands over the sealed shipment. Your employer checks the containers and transfers your payment. Whatever was inside, it was apparently worth the trouble."
    },

    "Answer a Distress Signal": {
        "mission_start_desc": "The distress signal cuts in and out. Before your team can help, you'll need to establish contact with your stranded teammate.",
        "challenge_1_to_2_desc": "Your team gathers the available location information and prepares to move. You need to travel to the outpost's last known position.",
        "challenge_2_to_3_desc": "Your team reaches the area surrounding the outpost. You can see signs of storm damage, but an environmental obstacle stands between you and the station.",
        "challenge_3_to_4_desc": "You reach the damaged outpost and find its occupants sheltering inside. Warning indicators show that a vital system needs immediate attention.",
        "challenge_4_to_5_desc": "Your team turns to the damage elsewhere in the station. The occupants are preparing to leave, but another repair needs attention before you can move on.",
        "challenge_5_to_6_desc": "It's time to leave the outpost. Your team gathers the stranded personnel and prepares to travel to the agreed extraction point.",
        "mission_complete_desc": "Your team reaches the rendezvous with the outpost's occupants. The extraction crew takes over, giving everyone a chance to rest after the difficult journey."
    },

    "Deactivate Super Weapon": {
        "mission_start_desc": "Your team begins the approach to the weapon facility. The charging sequence has already started, but the surrounding terrain immediately slows your progress.",
        "challenge_1_to_2_desc": "Your team continues towards the facility. Its outer structures form a barrier that you'll need to overcome before reaching the guarded entrance.",
        "challenge_2_to_3_desc": "You arrive at the secure perimeter. The enemy is watching closely, and your team needs a way past security.",
        "challenge_3_to_4_desc": "Your team reaches the weapon's control area. The emergency shutdown mechanism is jammed, and the charging indicators are climbing. This is the moment you came for.",
        "challenge_4_to_5_desc": "Enemy personnel are converging on the control area. Whatever the outcome at the controls, your team needs to leave immediately.",
        "challenge_5_to_6_desc": "Your team moves beyond the facility's immediate defences. The extraction crew won't wait forever. You need to reach the rendezvous.",
        "mission_complete_desc": "Your team reaches the extraction crew and leaves the facility behind. Command is waiting for your report on the weapon's status and the outcome of the operation."
    },
}


def get_mission_desc(location, mission):

    mission_desc = mission_desc_struc[mission]
    
    location_name = location.lower()
    item = ""
    item_desc = ""
        
    if mission == "Artifact Heist":
        item = location_info[location]["artifact_to_steal"]
        item_desc = location_info[location]["artifact_desc"]
        
    elif mission == "Jewel Heist":
        item = location_info[location]["jewel_to_steal"]
        item_desc = location_info[location]["jewel_desc"]


    # Replace location desc
    mission_desc = mission_desc.replace("<opening_sentence_location>", location_info[location]["opening_sentence_location"])
    # Replace location name
    mission_desc = mission_desc.replace("<location_name>", location_name)

    # If you are stealing an item, replace the item you are stealing
    mission_desc = mission_desc.replace("<artifact_to_steal>", item)
    mission_desc = mission_desc.replace("<jewel_to_steal>", item)
    # If you are stealing an item, replace the desc of the item you are stealing
    mission_desc = mission_desc.replace("<artifact_desc>", item_desc)
    mission_desc = mission_desc.replace("<jewel_desc>", item_desc)

    # Get the descs that occur between challenges
    challenge_descs = challenge_desc_struc[mission].copy()
    for challenge_desc_name in challenge_descs:
        challenge_descs[challenge_desc_name] = challenge_descs[challenge_desc_name].replace("<location_name>", location_name)
        challenge_descs[challenge_desc_name] = challenge_descs[challenge_desc_name].replace("<artifact_to_steal>", item)
        challenge_descs[challenge_desc_name] = challenge_descs[challenge_desc_name].replace("<jewel_to_steal>", item)
        challenge_descs[challenge_desc_name] = challenge_descs[challenge_desc_name].replace("<artifact_desc>", item_desc)
        challenge_descs[challenge_desc_name] = challenge_descs[challenge_desc_name].replace("<jewel_desc>", item_desc)


    return mission_desc, challenge_descs