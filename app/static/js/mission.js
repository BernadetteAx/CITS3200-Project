/*
  FRONT END ONLY NO BACKEND LOGIC YET
*/

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

  const instructionsBtn = document.getElementById("instructionsBtn");
  const instructionsPopup = document.getElementById("instructionsPopup");
  const instructionsClose = document.getElementById("instructionsClose");

  let selectedCard = null;

  const countdownFill = document.getElementById("countdownFill");
  const countdownTrack = countdownFill.parentElement;
  const duration = 60 * 1000; // 1 minute
  const startTime = Date.now();

  const countdown = setInterval(() => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, duration - elapsed);
    const percent = (remaining / duration) * 100;

    countdownFill.style.width = `${percent}%`;
    countdownTrack.setAttribute(
      "aria-valuenow",
      Math.ceil(remaining / 1000)
    );

    if (remaining === 0) {
      clearInterval(countdown);
      // TODO: time-up behaviour here
    }
  }, 50);

  // selecting one of the usable items
  itemGrid.addEventListener("click", (e) => {
    const card = e.target.closest(".item-card");
    if (!card || card.dataset.status === "used") return;

    if (selectedCard === card) {
      // clicking the same card again clears the selection
      card.dataset.selected = "false";
      selectedCard = null;
    } else {
      if (selectedCard) selectedCard.dataset.selected = "false";
      card.dataset.selected = "true";
      selectedCard = card;
    }

    useItemBtn.disabled = !selectedCard;
  });

  // item used becomes unavailable 
  function markItemUsed(itemId) {
    const card = itemGrid.querySelector(`[data-item-id="${itemId}"]`);
    if (card) {
      card.dataset.status = "used";
      card.dataset.selected = "false";
      card.disabled = true;
      const pill = card.querySelector(".item-status-pill");
      if (pill) pill.textContent = "Used";
    }

    const slot = hotbarSlots.querySelector(`[data-item-id="${itemId}"]`);
    if (slot) {
      slot.dataset.status = "used";
      slot.title = `${slot.querySelector("img")?.alt ?? "Item"} (used)`;
    }

    refreshHotbarLabel();
  }

  function refreshHotbarLabel() {
    const slots = hotbarSlots.querySelectorAll(".hotbar-slot.filled");
    const available = hotbarSlots.querySelectorAll('.hotbar-slot.filled[data-status="available"]');
    hotbarLabel.textContent = `TEAM INVENTORY · ${available.length}/${slots.length} AVAILABLE`;
  }

  // outcome feedback
  function openPopup(popup) {
    popup.classList.remove("hidden");
    popup.classList.add("show");
  }

  function closePopup(popup) {
    popup.classList.remove("show");
    popup.classList.add("hidden");
  }

  function showFeedback({ outcome, title, sub }) {
    feedbackBox.dataset.outcome = outcome; // "success" | "fail"
    feedbackTitle.textContent = title;
    feedbackSub.textContent = sub;
    openPopup(feedbackPopup);
  }

  useItemBtn.addEventListener("click", () => {
    if (!selectedCard) return;
    const itemName = selectedCard.querySelector(".item-name").textContent;
    const itemId = selectedCard.dataset.itemId;

    // TODO: backend: submit the team's voted item and receive the real outcome
    markItemUsed(itemId);
    selectedCard = null;
    useItemBtn.disabled = true;

    showFeedback({
      outcome: "success",
      title: "Obstacle Cleared",
      sub: `The team used the ${itemName} to get past the challenge. On to the next one.`,
    });
  });

  continueBtn.addEventListener("click", () => {
    // TODO: backend: record that the team continued without an item and apply the score penalty
    showFeedback({
      outcome: "fail",
      title: "Forced to Double Back",
      sub: "No item was used, so the team took the longer route. Your final score takes a hit.",
    });
  });

  feedbackClose.addEventListener("click", () => {
    closePopup(feedbackPopup);
    // TODO: backend: advance to the next challenge
  });

  // instructions popup
  instructionsBtn.addEventListener("click", () => openPopup(instructionsPopup));
  instructionsClose.addEventListener("click", () => closePopup(instructionsPopup));
  [feedbackPopup, instructionsPopup].forEach((popup) => {
    popup.addEventListener("click", (e) => {
      if (e.target === popup) closePopup(popup);
    });
  });

  refreshHotbarLabel();
});