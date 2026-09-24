challenges_dict = {
    "Contact Teammate/s": {
        "Alert Another Team": {
            "challenge_name": "Alert Another Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Rescue Op"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small signal fire. The other team sees it and is alerted to your position. The fire starter kit is used up in the process", "used": True, "point_value": 70, "point_desc": "The signal fire gets the team's attention and gives them a clear destination to aim for. It does, however, risk attracting unwanted attention."}, 
                "Handheld Radios": {"use_desc": "You use your handheld radios to call the the other team and alert them to your position. The radio batteries are used up in the process", "used": True, "point_value": 100, "point_desc": "The radios are perfectly suited for this scenario. Both teams are able to communicate and discuss a rendezvouz point."},
                "Mirror": {"use_desc": "You use the mirror to reflect light in the direction of the other team. They see it and are able to track it back, alerting them to your position.", "used": False, "point_value": 60, "point_desc": "The mirror was able to attract the other team's attention, but it was hard to trace back to an origin and took a while for them to even notice it in the first place."},
            }, 
            "failure_items": {},
            "desc": "To be able to continue your mission you are going to need to be able to alert the other team to your position.",
            "continue_failure_desc": "Without the right equipment, your team is unable to alert the other team to your presence. You'll just have to continue the mission and hope that they will know where to rendezvouz. You do have a regular spot nearby. Let's hope they remember it. This will take a long time and slow your team down.", 
            "final_failure_desc": "Your team is unable to work out how to contact the other team. Without being able to alert them to your position, you'll never be able to rendezvouz. Your mission ends here."
        },

        "Contact Rescue Team - Survival": {
            "challenge_name": "Contact Rescue Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Handheld Radios": {"use_desc": "Using your handheld radios you are able to find an active frequency and call for help. The radio batteries are used up in the process", "used": True, "point_value": 100, "point_desc": "The radios are ideal for getting in contact."},
            }, 
            "failure_items": {},
            "desc": "You're team is going to need to get in contact with someone if they hold out any hope of being rescued.",            
            "continue_failure_desc": "Your team is unable to find a method to get in contact with a rescue team. They are instead forced to make their way to a military base some distance away and petition them for help. The journey takes a long time and a lot of energy.", 
            "final_failure_desc": "Without the needed supplies to make contact with a rescue crew, your team is forced to attempt to trek to a distant military base and hope that they can help. Your team, out of options and completely exhausted, begins the perilous journey. They will never reach their destination."
        },

        "Contact Rescue Team - Escape": {
            "challenge_name": "Contact Rescue Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Escape"],
            "items":{
                "Handheld Radios": {"use_desc": "Using your handheld radios you are able to find an active frequency and call for help. The radio batteries are used up in the process", "used": True, "point_value": 100, "point_desc": "The radios are ideal for getting in contact."},
            }, 
            "failure_items": {},
            "desc": "Your team needs to put some distance between you and your captors. You'll need to get in contact with a rescue crew if you want to get out of here.",
            "continue_failure_desc": "Your team is unable to find a method to get in contact with a rescue team. They are instead forced to make their way to a military base some distance away and petition them for help. The journey takes a long time and a lot of energy.", 
            "final_failure_desc": "Without the needed supplies to make contact with a rescue crew, your team is forced to attempt to trek to a distant military base and hope that they can help. Your team, out of options and completely exhausted, begins the perilous journey. They will never reach their destination."
        },

        "Contact Stranded Teammate": {
            "challenge_name": "Contact Stranded Teammate",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Rescue"],
            "items":{
                "Handheld Radios": {"use_desc": "You use the handheld radios to contact your lost teammate and discuss a rendezvouz point. The radio batteries are used up in the process", "used": True, "point_value": 100, "point_desc": "The radios are ideal for getting in contact."},
            }, 
            "failure_items": {},
            "desc": "To have any hope of reconnecting with your teammate, you'll need to find a way to contact them and let know where to meet you.", 
            "continue_failure_desc": "Without any way of contacting your teammate, you'll be forced to follow their tracks as best you can and attempt to intercept them. This will take a significant amount of time and energy.", 
            "final_failure_desc": "Without any way of contacting your teammate, your team is forced to attempt to follow them and hope that they can intercept them. Unfortunatlely, the time you lost earlier has put a lot of distance between you and your teammate. Your exhausted crew is unable to reach reach them until it is already too late."
        },
    },

    

    "Environmental Obstacle": {
        "Arctic Bear": {
            "challenge_name": "Arctic Bear",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas to harmlessly incapacitate the arctic bear and use the gas mask to slip by unscathed. The gas is used up in the process.", "used": True, "point_value": 70, "point_desc": "The gas worked, but took a while to knock the bear out. You were delayed because of this."},
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the arctic bear retreats.", "used": False, "point_value": 60, "point_desc": "The axes scared the bear away, but it sure wasn't a picnic for your team to be forced to get that close. Some of you came away with minor injuries."},
                "Axe": {"use_desc": "You wield the axe as a weapon. You land a hit and the bear retreats.", "used": False, "point_value": 90, "point_desc": "The axe does its job, but it sure wasn't a picnic having to get that close to the bear."},
                "Mirror": {"use_desc": "You use the glint of the mirror to distract the bear and slip by unscathed. The mirror is dropped in the escape.", "used": True, "point_value": 90, "point_desc": "The mirror was effective at getting by the bear."},
                            
            }, 
            "failure_items": {},
            "desc": "Your team stumbles across an arctic bear. It looks like it's on the hunt and your its next meal. You'll need to find a way to evade it if you want to continue your mission.", 
            "continue_failure_desc": "Your team find a tiny crevice and jump in. The bear is too large to reach you. But it sure tries. Your team is forced to wait hours in the cramped hole before the bear gives up. It has left your team, stiff, sore and well behind schedule.", 
            "final_failure_desc": "Your team, lost too much time already and can't afford to wait the bear out. You attempt to make a run for it, but exhaustion means that the bear easily catches you. Your mission ends here."
        },
        
        "Ash": {
            "challenge_name": "Ash",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "The gas mask is able to protect your team from breathing in teh ash, and the goggles allow them to see.", "used": False, "point_value": 100, "point_desc": "The gas mask is ideal for the situation. It allows your team to both breathe, and see enough to find a way out."},
            }, 
            "failure_items": {},
            "desc": "A plume of ash from the volcano fills the sky. Your team begins to choke, and can't see through it to find a way out of the ash cloud.", 
            "continue_failure_desc": "Your team, unable to see or breathe properly are forced to stay where they are and cover their faces with their clothes. It is a long time before the ash subsides and they are able to continue their mission.", 
            "final_failure_desc": "Without the right tools, your team attempts to continue on, unable to see or breathe. One after teh other, just like lemmings, your team slips down a sheer cliff, unaware it was there until it was too late. Your mission ends here."
        },

        "Blizzard": {
            "challenge_name": "Blizzard",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Snow Boots": {"use_desc": "The snow boots keep your team warm and give them good grip on teh ground. Despite barely being able to see, the team is able to make it out of the blizzard through sheer force of will.", "used": False, "point_value": 70, "point_desc": "The snow boots are effective in keeping your team warm and getting them out of the blizzard. However some time is lost as the team is unable to see where they are going."},
            }, 
            "failure_items": {},
            "desc": "The wind picks up and snow begins to fall, faster, faster. Soon enough your team is caught in a terrible blizzard. You're freezing and can't see 2ft in front of you. You'll need to get out of the storm.", 
            "continue_failure_desc": "The team, unable to think of anything else to do are forced to huddle together for warmth and wait out the storm. It takes a long, long time and your team are freezing and exhausted by the end.", 
            "final_failure_desc": "The team, unable to think of anything else to do are forced to huddle together for warmth and wait out the storm. Unfortunately, their so exhausted from their earlier trials, that it isn't long before they start to fall asleep. The sort of sleep you don't wake up from. Your mission ends here."
        },

        "Cliff": {
            "challenge_name": "Cliff",
            "viable_locations": ["Arctic Tundra", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "Your team use the ice axes to wedge into the had rock and pull themselves up. The ice axes were damaged in the process.", "used": True, "point_value": 60, "point_desc": "The ice axes were able to get your team over the cliff, but they took a lot of work to use in this kind of climbing. Beyond that, the ascent was pretty dangerous."},
                "Rope": {"use_desc": "Your team uses the rope to secure yourselves to sections of the cliff and you successfully make the ascent. Being used in this way causes the rope to fray and become unusable.", "used": True, "point_value": 80, "point_desc": "The rope is able to get your team up the cliff successfully, but is a rather dangerous approach."},
                "Grapling hook":{"use_desc": "Your team uses the grapling hook to haul yourselves up sections of the cliff.", "used": False, "point_value": 90, "point_desc": "The grapling hook is great at getting your team up the cliff, even if it is a bit unsafe."},
                "Mountain Gear": {"use_desc": "Your team uses the mountain gear to secure yourself safely to the cliff and make the ascent.", "used": True, "point_value": 100, "point_desc": "The mountain gear is designed exactly for this. It allows your team to safely and efficiently scale the cliff."},
            }, 
            "failure_items": {},
            "desc": "Your team comes across a cliff that you'll need to scale if you want to continue your mission.", 
            "continue_failure_desc": "Your team, without the proper supplies is forced to free climb. It is dangerous, exhausting and very time consuming.", 
            "final_failure_desc": "Your team is desperate and without the proper supplies is forced to free climb. Unfortunately they are exhausted from earlier and are rushing to make up time. A slip turns into a fall, and the mission ends."
        },

        "Collosal Wave": {
            "challenge_name": "Collosal Wave",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Your team don the scuba gear and go under the water. You get rocked by the wave as it passes over you, but are safe and able to continue your mission. The scuba oxygen tank is used up in the process", "used": True, "point_value": 90, "point_desc": "The scuba gear is effective at getting you out of the path of the wave. But it does mean that you are forced to wait for the wave to pass before continuing your mission."},
                "Paraglider": {"use_desc": "Your team use the paraglider to put some distance between you and the wave. Damaging winds break the paraglider, making it unusable.", "used": True, "point_value": 60, "point_desc": "The paraglider is slow and bearly gets your team out in time. It is also precarious in the damaging winds."},
                "Helicopter": {"use_desc": "Your team pile into the helicopter and take off. The damaging winds tear at the craft and damage the blades, but not before you escape the wave.", "used": True, "point_value": 80, "point_desc": "The helicopter gets you away from the wave, but in the high winds, it's a dangerous maneuver."},
                "Boat": {"use_desc": "Your team pile into the boat and outrun the wave.", "used": False, "point_value": 100, "point_desc": "The boat is ideal for this situation and helps your team escape the wave."},
            }, 
            "failure_items": {}, 
            "desc": "Vicious winds tear at your team. And then you notice something on the horizon. It is an enormous wave headed right for you. You'll need to find a way to avoid it or risk being plunged deep into the ocean.", 
            "continue_failure_desc": "Your team unable to do anything else comes together and braces for the wave. It strikes and your team is tossed around like paper dolls. But the wave passes you and your team managed to stay together. If a little worse for wear.", 
            "final_failure_desc": "Your team, without the appropraite supplies attempst to come together and brace for the wave. Unfortunately you are all too exhausted from your earlier trials that it rips you from one another and you are lost to the ocean."},
        
        "Crocodile": {
            "challenge_name": "Crocodile",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas to harmlessly incapacitate the Crocodile and use the gas mask to slip by unscathed. The gas is used up in the process", "used": True, "point_value": 80, "point_desc": "The gas did manage to subdue teh crocodile, but it took a while to take effect, so your team had to scramble into the trees while you waited."},
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the crocodile retreats.", "used": False, "point_value": 80, "point_desc": "The ice axes are unwieldy, but do their job. But it sure wasn't a picnic having to get that close to the croc."},
                "Axe": {"use_desc": "You wield the axe as a weapon. You land a hit and the crocodile retreats.", "used": False, "point_value": 90, "point_desc": "The axe does its job, but it sure wasn't a picnic having to get that close toe the croc."},
                "Mirror": {"use_desc": "You use the glint of the mirror to distract the crocodile and slip by unscathed. The mirror is dropped in the escape.", "used": True, "point_value": 90, "point_desc": "The mirror was effective at getting by the croc."},
            }, 
            "failure_items": {},
            "desc": "Your team walk beside a river. A crocodile lurches from the deep. You'll need to find a way past it.", 
            "continue_failure_desc": "Your team is forced to take to the trees and wait for the reptile to leave. It takes a long time and your team are exhausted and scratched up from clinging to the trees.", 
            "final_failure_desc": "Your team, exhausted from earlier, react too slowly. The crocodile is on you in moments. Your mission ends here."
        },
        
        "Cyclone": {
            "challenge_name": "Cyclone",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Tent": {"use_desc": "Your team pitches the tent and takes shelter. You are forced to wait out the storm. The tent is damaged in the process", "used": True, "point_value": 40, "point_desc": "The tent did provide shelter, but your team was forced to wait for the storm to subside, whilst sitting under nothing but canvas."},
            }, 
            "failure_items": {
                "Helicopter": {"use_desc": "Your team attempt to go up in the helicopter. Unfortunately the winds are too strong and the chopper is tossed about in the wind like a leaf.", "used": True, "point_value": 0, "point_desc": "The helicopter was unable to handle the winds. It crashed miles from where you were and your whole team was wiped out."},
                "Paraglider": {"use_desc": "Your team attempts to glide away using the paragliders. Unfortunately the winds are too strong and your team is tossed about in the wind like leaves.", "used": True, "point_value": 0, "point_desc": "The paragliders ripped apart in the strong winds. But that was after they got yanked up much higher into the sky then your team anticipated. It was a long way to fall."},       
            },
            "desc": "The winds pick up. On teh horizon your team can see a cyclone brewing. It won't be long before it arrives.", 
            "continue_failure_desc": "Your team shelter together as best you can and wait it out. It takes a long time for the storm to subside and your team is left exhausted.", 
            "final_failure_desc": "Unable to do anything else, your team opt to shelter together as best you can and wait it out. Unfortunately, you are all so exhausted that you begin to fall asleep. The sleep you don't wake up from. Your mission ends here."
        },

        "Cyclone - Ocean": {
            "challenge_name": "Cyclone",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Your team pile onto a boat and take off in the opposite direction, eventually rounding the cyclone and being able to continue safely on your mission.", "used": True, "point_value": 100, "point_desc": "The boat allowed you to safely escape the path of the cyclone and continue swiftly with your mission."},
                "Inflatable Raft": {"use_desc": "Your team pile onto the raft. You try to paddle but can't outrun the storm. The raft shelters your team but near the end of the cyclone gets ripped.", "used": True, "point_value": 60, "point_desc": "The raft allowed you to survive teh storm. But it was a pretty harrowing time. You definitely thought that you were done for."},
            }, 
            "failure_items": {
                "Helicopter": {"use_desc": "Your team attempt to go up in the helicopter. Unfortunately the winds are too strong and the chopper is tossed about in the wind like a leaf.", "used": True, "point_value": 0, "point_desc": "The helicopter was unable to handle the winds. It crashed miles from where you were and your whole team was wiped out."},
                "Paraglider": {"use_desc": "Your team attempts to glide away using the paragliders. Unfortunately the winds are too strong and your team is tossed about in the wind like leaves.", "used": True, "point_value": 0, "point_desc": "The paragliders ripped apart in the strong winds. But that was after they got yanked up much higher into the sky then your team anticipated. It was a long way to fall."},       
            },
            "desc": "The winds pick up. On teh horizon your team can see a cyclone brewing. It won't be long before it arrives.", 
            "continue_failure_desc": "Your team shelter together as best you can and wait it out. It takes a long time for the storm to subside and your team is left exhausted.", 
            "final_failure_desc": "Unable to do anything else, your team opt to shelter together as best you can and wait it out. Unfortunately, you are all so exhausted that you begin to fall asleep. The sleep you don't wake up from. Your mission ends here."
        },
        
        "Deadly Insects": {
            "challenge_name": "Deadly Insects",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to light a large branch on fire. Wielding the branch you are able to pass through, using the flame and smoke to keep the bugs at bay. The kindling is used up in the process", "used": True, "point_value": 90, "point_desc": "The flame is able to easily deal with the swarm of bugs and is well suited to the task. Unfortunately a couple of bugs do get past, but their bites alone are not enough to inflict significant damage."},
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas. It is too potent for the bugs to pass through. You use the gas mask to pass by unscathed. The gas is used up in the process", "used": True, "point_value": 100, "point_desc": "The gas is able to easily deal with the swarm of bugs and is well suited to the task."},
            }, 
            "failure_items": {},
            "desc": "Your team stumbles across swarm of deadly insects, all fairly intent upon biting you. You'll need to get past them to progress.", 
            "continue_failure_desc": "Your team is forced to navigate around the swarm. This takes a significant amount of time and the longer trip significantly tires your team out.", 
            "final_failure_desc": "In desperation your team attempts to make a run for it. Unfortunately they are unable to outrun the swarm and 1 bite turns into 100. They are claimed by the jungle."
        },
        
        "Deadly Marshland Gases": {
            "challenge_name": "Deadly Marshland Gases",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous marshland gases.", "used": False, "point_value": 100, "point_desc": "The gas mask is ideal for situations just like this. It was the perfect tool to help you pass safely through the marshlands."},
                "Scuba Gear": {"use_desc": "Your team uses the scuba tanks and masks to breathe safely as make your way through the marshlands. The oxygen tank is used up in the process", "used": True, "point_value": 90, "point_desc": "The scuba gear is very effective and keeps your team safe. It is however, unwieldy and gets snagged on marshland plants and vines, slowing your progress."},
            },
            "failure_items": {
                "Fire Starter Kit": {"use_desc": "You use the fire starter to create a small flame. Within an instant, your entire team is wiped out.", "used": True, "point_value": 0, "point_desc": "This is what we call a bad idea. Turns out those deadly gases were not only toxic, but also highly flammable. The ensuing fireball that consumed your team was so explosive that your first clue that anything went wrong would have been you, knocking on the pearly gates."}},
            "desc": "Your team comes across an expansive stretch of marshland that you will be forced to cross if you want to continue your mission. Unfortunately, pockets of the marshland are full of deadly gases, invisible to the human eye.", 
            "continue_failure_desc": "Your team is forced to navigate around the marshlands. This takes a significant amount of time and the longer trip significantly tires your team out.", 
            "final_failure_desc": "In desperation, your team tries to progress through the marshlands without the correct equipment. As the marshland gases slowly invade their systems, they find it harder and harder to stay awake. The exhaustion overtakes them and they rest for what they plan to only be a minute. They are claimed by the jungle."
        },

        "Earthquake": {
            "challenge_name": "Earthquake",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Helmet": {"use_desc": "Your team don helmets and take shelter. The rocks begin to fall, and there are a couple of occasions where it would have been over were it not for the hard hats. The helmets are damaged in the process", "used": True, "point_value": 65, "point_desc": "The helmets do protect your team, but don't help them avoid the danger altogether."},
            }, 
            "failure_items": {}, 
            "desc": "The earth begins to shake. It's a strong earthquake cuased by the volcano. You need to take cover or risk being hit by falling rocks.", 
            "continue_failure_desc": "Your team, unable to find another solution, tucks themselves against a rock shelf. The earthquake hits and the rocks begin to fall. Your team is protected by the shelf, but still recieve some injuries.", 
            "final_failure_desc": "Your team spots a rock shelf that you could shelter under. They start to head for it but are exhausted and only make it halfway before the quake hits. It sends rocks tumbling towards the team and burries them alive."
        },

        "Extreme Heat": {
            "challenge_name": "Extreme Heat",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "The still suit doesn't do much, but the extra layer between you and the temperature gives you enough time to get out of the patch of heat. The extreme heat damages the still suit beyond repair.", "used": True, "point_value": 70, "point_desc": "The still suit allows your team to survive the temperature, but only acts as a second layer of skin. Some of it even melts onto your skin, burning you. So you live, but it isn't pretty."},
                "Heat Resistant Suit": {"use_desc": "The heat resistant suit protects your team from the temperature and allows them to safely navigate away. It does, however, suffer dammage from loose rocks.", "used": True, "point_value": 100, "point_desc": "The heat resistant suit is ideal for this situation and allows your team to get by unscathed."},
            }, 
            "failure_items": {
                "Thermal Clothing": {"use_desc": "The extra warmth really doesn't help. Your team is wiped out.", "used": True, "point_value": 0, "point_desc": "Warm clothing? To survive extreme heat? Really? Yeah. Shockingly your whole team is roasted alive."},
            }, 
            "desc": "As the volcano stirs your team is hit by a wave of extreme heat. You'll need to find a way to protect yourself from it.", 
            "continue_failure_desc": "Your team finds a nook in the rockface and take shelter. It feels like you are being fried alive, but you do survive until the heat subsides.", 
            "final_failure_desc": "Your team, are exhausted and unable to get to safety in time. You are cooked alive."
        },

        "Fallen Trees Block Path": {
            "challenge_name": "Fallen Trees Block Path",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Axe": {"use_desc": "Your team use the axe to cut the trees into smaller pieces that they are able to lug off the path.", "used": False, "point_value": 80, "point_desc": "It takes a while, but the axe is effective at clearing the path."},
            },  
            "failure_items": {}, 
            "desc": "The path is blocked by fallen trees. You'll need to find a way past or a way to clear the trees.", 
            "continue_failure_desc": "Your team, unable to find a way get past the trees is forced to carefully climb over. You have to be very cautious as the wood is eaten away in places by termites. More than a couple of times your team almost makes a fatal error. But you get by in the end, exhuasted and behind schedule.", 
            "final_failure_desc": "Your team, unable to find a way get past the trees is forced to carefully climb over. Unfortunately, many sections of the wood have been eaten away by termites. Your team doesn't realise this until it's too late. Your team puts a foot through the thin wood and falls. Your mission ends here."
        },

        "Fire": {
            "challenge_name": "Fire",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Heat Resistant Suit": {"use_desc": "The heat resistant suit protects your team from the fire and allows them to safely navigate around the border. It does, however, suffer dammage from flames.", "used": True, "point_value": 90, "point_desc": "The heat resistant suit did allow your team to navigate around the fire safely, but your team did still suffer from smoke inhalation. Nothing that you won't recover from, mind you."},
            },  
            "failure_items": {}, 
            "desc": "Your team is bathed in orange light. A roaring fire tears it's way through the trees towards your team. You'll need to find a way around it, or a way to put it out.", 
            "continue_failure_desc": "Your team, unequipped for the task at hand is forced to flee from the fire. You finally hit a river too wide for the flames to cross and take the plunge. Your team is forced to wait for the fire to burn itself out. This delays you significantly and the run has exhausted your team.", 
            "final_failure_desc": "Your team attempts to flee the fire, but being so exhausted, can't make it to safety in time. Your team is consumed by the flames."
        },

        "Flash Flood": {
            "challenge_name": "Flash Flood",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Frozen Lake": {
            "challenge_name": "Frozen Lake",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Skates": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Heat Wave": {
            "challenge_name": "Heat Wave",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Ice Cliff": {
            "challenge_name": "Ice Cliff",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use the Ice Axes to scale the ice cliff.", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Land Slide": {
            "challenge_name": "Land Slide",
            "viable_locations": ["Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wedge the ice axes as deep into the surrounding rock as possible and hold on tight. After the landslide has past, you need to dig yourselves out, but you are otherwise fine. The ice axes are damaged in the process", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Lava Spout": {
            "challenge_name": "Lava Spout",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "Incomplete. The extreme heat damages the still suit beyond repair.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Mirages": {
            "challenge_name": "Mirages",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Nest of Scorpions": {
            "challenge_name": "Nest of Scorpions",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You toss the smoking kindling into the nest and the smoke pacifies the scorpions allowing you to pass by unscathed. The kindling is used up in the process", "used": True, "point_value": 100, "point_desc": "Incomplete"},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister into the nest, the gas causes the scorpions to scatter allowing you to pass by unscathed. The gas is used up in the process", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Quick Sand": {
            "challenge_name": "Quick Sand",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use wedge the ice axes into the surrounding solid ground and use them to pull yourselves out. The ice axes are damaged in the process", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {},
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "River": {
            "challenge_name": "River",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Rockfall": {
            "challenge_name": "Rockfall",
            "viable_locations": ["Arctic Tundra", "Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Helmet": {"use_desc": "Incomplete. The helmet is damaged in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Sand Dunes": {
            "challenge_name": "Sand Dunes",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Dune Buggy": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Sand Storm": {
            "challenge_name": "Sand Storm",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Shovel": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Shallow Reef": {
            "challenge_name": "Shallow Reef",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Shark Attack": {
            "challenge_name": "Shark Attack",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the shark retreats.", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {},
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Sinkhole": {
            "challenge_name": "Sinkhole",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Grapling Hook": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {},
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Temperature Drop": {
            "challenge_name": "Temperature Drop",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Blanket": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Underwater Earthquake": {
            "challenge_name": "Underwater Earthquake",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Incomplete. The oxygen tank is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Venemous Snake": {
            "challenge_name": "Venemous Snake",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You use the flame to keep the reptile at bay, and pass by unscathed. The kindling is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister near the snake, harmlessly incapacitating it and you use the gas mask to slip by unscathed. The gas is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Volcanic Gases": {
            "challenge_name": "Volcanic Gases",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous fumes of the volcano.", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        "Narrow Crevasse": {
            "challenge_name": "Narrow Crevasse",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Rope": {"use_desc": "You secure the rope to solid anchors and help each teammate cross the gap.", "used": False, "point_value": 100, "point_desc": "The anchored rope gives everyone a controlled crossing."},
            },
            "failure_items": {},
            "desc": "A narrow crevasse splits the trail. Your team needs a secure way across.",
            "continue_failure_desc": "Your team follows the crevasse until it narrows, losing time on the detour.",
            "final_failure_desc": "Your team cannot find a crossing before the extraction window closes."
        },

        "Loose Scree Slope": {
            "challenge_name": "Loose Scree Slope",
            "viable_locations": ["Desert", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Rope": {"use_desc": "You anchor the rope to solid rock and lower the team down the slope.", "used": False, "point_value": 100, "point_desc": "A controlled descent prevents slips and keeps the group together."},
            },
            "failure_items": {},
            "desc": "Loose stones slide beneath your feet on a steep descent. Stable rock anchors line the slope.",
            "continue_failure_desc": "Your team searches for a gentler descent and loses valuable time.",
            "final_failure_desc": "Your team cannot descend safely before the mission deadline."
        },

        "Drifting Ice Floes": {
            "challenge_name": "Drifting Ice Floes",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Boat": {"use_desc": "You navigate slowly through the open gaps and reach the opposite shore.", "used": False, "point_value": 100, "point_desc": "The boat carries everyone across without relying on unstable ice."},
            },
            "failure_items": {},
            "desc": "A sheltered channel of broken ice separates your team from the far shore. Gaps between the floes are wide enough for a small boat.",
            "continue_failure_desc": "Your team walks inland to find a crossing, adding a long detour.",
            "final_failure_desc": "The ice drifts farther apart and your team cannot reach the objective in time."
        },
    },



    "Find Shelter": {
        "Find Civilization": {
            "challenge_name": "Find Civilization",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team has been out in the open for too long. You'll need to find your way back to civilization if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Your team was unable to find their way to nearby civilization. One of your team knows of a location, but it's a long, long trek. You make it, but you entire team is exhausted and lost a lot of time.", 
            "final_failure_desc": "Unable to find any nearby signs of civilization, your team is forced to keep moving. One of your team is familiar with a location, but it's a long, long distance away. Your team attempts to make the journey, but the exhaustion and time you lost earlier has caught up with you. You never make it to your destination."
        }, 

        "Find Land": {
            "challenge_name": "Find Land",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team has been out amoung the elements for far too long. You'll need to find some land for your team to re-cooperate on, if you hold out any hope of completing your mission.", 
            "continue_failure_desc": "Without the proper equipment, your team is unable to locate any land near you and is forced to try an make it to an island a long, long way away. The trip is exhausting and takes longer than you would have hoped.", 
            "final_failure_desc": "Without the proper equipment, your team is unable to locate any land near you and is forced to try an make it to an island a long, long way away. Your crew sets off for the island they hope will be their salvation, but the exhaustion and time you lost earlier has caught up with you. You never make it to your destination.", 
        }, 

        "Find Shelter": {
            "challenge_name": "Find Shelter",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team has been out in the open too long. Exposure to the elements is starting to slow you down. You'll need to take shelter if you hold out any hope of finishing your mission.", 
            "continue_failure_desc": "Your team looses time as they search desperately for any structure to shelter them from the elements. But, without the proper equipment, there is nothing they can do. With no shelter, they are forced to continue the mission without rest.", 
            "final_failure_desc": "Your team searches desperately for any structure they could use as shelter. Unfortunately, the time they lost earlier has left them exposed to the elements for longer than any human should be forced to endure. Without the needed supplies, your team will never be able to find shelter before it's too late. It isn't long before your entire team is lost."
        },
    },



    "Find Water": {
        "Get Water - Desert": {
            "challenge_name": "Get Water",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Water Bottle": {"use_desc": "Incomplete. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Arctic Tundra": {
            "challenge_name": "Get Water",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You stumble across a frozen river. You use the ice axes to break through the thick ice and gain access to the flowing water beneath. The ice axes are damaged in the process.", "used": True, "point_value": 80, "point_desc": "The ice axes were an effective tool for overcoming this obstacle."},
                "Fire Starter Kit": {"use_desc": "You find a large chunk of ice, and using the fire starter kit to create a small fire. The small flame melts some of the ice into water. The kindling is used up in the process.", "used": True, "point_value": 70, "point_desc": "Whilst the flame was able to melt the ice, the water it produced dampened the kindling and put the fire out. So, you managed to obtain water, but not as much as you might have wanted."},
                "Mirror": {"use_desc": "You find a large chunk of ice and use the mirror to focus a beam of sunlight on it. Very slowly the ice melts into water.", "used": False, "point_value": 50, "point_desc": "The mirror did successfully help you obtain water, it took a long time and produceed barely enough water."},
            }, 
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Jungle": {
            "challenge_name": "Get Water",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Water Bottle": {"use_desc": "Incomplete. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "So much exertion has left your team severely dehydrated. You'll need to find a source of clean water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Ocean": {
            "challenge_name": "Get Water",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Water Bottle": {"use_desc": "Incomplete. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.",  
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Volcano": {
            "challenge_name": "Get Water",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Water Bottle": {"use_desc": "Incomplete. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },
    },



    "Getaway": {
        "Air Based Getaway": {
            "challenge_name": "Getaway",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Paraglider": {"use_desc": "Your team finds the highest point they can and paraglide silently away.", "used": False, "point_value": 80, "point_desc": "The paragliders quickly put some distance between you and your would be pursuors. They are particularly effective due to how silently they move, but once you reach the forested jungle, they become cumbersome and impractical. Fortunately by that point you are pretty much in the clear."},
                "Helicopter": {"use_desc": "You quickly pile into the helicopter that is standing by and take off.", "used": False, "point_value": 90, "point_desc": "The helicopter is very efficient at putting putting some distance between you and your would be pursuors. It is very loud, which alerts the guards to your presences, but fortunately you're out of there before they get the chance to follow you."},
            }, 
            "failure_items": {},
            "desc": "Your team is going to need to get away, and fast. The only way out, from your current position, is by air.", 
            "continue_failure_desc": "Your team is forced to make a run for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },
        
        "Land Based Getaway": {
            "challenge_name": "Getaway",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Armoured Truck": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is overland land.", 
            "continue_failure_desc": "Your team is forced to make a run for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Mislead Pursuers": {
            "challenge_name": "Mislead Pursuers",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape"],
            "items":{
                "Fire Starter Kit": {"use_desc": "Incomplete. The kindling is used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team isn't going to be able to outmaneuver your pursuers. Looks like you'll have to out-think them instead and lead them in the wrong direction before doubling back.", 
            "continue_failure_desc": "Without any better ideas, your team is forced to deploy the fastest of you. They make their way in the opposite direction, luring the attackers away. When they have lead them far enough away, they double back. It took a lot of time to shake them and trip tires your teammate out significantly.", 
            "final_failure_desc": "In desperation, your team deploys the fastest of you to lure your attackers away. Unfortunately sheer exhaustion has caught up with your teammate and they are unable to outrun their pursuers. It isn't long before the rest of you find yourselves in enemy hands. Your mission ends here."
        },

        "Sand Based Getaway": {
            "challenge_name": "Getaway",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Dune Buggy": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is across the dunes.", 
            "continue_failure_desc": "Your team is forced to make a run for it (or as best a run as you can manage on sand). You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Snow Based Getaway": {
            "challenge_name": "Getaway",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Snow Mobile": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is over the freshly powdered snow.", 
            "continue_failure_desc": "Your team is forced to make a run for it (or as best a run as you can whilst tumbling into snow drifts). You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Use Stealth": {
            "challenge_name": "Use Stealth",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {
                "Armoured Truck": {"use_desc": "Your team pile into the armoured truck and stop for nothing. The vehicle draws a lot of attention as it tears away. You make it about 100m before your mission ends abruptly. The armoured truck is blown up.", "used": True, "point_value": 0, "point_desc": "What about an armoured truck struck you as particularly sneaky. Didn't you hear the part where I said that you were outgunned? Well yeah, they got you. One well placed rpg and your team was no more. Let's try a subtler approach next time, huh?"},
            }, 
            "desc": "Your opponents are well equipped, your team isn't going to be able to outmaneuver or outgun them. Looks like you're going to have to perform a sneaky getaway.", 
            "continue_failure_desc": "Without any better ideas, your team is forced to camp out in a cramped storage cupboard until an opportunity presents itself to slip by undetected. It took a long time though and your team is in no way happy about it.", 
            "final_failure_desc": "Unable to wait any longer your team attempts to make a break for it when an opportunity presents itself. Unfortunatley your team is exhausted and you can't make it out of sight in time. Alarms blare, and within a moment your whole team is captured. Your mission ends here."
        },

        "Water Based Getaway": {
            "challenge_name": "Getaway",
            "viable_locations": ["Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is via the water.", 
            "continue_failure_desc": "Your team is forced to swim for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are exhausted. You manage to stay afloat, but it isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },
    },



    "Make Repairs": {
        "Repair Collapsed Wall": {
            "challenge_name": "Repair Collapsed Wall",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Volcano"],
            "viable_mission_types": ["Survival", "Rescue"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your base has sustained damage to one of the outward-facing walls. You'll need to repair it.", 
            "continue_failure_desc": "Without the proper tools to mend it, your team is forced to try and make do. You manage to scavange some old beams from another section of the base and use it to support the wall structure. It takes a long time and is a very exhausting process.", 
            "final_failure_desc": "Your team attempt to repair the wall using beams, scavanged from a closed off section of your base. Unfortunately, in their rush and exhaustion, their judgment on which beams are structural is severely lacking. It isn't long before another wall collapses, making the base unusable. Your mission ends here."
        },

        "Repair Collapsed Wall - Ocean": {
            "challenge_name": "Repair Collapsed Wall",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your base has sustained damage to one of the outward-facing walls and a whole quadrant of your base is flooded and sealed off. You'll need to repair the wall before you can even think about pumping the water out",
            "continue_failure_desc": "Without the proper tools to mend it, your team is forced to leave the section closed off. Your team is forced to constantly navigate in open ocean to access the other sections of the base. It takes a long time and is a very exhausting process.", 
            "final_failure_desc": "Your team attempt to repair the wall using beams, scavanged from a closed off section of your base. Unfortunately, in their rush and exhaustion, their judgment on which beams are structural is severely lacking. It isn't long before another wall collapses flooding the rest of the base. Your mission ends here."
        },

        "Repair Enviro-Dome": {
            "challenge_name": "Repair Enviro-Dome",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your base has sustained damage to it's enviro-dome, housing numerous samples your team has collected from their time here. You'll need to work fast, but carefully to repair it, before the samples become inmpacted.", 
            "continue_failure_desc": "Without the right eqipment there's nothing you can do. You manage to rescue the samples and some are still holding out, but years of work have been lost. It takes a long time to rehouse the remaining samples.", 
            "final_failure_desc": "Without the correct equipment, the enviro dome is beyond repair. And with the time your team lost earlier, all the samples have been destroyed. Your mission ends here."
        },

        "Repair Enviro-Dome  - Ocean": {
            "challenge_name": "Repair Enviro-Dome",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your base has sustained damage and flooding to the enviro-dome, housing numerous samples your team has collected from their time here. You'll need to perform any repairs carefully, and quickly before the samples are impacted.",
            "continue_failure_desc": "Without the right eqipment there's nothing you can do. You manage to rescue the samples and some are still holding out, but years of work have been lost. It takes a long time to rehouse the remaining samples.", 
            "final_failure_desc": "Without the correct equipment, the enviro dome is beyond repair. And with the time your team lost earlier, all the samples have been destroyed. Your mission ends here."
        },

        "Repair Exit Hatch": {
            "challenge_name": "Repair Exit Hatch",
            "viable_locations": ["Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {
                "Explosives": {"use_desc": " The explosives, well, explode in the process.", "used": True, "point_value": 0, "point_desc": "You do realise that you're stuck inside the base, right? Not your brightest idea......................................................"},
            }, 
            "desc": "In a recent rock fall, your base suffered damage to the exit hatch. It's holding together for now, but there's no telling how long it will be before the door caves and everything beyond it, will find its way in. As well as that, whilst it's broken, your team has no way out.", 
            "continue_failure_desc": "Without the right equipment all your team can do is hope that it holds. You are, however, trapped. You are forced to re-wire the rover exit hatch to gain access to the outside of the base. It takes a long time, and squeezing through the tiny gap is an arduous feat.", 
            "final_failure_desc": "Whilst the hatch held out for a long time, it can't hold out for ever. The time you lost earlier catches up with you. Your team is trapped inside the base with no exit and no time to come up with an alternate way out, when the hatch caves. Your mission ends here."
        },

        "Repair Rover": {
            "challenge_name": "Repair Rover",
            "viable_locations": ["Arctic Tundra", "Desert", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your friendly little rover 'Georgie' has suffered damage in a recent rockfall. You'll need it to be in working condition if you hope to collect any more samples before they are destroyed by changing outside conditions.", 
            "continue_failure_desc": "Unfortunately, without the proper equipment, there's nothing you can do for your little rover, 'Georgie'. Your team is forced to collect samples by hand before external conditions change and destroy the samples. It's a dangerous activity and takes a long time and a lot of effort.", 
            "final_failure_desc": "Without the rover your team will be unable to collect any more samples. You might have had time to collect more samples by hand, but your delays have caught up with you. Changing external conditions have destroyed any more samples you might have been able to retrieve, ending your mission."
        },

        "Repair Solar Panels": {
            "challenge_name": "Repair Solar Panels",
            "viable_locations": ["Desert", "Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "The solar panels that help power vital sections of your base have been knocked out of alignment. You'll need to make a few repairs and get them back in their rightful places if you want to keep getting power.", 
            "continue_failure_desc": "You manage to re-align the solar panels, but you can't do anything about the repairs. They aren't going to be able to produce much power at all. It took a lot of time and effort to re-align them without the proper tools.", 
            "final_failure_desc": "In their exhaustion, one of your teammembers makes a mistake whilst re-aligning the solar panels and they dislodge from the base and crash to the ground. Without them vital systems in your base will be unable to function, rendering the base unusable. Your mission ends here."
        },

        "Repair Vehicle": {
            "challenge_name": "Repair Vehicle",
            "viable_locations": ["Arctic Tundra", "Desert", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "There is a nearby base that your team needs to gather supplies from. Unfortunately the vehicle that your team uses to make trips has suffered damage and will need to be repaired. ", 
            "continue_failure_desc": "Without the appropriate equipment, you team is unable to repair the vehicle. You'll be forced to trek to the outposts without it. This is a time consuming process and exhausting.", 
            "final_failure_desc": "Without the appropriate equipment, you team is unable to repair the vehicle. They are too tired to make the trips without it and are forced to give up the mission."
        },

        "Split Handrail": {
            "challenge_name": "Split Handrail",
            "viable_locations": ["City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Welding Kit": {"use_desc": "You weld the damaged mounting and check the repaired handrail before crossing. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The repair restores support along the narrow walkway."},
            },
            "failure_items": {},
            "desc": "A metal handrail has split at its mounting on a narrow maintenance walkway. The walkway itself is intact.",
            "continue_failure_desc": "Your team uses a longer enclosed route while avoiding the damaged walkway.",
            "final_failure_desc": "The alternate route takes too long and your team misses the repair deadline."
        },

        "Sand Buried Access Hatch": {
            "challenge_name": "Sand Buried Access Hatch",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Shovel": {"use_desc": "You clear the sand from the hatch and expose its handle and hinges.", "used": False, "point_value": 100, "point_desc": "The shovel restores access without damaging the hatch."},
            },
            "failure_items": {},
            "desc": "Windblown sand has buried the service hatch needed to reach the repair controls.",
            "continue_failure_desc": "Your team clears the sand by hand, using extra time and energy.",
            "final_failure_desc": "Your team cannot clear the hatch before the failing system shuts down."
        },
    },


    "Manmade Obstacle": {
        "Blockade": {
            "challenge_name": "Blockade",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Building": {
            "challenge_name": "Building",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Checkpoint": {
            "challenge_name": "Checkpoint",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Collapsed Bridge": {
            "challenge_name": "Collapsed Bridge",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Rope": {"use_desc": "You use the rope and, after numerous tries, manage to lasoo the broken parapet on the far side of the bridge. After testing that it can take the weight, your team takes turns lowering themselves down the side of the bridge and swinging across.", "used": False, "point_value": 60, "point_desc": "Whilst successful, swinging across the bridge was a risky manuever and the set up cost you a lot of time."},
                "Paraglider": {"use_desc": "Your team find the highest point in the surrounding area and glide across the gap. Everyone reaches the other side safely.", "used": False, "point_value": 100, "point_desc": "The glider is well suited to this kind of challenge and your team is able to quickly and easily navigate the obstacle."},
                "Grapling Hook": {"use_desc": "The team are able to hook the grapling hook on the broken parapet on the far side of the bridge. After testing that it can take the weight, your team takes turns lowering themselves down the side of the bridge and swinging across.", "used": False, "point_value": 75, "point_desc": "Whilst swinging across the bridge was a somewhat risky manuever, the grapling hooks were efficient and ensured that the lines were well secured."},
            }, 
            "failure_items": {},
            "desc": "Your team comes across a bridge that has collapsed. You'll need to cross over it to progress.", 
            "continue_failure_desc": "Your team is forced to navigate around the collapsed bridge. This takes a significant amount of time and the longer trip significantly tires your team out.", 
            "final_failure_desc": "Your team is too tired to find an alternate route and the idea to jump across the expanse is quickly shut down. This is where your mission ends."
        },
        
        "Dam": {
            "challenge_name": "Dam",
            "viable_locations": ["Arctic Tundra", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Fortefied Structure": {
            "challenge_name": "Fortefied Structure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Giant Wall": {
            "challenge_name": "Giant Wall",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Grapling Hook": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Sea Mines": {
            "challenge_name": "Sea Mine",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
        
        "Ship Graveyard": {
            "challenge_name": "Ship Graveyard",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {},
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Traffic": {
            "challenge_name": "Traffic",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Armoured Truck": {"use_desc": "Incomplete. The truck gets damaged as you ram your way through traffic.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Locked Service Gate": {
            "challenge_name": "Locked Service Gate",
            "viable_locations": ["City", "Jungle", "Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Lock Picks": {"use_desc": "You open the padlock and guide the team through the service gate.", "used": False, "point_value": 100, "point_desc": "The lock picks open the gate quietly without damaging it."},
            },
            "failure_items": {},
            "desc": "A service gate with a simple padlock blocks a maintenance passage.",
            "continue_failure_desc": "Your team follows the perimeter to another entrance, losing time.",
            "final_failure_desc": "The facility closes its remaining entrances before your team can get inside."
        },

        "Abandoned Fishing Net": {
            "challenge_name": "Abandoned Fishing Net",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Wire Cutters": {"use_desc": "You cut away the accessible netting and clear a path for the boat.", "used": False, "point_value": 100, "point_desc": "The cutters remove the obstruction without damaging your transport."},
            },
            "failure_items": {},
            "desc": "A discarded fishing net blocks a shallow channel and threatens to snag your boat. Its edge is within reach from the deck.",
            "continue_failure_desc": "Your team reverses out of the channel and takes a longer route.",
            "final_failure_desc": "The detour leaves your team too far from the objective to arrive in time."
        },

        "Debris Filled Stairwell": {
            "challenge_name": "Debris Filled Stairwell",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Shovel": {"use_desc": "You shovel the loose rubble aside until everyone can reach the stairs.", "used": False, "point_value": 100, "point_desc": "The shovel clears the obstruction efficiently."},
            },
            "failure_items": {},
            "desc": "Loose rubble blocks the ground-floor stairwell leading to the next level. The structure is stable, but a passage must be cleared.",
            "continue_failure_desc": "Your team searches for another staircase and loses valuable time.",
            "final_failure_desc": "Your team cannot reach the upper level before access is sealed."
        },

        "Retracted Loading Walkway": {
            "challenge_name": "Retracted Loading Walkway",
            "viable_locations": ["City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Grapling Hook": {"use_desc": "You secure the grappling hook to the railing and use its line to cross the gap.", "used": False, "point_value": 100, "point_desc": "The hook provides a secure crossing point without restarting the walkway."},
            },
            "failure_items": {},
            "desc": "A loading walkway has retracted, leaving a narrow gap above a dry service platform. A sturdy railing stands on the far side.",
            "continue_failure_desc": "Your team climbs down to the service platform and takes a slow alternate route.",
            "final_failure_desc": "Your exhausted team cannot complete the alternate route before the loading area closes."
        },
    },



    "Security Obstacle": {
        "Deactivate Alarms": {
            "challenge_name": "Deactivate Alarms",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Wire Cutters": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "The area you're attempting to sneak through is rigged with numerous alarms, all set to go off at the slightest disturbance. You'll have to deactivate them before you can proceed.", 
            "continue_failure_desc": "Without the proper equipment, your team is forced to navigate through the area at a tortoise's pace to avoid triggering any of the alarms. It takes a long time and isn't easy on any of the team.", 
            "final_failure_desc": "Without the appropriate equipment, your team is unable to deactivate the alarms, so have to try and make it past without triggering any. Unfortunately, your earlier delays have put you behind schedule and you team is forced to move through the area faster than you would have liked. You make it just 20m before the first alarm is triggered. Within a moment there's a cacophany as alarms blare and guards yell. Your team is captured. Your mission ends here."
        },

        "Deactivate Security Cameras": {
            "challenge_name": "Deactivate Security Cameras",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Wire Cutters": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "The area you're attempting to sneak through is under constant video surveillance. You'll need to find a way to deactivate the security cameras if you want to get past.", 
            "continue_failure_desc": "Without the proper equipment, your is unable to deactivate the cameras. It takes a long time, but your team manages to sneak past, timing their movements with the cameras' rotations. There's a lot of planning and even more backtracking, but you make it past. It just took a long time and a lot of effort.", 
            "final_failure_desc": "Without the proper equipment, your is unable to deactivate the cameras. You try to sneak by them, attempting to time your movements with the cameras' rotations, but you're in a rush. The time you lost earlier has caught back up with you and you aren't as careful as you need to be. None of you even noticed the camera in the left hall and within moments you are swamped by guards. Your team is captured. Your mission ends here."
        },
        
        "Distract Guards": {
            "challenge_name": "Distract Guards",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small fire. The smoke attracts the attention of the guards and they leave their post to investigate. The kindling is used up in the process.", "used": True, "point_value": 75, "point_desc": "The fire successfully drew the guards away, but it did cause some significant damage in the process."},
                "Handheld Radios": {"use_desc": "You leave one of the handheld radios at your current position and move a distance away, calling it from your new position. The noise attracts the attention of the guards and they leave their post to investigate. The radios get left behind in the process.", "used": True, "point_value": 60, "point_desc": "The handheld radios successfully drew the guards away, but its presence alerted them to the fact that there was someone on the premises."},
                "Mirror": {"use_desc": "You leave the mirror at your current position and move a distance away. The glint of the mirror attracts the attention of the closest guards and they leave their post to investigate. The mirror gets left behind in the process.", "used": True, "point_value": 80, "point_desc": "The mirror successfully attracted the attention of the guards, its subtlety did not raise suspicion, but not all of the guards left their post to investigate."},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister towards the guards, knocking them out. You use the gas mask to slip past. The gas is used up in the process.", "used": True, "point_value": 60, "point_desc": "Not the cleanest of maneuvers. Whilst it did successfully incapacitate the relevant guards, there was a risk that someone would stumble across the bodies and sound the alarm."},
            }, 
            "failure_items": {},
            "desc": "Your team spots guards posted at several points around the perimeter. You are going to need to distract them to be able to slip by.", 
            "continue_failure_desc": "Without any viable tools, the team is forced to wait for the change of guard shift. They use the opportunity to slip by. Being forced to wait, unfortunately costs them hours.", 
            "final_failure_desc": "In desperation, your team attempts to slip by the guards unnoticed. Unfortunately, the exhaustion has made them sloppy. One member of the team accidently trips and the guards, hearing the noise, rush to investigate. Your team tries to run for it, but are too tired and are swiftly captured. Your mission ends here."
        },
        
        "Find Another Entrance": {
            "challenge_name": "Find Another Entrance",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team approaches the facility. Unfortunately, your planned entrance is being guarded. If you want to get in, you'll need to find another way.", 
            "continue_failure_desc": "Your team is unable to find another way in, so are forced to wait for an opportunity to sneak in through the entrance you initially planned. It takes a long, long time but eventually the guards get distracted and you are able to slip by undiscovered.", 
            "final_failure_desc": "Your team is unable to find another way in, so are forced to wait for an opportunity to sneak in through the entrance you initially planned. It takes a long, long time but eventually the guards get distracted and you attempt to slip by. Unfortunately, your exhausted crew isn't at their prime and one of you trips. Within a moment your entire team is captured. Your mission ends here."
        },

        "Find Another Exit": {
            "challenge_name": "Find Another Exit",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Escape"],
            "items":{
                "Map": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team approaches the exit to the facility. Unfortunately, it's being guarded. If you want to get out, you'll need to find another way.", 
            "continue_failure_desc": "Your team is unable to find another way out, so are forced to wait for an opportunity to sneak out through the exit you initially planned. It takes a long, long time but eventually the guards get distracted and you are able to slip by undiscovered.", 
            "final_failure_desc": "Your team is unable to find another way out, so are forced to wait for an opportunity to sneak out through the exit you initially planned. It takes a long, long time but eventually the guards get distracted and you attempt to slip by. Unfortunately, your exhausted crew isn't at their prime and one of you trips. Within a moment your entire team is captured. Your mission ends here."
        },
        
        "Get Past the Laser Grid": {
            "challenge_name": "Get Past the Laser Grid",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Mirror": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Surrounding the entire facility is a laser grid. You'll need to find a way to get past it.", 
            "continue_failure_desc": "Without the correct equipment, you team is forced to wait for a guard to pass through a checkpoint. The laser grid in the section is temporarily disabled and you have just moments to slip by. It's a mad dash, but your team makes it in time. The sprint exhausts them and waiting for a guard has significantly delayed your team's progress.", 
            "final_failure_desc": "Without the correct equipment, you team is forced to wait for a guard to pass through a checkpoint. The laser grid in the section is temporarily disabled and you have just moments to slip by. The extra energy you used earlier has finally caught up with you. Your team is not able to make it in time and get caught in the laser grid as it comes back online. Alarms blare and within moments your team is swamped by guards. You are captured. Your mission ends here."
        },
    },



    "Steal": {
        "Break into the Vault": {
            "challenge_name": "Break into the Vault",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Lock Picks": {"use_desc": "Incomplete. The lock picks get damaged in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "The item you seek is stored inside a vault. It's locked with a combination. You'll need to find a way inside if you want to retrieve the item.", 
            "continue_failure_desc": "Without the proper supplies, you team is unable to devise a way to retrieve the item. You are forced to leave empty handed and behind schedule.", 
            "final_failure_desc": "Without the proper supplies, your team can't devise a simple solution to open the vault. In their exhaustion they aren't thinking straight and resort to attempting to brute force the lock. Unfortunately the time you lost earlier means that the change of guards is occurring now. An off duty guard spots your team and sounds the alarm. In an instant your entire team is taken captive. Your mission ends here."
        },

        "Open the crate": {
            "challenge_name": "Open the crate",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Axe": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "The item you seek is stored inside a crate. You'll need to find a way to open or break the crate if you want it's contents.", 
            "continue_failure_desc": "Without the proper supplies, you team is unable to devise a way to retrieve the item. You are forced to leave empty handed and behind schedule.", 
            "final_failure_desc": "Without the proper supplies, your team can't devise a simple solution to open the crate. The delirium brought on by exhaustion and deperation caused by running late has gotten the better of team and they try to break the crate open with nothing but their bare hands. The racket quickly draws attention and it isn't long before the entire team is captured. Your mission ends here."
        },

        "Pickpocket it": {
            "challenge_name": "Pickpocket it",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "You watch as an armed guard takes the item and slips it into their pocket for safe keeping. You'll need to find a way to get it off them", 
            "continue_failure_desc": "Without the proper supplies, you team is unable to devise a way to retrieve the item. You are forced to leave empty handed and behind schedule.", 
            "final_failure_desc": "Without the proper supplies, you team is unable to devise a way to retrieve the item. Unfortunately, due to your exhaustion and the time pressure you are under, you make a decision that you would otherwise have decided against. You attempt to overpower the armed guard for it. Unfortunately your timing is off and another guard is alerted to the scuffle. In a moment your team is swarmed by guards and captured. Your mission ends here."
        },
        
        "Retrieve the Item from the Laser Grid": {
            "challenge_name": "Retrieve the Item from the Laser Grid",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Mirror": {"use_desc": "You use the mirror to reflect the lasers away as one of you reaches in and grabs the goods.", "used": False, "point_value": 100, "point_desc": "The mirror was an ingenious solution, efficient, clean, and it left the system intact, making it hard to notice that the goods have even been taken."},
                "Wire Cutters": {"use_desc": "You find the system that powers the laser grid and cut the wires. It deactivates the grid and you are able to grab the goods.", "used": False, "point_value": 80, "point_desc": "You were successful in grabbing the goods, but there was evidence of your theft and the disappearence of the item was quickly noticed."},
            }, 
            "failure_items": {},
            "desc": "You find the item, but it's protected by a laser grid. You'll need to find a way to get the item past it.", 
            "continue_failure_desc": "Without the proper supplies, you team is unable to devise a way to retrieve the item. You are forced to leave empty handed and behind schedule.", 
            "final_failure_desc": "Your team desperately tries to find a way past the lasers. Unfortunately, their exhaustion has made them sloppy, and they accidently trigger the laser system. In seconds the team is captured by armed guards. Your mission ends here."
        },

        "Open the Document Case": {
            "challenge_name": "Open the Document Case",
            "viable_locations": ["City", "Desert", "Arctic Tundra"],
            "viable_mission_types": ["Heist"],
            "items": {
                "Lock Picks": {"use_desc": "You open the case lock and retrieve the documents.", "used": False, "point_value": 100, "point_desc": "The lock picks preserve the documents and leave the case intact."},
            },
            "failure_items": {},
            "desc": "The target documents are sealed inside a portable case with a mechanical lock.",
            "continue_failure_desc": "Your team cannot open the case and retreats empty-handed after wasting time.",
            "final_failure_desc": "Security returns before your team can open the case or withdraw."
        },
    },



    "System Failure": {
        "Air Recycling System Offline": {
            "challenge_name": "Air Recycling System Offline",
            "viable_locations": ["Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, filtering the air and making it breathable.", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            }, 
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Central Heating Offline": {
            "challenge_name": "Central Heating Offline",
            "viable_locations": ["Arctic Tundra", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Blanket": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Communications System Failure": {
            "challenge_name": "Communications System Failure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Handheld Radios": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Cooling Offline": {
            "challenge_name": "Cooling Offline",
            "viable_locations": ["Desert", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Geo-Thermal Reactor Failure": {
            "challenge_name": "Geo-Thermal Reactor Failure",
            "viable_locations": ["Arctic Tundra", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },

        "Main Reactor Failure": {
            "challenge_name": "Main Reactor Failure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Incomplete. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Incomplete", 
            "continue_failure_desc": "Incomplete", 
            "final_failure_desc": "Incomplete"
        },
    },



    "Travel To Rendezvouz": {
        "Air Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Helicopter": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is using air based transport.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to make the perilous journey on foot. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt the perilous journey on foot. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team is sloppy. It isn't long before a slip up leads to catastrophe. Your team never makes it to their destination."
        },

        "Land Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Armoured Truck": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is using on-the-ground transport.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to make the perilous journey on foot. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt the perilous journey on foot. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team is sloppy. It isn't long before a slip up leads to catastrophe. Your team never makes it to their destination."
        },

        "Sand Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Dune Buggy": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is over the dunes.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to make the perilous journey on foot. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt the perilous journey on foot. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team is sloppy. It isn't long before a slip up leads to catastrophe. Your team never makes it to their destination."
        },

        "Snow Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Snow Mobile": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is over the ice and snow.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to make the perilous journey on foot. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt the perilous journey on foot. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team is sloppy. It isn't long before a slip up leads to catastrophe. Your team never makes it to their destination."
        },

        "Water Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Incomplete", "used": False, "point_value": 100, "point_desc": "Incomplete"},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is using water based transport.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to swim the distance. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt to swim the distance. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut through rough waters. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team struggles to stay afloat in teh raging waters. It isn't long before catastrophe. Your team never makes it to their destination."
        },
    },
    
    "Deactivate Bomb": {
        "Disable the Bomb Controls": {
            "challenge_name": "Disable the Bomb Controls",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist"],
            "items": {
                "Toolkit": {"use_desc": "You use the toolkit to repair the damaged safety controls and activate the bomb's shutdown sequence. The countdown stops.", "used": False, "point_value": 100, "point_desc": "The toolkit restores the safety controls, allowing your team to deactivate the device without triggering it."},
            },
            "failure_items": {},
            "desc": "Your team reaches the device, but its safety controls have been damaged. The countdown is running. You'll need suitable equipment to restore the controls and shut it down.",
            "continue_failure_desc": "Unable to deactivate the device, your team raises the alarm and helps evacuate the area. The evacuation costs valuable time, and the device remains active.",
            "final_failure_desc": "Your team cannot restore the controls before the evacuation deadline. You are forced to abandon the objective and retreat. Your mission ends here."
        },
    },

    "Destroy Information": {
        "Destroy the Stolen Records": {
            "challenge_name": "Destroy the Stolen Records",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist"],
            "items": {
                "Fire Starter Kit": {"use_desc": "You gather the stolen paper records in an empty metal disposal bin and burn them until the information is unreadable. The kindling is used up in the process.", "used": True, "point_value": 100, "point_desc": "The fire destroys the records completely, preventing the enemy from recovering your team's information."},
            },
            "failure_items": {},
            "desc": "Your team locates the enemy's only copies of your confidential records. They are stored as paper documents inside an archive room. You'll need to destroy them before the guards return.",
            "continue_failure_desc": "Without suitable equipment, your team tears up as many records as possible before retreating. Some information remains recoverable, and the effort delays your escape.",
            "final_failure_desc": "Your team spends too long trying to destroy the records by hand. The guards return and discover you inside the archive. Your mission ends here."
        },
    },

    "Deactivate Super Weapon": {
        "Shut Down the Weapon": {
            "challenge_name": "Shut Down the Weapon",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist"],
            "items": {
                "Toolkit": {"use_desc": "You use the toolkit to free the jammed emergency shutdown mechanism. The weapon powers down and its charging sequence stops.", "used": False, "point_value": 100, "point_desc": "The toolkit allows your team to activate the emergency shutdown without damaging the surrounding facility."},
            },
            "failure_items": {},
            "desc": "The enemy's super weapon is charging. Your team reaches its emergency controls, but the shutdown mechanism is jammed. You'll need suitable tools to release it.",
            "continue_failure_desc": "Unable to activate the shutdown, your team triggers an evacuation alarm to interrupt the enemy's operation. This buys time, but the weapon remains operational and your escape is delayed.",
            "final_failure_desc": "Your team cannot release the shutdown mechanism before security arrives. The control room is sealed and your team is captured. Your mission ends here."
        },
    },
} 