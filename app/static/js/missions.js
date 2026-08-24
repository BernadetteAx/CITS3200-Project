possible_locations = ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"]

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
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Foretfied Structure"],
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
        "Manmade Obstacle":         ["Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Foretfied Structure"],
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
        "Manmade Obstacle":         ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Building", "Foretfied Structure"],
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
        "Manmade Obstacle":         [1],
        "Getaway":                  [1],
        "Security Obstacle":        [1],
        "Steal":                    [1],
        "Make Repairs":             ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Exit Hatch", "Repair Rover"], 
        "System Failure":           ["Cooling Offline", "Geo-Thermal Reactor Failure", "Communications System Failure", "Air Recycling System Offline"],
        "Find Water":               ["Find Water"],
        "Find Shelter":             ["Find Civilization", "Find Shelter"],
        "Contact Teammate/s":       ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
        "Travel To Rendezvouz":     ["Land Based Travel", "Air Based Travel"],
    },

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
