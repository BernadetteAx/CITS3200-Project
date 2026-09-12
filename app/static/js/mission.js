document.addEventListener("DOMContentLoaded", () => {
  const itemGrid = document.getElementById("itemGrid");
  const hotbarSlots = document.getElementById("hotbarSlots");
  const hotbarLabel = document.getElementById("hotbarLabel");
  const useItemBtn = document.getElementById("useItemBtn");
  const continueBtn = document.getElementById("continueBtn");
  const feedbackPopup = document.getElementById("feedbackPopup");
  const feedbackBox = document.getElementById("feedbackBox");
  const feedbackTitle = document.getElementById("feedbackTitle");
  const feedbackSub = document.getElementById("feedbackSub");
  const feedbackClose = document.getElementById("feedbackClose");
  const instructionsPopup = document.getElementById("instructionsPopup");
  const timerValue = document.getElementById("timerValue");
  const timerPill = document.getElementById("timerPill");
  const countdownFill = document.getElementById("countdownFill");
  const countdownTrack = document.getElementById("countdownTrack");
  let state = null;
  let selectedItemId = null;

  const show = (popup) => { popup.classList.remove("hidden"); popup.classList.add("show"); };
  const hide = (popup) => { popup.classList.remove("show"); popup.classList.add("hidden"); };
  const action = (event, extra = {}) => state && window.gameSocket.emit(event, {
    sessionCode: window.getSessionCode(), playerId: window.getPlayerId(),
    challengeIndex: state.currentChallengeIndex, ...extra,
  });

  function render(next) {
    state = next;
    if (state.phase === "result_page") return window.location.replace("/result_page");
    const challenge = state.challenge;
    document.getElementById("missionName").textContent = state.missionName;
    document.getElementById("challengeCount").textContent = `${Math.min(state.currentChallengeIndex + 1, state.totalChallenges)} OF ${state.totalChallenges}`;
    if (challenge) {
      document.getElementById("challengeProgress").textContent = `CHALLENGE ${state.currentChallengeIndex + 1}`;
      document.getElementById("challengeName").textContent = challenge.name;
      document.getElementById("challengeDesc").textContent = challenge.description;
      const image = document.querySelector("#challengeIcon img");
      image.src = `/static/images/${challenge.image || "icons8-mountain-64.png"}`;
      image.alt = challenge.name;
    }
    const active = state.status === "active";
    const available = state.inventory.filter((item) => !item.used);
    if (!available.some((item) => item.id === selectedItemId)) selectedItemId = null;
    itemGrid.replaceChildren();
    state.inventory.forEach((item) => {
      const usable = active && !item.used;
      const card = document.createElement("button");
      card.type = "button";
      card.className = "item-card";
      card.dataset.status = item.used ? "used" : "available";
      card.dataset.selected = String(selectedItemId === item.id);
      card.disabled = !usable;
      card.innerHTML = `<span class="item-icon"><img src="/static/images/${item.image}" alt=""></span><span class="item-name"></span><span class="item-status-pill"></span>`;
      card.querySelector(".item-name").textContent = item.name;
      card.querySelector(".item-status-pill").textContent = item.used ? "Used" : "Owned";
      if (usable) card.addEventListener("click", () => {
        selectedItemId = selectedItemId === item.id ? null : item.id;
        render(state);
      });
      itemGrid.appendChild(card);
    });
    hotbarLabel.textContent = `TEAM INVENTORY · ${available.length}/${state.inventory.length} AVAILABLE · SCORE ${state.score}`;
    hotbarSlots.replaceChildren();
    state.inventory.forEach((item) => {
      const slot = document.createElement("div");
      slot.className = "hotbar-slot filled";
      slot.dataset.status = item.used ? "used" : "available";
      slot.title = `${item.name}${item.used ? " (used)" : ""}`;
      slot.innerHTML = `<img src="/static/images/${item.image}" alt="">`;
      hotbarSlots.appendChild(slot);
    });
    useItemBtn.disabled = !active || !selectedItemId;
    continueBtn.disabled = !active;
    tickTimer();
    if (state.status === "resolved" && state.outcome) {
      feedbackBox.dataset.outcome = state.outcome.success ? "success" : "fail";
      feedbackTitle.textContent = state.outcome.title;
      feedbackSub.textContent = `${state.outcome.description}${state.outcome.penalty ? ` Score -${state.outcome.penalty}.` : ""}`;
      show(feedbackPopup);
    } else hide(feedbackPopup);
  }

  function tickTimer() {
    if (!state || state.status !== "active" || !state.endsAt) {
      countdownFill.style.width = "0%";
      countdownTrack.setAttribute("aria-valuenow", "0");
      return;
    }

    const remaining = Math.max(0, state.endsAt - Date.now() / 1000);
    const seconds = Math.ceil(remaining);
    const percent = Math.min(100, Math.max(0, remaining / 60 * 100));
    timerValue.textContent =
      `${String(Math.floor(seconds / 60)).padStart(2, "0")}:` +
      String(seconds % 60).padStart(2, "0");
    timerPill.classList.toggle("low", seconds <= 10);
    countdownFill.style.width = `${percent}%`;
    countdownFill.classList.toggle("low", seconds <= 10);
    countdownTrack.setAttribute("aria-valuenow", String(seconds));
  }

  useItemBtn.addEventListener("click", () => action("mission_use_item", { itemId: selectedItemId }));
  continueBtn.addEventListener("click", () => action("mission_continue"));
  feedbackClose.addEventListener("click", () => {
    if (state && state.status === "resolved") action("mission_advance");
  });
  document.getElementById("instructionsBtn").addEventListener("click", () => show(instructionsPopup));
  document.getElementById("instructionsClose").addEventListener("click", () => hide(instructionsPopup));
  instructionsPopup.addEventListener("click", (event) => {
    if (event.target === instructionsPopup) hide(instructionsPopup);
  });
  window.gameSocket.on("mission_state", render);
  window.gameSocket.on("mission_complete", () => window.location.replace("/result_page"));
  setInterval(tickTimer, 250);
});
