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
        "Environmental Obstacle":   ["Blizzard", "Temperature Drop", "Frozen Lake", "Ice Cliff", "Cliff", "Bear"],
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Fortefied Structure"],
        "Getaway":                  ["Land Based Getaway", "Snow Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it"],
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
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Solar Panels"], 
        "System Failure":           ["Cooling Offline", "Main Reactor Failure", "Communications System Failure"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Sand Based Travel", "Air Based Travel"],
    },  

    "Jungle": {
        "Environmental Obstacle":   ["Fire", "Flash Flood", "River", "Fallen Trees Block Path", "Quick Sand", "Cliff", "Cyclone", "Swamp", "Deadly Insects", "Crocodile"],
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Fortefied Structure"],
        "Getaway":                  ["Land Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it"],
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
        "Security Obstacle":        ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak Through"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it"],
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
        "Security Obstacle":        ["Distract Guards", "Find Another Entrance", "Sneak Through"],
        "Steal":                    ["Break into the Vault", "Open the crate", "Pickpocket it"],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Exit Hatch", "Repair Solar Panels"], 
        "System Failure":           ["Central Heating Offline", "Main Reactor Failure", "Communications System Failure", "Air Recycling System Offline"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Water Based Travel", "Air Based Travel"],
    },

    "Volcano": {
        "Environmental Obstacle":   ["Earthquake", "Eruption"],
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





challenges = {
    'Contact Teammate/s': {
        'Alert Another Team': {"items":{}, "desc": "", "failure_desc": ""},
        'Contact Rescue Team': {"items":{}, "desc": "", "failure_desc": ""},
        'Contact Stranded Teammate': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Environmental Obstacle': {
        'Bear': {"items":{}, "desc": "", "failure_desc": ""},
        'Blizzard': {"items":{}, "desc": "", "failure_desc": ""},
        'Cliff': {"items":{}, "desc": "", "failure_desc": ""},
        'Collosal Wave': {"items":{}, "desc": "", "failure_desc": ""},
        'Crocodile': {"items":{}, "desc": "", "failure_desc": ""},
        'Cyclone': {"items":{}, "desc": "", "failure_desc": ""},
        'Deadly Insects': {"items":{}, "desc": "", "failure_desc": ""},
        'Earthquake': {"items":{}, "desc": "", "failure_desc": ""},
        'Eruption': {"items":{}, "desc": "", "failure_desc": ""},
        'Fallen Trees Block Path': {"items":{}, "desc": "", "failure_desc": ""},
        'Fire': {"items":{}, "desc": "", "failure_desc": ""},
        'Flash Flood': {"items":{}, "desc": "", "failure_desc": ""},
        'Frozen Lake': {"items":{}, "desc": "", "failure_desc": ""},
        'Heat Wave': {"items":{}, "desc": "", "failure_desc": ""},
        'Ice Cliff': {"items":{}, "desc": "", "failure_desc": ""},
        'Mirages': {"items":{}, "desc": "", "failure_desc": ""},
        'Nest of Scorpions': {"items":{}, "desc": "", "failure_desc": ""},
        'Quick Sand': {"items":{}, "desc": "", "failure_desc": ""},
        'River': {"items":{}, "desc": "", "failure_desc": ""},
        'Sand Dunes': {"items":{}, "desc": "", "failure_desc": ""},
        'Sand Storm': {"items":{}, "desc": "", "failure_desc": ""},
        'Shallow Reef': {"items":{}, "desc": "", "failure_desc": ""},
        'Shark Attack': {"items":{}, "desc": "", "failure_desc": ""},
        'Swamp': {"items":{}, "desc": "", "failure_desc": ""},
        'Temperature Drop': {"items":{}, "desc": "", "failure_desc": ""},
        'Underwater Earthquake': {"items":{}, "desc": "", "failure_desc": ""},
        'Venemous Snake': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Find Shelter': {
        'Find Civilization': {"items":{}, "desc": "", "failure_desc": ""}, 
        'Find Shelter': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Find Water': {
        'Find Water': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Getaway': {
        'Air Based Getaway': {"items":{}, "desc": "", "failure_desc": ""},
        'Land Based Getaway': {"items":{}, "desc": "", "failure_desc": ""},
        'Mislead Pursuers': {"items":{}, "desc": "", "failure_desc": ""},
        'Sand Based Getaway': {"items":{}, "desc": "", "failure_desc": ""},
        'Snow Based Getaway': {"items":{}, "desc": "", "failure_desc": ""},
        'Use Stealth': {"items":{}, "desc": "", "failure_desc": ""},
        'Water Based Getaway': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Make Repairs': {
        'Repair Collapsed Wall': {"items":{}, "desc": "", "failure_desc": ""},
        'Repair Enviro-Dome': {"items":{}, "desc": "", "failure_desc": ""},
        'Repair Exit Hatch': {"items":{}, "desc": "", "failure_desc": ""},
        'Repair Rover': {"items":{}, "desc": "", "failure_desc": ""},
        'Repair Solar Panels': {"items":{}, "desc": "", "failure_desc": ""},
        'Repair Vehicle': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Manmade Obstacle': {
        'Blockade': {"items":{}, "desc": "", "failure_desc": ""},
        'Building': {"items":{}, "desc": "", "failure_desc": ""},
        'Checkpoint': {"items":{}, "desc": "", "failure_desc": ""},
        'Collapsed Bridge': {"items":{}, "desc": "", "failure_desc": ""},
        'Dam': {"items":{}, "desc": "", "failure_desc": ""},
        'Fortefied Structure': {"items":{}, "desc": "", "failure_desc": ""},
        'Giant Wall': {"items":{}, "desc": "", "failure_desc": ""},
        'Pirates': {"items":{}, "desc": "", "failure_desc": ""},
        'Sea Mines': {"items":{}, "desc": "", "failure_desc": ""},
        'Ship Graveyard': {"items":{}, "desc": "", "failure_desc": ""},
        'Traffic': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Security Obstacle': {
        'Deactivate Alarms': {"items":{}, "desc": "", "failure_desc": ""},
        'Deactivate Security Cameras': {"items":{}, "desc": "", "failure_desc": ""},
        'Distract Guards': {"items":{}, "desc": "", "failure_desc": ""},
        'Find Another Entrance': {"items":{}, "desc": "", "failure_desc": ""},
        'Sneak Through': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Steal': {
        'Break into the Vault': {"items":{}, "desc": "", "failure_desc": ""},
        'Open the crate': {"items":{}, "desc": "", "failure_desc": ""},
        'Pickpocket it': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'System Failure': {
        'Air Recycling System Offline': {"items":{}, "desc": "", "failure_desc": ""},
        'Central Heating Offline': {"items":{}, "desc": "", "failure_desc": ""},
        'Communications System Failure': {"items":{}, "desc": "", "failure_desc": ""},
        'Cooling Offline': {"items":{}, "desc": "", "failure_desc": ""},
        'Geo-Thermal Reactor Failure': {"items":{}, "desc": "", "failure_desc": ""},
        'Main Reactor Failure': {"items":{}, "desc": "", "failure_desc": ""}
    },

    'Travel To Rendezvouz': {
        'Air Based Travel': {"items":{}, "desc": "", "failure_desc": ""},
        'Land Based Travel': {"items":{}, "desc": "", "failure_desc": ""},
        'Sand Based Travel': {"items":{}, "desc": "", "failure_desc": ""},
        'Snow Based Travel': {"items":{}, "desc": "", "failure_desc": ""},
        'Water Based Travel': {"items":{}, "desc": "", "failure_desc": ""}
    }
}



function get_mission(){
    const contents = document.getElementById("mission_contents");
    
    mission_location = possible_locations[Math.floor(Math.random() * possible_locations.length)];

    // Viable Missions for each location are stored inside each 
    viable_missions = {"items":{}, "desc": "", "failure_desc": ""};

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
