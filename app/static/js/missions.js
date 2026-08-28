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
/* If the mission is available in each location is indicated by a boolean. 
This was done to more closely match how a database might handle this
e.g A column that indicates if it is allowed in each location, so you can select only 
missions with a value in that location column of true 
Shown in above Dict*/



/* As a table, it might look something like:
Mission Name    | Mission Type  | Arctic Tundra | Desert    | Jungle    | City      | Ocean     | Challenge 1 Type      | Challenge 2 Type      | Challenge 3 Type      | Challenge 4 Type      | Challenge 5 Type      | Challenge 6 Type      |
----------------|---------------|---------------|-----------|-----------|-----------|-----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
Artifact Heist  | Heist         | true          | true      | true      | true      | false     |Environmental Obstacle | Manmade Obstacle      | Security Obstacle     | Steal                 |Environmental Obstacle | Getaway               |
...etc
*/


// Retrieve item challenges are an opportunity for teams to use one of their remaining items to obtain an item that will definitely help them in a coming challenge. 
// It always occurs halfway through the mission and before the highest weighted challenge


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

    "Ice Axes": {"desc": "A...", "cost": 100},

    "Armoured Truck": {"desc": "A land based vehicle...", "cost": 600},
}


challenges = {
    "Contact Teammate/s": {
        "Alert Another Team": {
            "items":{
                "Fire Starter Kit": "You use the fire starter kit to make a small signal fire. The other team sees it and is alerted to your position.", 
                "Handheld Radios": "You use your handheld radios to get in call the the other team and alert them to your position.",
                "Mirror": "You use the mirror to reflect light in the direction of the other team. They see it and are able to track it back, alerting them to your position."
            }, 
            "desc": "To be able to continue your mission you are going to need to be able to alert the other team to your position.", 
            "failure_desc": ""},
        "Contact Rescue Team": {"items":{}, "desc": "", "failure_desc": ""},
        "Contact Stranded Teammate": {"items":{}, "desc": "", "failure_desc": ""}
    },

    

    "Environmental Obstacle": {
        "Arctic Bear": {
            "items":{
                "Gas Mask and Knockout Gas": "You use the knockout gas to harmlessly incapacitate the arctic bear and use the gas mask to slip by unscathed.",
                "Ice Axes": "You wield the ice axes as weapons. You land a hit and the arctic bear retreats.",
            }, "desc": "", "failure_desc": ""},
        
        "Ash": {"items":{}, "desc": "", "failure_desc": ""},
        "Blizzard": {"items":{}, "desc": "", "failure_desc": ""},
        "Cliff": {"items":{}, "desc": "", "failure_desc": ""},
        "Collosal Wave": {"items":{}, "desc": "", "failure_desc": ""},
        
        "Crocodile": {
            "items":{
                "Gas Mask and Knockout Gas": "You use the knockout gas to harmlessly incapacitate the Crocodile and use the gas mask to slip by unscathed.",
                "Ice Axes": "You wield the ice axes as weapons. You land a hit and the crocodile retreats.",
            }, "desc": "", "failure_desc": ""},
        
            "Cyclone": {"items":{}, "desc": "", "failure_desc": ""},
        
        "Deadly Insects": {
            "items":{
                "Fire Starter Kit": "You use the fire starter kit to light a large branch on fire. Wielding the branch you are able to pass through, using the flame and smoke to keep the bugs at bay.", 
                "Gas Mask and Knockout Gas": "You use the knockout gas. It is too potent for the bugs to pass through. You use the gas mask to pass by unscathed."
            }, "desc": "", "failure_desc": ""},
        
        "Earthquake": {"items":{}, "desc": "", "failure_desc": ""},
        "Extreme Heat": {"items":{}, "desc": "", "failure_desc": ""},
        "Fallen Trees Block Path": {"items":{}, "desc": "", "failure_desc": ""},
        "Fire": {"items":{}, "desc": "", "failure_desc": ""},
        "Flash Flood": {"items":{}, "desc": "", "failure_desc": ""},
        "Frozen Lake": {"items":{}, "desc": "", "failure_desc": ""},
        "Heat Wave": {"items":{}, "desc": "", "failure_desc": ""},

        "Ice Cliff": {
            "items":{
                "Ice Axes": "You use the Ice Axes to scale the ice cliff.",
            }, "desc": "", "failure_desc": ""},
        
        "Land Slide": {
            "items":{
                "Ice Axes": "You wedge the ice axes as deep into the surrounding rock as possible and hold on tight. After the landslide has past, you need to dig yourselves out, but you are otherwise fine.",
            }, "desc": "", "failure_desc": ""},
        
        "Lava Spout": {"items":{}, "desc": "", "failure_desc": ""},
        "Mirages": {"items":{}, "desc": "", "failure_desc": ""},
        
        "Nest of Scorpions": {
            "items":{
                "Fire Starter Kit": "You use the fire starter kit to create a small fire. You toss the smoking kindling into the nest and the smoke pacifies the scorpions allowing you to pass by unscathed.", 
                "Gas Mask and Knockout Gas": "You toss the knockout gas canister into the nest, the gas causes the scorpions to scatter allowing you to pass by unscathed."
            }, "desc": "", "failure_desc": ""},
        
        "Quick Sand": {
            "items":{
                "Ice Axes": "You use wedge the ice axes into the surrounding solid ground and use them to pull yourselves out.",
            }, 
            "desc": "", "failure_desc": ""},
        
        "River": {"items":{}, "desc": "", "failure_desc": ""},
        "Rockfall": {"items":{}, "desc": "", "failure_desc": ""},
        "Sand Dunes": {"items":{}, "desc": "", "failure_desc": ""},
        "Sand Storm": {"items":{}, "desc": "", "failure_desc": ""},
        "Shallow Reef": {"items":{}, "desc": "", "failure_desc": ""},
        "Shark Attack": {
            "items":{
                "Ice Axes": "You wield the ice axes as weapons. You land a hit and the shark retreats.",
            }, 
            "desc": "", "failure_desc": ""},

        "Deadly Marshland Gases": {
            "items":{
                "Gas Mask and Knockout Gas": "You wear the gas mask, protecting you from the dangerous marshland gases."
            }, "desc": "", "failure_desc": ""},
        
        "Temperature Drop": {"items":{}, "desc": "", "failure_desc": ""},
        "Underwater Earthquake": {"items":{}, "desc": "", "failure_desc": ""},
        
        "Venemous Snake": {
            "items":{
                "Fire Starter Kit": "You use the fire starter kit to create a small fire. You use the flame to keep the reptile at bay, and pass by unscathed.", 
                "Gas Mask and Knockout Gas": "You toss the knockout gas canister near the snake, harmlessly incapacitating it and you use the gas mask to slip by unscathed.",
            }, "desc": "", "failure_desc": ""},
        
            "Volcanic Gases": {
            "items":{
                "Gas Mask and Knockout Gas": "You wear the gas mask, protecting you from the dangerous fumes of the volcano."
            }, "desc": "", "failure_desc": ""},
    },

    "Find Shelter": {
        "Find Civilization": {"items":{}, "desc": "", "failure_desc": ""}, 
        "Find Shelter": {"items":{}, "desc": "", "failure_desc": ""}
    },

    "Find Water": {
        "Get Water - Desert": {"items":{}, "desc": "", "failure_desc": ""},
        "Get Water - Arctic Tundra": {
            "items":{
                "Ice Axes": "You find a stumble across a frozen river. You use the ice axes to break through the thick ice and gain access to the flowing water beneath.",
            }, "desc": "", "failure_desc": ""},
        "Get Water - Jungle": {"items":{}, "desc": "", "failure_desc": ""},
        "Get Water - Ocean": {"items":{}, "desc": "", "failure_desc": ""},
        "Get Water - Volcano": {"items":{}, "desc": "", "failure_desc": ""},
    },

    "Getaway": {
        "Air Based Getaway": {"items":{}, "desc": "", "failure_desc": ""},
        "Land Based Getaway": {"items":{}, "desc": "", "failure_desc": ""},
        "Mislead Pursuers": {"items":{}, "desc": "", "failure_desc": ""},
        "Sand Based Getaway": {"items":{}, "desc": "", "failure_desc": ""},
        "Snow Based Getaway": {"items":{}, "desc": "", "failure_desc": ""},
        "Use Stealth": {"items":{}, "desc": "", "failure_desc": ""},
        "Water Based Getaway": {"items":{}, "desc": "", "failure_desc": ""}
    },

    "Make Repairs": {
        "Repair Collapsed Wall": {"items":{}, "desc": "", "failure_desc": ""},
        "Repair Enviro-Dome": {"items":{}, "desc": "", "failure_desc": ""},
        "Repair Exit Hatch": {"items":{}, "desc": "", "failure_desc": ""},
        "Repair Rover": {"items":{}, "desc": "", "failure_desc": ""},
        "Repair Solar Panels": {"items":{}, "desc": "", "failure_desc": ""},
        "Repair Vehicle": {"items":{}, "desc": "", "failure_desc": ""}
    },

    "Manmade Obstacle": {
        "Blockade": {"items":{}, "desc": "", "failure_desc": ""},
        "Building": {"items":{}, "desc": "", "failure_desc": ""},
        "Checkpoint": {"items":{}, "desc": "", "failure_desc": ""},
        "Collapsed Bridge": {"items":{}, "desc": "", "failure_desc": ""},
        "Dam": {"items":{}, "desc": "", "failure_desc": ""},
        "Fortefied Structure": {"items":{}, "desc": "", "failure_desc": ""},
        "Giant Wall": {"items":{}, "desc": "", "failure_desc": ""},
        "Pirates": {"items":{}, "desc": "", "failure_desc": ""},
        "Sea Mines": {"items":{}, "desc": "", "failure_desc": ""},
        "Ship Graveyard": {"items":{}, "desc": "", "failure_desc": ""},
        "Traffic": {"items":{}, "desc": "", "failure_desc": ""}
    },

    "Security Obstacle": {
        "Deactivate Alarms": {"items":{}, "desc": "", "failure_desc": ""},
        "Deactivate Security Cameras": {"items":{}, "desc": "", "failure_desc": ""},
        "Distract Guards": {
            "items":{
                "Fire Starter Kit": "You use the fire starter kit to make a small fire. The smoke attracts the attention of the guards and they leave their post to investigate.",
                "Handheld Radios": "You leave one of the handheld radios at your current position and move a distance away, calling it from your new position. The noise attracts the attention of the guards and they leave their post to investigate.",
                "Mirror": "You leave the mirror at your current position and move a distance away. The glint of the mirror attracts the attention of the guards and they leave their post to investigate.",
                "Gas Mask and Knockout Gas": "You toss the knockout gas canister towards the guards, knocking them out. You use the gas mask to slip past."
            }, 
            "desc": "", 
            "failure_desc": ""},
        "Find Another Entrance": {"items":{}, "desc": "", "failure_desc": ""},
        "Sneak Through": {"items":{}, "desc": "", "failure_desc": ""},
        "Get Past the Laser Grid": {"items":{}, "desc": "", "failure_desc": ""},
    },

    "Steal": {
        "Break into the Vault": {"items":{}, "desc": "", "failure_desc": ""},
        "Open the crate": {"items":{}, "desc": "", "failure_desc": ""},
        "Pickpocket it": {"items":{}, "desc": "", "failure_desc": ""},
        "Retrieve the Item from the Laser Grid": {"items":{}, "desc": "", "failure_desc": ""},
    },

    "System Failure": {
        "Air Recycling System Offline": {
            "items":{
                "Gas Mask and Knockout Gas": "You wear the gas mask, filtering the air and making it breathable."
            }, "desc": "", "failure_desc": ""},
        "Central Heating Offline": {"items":{}, "desc": "", "failure_desc": ""},
        "Communications System Failure": {"items":{}, "desc": "", "failure_desc": ""},
        "Cooling Offline": {"items":{}, "desc": "", "failure_desc": ""},
        "Geo-Thermal Reactor Failure": {"items":{}, "desc": "", "failure_desc": ""},
        "Main Reactor Failure": {"items":{}, "desc": "", "failure_desc": ""}
    },

    "Travel To Rendezvouz": {
        "Air Based Travel": {"items":{}, "desc": "", "failure_desc": ""},
        "Land Based Travel": {"items":{}, "desc": "", "failure_desc": ""},
        "Sand Based Travel": {"items":{}, "desc": "", "failure_desc": ""},
        "Snow Based Travel": {"items":{}, "desc": "", "failure_desc": ""},
        "Water Based Travel": {"items":{}, "desc": "", "failure_desc": ""}
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

    // mission_type = 

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
