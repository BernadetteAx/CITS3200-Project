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
  const countdownFill = document.getElementById("countdownFill");
  const countdownTrack = document.getElementById("countdownTrack");
  const missionTransition = document.getElementById("missionTransition");
  const journeyBriefingDesc = document.getElementById("journeyBriefingDesc");
  const journeyBriefingBtn = document.getElementById("journeyBriefingBtn");
  const challengeBlock = document.getElementById("challengeBlock");
  const CHALLENGE_SECONDS = 60;
  let timerChallengeIndex = null;
  let timerInterval = null;
  let timerStart = null;
  let timedOutChallengeIndex = null;
  let challengeEndsAt = null;
  let state = null;
  let selectedItemId = null;
  let lastChallengeIndex = null;
  let transitioning = false;
  let pendingState = null;
  let submittedVotes = {};
  let challengeDescs = {};
  let journeyTimers = [];
  let journeyAnimationFrame = null;
  let activeTransitionState = null;
  let finalFailureTimer = null;
  let showingFinalFailure = false;

  const JOURNEY_TRAVEL_MS = 2000;
  const JOURNEY_NODE_COUNT = 6;

  const journeyPath = document.getElementById("journeyPathLine");
  const journeyPathEnergy = document.getElementById("journeyPathEnergy");
  const journeyRunner = document.getElementById("journeyRunner");
  const journeyParticles = document.getElementById("journeyParticles");
  const arrivalBurst = document.getElementById("arrivalBurst");

  const journeyNodes = Array.from(
    { length: JOURNEY_NODE_COUNT },
    (_, index) =>
    document.getElementById(`journeyNode${index + 1}`)
  );
  

  const show = (popup) => { popup.classList.remove("hidden"); popup.classList.add("show"); };
  const hide = (popup) => { popup.classList.remove("show"); popup.classList.add("hidden"); };
  const action = (event, extra = {}) => state && window.gameSocket.emit(event, {
    sessionCode: window.getSessionCode(), playerId: window.getPlayerId(),
    challengeIndex: state.currentChallengeIndex, ...extra,
  });

  function tickTimer() {
    if (!state || state.status !== "active" || !challengeEndsAt) {
      countdownFill.style.width = "0%";
      countdownTrack.setAttribute("aria-valuenow", "0");
      return;
    }
    const secondsLeft = Math.max(0, Math.ceil(challengeEndsAt - Date.now() / 1000));
    const percent = Math.min(100, Math.max(0, secondsLeft / CHALLENGE_SECONDS * 100));
    countdownFill.style.width = `${percent}%`;
    countdownFill.classList.toggle("low", secondsLeft <= 10);
    countdownTrack.setAttribute("aria-valuenow", String(secondsLeft));

    if (secondsLeft <= 0 && timedOutChallengeIndex !== state.currentChallengeIndex) {
      timedOutChallengeIndex = state.currentChallengeIndex;
      handleTimeout();
    }
  }

  function handleTimeout() {
    useItemBtn.disabled = true;
    continueBtn.disabled = true;
    feedbackBox.dataset.outcome = "fail";
    feedbackTitle.textContent = "TIME'S UP";
    feedbackSub.textContent = "Your team ran out of time on this challenge.";
    show(feedbackPopup);
    action("mission_timeout");
  }

  setInterval(tickTimer, 250);

