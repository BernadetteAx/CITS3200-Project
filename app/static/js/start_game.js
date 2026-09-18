const startAuctionBtn = document.getElementById("startAuctionBtn");

const helpBtn = document.getElementById("helpBtn");
const helpPopup = document.getElementById("helpPopup");
const closeHelpBtn = document.getElementById("closeHelpBtn");



function showHelp() {
    helpPopup.classList.remove("hidden");

    requestAnimationFrame(() => {
        helpPopup.classList.add("show");
    });
}


function hideHelp() {
    helpPopup.classList.remove("show");

    setTimeout(() => {
        helpPopup.classList.add("hidden");
    }, 200);
}


helpBtn.addEventListener("click", showHelp);

closeHelpBtn.addEventListener("click", hideHelp);


helpPopup.addEventListener("click", (event) => {

    if (event.target === helpPopup) {
        hideHelp();
    }

});


function typeText(el, text, speed = 200) {
    el.textContent = "";
    let i = 0;
    const interval = setInterval(() => {
        el.textContent += text[i];
        i++;
        if (i === text.length) clearInterval(interval);
    }, speed);
}
if (window.gameVisuals.motionEnabled()) typeText(document.querySelector(".start-title"), "GET READY");


startAuctionBtn.addEventListener("click", () => {
    window.gameSocket.emit("begin_mission_description", {
        sessionCode: window.getSessionCode(),
        playerId: window.getPlayerId()
    });
});

window.gameSocket.on("mission_description_started", () => {
    window.location.href = "/mission_description";
});
