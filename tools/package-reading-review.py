"""Package only this acceptance report and its actual browser evidence."""
from pathlib import Path
import hashlib,html,json,shutil,subprocess,zipfile

R=Path(__file__).resolve().parents[1]
O=R/'reports/full-book-reading-2026-11-07'
D=R/'deliverables';D.mkdir(exist_ok=True)
GIT=r'C:/Program Files/Git/cmd/git.exe'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
def git(*args):return subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),*args],cwd=R).decode('utf8').strip()

def gallery():
    sections=[]
    for name,label in [('desktop','桌面'),('mobile-confirmed','手机390px')]:
        records=json.loads((O/f'figures-browser-{name}.json').read_text('utf8'))
        cards=[]
        for x in records:
            urls=[x['screenshot']]+([x['scrollScreenshot']] if x.get('scrollScreenshot') else [])
            pics=''.join(f'<a href="{html.escape(u)}"><img loading="lazy" src="{html.escape(u)}" alt="{x["id"]} {x["lang"]} actual browser viewport"></a>' for u in urls)
            cards.append(f'<article><h3>{x["id"]} · {x["lang"]} · §{x["section"]}</h3>{pics}</article>')
        sections.append(f'<h2>{label}</h2><div class="grid">'+''.join(cards)+'</div>')
    (O/'browser-gallery.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>全书阅读验收：实际浏览器截图</title><style>body{font:16px/1.7 system-ui;max-width:1440px;margin:32px auto;padding:16px;background:#faf8f1;color:#173b37}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}article{min-width:0;border-top:1px solid #c7d1c9}img{width:100%;height:auto;display:block;margin:8px 0}h3{font-size:16px}</style><h1>实际浏览器截图索引</h1><p>工作稿：桌面与390px浏览器视口。图片来自实际网页，不是SVG静态渲染。每份交互图仅抽查一个非默认状态；长图分视口及滚动记录，不是整页或原生PDF。真机、全部参数及最终作者审美仍开放。</p><p><a href="REPORT.md">完整报告</a> · <a href="chapter-inventory.csv">逐章清单</a></p>'+''.join(sections)+'</html>',encoding='utf8',newline='\n')

def package():
    head=git('rev-parse','HEAD');short=head[:8]
    assert git('branch','--show-current')=='qa/full-book-reading-2026-11-07'
    patch=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'diff','771fb0ee',head,'--','build-chapters.py','reader-mode.js','publication/chapter-reading-layout.css','tools/build-chapter-print.py','tools/build-chapter11-print.py','tools/publication_site.py','tools/chapter_reading_layout.py','tools/prepare-reading-acceptance.py','tools/check-reading-acceptance.py','tools/catalog-reading-visuals.py','tools/reading-browser-checks.mjs','tools/package-reading-offline.py','tools/finalize-reading-acceptance.py','tools/package-reading-review.py'],cwd=R)
    (D/f'reading-fixes-{short}.patch').write_bytes(patch)
    review=D/f'chance-mathematics-reading-review-20261107-{short}.zip'
    members=[]
    with zipfile.ZipFile(review,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(O.rglob('*')):
            if not p.is_file():continue
            rel=p.relative_to(O).as_posix()
            assert not any(x.startswith('.') for x in p.relative_to(O).parts)
            z.write(p,'review/'+rel);members.append({'path':'review/'+rel,'sha256':sha(p)})
        z.writestr('reading-fixes.patch',patch)
        z.writestr('START-HERE.txt',f'全书阅读验收 / 2026-11-07 / {head}\n先读 review/REPORT.md；打开 review/browser-gallery.html 浏览实际截图。\n逐章和全量图源清单分别为 chapter-inventory.csv、all-visual-assets.csv。\n本包是作者审阅证据，不是线上部署，不包含整个源码仓库或未发表论文。\n原生PDF、真机及独立数学终审仍开放。\n')
        z.writestr('REVIEW-MANIFEST.json',json.dumps({'source_commit':head,'base':'771fb0ee','files':members,'published':False,'pushed':False},ensure_ascii=False,indent=2))
    with zipfile.ZipFile(review) as z:
        assert z.testzip() is None
        for x in members:assert hashlib.sha256(z.read(x['path'])).hexdigest()==x['sha256']
    offline_source=R/'work/reading-acceptance/site/downloads/complete-offline.zip'
    offline=D/f'chance-mathematics-offline-reading-20261107-{short}.zip'
    shutil.copyfile(offline_source,offline)
    assert sha(offline)==json.loads((O/'offline-package.json').read_text('utf8'))['sha256']
    receipt={'source_commit':head,'branch':git('branch','--show-current'),'base_commit':'771fb0ee','local_only':True,'published':False,'pushed':False,'review':{'path':str(review),'sha256':sha(review),'bytes':review.stat().st_size,'CRC_and_member_hashes':True},'offline':{'path':str(offline),'sha256':sha(offline),'bytes':offline.stat().st_size},'patch':{'path':str(D/f'reading-fixes-{short}.patch'),'sha256':hashlib.sha256(patch).hexdigest()}}
    save(D/f'DELIVERY-{short}.json',receipt)
    print(json.dumps(receipt,ensure_ascii=False))

if __name__=='__main__':
    import sys
    gallery() if '--gallery' in sys.argv else package()