function applyState(next) {
    state = next;
    if (state.phase === "result_page") return window.location.replace("/result_page");
    if (state.myVote !== undefined && state.myVote !== null) submittedVotes[state.currentChallengeIndex] = state.myVote;
    const submittedVote = submittedVotes[state.currentChallengeIndex];
    const challenge = state.challenge;
    document.getElementById("missionName").textContent = state.missionName;
    document.getElementById("challengeCount").textContent = `${Math.min(state.currentChallengeIndex + 1, state.totalChallenges)} OF ${state.totalChallenges}`;
    if (challenge) {
      document.getElementById("challengeProgress").textContent = `CHALLENGE ${state.currentChallengeIndex + 1}`;
      document.getElementById("challengeName").textContent = challenge.name;
      document.getElementById("challengeDesc").textContent = challenge.description;
      const image = document.querySelector("#challengeIcon img");
      image.src = `/static/images/${challenge.image}`;
      image.alt = challenge.name;
      const visual = window.gameVisuals.challengeVisual({ ...challenge, challengeIndex: state.currentChallengeIndex }, state.location, state.missionName);
      window.gameVisuals.paint(document.getElementById("challengeScene"), visual.cell, visual.source, visual.alt);

      if (state.status === "active" && timerChallengeIndex !== state.currentChallengeIndex) {
        timerChallengeIndex = state.currentChallengeIndex;
        challengeEndsAt = state.endsAt || Date.now() / 1000 + CHALLENGE_SECONDS;
        timedOutChallengeIndex = null;
      }
      if (state.status !== "active") {
        challengeEndsAt = null;
      }
    }
    const active = state.status === "active";
    const available = state.inventory.filter((item) => !item.used);
    if (!available.some((item) => item.id === selectedItemId)) selectedItemId = null;

    itemGrid.replaceChildren();
    if (!state.inventory.length) {
      const empty = document.createElement("p");
      empty.className = "empty-inventory";
      empty.textContent = "Your crew has no equipment. You can still take the long way round and continue without an item.";
      itemGrid.appendChild(empty);
    }
    state.inventory.forEach((item) => {
      const usable = active && submittedVote === undefined && !item.used;
      const voteSubmittedForItem = active && submittedVote === item.id;
      const usedForThisChallenge = state.outcome?.item?.id === item.id;
      const card = document.createElement("button");
      card.type = "button";
      card.className = "item-card";
      card.dataset.status = item.used ? "used" : "available";
      card.dataset.selected = String(selectedItemId === item.id);
      card.dataset.voteSubmitted = String(voteSubmittedForItem);
      card.disabled = !usable;
      card.setAttribute("aria-pressed", String(selectedItemId === item.id));
      card.innerHTML = `<span class="item-icon"><img src="/static/images/${item.image}" alt=""></span><span class="item-name"></span><span class="item-status-pill"></span>`;
      card.querySelector('.item-icon').replaceChildren(window.gameVisuals.itemArt(item));
      card.querySelector(".item-name").textContent = item.name;
      card.querySelector(".item-status-pill").textContent = item.used
        ? "Used"
        : usedForThisChallenge
          ? "Used"
          : voteSubmittedForItem
            ? "Vote submitted"
            : "Owned";
      if (usable) card.addEventListener("click", () => {
        selectedItemId = selectedItemId === item.id ? null : item.id;
        applyState(state);
      });
      itemGrid.appendChild(card);
    });

    hotbarLabel.textContent = `TEAM INVENTORY · ${available.length}/${state.inventory.length} AVAILABLE · SCORE ${state.score}`;
    hotbarSlots.replaceChildren();
    (state.inventorySlots || state.inventory).forEach((item) => {
      if (!item) {
        const slot = document.createElement("div");
        slot.className = "hotbar-slot blocked";
        slot.textContent = "";
        slot.title = "No item purchased this round";
        slot.setAttribute("aria-label", slot.title);
        hotbarSlots.appendChild(slot);
        return;
      }
      const slot = document.createElement("div");
      slot.className = "hotbar-slot filled";
      slot.dataset.status = item.used ? "used" : "available";
      slot.title = `${item.name}${item.used ? " (used)" : ""}`;
      slot.innerHTML = `<img src="/static/images/${item.hotbar_image || item.image}" alt="${item.name}">`;
      slot.replaceChildren(window.gameVisuals.itemArt(item));
      hotbarSlots.appendChild(slot);
    });

    useItemBtn.disabled = !active || submittedVote !== undefined || !selectedItemId;
    continueBtn.disabled = !active || submittedVote !== undefined;
    useItemBtn.dataset.submitted = String(submittedVote !== undefined && submittedVote !== "__continue__");
    continueBtn.dataset.submitted = String(submittedVote === "__continue__");
    const tally = Object.entries(state.voteTally || {})
      .map(([id, count]) => `${id === "__continue__" ? "No item" : (state.inventory.find((item) => item.id === id)?.name || id)}: ${count}`)
      .join(" · ");
    document.getElementById("voteStatus").textContent = submittedVote !== undefined
      ? `Your vote is submitted. Votes: ${state.voteCount}/${state.playerCount}${tally ? ` · ${tally}` : ""}`
      : `Votes submitted: ${state.voteCount}/${state.playerCount}${tally ? ` · ${tally}` : ""}`;

    if (state.status === "resolved" && state.outcome) {
      feedbackBox.dataset.outcome = state.outcome.success ? "success" : "fail";
      feedbackTitle.textContent = state.outcome.title;
      const scoreChange = state.outcome.pointsEarned
        ? ` Score +${state.outcome.pointsEarned}.`
        : " Score 0.";
      feedbackSub.textContent = `${state.outcome.description}${scoreChange}`;
      show(feedbackPopup);
    } else {
      hide(feedbackPopup);
    }
  }

  function resetJourneyNodes() {
    journeyNodes.forEach((node) => {
      node.classList.remove("completed");
      node.classList.remove("active");
    });
  }

  function updateJourneyNodes(currentIndex, targetIndex) {

    resetJourneyNodes();

    journeyNodes.forEach((node, index) => {

      const challengeNumber = index + 1;

      /* Challenges before the destination have already been completed.*/
      if (challengeNumber <= currentIndex) {
        node.classList.add("completed");
      }

      /* The challenge we are travelling towards gets the large pulsing destination effect.*/
      if (challengeNumber === targetIndex) {
        node.classList.add("active");
      }

    });
  }

  function getPathPosition(progress) {
    const length = journeyPath.getTotalLength();

    const point = journeyPath.getPointAtLength(
      length * progress
    );

    return {
      x: point.x,
      y: point.y
    };
  }


  function setRunnerPosition(progress) {
    const point = getPathPosition(progress);

    if (journeyPathEnergy && journeyPath) {
      const pathLength = journeyPath.getTotalLength();
      journeyPathEnergy.style.strokeDasharray = `${pathLength}`;
      journeyPathEnergy.style.strokeDashoffset = `${pathLength * (1 - progress)}`;
    }

    journeyRunner.style.left =
      `${point.x / 1000 * 100}%`;

    journeyRunner.style.top =
      `${point.y / 600 * 100}%`;
  }

  function getNodePathProgress(nodeNumber) {
    const nodeCoordinates = [
      { x: 90,  y: 480 },
      { x: 250, y: 300 },
      { x: 430, y: 500 },
      { x: 610, y: 190 },
      { x: 770, y: 390 },
      { x: 930, y: 110 },
    ];

    const target = nodeCoordinates[nodeNumber - 1];

    if (!target) return 0;

    const totalLength = journeyPath.getTotalLength();

    let closestLength = 0;
    let closestDistance = Infinity;

    // Sample the path to find the point closest to the node.
    for (let i = 0; i <= 1000; i++) {
      const length = (i / 1000) * totalLength;
      const point = journeyPath.getPointAtLength(length);

      const dx = point.x - target.x;
      const dy = point.y - target.y;
      const distance = dx * dx + dy * dy;

      if (distance < closestDistance) {
        closestDistance = distance;
        closestLength = length;
      }
    }

    return closestLength / totalLength;
  }

  function createJourneyParticle() {
    const particle =
      document.createElement("div");

    particle.className =
      "journey-particle";

    /* start around the travelling marker.*/
    const runnerRect =
      journeyRunner.getBoundingClientRect();

    const mapRect =
      journeyParticles.getBoundingClientRect();

    particle.style.left =
      `${runnerRect.left - mapRect.left + runnerRect.width / 2}px`;

    particle.style.top =
      `${runnerRect.top - mapRect.top + runnerRect.height / 2}px`;

    /* ran burst direction.*/
    const angle =
      Math.random() * Math.PI * 2;

    const distance =
      15 + Math.random() * 45;

    particle.style.setProperty(
      "--dx",
      Math.cos(angle) * distance
    );

    particle.style.setProperty(
      "--dy",
      Math.sin(angle) * distance
    );

    journeyParticles.appendChild(particle);

    setTimeout(() => {
      particle.remove();
    }, 950);
  }


  function startJourneyParticles() {

    const particleInterval =
      setInterval(() => {

        if (!transitioning) {
          clearInterval(particleInterval);
          return;
        }

        for (let i = 0; i < 3; i++) {
          createJourneyParticle();
        }

      }, 90);

    return particleInterval;
  }

  function playArrivalBurst(targetIndex) {

    const targetNode =
      journeyNodes[targetIndex - 1];

    if (!targetNode) return;

    const mapRect =
      document
        .querySelector(".journey-map")
        .getBoundingClientRect();

    const nodeRect =
      targetNode.getBoundingClientRect();

    arrivalBurst.style.left =
      `${nodeRect.left - mapRect.left + nodeRect.width / 2}px`;

    arrivalBurst.style.top =
      `${nodeRect.top - mapRect.top + nodeRect.height / 2}px`;

    arrivalBurst.classList.remove("play");

    /* force browser to restart the animation.*/
    void arrivalBurst.offsetWidth;

    arrivalBurst.classList.add("play");
  }

