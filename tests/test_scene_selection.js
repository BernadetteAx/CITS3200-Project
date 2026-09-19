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
const screenshot = game('screenshot');
const names = ['Sinkhole', 'Building', 'Distract Guards', 'Retrieve the Item from the Laser Grid', 'Sinkhole', 'Land Based Getaway'];
const scenes = names.map((name, challengeIndex) => screenshot.visuals.challengeVisual({ name, challengeIndex }, 'Desert', 'Artifact Heist', 'results'));
assert.equal(new Set(scenes.map(key)).size, 6);
assert.deepEqual(scenes.map(s => s.cell), [0, 2, 4, 6, 1, 18]);
for (const location of ['Arctic Tundra', 'Desert', 'Jungle', 'City', 'Ocean', 'Volcano']) {
  const run = game(location);
  const chosen = [];
  for (const context of ['play', 'results']) {
    for (let challengeIndex = 0; challengeIndex < 6; challengeIndex++) {
      const challenge = { name: 'Sinkhole', challengeIndex };
      const scene = run.visuals.challengeVisual(challenge, location, 'Escape Enemy Base', context);
      chosen.push(key(scene));
      assert.equal(key(run.visuals.challengeVisual(challenge, location, 'Escape Enemy Base', context)), key(scene));
      assert.ok(['phases', 'arctic-challenges', 'desert-challenges', 'jungle-challenges'].includes(scene.source));
    }
  }
  assert.equal(new Set(chosen).size, 12, location);
  const reloaded = game(location, run.session);
  assert.equal(key(reloaded.visuals.challengeVisual({ name: 'Sinkhole', challengeIndex: 0 }, location, 'Escape Enemy Base')), chosen[0]);
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
console.log('Scene selection checks passed: matching obstacles, unique scenes, stable reconnects, visit history and finite reels.');
