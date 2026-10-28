"""Explicit public-content boundary shared by downloads, snapshots and exports."""
from pathlib import Path
import json,os,hashlib

PUBLIC_FOLDERS = {'chapters', 'chapters-en', 'advanced', 'advanced-en', 'foundations', 'foundations-en', 'assets', 'tools', 'publication', 'licenses', 'volumes', 'volumes-en'}
PUBLIC_TRANSLATIONS = {'math-labels.json', 'ui-labels.json', 'manifest.json', 'proofs.md', 'reading-routes.md', 'references.md'}
PUBLIC_METADATA = {'provenance/build-inputs.json', 'provenance/charts.json'}
PUBLIC_DOCS = {'docs/GITHUB_PUBLIC_SOURCE.md', 'docs/PUBLIC_SOURCE_INTEGRITY.json'}
PRIVATE_PLANNING_TOOLS = {'tools/book_plan.py', 'tools/check-book-plan.py', 'tools/test-book-plan.py','tools/check-chapter11-adoption.py','tools/foundation_preservation.py','tools/check-foundation-supplements.py','tools/check-publication.py','tools/check-chapter10-refinements.py','tools/academic_preservation.py','tools/check-academic-navigation.py'}
PRIVATE_PLANNING_TOOLS.update({'tools/chapter13_preservation.py','tools/sync-chapter13-protection.py','tools/check-chapter13.py'})
PRIVATE_PLANNING_TOOLS.add('tools/chapter13_adoption.py')
PRIVATE_PLANNING_TOOLS.update({'tools/chapter14_preservation.py','tools/sync-chapter14-protection.py','tools/check-chapter14.py'})
PRIVATE_PLANNING_TOOLS.add('tools/chapter14_review.py')
PRIVATE_PLANNING_TOOLS.update({'tools/chapter15_preservation.py','tools/sync-chapter15-protection.py','tools/prepare-chapter15-metadata.py','tools/check-chapter15.py'})
PRIVATE_PLANNING_TOOLS.update({'tools/check-volume-navigation.py','tools/batch16_20.py','tools/update-batch16-20.py','tools/check-batch16-20.py'})
PRIVATE_PLANNING_TOOLS.add('tools/targeted16_20_review.py')
PRIVATE_PLANNING_TOOLS.add('tools/deep16_20.py')
PRIVATE_PLANNING_TOOLS.add('tools/chapter20_recreation.py')
PRIVATE_PLANNING_TOOLS.add('tools/chapter17_revision.py')
PRIVATE_PLANNING_TOOLS.add('tools/chapter21_preservation.py')
PRIVATE_PLANNING_TOOLS.update({'tools/chapter22_preservation.py','tools/chapter23_preservation.py','tools/chapter24_preservation.py','tools/chapter25_preservation.py','tools/chapter26_preservation.py','tools/chapter27_preservation.py'})
PRIVATE_PLANNING_TOOLS.update({'tools/chapter27_closure.py','tools/chapter28_preservation.py','tools/chapter29_preservation.py'})
PUBLIC_TOP = {'README.md', 'LICENSE.md', 'CONTRIBUTING.md', 'CITATION.cff', 'package.json', 'pnpm-lock.yaml', 'requirements.txt',
              '.gitignore', '.gitattributes', 'build.py', 'build-chapters.py', 'prepare-publication.py', 'preview.ps1',
              'style.css', 'home.css', 'reader-mode.css', 'reader-mode.js', 'home-ui.js', 'enhancements.css', 'app.js',
              'experiments.js', 'test_experiments.js', 'site-links.json', 'baseline-manuscript.json', 'verify-chapters.py',
              '校订与证明补充.md', '引用与配图来源.md', '延伸阅读与证明路线.md'}
PUBLIC_TOP.add('VISUAL_STYLE_GUIDE.md')

def public_path(name):
    p = Path(name); parts = p.parts
    if name in PRIVATE_PLANNING_TOOLS or name in {'tools/restructure-brownian.py','tools/sync-academic-protection.py','tools/export-academic-originals.py','tools/sync-intro-protection.py','tools/sync-opening-polish.py','tools/check-chapter-openings.py'}: return False
    if not parts or any(x in {'node_modules', '.git', '__pycache__'} for x in parts): return False
    return (parts[0] in PUBLIC_FOLDERS
            or (len(parts) == 3 and parts[:2] == ('translations', 'en') and p.name in PUBLIC_TRANSLATIONS)
            or name in PUBLIC_METADATA or name in PUBLIC_DOCS or name in PUBLIC_TOP
            or name == 'archives/before-brownian-restructure/04-brownian.md')

