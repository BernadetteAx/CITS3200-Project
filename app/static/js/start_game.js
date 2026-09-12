const startAuctionBtn = document.getElementById("startAuctionBtn");

const helpBtn = document.getElementById("helpBtn");
const helpPopup = document.getElementById("helpPopup");
const closeHelpBtn = document.getElementById("closeHelpBtn");
const ICONS = ["$"];


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
typeText(document.querySelector(".start-title"), "GET READY");


function spawnFloatingIcon() {
    const container = document.getElementById("floatingIcons");
    const icon = document.createElement("span");

    icon.className = "floating-icon";
    icon.textContent = ICONS[Math.floor(Math.random() * ICONS.length)];

    icon.style.left = `${Math.random() * 100}%`;
    icon.style.fontSize = `${1 + Math.random() * 1.2}rem`;

    const duration = 8 + Math.random() * 6;
    icon.style.animationDuration = `${duration}s`;

    container.appendChild(icon);

    setTimeout(() => icon.remove(), duration * 1000);
}

setInterval(spawnFloatingIcon, 900);
spawnFloatingIcon();


startAuctionBtn.addEventListener("click", () => {
    window.gameSocket.emit("begin_auction", {
        sessionCode: window.getSessionCode(),
        playerId: window.getPlayerId()
    });
});

window.gameSocket.on("auction_started", () => {
    window.location.href = "/auction";
});
