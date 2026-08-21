// FRONT END NOT BACKEND LOGIC SO GO BACK THROUGH AFTER
// this is just to demo how it can work

// selecting/change vote
const itemGrid = document.getElementById('itemGrid');
const tiles = Array.from(itemGrid.querySelectorAll('.item-tile'));
let selected = null;

tiles.forEach(tile => {
  tile.addEventListener('click', () => {
    if (tile.dataset.state === 'unavailable') return;
    tiles.forEach(t => {
      t.dataset.state = 'idle';
      t.querySelector('.vote-check').textContent = 'TAP TO VOTE';
    });
    if (selected !== tile) {
      tile.dataset.state = 'selected';
      tile.querySelector('.vote-check').textContent = '✓ YOUR VOTE';
      selected = tile;
    } else {
      selected = null;
    }
  });
});

// timer countdown
let secondsLeft = 45;
const timerValue = document.getElementById('timerValue');
const timerPill = document.getElementById('timerPill');
const timerInterval = setInterval(() => {
  secondsLeft = Math.max(0, secondsLeft - 1);
  const m = String(Math.floor(secondsLeft / 60)).padStart(2, '0');
  const s = String(secondsLeft % 60).padStart(2, '0');
  timerValue.textContent = `${m}:${s}`;
  if (secondsLeft <= 10) timerPill.classList.add('low');
  if (secondsLeft === 0) clearInterval(timerInterval);
}, 1000);

// instructions popup
const helpBtn = document.getElementById('helpBtn');
const helpPopup = document.getElementById('helpPopup');
helpBtn.addEventListener('click', () => {
  helpPopup.classList.remove('hidden');
  requestAnimationFrame(() => helpPopup.classList.add('show'));
});
document.getElementById('closeHelp').addEventListener('click', () => {
  helpPopup.classList.remove('show');
  setTimeout(() => helpPopup.classList.add('hidden'), 200);
});

// voting popup
const resultPopup = document.getElementById('resultPopup');
const resultIcon = document.getElementById('resultIcon');
const resultTitle = document.getElementById('resultTitle');
const resultSub = document.getElementById('resultSub');

function showResult(type) {
  if (type === 'purchase' && selected) {
    const name = selected.querySelector('.item-name').textContent;
    const cost = selected.querySelector('.cost-tag').textContent;
    const icon = selected.querySelector('.item-image').textContent;
    resultIcon.textContent = icon;
    resultTitle.textContent = 'ITEM PURCHASED';
    resultSub.textContent = `Your team bought the ${name} for ${cost}.`;
  } else if (type === 'tie') {
    resultIcon.textContent = '⚔️';
    resultTitle.textContent = "IT'S A TIE";
    resultSub.textContent = 'No item was purchased this round. Talk it out next time!';
  } else {
    resultIcon.textContent = '➡️';
    resultTitle.textContent = 'MOVING ON';
    resultSub.textContent = 'Your team continued without buying an item this round.';
  }
  resultPopup.classList.remove('hidden');
  requestAnimationFrame(() => resultPopup.classList.add('show'));
}

document.getElementById('finishBtn').addEventListener('click', () => {
  showResult(selected ? 'purchase' : 'tie');
});
document.getElementById('skipBtn').addEventListener('click', () => showResult('skip'));
document.getElementById('closeResult').addEventListener('click', () => {
  resultPopup.classList.remove('show');
  setTimeout(() => resultPopup.classList.add('hidden'), 200);
});
