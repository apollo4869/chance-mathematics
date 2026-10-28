"""Static, script-free bilingual Chapter11 print preview from the same full reader DOM."""
from pathlib import Path
import sys,posixpath,re,copy
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
out=ROOT/'dist/print';out.mkdir(exist_ok=True)
for en in [False,True]:
    source=ROOT/('dist/en/chapters/11-characteristic-functions.html' if en else 'dist/chapters/11-characteristic-functions.html')
    soup=BeautifulSoup(source.read_bytes(),'html.parser');body=soup.select_one('.book-section')
    for n in body.select('.chapter-links,.section-kicker'):n.decompose()
    for unit in list(body.select('.reading-unit')):unit.unwrap()
    for node in body.select('[hidden]'):del node['hidden']
    for image in body.select('img[loading]'):del image['loading']
    head=BeautifulSoup('<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>','html.parser').head
    for node in soup.head.select('link[rel=stylesheet],style'):head.append(copy.copy(node))
    for n in [*body.select('[href],[src]'),*head.select('[href],[src]')]:
        attr='href' if n.get('href') is not None else 'src';u=urlsplit(n[attr])
        if u.scheme or u.netloc or not u.path:continue
        destination=(ROOT/'dist'/unquote(u.path).lstrip('/')) if u.path.startswith('/') else source.parent/unquote(u.path)
        n[attr]=posixpath.relpath(destination.resolve().as_posix(),out.resolve().as_posix())+('?' +u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
    title='Chapter 11 — Printable full text' if en else '第十一章 · 可打印全文'
    head.append(BeautifulSoup('<title>'+title+'</title><style>@page{size:A4;margin:18mm 15mm}body{background:#eee;color:#182a29;font-size:11pt}main{margin:20px auto;padding:18mm 14mm;background:white;max-width:210mm;box-shadow:0 1px 8px #ccc}.print-meta{font:10pt/1.5 sans-serif;border-bottom:1px solid #ccc;padding-bottom:10pt}.book-section{padding:0}.reading-unit[hidden]{display:block!important}.formula.display{overflow:visible}.tex-source{display:none!important}.print-meta a{margin-right:12px}@media print{body{background:white}main{margin:0;padding:0;max-width:none;box-shadow:none}.print-meta{color:black}.math-typewriter{display:none!important}}</style>','html.parser'))
    backlink='../en/chapters/11-characteristic-functions.html' if en else '../chapters/11-characteristic-functions.html'
    page='<!doctype html><html lang="'+('en' if en else 'zh-CN')+'">'+str(head)+'<body><main><header class="print-meta">Haobai Wang · '+title+'<br><a href="'+backlink+'">'+('Section reader' if en else '返回分节阅读')+'</a></header>'+str(body)+'</main></body></html>'
    (out/('11-characteristic-functions.'+('en' if en else 'zh')+'.html')).write_bytes(page.encode())
print('Bilingual full-text print previews generated without scripts or hidden sections.')
