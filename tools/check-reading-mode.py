"""Check presentation-only section boundaries against frozen content."""
from pathlib import Path
import sys,json,hashlib,subprocess,re
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
before='current frozen Markdown rendering before reader wrappers'
authorized_render=json.loads((ROOT/'build/pre-reading-chapters.json').read_text(encoding='utf-8'))
baseline=json.loads((ROOT/'baseline-manuscript.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in baseline['files'].items())
rows=[]
for p in sorted((ROOT/'dist/chapters').glob('*.html')):
    old=BeautifulSoup(authorized_render['chapter-'+str(int(p.name[:2]))],'html.parser').select_one('.book-section')
    soup=BeautifulSoup(p.read_bytes().decode('utf-8'),'html.parser');now=soup.select_one('.book-section')
    units=now.select(':scope > .reading-unit')
    assert len(units)>2,p.name
    labels=[u['data-reader-title'] for u in units]
    numbered=[x for x in labels if re.match(r'^\d+\.\d+\s',x)]
    assert len(numbered)>4,p.name
    assert soup.select_one('#reader-controls') and soup.select_one('#reader-previous') and soup.select_one('#reader-next')
    assert soup.select_one('#reader-controls #reader-previous-top') and soup.select_one('#reader-controls #reader-next-top')
    for unit in units:
        assert now.find(id=unit['data-reader-anchor'])
        unit.unwrap()
    # This branch must leave the chapter DOM exact after removing presentation wrappers.
    assert str(old)==str(now),p.name
    rows.append({'chapter':p.name,'units':len(units),'numbered_sections':len(numbered),'chapter_dom_unchanged_after_unwrap':True})
report={'status':'PASS','protected_files':len(baseline['files']),'source_reference':before,'chapters':rows,'scope':'Static boundary and exact chapter DOM check; browser behavior checked separately','publication':False}
if '--no-report' not in sys.argv:
    (ROOT/'reports/reading-mode-static.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
