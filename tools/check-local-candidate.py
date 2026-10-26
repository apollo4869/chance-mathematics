"""Check local chapter preservation, TeX and links; no academic approval or reports."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import hashlib, json, os, re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / 'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup

baseline = json.loads((ROOT / 'baseline-manuscript.json').read_text('utf-8'))
for name, digest in baseline['files'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
inputs = json.loads((ROOT / 'provenance/build-inputs.json').read_text('utf-8'))
items = [{'id': f'chapter-{i}', 'path': str(ROOT / 'chapters' / name), 'syntax': 'slash'}
         for i, name in enumerate(inputs['chapters'], 1) if i >= 7]
request = {'engineProject': str(ROOT if (ROOT / 'node_modules/markdown-it').exists()
                               else ROOT.parent / 'chance-mathematics-restored-v2'),
           'items': items, 'output': str(ROOT / 'build/local-expected.json')}
(ROOT / 'build/local-request.json').write_text(json.dumps(request), 'utf-8')
node = shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
subprocess.run([node, str(ROOT / 'tools/expected-content.cjs'),
                str(ROOT / 'build/local-request.json')], check=True)
expected = json.loads((ROOT / 'build/local-expected.json').read_text('utf-8'))
dist = ROOT / 'dist'
pages = {p.resolve(): BeautifulSoup(p.read_text('utf-8'), 'html.parser')
         for p in dist.rglob('*.html')}
ids = {p: Counter(n['id'] for n in s.select('[id]')) for p, s in pages.items()}
formula_count = 0
for p, soup in pages.items():
    assert all(n == 1 for n in ids[p].values()), f'duplicate ID: {p}'
    assert not soup.select('merror,[data-mjx-error],.math-failed'), f'formula error: {p}'
    for formula in soup.select('.book-section .formula'):
        assert formula.select_one('mjx-container svg'), f'unrendered formula: {p}'
        formula_count += 1
links = 0
for p, soup in pages.items():
    for n in soup.select('a[href],script[src],link[href],img[src]'):
        value = n.get('href', n.get('src'))
        u = urlsplit(value)
        if u.scheme or u.netloc:
            continue
        target = (dist / unquote(u.path).lstrip('/')) if u.path.startswith('/') else (
                  p.parent / unquote(u.path) if u.path else p)
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        assert target.exists(), f'missing file: {p}: {value}'
        assert not (u.fragment and target in ids and unquote(u.fragment) not in ids[target]), (
            f'missing anchor: {p}: {value}')
        links += 1

def content(fragment):
    soup = BeautifulSoup(str(fragment), 'html.parser')
    for n in soup.select('.section-kicker,.chapter-links'):
        n.decompose()
    formulas = []
    for n in soup.select('.formula,.audit-math'):
        formulas.append(n.get('data-tex', n.get('data-audit-tex', '')).replace('\r\n', '\n').replace('\r', '\n').strip())
        n.replace_with(' ⟦MATH⟧ ')
    compact = lambda s: re.sub(r'\s+', '', s)
    return {'text': compact(soup.get_text()), 'formulas': formulas,
            'headings': [(n.name, compact(n.get_text()))
                         for n in soup.find_all(re.compile('^h[1-6]$'))]}

chapter_counts = {}
for item in expected:
    number = int(item['id'].split('-')[1])
    path = (dist / 'chapters' / Path(inputs['chapters'][number-1]).with_suffix('.html')).resolve()
    actual = content(pages[path].find('section', id=item['id']))
    wanted = content(item['html'])
    assert actual == wanted, f'independent Markdown comparison failed: {item["id"]}'
    chapter_counts[number] = len(actual['formulas'])
print(json.dumps({'scope': 'Local rendering and preservation only; not mathematical/history acceptance',
                  'status': 'PASS', 'protected_hashes': len(baseline['files']),
                  'pages': len(pages), 'local_links': links,
                  'body_formulas': formula_count, 'independent_chapter_formulas': chapter_counts,
                  'publication': False}, ensure_ascii=False))
