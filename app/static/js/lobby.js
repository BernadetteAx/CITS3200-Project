const instructionsPopup = document.getElementById("instructions-popup");
const openBtn = document.getElementById("openInstructionsBtn");
const closeBtn = document.getElementById("closeInstructionsBtn");
const copyBtn = document.getElementById("copyCodeBtn");
const roomCode = document.getElementById("roomCode");
const readyToggleBtn = document.getElementById("readyToggleBtn");
const startGameBtn = document.getElementById("startGameBtn");

function showInstructions() {
  instructionsPopup.classList.remove("hidden");
  instructionsPopup.offsetHeight;
  instructionsPopup.classList.add("show");
}

function hideInstructions() {
  instructionsPopup.classList.remove("show");
  setTimeout(() => instructionsPopup.classList.add("hidden"), 200);
}

openBtn.addEventListener("click", showInstructions);
closeBtn.addEventListener("click", hideInstructions);
instructionsPopup.addEventListener("click", (e) => {
  if (e.target === instructionsPopup) hideInstructions();
});

// Chnage the text for the copy button
copyBtn.addEventListener("click", () => {
  navigator.clipboard?.writeText(roomCode.textContent.trim());
  copyBtn.textContent = "COPIED";
  setTimeout(() => (copyBtn.textContent = "COPY"), 1200);
});

// toggle the ready button
readyToggleBtn.addEventListener("click", () => {
  const isReady = readyToggleBtn.getAttribute("data-ready") === "true";
  readyToggleBtn.setAttribute("data-ready", (!isReady).toString());
  readyToggleBtn.textContent = isReady ? "MARK READY" : "READY ✓";
});

// Show instructions automatically on first visit, then just use the "?"
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("chaosAuctionFirstVisit") !== "false") {
    showInstructions();
    localStorage.setItem("chaosAuctionFirstVisit", "false");
  }
});

// start the game
startGameBtn.addEventListener("click", () => {
  window.location.href = "/auction";
});
