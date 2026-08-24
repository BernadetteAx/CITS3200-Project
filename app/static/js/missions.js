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
        "Environmental Obstacle": {
            "Blizzard":{"items": [], "description": [], "failure_description":[]}, 
            "Temperature Drop":{"items": [], "description": [], "failure_description":[]}, 
            "Frozen Lake":{"items": [], "description": [], "failure_description":[]}, 
            "Ice Cliff":{"items": [], "description": [], "failure_description":[]}, 
            "Cliff":{"items": [], "description": [], "failure_description":[]}, 
            "Bear":{"items": [], "description": [], "failure_description":[]}
        },
        "Manmade Obstacle":         {"Dam":{"items": [], "description": [], "failure_description":[]}, "Giant Wall":{"items": [], "description": [], "failure_description":[]}, "Checkpoint":{"items": [], "description": [], "failure_description":[]}, "Blockade":{"items": [], "description": [], "failure_description":[]}, "Collapsed Bridge":{"items": [], "description": [], "failure_description":[]}, "Building":{"items": [], "description": [], "failure_description":[]}, "Foretfied Structure":{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {"Land Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Snow Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Water Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Air Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Use Stealth":{"items": [], "description": [], "failure_description":[]}, "Mislead Pursuers":{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {"Deactivate Security Cameras":{"items": [], "description": [], "failure_description":[]}, "Deactivate Alarms":{"items": [], "description": [], "failure_description":[]}, "Distract Guards":{"items": [], "description": [], "failure_description":[]}, "Find Another Entrance":{"items": [], "description": [], "failure_description":[]}, "Sneak Through":{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {"Break into the Vault":{"items": [], "description": [], "failure_description":[]}, "Open the crate":{"items": [], "description": [], "failure_description":[]}, "Pickpocket it":{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Enviro-Dome":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Central Heating Offline":{"items": [], "description": [], "failure_description":[]}, "Main Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Civilization":{"items": [], "description": [], "failure_description":[]}, "Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Land Based Travel":{"items": [], "description": [], "failure_description":[]}, "Snow Based Travel":{"items": [], "description": [], "failure_description":[]}, "Water Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
    },  

    "Desert": {
        "Environmental Obstacle":   {"Sand Storm":{"items": [], "description": [], "failure_description":[]}, "Heat Wave":{"items": [], "description": [], "failure_description":[]}, "Venemous Snake":{"items": [], "description": [], "failure_description":[]}, "Sand Dunes":{"items": [], "description": [], "failure_description":[]}, "Quick Sand":{"items": [], "description": [], "failure_description":[]}, "Mirages":{"items": [], "description": [], "failure_description":[]}, "Nest of Scorpions":{"items": [], "description": [], "failure_description":[]}},
        "Manmade Obstacle":         {"Giant Wall":{"items": [], "description": [], "failure_description":[]}, "Checkpoint":{"items": [], "description": [], "failure_description":[]}, "Blockade":{"items": [], "description": [], "failure_description":[]}, "Collapsed Bridge":{"items": [], "description": [], "failure_description":[]}, "Building":{"items": [], "description": [], "failure_description":[]}, "Foretfied Structure":{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {"Land Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Sand Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Air Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Use Stealth":{"items": [], "description": [], "failure_description":[]}, "Mislead Pursuers":{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {"Deactivate Security Cameras":{"items": [], "description": [], "failure_description":[]}, "Deactivate Alarms":{"items": [], "description": [], "failure_description":[]}, "Distract Guards":{"items": [], "description": [], "failure_description":[]}, "Find Another Entrance":{"items": [], "description": [], "failure_description":[]}, "Sneak Through":{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {"Break into the Vault":{"items": [], "description": [], "failure_description":[]}, "Open the crate":{"items": [], "description": [], "failure_description":[]}, "Pickpocket it":{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Enviro-Dome":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}, "Repair Solar Panels":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Cooling Offline":{"items": [], "description": [], "failure_description":[]}, "Main Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Civilization":{"items": [], "description": [], "failure_description":[]}, "Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Land Based Travel":{"items": [], "description": [], "failure_description":[]}, "Sand Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
    },  

    "Jungle": {
        "Environmental Obstacle":   {"Fire":{"items": [], "description": [], "failure_description":[]}, "Flash Flood":{"items": [], "description": [], "failure_description":[]}, "River":{"items": [], "description": [], "failure_description":[]}, "Fallen Trees Block Path":{"items": [], "description": [], "failure_description":[]}, "Quick Sand":{"items": [], "description": [], "failure_description":[]}, "Cliff":{"items": [], "description": [], "failure_description":[]}, "Cyclone":{"items": [], "description": [], "failure_description":[]}, "Swamp":{"items": [], "description": [], "failure_description":[]}, "Deadly Insects":{"items": [], "description": [], "failure_description":[]}, "Crocodile":{"items": [], "description": [], "failure_description":[]}},
        "Manmade Obstacle":         {"Dam":{"items": [], "description": [], "failure_description":[]}, "Giant Wall":{"items": [], "description": [], "failure_description":[]}, "Checkpoint":{"items": [], "description": [], "failure_description":[]}, "Blockade":{"items": [], "description": [], "failure_description":[]}, "Collapsed Bridge":{"items": [], "description": [], "failure_description":[]}, "Building":{"items": [], "description": [], "failure_description":[]}, "Foretfied Structure":{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {"Land Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Water Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Air Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Use Stealth":{"items": [], "description": [], "failure_description":[]}, "Mislead Pursuers":{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {"Deactivate Security Cameras":{"items": [], "description": [], "failure_description":[]}, "Deactivate Alarms":{"items": [], "description": [], "failure_description":[]}, "Distract Guards":{"items": [], "description": [], "failure_description":[]}, "Find Another Entrance":{"items": [], "description": [], "failure_description":[]}, "Sneak Through":{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {"Break into the Vault":{"items": [], "description": [], "failure_description":[]}, "Open the crate":{"items": [], "description": [], "failure_description":[]}, "Pickpocket it":{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Enviro-Dome":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Main Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Civilization":{"items": [], "description": [], "failure_description":[]}, "Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Land Based Travel":{"items": [], "description": [], "failure_description":[]}, "Water Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
    },   

    "City": {
        "Environmental Obstacle":   {"Sand Storm":{"items": [], "description": [], "failure_description":[]}, "Blizzard":{"items": [], "description": [], "failure_description":[]}, "Temperature Drop":{"items": [], "description": [], "failure_description":[]}, "Fire":{"items": [], "description": [], "failure_description":[]}, "Flash Flood":{"items": [], "description": [], "failure_description":[]}, "River":{"items": [], "description": [], "failure_description":[]}, "Fallen Trees Block Path":{"items": [], "description": [], "failure_description":[]}, "Heat Wave":{"items": [], "description": [], "failure_description":[]}, "Cyclone":{"items": [], "description": [], "failure_description":[]}},
        "Manmade Obstacle":         {"Dam":{"items": [], "description": [], "failure_description":[]}, "Giant Wall":{"items": [], "description": [], "failure_description":[]}, "Checkpoint":{"items": [], "description": [], "failure_description":[]}, "Blockade":{"items": [], "description": [], "failure_description":[]}, "Collapsed Bridge":{"items": [], "description": [], "failure_description":[]}, "Traffic":{"items": [], "description": [], "failure_description":[]}, "Building":{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {"Land Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Water Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Air Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Use Stealth":{"items": [], "description": [], "failure_description":[]}, "Mislead Pursuers":{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {"Deactivate Security Cameras":{"items": [], "description": [], "failure_description":[]}, "Deactivate Alarms":{"items": [], "description": [], "failure_description":[]}, "Distract Guards":{"items": [], "description": [], "failure_description":[]}, "Find Another Entrance":{"items": [], "description": [], "failure_description":[]}, "Sneak Through":{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {"Break into the Vault":{"items": [], "description": [], "failure_description":[]}, "Open the crate":{"items": [], "description": [], "failure_description":[]}, "Pickpocket it":{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}, "Repair Solar Panels":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Central Heating Offline":{"items": [], "description": [], "failure_description":[]}, "Cooling Offline":{"items": [], "description": [], "failure_description":[]}, "Main Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Land Based Travel":{"items": [], "description": [], "failure_description":[]}, "Water Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
    },   

    "Ocean": {
        "Environmental Obstacle":   {"Cyclone":{"items": [], "description": [], "failure_description":[]}, "Collosal Wave":{"items": [], "description": [], "failure_description":[]}, "Shark Attack":{"items": [], "description": [], "failure_description":[]}, "Underwater Earthquake":{"items": [], "description": [], "failure_description":[]}, "Shallow Reef":{"items": [], "description": [], "failure_description":[]}},
        "Manmade Obstacle":         {"Blockade":{"items": [], "description": [], "failure_description":[]}, "Sea Mines":{"items": [], "description": [], "failure_description":[]}, "Ship Graveyard":{"items": [], "description": [], "failure_description":[]}, "Pirates":{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {"Water Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Air Based Getaway":{"items": [], "description": [], "failure_description":[]}, "Use Stealth":{"items": [], "description": [], "failure_description":[]}, "Mislead Pursuers":{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {"Distract Guards":{"items": [], "description": [], "failure_description":[]}, "Find Another Entrance":{"items": [], "description": [], "failure_description":[]}, "Sneak Through":{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {"Break into the Vault":{"items": [], "description": [], "failure_description":[]}, "Open the crate":{"items": [], "description": [], "failure_description":[]}, "Pickpocket it":{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Enviro-Dome":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}, "Repair Exit Hatch":{"items": [], "description": [], "failure_description":[]}, "Repair Solar Panels":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Central Heating Offline":{"items": [], "description": [], "failure_description":[]}, "Main Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}, "Air Recycling System Offline":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Civilization":{"items": [], "description": [], "failure_description":[]}, "Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Water Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
    },

    "Volcano": {
        "Environmental Obstacle":   {"Earthquake":{"items": [], "description": [], "failure_description":[]}, "Eruption":{"items": [], "description": [], "failure_description":[]}},
        "Manmade Obstacle":         {1:{"items": [], "description": [], "failure_description":[]}},
        "Getaway":                  {1:{"items": [], "description": [], "failure_description":[]}},
        "Security Obstacle":        {1:{"items": [], "description": [], "failure_description":[]}},
        "Steal":                    {1:{"items": [], "description": [], "failure_description":[]}},
        "Make Repairs":             {"Repair Vehicle":{"items": [], "description": [], "failure_description":[]}, "Repair Enviro-Dome":{"items": [], "description": [], "failure_description":[]}, "Repair Collapsed Wall":{"items": [], "description": [], "failure_description":[]}, "Repair Exit Hatch":{"items": [], "description": [], "failure_description":[]}, "Repair Rover":{"items": [], "description": [], "failure_description":[]}}, 
        "System Failure":           {"Cooling Offline":{"items": [], "description": [], "failure_description":[]}, "Geo-Thermal Reactor Failure":{"items": [], "description": [], "failure_description":[]}, "Communications System Failure":{"items": [], "description": [], "failure_description":[]}, "Air Recycling System Offline":{"items": [], "description": [], "failure_description":[]}},
        "Find Water":               {"Find Water":{"items": [], "description": [], "failure_description":[]}},
        "Find Shelter":             {"Find Civilization":{"items": [], "description": [], "failure_description":[]}, "Find Shelter":{"items": [], "description": [], "failure_description":[]}},
        "Contact Teammate/s":       {"Contact Stranded Teammate":{"items": [], "description": [], "failure_description":[]}, "Contact Rescue Team":{"items": [], "description": [], "failure_description":[]}, "Alert Another Team":{"items": [], "description": [], "failure_description":[]}},
        "Travel To Rendezvouz":     {"Land Based Travel":{"items": [], "description": [], "failure_description":[]}, "Air Based Travel":{"items": [], "description": [], "failure_description":[]}},
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
        all_possible_challenges = Object.keys(location_challenges[mission_location][challenge_type]);
        selected_challenges += "\n - " + all_possible_challenges[Math.floor(Math.random() * all_possible_challenges.length)];
    };

    contents.innerText = `
    Mission Location = ${mission_location}\n 
    Selected Mission = ${selected_mission}\n
    Mission Challenges: ${selected_challenges}\n
    `;

}
