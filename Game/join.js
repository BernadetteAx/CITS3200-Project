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

// Find the temporary error popup elements
const testErrorBtn = document.getElementById("testErrorBtn");
const errorPopup = document.getElementById("error-popup");
const closeErrorBtn = document.getElementById("closeErrorBtn");

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

// Show the error popup
testErrorBtn.addEventListener("click", function () {
   // show error pop up
    errorPopup.classList.remove("hidden");

    // auto close error pop up
    setTimeout(function () {
        errorPopup.classList.add("hidden");
    }, 1900);
});

// Close the error popup
closeErrorBtn.addEventListener("click", function () {
    errorPopup.classList.add("hidden");
});