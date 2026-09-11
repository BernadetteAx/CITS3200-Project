example_mission = {
    "location": "Jungle", 
    "mission": "Artifact Heist", 
    "challenge_1": {
        "challenge_name": "Deadly Marshland Gases",
        "viable_locations": ["Jungle"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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
    "challenge_2": {
        "challenge_name": "Collapsed Bridge",
        "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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
        "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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
        "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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
        "viable_locations": ["Jungle"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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
        "viable_locations": ["Arctic Tundra", "Desert", "Jungle", "City", "Ocean", "Volcano"],
        "viable_mission_types": ["Heist", "Escape", "Rescue Op", "Survival"],
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