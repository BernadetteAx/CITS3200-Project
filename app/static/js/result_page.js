document.addEventListener("DOMContentLoaded", () => {
    const socket = window.gameSocket;
    const message = document.getElementById("result-message");
    let hasResults = false;
  
    function setText(id, value) {
      document.getElementById(id).textContent = value ?? "---";
    }
  
    function addDetail(parent, label, value, className = "") {
      const paragraph = document.createElement("p");
      paragraph.textContent = `${label}: ${value ?? "---"}`;
  
      if (className) paragraph.className = className;
  
      parent.appendChild(paragraph);
    }
  
    function displayChallenges(challenges) {
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
  
        if (challenge.description) {
          const description = document.createElement("p");
          description.textContent = challenge.description;
          info.appendChild(description);
        }
  
        const status = document.createElement("div");
        status.className = "mission-status";
  
        addDetail(
          status,
          "Result",
          challenge.success ? "Passed" : "Failed",
          "challenge-outcome"
        );
  
        addDetail(status, "Penalty points", challenge.penalty);
  
        card.append(info, status);
        list.appendChild(card);
      });
    }
  
    function displayItems(listId, emptyId, items) {
      const list = document.getElementById(listId);
      list.replaceChildren();
  
      document.getElementById(emptyId).hidden = items.length !== 0;
  
      items.forEach((item) => {
        const entry = document.createElement("li");
        entry.textContent = item.name ?? item.id;
        list.appendChild(entry);
      });
    }
  
    function displayResults(result) {
      hasResults = true;
  
      setText("final-score", result.finalScore);
  
      setText(
        "leftover-money",
        result.leftoverMoney == null ? "$---" : `$${result.leftoverMoney}`
      );
  
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
      setText("total-penalties", result.totalPenalties);
  
      const hasOutcome =
        result.missionOutcome != null && result.missionOutcome !== "";
  
      document.getElementById("mission-outcome-row").hidden = !hasOutcome;
      setText("mission-outcome", result.missionOutcome);
  
      displayChallenges(result.challenges ?? []);
  
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