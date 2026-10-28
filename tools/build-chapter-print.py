"""Produce an unpaginated bilingual print reader from the complete chapter DOM."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import argparse,copy,json,posixpath,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
ap=argparse.ArgumentParser();ap.add_argument('--chapter',type=int,required=True);a=ap.parse_args()
inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'))['chapters'];slug=Path(inputs[a.chapter-1]).stem
out=ROOT/'dist/print';out.mkdir(exist_ok=True)
for en in [False,True]:
    source=ROOT/'dist'/('en' if en else '')/'chapters'/(slug+'.html')
    s=BeautifulSoup(source.read_bytes(),'html.parser');body=s.select_one('.book-section')
    for n in body.select('.chapter-links,.section-kicker'):n.decompose()
    for n in list(body.select('.reading-unit')):n.unwrap()
    for n in body.select('[hidden]'):del n['hidden']
    for n in body.select('img[loading]'):del n['loading']
    head=BeautifulSoup('<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>','html.parser').head
    for n in s.head.select('link[rel=stylesheet],style'):head.append(copy.copy(n))
    for n in [*body.select('[href],[src]'),*head.select('[href],[src]')]:
        attr='href' if n.get('href') is not None else 'src';u=urlsplit(n[attr])
        if u.scheme or u.netloc or not u.path:continue
        dest=ROOT/'dist'/unquote(u.path).lstrip('/') if u.path.startswith('/') else source.parent/unquote(u.path)
        n[attr]=posixpath.relpath(dest.resolve().as_posix(),out.resolve().as_posix())+('?' +u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
    title=('Chapter '+str(a.chapter)+' — Printable full text') if en else ('第'+str(a.chapter)+'章 · 可打印全文')
    head.append(BeautifulSoup('<title>'+title+'</title><style>@page{size:A4;margin:18mm 15mm}body{background:#eee;color:#182a29;font-size:11pt}main{margin:20px auto;padding:18mm 14mm;background:white;max-width:210mm}.book-section{padding:0}.formula.display{overflow:visible}.tex-source{display:none!important}.print-meta{font:10pt/1.5 sans-serif;border-bottom:1px solid #ccc;padding-bottom:10pt}@media print{body,main{background:white}main{margin:0;padding:0;max-width:none}}</style>','html.parser'))
    backlink='../'+('en/' if en else '')+'chapters/'+slug+'.html'
    page='<!doctype html><html lang="'+('en' if en else 'zh-CN')+'">'+str(head)+'<body><main><header class="print-meta">Haobai Wang · '+title+'<br><a href="'+backlink+'">'+('Section reader' if en else '返回分节阅读')+'</a></header>'+str(body)+'</main></body></html>'
    (out/(slug+'.'+('en' if en else 'zh')+'.html')).write_bytes(page.encode())
print('Bilingual complete print chapter generated:',a.chapter)
