challenges_dict = {
    "Contact Teammate/s": {
        "Alert Another Team": {
            "challenge_name": "Alert Another Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small signal fire. The other team sees it and is alerted to your position.", "point_value": 70, "point_desc": "The signal fire gets the team's attention and gives them a clear destination to aim for. It does, however, risk attracting unwanted attention."}, 
                "Handheld Radios": {"use_desc": "You use your handheld radios to call the the other team and alert them to your position.", "point_value": 100, "point_desc": "The radios are perfectly suited for this scenario. Both teams are able to communicate and discuss a rendovouz point."},
                "Mirror": {"use_desc": "You use the mirror to reflect light in the direction of the other team. They see it and are able to track it back, alerting them to your position.", "point_value": 60, "point_desc": "The mirror was able to attract the other team's attention, but it was hard to trace back to an origin and took a while for them to even notice it in the first place."},
            }, 
            "desc": "To be able to continue your mission you are going to need to be able to alert the other team to your position.",
            "continue_failure_desc": "Without the right equipment, your team is unable to alert the other team to your presence. You'll just have to continue the mission and hope that they will know where to rendovouz. This will take a long time and slow your team down.", 
            "final_failure_desc": "Your team is unable to work out how to contact the other team. Without being able to alert them to your position, you'll never be able to rendovouz. Your mission ends here."
        },

        "Contact Rescue Team - Survival": {
            "challenge_name": "Contact Rescue Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{
                "Handheld Radios": {"use_desc": "Using your handheld radios you are able to find an active frequency and call for help.", "point_value": 100, "point_desc": ""},
            }, 
            "desc": "You're team is going to need to get in contact with someone if they hold out any hope of being rescued.",            
            "continue_failure_desc": "Your team is unable to find a method to get in contact with a rescue team. They are instead forced to make their way to a military base some distance away and petition them for help. The journey takes a long time and a lot of energy.", 
            "final_failure_desc": "Without the needed supplies to make contact with a rescue crew, your team is forced to attempt to trek to a distant military base and hope that they can help. Your team, out of options and completely exhausted, begins the perilous journey. They will never reach their destination."
        },

        "Contact Rescue Team - Escape": {
            "challenge_name": "Contact Rescue Team",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Escape"],
            "items":{
                "Handheld Radios": {"use_desc": "Using your handheld radios you are able to find an active frequency and call for help.", "point_value": 100, "point_desc": ""},
            }, 
            "desc": "Your team needs to put some distance between you and your captors. You'll need to get in contact with a rescue crew if you want to get out of here.",
            "continue_failure_desc": "Your team is unable to find a method to get in contact with a rescue team. They are instead forced to make their way to a military base some distance away and petition them for help. The journey takes a long time and a lot of energy.", 
            "final_failure_desc": "Without the needed supplies to make contact with a rescue crew, your team is forced to attempt to trek to a distant military base and hope that they can help. Your team, out of options and completely exhausted, begins the perilous journey. They will never reach their destination."
        },

        "Contact Stranded Teammate": {
            "challenge_name": "Contact Stranded Teammate",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Rescue"],
            "items":{

            }, 
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
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas to harmlessly incapacitate the arctic bear and use the gas mask to slip by unscathed.", "point_value": 100, "point_desc": ""},
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the arctic bear retreats.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Ash": {
            "challenge_name": "Ash",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Blizzard": {
            "challenge_name": "Blizzard",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        "Cliff": {
            "challenge_name": "Cliff",
            "viable_locations": ["Arctic Tundra", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Collosal Wave": {
            "challenge_name": "Collosal Wave",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""},
        
        "Crocodile": {
            "challenge_name": "Crocodile",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas to harmlessly incapacitate the Crocodile and use the gas mask to slip by unscathed.", "point_value": 100, "point_desc": ""},
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the crocodile retreats.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Cyclone": {
            "challenge_name": "Cyclone",
            "viable_locations": ["Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Deadly Insects": {
            "challenge_name": "Deadly Insects",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to light a large branch on fire. Wielding the branch you are able to pass through, using the flame and smoke to keep the bugs at bay.", "point_value": 90, "point_desc": "The flame is able to easily deal with the swarm of bugs and is well suited to the task. Unfortunately a couple of bugs do get past, but their bites alone are not enough to inflict significant damage."},
                "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas. It is too potent for the bugs to pass through. You use the gas mask to pass by unscathed.", "point_value": 100, "point_desc": "The gas is able to easily deal with the swarm of bugs and is well suited to the task."},
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
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous marshland gases.", "point_value": 100, "point_desc": "The gas mask is ideal for situations just like this. It was the perfect tool to help you pass safely through the marshlands."},
                "Scuba Gear": {"use_desc": "Your team uses the scuba tanks and masks to breathe safely as make your way through the marshlands.", "point_value": 90, "point_desc": "The scuba gear is very effective and keeps your team safe. It is however, unwieldy and gets snagged on marshland plants and vines, slowing your progress."},
            },
            "failure_items": {
                "Fire Starter Kit": {"use_desc": "You use the fire starter to create a small flame. Within an instant, your entire team is wiped out.", "point_value": 0, "point_desc": "This is what we call a bad idea. Turns out those deadly gases were not only toxic, but also highly flammable. The ensuing fireball that consumed your team was so explosive that your first clue that anything went wrong would have been you, knocking on the pearly gates."}},
            "desc": "Your team comes across an expansive stretch of marshland that you will be forced to cross if you want to continue your mission. Unfortunately, pockets of the marshland are full of deadly gases, invisible to the human eye.", 
            "continue_failure_desc": "Your team is forced to navigate around the marshlands. This takes a significant amount of time and the longer trip significantly tires your team out.", 
            "final_failure_desc": "In desperation, your team tries to progress through the marshlands without the correct equipment. As the marshland gases slowly invade their systems, they find it harder and harder to stay awake. The exhaustion overtakes them and they rest for what they plan to only be a minute. They are claimed by the jungle."
        },

        "Earthquake": {
            "challenge_name": "Earthquake",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Extreme Heat": {
            "challenge_name": "Extreme Heat",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fallen Trees Block Path": {
            "challenge_name": "Fallen Trees Block Path",
            "viable_locations": ["Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fire": {
            "challenge_name": "Fire",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Flash Flood": {
            "challenge_name": "Flash Flood",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Frozen Lake": {
            "challenge_name": "Frozen Lake",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Heat Wave": {
            "challenge_name": "Heat Wave",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Ice Cliff": {
            "challenge_name": "Ice Cliff",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use the Ice Axes to scale the ice cliff.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Land Slide": {
            "challenge_name": "Land Slide",
            "viable_locations": ["Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wedge the ice axes as deep into the surrounding rock as possible and hold on tight. After the landslide has past, you need to dig yourselves out, but you are otherwise fine.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Lava Spout": {
            "challenge_name": "Lava Spout",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Mirages": {
            "challenge_name": "Mirages",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Nest of Scorpions": {
            "challenge_name": "Nest of Scorpions",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You toss the smoking kindling into the nest and the smoke pacifies the scorpions allowing you to pass by unscathed.", "point_value": 100, "point_desc": ""},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister into the nest, the gas causes the scorpions to scatter allowing you to pass by unscathed.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Quick Sand": {
            "challenge_name": "Quick Sand",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You use wedge the ice axes into the surrounding solid ground and use them to pull yourselves out.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "River": {
            "challenge_name": "River",
            "viable_locations": ["Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Rockfall": {
            "challenge_name": "Rockfall",
            "viable_locations": ["Arctic Tundra", "Jungle", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Dunes": {
            "challenge_name": "Sand Dunes",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Storm": {
            "challenge_name": "Sand Storm",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Shallow Reef": {
            "challenge_name": "Shallow Reef",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Shark Attack": {
            "challenge_name": "Shark Attack",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Ice Axes": {"use_desc": "You wield the ice axes as weapons. You land a hit and the shark retreats.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Temperature Drop": {
            "challenge_name": "Temperature Drop",
            "viable_locations": ["Arctic Tundra", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Underwater Earthquake": {
            "challenge_name": "Underwater Earthquake",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Venemous Snake": {
            "challenge_name": "Venemous Snake",
            "viable_locations": ["Desert", "Jungle"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to create a small fire. You use the flame to keep the reptile at bay, and pass by unscathed.", "point_value": 100, "point_desc": ""},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister near the snake, harmlessly incapacitating it and you use the gas mask to slip by unscathed.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Volcanic Gases": {
            "challenge_name": "",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous fumes of the volcano.", "point_value": 100, "point_desc": ""},
            },
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Find Shelter": {
        "Find Civilization": {
            "challenge_name": "Find Civilization",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        }, 

        "Find Shelter": {
            "challenge_name": "Find Shelter",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Find Water": {
        "Get Water - Desert": {
            "challenge_name": "Get Water",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
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
                "Ice Axes": {"use_desc": "You stumble across a frozen river. You use the ice axes to break through the thick ice and gain access to the flowing water beneath.", "point_value": 80, "point_desc": "The ice axes were an effective tool for overcoming this obstacle."},
                "Fire Starter Kit": {"use_desc": "You find a large chunk of ice, and using the fire starter kit to create a small fire. The small flame melts some of the ice into water.", "point_value": 70, "point_desc": "Whilst the flame was able to melt the ice, the water it produced dampened the kindling and put the fire out. So, you managed to obtain water, but not as much as you might have wanted."},
                "Mirror": {"use_desc": "You find a large chunk of ice and use the mirror to focus a beam of sunlight on it. Very slowly the ice melts into water.", "point_value": 50, "point_desc": "The mirror did successfully help you obtain water, it took a long time and produceed barely enough water."},
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "So much exertion has left your team severely dehydrated. You'll need to find a source of clean water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Ocean": {
            "challenge_name": "Get Water",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.",  
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },

        "Get Water - Volcano": {
            "challenge_name": "Get Water",
            "viable_locations": ["Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "In such a harsh environment, your team finds that they have become severely dehydrated. You'll need to find a source of water if you have any hope of continuing your mission.", 
            "continue_failure_desc": "Unable to find a source of clean water, your team is forced to continue in their dehydrated and exhausted state. You'll have to hope that you finish your mission before it catches up with you.", 
            "final_failure_desc": "Unable to find a source of clean water, your team is forced to try to continue their mission in their severely dehydrated state. Unfortunately the time and energy you expended earlier has cuaght up with you. It isn't long before your team collapses, never to wake again."
        },
    },



    "Getaway": {
        "Air Based Getaway": {
            "challenge_name": "Air Based Getaway",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Paraglider": {"use_desc": "Your team finds the highest point they can and paraglide silently away.", "point_value": 80, "point_desc": "The paragliders quickly put some distance between you and your would be pursuors. They are particularly effective due to how silently they move, but once you reach the forested jungle, they become cumbersome and impractical. Fortunately by that point you are pretty much in the clear."},
                "Helicopter": {"use_desc": "You quickly pile into the helicopter that is standing by and take off.", "point_value": 90, "point_desc": "The helicopter is very efficient at putting putting some distance between you and your would be pursuors. It is very loud, which alerts the guards to your presences, but fortunately you're out of there before they get the chance to follow you."},
            }, 
            "failure_items": {},
            "desc": "Your team is going to need to get away, and fast. The only way out, from your current position, is by air.", 
            "continue_failure_desc": "Your team is forced to make a run for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },
        
        "Land Based Getaway": {
            "challenge_name": "Land Based Getaway",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is overland land.", 
            "continue_failure_desc": "Your team is forced to make a run for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Mislead Pursuers": {
            "challenge_name": "Mislead Pursuers",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your team isn't going to be able to outmaneuver your pursuers. Looks like you'll have to out-think them instead and lead them in the wrong direction before doubling back.", 
            "continue_failure_desc": "Without any better ideas, your team is forced to deploy the fastest of you. They make their way in the opposite direction, luring the attackers away. When they have lead them far enough away, they double back. It took a lot of time to shake them and trip tires your teammate out significantly.", 
            "final_failure_desc": "In desperation, your team deploys the fastest of you to lure your attackers away. Unfortunately sheer exhaustion has caught up with your teammate and they are unable to outrun their pursuers. It isn't long before the rest of you find yourselves in enemy hands. Your mission ends here."
        },

        "Sand Based Getaway": {
            "challenge_name": "Sand Based Getaway",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is across the dunes.", 
            "continue_failure_desc": "Your team is forced to make a run for it (or as best a run as you can manage on sand). You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Snow Based Getaway": {
            "challenge_name": "Snow Based Getaway",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your team is going to need to get away, and fast. The only way out, is over the freshly powdered snow.", 
            "continue_failure_desc": "Your team is forced to make a run for it (or as best a run as you can whilst tumbling into snow drifts). You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
            "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
        },

        "Use Stealth": {
            "challenge_name": "Use Stealth",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {
                "Armoured Truck": {"use_desc": "Your team pile into the armoured truck and stop for nothing. The vehicle draws a lot of attention as it tears away. You make it about 100m before your mission ends abruptly.", "point_value": 0, "point_desc": "What about an armoured truck struck you as particularly sneaky. Didn't you hear the part where I said that you were outgunned? Well yeah, they got you. One well placed rpg and your team was no more. Let's try a subtler approach next time, huh?"},
            }, 
            "desc": "Your opponents are well equipped, your team isn't going to be able to outmaneuver or outgun them. Looks like you're going to have to perform a sneaky getaway.", 
            "continue_failure_desc": "Without any better ideas, your team is forced to camp out in a cramped storage cupboard until an opportunity presents itself to slip by undetected. It took a long time though and your team is in no way happy about it.", 
            "final_failure_desc": "Unable to wait any longer your team attempts to make a break for it when an opportunity presents itself. Unfortunatley your team is exhausted and you can't make it out of sight in time. Alarms blare, and within a moment your whole team is captured. Your mission ends here."
        },

        "Water Based Getaway": {
            "challenge_name": "Water Based Getaway",
            "viable_locations": ["Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
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
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your base has sustained damage to one of the outward-facing walls. You'll need to repair it.", 
            "continue_failure_desc": "Without the proper tools to mend it, your team is forced to try and make do. You manage to scavange some old beams from another section of the base and use it to support the wall structure. It takes a long time and is a very exhausting process.", 
            "final_failure_desc": "Your team attempt to repair the wall using beams, scavanged from a closed off section of your base. Unfortunately, in their rush and exhaustion, their judgment on which beams are structural is severely lacking. It isn't long before another wall collapses, making the base unusable. Your mission ends here."
        },

        "Repair Collapsed Wall - Ocean": {
            "challenge_name": "Repair Collapsed Wall",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your base has sustained damage to one of the outward-facing walls and a whole quadrant of your base is flooded and sealed off. You'll need to repair the wall before you can even think about pumping the water out",
            "continue_failure_desc": "Without the proper tools to mend it, your team is forced to leave the section closed off. Your team is forced to constantly navigate in open ocean to access the other sections of the base. It takes a long time and is a very exhausting process.", 
            "final_failure_desc": "Your team attempt to repair the wall using beams, scavanged from a closed off section of your base. Unfortunately, in their rush and exhaustion, their judgment on which beams are structural is severely lacking. It isn't long before another wall collapses flooding the rest of the base. Your mission ends here."
        },

        "Repair Enviro-Dome": {
            "challenge_name": "Repair Enviro-Dome",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your base has sustained damage to it's enviro-dome, housing numerous samples your team has collected from their time here. You'll need to work fast, but carefully to repair it, before the samples become inmpacted.", 
            "continue_failure_desc": "Without the right eqipment there's nothing you can do. You manage to rescue the samples and some are still holding out, but years of work have been lost. It takes a long time to rehouse the remaining samples.", 
            "final_failure_desc": "Without the correct equipment, the enviro dome is beyond repair. And with the time your team lost earlier, all the samples have been destroyed. Your mission ends here."
        },

        "Repair Enviro-Dome  - Ocean": {
            "challenge_name": "Repair Enviro-Dome",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your base has sustained damage and flooding to the enviro-dome, housing numerous samples your team has collected from their time here. You'll need to perform any repairs carefully, and quickly before the samples are impacted.",
            "continue_failure_desc": "Without the right eqipment there's nothing you can do. You manage to rescue the samples and some are still holding out, but years of work have been lost. It takes a long time to rehouse the remaining samples.", 
            "final_failure_desc": "Without the correct equipment, the enviro dome is beyond repair. And with the time your team lost earlier, all the samples have been destroyed. Your mission ends here."
        },

        "Repair Exit Hatch": {
            "challenge_name": "Repair Exit Hatch",
            "viable_locations": ["Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {
                "Explosives": {"use_desc": "", "point_value": 0, "point_desc": "You do realise that you're stuck inside the base, right? Not your brightest idea......................................................"},
            }, 
            "desc": "In a recent rock fall, your base suffered damage to the exit hatch. It's holding together for now, but there's no telling how long it will be before the door caves and everything beyond it, will find its way in. And besides that, whilst it's broken, your team has no way out.", 
            "continue_failure_desc": "Without the right equipment all your team can do is hope that it holds. You are, however, trapped. You are forced to re-wire the rover exit hatch to gain access to the outside of the base. It takes a long time, and squeezing through the tiny gap is an arduous feat.", 
            "final_failure_desc": "Whilst the hatch held out for a long time, it can't hold out for ever. The time you lost earlier catches up with you. Your team is trapped inside the base with no exit and no time to come up with an alternate way out, when the hatch caves. Your mission ends here."
        },

        "Repair Rover": {
            "challenge_name": "Repair Rover",
            "viable_locations": ["Arctic Tundra", "Desert", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "Your friendly little rover 'Georgie' has suffered damage in a recent rockfall. You'll need it to be in working condition if you hope to collect any more samples before they are destroyed by changing outside conditions.", 
            "continue_failure_desc": "Unfortunately, without the proper equipment, there's nothing you can do for your little rover, 'Georgie'. Your team is forced to collect samples by hand before external conditions change and destroy the samples. It's a dangerous activity and takes a long time and a lot of effort.", 
            "final_failure_desc": "Without the rover your team will be unable to collect any more samples. You might have had time to collect more samples by hand, but your delays have caught up with you. Changing external conditions have destroyed any more samples you might have been able to retrieve, ending your mission."
        },

        "Repair Solar Panels": {
            "challenge_name": "Repair Solar Panels",
            "viable_locations": ["Desert", "Ocean"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "The solar panels that help power vital sections of your base have been knocked out of alignment. You'll need to make a few repairs and get them back in their rightful places if you want to keep getting power.", 
            "continue_failure_desc": "You manage to re-align the solar panels, but you can't do anything about the repairs. They aren't going to be able to produce much power at all. It took a lot of time and effort to re-align them without the proper tools.", 
            "final_failure_desc": "In their exhaustion, one of your teammembers makes a mistake whilst re-aligning the solar panels and they dislodge from the base and crash to the ground. Without them vital systems in your base will be unable to function, rendering the base unusable. Your mission ends here."
        },

        "Repair Vehicle": {
            "challenge_name": "Repair Vehicle",
            "viable_locations": ["Arctic Tundra", "Desert", "Ocean", "Volcano"],
            "viable_mission_types": ["Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "There is a nearby base that your team needs to gather supplies from. Unfortunately the vehicle that your team uses to make trips has suffered damage and will need to be repaired. ", 
            "continue_failure_desc": "Without the appropriate equipment, you team is unable to repair the vehicle. You'll be forced to trek to the outposts without it. This is a time consuming process and exhausting.", 
            "final_failure_desc": "Without the appropriate equipment, you team is unable to repair the vehicle. They are too tired to make the trips without it and are forced to give up the mission."
        },
    },



    "Manmade Obstacle": {
        "Blockade": {
            "challenge_name": "Blockade",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Building": {
            "challenge_name": "Building",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Checkpoint": {
            "challenge_name": "Checkpoint",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Collapsed Bridge": {
            "challenge_name": "Collapsed Bridge",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Rope": {"use_desc": "You use the rope and, after numerous tries, manage to lasoo the broken parapet on the far side of the bridge. After testing that it can take the weight, your team takes turns lowering themselves down the side of the bridge and swinging across.", "point_value": 60, "point_desc": "Whilst successful, swinging across the bridge was a risky manuever and the set up cost you a lot of time."},
                "Paraglider": {"use_desc": "Your team find the highest point in the surrounding area and glide across the gap. Everyone reaches the other side safely.", "point_value": 100, "point_desc": "The glider is well suited to this kind of challenge and your team is able to quickly and easily navigate the obstacle."},
                "Grapling Hook": {"use_desc": "The team are able to hook the grapling hook on the broken parapet on the far side of the bridge. After testing that it can take the weight, your team takes turns lowering themselves down the side of the bridge and swinging across.", "point_value": 75, "point_desc": "Whilst swinging across the bridge was a somewhat risky manuever, the grapling hooks were efficient and ensured that the lines were well secured."},
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fortefied Structure": {
            "challenge_name": "Fortefied Structure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Giant Wall": {
            "challenge_name": "Giant Wall",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Pirates": {
            "challenge_name": "Pirates",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Sea Mines": {
            "challenge_name": "Sea Mine",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Ship Graveyard": {
            "challenge_name": "Ship Graveyard",
            "viable_locations": ["Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Traffic": {
            "challenge_name": "Traffic",
            "viable_locations": ["City"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Security Obstacle": {
        "Deactivate Alarms": {
            "challenge_name": "Deactivate Alarms",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Deactivate Security Cameras": {
            "challenge_name": "Deactivate Security Cameras",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Distract Guards": {
            "challenge_name": "Distract Guards",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small fire. The smoke attracts the attention of the guards and they leave their post to investigate.", "point_value": 75, "point_desc": "The fire successfully drew the guards away, but it did cause some significant damage in the process."},
                "Handheld Radios": {"use_desc": "You leave one of the handheld radios at your current position and move a distance away, calling it from your new position. The noise attracts the attention of the guards and they leave their post to investigate.", "point_value": 60, "point_desc": "The handheld radios successfully drew the guards away, but its presence alerted them to the fact that there was someone on the premises."},
                "Mirror": {"use_desc": "You leave the mirror at your current position and move a distance away. The glint of the mirror attracts the attention of the closest guards and they leave their post to investigate.", "point_value": 80, "point_desc": "The mirror successfully attracted the attention of the guards, its subtlety did not raise suspicion, but not all of the guards left their post to investigate."},
                "Gas Mask and Knockout Gas": {"use_desc": "You toss the knockout gas canister towards the guards, knocking them out. You use the gas mask to slip past.", "point_value": 60, "point_desc": "Not the cleanest of maneuvers. Whilst it did successfully incapacitate the relevant guards, there was a risk that someone would stumble across the bodies and sound the alarm."},
            }, 
            "failure_items": {},
            "desc": "Your team spots guards posted at several points around the perimeter. You are going to need to distract them to be able to slip by.", 
            "continue_failure_desc": "Without any viable tools, the team is forced to wait for the change of guard shift. They use the opportunity to slip by. Being forced to wait, unfortunately costs them hours.", 
            "final_failure_desc": "In desperation, your team attempts to slip by the guards unnoticed. Unfortunately, the exhaustion has made them sloppy. One member of the team accidently trips and the guards, hearing the noise, rush to investigate. Your team tries to run for it, but are too tired and are swiftly captured. Your mission ends here."
        },
        
        "Find Another Entrance": {
            "challenge_name": "Find Another Entrance",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Sneak Through": {
            "challenge_name": "Sneak Through",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Past the Laser Grid": {
            "challenge_name": "Get Past the Laser Grid",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Steal": {
        "Break into the Vault": {
            "challenge_name": "Break into the Vaul",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Open the crate": {
            "challenge_name": "Open the crate",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Pickpocket it": {
            "challenge_name": "Pickpocket it",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Retrieve the Item from the Laser Grid": {
            "challenge_name": "Retrieve the Item from the Laser Grid",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Mirror": {"use_desc": "You use the mirror to reflect the lasers away as one of you reaches in and grabs the insert_item_here.", "point_value": 100, "point_desc": "The mirror was an ingenious solution, efficient, clean, and it left the system intact, making it hard to notice that the insert_item_here had even been taken."},
                "Wire Cutters": {"use_desc": "You find the system that powers the laser grid and cut the wires. It deactivates the grid and you are able to grab the insert_item_here.", "point_value": 80, "point_desc": "You were successful in grabbing the insert_item_here, but there was evidence of your theft and the disappearence of the insert_item_here was quickly noticed."},
            }, 
            "failure_items": {},
            "desc": "You find the insert_item_here, but it's protected by a laser grid.", 
            "continue_failure_desc": "Your team attempts numerous solutions but remains unable to retrieve the item. You are forced to leave empty handed.", 
            "final_failure_desc": "Your team desperately tries to find a way past the lasers. Unfortunately, their exhaustion has made them sloppy, and they accidently trigger the laser system. In seconds the team is captured by armed guards. Your mission ends here."
        },
    },



    "System Failure": {
        "Air Recycling System Offline": {
            "challenge_name": "Air Recycling System Offline",
            "viable_locations": ["Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{
                "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, filtering the air and making it breathable.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Central Heating Offline": {
            "challenge_name": "Central Heating Offline",
            "viable_locations": ["Arctic Tundra", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Communications System Failure": {
            "challenge_name": "Communications System Failure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Cooling Offline": {
            "challenge_name": "Cooling Offline",
            "viable_locations": ["Desert", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Geo-Thermal Reactor Failure": {
            "challenge_name": "Geo-Thermal Reactor Failure",
            "viable_locations": ["Arctic Tundra", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Main Reactor Failure": {
            "challenge_name": "Main Reactor Failure",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Travel To Rendezvouz": {
        "Air Based Travel": {
            "challenge_name": "Air Based Travel",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Land Based Travel": {
            "challenge_name": "Land Based Travel",
            "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Volcano"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Based Travel": {
            "challenge_name": "Sand Based Travel",
            "viable_locations": ["Desert"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Snow Based Travel": {
            "challenge_name": "Snow Based Travel",
            "viable_locations": ["Arctic Tundra"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Water Based Travel": {
            "challenge_name": "Water Based Travel",
            "viable_locations": ["Jungle", "City", "Ocean"],
            "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Rescue", "Survival"],
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    }
}