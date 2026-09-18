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
  ['arctic', 'desert', 'jungle'].forEach(source => {
    assets[`${source}-challenges`] = { url: `${root}${source}-challenges-v1.png`, grid: 6 };
  });
  assets.phases = { url: `${root}crew-phases-v1.png`, grid: 6 };
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
  function planningVisual(key = `briefing-plan-${pageVisit}`) {
    return { ...(chooseVisual([...cells('phases', 9, 17), ...planningScenes], key) || planningScenes[0]),
      alt: 'Teammates planning their expedition.' };
  }

  function readPreference(key) { try { return localStorage.getItem(key); } catch { return null; } }
  function savePreference(key, value) { try { localStorage.setItem(key, value); } catch { /* Storage may be disabled. */ } }
  const room = sessionStorage.getItem('sessionCode') || 'preview';
  let sceneRun;
  try { sceneRun = JSON.parse(sessionStorage.getItem('cc-scene-run')); } catch { /* Start a fresh deck. */ }
  if (!sceneRun || sceneRun.room !== room) sceneRun = { room, used: [], assigned: {}, visits: 0 };
  const pageVisit = ++sceneRun.visits;
  function cells(source, first, last) {
    return Array.from({ length: last - first + 1 }, (_, index) => ({ source, cell: first + index }));
  }
  function chooseVisual(candidates, key) {
    if (sceneRun.assigned[key]) return sceneRun.assigned[key];
    let available = candidates.filter(scene => !sceneRun.used.includes(`${scene.source}:${scene.cell}`));
    if (!available.length) return null;
    const rank = Math.min(...available.map(scene => scene.rank || 0));
    available = available.filter(scene => (scene.rank || 0) === rank);
    let history;
    try { history = JSON.parse(readPreference('cc-scene-history')) || []; } catch { history = []; }
    available.sort((a, b) => history.lastIndexOf(`${a.source}:${a.cell}`) - history.lastIndexOf(`${b.source}:${b.cell}`));
    const oldest = history.lastIndexOf(`${available[0].source}:${available[0].cell}`);
    const fresh = available.filter(scene => history.lastIndexOf(`${scene.source}:${scene.cell}`) === oldest);
    const selected = fresh[Math.floor(Math.random() * fresh.length)];
    sceneRun.used.push(`${selected.source}:${selected.cell}`);
    sceneRun.assigned[key] = selected;
    try { sessionStorage.setItem('cc-scene-run', JSON.stringify(sceneRun)); } catch { /* Keep the in-memory deck. */ }
    history.push(`${selected.source}:${selected.cell}`);
    savePreference('cc-scene-history', JSON.stringify(history.slice(-600)));
    return selected;
  }
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let motion = !reducedMotion.matches;
  function updateMotion() {
    document.documentElement.classList.toggle('motion-paused', !motion);
    document.dispatchEvent(new Event('game-motion-change'));
  }
  reducedMotion.addEventListener('change', () => { motion = !reducedMotion.matches; updateMotion(); });
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
    const original = { cell: originalLocations[location] ?? 0, source: originalLocations[location] !== undefined ? 'missions' : assets[biomeSources[location]] ? biomeSources[location] : 'preparation' };
    const extra = assets[`${biomeSources[location]}-challenges`] ? cells(`${biomeSources[location]}-challenges`, 32, 33) : [];
    const selected = chooseVisual([original, ...extra], `location-${location}-${pageVisit}`) || original;
    return { ...selected, alt: `An expedition team surveying the terrain in ${location}.` };
  }

  function missionVisual(location, name, variation = 0) {
    const target = name === 'Artifact Heist' ? 'artifact' : name === 'Jewel Heist' ? 'jewel' : null;
    if (target && Number.isInteger(targetCells[location])) {
      const first = targetCells[location] + (target === 'jewel' ? 8 : 0);
      const selected = chooseVisual(cells('targets', first, first + 1), `objective-${location}-${name}-${pageVisit}-${variation}`)
        || planningVisual(`objective-plan-${location}-${name}-${pageVisit}-${variation}`);
      return { ...selected,
        alt: selected.source === 'targets' ? `${catalog.targets[location]?.[target] || 'The mission treasure'} secured inside a ${location.toLowerCase()} facility.` : `The crew planning the ${name} in ${location}.` };
    }
    const original = { cell: assets[biomeSources[location]] ? missionCells[name] ?? 0 : originalObjectives[name] ?? 0, source: assets[biomeSources[location]] ? biomeSources[location] : 'missions' };
    const selected = chooseVisual([original], `objective-${location}-${name}-${pageVisit}-${variation}`)
      || planningVisual(`objective-plan-${location}-${name}-${pageVisit}-${variation}`);
    return { ...selected, alt: `Concept art for ${name}; the briefing describes the mission's ${location || 'field'} setting.` };
  }

  function challengeVisual(challenge, location = '', missionName = '', context = 'play') {
    const type = challenge.type || '';
    const name = (challenge.name || '').toLowerCase();
    const source = `${biomeSources[location]}-challenges`;
    let theme = 16;
    if (/sinkhole|crevasse|earthquake/.test(name)) theme = 0;
    else if (/guard|patrol|stealth|pursuer|pickpocket/.test(name)) theme = 2;
    else if (/laser/.test(name)) theme = 3;
    else if (/camera|alarm/.test(name)) theme = 5;
    else if (type === 'Contact Teammate/s' || /contact|signal|alert/.test(name)) theme = 6;
    else if (type === 'Find Water') theme = 8;
    else if (type === 'Find Shelter') theme = 7;
    else if (type === 'Make Repairs') theme = 12;
    else if (type === 'System Failure' || /offline|reactor|failure/.test(name)) theme = 13;
    else if (/air based/.test(name)) theme = 10;
    else if (/water based|canal|sea mines|ship graveyard|fishing net/.test(name)) theme = 11;
    else if (['Getaway', 'Travel To Rendezvouz'].includes(type) || /land based|sand based|snow based|desert basin/.test(name)) theme = 9;
    else if (/locked|entrance|exit|staff only/.test(name)) theme = 4;
    else if (type === 'Steal') theme = 17;
    else if (/building|fortefied|wall|blockade|checkpoint|gate|dam/.test(name)) theme = 1;
    else if (/bear|crocodile|shark|snake|insect|scorpion/.test(name)) theme = 15;
    else if (/ash|blizzard|cyclone|heat|fire|flood|storm|temperature|gas|mirage|lava/.test(name)) theme = 14;
    let primary = assets[source] ? cells(source, theme * 2, theme * 2 + 1) : [];
    if (theme === 15 && location !== 'Arctic Tundra') {
      if (/crocodile|scorpion/.test(name)) primary = primary.slice(0, 1);
      else if (/snake/.test(name)) primary = primary.slice(1);
      else primary = [];
    }
    if (/deadly insects|marshland gases|frozen lake|fallen trees|thorn|kelp/.test(name)) primary = [];
    const terrain = assets[source] && theme === 0 ? cells(source, 32, 33).map(scene => ({ ...scene, rank: 1 })) : [];
    const preparation = [...cells('phases', 9, 17), ...[0, 1, 6, 7, 18, 19, 20, 21, 23, 26].map(cell => ({ source: 'phases', cell }))].map(scene => ({ ...scene, rank: 2 }));
    const key = `challenge-${context}-${location}-${missionName}-${challenge.challengeIndex ?? name}`;
    const selected = chooseVisual([...primary, ...terrain, ...preparation], key) || planningVisual();
    return { ...selected, alt: selected.source === 'phases' ? `The crew planning how to tackle ${challenge.name} in ${location}.` : `The crew assessing ${challenge.name} in ${location}.` };
  }

  function createReel({ render, length, interval = 6500, initialIndex = 0 }) {
    let index = initialIndex;
    let timer = null;
    let shown = 1;
    function sync() {
      clearInterval(timer);
      timer = null;
      if (motion && !document.hidden && shown < length) timer = setInterval(() => {
        index = (index + 1) % length;
        shown++;
        if (render(index) === false || shown >= length) clearInterval(timer);
      }, interval);
    }
    if (render(index) === false) shown = length;
    sync();
    document.addEventListener('game-motion-change', sync);
    document.addEventListener('visibilitychange', sync);
    window.addEventListener('pagehide', () => clearInterval(timer));
    window.addEventListener('pageshow', sync);
  }

  window.gameVisuals = { paint, itemArt, challengeVisual, missionVisual, locationVisual, planningVisual, createReel, nextVariant, motionEnabled: () => motion };
  document.querySelectorAll('.game-scene[data-scene]').forEach(frame => {
    if (!frame.closest('[data-phase]') && frame.id !== 'previewArt') paint(frame, Number(frame.dataset.scene), frame.dataset.source || 'game');
  });
  const phaseScenes = { lobby: cells('phases', 0, 8), planning: cells('phases', 9, 17), shop: cells('phases', 18, 26), return: cells('phases', 27, 35) };
  document.querySelectorAll('[data-phase]').forEach(banner => {
    const phase = banner.dataset.phase;
    const frame = banner.querySelector('.game-scene');
    const scenes = phaseScenes[phase];
    if (!frame || !scenes) return;
    createReel({ length: scenes.length, interval: 7200, initialIndex: nextVariant(phase, scenes.length), render(index) {
      const selected = chooseVisual(scenes, `phase-${phase}-${pageVisit}-${index}`);
      if (!selected) return false;
      paint(frame, selected.cell, selected.source, `The expedition crew ${phase === 'return' ? 'returning from their adventure' : phase === 'shop' ? 'visiting an equipment supplier' : phase === 'planning' ? 'planning their mission' : 'gathering before their mission'}.`);
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
  createReel({ length: frames.length, initialIndex: nextVariant('preview-start', frames.length), render(index) {
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
