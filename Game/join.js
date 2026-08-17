// Find the session code input
const sessionCodeInput = document.getElementById("sessionCode");

// Find the player name input
const playerNameInput = document.getElementById("playerName");

// Find the Join Game button
const joinGameBtn = document.getElementById("joinGameBtn");

// Find the instructions popup and buttons
const openInstructionsBtn = document.getElementById("openInstructionsBtn");
const closeInstructionsBtn = document.getElementById("closeInstructionsBtn");
const instructionsPopup = document.getElementById("instructions-popup");

playerNameInput.addEventListener("input", function () {

    const playerName = playerNameInput.value.trim();

    if (playerName === "") {
        sessionCodeInput.disabled = true;
    }
    else {
        sessionCodeInput.disabled = false;
    }

});

sessionCodeInput.addEventListener("input", function () {

    const sessionCode = sessionCodeInput.value.trim();

    if (sessionCode === "") {
        joinGameBtn.disabled = true;
    }
    else {
        joinGameBtn.disabled = false;
    }

});


// Run this function when the Join Game button is clicked
joinGameBtn.addEventListener("click", function () {

    // Get what the user typed
    const sessionCode = sessionCodeInput.value.trim();
    const playerName = playerNameInput.value.trim();


    // Check if session code is empty
    if (sessionCode === "") {
        alert("Please enter a session code");
        return;
    }


    // Check if player name is empty
    if (playerName === "") {
        alert("Please enter your player name");
        return;
    }


    // Both fields have been entered
    // Go to the lobby page
    window.location.href = "lobby.html";

});

// Open instructions when ? is clicked
openInstructionsBtn.addEventListener("click", function () {
    instructionsPopup.classList.remove("hidden");
    instructionsPopup.classList.add("show");
});

// Close instructions when GOT IT is clicked
closeInstructionsBtn.addEventListener("click", function () {
    instructionsPopup.classList.remove("show");
    instructionsPopup.classList.add("hidden");
});