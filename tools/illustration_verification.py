"""Verify adopted companion fragments exactly before excluding them from prose audits."""
from pathlib import Path
from html import escape
import json,re
from bs4 import BeautifulSoup,Comment
ROOT=Path(__file__).resolve().parents[1]

def remove_adopted(fragment):
    soup=fragment if hasattr(fragment,'select') else BeautifulSoup(str(fragment),'html.parser')
    rows=json.loads((ROOT/'publication/illustration-release.json').read_text('utf8'))['figures']
    seen=[]
    for start in list(soup.find_all(string=lambda s:isinstance(s,Comment) and str(s).startswith(' illustration-release:'))):
        code=str(start).strip().split(':',1)[1];nodes=[];end=start.next_sibling
        while end is not None and not (isinstance(end,Comment) and str(end).strip()=='/illustration-release:'+code):
            nodes.append(end);end=end.next_sibling
        assert end is not None,('unterminated adopted illustration',code)
        actual=''.join(str(n) for n in nodes)
        candidates=[]
        for row in rows:
            if row['id']!=code:continue
            lg=row['lang'];paths=re.findall(r'/assets/visuals/[^"<>]+/'+re.escape(code)+r'\.'+lg+r'\.svg',row['html'])
            assert paths,(code,lg)
            svg=paths[0];title=escape(row['title']);condition=escape(row.get('condition',''))
            screen=row['html'].replace(f'href="/print/{code}.{lg}.html"',f'href="/print/figures/{code}.{lg}.html"')
            candidates += ['<div class="illustration-screen-only">'+screen+'</div><img class="illustration-print-only" src="'+svg+'" alt="'+title+'">',
                           f'<figure class="illustration-static" id="visual-{code}"><img src="{svg}" alt="{title}"><figcaption>{condition}</figcaption></figure>']
        assert any(actual==str(BeautifulSoup(c,'html.parser')) for c in candidates),('unapproved or modified illustration',code)
        assert code not in seen,('duplicate illustration',code)
        seen.append(code)
        for n in nodes:n.extract()
        start.extract();end.extract()
    assert not soup.find_all(string=lambda s:isinstance(s,Comment) and 'illustration-release:' in str(s)), 'unmatched illustration marker'
    return soup