def public_sources(root):
    """Walk only declared trees, never private records or dependency directories."""
    paths = [root/name for name in PUBLIC_TOP | PUBLIC_METADATA | PUBLIC_DOCS]
    paths += [root/'archives/before-brownian-restructure/04-brownian.md']
    for folder in PUBLIC_FOLDERS | {'translations'}:
        base = root/folder
        if base.exists(): paths.extend(p for p in base.rglob('*') if p.is_file())
    files=[(p.relative_to(root).as_posix(), p.read_bytes()) for p in set(paths)
           if p.is_file() and public_path(p.relative_to(root).as_posix())]
    # Server sources only: never traverse local D1, secrets, dependencies or generated book copies.
    host=root/'analytics-host'
    if host.exists():
        excluded={'node_modules','.git','.wrangler','.sites-runtime','.vinext','.next','dist','outputs','work','examples','__pycache__'}
        for base,dirs,names in os.walk(host):
            dirs[:]=[d for d in dirs if d not in excluded]
            for name in names:
                p=Path(base)/name;rel=p.relative_to(host).as_posix()
                if (name.startswith(('.env','.dev.vars')) and name!='.env.example') or name.endswith(('.tsbuildinfo','.log')):continue
                if rel.startswith('public/') and rel not in {'public/reader-analytics.js','public/privacy-controls.js','public/campaign-attribution.js','public/analytics-dashboard.js','public/favicon.svg'}:continue
                files.append(('analytics-host/'+rel,p.read_bytes()))
    return sorted(files)

def public_baseline(root, names):
    value = json.loads((root/'baseline-manuscript.json').read_text('utf-8'))
    value['files'] = {p:h for p,h in value['files'].items() if p in names}
    # Reader-source exports clean archival wrappers only, preserving every math body.
    audit=json.loads(names['publication/reader-source-sanitization.json']) if 'publication/reader-source-sanitization.json' in names else {'files':{}}
    changed=set(audit['files'])|{'translations/en/manifest.json'}
    for p in changed&value['files'].keys():value['files'][p]=hashlib.sha256(names[p]).hexdigest()
    value['reader_source_cleanup']='Archival editorial wrappers only; canonical/body hashes are recorded in publication/reader-source-sanitization.json.'
    value['source_root'] = 'public-book-source'
    value['author_policy'] = 'Included manuscript hashes are preserved; private author planning and decisions are omitted.'
    value['public_export_scope'] = 'Original included book hashes retained; private author notes and archives excluded.'
    value.pop('previous_baseline', None)
    value.pop('previous_git_ref', None); value.pop('previous_baseline_git_ref', None)
    return (json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode()

def checked_public_sources(root):
    files = dict(public_sources(root))
    try:from academic_navigation import sanitize_reader_sources
    except ImportError:from .academic_navigation import sanitize_reader_sources
    files,_=sanitize_reader_sources(root,files)
    files['baseline-manuscript.json'] = public_baseline(root, files)
    files['README.md'] = ('# 偶然的数学 / The Mathematics of Chance\n\nPrimary author: Haobai Wang.\n\n'
        'Complete book manuscripts and engineering, with private notes excluded. See LICENSE.md, CITATION.cff and CONTRIBUTING.md. '
        'Formal releases and working previews are distinct; see the website versions page.\n\n'
        'Build: install Python requirements.txt and Node package.json dependencies, then run python build.py. '
        'Open dist/index.html for offline reading, or python -m http.server 8768 --bind 127.0.0.1 --directory dist.\n\n'
        'Copyright and third-party materials are managed separately in publication/materials.json. '
        'Public source is not a general reuse licence.\n').encode()
    return sorted(files.items())

PRIVATE_PLANNING_TOOLS.update({'tools/volume4_closure.py','tools/check-volume4-closure.py'})

PRIVATE_PLANNING_TOOLS.update({'tools/chapter30_preservation.py','tools/check-chapter30.py'})

PRIVATE_PLANNING_TOOLS.update({'tools/chapter31_preservation.py','tools/check-chapter31.py'})