function animateJourney(fromChallenge, toChallenge) {

    const startProgress =
      getNodePathProgress(fromChallenge);

    const endProgress =
      getNodePathProgress(toChallenge);

    const duration =
      JOURNEY_TRAVEL_MS;

    const startTime =
      performance.now();

    setRunnerPosition(startProgress);

    journeyRunner.style.opacity = "1";

    function frame(now) {

      const elapsed =
        now - startTime;

      const rawProgress =
        Math.min(
          elapsed / duration,
          1
        );

      const easedProgress =
        rawProgress < 0.5
          ? 2 * rawProgress * rawProgress
          : 1 -
            Math.pow(
              -2 * rawProgress + 2,
              2
            ) / 2;

      const pathProgress =
        startProgress +
        (endProgress - startProgress) *
        easedProgress;

      setRunnerPosition(pathProgress);

      if (rawProgress < 1) {

        journeyAnimationFrame = requestAnimationFrame(frame);

      } else {
        setRunnerPosition(endProgress);

        playArrivalBurst(toChallenge);

        journeyNodes[toChallenge - 1]
          ?.classList.add("completed");

      }
    }

    journeyAnimationFrame = requestAnimationFrame(frame);
  }

  function finishJourneyTransition() {
    journeyTimers.forEach(clearTimeout);
    journeyTimers = [];
    if (journeyAnimationFrame !== null) {
      cancelAnimationFrame(journeyAnimationFrame);
      journeyAnimationFrame = null;
    }
    // Prefer the newest socket snapshot received during the animation so a
    // skipped transition cannot restore an older inventory state.
    const finalState = pendingState || activeTransitionState;
    pendingState = null;
    if (finalState) applyState(finalState);
    missionTransition.classList.remove("active");
    journeyRunner.style.opacity = "0";
    transitioning = false;
    activeTransitionState = null;

  }

