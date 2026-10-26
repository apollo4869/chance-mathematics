/* Presentation only. Manuscripts, formula nodes and widget instances are never cloned. */
(() => {
  'use strict';
  const book = document.querySelector('.book-section');
  const controls = document.getElementById('reader-controls');
  if (!book || !controls) return;
  const units = [...book.querySelectorAll(':scope > .reading-unit')];
  if (!units.length) return;
  const select = document.getElementById('reader-section');
  const status = document.getElementById('reader-status');
  const buttons = [...controls.querySelectorAll('[data-reading-mode]')];
  const previous = [...document.querySelectorAll('#reader-previous,#reader-previous-top')];
  const next = [...document.querySelectorAll('#reader-next,#reader-next-top')];
  const key = 'chance-reader-position:' + location.pathname;
  const read = k => { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } };
  const save = (k, value) => { try { localStorage.setItem(k, JSON.stringify(value)); } catch {} };
  let mode = read('chance-reader-mode') === 'chapter' ? 'chapter' : 'section';
  let current = 0, changing = false, timer;
  const line = () => controls.getBoundingClientRect().bottom + 18;
  function metrics() {
    const height = document.querySelector('.topbar').getBoundingClientRect().height;
    document.documentElement.style.setProperty('--reader-top', height + 'px');
    document.documentElement.style.scrollPaddingTop = (height + controls.offsetHeight + 18) + 'px';
  }
  function indexOf(node) {
    if (!node || node === book) return 0;
    const index = units.indexOf(node.closest('.reading-unit'));
    return index < 0 ? current : index;
  }
  function capture() {
    const nodes = [...book.querySelectorAll('h1[id],h2[id],h3[id],h4[id],p[id],.formula.display[id],figure[id],.experiment[id]')]
      .filter(n => !n.closest('[hidden]') && n.getBoundingClientRect().height > 0);
    const y = line();
    let node = nodes[0];
    for (const n of nodes) {
      if (n.getBoundingClientRect().top <= y + 1) node = n;
      else { if (!node) node = n; break; }
    }
    return node ? {anchor:node.id, delta:node.getBoundingClientRect().top-y, unit:indexOf(node)} : null;
  }
  function update() {
    document.body.dataset.readingMode = mode;
    document.body.dataset.readingAtEnd = String(current === units.length - 1);
    units.forEach((u, i) => { u.hidden = mode === 'section' && i !== current; });
    select.value = String(current);
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.readingMode === mode)));
    status.textContent = `${current + 1} / ${units.length} · ${mode === 'section' ? '按小节阅读' : '整章阅读'}`;
    previous.forEach(b => {
      b.disabled = current === 0;
      b.title = current ? units[current-1].dataset.readerTitle : '已到本章开头';
    });
    next.forEach(b => {
      b.disabled = current === units.length - 1;
      b.title = current < units.length-1 ? units[current+1].dataset.readerTitle : '已到本章末尾';
    });
    metrics();
  }
  function instantScroll(top) {
    window.scrollTo({top:Math.max(0,top),behavior:'instant'});
  }
  function restore(position) {
    if (!position) return;
    const node = document.getElementById(position.anchor);
    if (!node) return;
    instantScroll(scrollY + node.getBoundingClientRect().top - line() - position.delta);
  }
  function settle(action) {
    changing = true;
    action();
    requestAnimationFrame(() => {
      action();
      changing = false;
      save(key, capture());
      window.dispatchEvent(new Event('scroll'));
    });
  }
  function jump(node, push = true) {
    current = indexOf(node);
    update();
    if (push) history.pushState(null, '', '#' + encodeURIComponent(node.id));
    settle(() => instantScroll(scrollY + node.getBoundingClientRect().top - line()));
  }
  function navigate(index) {
    const target = document.getElementById(units[index].dataset.readerAnchor) || units[index];
    jump(target);
  }
  buttons.forEach(b => b.addEventListener('click', () => {
    if (b.dataset.readingMode === mode) return;
    const position = capture();
    controls.dataset.positionAnchor = position?.anchor || '';
    controls.dataset.positionDelta = String(position?.delta || 0);
    if (position) current = position.unit;
    mode = b.dataset.readingMode;
    save('chance-reader-mode', mode);
    if (position) history.replaceState(null, '', '#' + encodeURIComponent(position.anchor));
    update();
    settle(() => restore(position));
  }));
  select.addEventListener('change', () => navigate(Number(select.value)));
  previous.forEach(b => b.addEventListener('click', () => navigate(current-1)));
  next.forEach(b => b.addEventListener('click', () => navigate(current+1)));
  // Reveal a hidden section before following TOC, citation, or search bookmarks.
  document.addEventListener('click', event => {
    const a = event.target.closest('a[href]');
    if (!a || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || url.pathname !== location.pathname || !url.hash) return;
    let id; try { id = decodeURIComponent(url.hash.slice(1)); } catch { return; }
    const node = document.getElementById(id);
    if (!node || !book.contains(node)) return;
    event.preventDefault();
    jump(node);
  });
  function fromHash() {
    let node; try { node = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch {}
    if (node && book.contains(node)) { jump(node, false); return true; }
    return false;
  }
  window.addEventListener('hashchange', fromHash);
  window.addEventListener('popstate', () => {
    if (!fromHash() && !location.hash) jump(document.getElementById(units[0].dataset.readerAnchor) || units[0], false);
  });
  window.addEventListener('scroll', () => {
    if (changing) return;
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (changing) return;
      const position = capture();
      if (!position) return;
      if (mode === 'chapter' && position.unit !== current) {
        current = position.unit;
        update();
      }
      save(key, position);
    }, 170);
  }, {passive:true});
  new ResizeObserver(metrics).observe(document.querySelector('.topbar'));
  new ResizeObserver(metrics).observe(controls);
  update();
  if (!fromHash()) {
    const position = read(key);
    if (position && document.getElementById(position.anchor) && book.contains(document.getElementById(position.anchor))) {
      current = indexOf(document.getElementById(position.anchor));
      update();
      settle(() => restore(position));
      if (document.readyState !== 'complete') window.addEventListener('load', () => settle(() => restore(position)), {once:true});
    }
  }
})();
