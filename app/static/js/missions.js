possible_locations = ["Artic Tundra", "Desert", "Jungle", "City", "Ocean"]

mission_structures = {
    "Train Job":                ["Heist",      {"Artic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Steal",                "Manmade Obstacle",         "Getaway"               ]],
    "Artifact Heist":           ["Heist",      {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Steal",                "Environmental Obstacle",   "Getaway"               ]],
    "Jewel Heist":              ["Heist",      {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Steal",                "Manmade Obstacle",         "Getaway"               ]],
    "Steal Enemy Information":  ["Heist",      {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Environmental Obstacle",  "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Steal",                "Security Obstacle",        "Getaway"               ]],
    "Break Out Another Team":   ["Heist",      {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Travel To Rendezvouz",    "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Contact Teammate/s",   "Security Obstacle",        "Getaway"               ]],
    "Escape Enemy Base":        ["Escape",     {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Security Obstacle",       "Manmade Obstacle",         "Security Obstacle",        "Retrieve Item",        "Getaway",              "Contact Teammate/s",       "Travel To Rendezvouz"  ]],
    "Extract Another Team":     ["Rescue Op",  {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": false},    ["Contact Teammate/s",      "Environmental Obstacle",   "Travel To Rendezvouz",     "Retrieve Item",        "Getaway",              "Environmental Obstacle",   "Find Shelter"          ]],
    "Rescue Stranded Teammate": ["Rescue Op",  {"Artic Tundra": true,   "Desert": true,   "Jungle": false,  "City": false,   "Ocean": true},    ["System Failure",          "Find Shelter",             "Environmental Obstacle",   "Retrieve Item",        "Contact Teammate/s",   "Travel To Rendezvouz",     "Environmental Obstacle"]],
    "Repair Research Base":     ["Survival",   {"Artic Tundra": true,   "Desert": true,   "Jungle": false,  "City": false,   "Ocean": true},    ["Environmental Obstacle",  "SystemFailure",            "Environmental Obstacle",   "Retrieve Item",        "Make Repairs",         "Environmental Obstacle",   "Make Repairs"          ]],
    "Get Rescued":              ["Survival",   {"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": false,   "Ocean": true},    ["Environmental Obstacle",  "Find Water",               "Environmental Obstacle",   "Retrieve Item",        "Find Shelter",         "Contact Teammate/s",       "Travel To Rendezvouz"  ]],
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
Mission Name    | Mission Type  | Artic Tundra  | Desert    | Jungle    | City      | Ocean     | Challenge 1 Type      | Challenge 2 Type      | Challenge 3 Type      | Challenge 4 Type      | Challenge 5 Type      | Challenge 6 Type      | Challenge 6 Type      |
----------------|---------------|---------------|-----------|-----------|-----------|-----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
Articfact Heist | Heist         | true          | true      | true      | true      | false     |Environmental Obstacle | Manmade Obstacle      | Security Obstacle     | Steal                 | Steal                 |Environmental Obstacle | Getaway               |
...etc
*/


// Retrieve item challenges are an opportunity for teams to use one of their remaining items to obtain an item that will definitely help them in a coming challenge. 
// It always occurs halfway through the mission and before the highest weighted challenge

challenge_types = {
    "Retrieve Item": ["Break into Building", "Retrieve it", "Steal It From Someone"],
    "Environmental Obstacle": ["Sand Storm", "Snow Storm", "Fire", "Flash Flood", "Fallen Trees Block Path", "Heat Wave", "Ice Cliff", "Cliff", "Hurricane"],
    "Manmade Obstacle": ["Dam", "Giant Wall", "Checkpoint", "Blockade", "Collapsed Bridge", "Traffic", "Building", "Foretfied Structure"],
    "Getaway": ["Land Based Getaway", "Snow Based Getaway", "Water Based Getaway", "Air Based Getaway", "Use Stealth", "Mislead Pursuers"],
    "Security Obstacle": ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak In"],
    "Steal": ["Break into the Vault", "Open the crate", "Pickpocket it"],
    "Make Repairs": ["Repair Vehicle", "Repair Enviro-Dome", "Repair Collapsed Wall", "Repair Exit Hatch", "Repair Solar Panels"], 
    "System Failure": ["Central Heating Offline", "Cooling Offline", "Main Reactor Failure", "Communications System Failure", "Air Recycling System Offline"],
    "Find Water": ["Find Water"],
    "Find Shelter": ["Find Civilization", "Find Shelter"],
    "Contact Teammate/s": ["Contact Stranded Teammate", "Contact Rescue Team", "Alert Another Team"],
    "Travel To Rendezvouz": ["Land Based Travel", "Snow Based Travel", "Water Based Travel", "Air Based Travel", "Hitch a Ride"],
}

challenges = {
    // Retrieve Item
    "Break into Building":      [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Retrieve it":              [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Steal It From Someone":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Enviro 
    "Sand Storm":               [{"Artic Tundra": false,  "Desert": true,   "Jungle": false,  "City": true,   "Ocean": false},], 
    "Blizzard":                 [{"Artic Tundra": true,   "Desert": false,  "Jungle": false,  "City": true,   "Ocean": false},], 
    "Fire":                     [{"Artic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": false},], 
    "Flash Flood":              [{"Artic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": false},], 
    "Fallen Trees Block Path":  [{"Artic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": false},], 
    "Heat Wave":                [{"Artic Tundra": false,  "Desert": true,   "Jungle": false,  "City": true,   "Ocean": false},], 
    "Ice Cliff":                [{"Artic Tundra": true,   "Desert": false,  "Jungle": false,  "City": false,  "Ocean": false},], 
    "Cliff":                    [{"Artic Tundra": true,   "Desert": false,  "Jungle": true,   "City": false,  "Ocean": false},], 
    "Cyclone":                  [{"Artic Tundra": false,  "Desert": false,  "Jungle": true,   "City": true,   "Ocean": true},], 
    
    // Manmade
    "Dam":                  [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Giant Wall":           [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Checkpoint":           [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], "Blockade": [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Collapsed Bridge":     [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Traffic":              [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Building":             [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Foretfied Structure":  [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Getaways
    "Land Based Getaway":   [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Snow Based Getaway":   [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Water Based Getaway":  [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Air Based Getaway":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Use Stealth":          [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Mislead Pursuers":     [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Security
    "Deactivate Security Cameras":  [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Deactivate Alarms":            [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Distract Guards":              [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Find Another Entrance":        [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Sneak In":                     [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Steal
    "Break into the Vault": [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Open the crate":       [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Pickpocket it":        [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Repair
    "Repair Vehicle":           [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Repair Enviro-Dome":       [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Repair Collapsed Wall":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Repair Exit Hatch":        [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Repair Solar Panels":      [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // System Failure
    "Central Heating Offline":          [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Cooling Offline":                  [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Main Reactor Failure":             [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Communications System Failure":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Air Recycling System Offline":     [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Find water
    "Find Water":           [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Find Shelter
    "Find Civilization":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Find Shelter":         [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Contact
    "Contact Stranded Teammate":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Contact Rescue Team":          [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Alert Another Team":           [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],
    
    // Travel
    "Land Based Travel":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Snow Based Travel":    [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Water Based Travel":   [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Air Based Travel":     [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},], 
    "Hitch a Ride":         [{"Artic Tundra": true,   "Desert": true,   "Jungle": true,   "City": true,   "Ocean": true},],


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
        all_possible_challenges = challenge_types[challenge_type];
        selected_challenges += "\n - " + all_possible_challenges[Math.floor(Math.random() * all_possible_challenges.length)];
    };

    contents.innerText = `
    Mission Location = ${mission_location}\n 
    Selected Mission = ${selected_mission}\n
    Mission Challenges: ${selected_challenges}\n
    `;

}
