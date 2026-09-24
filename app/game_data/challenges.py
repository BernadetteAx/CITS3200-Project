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
                "Gas Mask and Knockout Gas": {"use_desc": "The gas mask is able to protect your team from breathing in the ash, and the goggles allow them to see.", "used": False, "point_value": 100, "point_desc": "The gas mask is ideal for the situation. It allows your team to both breathe, and see enough to find a way out."},
            }, 
            "failure_items": {},
            "desc": "A plume of ash from the volcano fills the sky. Your team begins to choke, and can't see through it to find a way out of the ash cloud.", 
            "continue_failure_desc": "Your team, unable to see or breathe properly are forced to stay where they are and cover their faces with their clothes. It is a long time before the ash subsides and they are able to continue their mission.", 
            "final_failure_desc": "Without the right tools, your team attempts to continue on, unable to see or breathe. One after the other, just like lemmings, your team slips down a sheer cliff, unaware it was there until it was too late. Your mission ends here."
        },

        "Blizzard": {
            "challenge_name": "Blizzard",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Snow Boots": {"use_desc": "The snow boots keep your team warm and give them good grip on the ground. Despite barely being able to see, the team is able to make it out of the blizzard through sheer force of will.", "used": False, "point_value": 70, "point_desc": "The snow boots are effective in keeping your team warm and getting them out of the blizzard. However some time is lost as the team is unable to see where they are going."},
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
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas to harmlessly incapacitate the Crocodile and use the gas mask to slip by unscathed. The gas is used up in the process", "used": True, "point_value": 80, "point_desc": "The gas did manage to subdue the crocodile, but it took a while to take effect, so your team had to scramble into the trees while you waited."},
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
            "desc": "The winds pick up. On the horizon your team can see a cyclone brewing. It won't be long before it arrives.", 
            "continue_failure_desc": "Your team shelter together as best you can and wait it out. It takes a long time for the storm to subside and your team is left exhausted.", 
            "final_failure_desc": "Unable to do anything else, your team opt to shelter together as best you can and wait it out. Unfortunately, you are all so exhausted that you begin to fall asleep. The sleep you don't wake up from. Your mission ends here."
        },

        "Cyclone - Ocean": {
            "challenge_name": "Cyclone",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Your team pile onto a boat and take off in the opposite direction, eventually rounding the cyclone and being able to continue safely on your mission.", "used": True, "point_value": 100, "point_desc": "The boat allowed you to safely escape the path of the cyclone and continue swiftly with your mission."},
                "Inflatable Raft": {"use_desc": "Your team pile onto the raft. You try to paddle but can't outrun the storm. The raft shelters your team but near the end of the cyclone gets ripped.", "used": True, "point_value": 60, "point_desc": "The raft allowed you to survive the storm. But it was a pretty harrowing time. You definitely thought that you were done for."},
            }, 
            "failure_items": {
                "Helicopter": {"use_desc": "Your team attempt to go up in the helicopter. Unfortunately the winds are too strong and the chopper is tossed about in the wind like a leaf.", "used": True, "point_value": 0, "point_desc": "The helicopter was unable to handle the winds. It crashed miles from where you were and your whole team was wiped out."},
                "Paraglider": {"use_desc": "Your team attempts to glide away using the paragliders. Unfortunately the winds are too strong and your team is tossed about in the wind like leaves.", "used": True, "point_value": 0, "point_desc": "The paragliders ripped apart in the strong winds. But that was after they got yanked up much higher into the sky then your team anticipated. It was a long way to fall."},       
            },
            "desc": "The winds pick up. On the horizon your team can see a cyclone brewing. It won't be long before it arrives.", 
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
                "Boat": {"use_desc": "Your team pile into the boat. As soon as the waters are high enough, the boat is able to navigate on top.", "used": False, "point_value": 100, "point_desc": "The boat is ideal for handling the flooding."},
            },  
            "failure_items": {}, 
            "desc": "A torrential downpour begins. Your team recognises the conditions. It won't be long before a flood follows.", 
            "continue_failure_desc": "Your team, unabel to get to safety, are forced to climb trees and hope they don't get swpet away with the current. It is exhausting, but your team manages to cling on through the ragin waters. When the flood subsides, your team is exhausted and has lost a lot of time.", 
            "final_failure_desc": "Your team, unabel to get to safety, are forced to climb trees and hope they don't get swpet away with the current. Unfortunately, they are exhausted from their earlier trials, and when the first wave hits, they are wrenched from the trees and scattered. You can't outswim that kind of water. Your team drowns."
        },

        "Frozen Lake": {
            "challenge_name": "Frozen Lake",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Skates": {"use_desc": "The team don the ice skates and use them to easily navigate over the forzen lake.", "used": False, "point_value": 100, "point_desc": "The ice skates are idel for navigating over the lake and your team is able to move quickly to their next challenge."},
            },  
            "failure_items": {}, 
            "desc": "A frozen lake seperates your from your destination. You'll need to cross it, but be careful. The ice can be thin in places.", 
            "continue_failure_desc": "Without the appropriate eqipment, your team is forced to navigate the river on foot. It's slow and there is a lot of slipping involved. But your team is able to carefully avoid the thin ice and make it to the other side.", 
            "final_failure_desc": "Without the appropriate eqipment, your team is forced to navigate the river on foot. It's slow and there is a lot of slipping involved. The time you lost earlier is weighing on your team and they try to move fast. Unfortunately, it means that they miss the patch of thin ice. It cracks and they are plunged into the icy depths. Perhaps if they were less tired they could have pulled themselves out. We'll never know. They are claimed by the frozen waters."
        },

        "Heat Wave": {
            "challenge_name": "Heat Wave",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "The still suit recycles the water from your team's bodies. It keeps you cool and hydrated and allows your team to continue without hinderance.", "used": False, "point_value": 100, "point_desc": "The still-suit is ideal for handling a heatwave."},
            },  
            "failure_items": {}, 
            "desc": "The desert heat has finally caught up to your team. You'll need to find a way to combat the heat if you wish to continue your mission.", 
            "continue_failure_desc": "Without any supplies, the team is forced to wait for the midday heat to subside before they continue. Your team loses a lot of time and are feeling very tired by the time the heta disipates.", 
            "final_failure_desc": "Without any supplies, the team is forced to wait for the midday heat to subside before they continue. Unfortunately, they are exhausted and can barely stay awake. It isn't long before they fall asleep one by one. The kind of sleep you don't wake up from. The mission ends here."
        },

        "Ice Cliff": {
            "challenge_name": "Ice Cliff",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use the Ice Axes to scale the ice cliff with ease.", "used": False, "point_value": 100, "point_desc": "The ice axes are ideal for this kind of challenge as they are able to easily get a hold on the smooth surface."},
            }, 
            "failure_items": {}, 
            "desc": "Your team comes across an ice cliff that you'll need to scale if you want to continue your mission.", 
            "continue_failure_desc": "Your team, without the proper supplies is forced to free climb. It is dangerous, exhausting and very time consuming.", 
            "final_failure_desc": "Your team is desperate and without the proper supplies is forced to free climb. Unfortunately they are exhausted from earlier and are rushing to make up time. A slip turns into a fall, and the mission ends."
        },
        
        "Land Slide": {
            "challenge_name": "Land Slide",
            "viable_locations": ["Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wedge the ice axes as deep into the surrounding rock as possible and hold on tight. After the landslide has past, you need to dig yourselves out, but you are otherwise fine. The ice axes are damaged in the process", "used": True, "point_value": 70, "point_desc": "The ice axes helped your team get a grip and keep together, but your team was still caught in the slide."},
            }, 
            "failure_items": {}, 
            "desc": "Your team finds themselves next to a steep slope when a minor earthquake shifts the ground. The earthquake triggers a landslide. You'll need to outrun it or withstand it.", 
            "continue_failure_desc": "Your team are forced to try to outrun the slide. You get pretty far, but it eventually catches up to you. Your team is burried. You manage to dig yourselves out, but it takes a long time and is exhausting.", 
            "final_failure_desc": "Your team is forced to try to outrun the slide. Unfortunately, they are exhausted and don't get far before it catches them. The team is burried and unable to dig themselves out. Your mission ends here."
        },
        
        "Lava Spout": {
            "challenge_name": "Lava Spout",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Heat Resistant Suit": {"use_desc": "You don the heat resistant suits and are able to safely navigate areound the lava spout. It may be good, but even the heat resistant suit can barely hold it's own against lava. The extreme heat damages the heat-resistant suit beyond repair.", "used": True, "point_value": 90, "point_desc": "The heat resistant suit allowed your team to navigate around the lava spout, though it was a bit precarious being so close to the lava."},
            },  
            "failure_items": {}, 
            "desc": "A lava spout erupts from the earth and blocks your path. You'll need to find a way past it.", 
            "continue_failure_desc": "Unable to find a way past, your team is forced to wait for the spout to stop and the lava to cool. A long, long time later you are able to continue on your mission.", 
            "final_failure_desc": "Your team has lost too much time already and can't wait for the spout to stop. Your team try to make their way past, but a misplaced step sends a rocks flying. They crash into the surrounding ground allowing for more lava spouts to form, right on top of you. At least it's quick."
        },

        "Mirages": {
            "challenge_name": "Mirages",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Your team is able to use the few landmarks nearby to orient themselves. With a better idea of where they are going, the team is able to continue the mission.", "used": False, "point_value": 100, "point_desc": "The map is ideal for finding your way through the desert."},
                "Compass": {"use_desc": "your team use the compass to orient themselves. With a better idea of where they are, the team is able to continue the mission.", "used": False, "point_value": 100, "point_desc": "The compass is ideal for getting your team headed in the right direction."},              
            },  
            "failure_items": {}, 
            "desc": "Your team is trying to progress, but keeps getting truned around by mirages cause by the desert heat. You'll need to find a way to know where your going.", 
            "continue_failure_desc": "Unable to find your way, your team is forced to wait for the heat of the day to subside. It takes a long, long time and your team is exhausted from waiting out in the heat.", 
            "final_failure_desc": "Your team has lost too much time to wait for th eheat of the day to subside. They decide to trust their guts. They travel deep into the desert, but in the wrong direction. It isn't long before they are claimed by the desert heat."
        },
        
        "Nest of Scorpions": {
            "challenge_name": "Nest of Scorpions",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You toss the smoking kindling into the nest and the smoke pacifies the scorpions allowing you to pass by unscathed. The kindling is used up in the process", "used": True, "point_value": 100, "point_desc": "The firestarter kit is effective at dealing with the scorpions and didn't require any animals to be hurt in the process."},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister into the nest, the gas causes the scorpions to scatter allowing you to pass by unscathed. The gas is used up in the process", "used": True, "point_value": 100, "point_desc": "The gas is effective at dealing with the scorpions and didn't require any animals to be hurt in the process."},
            }, 
            "failure_items": {}, 
            "desc": "Your team stumbles across a nest of scorpions blocking your path. You'll need to get by them to continue your mission.", 
            "continue_failure_desc": "Your team is forced to take the long way around. And let me tell you. It's a long, long way. By the time your team reach their destination they are exhausted and well behind schedule.", 
            "final_failure_desc": "Your team doesn't have the time nor the stamina to go the long way around. Your team is forced to try and pass through the nest. Unfortunately your exhaustion makes you sloppy, and you step on one of the little guys. In seconds the scorpions turn on the team and sting them. It's a painful way to go."
        },
        
        "Quick Sand": {
            "challenge_name": "Quick Sand",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use wedge the ice axes into the surrounding solid ground and use them to pull yourselves out. The ice axes are damaged in the process", "used": True, "point_value": 90, "point_desc": "The ice axes are able to help your team haul themselves out of th epit, though it takes a lot of effort."},
            }, 
            "failure_items": {},
            "desc": "Your team is travelling when suddenly the earth seems to rise up around them. Or more accurately, they start to sink. It's quicksand. You'll need to find a way to pull yourselves out.", 
            "continue_failure_desc": "One of your crew remembers what to do and your team lay on their backs. Who knew that boyancy still worked on sand. You stop sinking but it is a long and scary process to make your way to the edge of the pit to pull yourselves out. It takes a long time and exhausts your team.", 
            "final_failure_desc": "Your team panics. Without the right tools they don't know what to do. Their floundering is making them sink faster and they are too exhausted to find another way out. The team is claimed by the earth."
        },
        
        "River": {
            "challenge_name": "River",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Boat": {"use_desc": "Your team pile into the boat, and just moments later you are safely on the other bank fo the river.", "used": False, "point_value": 100, "point_desc": "The boat is ideal for crossing the river."},
            },  
            "failure_items": {}, 
            "desc": "A raging river stands between your team and their destination. You'll have to cross it if you want to continue your mission.", 
            "continue_failure_desc": "Without any better ideas, you team decides to try to swim for it. The current is strong an they get washed way downstream. Fortunately your team has the strength to pull themselves across the river, though it is exhausting. Your team has to trek back up river, costing you time.", 
            "final_failure_desc": "Without any better ideas, you team decides to try to swim for it. The waters are strong and drag the team downstream. Unfortunately, they are too tired to beat the current and never make it to the far bank. Your mission ends here."
        },

        "Rockfall": {
            "challenge_name": "Rockfall",
            "viable_locations": ["Arctic Tundra", "Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Helmet": {"use_desc": "Your team don helmets. When to rocks hit your team only suffers minor injuries. The helmets are damaged in the process.", "used": True, "point_value": 40, "point_desc": "The helmets meant that your team survived the rocks, but it still left the rest of your bodies exposed. Your team still suffered damage from the fall."},
            },  
            "failure_items": {}, 
            "desc": "Your team finds themselves next to a steep slope. There's a crash and you team looks up to find that some rocks have come loose and are headed your way.", 
            "continue_failure_desc": "Without any bright ideas, your team dives out the way. Unfortunately some of you get knocked unconscious by the rocks. Your team is forced to wait for them to recover before continuing the mission. You have to wait a long time, and even when they come to, they aren't in great shape.", 
            "final_failure_desc": "Your team is exhausted and slow to react. The rocks bear down upon them and they don't get out of the way in time. The rocks smash into them and the team is wiped out."
        },

        "Sand Dunes": {
            "challenge_name": "Sand Dunes",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Dune Buggy": {"use_desc": "Your team pile into the dune buggy and tear off. It makes quick work of the dunes and your team is able to continue their mission.", "used": False, "point_value": 100, "point_desc": "The dune buggy is ideal for traversing sand dunes."},
            },  
            "failure_items": {}, 
            "desc": "Your team finds themselves facing an expanse of desert with particularly steep, and seemingly endless, sand dunes. You'll need to traverse them to continue your mission.", 
            "continue_failure_desc": "With no bright ideas, your team is forced to traverse the sand dunes on foot. It is exhausting and time consuming.", 
            "final_failure_desc": "Your team attempts to traverse the dunes on foot. Unfortunately, they're too tired to get far. The team pauses to rest, for what was only meant to be 5 minutes. They never wake up."
        },

        "Sand Storm": {
            "challenge_name": "Sand Storm",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Shovel": {"use_desc": "Your team dig down and make a shallow pit to hide in. The winds swirl above you, but you're safe until the storm passes.", "used": False, "point_value": 40, "point_desc": "The shovel helped you keep your team safe, but it did mean that you had to wait for the storm to subside."},
            },  
            "failure_items": {}, 
            "desc": "The wind picks up and begins to stir the sands into the air. In a matter of minutes the world around you is plunged into darkness as sand swirls around you. You'll need to find a way out if you have any hope of coontinuing your mission.", 
            "continue_failure_desc": "With no other equipment, your team huddles together and waits out the storm. It is a time consuming and taxing ordeal.", 
            "final_failure_desc": "With no time to spare your team attempts to continue their mission despite the storm. In seconds the team is scattered by the strong winds. You call to one another, but nothing is heard over the howling wind. Your mission ends here."
        },

        "Shallow Reef": {
            "challenge_name": "Shallow Reef",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "The team don the scuba gear and go underwater. Your team is able to easily maneuver around the coral and even seem some cool fish.", "used": False, "point_value": 100, "point_desc": "The scuba gear is ideal for navigating easily in underwater spaces."},
            },  
            "failure_items": {
                "Boat": {"use_desc": "Your team pile into the boat and attempt to navigate it through the reef. Unfortunately a wave rocks the boat onto a bed of coral and it crashes. Fuel begins to leak. Then there's a spark. The boat goes up in flames. And your crew too.", "used": True, "point_value": 0, "point_desc": "The boat simply wasn't the right choice."},
            }, 
            "desc": "Your team needs to cross a shallow reef to continue the mission. But be careful, this reef has claimed many a ship.", 
            "continue_failure_desc": "Your team are forced to try and swim across the reef. It takes a long time and the crew recieves more than a few cuts and scrapes as they are kncoked against the reef.", 
            "final_failure_desc": "Your team are forced to try and swim across the reef. Unfortunately, the time and energy the team lost earlier have cuaght up with you. The team is unable to stay afloat and are claimed by the ocean. Your mission ends here."
        },

        "Shark Attack": {
            "challenge_name": "Shark Attack",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the shark retreats.", "used": False, "point_value": 70, "point_desc": "The ice axes do successfully repel the shark, but it does add some blood to the water. Who knows if more sharks are coming."},
            }, 
            "failure_items": {},
            "desc": "Your team are travelling when you come under attack by a shark. You'll need to fend him off or outrun him if you have any hope of continuing the mission.", 
            "continue_failure_desc": "Without any better ideas, you team comes together. You try to look like 1 very big animal to scare the shark off. It takes a long time and the shark tries to attack you a couple of times but eventually it gives up and leave you alone. You're team is exhausted and lost a lot of time.", 
            "final_failure_desc": "Your team are exhausted and scatter as the shark approaches. Without any coordination, it isn't long before you are picked off one, by one. Your mission ends here."
        },

        "Sinkhole": {
            "challenge_name": "Sinkhole",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Grapling Hook": {"use_desc": "In the few moments you have, your team manages to latch the grapling hook to the far side of the hole. When the ground gives way, your team is able to swing to safety.", "used": False, "point_value": 90, "point_desc": "The grapling hook handly passes the challenge, and apart from a few minor cuts, your team comes away unscathed."},
            }, 
            "failure_items": {},
            "desc": "Your team is travelling along when suddenly the ground seems to open. A sinkhole has just appeared and your team is falling into it.", 
            "continue_failure_desc": "Without the right tools your team manages to scramble to the edge of the hole and haul themselves out. It is an exhausting process and your team is forced to take time to recover.", 
            "final_failure_desc": "Your team is exhausted and reacts slowly. They fall into the sinkhole and those who survive the fall, can find no way out. Your mission ends here."
        },

        "Temperature Drop": {
            "challenge_name": "Temperature Drop",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Blanket": {"use_desc": "Your team huddle under the blanket for warmth and wait for the temperature to climb once more.", "used": False, "point_value": 70, "point_desc": "The team is able to survive the tempertaure drop, but is unable to go anywhere until the climate improved."},
                "Thermal Clothing": {"use_desc": "Your team don the thermal clothing and are able to continue their mission unhindered.", "used": False, "point_value": 100, "point_desc": "Thermal clothing is ideal for this time of climate related problem."},
                "Snow Boots": {"use_desc": "Your team wear the snow boots, which keeps their toes warm at the least. It does little to keep the rest of your bodies warm. Fortunately your team is able to find their way out of the cold patch and continue the mission.", "used": True, "point_value": 40, "point_desc": "The snow boots are barely enough, but do allow your team to exit the cold patch."},    
            },  
            "failure_items": {}, 
            "desc": "There is a sudden drop in temperature and your team is caught out in it. You'll need to find a way to withstand the cold if you want to continue your mission.", 
            "continue_failure_desc": "With nothing to keep them warm, your team is forced to huddle together and wait for the climate to return to normal. It takes a long time and leaves your team exhausted.", 
            "final_failure_desc": "With nothing to keep them warm, your team is forced to huddle together and wait for the climate to return to normal. It takes longer than you can spare. Your team is already exhausted and very soon, they are frozen. Your mission ends here."
        },
        
        "Venemous Snake": {
            "challenge_name": "Venemous Snake",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You use the flame to keep the reptile at bay, and pass by unscathed. The kindling is used up in the process.", "used": True, "point_value": 100, "point_desc": "The fire is very effective at keeping the snake at bay. And it didn't require any injuries to wildlife."},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister near the snake, harmlessly incapacitating it and you use the gas mask to slip by unscathed. The gas is used up in the process.", "used": True, "point_value": 100, "point_desc": "The gas is great at handling the snake. And it didn't require any injuries to wildlife."},
            }, 
            "failure_items": {}, 
            "desc": "A venemous snake blocks the path. Your team will need to evade it if you want to continue your mission.", 
            "continue_failure_desc": "Your team are forced to double back and go the long, long way round, costing significant time and energy.", 
            "final_failure_desc": "Your team don't have time to double back and attempt to slip by the snake. Unfortunately one of you gets too close and it strikes. There's a panic and within moments the entire team has the snake's venom coursing through them. Even after yu kill the snake there is nothing your team can do. Your mission ends here."
        },
        
        "Volcanic Gases": {
            "challenge_name": "Volcanic Gases",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous fumes of the volcano.", "used": False, "point_value": 100, "point_desc": "The gas mask is ideal for handling toxic gases."},
            },
            "failure_items": {}, 
            "desc": "Your team passes through what appears to be an empty section of rock. But something is wrong. There is a dense layer of volcanic gases, deadly to anything that breathes. You'll need to find a way around, or through it is you want to continue your mission.", 
            "continue_failure_desc": "Your team are forced to double back and go the long, long way round, costing significant time and energy.", 
            "final_failure_desc": "Your team have lost too much time to double back now. They make the unwise decision to try and pass through, afterall, there are probably patches of air somewhere in there. They hold their breath and start walking. They don't get far. The gases knock the team out and they slump to the ground one by one, never to wake again."
        },

        "Narrow Crevasse": {
            "challenge_name": "Narrow Crevasse",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Rope": {"use_desc": "Your team manage to lasoo a rock jutting up on the far side. You carefully swing each teammate across the gap.", "used": False, "point_value": 70, "point_desc": "The rope is able to get your team across, but it's a risky maneuver."},
            },
            "failure_items": {},
            "desc": "A crevasse blocks your path. Your team needs to cross it if you want to continue your mission.",
            "continue_failure_desc": "Your team follows the crevasse until it narrows, losing time and energy on the detour.",
            "final_failure_desc": "Your team, out of time and energy make a desperate decision to try to jump the distance, it is after all, only a narrow crevasse. Unfortunately they are too tired to get a proper run. The fall is a lot further than they could have imagined. Your mission ends here."
        },
    },



    "Find Shelter": {
        "Find Civilization": {
            "challenge_name": "Find Civilization",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Map": {"use_desc": "Your team is able to use the few landmarks nearby to orient themselves. Your team is able to use the map to work out where the nearest patch of civilization is and head towards it.", "used": False, "point_value": 100, "point_desc": "The map is ideal for helping your team navigate towards civilization."},
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
                "Map": {"use_desc": "You use the map to orient yourself and work out where the nearest stretch of land is. The map isn't waterproof so gets damaged in the process.", "used": True, "point_value": 80, "point_desc": "The map is successful in getting your team to orient themselves, but it disintergrates in the water, so your team is forced to memorise the heading. A risky but successful maneuver."},
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
                "Map": {"use_desc": "You use the map to orient yourself and work out where the nearest shelter would be. This helps your team get there efficiently.", "used": False, "point_value": 80, "point_desc": "The map is successful in ensuring that your team is on the fastest path, but doesn't help them get there."},
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
                "Water Bottle": {"use_desc": "You drink from the water bottle, refreshing yourselves for the rest of the mission. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "The water bottle is an ideal and quick solution to dehydration."},
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
                "Water Bottle": {"use_desc": "You drink from the water bottle, refreshing yourselves for the rest of the mission. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "The water bottle is an ideal and quick solution to dehydration."},
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
                "Water Bottle": {"use_desc": "You drink from the water bottle, refreshing yourselves for the rest of the mission. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "The water bottle is an ideal and quick solution to dehydration."},
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
                "Water Bottle": {"use_desc": "You drink from the water bottle, refreshing yourselves for the rest of the mission. The water is used up in the process.", "used": True, "point_value": 100, "point_desc": "The water bottle is an ideal and quick solution to dehydration."},
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
                "Armoured Truck": {"use_desc": "Your team pile into the armoured truck and tear off. Nothing stands in your way and whilst it's a messy getaway, it is successful.", "used": False, "point_value": 90, "point_desc": "The getaway is messy, but the armoured truck means that you can move as fast as you like without having to worry about anything."},
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
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small fire. The smoke attracts the attention of your pursuers. You travel in the opposite direction, using the fire as a diversion. The kindling is used up in the process.", "used": True, "point_value": 75, "point_desc": "The fire successfully mislead the pursuers, but it did cause some significant damage in the process."},
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
                "Dune Buggy": {"use_desc": "Your team pile into the dune buggy and tear off. It is fast even over the sand and your team is able to continue their mission.", "used": False, "point_value": 100, "point_desc": "The dune buggy is ideal for traversing desert."},
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
                "Snow Mobile": {"use_desc": "Your team pile into the snow modile and it tears off across the fresh snow.", "used": False, "point_value": 100, "point_desc": "The snow mobile is ideal for getting places fast on snow."},
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
                "Stolen Uniforms": {"use_desc": "Your team don the stolen uniforms and blend right in. There's a terrifying moment when another guard asks to see your id, but you manage to bluff your way past.", "used": False, "point_value": 80, "point_desc": "Putting yourself in plain sight. An effective but dangerous maneuver."},
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
                "Boat": {"use_desc": "Your team pile into the boat and tear away.", "used": False, "point_value": 100, "point_desc": "The boat is ideal for quick getaways on the water."},
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
                "Welding Kit": {"use_desc": "Your team uses the welding kit to fuse another section of beams together with the wall into a kind of braced structure. It's messy but works. The welding supplies are used up in the process.", "used": True, "point_value": 60, "point_desc": "The welding kit did the job, but it's only a temporary solution."},
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
                "Welding Kit": {"use_desc": "Your team welds shut a section that had been torn. It should hold for some time yet. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The welding supplies are ideal for re-connecting the 2 sections of metal wall."},
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
                "Welding Kit": {"use_desc": "Your team uses the welding kit to fuse another section of beams together with the enviro-dome room into a kind of braced structure. It's messy but works. The welding supplies are used up in the process.", "used": True, "point_value": 60, "point_desc": "The welding kit did the job, but it's only a temporary solution."},
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
                "Welding Kit": {"use_desc": "Your team welds shut a section that had been torn. It should hold for some time yet. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The welding supplies are ideal for re-connecting the 2 sections of metal wall."},
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
                "Welding Kit": {"use_desc": "You find that the hinges to the door have been knocked out of alignment. You use the welding kit to fuse them back in the correct position, allowing the door to open. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The welding kit is ideal for handling a job like this."},
            },  
            "failure_items": {
                "Explosives": {"use_desc": " The explosives, well, explode in the process.", "used": True, "point_value": 0, "point_desc": "You do realise that you're stuck inside the base, right? Not your brightest idea. I mean you got it open, it's just not really of any use to you anymore."},
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
                "Welding Kit": {"use_desc": "You add scraps of metal to 'Gerogie' and weld them into place. It should hold for some time yet. The welding supplies are used up in the process.", "used": True, "point_value": 70, "point_desc": "You do successfully repair the damage to the rover, but are unable to fix some of the inner mechanisms with such a crude implement."},
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
                "Welding Kit": {"use_desc": "You re-attach the solar panels to their correct positions and use the welding kit to fuse it in place. The welding supplies are used up in the process.", "used": True, "point_value": 60, "point_desc": "You do manage to re-attach the solar panels, but unfortunately, you can do little to repair their functionality with such a crude implement."},
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
                "Welding Kit": {"use_desc": "You use scraps of metal and weld them over the damaged portions of the vehicle. It's messy, but should hold. The welding supplies are used up in the process.", "used": True, "point_value": 70, "point_desc": "The vehicle is now in working order, but the solution is only temporary."},
            },  
            "failure_items": {}, 
            "desc": "There is a nearby base that your team needs to gather supplies from. Unfortunately the vehicle that your team uses to make trips has suffered damage and will need to be repaired.", 
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
                "Shovel": {"use_desc": "You clear the sand from the hatch, making it usable once more.", "used": False, "point_value": 100, "point_desc": "The shovel is ideal for this situation as it restores access without damaging the hatch."},
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
                "Stolen Uniforms": {"use_desc": "Your team don the stolen uniforms and saunter by with nary a turned head.", "used": False, "point_value": 100, "point_desc": "The stolen uniforms are ideal as they allow you to slip by quickly and without raising any suspicion."},
                "Explosives": {"use_desc": "Your team set up the explosives next to one of the unmanned walls and blow it. You dash through the hole in the wall before anyone knows what happened.", "used": True, "point_value": 80, "point_desc": "It's certainly dramatic and destructive, but does allow your team to successfully make it past the blockade."},
            },  
            "failure_items": {}, 
            "desc": "A blockade stands between you and your destination. And these guys don't look friendly. You'll need to find a way around, or through if you want to continue your mission.", 
            "continue_failure_desc": "Your team is forced to wait for a changing of the guards and takes the opportunity to slip past. It takes a long time.", 
            "final_failure_desc": "Your team, with no time to spare attempts a direct approach. You decide to try to bluff your way past, but they can small your lies a mile away and your team is taken in for questioning. Your mission ends here."
        },

        "Building/Locked Gate": {
            "challenge_name": "Locked Gate",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Explosives": {"use_desc": "Your team set up the explosives next to gate and blow it. You dash through before anyone knows what happened.", "used": True, "point_value": 80, "point_desc": "It's certainly dramatic and destructive, but does allow your team to successfully make it past the gate."},
            },  
            "failure_items": {}, 
            "desc": "There is a locked gate blocking your path, and your team is going to need to get past it. There is a building nearby with a key, if you can get in.", 
            "continue_failure_desc": "Your team decides to scale the gate. It takes a long time and your team receives a few injuries in doing so.", 
            "final_failure_desc": "Your team is too tired to find a way past the gate. You are simply forced to throw in the towel. Your mission ends here."
        },

        "Checkpoint": {
            "challenge_name": "Checkpoint",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Stolen Uniforms": {"use_desc": "Your team don the stolen uniforms and saunter by with nary a turned head.", "used": False, "point_value": 100, "point_desc": "The stolen uniforms are ideal as they allow you to slip by quickly and without raising any suspicion."},
            },  
            "failure_items": {}, 
            "desc": "There is a checkpoint your team will need to pass in order to continue your mission. Unfortunately, they're checking Ids and every member of your team has a, let's say, colourful past.", 
            "continue_failure_desc": "Your team is forced to wait for a changing of the guards and takes the opportunity to slip past. It takes a long time.", 
            "final_failure_desc": "Your team, with no time to spare attempts a direct approach. You decide to try to bluff your way past, but when you refuse to show your ids, your whole team taken in for questioning. Your mission ends here."
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
                "Boat": {"use_desc": "Your team pile into the boat and take off across the dam. Security spotsyou and try to intercept you, but you make it across safely. Unfortunatley you have to abandon the boat.", "used": True, "point_value": 60, "point_desc": "Not exactly a subtle maneuver, although it did get you across the dam pretty quick."},
            },  
            "failure_items": {}, 
            "desc": "A dam stands between you and your destination. You'll need to find a way over or around it if you want to continue your mission.", 
            "continue_failure_desc": "Your team are forced to trek around the enitre lake feeding the dam. A lengthy and tiring process.", 
            "final_failure_desc": "Your team attempts to cross the walkway across the dam. It is however blocked off. So when guards find you on the wrong side of the fence, they take you in for questioning. Your mission ends here."
        },

        "Giant Wall": {
            "challenge_name": "Giant Wall",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Grapling Hook": {"use_desc": "Your team secure the grapling hook to the top of the wall, and make your way easily to the top. Then you secure it again and make your way down. Easy.", "used": False, "point_value": 100, "point_desc": "The grapling hook is ideal for climbing especially walls. It's what grapling hooks are built for after all."},
            },  
            "failure_items": {}, 
            "desc": "An enormous wall, previously constructed by the military, stands between you and where you're going. It's abadnonded, but is still in the way. You'll need to find a way over, around or through it is you want to continue your mission.", 
            "continue_failure_desc": "You team is forced to go around. And that happens to be a long, long , long way. The trip tires your team out and takes a long time.", 
            "final_failure_desc": "Your team, without any way to get past it are forced to throw in the towel. Your mission ends here."
        },
        
        "Sea Mines": {
            "challenge_name": "Sea Mine",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Your team don the scuba gear. The flippers help you to move swiftly through the mine field and your maneuverable enough to get by unscathed. The oxygen tank is used up in the process.", "used": True, "point_value": 100, "point_desc": "The scuba gear is ideal for this situation. It allows you to move efficiently and safely past the sea mines."},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to traverse a patch of ocean. Unfortunately, it is full of sea mines left behind after some war, designed to blow up ships and submarines. You'll need to make sure that you can easily maneuver around them.", 
            "continue_failure_desc": "Your team decides to swim. Your certainly maneverable, but also slow. It is a time consuming and exhausting process, but eventually you pass the mines.", 
            "final_failure_desc": "Your team decides to swim. Unfortunately your exhaustion from earlier has caught up with you. Your team can barely stay afloat. The mines don't even get a chance to finish you. Your team simply stops having the strength to swim and is claimed by the ocean."
        },
        
        "Ship Graveyard": {
            "challenge_name": "Ship Graveyard",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Scuba Gear": {"use_desc": "Your team dons the scuba gear and quickly and easily navigate the ship wrecked environment. The oxygen tank is used up in the process.", "used": True, "point_value": 100, "point_desc": "The scuba gear is ideal for this situation. It allows you to move efficiently and safely past the sunken ships."},
            },  
            "failure_items": {},
            "desc": "Your team needs to traverse a section of ocean, unfortunately the shallow reef has wrecked many a ship. The water is littered with the metal skeletons. Rusted metal juts at all angles. You'll need to be careful.", 
            "continue_failure_desc": "Your team decides to swim. You manage to avoid the shipwrecks, but it is a tiring and time consuming process.", 
            "final_failure_desc": "Your team decides to swim for it. Your doing ok, but your exhaustion makes your team sloppy. One of your team gets their clothing snagged on a piece of underwater debree and is dragged under. The team rushes to help, but they are pulled further under as the debree falls to the ocean floor. Your team try desperately to free them but can do nothing. Very soon they are in their own predicament as they run out of air. Too exhausted to make it to the surface, they drown."
        },

        "Traffic": {
            "challenge_name": "Traffic",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Armoured Truck": {"use_desc": "Your team pile into the armoured truck and, just like an icebreaker, plow it through traffic. It's messy and almost certainly injures a few people, but you do make it through. The truck gets damaged as you ram your way through traffic.", "used": True, "point_value": 80, "point_desc": "A very messy an dangerous approach. Although you did successfully beat traffic."},
            },  
            "failure_items": {}, 
            "desc": "Your team need to cross a busy intersection of the city if you are to continue your mission. UNfortunately an accident earlier in the day has blocked all the roads with traffic.", 
            "continue_failure_desc": "Your team are forced to wait for traffic to clear before they continue. It takes a long, long time.", 
            "final_failure_desc": "Your team decide to try to run between the cars. Unfortunately you miss-time one of your sprints and get hit. You go down. Your mission ends here."
        },

        "Debris Filled Stairwell": {
            "challenge_name": "Debris Filled Stairwell",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Shovel": {"use_desc": "You shovel the loose rubble aside until everyone can reach the stairs.", "used": False, "point_value": 100, "point_desc": "The shovel clears the obstruction efficiently."},
            },
            "failure_items": {},
            "desc": "Your team needs to make it through an alley. Unfortunately the end of the alley has a stairwell, full of debris. The structure is stable, but a passage must be cleared.",
            "continue_failure_desc": "Your team searches for another staircase and loses valuable time.",
            "final_failure_desc": "Your team cannot reach the upper level before access is sealed."
        },

        "Retracted Loading Walkway": {
            "challenge_name": "Retracted Loading Walkway",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items": {
                "Grapling Hook": {"use_desc": "You secure the grappling hook to the railing and use its line to cross the gap.", "used": False, "point_value": 100, "point_desc": "The hook provides a secure crossing point without restarting the walkway."},
            },
            "failure_items": {},
            "desc": "Your team needs to make it to the other side of a walkway. Unfortunately the walkway has retracted, leaving a narrow gap above a dry service platform. A sturdy railing stands on the far side.",
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
                "Wire Cutters": {"use_desc": "Your team break open a fuse box that powers the alarms. You cut the wires to the alarms in the nearby sections preventing them from triggering.", "used": False, "point_value": 100, "point_desc": "The wire cutters are ideal for this task, they not only deactivate the alarms, but the appraoch is subtle enough that it didn't draw any attention."},
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
                "Wire Cutters": {"use_desc": "Your team break open a fuse box that powers the security cameras. You cut the wires to the cameras, and thereby cut the feed.", "used": False, "point_value": 70, "point_desc": "You were successful in deactivating the cameras, but cutting the feeds will draw unwanted attention. It won't be long before someone is sent to find out what went wrong."},
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
                "Map": {"use_desc": "Your team check the schematics of the building. You use it to locate a service entrance that your team sneaks in through.", "used": False, "point_value": 100, "point_desc": "The map is ideal for finding alternate routes inside."},
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
                "Map": {"use_desc": "Your team check the schematics of the building. You use it to locate a service entrance that your team sneaks out through.", "used": False, "point_value": 100, "point_desc": "The map is ideal for finding alternate routes out of the building."},
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
                "Mirror": {"use_desc": "Your team use the mirror to harmlessly deflect the lasers and get past.", "used": False, "point_value": 100, "point_desc": "The mirror is ideal for dealing with laser based problems like this."},
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
                "Lock Picks": {"use_desc": "Your team uses the lock picks to break into the vault. It's tricky and not exactly what they were designed for. But it gets the job done. The lock picks get damaged in the process.", "used": True, "point_value": 80, "point_desc": "It's a time consuming process, but using the lock picks does allow the team to break open the safe subtly."},
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
                "Axe": {"use_desc": "Your team uses the axe to break the wooden crate. It's easy enough to do, just a little loud.", "used": False, "point_value": 80, "point_desc": "The axe is effective at getting the goods from the crate, but creates a lot of noise in the process."},
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
                "Stolen Uniforms": {"use_desc": "One member of the team puts on a uniform. They act as casually as they can and 'bump' into the guard who has the item. They get the item without anyone being the wiser.", "used": False, "point_value": 100, "point_desc": "The stolen uniform is ideal for stealing the item without raising suspicion."},
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
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, filtering the air and making it breathable.", "used": False, "point_value": 40, "point_desc": "The gas mask is an effective, but temporary solution. You didn't actually 'fix' anything."},
            }, 
            "failure_items": {}, 
            "desc": "The base's air recycling system has gone offline. It won't be long before the air in the base becomes unbreatheable. You'll need to fix it.", 
            "continue_failure_desc": "Your team try to fix the system with what they have, costing significant time and energy, but there's nothing they can do. With no useful tools, you team opens a roof hatch to allow fresh air in. It's a temporary solution and likely won't work for long.", 
            "final_failure_desc": "With no useful tools your team is unable to repair the system. Unfortunately, the time your team lost earlier has meant that the air being pumped in the base is already toxic. It doesn't take long before the team collapse, never to get back up."
        },

        "Central Heating Offline": {
            "challenge_name": "Central Heating Offline",
            "viable_locations": ["Arctic Tundra", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Blanket": {"use_desc": "Your team wear blankets that keep them warm.", "used": False, "point_value": 30, "point_desc": "The blankets are cumbersome and don't actually resolve the heating issue. They however, do your keep your team warm. For now."},
            },  
            "failure_items": {}, 
            "desc": "The central heating system has gone offline. You'll need to fix it if you don't want to freeze to death.", 
            "continue_failure_desc": "Your team try to fix the system with what they have, costing significant time and energy, but there's nothing they can do. Your team rug up as best they can. They'll just have to handle the freezing temperatures.", 
            "final_failure_desc": "Your team try to fix the system with what they have, but there's nothing they can do. Their exhaustion makes them slower and slower. They are forced to rest and eventually fall asleep, never to wake again."
        },

        "Communications System Failure": {
            "challenge_name": "Communications System Failure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Handheld Radios": {"use_desc": "Your team uses the handheld radios to communicate with one another. The radio's batteries are drained in the process.", "used": True, "point_value": 50, "point_desc": "Whilst it does temporarily allow for communication, the radios are only a temporary fix."},
            },  
            "failure_items": {}, 
            "desc": "The communications system is offline. As the base is so large and sprawling, it's going need to be fixed if the base is to remain useable.", 
            "continue_failure_desc": "Your team manages to rig up the system to give very crackly output. It's almost workable, but took significant time to complete.", 
            "final_failure_desc": "Your team, unable to develop a solution to the comms problem is forced to give up on the mission. Without a working comms system, the base is unusable. Your mission ends here."
        },

        "Cooling Offline": {
            "challenge_name": "Cooling Offline",
            "viable_locations": ["Desert", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Still-suit": {"use_desc": "Your team don still suits. They provide relief from the scorching temperatures.", "used": False, "point_value": 50, "point_desc": "The still suits are well equipped to handle the heat, but they are only a temporary fix."},
            },  
            "failure_items": {}, 
            "desc": "The central cooling system has gone offline. You'll need to fix it if you don't want to collapse from the heat.", 
            "continue_failure_desc": "Your team try to fix the system with what they have, costing significant time and energy, but there's nothing they can do. They'll just have to handle the scorching temperatures.", 
            "final_failure_desc": "Your team try to fix the system with what they have, but there's nothing they can do. Their exhaustion makes them slower and slower. They are forced to rest and eventually fall asleep, never to wake again."
        },

        "Geo-Thermal Reactor Failure": {
            "challenge_name": "Geo-Thermal Reactor Failure",
            "viable_locations": ["Arctic Tundra", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Your team uses the welding kit to reconnect the sections of the geothermal reactor that are broken and get it back into working order. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The welding kit is ideal for these sorts of situations."},
            },  
            "failure_items": {}, 
            "desc": "There is a failure with the Geo-Thermal reactor. Without it the base won't have power. You'll need to fix it if you want the base to remain usable.", 
            "continue_failure_desc": "Your team manage to scavange some wiring from other sections of the base and rig up some rudimentary repairs. It is by no means a solution, but it'll work for now.", 
            "final_failure_desc": "Your team, unable to develop a solution to the problem is forced to give up on the mission. Without a access to a steady power supply the base is unusable. Your mission ends here."
        },

        "Main Reactor Failure": {
            "challenge_name": "Main Reactor Failure",
            "viable_locations": ["Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Welding Kit": {"use_desc": "Your team uses the welding kit to reconnect the sections of the main reactor that are broken and get it back into working order. The welding supplies are used up in the process.", "used": True, "point_value": 100, "point_desc": "The welding kit is ideal for these sorts of situations."},
            },  
            "failure_items": {}, 
            "desc": "There is a failure with the main reactor. Without it the base won't have power. You'll need to fix it if you want the base to remain usable.", 
            "continue_failure_desc": "Your team manage to scavange some wiring from other sections of the base and rig up some rudimentary repairs. It is by no means a solution, but it'll work for now.", 
            "final_failure_desc": "Your team, unable to develop a solution to the problem is forced to give up on the mission. Without a access to a steady power supply the base is unusable. Your mission ends here."
        },
    },



    "Travel To Rendezvouz": {
        "Air Based Travel": {
            "challenge_name": "Travel To Rendezvou",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Helicopter": {"use_desc": "Your team pile into the helicopter and make your way to the rendezvouz quickly and safely.", "used": False, "point_value": 100, "point_desc": "The helicopter is ideal for air based travel"},
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
                "Armoured Truck": {"use_desc": "Your team pile into the armoured truck and take off towards the rendezvouz point. It allows you to make the journey quickly and safely.", "used": False, "point_value": 100, "point_desc": "The armoured truck is an ideal option for land based travel."},
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
                "Dune Buggy": {"use_desc": "Your team pile into the dune buggy and take off towards the rendezvouz point. It allows you to make the journey quickly and safely.", "used": False, "point_value": 100, "point_desc": "The Dune Buggy is an ideal option for travel over sand."},
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
                "Snow Mobile": {"use_desc": "Your team pile into the snow mobile and take off towards the rendezvouz point. It allows you to make the journey quickly and safely.", "used": False, "point_value": 100, "point_desc": "The snow mobile is an ideal option for travel over snow."},
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
                "Boat": {"use_desc": "Your team pile into the boat and take off towards the rendezvouz point. It allows you to make the journey quickly and safely.", "used": False, "point_value": 100, "point_desc": "The boat is an ideal option for travel over water."},
            },  
            "failure_items": {}, 
            "desc": "Your team needs to travel to the agreed rendezvouz point. From your current position, the fastest and safest way to get there is using water based transport.", 
            "continue_failure_desc": "Without an appropriate method of transportation, your team is forced to swim the distance. It's a long way and not at all an easy trip. When your team eventually arrives at the rendezvouz point they've lost a lot of time and are exhausted.", 
            "final_failure_desc": "Without an appropriate method of transportation, your team is forced to attempt to swim the distance. The time they lost earlier is weighing on them and they know they'll have to move fast if they are to reach the rendezvouz point on time. Your team makes the unwise decision to take a shortcut through rough waters. It's a hazardous path, one your team could barely manage in peak conddition, and they are far from that. Exhausted from their earlier efforts, your team struggles to stay afloat in the raging waters. It isn't long before catastrophe. Your team never makes it to their destination."
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