document.addEventListener("DOMContentLoaded", () => {
    const missionTitle = document.getElementById("missionTitle");
    const missionLocation = document.getElementById("missionLocation");
    const missionDescription = document.getElementById("missionDescription");
    const typingCursor = document.getElementById("typingCursor");
    const continueBtn = document.getElementById("continueAuctionBtn");

    let briefingLoaded = false;

    // Ask the server for the mission assigned to this game.
    window.gameSocket.emit("get_mission_description", {
        sessionCode: window.getSessionCode(),
        playerId: window.getPlayerId()
    });

    window.gameSocket.on("mission_description_state", (data) => {
        if (briefingLoaded) return;
        briefingLoaded = true;

        missionTitle.textContent = data.mission.toUpperCase();
        missionLocation.textContent = data.location.toUpperCase();

        typeMissionDescription(data.description, data.isHost);
    });

    function typeMissionDescription(text, isHost) {
        let index = 0;
        missionDescription.textContent = "";

        const typingInterval = setInterval(() => {
            missionDescription.textContent += text.charAt(index);
            index++;

            if (index >= text.length) {
                clearInterval(typingInterval);

                typingCursor.style.display = "none";

                if (isHost) {
                    continueBtn.disabled = false;
                    continueBtn.textContent = "CONTINUE TO ITEM SHOP";
                } else {
                    continueBtn.disabled = true;
                    continueBtn.textContent = "WAITING FOR HOST";
                }
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
});