function playChallengeTransition(next) {

    transitioning = true;
    activeTransitionState = next;
    journeyTimers.forEach(clearTimeout);
    journeyTimers = [];

    hide(feedbackPopup);

    const fromChallenge =
      (state?.currentChallengeIndex ?? 0) + 1;

    const toChallenge =
      next.currentChallengeIndex + 1;


    /*Safety check. There should only be six challenges. */
    if (
      fromChallenge < 1 ||
      fromChallenge > JOURNEY_NODE_COUNT ||
      toChallenge < 1 ||
      toChallenge > JOURNEY_NODE_COUNT
    ) {

      applyState(next);

      transitioning = false;

      return;
    }

    missionTransition.classList.add("active");

    updateJourneyNodes(
      fromChallenge,
      toChallenge
    );

    journeyRunner.style.opacity = "0";

    setRunnerPosition(
      getNodePathProgress(fromChallenge)
    );

    // Display the appropriate intermission description
    const descKey = `challenge_${fromChallenge}_to_${toChallenge}_desc`;
    const briefingText = challengeDescs[descKey] || challengeDescs.mission_start_desc || state?.missionDescription || "";
    journeyBriefingDesc.textContent = briefingText;
    document.getElementById("journeyBriefingTitle").textContent = `CHALLENGE ${toChallenge}`;

    /*give the browser a moment to render the map before starting the actual movement.*/
    journeyTimers.push(setTimeout(() => {

      journeyRunner.style.opacity = "1";

      startJourneyParticles();

      animateJourney(
        fromChallenge,
        toChallenge
      );

    }, 350));


    // Keep the briefing visible after the journey animation ends. The team
    // advances to the next challenge only when they press Skip.
  }

  function render(next) {

    if (transitioning) {

      pendingState = next;

      return;
    }

    const advancingToNewChallenge =
      state &&
      next.challenge &&
      next.status === "active" &&
      lastChallengeIndex !== null &&
      next.currentChallengeIndex !== lastChallengeIndex;

    lastChallengeIndex =
      next.currentChallengeIndex;

    if (advancingToNewChallenge) {

      playChallengeTransition(next);

    } else {

      applyState(next);

    }
  }

  useItemBtn.addEventListener("click", () => {
    if (!selectedItemId || submittedVotes[state.currentChallengeIndex] !== undefined) return;
    submittedVotes[state.currentChallengeIndex] = selectedItemId;
    action("mission_use_item", { itemId: selectedItemId });
    applyState(state);
  });
  continueBtn.addEventListener("click", () => {
    if (submittedVotes[state.currentChallengeIndex] !== undefined) return;
    submittedVotes[state.currentChallengeIndex] = "__continue__";
    action("mission_continue");
    applyState(state);
  });
  feedbackClose.addEventListener("click", () => {
    if (state && (state.status === "resolved" || timedOutChallengeIndex === state.currentChallengeIndex)) {
      action("mission_advance");
    }
  });
  journeyBriefingBtn.addEventListener("click", () => {
    if (showingFinalFailure) {
      window.location.replace("/result_page");
      return;
    }
    finishJourneyTransition();
  });
  document.getElementById("instructionsBtn").addEventListener("click", () => show(instructionsPopup));
  document.getElementById("instructionsClose").addEventListener("click", () => hide(instructionsPopup));
  instructionsPopup.addEventListener("click", (event) => {
    if (event.target === instructionsPopup) hide(instructionsPopup);
  });
  window.gameSocket.on("mission_state", (data) => {
    // Store challenge descriptions when received
    if (data.challengeDescs) {
      challengeDescs = data.challengeDescs;
    }
    render(data);
  });
  window.gameSocket.on("mission_final_failure", (description) => {
    showingFinalFailure = true;
    clearTimeout(finalFailureTimer);
    missionTransition.classList.add("active", "final-failure");
    journeyBriefingDesc.textContent = description || "Your team has reached the mission's failure limit.";
    document.getElementById("journeyBriefingTitle").textContent = "MISSION FAILED · 3 FAILURES";
    journeyBriefingBtn.querySelector(".briefing-btn-text").textContent = "VIEW RESULTS";
    journeyBriefingBtn.setAttribute("aria-label", "Continue to mission results");
    finalFailureTimer = setTimeout(() => window.location.replace("/result_page"), 7000);
  });
  window.gameSocket.on("mission_complete", () => window.location.replace("/result_page"));
});
