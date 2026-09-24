const instructionsPopup = document.getElementById("instructions-popup");
const openBtn = document.getElementById("openInstructionsBtn");
const closeBtn = document.getElementById("closeInstructionsBtn");
const copyBtn = document.getElementById("copyCodeBtn");
const roomCode = document.getElementById("roomCode");
//new
const playerList = document.getElementById("playerList");
const playerCount = document.getElementById("playerCount");

// Show the actual session code
roomCode.textContent = sessionStorage.getItem("sessionCode");

const readyToggleBtn = document.getElementById("readyToggleBtn");
const startGameBtn = document.getElementById("startGameBtn");
const leaveLobbyBtn = document.getElementById("leaveLobbyBtn");

leaveLobbyBtn.addEventListener("click", () => {
  leaveLobbyBtn.disabled = true;
  window.gameSocket.emit("leave_session", { sessionCode: window.getSessionCode(), playerId: window.getPlayerId() });
});

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

// Toggle ready and tell the server
readyToggleBtn.addEventListener("click", () => {

  const isReady = readyToggleBtn.getAttribute("data-ready") === "true";
  const newReadyState = !isReady;

  readyToggleBtn.setAttribute("data-ready", newReadyState.toString());
  readyToggleBtn.textContent = newReadyState ? "READY ✓" : "MARK READY";

  window.gameSocket.emit("player_ready", {
    sessionCode: window.getSessionCode(),
    playerId: window.getPlayerId(),
    ready: newReadyState
  });

});

// Each player sees the guide once for this lobby, including returning players.
function promptLobbyInstructions(payload) {
  const playerId = window.getPlayerId();
  if (!payload.players.some(player => player.id === playerId)) return;
  const key = `lobbyInstructions:${window.getSessionCode()}:${playerId}`;
  if (sessionStorage.getItem(key) !== "seen") {
    showInstructions();
    sessionStorage.setItem(key, "seen");
  }
}

// Start the game when the host clicks START GAME
startGameBtn.addEventListener("click", () => {
  window.gameSocket.emit("start_game", {
    sessionCode: window.getSessionCode(),
    playerId: window.getPlayerId()
  });
});

leaveLobbyBtn.addEventListener("click", () => {
  leaveLobbyBtn.disabled = true;

  window.gameSocket.emit("leave_session", {
    sessionCode: window.getSessionCode(),
    playerId: window.getPlayerId()
  }, (response) => {
    if (!response?.ok) {
      leaveLobbyBtn.disabled = false;
      return;
    }

    sessionStorage.removeItem("sessionCode");
    sessionStorage.removeItem("playerId");
    sessionStorage.removeItem("isHost");
    sessionStorage.removeItem("auctionStartTime");
    window.location.replace("/join");
  });
});

// When the server starts the game, send everyone to the auction
window.gameSocket.on("game_started", () => {
  window.location.href = "/start_game";
});

// Receive the latest lobby state from the server
window.gameSocket.on("lobby_state", (payload) => {
  promptLobbyInstructions(payload);

  // Remove the demo players
  playerList.innerHTML = "";

  // Add every real player
  payload.players.forEach((player) => {

    const playerTile = document.createElement("div");
    playerTile.classList.add("player-tile");
    playerTile.setAttribute(
      "data-state",
      player.ready ? "ready" : "waiting"
    );

    playerTile.innerHTML = `
      <span class="player-name">
        <span class="avatar-dot"></span>
        ${player.name}
        ${player.isHost ? '<span class="host-tag">HOST</span>' : ''}
      </span>
      <span class="status-pill">
        ${player.ready ? "READY" : "WAITING"}
      </span>
    `;

    playerList.appendChild(playerTile);
  });

  // Update player count
playerCount.textContent =
  `${payload.players.length} / 10 PLAYERS · MIN ${payload.players.length} TO START`;

// Check if this browser belongs to the host
const currentPlayerId = window.getPlayerId();

const currentPlayer = payload.players.find(
  player => player.id === currentPlayerId
);

const isHost = currentPlayer && currentPlayer.isHost;

// Check if the game is allowed to start
const enoughPlayers = payload.players.length >= payload.players.length;
const allReady = payload.players.every(player => player.ready);

// Enable START GAME only for the host when everyone is ready
startGameBtn.disabled = !(isHost && enoughPlayers && allReady);

});
