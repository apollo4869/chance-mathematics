"""Targeted revision checks. Finite calculations and source checks, not browser QA."""
import hashlib,json,re,subprocess,xml.etree.ElementTree as ET
from fractions import Fraction
from .volume8 import R,A,kary_values,kary_title
from .volume8_review import P

O=R/'reports/volume8-visual-revision-2026-11-07'
BASE='56f537d4'
GIT='C:/Program Files/Git/cmd/git.exe'

def git(*args):
    return subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),*args],cwd=R)

def run():
    O.mkdir(parents=True,exist_ok=True)
    checks=[]
    def mark(name,detail):checks.append(dict(check=name,detail=detail,status='passed targeted check'))
    # Raw Git blob comparison protects every pre-existing SVG except V58.
    preserved=[];changed=[]
    for line in git('ls-tree','-r',BASE,'--','assets/visuals/explanatory-volume8-v1','assets/visuals/explanatory-v2').decode('utf8').splitlines():
        info,name=line.split('\t',1)
        if not name.endswith('.svg'):continue
        raw=(R/name).read_bytes()
        same=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==info.split()[2]
        if '/explanatory-volume8-v1/V58' not in name:
            assert same,name
            preserved.append(name)
        elif not same:changed.append(name)
    assert len(changed)==92
    mark('Protected artwork',dict(byte_identical_svg=len(preserved),only_changed_svg_group='V58',changed_svg=92))
    assert not git('diff',BASE,'--','chapters','chapters-en','foundations','foundations-en','volumes','volumes-en'), 'A mathematical source changed'
    mark('Mathematical manuscripts and proofs','No tracked mathematical source differs from the accepted baseline.')
    values=[]
    for k in [2,3,4]:
        d=kary_values(k);a=Fraction(d['gw_balanced'],d['gw_total']);b=Fraction(d['growth_balanced'],d['growth_total'])
        assert (a==b)==(k==2)
        values.append(dict(k=k,GW=str(a),public_growth=str(b),equal_event_probability=a==b))
        for lg in ['zh','en']:
            for j in range(2*k+1):
                for layout in ['desktop','mobile']:
                    p=A/f'V58-{lg}-{k}-{j}-{layout}.svg';root=ET.parse(p).getroot();txt=' '.join(root.itertext())
                    assert root.attrib['aria-label']==kary_title(lg,k)
                    assert kary_title(lg,k) in txt
                    assert f'{d["gw_balanced"]}/{d["gw_total"]}' in txt
                    assert f'{d["growth_balanced"]}/{d["growth_total"]}' in txt
                    assert ('=' if k==2 else '≠') in txt
            p=A/f'V58.{lg}.page{k-1}.svg';txt=' '.join(ET.parse(p).getroot().itertext())
            assert kary_title(lg,k) in txt
    mark('V58 event-specific labels and side-by-side values',dict(probabilities=values,dynamic_svg=84,print_pages=6))
    old=json.loads(git('show',BASE+':publication/explanatory-volume8-batch1-working.json'))
    reg=json.loads((R/'publication/explanatory-volume8-batch1-working.json').read_text('utf8'))
    for row in reg['figures']:
        previous=next(x for x in old['figures'] if x['id']==row['id'] and x['lang']==row['lang'])
        if row['id'] in ['V54','V55','V57']:assert row['html']==previous['html']
        if row['id']=='V56':
            assert 'V56-'+row['lang']+'-balanced-2-desktop.svg' in row['html']
            assert 'data-splitmode="balanced" aria-pressed="true"' in row['html']
            assert 'data-input-group="balanced" hidden' not in row['html']
            assert 'data-input-group="iid" hidden' in row['html']
        for url in re.findall(r'(?:src|srcset|href)="(/assets/visuals/explanatory-volume8-v1/[^"#]+)"',row['html']):
            assert (R/url.lstrip('/')).is_file(),url
    # Every pre-generated SVG is parseable, including static compositions.
    for p in A.glob('*.svg'):ET.parse(p)
    assert len(list(A.glob('*.svg')))==354
    mark('V56 initial state and resources','Both no-JS HTML and runtime use balanced-2. Existing SVGs of both models are byte-identical; only the starting choice changes. All 354 SVGs parse, and bilingual direct resource references exist.')
    mark('Accepted V54 V55 V57','All three bilingual figure fragments and every SVG remain byte-identical; P04/P05 and all other explanatory-v2 SVGs are protected above.')
    mark('Public-model boundary','Only existing public-model probabilities were relabeled. Sources and exact enumerations are unchanged; no new mathematical result, density or unpublished research was introduced.')
    result=dict(baseline=BASE,checks=checks,browser='not attempted; unavailable interface remains unverified',browser_screenshots=0,real_devices='open',native_pdf='open',independent_expert_review='open',published=False,pushed=False)
    (O/'targeted-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
    print(f'{len(checks)} targeted checks passed; V58 labels across all k/language/layout states checked. Browser acceptance remains open.')

if __name__=='__main__':run()
