/* Localize landing-page controls without changing the protected reading script. */
(() => {
  const topbar = document.querySelector('.topbar');
  const sizeHeader = () => document.documentElement.style.setProperty('--site-header-height', topbar.offsetHeight + 'px');
  new ResizeObserver(sizeHeader).observe(topbar);
  sizeHeader();
  document.querySelectorAll('[data-language-switch]').forEach(link => {
    link.addEventListener('click', () => {
      const destination = new URL(link.href, location.href);
      if (location.hash) destination.hash = location.hash;
      const book = document.querySelector('.book-section');
      if (book) {
        const line = document.getElementById('reader-controls')?.getBoundingClientRect().bottom || topbar.getBoundingClientRect().bottom;
        const nodes = [...book.querySelectorAll('h1[id],h2[id],h3[id],p[id],.formula.display[id]')].filter(n => !n.closest('[hidden]') && n.getBoundingClientRect().height > 0);
        let current = nodes[0];
        for (const node of nodes) { if (node.getBoundingClientRect().top <= line + 20) current = node; else break; }
        if (current) destination.hash = current.id;
      }
      link.href = destination.href;
    });
  });
  if (document.documentElement.lang !== 'en') return;
  const theme = document.getElementById('theme');
  const updateTheme = () => { theme.textContent = document.body.classList.contains('dark') ? 'Light' : 'Dark'; };
  const toggle = theme.onclick;
  theme.onclick = event => { toggle.call(theme, event); updateTheme(); };
  updateTheme();
  const count = document.getElementById('search-count');
  new MutationObserver(() => {
    const match = count.textContent.match(/^找到 (\d+) 处/);
    if (match) count.textContent = `${match[1]} matches${Number(match[1]) > 60 ? ' · showing the first 60' : ''}`;
  }).observe(count, { childList: true });
})();
