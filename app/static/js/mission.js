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
    console.log("MISSION STATE:", state);
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
    if (state.status === "resolved" && state.outcome) {
      feedbackBox.dataset.outcome = state.outcome.success ? "success" : "fail";
      feedbackTitle.textContent = state.outcome.title;
      feedbackSub.textContent = `${state.outcome.description}${state.outcome.penalty ? ` Score -${state.outcome.penalty}.` : ""}`;
      show(feedbackPopup);
    } else hide(feedbackPopup);
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
});
