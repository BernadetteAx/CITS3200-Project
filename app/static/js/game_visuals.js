(() => {
  const assets = {
    game: document.body.dataset.gameAtlas,
    missions: document.body.dataset.missionAtlas,
    preparation: document.body.dataset.preparation,
  };
  const locationCells = { "Arctic Tundra": 0, Desert: 1, Jungle: 2, City: 3, Ocean: 4, Volcano: 5 };
  const missionCells = { "Train Heist": 6, "Artifact Heist": 7, "Jewel Heist": 8, "Steal Enemy Information": 9, "Escape Enemy Base": 10, "Break Out Another Team": 11, "Extract Another Team": 12, "Rescue Stranded Teammate": 13, "Repair Research Base": 14, "Get Rescued": 15 };

  function paint(frame, cell, source = "game", alt = null) {
    if (!frame || !assets[source]) return;
    const key = `${source}:${cell}`;
    if (alt) frame.setAttribute("aria-label", alt);
    if (frame.dataset.visualKey === key) return;
    frame.dataset.visualKey = key;
    let layers = [...frame.querySelectorAll(".scene-layer")];
    if (!layers.length) {
      layers = [document.createElement("div"), document.createElement("div")];
      layers.forEach((layer) => { layer.className = "scene-layer"; layer.setAttribute("aria-hidden", "true"); frame.prepend(layer); });
    }
    const next = layers.find((layer) => !layer.classList.contains("is-active")) || layers[0];
    const grid = source === "game" ? 3 : source === "missions" ? 4 : 1;
    const position = grid > 1 ? `${(cell % grid) * 100 / (grid - 1)}% ${Math.floor(cell / grid) * 100 / (grid - 1)}%` : "center";
    next.style.backgroundImage = `url("${assets[source]}")`;
    next.style.backgroundSize = `${grid * 100}% ${grid * 100}%`;
    next.style.backgroundPosition = position;
    layers.forEach((layer) => layer.classList.toggle("is-active", layer === next));
  }

  function challengeVisual(challenge, location = "", missionName = "") {
    const text = `${challenge.type || ""} ${challenge.name || ""}`.toLowerCase();
    if (/contact|signal|alert.*team/.test(text)) return { cell: 5, source: "game", alt: "Teammates trying to establish radio contact in the field." };
    if (/repair|failure|generator|system/.test(text)) return { cell: 7, source: "game", alt: "Teammates assessing damaged research equipment." };
    if (/shelter|water|food|survival/.test(text)) return { cell: 6, source: "game", alt: "Teammates gathering at a temporary wilderness shelter." };
    if (/\bsteal\b|retrieve/.test(text)) return { cell: missionCells[missionName] ?? 8, source: "missions", alt: "Concept art of the team's secured mission objective." };
    if (/security|guard|lock|door|wall|manmade|laser/.test(text)) return { cell: 4, source: "game", alt: "Teammates assessing a secured entrance." };
    if (/air.*getaway/.test(text)) return { cell: 15, source: "missions", alt: "Teammates signalling a rescue helicopter." };
    if (/getaway|travel|rendez|route|escape/.test(text)) return { cell: 8, source: "game", alt: "Teammates navigating towards a distant rendezvous beacon." };
    if (/bridge|cliff|ravine|tree|rock/.test(text)) return { cell: 3, source: "game", alt: "Teammates assessing a broken crossing in rough terrain." };
    return { cell: locationCells[location] ?? 2, source: "missions", alt: `Concept art of the team's ${location || "wilderness"} mission environment.` };
  }

  // One playback controller: auto flow, explicit pause, and no background timers.
  function createReel({ render, button, length, interval = 6500 }) {
    let index = 0;
    let timer = null;
    let paused = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function sync() {
      clearInterval(timer);
      timer = null;
      button.setAttribute("aria-pressed", String(paused));
      button.textContent = paused ? "RESUME" : "PAUSE";
      button.setAttribute("aria-label", paused ? "Resume rotating illustrations" : "Pause rotating illustrations");
      if (!paused && !document.hidden) timer = setInterval(() => { index = (index + 1) % length; render(index); }, interval);
    }
    render(index);
    sync();
    button.addEventListener("click", () => { paused = !paused; sync(); });
    document.addEventListener("visibilitychange", sync);
    window.addEventListener("pagehide", () => clearInterval(timer));
    window.addEventListener("pageshow", sync);
  }

  window.gameVisuals = { paint, challengeVisual, createReel };
  document.querySelectorAll(".game-scene[data-scene]").forEach((frame) => paint(frame, Number(frame.dataset.scene), frame.dataset.source || "game"));

  const preview = document.getElementById("previewArt");
  if (!preview) return;
  const frames = [
    { cell: 2, source: "missions", eyebrow: "EXPLORE TOGETHER", title: "Deep in the unknown", copy: "From hidden jungle bases to the open ocean, every mission takes your team somewhere new.", alt: "An expedition team entering the jungle." },
    { cell: 6, source: "missions", eyebrow: "PULL OFF THE IMPOSSIBLE", title: "A heist at full speed", copy: "Catch the cargo, slip past security and make your getaway. Your crew's choices shape the adventure.", alt: "An adventure team boarding a moving cargo train." },
    { cell: 12, source: "missions", eyebrow: "BRING THEM HOME", title: "No teammate left behind", copy: "Find missing researchers, answer the call and turn a difficult expedition into a daring rescue.", alt: "A rescue team reaching missing researchers." },
    { cell: 1, source: "game", eyebrow: "GEAR UP AS A TEAM", title: "One budget. Big decisions.", copy: "Vote for equipment together. The right tool can clear an obstacle; an unexpected choice can lead to a costly detour.", alt: "An adventure team inspecting expedition supplies." },
    { cell: 0, source: "missions", eyebrow: "EXPECT THE UNEXPECTED", title: "Out in the elements", copy: "Arctic ridges, scorching dunes and volcanic craters. Make a plan, then adapt when the mission gets chaotic.", alt: "An expedition team approaching a snowy research base under an aurora." },
    { cell: 2, source: "game", eyebrow: "EVERY CHOICE COUNTS", title: "Your crew. Your story.", copy: "Six challenges. A shared score. Whether it's a clean solve or the long way round, you face it together.", alt: "An adventure team returning to their command room together." },
  ];
  createReel({ button: document.getElementById("previewPause"), length: frames.length, render(index) {
    const frame = frames[index];
    paint(preview, frame.cell, frame.source, frame.alt);
    document.getElementById("previewCounter").textContent = `0${index + 1} / 06`;
    document.getElementById("previewEyebrow").textContent = frame.eyebrow;
    document.getElementById("previewTitle").textContent = frame.title;
    document.getElementById("previewCopy").textContent = frame.copy;
    document.querySelectorAll("#previewSteps > span").forEach((step, i) => step.classList.toggle("is-current", i === index));
  }});
})();
