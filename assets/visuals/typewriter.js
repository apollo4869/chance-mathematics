/* Optional Chapter 7 exploration. All interval mathematics comes from math-model.js. */
(function (global) {
  'use strict';
  const words = {
    zh: {
      title: '动手观察：缩小的窗口，会不会最终离开你？',
      help: '改变轮次、窗口位置或固定样本点；左右两幅图始终使用相同宽度。',
      round: '轮次 k', position: '窗口编号 j（从 0 开始）', point: '固定样本点 u',
      previous: '← 上一扇窗口', next: '下一扇窗口 →', reset: '恢复初始参数',
      moving: '移动窗口 Aₙ：每轮从左到右扫描', fixed: '左端窗口 Bₙ：同宽度，始终停在 0',
      hit: '命中', miss: '未命中', probability: '本次命中概率', index: '观察编号',
      interval: '窗口', value: '指示函数值', marker: '▲ 为固定样本点；实线及斜线区域为当前窗口。',
      reason: '每轮的半开区间恰好分割 [0,1)，所以每个样本点在每轮被移动窗口命中一次；其余窗口给出 0。这个分割机制说明无穷多次命中，而不是有限帧模拟证明了无限结论。',
      zero: '现在 u = 0：左端窗口每轮仍包含它，Zₙ(0) = 1。这是概率为 0 的例外；“几乎必然趋零”允许这样的例外。',
      positive: '现在 u > 0：当 2⁻ᵏ ≤ u 后，左端窗口便不再包含它。它与移动窗口在每次观察中的命中概率相同，但固定记录的命运不同。',
      boundary: '区间均左闭右开；若 u 恰为右端点，属于下一扇窗口。u 限于 [0,1)，因此这里不提供端点 1。',
      deterministic: '这是确定性反例的有限参数演示，无随机采样，也不使用随机种子。静态出版图保留完整核心解释。',
      diagram: '在单位区间上，显示半开窗口与固定样本点的相对位置',
    },
    en: {
      title: 'Explore: must a shrinking window eventually leave you behind?',
      help: 'Change the round, window index or fixed sample point. Both diagrams always use the same width.',
      round: 'Round k', position: 'Window index j (starting at 0)', point: 'Fixed sample point u',
      previous: '← Previous window', next: 'Next window →', reset: 'Reset parameters',
      moving: 'Moving window Aₙ: scan left to right each round', fixed: 'Left-end window Bₙ: same width, anchored at 0',
      hit: 'Hit', miss: 'Miss', probability: 'Hit probability at this observation', index: 'Observation index',
      interval: 'Window', value: 'Indicator value', marker: '▲ marks the fixed sample point; solid edges and hatching mark the window.',
      reason: 'The half-open windows partition [0,1) in every round, so each point is hit by the moving window once per round and has value 0 in the other windows. This partition argument explains infinitely many hits; finite frames do not prove an infinite conclusion.',
      zero: 'Here u = 0: the left-end window still contains it in every round, so Zₙ(0) = 1. This is a probability-zero exception, allowed by almost-sure convergence to zero.',
      positive: 'Here u > 0: once 2⁻ᵏ ≤ u, the left-end window no longer contains it. The two windows have the same hit probability at every observation but different behavior along a fixed record.',
      boundary: 'All windows are closed on the left and open on the right. A point at a right endpoint belongs to the next window. The sample space is [0,1), so the control excludes 1.',
      deterministic: 'This is a finite-parameter view of a deterministic counterexample, with no random sampling or seed. The static publication figure retains the core explanation.',
      diagram: 'A half-open window and a fixed sample point on the unit interval',
    },
  };
  let serial = 0;
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const decimal = x => Number(x.toFixed(8)).toString();

  function init(root) {
    if (root.dataset.typewriterReady === 'true' || !global.ChanceVisualMath || typeof global.ChanceVisualMath.typewriter !== 'function') return;
    const w = words[root.dataset.language === 'en' ? 'en' : 'zh'];
    const uid = 'typewriter-' + (++serial);
    const state = { k: 2, j: 0, u: 0.3 };
    const control = (name, text, min, max, step, value) =>
      '<label class="typewriter-control" for="' + uid + '-' + name + '"><span>' + esc(text) + ' <output data-value="' + name + '"></output></span>' +
      '<input id="' + uid + '-' + name + '" data-control="' + name + '" type="range" min="' + min + '" max="' + max + '" step="' + step + '" value="' + value + '"></label>';
    root.innerHTML = '<p class="typewriter-title">' + esc(w.title) + '</p><p class="typewriter-help">' + esc(w.help) + '</p>' +
      '<div class="typewriter-controls">' + control('round', w.round, 1, 8, 1, state.k) + control('window', w.position, 0, 3, 1, state.j) + control('point', w.point, 0, 0.999, 0.001, state.u) + '</div>' +
      '<div class="typewriter-buttons"><button type="button" data-action="previous">' + esc(w.previous) + '</button><button type="button" data-action="next">' + esc(w.next) + '</button><button type="button" data-action="reset">' + esc(w.reset) + '</button></div>' +
      '<div class="typewriter-diagrams"><section><p class="typewriter-diagram-title">' + esc(w.moving) + '</p><svg data-diagram="moving" viewBox="0 0 360 125" role="img" aria-label="' + esc(w.diagram) + '"></svg><p data-result="moving"></p></section>' +
      '<section><p class="typewriter-diagram-title">' + esc(w.fixed) + '</p><svg data-diagram="fixed" viewBox="0 0 360 125" role="img" aria-label="' + esc(w.diagram) + '"></svg><p data-result="fixed"></p></section></div>' +
      '<p class="typewriter-marker">' + esc(w.marker) + '</p><output class="typewriter-status" aria-live="polite" aria-atomic="true"></output>' +
      '<p class="typewriter-reason">' + esc(w.reason) + '</p><p class="typewriter-point-note"></p><p class="typewriter-boundary">' + esc(w.boundary) + '</p><p class="typewriter-limit">' + esc(w.deterministic) + '</p>';
    const round = root.querySelector('[data-control="round"]');
    const position = root.querySelector('[data-control="window"]');
    const point = root.querySelector('[data-control="point"]');
    const previous = root.querySelector('[data-action="previous"]');
    const next = root.querySelector('[data-action="next"]');

    function diagram(svg, left, right, hit, kind) {
      const x = v => 20 + 320 * v;
      const a = x(left), b = x(right), px = x(state.u), pid = uid + '-' + kind + '-hatch';
      svg.innerHTML = '<defs><pattern id="' + pid + '" width="7" height="7" patternUnits="userSpaceOnUse"><path d="M-2 2L2-2M0 7L7 0M5 9L9 5" fill="none" stroke="currentColor" stroke-width="0.8"/></pattern></defs>' +
        '<path d="M20 66H340" fill="none" stroke="currentColor" stroke-width="1.4"/>' +
        '<rect x="' + a + '" y="39" width="' + (b-a) + '" height="27" fill="url(#' + pid + ')" stroke="currentColor" stroke-width="1.5"/>' +
        '<circle cx="' + a + '" cy="66" r="3.1" fill="currentColor"/><circle cx="' + b + '" cy="66" r="3.1" fill="var(--paper,#fff)" stroke="currentColor" stroke-width="1.3"/>' +
        '<path d="M' + px + ' 20V76" fill="none" stroke="currentColor" stroke-dasharray="4 3" stroke-width="1.4"/>' +
        '<path d="M' + px + ' 22l-5-8h10z" fill="currentColor"/><text x="' + Math.min(318,Math.max(42,px)) + '" y="10" text-anchor="middle">u = ' + decimal(state.u) + '</text>' +
        [0,0.5,1].map(v => '<path d="M' + x(v) + ' 66v6" stroke="currentColor"/><text x="' + x(v) + '" y="93" text-anchor="middle">' + v + '</text>').join('') +
        '<text x="180" y="119" text-anchor="middle">' + esc(w.interval) + ': [' + decimal(left) + ', ' + decimal(right) + ')</text>';
      svg.setAttribute('aria-label', w.diagram + '; ' + w.interval + ' [' + decimal(left) + ', ' + decimal(right) + '), u = ' + decimal(state.u) + ', ' + (hit ? w.hit : w.miss));
    }

    function render() {
      const m = global.ChanceVisualMath.typewriter(state.k,state.j,state.u);
      round.value = String(state.k); position.max = String(2 ** state.k - 1); position.value = String(state.j); point.value = String(state.u);
      root.querySelector('[data-value="round"]').textContent = String(state.k);
      root.querySelector('[data-value="window"]').textContent = state.j + ' / ' + (2 ** state.k - 1);
      root.querySelector('[data-value="point"]').textContent = state.u.toFixed(3);
      diagram(root.querySelector('[data-diagram="moving"]'),m.left,m.right,m.hit,'moving');
      diagram(root.querySelector('[data-diagram="fixed"]'),0,m.width,m.fixedHit,'fixed');
      root.querySelector('[data-result="moving"]').textContent = 'Yₙ(u) = ' + Number(m.hit) + ' · ' + (m.hit ? w.hit : w.miss);
      root.querySelector('[data-result="fixed"]').textContent = 'Zₙ(u) = ' + Number(m.fixedHit) + ' · ' + (m.fixedHit ? w.hit : w.miss);
      root.querySelector('.typewriter-status').textContent = 'k = ' + state.k + ', j = ' + state.j + '; ' + w.index + ' n = ' + m.n + '; ' + w.probability + ' = 2⁻' + state.k + ' = ' + decimal(m.width) + '.';
      root.querySelector('.typewriter-point-note').textContent = state.u === 0 ? w.zero : w.positive;
      previous.disabled = state.k === 1 && state.j === 0;
      next.disabled = state.k === 8 && state.j === 255;
      Object.assign(root.dataset,{round:String(state.k),window:String(state.j),point:String(state.u),hit:String(Number(m.hit)),fixedHit:String(Number(m.fixedHit)),observation:String(m.n)});
    }
    round.addEventListener('input', () => { state.k = Number(round.value); state.j = 0; render(); });
    position.addEventListener('input', () => { state.j = Number(position.value); render(); });
    point.addEventListener('input', () => { state.u = Number(point.value); render(); });
    previous.addEventListener('click', () => {
      if (state.j > 0) state.j--; else if (state.k > 1) { state.k--; state.j = 2 ** state.k - 1; } render();
    });
    next.addEventListener('click', () => {
      if (state.j < 2 ** state.k - 1) state.j++; else if (state.k < 8) { state.k++; state.j = 0; } render();
    });
    root.querySelector('[data-action="reset"]').addEventListener('click', () => { state.k = 2; state.j = 0; state.u = 0.3; render(); });
    render(); root.dataset.typewriterReady = 'true'; root.hidden = false;
  }
  function initAll() { document.querySelectorAll('.math-typewriter[data-visual-id="typewriter"]').forEach(init); }
  global.ChanceTypewriter = Object.freeze({init:initAll});
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',initAll,{once:true}); else initAll();
})(window);
