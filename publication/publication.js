/* Clipboard writes occur only after the reader clicks a citation button. */
(() => {
  const english = document.documentElement.lang === 'en';
  document.querySelectorAll('[data-copy-target]').forEach(button => {
    button.addEventListener('click', async () => {
      const code = document.getElementById(button.dataset.copyTarget);
      const feedback = button.parentElement.querySelector('.copy-feedback');
      const text = code.textContent;
      let copied = false;
      try {
        if (navigator.clipboard?.writeText) { await navigator.clipboard.writeText(text); copied = true; }
      } catch {}
      if (!copied) {
        const field = document.createElement('textarea');
        field.value = text; field.setAttribute('readonly', '');
        field.style.cssText = 'position:fixed;left:-9999px;top:0';
        document.body.append(field); field.select();
        try { copied = document.execCommand('copy'); } catch {}
        field.remove();
      }
      if (!copied) {
        const range = document.createRange(); range.selectNodeContents(code);
        const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      }
      feedback.textContent = copied ? (english ? 'BibTeX copied.' : 'BibTeX 已复制。')
        : (english ? 'Text selected. Press Ctrl+C / Cmd+C to copy.' : '已选中文本，请按 Ctrl+C / Cmd+C 复制。');
    });
  });
  const select = document.getElementById('citation-chapter');
  if (select) {
    const requested = new URLSearchParams(location.search).get('chapter');
    if ([...select.options].some(o => o.value === requested)) select.value = requested;
    const show = () => document.querySelectorAll('[data-citation-chapter]').forEach(node => {
      node.hidden = node.dataset.citationChapter !== select.value;
    });
    select.addEventListener('change', show); show();
  }
})();
