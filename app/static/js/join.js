// Find the session code input
const sessionCodeInput = document.getElementById("sessionCode");

// Find the player name input
const playerNameInput = document.getElementById("playerName");

// Find the Join Game button
const joinGameBtn = document.getElementById("joinGameBtn");

// Find the Host Game button
const hostGameBtn = document.getElementById("hostGameBtn");

// Find the instructions popup and buttons
const openInstructionsBtn = document.getElementById("openInstructionsBtn");
const closeInstructionsBtn = document.getElementById("closeInstructionsBtn");
const instructionsPopup = document.getElementById("instructions-popup");

// Find the temporary error popup elements
const testErrorBtn = document.getElementById("testErrorBtn");
const errorPopup = document.getElementById("error-popup");
const closeErrorBtn = document.getElementById("closeErrorBtn");

// Find the player name error popup
const nameErrorPopup = document.getElementById("name-error-popup");
const closeNameErrorBtn = document.getElementById("closeNameErrorBtn");

// Find the session code error popup
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

    // Name + session code entered = join game
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

    // Name entered + no session code = host game
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