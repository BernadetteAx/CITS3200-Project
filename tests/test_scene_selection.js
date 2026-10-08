const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../app/static/js/game_visuals.js'), 'utf8');
const history = new Map();
function storage(values) {
  return { getItem: key => values.get(key) ?? null, setItem: (key, value) => values.set(key, value) };
}
function game(room, session = new Map()) {
  session.set('sessionCode', room);
  const timers = new Map();
  let timerId = 0;
  const element = () => ({ style: { setProperty() {} }, append() {}, prepend() {}, setAttribute() {}, classList: { toggle() {} } });
  const context = {
    window: { matchMedia: () => ({ matches: false, addEventListener() {} }), addEventListener() {} },
    document: { body: { dataset: { artworkRoot: '/static/images/briefing/' }, prepend() {} }, documentElement: element(),
      hidden: false, createElement: element, getElementById: () => null, querySelectorAll: () => [], addEventListener() {}, dispatchEvent() {} },
    localStorage: storage(history), sessionStorage: storage(session),
    setInterval: fn => { const id = ++timerId; timers.set(id, fn); return id; }, clearInterval: id => timers.delete(id),
    Event: class {}, Image: class {}, Math: Object.create(Math),
  };
  context.Math.random = () => 0;
  vm.runInNewContext(source, context);
  return { visuals: context.window.gameVisuals, timers, session };
}
const key = scene => `${scene.source}:${scene.cell}`;
for (const location of ['Arctic Tundra', 'Desert', 'Jungle']) {
  const run = game(location);
  for (let challengeIndex = 0; challengeIndex < 12; challengeIndex++) {
    const challenge = { name: 'Sinkhole', challengeIndex };
    const played = run.visuals.challengeVisual(challenge, location, 'Escape Enemy Base');
    assert.equal(played.source, `${location === 'Arctic Tundra' ? 'arctic' : location.toLowerCase()}-challenges`);
    assert.ok([0, 1].includes(played.cell));
    assert.equal(key(run.visuals.challengeVisual(challenge, location, 'Escape Enemy Base', 'results')), key(played));
    const reloaded = game(location, run.session);
    assert.equal(key(reloaded.visuals.challengeVisual(challenge, location, 'Escape Enemy Base')), key(played));
  }
  for (let visit = 0; visit < 10; visit++) {
    assert.equal(run.visuals.missionVisual(location, 'Train Heist', visit).source,
      location === 'Arctic Tundra' ? 'arctic' : location.toLowerCase());
  }
}
for (const [artKey, cell] of [['Air Based Getaway', 20], ['Water Based Getaway', 22], ['Air Based Travel', 20], ['Water Based Travel', 22]]) {
  const run = game(artKey);
  const scene = run.visuals.challengeVisual({name: artKey.includes('Travel') ? 'Travel To Rendezvous Point' : 'Getaway', type: artKey.includes('Travel') ? 'Travel To Rendezvous' : 'Getaway', artKey}, 'Jungle');
  assert.equal(scene.cell, cell);
}
const firstRun = game('history-first');
const first = firstRun.visuals.challengeVisual({ name: 'Building', challengeIndex: 0 }, 'Desert');
const second = game('history-second').visuals.challengeVisual({ name: 'Building', challengeIndex: 0 }, 'Desert');
assert.notEqual(key(first), key(second));
const reel = game('reel');
const frames = [];
reel.visuals.createReel({ length: 3, render: index => frames.push(index) });
while (reel.timers.size) [...reel.timers.values()][0]();
assert.deepEqual(frames, [0, 1, 2]);
console.log('Scene selection checks passed: relevant scene reuse, stable results/reconnects, visit history and finite reels.');
