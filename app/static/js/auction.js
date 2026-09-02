const itemGrid = document.getElementById("itemGrid");
const budgetValue = document.getElementById("budgetValue");
const roundText = document.getElementById("roundText");
const voteCountText = document.getElementById("voteCountText");
const progressFill = document.getElementById("progressFill");
const finishBtn = document.getElementById("finishBtn");
const skipBtn = document.getElementById("skipBtn");
const timerValue = document.getElementById("timerValue");
const timerPill = document.getElementById("timerPill");
const countdownFill = document.getElementById("countdownFill");
const countdownTrack = document.getElementById("countdownTrack");
const inventory = document.getElementById("inventorySlots");
const inventoryLabel = document.getElementById("inventoryLabel");
const resultPopup = document.getElementById("resultPopup");
let latestState = null;

function action(event, extra = {}) {
  window.gameSocket.emit(event, { sessionCode: window.getSessionCode(), playerId: window.getPlayerId(), ...extra });
}

function render(state) {
  // Room broadcasts keep choices anonymous. A player's authoritative personal
  // choice is sent separately by the server after its action/reconnect.
  if (latestState && state.myVote === undefined && state.round === latestState.round) state.myVote = latestState.myVote;
  latestState = state;
  budgetValue.textContent = `$${state.budget}`;
  roundText.textContent = `${Math.min(state.round, state.totalRounds)} OF ${state.totalRounds}`;
  voteCountText.textContent = `${state.voteCount} / ${state.playerCount} TEAMMATES HAVE VOTED`;
  progressFill.style.width = `${state.playerCount ? state.voteCount / state.playerCount * 100 : 0}%`;
  itemGrid.innerHTML = "";
  state.items.forEach((item) => {
    const selected = state.myVote === item.id;
    const unavailable = state.status !== "voting" || item.cost > state.budget;
    const tile = document.createElement("button");
    tile.type = "button"; tile.className = "item-tile";
    tile.dataset.state = unavailable ? "unavailable" : selected ? "selected" : "idle";
    tile.innerHTML = `<div class="item-image"><img src="/static/images/${item.image}" alt="${item.name}"></div><div class="item-name">${item.name}</div><div class="item-desc">${item.description}</div><div class="item-footer"><span class="cost-tag">$${item.cost}</span><span class="vote-check">${selected ? "✓ YOUR VOTE" : "TAP TO VOTE"}</span></div>`;
    if (!unavailable) tile.addEventListener("click", () => action("auction_vote", { itemId: item.id }));
    itemGrid.appendChild(tile);
  });
  const voting = state.status === "voting";
  finishBtn.disabled = !voting || !state.myVote || state.myVote === "skip";
  skipBtn.disabled = !voting;
  inventoryLabel.textContent = `TEAM INVENTORY · ${state.purchasedItems.length}/8 SLOTS FILLED`;
  inventory.innerHTML = state.purchasedItems.map((item) => `<div class="hotbar-slot filled" title="${item.name}"><img src="/static/images/${item.image}" alt="${item.name}"></div>`).join("") + Array.from({length: Math.max(0, 8 - state.purchasedItems.length)}, () => '<div class="hotbar-slot empty">＋</div>').join("");
  if (state.status !== "voting") {
    countdownFill.style.width = "0%";
    countdownTrack.setAttribute("aria-valuenow", "0");
  } else {
    tickTimer();
  }
  state.status === "resolved" ? showResult(state.roundResult) : hideResult();
}

function tickTimer() {
  if (!latestState || latestState.status !== "voting" || !latestState.endsAt) return;
  const seconds = Math.max(0, Math.ceil(latestState.endsAt - Date.now() / 1000));
  const percent = Math.min(100, Math.max(0, (latestState.endsAt - Date.now() / 1000) / 60 * 100));
  timerValue.textContent = `${String(Math.floor(seconds / 60)).padStart(2, "0")}:${String(seconds % 60).padStart(2, "0")}`;
  timerPill.classList.toggle("low", seconds <= 10);
  countdownFill.style.width = `${percent}%`;
  countdownFill.classList.toggle("low", seconds <= 10);
  countdownTrack.setAttribute("aria-valuenow", String(seconds));
}
setInterval(tickTimer, 250);

function showResult(result) {
  if (!result) return;
  const title = document.getElementById("resultTitle"), sub = document.getElementById("resultSub"), icon = document.getElementById("resultIcon");
  if (result.type === "purchase") { title.textContent = "ITEM PURCHASED"; sub.textContent = `Your team bought the ${result.item.name} for $${result.item.cost}.`; icon.textContent = "✓"; }
  else if (result.type === "unaffordable") { title.textContent = "NOT ENOUGH BUDGET"; sub.textContent = `${result.item.name} could not be purchased.`; icon.textContent = "!"; }
  else if (result.type === "skip") { title.textContent = "MOVING ON"; sub.textContent = "Your team continued without buying an item."; icon.textContent = "→"; }
  else { title.textContent = "IT'S A TIE"; sub.textContent = "No item was purchased this round."; icon.textContent = "⚔"; }
  resultPopup.classList.remove("hidden"); resultPopup.classList.add("show");
}
function hideResult() { resultPopup.classList.remove("show"); resultPopup.classList.add("hidden"); }

finishBtn.addEventListener("click", () => action("auction_finish_voting"));
skipBtn.addEventListener("click", () => action("auction_skip"));
document.getElementById("closeResult").addEventListener("click", hideResult);

const helpBtn = document.getElementById("helpBtn"), helpPopup = document.getElementById("helpPopup");
helpBtn.addEventListener("click", () => { helpPopup.classList.remove("hidden"); helpPopup.classList.add("show"); });
document.getElementById("closeHelp").addEventListener("click", () => { helpPopup.classList.remove("show"); helpPopup.classList.add("hidden"); });

window.gameSocket.on("auction_state", render);
window.gameSocket.on("auction_complete", () => { window.location.href = "/mission"; });
