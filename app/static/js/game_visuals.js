(() => {
  const root = document.body.dataset.artworkRoot;
  const catalog = JSON.parse(document.getElementById('visualCatalog')?.textContent || '{"missions":[],"targets":{}}');
  const biomeSources = { 'Arctic Tundra': 'arctic', Desert: 'desert', Jungle: 'jungle', City: 'city', Ocean: 'ocean', Volcano: 'volcano' };
  const missionCells = { 'Train Heist': 1, 'Artifact Heist': 2, 'Jewel Heist': 3, 'Steal Enemy Information': 4, 'Escape Enemy Base': 5, 'Break Out Another Team': 15, 'Extract Another Team': 7, 'Rescue Stranded Teammate': 8, 'Repair Research Base': 9, 'Get Rescued': 10 };
  const targetCells = { 'Arctic Tundra': 0, Desert: 2, Jungle: 4, City: 6 };
  const assets = {
    game: { url: document.body.dataset.gameAtlas, grid: 3 },
    missions: { url: document.body.dataset.missionAtlas, grid: 4 },
    preparation: { url: document.body.dataset.preparation, grid: 1 },
  };
  ['arctic', 'desert', 'jungle', 'targets'].forEach(source => {
    assets[source] = { url: `${root}${source}-scenes-v2.png`, grid: 4 };
  });
  const originalLocations = { City: 3, Ocean: 4, Volcano: 5 };
  const originalObjectives = { 'Train Heist': 6, 'Artifact Heist': 7, 'Jewel Heist': 8, 'Steal Enemy Information': 9, 'Escape Enemy Base': 10, 'Break Out Another Team': 11, 'Extract Another Team': 12, 'Rescue Stranded Teammate': 13, 'Repair Research Base': 14, 'Get Rescued': 15 };
  const planningScenes = [{ source: 'preparation', cell: 0 }, { source: 'game', cell: 1 }, { source: 'game', cell: 0 }];
  const equipment = [
    ['Fire Starter Kit', 'Handheld Radios', 'Mirror', 'Gas Mask and Knockout Gas', 'Ice Axes', 'Armoured Truck', 'Rope', 'Paraglider', 'Helicopter', 'Grapling Hook', 'Scuba Gear', 'Wire Cutters', 'Explosives', 'Water Bottle', 'Fuel', 'Taser'],
    ['Compass', 'Apple', 'Armoured Boots', 'Camping Tent', 'Hat', 'GPS', 'Map', 'Mountain Gear', 'Car', 'Toolkit', 'Shovel', 'Medical Supplies', 'Weapons', 'Axe', 'Boat', 'Lock Picks'],
    ['Stolen Uniforms', 'Welding Kit', 'Dune Buggy'],
  ];
  function itemArt(item) {
    const group = equipment.findIndex(names => names.includes(item.name));
    if (group < 0) {
      const fallback = document.createElement('img');
      fallback.src = `/static/images/${item.image}`;
      fallback.alt = item.name;
      return fallback;
    }
    const cell = equipment[group].indexOf(item.name);
    const grid = group === 2 ? 2 : 4;
    const art = document.createElement('span');
    art.className = 'equipment-art';
    art.setAttribute('role', 'img');
    art.setAttribute('aria-label', item.name);
    art.dataset.item = item.name;
    art.style.backgroundImage = `url("${root}equipment-${['a', 'b', 'c'][group]}-v1.png")`;
    art.style.backgroundSize = `${grid * 100}% ${grid * 100}%`;
    art.style.backgroundPosition = `${cell % grid * 100 / (grid - 1)}% ${Math.floor(cell / grid) * 100 / (grid - 1)}%`;
    return art;
  }
  function planningVisual() { return { ...planningScenes[nextVariant('planning', planningScenes.length)], alt: 'Teammates discussing their expedition and choosing supplies in headquarters.' }; }

  function readPreference(key) { try { return localStorage.getItem(key); } catch { return null; } }
  function savePreference(key, value) { try { localStorage.setItem(key, value); } catch { /* Storage may be disabled. */ } }
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let motion = readPreference('cc-motion') !== 'off' && !reducedMotion.matches;
  const motionButton = document.createElement('button');
  motionButton.className = 'motion-toggle';
  motionButton.type = 'button';
  if (!document.body.classList.contains('landing-page')) document.body.append(motionButton);
  function updateMotion() {
    document.documentElement.classList.toggle('motion-paused', !motion);
    motionButton.textContent = motion ? 'Ⅱ PAUSE MOTION' : '▶ ENABLE MOTION';
    motionButton.setAttribute('aria-label', motion ? 'Pause background motion and automatic pictures' : 'Enable background motion and automatic pictures');
    motionButton.setAttribute('aria-pressed', String(!motion));
    document.dispatchEvent(new Event('game-motion-change'));
  }
  motionButton.addEventListener('click', () => {
    motion = !motion;
    savePreference('cc-motion', motion ? 'on' : 'off');
    updateMotion();
  });
  reducedMotion.addEventListener('change', () => { motion = !reducedMotion.matches && readPreference('cc-motion') !== 'off'; updateMotion(); });
  updateMotion();

  const ambience = document.createElement('div');
  ambience.className = 'game-ambience';
  ambience.setAttribute('aria-hidden', 'true');
  for (let i = 0; i < 12; i++) {
    const particle = document.createElement('span');
    particle.className = i % 3 === 0 ? 'ambient-particle ambient-square' : 'ambient-particle';
    particle.textContent = i % 3 === 0 ? '' : i % 2 ? '$' : '+';
    particle.style.setProperty('--left', `${3 + i * 8.3}%`);
    particle.style.setProperty('--duration', `${18 + i % 5 * 3}s`);
    particle.style.setProperty('--delay', `${-i * 3.7}s`);
    ambience.append(particle);
  }
  document.body.prepend(ambience);
  document.addEventListener('visibilitychange', () => document.documentElement.classList.toggle('page-hidden', document.hidden));

  // Remember the last variation locally so a return visit starts on a different image.
  function nextVariant(key, length) {
    const stored = readPreference(`cc-art-${key}`);
    const previous = stored === null ? -1 : Number(stored);
    const index = Number.isInteger(previous) && previous >= 0
      ? (previous + 1 + Math.floor(Math.random() * (length - 1))) % length
      : Math.floor(Math.random() * length);
    savePreference(`cc-art-${key}`, String(index));
    return index;
  }

  const loaded = new Map();
  function loadImage(url) {
    if (!loaded.has(url)) loaded.set(url, new Promise(resolve => {
      const image = new Image();
      image.onload = () => resolve(true);
      image.onerror = () => { loaded.delete(url); resolve(false); };
      image.src = url;
    }));
    return loaded.get(url);
  }

  async function paint(frame, cell, source = 'game', alt = null) {
    if (!frame || !assets[source]?.url) return;
    const key = `${source}:${cell}`;
    if (frame.dataset.visualKey === key) return;
    frame.dataset.visualKey = key;
    const { url, grid } = assets[source];
    // Keep the current scene visible while the next atlas downloads.
    if (!await loadImage(url)) { if (frame.dataset.visualKey === key) delete frame.dataset.visualKey; return; }
    if (frame.dataset.visualKey !== key) return;
    if (alt) frame.setAttribute('aria-label', alt);
    let layers = [...frame.querySelectorAll('.scene-layer')];
    if (!layers.length) {
      layers = [document.createElement('div'), document.createElement('div')];
      layers.forEach(layer => { layer.className = 'scene-layer'; layer.setAttribute('aria-hidden', 'true'); frame.prepend(layer); });
    }
    const next = layers.find(layer => !layer.classList.contains('is-active')) || layers[0];
    next.style.backgroundImage = `url("${url}")`;
    next.style.backgroundSize = `${grid * 100}% ${grid * 100}%`;
    next.style.backgroundPosition = grid > 1 ? `${cell % grid * 100 / (grid - 1)}% ${Math.floor(cell / grid) * 100 / (grid - 1)}%` : 'center';
    layers.forEach(layer => layer.classList.toggle('is-active', layer === next));
    frame.dataset.loadedVisual = key;
  }

  function locationVisual(location) {
    return { cell: originalLocations[location] ?? 0, source: originalLocations[location] !== undefined ? 'missions' : assets[biomeSources[location]] ? biomeSources[location] : 'preparation', alt: `An expedition team preparing to explore ${biomeSources[location] ? location : 'their mission'}.` };
  }

  function missionVisual(location, name, variation = 0) {
    const target = name === 'Artifact Heist' ? 'artifact' : name === 'Jewel Heist' ? 'jewel' : null;
    if (target && Number.isInteger(targetCells[location])) {
      return { source: 'targets', cell: targetCells[location] + (target === 'jewel' ? 8 : 0) + variation % 2,
        alt: `${catalog.targets[location]?.[target] || 'The mission treasure'} secured inside a ${location.toLowerCase()} facility.` };
    }
    return { cell: assets[biomeSources[location]] ? missionCells[name] ?? 0 : originalObjectives[name] ?? 0, source: assets[biomeSources[location]] ? biomeSources[location] : 'missions', alt: `Concept art for ${name}; the briefing describes the mission's ${location || 'field'} setting.` };
  }

  function challengeVisual(challenge, location = '', missionName = '') {
    const type = challenge.type || '';
    const name = (challenge.name || '').toLowerCase();
    const source = biomeSources[location];
    if (!assets[source]) return type === 'Steal' ? missionVisual(location, missionName) : locationVisual(location);
    let cell = 0;
    let subject = 'The team exploring the mission environment';
    if (type === 'Steal') return missionVisual(location, missionName);
    if (['Make Repairs', 'System Failure'].includes(type) || /repair|offline|failure|jammed/.test(name)) { cell = 9; subject = 'The team assessing damaged research systems'; }
    else if (type === 'Contact Teammate/s' || /contact|signal|alert/.test(name)) { cell = 13; subject = 'The team trying to establish contact'; }
    else if (['Find Shelter', 'Find Water'].includes(type)) { cell = 14; subject = 'The team managing shelter and limited supplies'; }
    else if (['Getaway', 'Travel To Rendezvouz'].includes(type)) { cell = 15; subject = 'The team approaching a rendezvous'; }
    else if (type === 'Security Obstacle' || /gate|checkpoint|blockade|wall|fortefied|building/.test(name)) { cell = 12; subject = 'The team approaching a secured facility'; }
    else if (/cliff|crevasse|bridge|crossing|ravine/.test(name)) { cell = 11; subject = 'The team facing difficult terrain'; }
    // Other hazards use the real environment without inventing a different obstacle.
    return { cell, source, alt: `${subject} in ${location}.` };
  }

  function createReel({ render, button = null, length, interval = 6500, initialIndex = 0 }) {
    let index = initialIndex;
    let timer = null;
    let paused = false;
    function sync() {
      clearInterval(timer);
      timer = null;
      if (button) {
        button.setAttribute('aria-pressed', String(paused));
        button.textContent = paused ? 'RESUME' : 'PAUSE';
        button.setAttribute('aria-label', paused ? 'Resume rotating illustrations' : 'Pause rotating illustrations');
        button.disabled = !motion;
      }
      if (!paused && motion && !document.hidden && length > 1) timer = setInterval(() => { index = (index + 1) % length; render(index); }, interval);
    }
    render(index);
    sync();
    button?.addEventListener('click', () => { paused = !paused; sync(); });
    document.addEventListener('game-motion-change', sync);
    document.addEventListener('visibilitychange', sync);
    window.addEventListener('pagehide', () => clearInterval(timer));
    window.addEventListener('pageshow', sync);
  }

  window.gameVisuals = { paint, itemArt, challengeVisual, missionVisual, locationVisual, planningVisual, createReel, nextVariant, motionEnabled: () => motion };
  document.querySelectorAll('.game-scene[data-scene]').forEach(frame => {
    if (!frame.closest('[data-phase]') && frame.id !== 'previewArt') paint(frame, Number(frame.dataset.scene), frame.dataset.source || 'game');
  });
  const phaseScenes = { lobby: [{source: 'game', cell: 0}, {source: 'preparation', cell: 0}], planning: planningScenes, shop: [{source: 'game', cell: 1}, {source: 'preparation', cell: 0}], return: [{source: 'game', cell: 2}, {source: 'game', cell: 0}] };
  document.querySelectorAll('[data-phase]').forEach(banner => {
    const phase = banner.dataset.phase;
    const frame = banner.querySelector('.game-scene');
    const scenes = phaseScenes[phase];
    if (!frame || !scenes) return;
    createReel({ length: scenes.length, interval: 7200, initialIndex: nextVariant(phase, scenes.length), render(index) {
      savePreference(`cc-art-${phase}`, String(index));
      paint(frame, scenes[index].cell, scenes[index].source, 'Teammates together in their expedition headquarters.');
    } });
  });

  const preview = document.getElementById('previewArt');
  if (!preview) return;
  // Build one valid mission per environment directly from the game's catalog.
  const frames = Object.keys(biomeSources).map(location => {
    const missions = catalog.missions.filter(mission => mission.locations.includes(location));
    const mission = missions[nextVariant(`preview-${location}`, missions.length)];
    return { location, mission: mission?.name || 'Explore together' };
  });
  createReel({ button: document.getElementById('previewPause'), length: frames.length, initialIndex: nextVariant('preview-start', frames.length), render(index) {
    const { location, mission } = frames[index];
    const frame = missionVisual(location, mission);
    paint(preview, frame.cell, frame.source, frame.alt);
    document.getElementById('previewCounter').textContent = `${String(index + 1).padStart(2, '0')} / 06`;
    document.getElementById('previewEyebrow').textContent = `DESTINATION / ${location.toUpperCase()}`;
    document.getElementById('previewTitle').textContent = mission;
    document.getElementById('previewCopy').textContent = `${location}. One shared budget. Six challenges. Plan with your crew, choose your equipment and face the unexpected together.`;
    document.querySelectorAll('#previewSteps > span').forEach((step, i) => step.classList.toggle('is-current', i === index));
  } });
})();
