"""Add approved companion figures without rewriting manuscript text or anchor IDs."""
from pathlib import Path
import json,html,re,shutil
ROOT=Path(__file__).resolve().parents[1]
def records():return json.loads((ROOT/'publication/math-visuals.json').read_text('utf8'))['figures']
def figure_html(row,en=False):
    lang='en' if en else 'zh';item=row[lang];key=row['id'];base='/assets/visuals/print/'+key+'.'+lang
    esc=lambda s:html.escape(s,quote=True)
    links='SVG · '+('vector PDF' if en else '矢量PDF')
    fig='<div class="math-visual-companion" data-math-visual="'+key+'"><figure id="visual-'+key+'" class="publication-math-figure"><a class="visual-open" href="'+base+'.svg"><img loading="lazy" decoding="async" src="'+base+'.svg" alt="'+esc(item['alt'])+'"></a><figcaption><strong>'+esc(item['title'])+'</strong> '+esc(item['caption'])+'</figcaption><nav class="visual-downloads" aria-label="'+('Figure source formats' if en else '图示格式')+'"><a href="'+base+'.svg">SVG</a> · <a href="'+base+'.pdf">'+('Vector PDF' if en else '矢量PDF')+'</a></nav></figure>'
    if key=='typewriter':fig+='<div id="experiment-typewriter" class="math-typewriter" data-visual-id="typewriter" data-language="'+lang+'" hidden></div>'
    return fig+'</div>'
def insert_figures(sections,en=False):
    from bs4 import BeautifulSoup
    result=dict(sections)
    for row in records():
        key='chapter-'+str(row['chapter']);s=BeautifulSoup(result[key],'html.parser');position=row['placement']
        if position.get('before_widget'):target=s.select_one('[data-widget="'+position['before_widget']+'"]');before=True
        elif position.get('before_heading'):
            target=next((n for n in s.select('h2,h3') if re.match('^'+re.escape(position['before_heading'])+r'(?:\s|$)',n.get_text(' ',strip=True))),None);before=True
        else:
            prefix=position['after_paragraph']['en' if en else 'zh'];target=next((n for n in s.select('p') if n.get_text(' ',strip=True).startswith(prefix)),None);before=False
        assert target is not None,('figure insertion anchor missing',key,row['id'])
        fragment=BeautifulSoup(figure_html(row,en),'html.parser').div
        if before:target.insert_before(fragment)
        else:target.insert_after(fragment)
        result[key]=str(s)
    return result
def remove_figures(fragment):
    """Used only alongside independent exact figure/model/placement checks."""
    for n in list(fragment.select('[data-math-visual]')):n.decompose()
    return fragment
def copy_assets():shutil.copytree(ROOT/'assets/visuals',ROOT/'dist/assets/visuals',dirs_exist_ok=True)
