const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const code = fs.readFileSync(path.join(__dirname, '../app/static/js/game_visuals.js'), 'utf8');
const pending = [];
const loaded = new Map();
function layer(active = false) {
  return {style: {}, setAttribute() {}, classList: {
    active, remove() { this.active = false; }, contains() { return this.active; },
    toggle(_, value) { this.active = value; }
  }};
}
const ctx = {loaded, assets: {lava: {url: '/lava.png', grid: 4}, wave: {url: '/wave.png', grid: 4}},
  Image: class {set src(value) {pending.push(this);}}, document: {createElement: () => layer()}};
vm.createContext(ctx);
vm.runInContext(code.slice(code.indexOf('  function loadImage('), code.indexOf('  function locationVisual(')), ctx);
(async () => {
  const old = layer(true), next = layer(false);
  const frame = {dataset: {visualKey: 'old:0', loadedVisual: 'old:0'}, layers: [old, next],
    querySelectorAll() {return this.layers;}, setAttribute(_, value) {this.alt = value;}};
  const first = ctx.paint(frame, 0, 'lava', 'Lava Spout', false);
  assert.equal(old.classList.active, false, 'old hazard hidden during loading');
  assert.equal(frame.dataset.loadedVisual, undefined);
  const second = ctx.paint(frame, 0, 'wave', 'Colossal Wave', false);
  pending[0].onload(); await first;
  assert.equal(old.classList.active, false, 'late load must not restore a stale hazard');
  pending[1].onerror(); await second;
  assert.equal(frame.dataset.loadedVisual, undefined, 'failed load must not show unrelated art');
  const retry = ctx.paint(frame, 0, 'wave', 'Colossal Wave', false);
  pending[2].onload(); await retry;
  assert.equal(frame.dataset.loadedVisual, 'wave:0');
  console.log('Challenge paint checks passed: loading, race, failure and retry.');
})().catch(error => {console.error(error); process.exitCode = 1;});
