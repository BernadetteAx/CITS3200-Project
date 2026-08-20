possible_locations = ["Artic Tundra", "Desert", "Jungle", "City", "Ocean"]

// viable_missions_by_location = {
//     "Artic Tundra": ["Artifact Heist", "Jewel Heist", "Information Heist", "Repair Research Base", "Get Rescued", "Survive", "Rescue Stranded Teammate", "Escape Enemy Base"],
//     "Desert": ["Artifact Heist", "Jewel Heist", "Information Heist", "Repair Research Base", "Get Rescued", "Survive", "Rescue Stranded Teammate", "Escape Enemy Base"],
//     "Jungle": ["Artifact Heist", "Jewel Heist", "Information Heist", "Repair Research Base", "Get Rescued", "Survive", "Escape Enemy Base"], 
//     "City": ["Artifact Heist", "Jewel Heist", "Information Heist", "Escape Enemy Base"], 
//     "Ocean": ["Repair Research Base", "Get Rescued", "Survive", "Rescue Stranded Teammate"],
// }

/* If the mission is available in each location is indicated by a boolean. 
This was done to more closely match how a database might handle this
e.g A column that indicates if it is allowed in each location, so you can select only 
missions with a value in that location column of true 
Shown below Dict*/
mission_structures = {
    "Artifact Heist":           ["Heist",      [true,   true,   true,   true,   false], ["Environmental Obstacle", "Manmade Obstacle", "Security Obstacle", "Steal", "Manmade Obstacle", "Getaway"]],
    "Jewel Heist":              ["Heist",      [true,   true,   true,   true,   false], ["Environmental Obstacle", "Manmade Obstacle", "Security Obstacle", "Steal", "Manmade Obstacle", "Getaway"]],
    "Information Heist":        ["Heist",      [true,   true,   true,   true,   false], ["Environmental Obstacle", "Manmade Obstacle", "Security Obstacle", "Steal", "Manmade Obstacle", "Getaway"]],
    "Repair Research Base":     ["Survival",   [true,   true,   false,  false,  true],  ["Environmental Obstacle", "SystemFailure", "Environmental Obstacle", "Make Repairs", "Environmental Obstacle", "Make Repairs"]],
    "Get Rescued":              ["Survival",   [true,   true,   true,   false,  true],  ["Environmental Obstacle", "Find Water", "Environmental Obstacle", "Find Shelter", "Contact Rescuers", "Travel To Rendezvouz"]],
    "Rescue Stranded Teammate": ["Survival",   [true,   true,   false,  false,  true],  ["Travel To Rendezvouz", "Environmental Obstacle"]],
    "Escape Enemy Base":        ["NO IDEA",    [true,   true,   true,   true,   false], []],
}


/* As a database might look something like:
Mission Name    | Mission Type  | Artic Tundra  | Desert    | Jungle    | City      | Ocean     | Challenge 1 Type      | Challenge 2 Type      | Challenge 3 Type      | Challenge 4 Type      | Challenge 5 Type      | Challenge 6 Type      |
----------------|---------------|---------------|-----------|-----------|-----------|-----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
Articfact Heist | Heist         | true          | true      | true      | true      | false     | Environmental Obstacle| Manmade Obstacle      | Security Obstacle     | Steal                 | Manmade Obstacle      | Getaway               |
...etc
*/




challenge_types = {
    "Environmental Obstacle": [1],
    "Manmade Obstacle": [1],
    "Getaway": [1],
    "Security Obstacle": ["Deactivate Security Cameras", "Deactivate Alarms", "Distract Guards", "Find Another Entrance", "Sneak In"],
    "Steal": [1],
    "Make Repairs": [1], 
    "System Failure": [1],
    "Find Water": [1],
    "Find Shelter": [1],
    "Contact Rescuers": [1],
    "Travel To Rendezvouz": [1],
}


// challenges ={
//     "deactivate_security_cameras": []
// }

// items_dict = {}


function get_mission(){
    const contents = document.getElementById("mission_contents");

    location_value = Math.floor(Math.random() * possible_locations.length);
    
    mission_location = possible_locations[location_value];

    // Viable Missions for each location are stored inside each 
    viable_missions = [];

    for (var mission in mission_structures){
        if (mission_structures[mission][1][location_value]){
            viable_missions.push(mission);
        }
    }

    selected_mission = viable_missions[Math.floor(Math.random() * viable_missions.length)]

    mission_challenges = mission_structures[selected_mission][2];


    selected_challenges = "\n";
    for (var challenge_type of mission_challenges){
        
        console.log(challenge_type)
        selected_challenges += "\n - " + challenge_type;
    };

    contents.innerText = `
    Mission Location = ${mission_location}\n 
    Selected Mission = ${selected_mission}\n
    Mission Challenges: ${selected_challenges}\n
    `;

}
