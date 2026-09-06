// Join page inputs and buttons
const sessionCodeInput = document.getElementById("sessionCode");
const playerNameInput = document.getElementById("playerName");
const joinGameBtn = document.getElementById("joinGameBtn");
const hostGameBtn = document.getElementById("hostGameBtn");

// Instructions popup
const openInstructionsBtn = document.getElementById("openInstructionsBtn");
const closeInstructionsBtn = document.getElementById("closeInstructionsBtn");
const instructionsPopup = document.getElementById("instructions-popup");

// Invalid session code popup
const errorPopup = document.getElementById("error-popup");
const closeErrorBtn = document.getElementById("closeErrorBtn");

const savedPlayerName = sessionStorage.getItem("playerName");
const savedSessionCode = sessionStorage.getItem("sessionCode");

if (savedPlayerName) {
    playerNameInput.value = savedPlayerName;
    sessionCodeInput.disabled = false;
}

if (savedSessionCode) {
    sessionCodeInput.value = savedSessionCode;
    joinGameBtn.disabled = false;
    hostGameBtn.disabled = true;
}

// Show invalid session popup if the server rejected the code
if (sessionStorage.getItem("invalidSession") === "true") {
    errorPopup.classList.remove("hidden");
    sessionStorage.removeItem("invalidSession");

    setTimeout(function () {
        errorPopup.classList.add("hidden");
    }, 3000);
}

// Player name error popup
const nameErrorPopup = document.getElementById("name-error-popup");
const closeNameErrorBtn = document.getElementById("closeNameErrorBtn");

// Missing session code popup
const codeErrorPopup = document.getElementById("code-error-popup");
const closeCodeErrorBtn = document.getElementById("closeCodeErrorBtn");

// PLAYER NAME INPUT
playerNameInput.addEventListener("input", function () {

    const playerName = playerNameInput.value.trim();

    if (playerName === "") {
        // No name = cannot enter a session code or join
        sessionCodeInput.value = "";
        sessionCodeInput.disabled = true;

        joinGameBtn.disabled = true;
        hostGameBtn.disabled = false;
    }
    else {
        // Name entered = allow session code entry
        sessionCodeInput.disabled = false;
    }

});

// SESSION CODE INPUT
sessionCodeInput.addEventListener("input", function () {

    const sessionCode = sessionCodeInput.value.trim();

    if (sessionCode === "") {
        // No code = can host, cannot join
        joinGameBtn.disabled = true;
        hostGameBtn.disabled = false;
    }
    else {
        // Code entered = can join, cannot host
        joinGameBtn.disabled = false;
        hostGameBtn.disabled = true;
    }

});

// JOIN GAME
joinGameBtn.addEventListener("click", function () {

    const playerName = playerNameInput.value.trim();
    const sessionCode = sessionCodeInput.value.trim();

    // Must have a player name
    if (playerName === "") {
        nameErrorPopup.classList.remove("hidden");

        setTimeout(function () {
            nameErrorPopup.classList.add("hidden");
        }, 2700);

        return;
    }

    // Must have a session code
    if (sessionCode === "") {
        codeErrorPopup.classList.remove("hidden");

        setTimeout(function () {
            codeErrorPopup.classList.add("hidden");
        }, 2700);

        return;
    }

    // Get the session this player was previously in
    const previousSessionCode = sessionStorage.getItem("sessionCode");
    const newSessionCode = sessionCode.toUpperCase();

    // If joining a different game, they need a new player ID
    if (previousSessionCode !== newSessionCode) {
        sessionStorage.removeItem("playerId");
    }

    // Save player details
    sessionStorage.setItem("playerName", playerName);
    sessionStorage.setItem("sessionCode", newSessionCode);

    // This player is joining, not creating a new game
    sessionStorage.removeItem("isHost");

    // Go to lobby
    window.location.href = "/lobby";

});

// HOST GAME
hostGameBtn.addEventListener("click", function () {

    const playerName = playerNameInput.value.trim();
    const sessionCode = sessionCodeInput.value.trim();

    // Must have a player name
    if (playerName === "") {
        nameErrorPopup.classList.remove("hidden");

        setTimeout(function () {
            nameErrorPopup.classList.add("hidden");
        }, 2700);

        return;
    }

    // Cannot host if a session code has been entered
    if (sessionCode !== "") {
        return;
    }

    // Generate a random 4-character session code
    const generatedCode = Math.random()
        .toString(36)
        .substring(2, 6)
        .toUpperCase();

    // Save host details for the lobby
    sessionStorage.setItem("playerName", playerName);
    sessionStorage.setItem("sessionCode", generatedCode);
    sessionStorage.removeItem("playerId");
    sessionStorage.setItem("isHost", "true");

    // Go to lobby
    window.location.href = "/lobby";

});

// OPEN INSTRUCTIONS
openInstructionsBtn.addEventListener("click", function () {
    instructionsPopup.classList.remove("hidden");
    instructionsPopup.classList.add("show");
});

// CLOSE INSTRUCTIONS
closeInstructionsBtn.addEventListener("click", function () {
    instructionsPopup.classList.remove("show");
    instructionsPopup.classList.add("hidden");
});

// CLOSE INVALID SESSION CODE POPUP
closeErrorBtn.addEventListener("click", function () {
    errorPopup.classList.add("hidden");
});

// CLOSE PLAYER NAME ERROR POPUP
closeNameErrorBtn.addEventListener("click", function () {
    nameErrorPopup.classList.add("hidden");
});

// CLOSE SESSION CODE ERROR POPUP
closeCodeErrorBtn.addEventListener("click", function () {
    codeErrorPopup.classList.add("hidden");
});