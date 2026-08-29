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
const testErrorBtn = document.getElementById("testErrorBtn");
const errorPopup = document.getElementById("error-popup");
const closeErrorBtn = document.getElementById("closeErrorBtn");

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

    // Save player details for the lobby
    sessionStorage.setItem("playerName", playerName);
    sessionStorage.setItem("sessionCode", sessionCode.toUpperCase());

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

// TEST INVALID SESSION CODE POPUP
testErrorBtn.addEventListener("click", function () {

    errorPopup.classList.remove("hidden");

    setTimeout(function () {
        errorPopup.classList.add("hidden");
    }, 1900);

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