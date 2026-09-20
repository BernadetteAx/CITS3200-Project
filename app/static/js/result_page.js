document.addEventListener("DOMContentLoaded", () => {
    const socket = window.gameSocket;
    const message = document.getElementById("result-message");
    let hasResults = false;
    let challengePage = 0;
    function renderChallengePage() {
      const cards = [...document.querySelectorAll("#challenge-results > article")];
      const paged = window.innerWidth < 700;
      cards.forEach((card, index) => { card.hidden = paged && index !== challengePage; });
      document.querySelector(".challenge-pages").hidden = !paged || cards.length < 2;
      document.getElementById("challengeResultPage").textContent = `${cards.length ? challengePage + 1 : 0} / ${cards.length}`;
      document.getElementById("previousChallengeResult").disabled = challengePage === 0;
      document.getElementById("nextChallengeResult").disabled = challengePage >= cards.length - 1;
    }
    document.getElementById("previousChallengeResult").addEventListener("click", () => { challengePage--; renderChallengePage(); });
    document.getElementById("nextChallengeResult").addEventListener("click", () => { challengePage++; renderChallengePage(); });
    window.addEventListener("resize", renderChallengePage);
  
    function setText(id, value) {
      document.getElementById(id).textContent = value ?? "---";
    }
  
    function addDetail(parent, label, value, className = "") {
      const paragraph = document.createElement("p");
      paragraph.textContent = `${label}: ${value ?? "---"}`;
  
      if (className) paragraph.className = className;
  
      parent.appendChild(paragraph);
    }
  
    function displayChallenges(challenges, location, missionName) {
      const list = document.getElementById("challenge-results");
      list.replaceChildren();
  
      if (challenges.length === 0) {
        const empty = document.createElement("p");
        empty.textContent = "No challenge results recorded.";
        list.appendChild(empty);
        return;
      }
  
      challenges.forEach((challenge) => {
        const card = document.createElement("article");
        card.className = "mission-card";
        card.dataset.outcome = challenge.success ? "success" : "fail";
        const art = document.createElement("div");
        art.className = "game-scene result-challenge-art";
        art.setAttribute("role", "img");
        const visual = window.gameVisuals.challengeVisual(challenge, location, missionName, 'results');
        window.gameVisuals.paint(art, visual.cell, visual.source, visual.alt);
  
        const info = document.createElement("div");
        info.className = "mission-info";
  
        const heading = document.createElement("h3");
        heading.textContent =
          `CHALLENGE ${challenge.challengeIndex + 1}: ${challenge.name}`;
        info.appendChild(heading);
  
        addDetail(
          info,
          "Item used",
          challenge.itemUsed?.name ?? "No item used"
        );
  
        // Challenge Card Detail - START
        // Prefer the item's point_desc from game_data over the generic
        // "gets the team past the challenge" sentence. Falls back when a
        // challenge has no point copy recorded.
        const outcomeText = challenge.pointDesc ?? challenge.description;

        if (outcomeText) {
          const description = document.createElement("p");
          description.textContent = outcomeText;
          info.appendChild(description);
        }
        // Challenge Card Detail - END
  
        const status = document.createElement("div");
        status.className = "mission-status";
  
        addDetail(
          status,
          "Result",
          challenge.success ? "Passed" : "Failed",
          "challenge-outcome"
        );
  
        // Challenge Card Detail - START
        // Show the item's point_value from game_data. Falls back to the
        // penalty for challenges with no point value recorded.
        if (challenge.pointValue != null) {
          addDetail(status, "Points", challenge.pointValue);
        } else {
          addDetail(status, "Penalty points", challenge.penalty);
        }
        // Challenge Card Detail - END
  
        card.append(art, info, status);
        list.appendChild(card);
      });
      renderChallengePage();
    }
  
    function displayItems(listId, emptyId, items) {
      const list = document.getElementById(listId);
      list.replaceChildren();
  
      document.getElementById(emptyId).hidden = items.length !== 0;
  
      items.forEach((item) => {
        const entry = document.createElement("li");
        if (item.hotbar_image || item.image) {
          entry.appendChild(window.gameVisuals.itemArt(item));
        }
        entry.append(document.createTextNode(item.name ?? item.id));
        list.appendChild(entry);
      });
    }
  
    function displayResults(result) {
      hasResults = true;
  
      setText("final-score", result.finalScore);
  
      // Mission Achievement - START
      // The LEFTOVER MONEY panel was replaced by MISSION ACHIEVEMENT, so
      // #leftover-money no longer exists. setText() does not null-check,
      // so this call has to go or displayResults() throws. The achievement
      // panel is rendered separately by result_achievement.js.
      // Mission Achievement - END

      setText(
        "completion-status",
        result.completionStatus === "complete"
          ? "Complete"
          : result.completionStatus
      );
  
      setText("challenges-completed", result.challengesCompleted);
      setText("total-challenges", result.totalChallenges);
      setText("challenges-passed", result.challengesPassed);
      setText("challenges-failed", result.challengesFailed);
      // setText("total-penalties", result.totalPenalties);
  
      const hasOutcome =
        result.missionOutcome != null && result.missionOutcome !== "";
  
      document.getElementById("mission-outcome-row").hidden = !hasOutcome;
      setText("mission-outcome", result.missionOutcome);
  
      displayChallenges(result.challenges ?? [], result.location, result.missionName);
  
      displayItems(
        "items-purchased",
        "no-purchased-items",
        result.itemsPurchased ?? []
      );
  
      displayItems(
        "items-used",
        "no-used-items",
        result.itemsUsed ?? []
      );
  
      message.textContent = "YOUR TEAM'S FINAL RESULTS";
    }
  
    if (!socket) {
      message.textContent =
        "Unable to connect to the game. Please refresh the page.";
      return;
    }
  
    socket.on("result_state", displayResults);
  
    socket.on("result_error", (payload) => {
      message.textContent =
        payload?.message ?? "Unable to load this game's results.";
    });
  
    socket.on("disconnect", () => {
      message.textContent = hasResults
        ? "Connection lost. Showing the last received results."
        : "Connection lost. Waiting to reconnect…";
    });
  
    socket.on("connect", () => {
      message.textContent = "Loading your team's results…";
    });
  
    socket.on("connect_error", () => {
      message.textContent =
        "Unable to connect. Waiting to retry…";
    });
  });
