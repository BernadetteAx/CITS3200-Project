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
          addDetail(status, "Points Earned", challenge.penalty);
        }
        // Challenge Card Detail - END
  
        card.append(art, info, status);
        list.appendChild(card);
      });
      renderChallengePage();
    }
  
    // Item Inventory - START
    // Renders ONE inventory list from itemsPurchased, marking each entry
    // active when its id appears in itemsUsed. Replaces the former pair of
    // "purchased" / "used" lists. The payload is read as-is; nothing here
    // changes result data or window.gameVisuals.
    function displayItems(purchased, used) {
      const list = document.getElementById("item-inventory");
      const empty = document.getElementById("no-inventory-items");
      if (!list || !empty) return;

      list.replaceChildren();

      const keyOf = (item) => item.id ?? item.name;
      const usedIds = new Set(used.map(keyOf));
      const rendered = new Set();

      const addEntry = (item, active) => {
        const entry = document.createElement("li");
        entry.className = "inventory-item";
        entry.dataset.state = active ? "active" : "inactive";

        // Row: sprite on the left, then a name/badge stack on the right.
        // The sprite sits directly in the cell — the active highlight is
        // drawn on its own edge, so there is no wrapper box around it.
        if (item.hotbar_image || item.image) {
          entry.appendChild(window.gameVisuals.itemArt(item));
        }

        // Unstyled grouping for the text stack; not a box.
        const text = document.createElement("span");
        text.className = "inventory-text";

        const name = document.createElement("span");
        name.className = "inventory-name";
        name.textContent = item.name ?? item.id;
        text.appendChild(name);

        // Status is stated in text, not colour alone.
        if (active) {
          const badge = document.createElement("span");
          badge.className = "inventory-badge";
          badge.textContent = "[ACTIVE]";
          text.appendChild(badge);
        }

        entry.appendChild(text);

        list.appendChild(entry);
        rendered.add(keyOf(item));
      };

      purchased.forEach((item) => addEntry(item, usedIds.has(keyOf(item))));

      // Defensive: a used item with no purchase record still shows, as active,
      // rather than vanishing from the debrief.
      used.forEach((item) => {
        if (!rendered.has(keyOf(item))) addEntry(item, true);
      });

      empty.hidden = rendered.size !== 0;
    }
    // Item Inventory - END
  
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
  
      // Item Inventory - START
      displayItems(result.itemsPurchased ?? [], result.itemsUsed ?? []);
      // Item Inventory - END
  
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
