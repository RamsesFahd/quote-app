const THEME = {
  motivation: '#8b6914',
  wisdom:     '#4a6b52',
  peace:      '#4a5f7c',
  courage:    '#6b4a7c',
  friendship: '#3d7c6b',
  love:       '#7c3d4a',
};

let currentCategory = 'all';
let currentQuote    = null;
let favorites       = JSON.parse(localStorage.getItem('quotidianFavs') || '[]');

const card       = document.getElementById('quoteCard');
const charTag    = document.getElementById('charTag');
const quoteText  = document.getElementById('quoteText');
const attribution = document.getElementById('attribution');
const favBtn     = document.getElementById('favBtn');
const favCount   = document.getElementById('favCount');
const toast      = document.getElementById('toast');
const favPanel   = document.getElementById('favPanel');
const overlay    = document.getElementById('overlay');
const favList    = document.getElementById('favList');

async function loadQuote(category = 'all') {
  card.classList.add('fading');
  await delay(260);

  try {
    const res  = await fetch(`/api/quote?category=${category}`);
    const data = await res.json();
    currentQuote = data;
    applyTheme(data);
  } catch {
    quoteText.textContent = 'Could not load a quote. Please try again.';
  }

  card.classList.remove('fading');
}

function applyTheme(data) {
  const color = THEME[data.category] || '#8b6914';

  charTag.textContent     = cap(data.category);
  charTag.style.color     = color;
  quoteText.textContent   = data.quote;
  attribution.textContent = `— ${data.character.name}`;

  document.documentElement.style.setProperty('--accent', color);

  updateFavBtn();
}

function updateFavBtn() {
  const saved = currentQuote && favorites.some(f => f.quote === currentQuote.quote);
  favBtn.textContent = saved ? 'Saved ✓' : 'Save';
  favBtn.classList.toggle('saved', !!saved);
}

function syncCount() {
  favCount.textContent = favorites.length;
}

function renderFavList() {
  syncCount();
  if (!favorites.length) {
    favList.innerHTML = '<p class="empty-msg">No favorites saved yet.<br />Hit &ldquo;Save&rdquo; on any quote to keep it here.</p>';
    return;
  }
  favList.innerHTML = favorites.map((f, i) => `
    <div class="fav-item">
      <div class="fav-item-meta">${cap(f.category)} &middot; ${f.name}</div>
      <p class="fav-item-text">&ldquo;${f.quote}&rdquo;</p>
      <button class="fav-remove" onclick="removeFav(${i})">Remove</button>
    </div>
  `).join('');
}

function removeFav(i) {
  favorites.splice(i, 1);
  persist();
  renderFavList();
  updateFavBtn();
}
window.removeFav = removeFav;

function persist() {
  localStorage.setItem('quotidianFavs', JSON.stringify(favorites));
}

function showToast(msg) {
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2200);
}

function openPanel() {
  renderFavList();
  favPanel.classList.add('open');
  overlay.classList.add('open');
}

function closePanel() {
  favPanel.classList.remove('open');
  overlay.classList.remove('open');
}

function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Listeners ──

document.getElementById('newBtn').addEventListener('click', () => loadQuote(currentCategory));

document.getElementById('copyBtn').addEventListener('click', () => {
  if (!currentQuote) return;
  navigator.clipboard.writeText(`"${currentQuote.quote}" — ${currentQuote.character.name}`)
    .then(() => showToast('Copied to clipboard.'));
});

favBtn.addEventListener('click', () => {
  if (!currentQuote) return;
  const idx = favorites.findIndex(f => f.quote === currentQuote.quote);
  if (idx >= 0) {
    favorites.splice(idx, 1);
  } else {
    favorites.push({
      quote:    currentQuote.quote,
      name:     currentQuote.character.name,
      category: currentQuote.category,
    });
  }
  persist();
  updateFavBtn();
  syncCount();
});

document.getElementById('favToggle').addEventListener('click', openPanel);
document.getElementById('closePanel').addEventListener('click', closePanel);
overlay.addEventListener('click', closePanel);

document.querySelectorAll('.cat-pill').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    currentCategory = pill.dataset.category;
    loadQuote(currentCategory);
  });
});

// ── Init ──
syncCount();
loadQuote();
