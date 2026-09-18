document.addEventListener("DOMContentLoaded", () => {
    const missionTitle = document.getElementById("missionTitle");
    const missionLocation = document.getElementById("missionLocation");
    const missionDescription = document.getElementById("missionDescription");
    const typingCursor = document.getElementById("typingCursor");
    const continueBtn = document.getElementById("continueAuctionBtn");

    let briefingLoaded = false;
    let typingFinished = false;
    let isHost = sessionStorage.getItem("isHost") === "true";

    // Ask the server for the mission assigned to this game.
    function requestBriefing() {
        window.gameSocket.emit("get_mission_description", {
            sessionCode: window.getSessionCode(),
            playerId: window.getPlayerId()
        });
    }
    window.gameSocket.on("joined", requestBriefing);
    if (window.gameSocket.connected && window.getPlayerId()) requestBriefing();

    function updateContinueButton() {
        continueBtn.disabled = !typingFinished || !isHost;
        continueBtn.textContent = isHost ? "CONTINUE TO ITEM SHOP" : "WAITING FOR HOST";
    }

    window.gameSocket.on("host_changed", (data) => {
        isHost = data.hostId === window.getPlayerId();
        updateContinueButton();
    });

    window.gameSocket.on("mission_description_state", (data) => {
        if (briefingLoaded) return;
        briefingLoaded = true;

        missionTitle.textContent = data.mission.toUpperCase();
        missionLocation.textContent = data.location.toUpperCase();

        isHost = data.isHost;
        buildVisualStory(data);
        typeMissionDescription(data.description);
    });

    function typeMissionDescription(text) {
        let index = 0;
        missionDescription.textContent = "";

        if (!window.gameVisuals.motionEnabled() || !text) {
            missionDescription.textContent = text || "";
            typingCursor.style.display = "none";
            typingFinished = true;
            updateContinueButton();
            return;
        }

        const typingInterval = setInterval(() => {
            missionDescription.textContent += text.charAt(index);
            index++;

            if (index >= text.length) {
                clearInterval(typingInterval);

                typingCursor.style.display = "none";

                typingFinished = true;
                updateContinueButton();
            }
        }, 10);
    }

    continueBtn.addEventListener("click", () => {
        if (continueBtn.disabled) return;

        window.gameSocket.emit("begin_auction", {
            sessionCode: window.getSessionCode(),
            playerId: window.getPlayerId()
        });
    });

    window.gameSocket.on("auction_started", () => {
        window.location.href = "/auction";
    });

    // Atlas cells follow the six locations, then the ten mission objectives.
    const locations = {
        "Arctic Tundra": { cell: 0, title: "Into the frozen unknown", caption: "Snow-covered ridges stretch towards the horizon. Your mission takes the team into the heart of the arctic tundra." },
        "Desert": { cell: 1, title: "Beyond the dunes", caption: "A remote outpost lies beyond the sand. Your team is heading into the middle of the scorching desert." },
        "Jungle": { cell: 2, title: "Deep in the green", caption: "Dense foliage and mist conceal what lies ahead. Your mission takes place deep in the heart of the jungle." },
        "City": { cell: 3, title: "Under the city lights", caption: "Behind the skyline, your objective awaits. Your team must navigate a mission in the very heart of the city." },
        "Ocean": { cell: 4, title: "Far from the shore", caption: "Open water surrounds the expedition. Hundreds of miles out to sea, your team will have to rely on one another." },
        "Volcano": { cell: 5, title: "On the edge of the crater", caption: "Lava lights the slopes below. Your team is heading halfway down the crater of a volcano." }
    };
    const objectives = {
        "Train Heist": { cell: 6, title: "Catch the cargo", caption: "A rival's valuable cargo is on the move. Board the train, secure the goods and deliver them to your employer.", plan: "Choose equipment for a moving-train heist and a safe getaway. The cargo needs to reach your employer." },
        "Artifact Heist": { cell: 7, title: "Take back the artifact", caption: "A stolen artifact is hidden inside a fortified base. Get through its defences and return it to its rightful owners.", plan: "Plan a way into the fortified base and a way back out. Choose supplies that help your team retrieve the artifact." },
        "Jewel Heist": { cell: 8, title: "A gem behind the defences", caption: "A valuable jewel sits inside a heavily protected museum. Its harmless-looking exterior hides a serious security problem.", plan: "Think about obstacles, security and your escape before buying equipment. The jewel is only the beginning of the getaway." },
        "Steal Enemy Information": { cell: 9, title: "Find the enemy files", caption: "Your government needs vital information. Break into a secure military complex, take the files and get back out.", plan: "Prepare to enter a secure complex and leave with the files. Pick equipment for both infiltration and escape." },
        "Escape Enemy Base": { cell: 10, title: "Find a way out", caption: "Your team wakes up inside an enemy facility with no memory of how you got there. Escape, contact help and make a daring getaway.", plan: "Choose tools to overcome locked routes and contact someone who can rescue you. Getting outside is only part of the escape." },
        "Break Out Another Team": { cell: 11, title: "The pickup has gone quiet", caption: "Another team was due at your rendezvous, but contact has stopped. Reach the meeting point and be ready if the extraction goes wrong.", plan: "Prepare for a rendezvous that could become a rescue. Your equipment must help you reach the team and bring them home." },
        "Extract Another Team": { cell: 12, title: "Bring the researchers home", caption: "A research team went missing after a violent storm. Find them deep in the field and get them to safety.", plan: "Plan for rough travel, lost communications and an extraction. Choose supplies that help both your team and the missing researchers." },
        "Rescue Stranded Teammate": { cell: 13, title: "One teammate is still out there", caption: "A storm has damaged your base and stranded a researcher. Repair what you can and reach your missing teammate before exposure takes its toll.", plan: "Balance base repairs with a rescue in hostile conditions. Choose equipment that keeps the team moving and helps you find your teammate." },
        "Repair Research Base": { cell: 14, title: "Get the systems back online", caption: "The storm has left vital systems offline. Work together to repair the research base before your team's work is lost.", plan: "Prioritise the tools and supplies needed to restore the base. Your team's research depends on getting its vital systems running again." },
        "Get Rescued": { cell: 15, title: "Make contact. Stay alive.", caption: "Your base has been destroyed by a storm. With supplies gone, your team must find a way to get rescued before exposure claims you.", plan: "Think about water, shelter, communication and reaching help. Use the shared budget to give your team a way home." }
    };
    const art = document.getElementById("storyArt");
    const chapters = [...document.querySelectorAll(".story-chapter")];
    const play = document.getElementById("storyPlay");
    let story = [];
    let missionData = null;
    let objectiveView = 0;

    function buildVisualStory(data) {
        missionData = data;
        objectiveView = window.gameVisuals.nextVariant(`objective-${data.location}-${data.mission}`, 2);
        const location = locations[data.location];
        const objective = objectives[data.mission];
        // Unknown future missions retain an accurate preparation illustration.
        story = [
            { ...(location || { title: data.location, caption: "Explore the mission location described in your briefing." }), eyebrow: "01 / THE LOCATION", label: data.location, alt: `Pixel-art illustration of your team approaching the ${data.location.toLowerCase()} mission location.` },
            { ...(objective || { title: data.mission, caption: "Read the briefing to learn your team's objective." }), eyebrow: "02 / THE OBJECTIVE", label: data.mission, alt: `Pixel-art concept illustration for ${data.mission}: ${objective ? objective.caption : "a team planning its mission"}` },
            { title: "Good plans start together", caption: `${objective ? objective.plan : "Discuss the mission and choose your equipment together."} You have $1,000 to spend as a team in the item shop.`, eyebrow: "03 / PREPARE YOUR TEAM", label: "SHARED BUDGET / $1,000", alt: "Pixel-art teammates planning a route around a table of maps, tools, radios and expedition supplies." }
        ];
        play.disabled = false;
        window.gameVisuals.createReel({ button: play, length: story.length, interval: 8000, render: renderChapter });
    }

    function renderChapter(index) {
        const chapter = story[index];
        let visual;
        if (index === 0) visual = window.gameVisuals.locationVisual(missionData.location);
        else if (index === 1) {
            visual = window.gameVisuals.missionVisual(missionData.location, missionData.mission, objectiveView);
            objectiveView = (objectiveView + 1) % 2;
        } else visual = window.gameVisuals.planningVisual();
        window.gameVisuals.paint(art, visual.cell, visual.source, visual.alt);
        document.getElementById("storySceneLabel").textContent = chapter.label.toUpperCase();
        document.getElementById("storyCounter").textContent = `0${index + 1} / 03`;
        document.getElementById("storyEyebrow").textContent = chapter.eyebrow;
        document.getElementById("storyTitle").textContent = chapter.title;
        document.getElementById("storyCaption").textContent = chapter.caption;
        chapters.forEach((step, i) => step.classList.toggle("is-current", i === index));
    }
});
