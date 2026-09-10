// =====================================================================
// SOCKET.JS — sets up the ONE socket connection this browser tab uses
// =====================================================================
//
// this is the client-side half of app/sockets/handlers/lobby.py etc.
// Flask-SocketIO's Python side pairs with a JS LIBRARY on the browser
// side called socket.io-client — NOT the plain browser `WebSocket`
// class. It handles a few things for us automatically (auto-reconnect
// attempts, falling back to older transports on flaky connections)
// that we'd otherwise have to build by hand
//
// the pattern to remember is the same as before:
//   1. Open the connection (happens automatically when this file loads)
//   2. Tell the server who you are (join_session)
//   3. Listen for named events from the server, and update the screen
//      based on whatever the server says the current state is
//   4. When the player does something, emit a small message describing
//      what they want — never calculate the outcome yourself client-side
//
// this file only sets up the connection and exposes small helpers.
// Each page's own JS file (lobby.js, auction.js, mission.js) listens
// for the events IT cares about — see the snippet comments at the
// bottom of this file for exactly what to add to each

// `io()` with no arguments connects back to the same host that served
// the page — this works because Flask-SocketIO serves both your normal
// pages AND the socket endpoint from the same Flask app
const socket = io();

// RECONNECT SUPPORT:
// sessionStorage survives page refreshes and navigation in this tab, while
// keeping each browser tab as a separate player. localStorage is shared by
// every tab, which would make test players look like the same person.
// This lets the server recognise a reconnecting player as the SAME player.
// (see the reconnect handling in handlers/lobby.py's handle_join_session)
let playerId = sessionStorage.getItem('playerId') || null;

// read the session code from wherever your app currently stores it —
// e.g. a data attribute on the page, or a variable already set by your
// Flask template. Adjust this line to match how join.js/lobby.js
// currently pass the code around
const sessionCode = sessionStorage.getItem("sessionCode");
const playerName = sessionStorage.getItem("playerName");

// fired once the connection is established
socket.on('connect', () => {
  socket.emit('join_session', {
    sessionCode,
    name: playerName,
    playerId,
    isHost: sessionStorage.getItem('isHost') === 'true',
  });
});

// server assigns us our official playerId on first join — save it
socket.on('joined', (payload) => {

  playerId = payload.playerId;
  sessionStorage.setItem('playerId', playerId);
  sessionStorage.setItem('isHost', payload.isHost ? 'true' : 'false');

  if (payload.auctionStartTime) {
    sessionStorage.setItem('auctionStartTime', payload.auctionStartTime);
  }

  const phasePages = {
    lobby: "/lobby",
    start_game: "/start_game",
    auction: "/auction",
    mission: "/mission",
    result_page: "/result_page"
  };

  const currentPage = window.location.pathname;
  const correctPage = phasePages[payload.phase];

  if (correctPage && currentPage !== correctPage) {
    window.location.replace(correctPage);
  }
});

// Keep this browser's host status updated if the host changes
socket.on('host_changed', (payload) => {
  const amIHost = payload.hostId === playerId;
  sessionStorage.setItem('isHost', amIHost ? 'true' : 'false');
});

// Invalid session code
socket.on('invalid_session', () => {
  sessionStorage.setItem('invalidSession', 'true');
  sessionStorage.removeItem('sessionCode');
  sessionStorage.removeItem('playerId');
  window.location.href = '/join';
});

// exported (via `window`) so lobby.js/auction.js/mission.js can use the
// same connection and helpers without opening their own separate socket
window.gameSocket = socket;
window.getPlayerId = () => playerId;
window.getSessionCode = () => sessionStorage.getItem("sessionCode");

// If the player presses Back during the game, return to the Join page
window.addEventListener("pageshow", (event) => {
  const gamePages = ["/lobby", "/start_game", "/auction", "/mission", "/result_page"];

  if (event.persisted && gamePages.includes(window.location.pathname)) {
    window.location.replace("/join");
  }
});

// =====================================================================
// WHAT TO ADD TO lobby.js / auction.js / mission.js (generated example)
// =====================================================================
//
// In lobby.js, listen for the events the lobby cares about:
//
//   window.gameSocket.on('lobby_state', (payload) => {
//     // payload.players, payload.phase — update the lobby UI here
//   });
//
//   window.gameSocket.on('game_started', (payload) => {
//     // e.g. window.location.href = '/auction' or however phase changes work
//   });
//
// And to send an action (e.g. a "ready" checkbox toggling):
//
//   function toggleReady(isReady) {
//     window.gameSocket.emit('player_ready', {
//       sessionCode: window.getSessionCode(),
//       playerId: window.getPlayerId(),
//       ready: isReady,
//     });
//   }
//
// auction.js and mission.js will follow the identical shape once their
// Python handlers (auction.py, mission.py) are built — listen for
// 'auction_state'/'mission_state', emit 'place_bid'/'item_used' with
// sessionCode + playerId included in the payload every time
