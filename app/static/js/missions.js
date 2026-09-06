possible_locations = ["Arctic Tundra",  "Desert",  "Jungle",  "City",  "Ocean",  "Volcano"]

mission_structures = {
    "Train Hesit":              ["Heist",      {"Arctic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": false, "Volcano": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Steal",                "Manmade Obstacle",         "Getaway"               ]],
    "Artifact Heist":           ["Heist",      {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false, "Volcano": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Steal",                "Environmental Obstacle",   "Getaway"               ]],
    "Jewel Heist":              ["Heist",      {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false, "Volcano": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Steal",                "Manmade Obstacle",         "Getaway"               ]],
    "Steal Enemy Information":  ["Heist",      {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true,  "Volcano": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Steal",                "Security Obstacle",        "Getaway"               ]],
    "Break Out Another Team":   ["Heist",      {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false, "Volcano": false},    ["Travel To Rendezvouz",    "Manmade Obstacle",         "Security Obstacle",        "Contact Teammate/s",   "Security Obstacle",        "Getaway"               ]],
    "Escape Enemy Base":        ["Escape",     {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false, "Volcano": false},    ["Security Obstacle",       "Manmade Obstacle",         "Security Obstacle",        "Getaway",              "Contact Teammate/s",       "Travel To Rendezvouz"  ]],
    "Extract Another Team":     ["Rescue Op",  {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true,  "Volcano": true},     ["Contact Teammate/s",      "Environmental Obstacle",   "Travel To Rendezvouz",     "Getaway",              "Environmental Obstacle",   "Find Shelter"          ]],
    "Rescue Stranded Teammate": ["Rescue Op",  {"Arctic Tundra": true,   "Desert": true,   "Jungle": false,  "City": false,  "Ocean": true,  "Volcano": true},     ["System Failure",          "Find Shelter",             "Environmental Obstacle",   "Contact Teammate/s",   "Travel To Rendezvouz",     "Environmental Obstacle"]],
    "Repair Research Base":     ["Survival",   {"Arctic Tundra": true,   "Desert": true,   "Jungle": false,  "City": false,  "Ocean": true,  "Volcano": true},     ["Environmental Obstacle",  "SystemFailure",            "Environmental Obstacle",   "Make Repairs",         "Environmental Obstacle",   "Make Repairs"          ]],
    "Get Rescued":              ["Survival",   {"Arctic Tundra": true,   "Desert": true,   "Jungle": true,   "City": false,  "Ocean": true,  "Volcano": true},     ["Environmental Obstacle",  "Find Water",               "Environmental Obstacle",   "Find Shelter",         "Contact Teammate/s",       "Travel To Rendezvouz"  ]],
    // Deactivate Bomb
    // Loot Wreck (Jungle - Aeroplane, Ocean - Ship)
    // Destroy our info in enemy base
    // Make a switch
    // Smuggle Goods?
    // Answer a Distress Signal
    // Deactivate Super Weapon
}


location_challenges = {
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


//CONSIDER HAVING ITEMS THAT IF USED IN CERTAIN CASES END THE RUN (E.G USING FIRE WHEN SURROUNDED BY GASES CAUSES AN EXPLOSION)

items = {
    "Fire Starter Kit": {"desc": "A small kit comprising ...", "cost": 40},
    "Handheld Radios": {"desc": "A small device...", "cost": 60},
    "Mirror": {"desc": "A small reflective...", "cost": 20},
    "Gas Mask and Knockout Gas": {"desc": "A...", "cost": 200},

    "Ice Axes": {"desc": "A pair of ...", "cost": 100},

    "Armoured Truck": {"desc": "A land based vehicle...", "cost": 600},
    "Rope": {"desc": "A...", "cost": 100},
    "Paraglider": {"desc": "A...", "cost": 100},
    "Helicopter": {"desc": "A...", "cost": 100},
    "Grapling Hook": {"desc": "A...", "cost": 100},
    "Scuba Gear": {"desc": "A...", "cost": 100},
    "Wire Cutters": {"desc": "A...", "cost": 100},
    "Explosives": {"desc": "A...", "cost": 100},
}


challenges = {
    "Contact Teammate/s": {
        "Alert Another Team": {
            "challenge_name": "Alert Another Team",
            "items":{
                "Fire Starter Kit": {"use_desc": "You use the fire starter kit to make a small signal fire. The other team sees it and is alerted to your position.", "point_value": 100, "point_desc": ""}, 
                "Handheld Radios": {"use_desc": "You use your handheld radios to get in call the the other team and alert them to your position.", "point_value": 100, "point_desc": ""},
                "Mirror": {"use_desc": "You use the mirror to reflect light in the direction of the other team. They see it and are able to track it back, alerting them to your position.", "point_value": 100, "point_desc": ""},
            }, 
            "desc": "To be able to continue your mission you are going to need to be able to alert the other team to your position.",
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Contact Rescue Team": {
            "challenge_name": "Contact Rescue Team",
            "items":{

            }, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Contact Stranded Teammate": {
            "challenge_name": "Contact Stranded Teammate",
            "items":{

            }, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },

    

    "Environmental Obstacle": {
        "Arctic Bear": {
            "challenge_name": "Arctic Bear",
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
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Blizzard": {
            "challenge_name": "Blizzard",
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        "Cliff": {
            "challenge_name": "Cliff",
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Collosal Wave": {
            "challenge_name": "Collosal Wave",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""},
        
        "Crocodile": {
            "challenge_name": "Crocodile",
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
            "items":{

            }, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Deadly Insects": {
            "challenge_name": "Deadly Insects",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Extreme Heat": {
            "challenge_name": "Extreme Heat",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fallen Trees Block Path": {
            "challenge_name": "Fallen Trees Block Path",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fire": {
            "challenge_name": "Fire",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Flash Flood": {
            "challenge_name": "Flash Flood",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Frozen Lake": {
            "challenge_name": "Frozen Lake",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Heat Wave": {
            "challenge_name": "Heat Wave",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Ice Cliff": {
            "challenge_name": "Ice Cliff",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Mirages": {
            "challenge_name": "Mirages",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Nest of Scorpions": {
            "challenge_name": "Nest of Scorpions",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Rockfall": {
            "challenge_name": "Rockfall",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Dunes": {
            "challenge_name": "Sand Dunes",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Storm": {
            "challenge_name": "Sand Storm",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Shallow Reef": {
            "challenge_name": "Shallow Reef",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Shark Attack": {
            "challenge_name": "Shark Attack",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Underwater Earthquake": {
            "challenge_name": "Underwater Earthquake",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Venemous Snake": {
            "challenge_name": "Venemous Snake",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        }, 

        "Find Shelter": {
            "challenge_name": "Find Shelter",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Find Water": {
        "Get Water - Desert": {
            "challenge_name": "Get Water - Desert",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Water - Arctic Tundra": {
            "challenge_name": "Get Water - Arctic Tundra",
            "items":{
                "Ice Axes": {"use_desc": "You find a stumble across a frozen river. You use the ice axes to break through the thick ice and gain access to the flowing water beneath.", "point_value": 100, "point_desc": ""},
            }, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Water - Jungle": {
            "challenge_name": "Get Water - Jungle",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Water - Ocean": {
            "challenge_name": "Get Water - Ocean",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Water - Volcano": {
            "challenge_name": "Get Water - Volcano",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Getaway": {
        "Air Based Getaway": {
            "challenge_name": "Air Based Getaway",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Mislead Pursuers": {
            "challenge_name": "Mislead Pursuers",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Based Getaway": {
            "challenge_name": "Sand Based Getaway",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Snow Based Getaway": {
            "challenge_name": "Snow Based Getaway",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Use Stealth": {
            "challenge_name": "Use Stealth",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Water Based Getaway": {
            "challenge_name": "Water Based Getaway",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Make Repairs": {
        "Repair Collapsed Wall": {
            "challenge_name": "Repair Collapsed Wall",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Repair Enviro-Dome": {
            "challenge_name": "Repair Enviro-Dome",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Repair Exit Hatch": {
            "challenge_name": "Repair Exit Hatch",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Repair Rover": {
            "challenge_name": "Repair Rover",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Repair Solar Panels": {
            "challenge_name": "Repair Solar Panels",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Repair Vehicle": {
            "challenge_name": "Repair Vehicle",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    },



    "Manmade Obstacle": {
        "Blockade": {
            "challenge_name": "Blockade",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Building": {
            "challenge_name": "Building",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Checkpoint": {
            "challenge_name": "Checkpoint",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Collapsed Bridge": {
            "challenge_name": "Collapsed Bridge",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Fortefied Structure": {
            "challenge_name": "Fortefied Structure",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Giant Wall": {
            "challenge_name": "Giant Wall",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Pirates": {
            "challenge_name": "Pirates",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Sea Mines": {
            "challenge_name": "Sea Mine",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Ship Graveyard": {
            "challenge_name": "Ship Graveyard",
            "items":{}, 
            "failure_items": {},
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Traffic": {
            "challenge_name": "Traffic",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Deactivate Security Cameras": {
            "challenge_name": "Deactivate Security Cameras",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Distract Guards": {
            "challenge_name": "Distract Guards",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Sneak Through": {
            "challenge_name": "Sneak Through",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Get Past the Laser Grid": {
            "challenge_name": "Get Past the Laser Grid",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Open the crate": {
            "challenge_name": "Open the crate",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Pickpocket it": {
            "challenge_name": "Pickpocket it",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
        
        "Retrieve the Item from the Laser Grid": {
            "challenge_name": "Retrieve the Item from the Laser Grid",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Communications System Failure": {
            "challenge_name": "Communications System Failure",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Cooling Offline": {
            "challenge_name": "Cooling Offline",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Geo-Thermal Reactor Failure": {
            "challenge_name": "Geo-Thermal Reactor Failure",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Main Reactor Failure": {
            "challenge_name": "Main Reactor Failure",
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
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Land Based Travel": {
            "challenge_name": "Land Based Travel",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Sand Based Travel": {
            "challenge_name": "Sand Based Travel",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Snow Based Travel": {
            "challenge_name": "Snow Based Travel",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },

        "Water Based Travel": {
            "challenge_name": "Water Based Travel",
            "items":{}, 
            "failure_items": {}, 
            "desc": "", 
            "continue_failure_desc": "", 
            "final_failure_desc": ""
        },
    }
}



function get_mission(){
    const contents = document.getElementById("mission_contents");
    
    mission_location = possible_locations[Math.floor(Math.random() * possible_locations.length)];

    // Viable Missions for each location are stored inside each 
    viable_missions = [];

    for (var mission in mission_structures){
        if (mission_structures[mission][1][mission_location]){
            viable_missions.push(mission);
        }
    }

    selected_mission = viable_missions[Math.floor(Math.random() * viable_missions.length)]

    mission_challenges = mission_structures[selected_mission][2];


    selected_challenges = "\n";
    for (var challenge_type of mission_challenges){
        all_possible_challenges = location_challenges[mission_location][challenge_type];
        selected_challenges += "\n - " + all_possible_challenges[Math.floor(Math.random() * all_possible_challenges.length)];
    };

    contents.innerText = `
    Mission Location = ${mission_location}\n 
    Selected Mission = ${selected_mission}\n
    Mission Challenges: ${selected_challenges}\n
    `;

}



example_mission = {
    "location": "Jungle", 
    "mission": "Artifact Heist", 
    "challenge_1": {
        "challenge_name": "Deadly Marshland Gases",
        "items":{
            "Gas Mask and Knockout Gas": {"use_desc": "You wear the gas mask, protecting you from the dangerous marshland gases.", "point_value": 100, "point_desc": "The gas mask is ideal for situations just like this. It was the perfect tool to help you pass safely through the marshlands."},
            "Scuba Gear": {"use_desc": "Your team uses the scuba tanks and masks to breathe safely as make your way through the marshlands.", "point_value": 90, "point_desc": "The scuba gear is very effective and keeps your team safe. It is however, unwieldy and gets snagged on marshland plants and vines, slowing your progress."},
        },
        "failure_items": {
            "Fire Starter Kit": {"use_desc": "You use the fire starter to create a small flame. Within an instant, your entire team is wiped out.", "point_value": 0, "point_desc": "This is what we call a bad idea. Turns out those deadly gases were not only toxic, but also highly flammable. The ensuing fireball that consumed your team was so explosive that your first clue that anything went wrong would have been you, knocking on the pearly gates."}
        },
        "desc": "Your team comes across an expansive stretch of marshland that you will be forced to cross if you want to continue your mission. Unfortunately, pockets of the marshland are full of deadly gases, invisible to the human eye.", 
        "continue_failure_desc": "Your team is forced to navigate around the marshlands. This takes a significant amount of time and the longer trip significantly tires your team out.", 
        "final_failure_desc": "In desperation, your team tries to progress through the marshlands without the correct equipment. As the marshland gases slowly invade their systems, they find it harder and harder to stay awake. The exhaustion overtakes them and they rest for what they plan to only be a minute. They are claimed by the jungle."
    },
    "challenge_2": {
        "challenge_name": "Collapsed Bridge",
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
    "challenge_3": {
        "challenge_name": "Distract Guards",
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
    "challenge_4": {
        "challenge_name": "Retrieve the Item from the Laser Grid",
        "items":{
            "Mirror": {"use_desc": "You use the mirror to reflect the lasers away as one of you reaches in and grabs the insert_item_here.", "point_value": 100, "point_desc": "The mirror was an ingenious solution, efficient, clean, and it left the system intact, making it hard to notice that the insert_item_here had even been taken."},
            "Wire Cutters": {"use_desc": "You find the system that powers the laser grid and cut the wires. It deactivates the grid and you are able to grab the insert_item_here.", "point_value": 80, "point_desc": "You were successful in grabbing the insert_item_here, but there was evidence of your theft and the disappearence of the insert_item_here was quickly noticed."},
        }, 
        "failure_items": {},
        "desc": "You find the insert_item_here, but it's protected by a laser grid.", 
        "continue_failure_desc": "Your team attempts numerous solutions but remains unable to retrieve the item. You are forced to leave empty handed.", 
        "final_failure_desc": "Your team desperately tries to find a way past the lasers. Unfortunately, their exhaustion has made them sloppy, and they accidently trigger the laser system. In seconds the team is captured by armed guards. Your mission ends here."
    },
    "challenge_5": {
        "challenge_name": "Deadly Insects",
        "items":{
            "Fire Starter Kit": {"use_desc": "You use the fire starter kit to light a large branch on fire. Wielding the branch you are able to pass through, using the flame and smoke to keep the bugs at bay.", "point_value": 90, "point_desc": "The flame is able to easily deal with the swarm of bugs and is well suited to the task. Unfortunately a couple of bugs do get past, but their bites alone are not enough to inflict significant damage."},
            "Gas Mask and Knockout Gas": {"use_desc": "You use the knockout gas. It is too potent for the bugs to pass through. You use the gas mask to pass by unscathed.", "point_value": 100, "point_desc": "The gas is able to easily deal with the swarm of bugs and is well suited to the task."},
        }, 
        "failure_items": {},
        "desc": "Your team stumbles across swarm of deadly insects, all fairly intent upon biting you. You'll need to get past them to progress.", 
        "continue_failure_desc": "Your team is forced to navigate around the swarm. This takes a significant amount of time and the longer trip significantly tires your team out.", 
        "final_failure_desc": "In desperation your team attempts to make a run for it. Unfortunately they are unable to outrun the swarm and 1 bite turns into 100. They are claimed by the jungle."
    },
    "challenge_6": {
        "challenge_name": "Air Based Getaway",
        "items":{
            "Paraglider": {"use_desc": "Your team finds the highest point they can and paraglide silently away.", "point_value": 80, "point_desc": "The paragliders quickly put some distance between you and your would be pursuors. They are particularly effective due to how silently they move, but once you reach the forested jungle, they become cumbersome and impractical. Fortunately by that point you are pretty much in the clear."},
            "Helicopter": {"use_desc": "You quickly pile into the helicopter that is standing by and take off.", "point_value": 90, "point_desc": "The helicopter is very efficient at putting putting some distance between you and your would be pursuors. It is very loud, which alerts the guards to your presences, but fortunately you're out of there before they get the chance to follow you."},
        }, 
        "failure_items": {},
        "desc": "Your team is going to need to get away, and fast. The only way out, from your current position, is by air.", 
        "continue_failure_desc": "Your team is forced to make a run for it. You manage to evade your pursuors, but the trip tires your team significantly and takes a long time.", 
        "final_failure_desc": "Your team tries desperately to flee, but are too tired to escape by foot. It isn't long before your pursuors catch up to the team and take them captive. Your mission ends here."
    },
}

function get_example_mission(){
    return example_mission
}