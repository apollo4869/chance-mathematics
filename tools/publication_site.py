"""Reader-facing authorship, citation, rights and verifiable edition metadata."""
from pathlib import Path
import hashlib,html,json,re,shutil,subprocess

ROUTES={'author':'author.html','citation':'citation.html','copyright':'copyright-attribution.html',
        'versions':'versions.html','contributors':'contributors.html','privacy':'privacy.html'}
LABELS={
 'author':('作者介绍','About the author'),'citation':('引用本书 · Citation','Citation'),
 'copyright':('版权与署名 · Copyright & Attribution','Copyright & Attribution'),
 'versions':('版本与发布快照','Versions & snapshots'),'contributors':('贡献与审阅署名','Contributors & review credits'),'privacy':('阅读统计与隐私','Reading statistics & privacy')}
esc=lambda x:html.escape(str(x),quote=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
def write_json(p,v):
    import time
    data=(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
    if p.exists() and p.read_bytes()==data:return
    pending=p.with_name(p.name+'.pending')
    try:
        for attempt in range(6):
            try:
                pending.write_bytes(data)
                pending.replace(p)
                break
            except OSError as error:
                if attempt==5 or (getattr(error,'winerror',None) not in {5,32} and error.errno!=22):raise
                time.sleep(.15*2**attempt)
    finally:
        if pending.exists():pending.unlink()

class PublicationSite:
    def __init__(self,root):
        self.root=root;self.book=json.loads((root/'publication/book.json').read_text('utf-8'))
        self.materials=json.loads((root/'publication/materials.json').read_text('utf-8'))
        self.credits=json.loads((root/'publication/contributors.json').read_text('utf-8'))
        self.releases=[json.loads(p.read_text('utf-8')) for p in sorted((root/'publication/releases').glob('*.json'))]
        self.formal=max((r for r in self.releases if r['kind']=='FORMAL_WEB_PUBLICATION'),key=lambda r:(r['published_date'],r['hosting_version_number']))
        statuses=json.loads((root/'docs/AUTHOR_REVIEW_STATUS.json').read_text('utf-8')) if (root/'docs/AUTHOR_REVIEW_STATUS.json').exists() else json.loads((root/'publication/editorial-status.json').read_text('utf-8'))
        self.chapters=[]
        inputs=json.loads((root/'provenance/build-inputs.json').read_text('utf-8'))
        for i,name in enumerate(inputs['chapters'],1):
            row={'chapter':i,'slug':Path(name).stem,'author':'Haobai Wang','languages':{}}
            for language,folder in [('zh-CN','chapters'),('en','chapters-en')]:
                path=folder+'/'+name;data=(root/path).read_bytes()
                match=re.search(r'^#{1,2}\s+((?:第.+章|Chapter \d+)[：:].+)$',data.decode('utf-8'),re.M)
                try:
                    commit=subprocess.check_output(['git','log','-1','--format=%H','--',path],cwd=root,stderr=subprocess.DEVNULL).decode().strip()
                    committed=subprocess.check_output(['git','show',commit+':'+path],cwd=root,stderr=subprocess.DEVNULL)
                    dirty=committed!=data
                except subprocess.CalledProcessError:commit=None;dirty=True
                row['languages'][language]={'path':path,'title':match[1] if match else Path(name).stem,
                    'sha256':sha(data),'version':f'ch{i:02}-'+('en-' if language=='en' else 'zh-')+sha(data)[:12],
                    'last_content_commit':commit,'uncommitted_content':dirty}
            status=next((r for r in statuses['chapters'] if r['chapter']==i),{})
            row['author_reading_approval']=status.get('author_reading_approval','NOT_RECORDED')
            row['mathematical_review']=status.get('mathematical_review','NOT_RECORDED')
            row['historical_verification']=status.get('historical_verification','NOT_RECORDED')
            row['engineering_build']='LOCAL_PAGES_GENERATED'
            row['edition_status']='LOCAL_PREVIEW_NOT_FORMAL_PUBLICATION'
            row['formal_history']=[{'release_id':r['release_id'],'source_commit':r['source_commit'],'source_sha256':c['source_sha256']} for r in self.releases if r['kind']=='FORMAL_WEB_PUBLICATION' for c in r['chapters'] if c['chapter']==i]
            self.chapters.append(row)
        self.preview='preview-'+sha(json.dumps([{k:v['sha256'] for k,v in r['languages'].items()} for r in self.chapters],sort_keys=True).encode())[:12]

    def link(self,key,en=False):return ('/en/' if en else '/')+ROUTES[key]

    def author_card(self,en=False):
        bio=self.book['biography_en' if en else 'biography_zh']
        return ('<section class="home-author" id="author" aria-labelledby="author-heading"><div class="author-monogram" aria-hidden="true">HW</div><div>'
                '<p class="pub-eyebrow">'+('PRIMARY AUTHOR' if en else '主作者')+'</p><h2 id="author-heading">Haobai Wang</h2>'
                '<p>'+esc(bio)+'</p><a href="'+self.link('author',en)+'">'+('About the author' if en else '作者介绍')+'</a>'
                '<span aria-hidden="true"> · </span><a href="'+self.link('citation',en)+'">'+('Cite this book' if en else '引用本书')+'</a></div></section>')

    def footer(self,en=False):
        nav=''.join('<a href="'+self.link(k,en)+'">'+esc(LABELS[k][int(en)])+'</a>' for k in ROUTES)
        rights=('Rights reserved where lawfully owned; third-party rights and statutory exceptions preserved.' if en else '依法归作者所有的受保护部分保留权利；第三方权利及法定例外不受影响。')
        return '<footer class="publication-footer"><p>© 2026 Haobai Wang · '+rights+'</p><nav aria-label="'+('Publication information' if en else '出版信息')+'">'+nav+'</nav><p>'+('Free to read · Share official links for teaching · Local preview' if en else '免费阅读 · 欢迎教学分享正式链接 · 当前为本地预览')+'</p></footer>'

    def chapter_bar(self,key,en=False):
        if not key.startswith('chapter-'):return ''
        row=self.chapters[int(key.split('-')[1])-1];v=row['languages']['en' if en else 'zh-CN']
        return ('<details class="chapter-edition"><summary>Haobai Wang · '+('Local preview' if en else '本地预览')+' · '+v['version']+'</summary>'
                '<p>'+('This content fingerprint identifies the text, not a formal release or an independent proof of authorship.' if en else '内容指纹用于核对本章文本，不表示正式发布或独立的作者身份证明。')+'</p><p>SHA-256: <code>'+v['sha256']+'</code></p>'
                '<a href="'+self.link('versions',en)+'#chapter-'+str(row['chapter'])+'">'+('Version history' if en else '版本记录')+'</a> · '
                '<a href="'+self.link('citation',en)+'?chapter='+str(row['chapter'])+'#chapter-citations">'+('Cite this chapter' if en else '引用本章')+'</a></details>')

    def head(self,key,en=False):
        title=self.book['title_en' if en else 'title']
        if key.startswith('chapter-'):title=self.chapters[int(key.split('-')[1])-1]['languages']['en' if en else 'zh-CN']['title']
        data={'@context':'https://schema.org','@type':'Book','name':title,'author':{'@type':'Person','name':'Haobai Wang'},
              'inLanguage':'en' if en else 'zh-CN','isAccessibleForFree':True,'version':self.preview}
        return ('<meta name="author" content="Haobai Wang"><meta name="citation_author" content="Wang, Haobai">'
                '<meta name="citation_title" content="'+esc(title)+'"><meta name="dcterms.rights" content="Rights reserved only where lawfully owned; statutory exceptions and third-party rights preserved.">'
                '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script>')

    def bib(self,kind='formal',chapter=None,en=False):
        if chapter is not None:
            row=self.chapters[chapter-1];v=row['languages']['en' if en else 'zh-CN'];title=v['title']
            note='Unpublished local preview; '+v['version']+'; SHA-256 '+v['sha256'];key='wang2026chance_ch'+str(chapter)+('_en' if en else '')
        else:
            title=self.book['title'];key='wang2026chance'+('_preview' if kind=='preview' else '')
            note=(f"Formal web version {self.formal['hosting_version_number']}; first {self.formal['chapter_count']} chapters; source snapshot {self.formal['release_id']}"
                  if kind=='formal' else 'Unpublished local preview; '+self.preview)
        lines=['@misc{'+key+',','  author = {Wang, Haobai},','  title = {{'+title+'}},','  year = {2026},',
               '  howpublished = {'+('Online book' if kind=='formal' and chapter is None else 'Unpublished working draft')+'},']
        if kind=='formal' and chapter is None:lines.append('  url = {'+self.book['canonical_url']+'},')
        lines.extend(['  note = {'+note+'}','}'])
        return '\n'.join(lines)

    def copy_box(self,name,text,en=False):
        return '<div class="citation-box"><button type="button" data-copy-target="'+name+'">'+('Copy BibTeX' if en else '复制 BibTeX')+'</button><pre><code id="'+name+'">'+esc(text)+'</code></pre><p class="copy-feedback" aria-live="polite"></p></div>'

    def bodies(self,en=False):
        t=lambda zh,eng:eng if en else zh
        b=self.book;bio=b['biography_en' if en else 'biography_zh']
        author='<p class="pub-eyebrow">'+t('主作者','PRIMARY AUTHOR')+'</p><h1>Haobai Wang</h1><p class="pub-lead">'+esc(bio)+'</p>'
        author+='<h2>'+t('关于这部著作','About the book')+'</h2><p>'+esc(b['title_en' if en else 'title'])+'</p><p>'+t(
            '这是一部持续发展的长篇数学著作。正式发布、作者阅读采用、数学审校与史料核验分别记录，读者可以按版本追溯具体内容。',
            'This is a developing long-form mathematical work. Formal release, author adoption, mathematical review and historical verification are recorded separately so readers can identify the text of each edition.')+'</p>'
        author+='<h2 id="writing-principles">'+t('写作与采用','Writing and editorial adoption')+'</h2><p>'+t(
            '主作者决定全书选题、叙事方向、内容取舍和最终采用。AI辅助草拟、讨论、翻译和工程的情况单独披露；主作者署名不意味着所有AI输出都自动获得版权保护，也不意味着全部数学与史料已通过终审。',
            'The primary author directs questions, narrative, content selection and adoption. AI assistance with drafting, discussion, translation and engineering is disclosed separately. Attribution does not automatically make every AI output copyrightable or certify final mathematical and historical review.')+'</p><p><a href="'+self.link('copyright',en)+'">'+t('版权与 AI 辅助说明','Rights and AI-assistance statement')+'</a> · <a href="'+('/en/' if en else '/')+'writing-rules.html">'+t('公开写作原则','Public writing principles')+'</a></p>'

        citation='<h1>'+t('引用本书 · Citation','Citation')+'</h1><p class="pub-lead">'+t(
            '请引用 Haobai Wang，并注明实际阅读的版本。正式网页、公开八章源码快照和当前本地预览不是同一个版本。',
            'Credit Haobai Wang and identify the edition actually consulted. The formal website, public eight-chapter source snapshot and current local preview are different editions.')+'</p>'
        citation+='<h2>'+t('正式网页版本','Formal web edition')+'</h2><p>Haobai Wang. '+esc(b['title'])+'. 2026. '+t(f"正式网页第{self.formal['hosting_version_number']}版，前{self.formal['chapter_count']}章。",f"Formal web version {self.formal['hosting_version_number']}, first {self.formal['chapter_count']} chapters.")+' <a href="'+b['canonical_url']+'">'+t('正式阅读网址','Official reading URL')+'</a>.</p>'
        citation+=self.copy_box('cite-formal',self.bib(),en)
        citation+='<p><a href="/metadata/book-citation.bib" download>BibTeX ↓</a> · <a href="/metadata/CITATION.cff" download>CITATION.cff ↓</a></p>'
        citation+='<h2>'+t('引用当前本地预览','Citing this local preview')+'</h2><p>'+t(
            '当前预览尚未正式发布。不填造出版社、ISBN、DOI或一个并不存在的公开第九章网址；可随所分享的预览文件保留版本指纹。',
            'This preview is unpublished. No publisher, ISBN, DOI or nonexistent public Chapter 9 URL is invented. Retain its fingerprint with any preview file shared for review.')+'</p>'+self.copy_box('cite-preview',self.bib('preview'),en)
        citation+='<h2 id="chapter-citations">'+t('引用本章工作稿','Citing a chapter draft')+'</h2><label for="citation-chapter">'+t('选择章节','Choose a chapter')+'</label> <select id="citation-chapter">'
        citation+=''.join('<option value="'+str(r['chapter'])+'">'+esc(r['languages']['en' if en else 'zh-CN']['title'])+'</option>' for r in self.chapters)+'</select>'
        for row in self.chapters:
            i=row['chapter'];citation+='<section class="chapter-citation" data-citation-chapter="'+str(i)+'"'+(' hidden' if i!=1 else '')+'><h3>'+esc(row['languages']['en' if en else 'zh-CN']['title'])+'</h3>'+self.copy_box('cite-chapter-'+str(i),self.bib('preview',i,en),en)+'</section>'
        citation+='<p>'+t('引用格式是学术署名工具，不等于转载、改编或商业再出版许可。','A citation supplies scholarly attribution; it is not permission to republish, adapt or commercially reissue protected material.')+'</p>'

        rights='<h1>Copyright &amp; Attribution</h1><p class="pub-lead">© 2026 Haobai Wang · '+t('限依法归作者所有的受保护部分。','For protected material lawfully owned by the author.')+'</p>'
        rights+='<h2>'+t('阅读与教学分享','Reading and teaching links')+'</h2><p>'+t(
            '网站免费阅读，欢迎教师向学生分享正式网页链接。可保留署名与权利说明，使用本站提供的离线包个人阅读；不因此开放一般性的转载、改编、再分发或商业再出版权限。',
            'The website is free to read. Teachers are welcome to share official webpage links with students. Provided offline packages may be used for personal reading with attribution and rights notices retained. These facilities grant no general republication, adaptation, redistribution or commercial reissue rights.')+'</p>'
        rights+='<h2>'+t('分层许可','Separate material policies')+'</h2><table><thead><tr><th>'+t('材料','Material')+'</th><th>'+t('当前规则','Current policy')+'</th></tr></thead><tbody>'
        rows=[(t('书籍正文与编排','Book text and arrangement'),t('对依法归作者所有的原创表达、选择与编排保留权利；不采用CC BY-SA 4.0。','Rights reserved in original expression, selection and arrangement lawfully owned by the author; no CC BY-SA 4.0 adoption.')),
              (t('项目程序代码','Project software'),t('单独管理；尚未选择通用开放源码许可，不自动套用正文许可。','Managed separately; no general open-source licence selected. Text policy does not relicense code.')),
              (t('项目制作的封面与图示','Project-created cover and diagrams'),t('逐项记录来源与AI辅助情况；“项目制作”不等于自动确认著作权。','Record provenance and AI assistance per item; project creation does not automatically establish copyright.')),
              (t('第三方代码','Third-party software'),'; '.join(esc(d['name']+' '+d['version']+' — '+d['license']) for d in self.materials['third_party_software'])+'. '+t('原许可另存并随包保留。','Original notices are retained with distributions.')),
              (t('图片、引文及其他第三方材料','Images, quotations and other third-party material'),t('原权利人与已有许可不变；标注来源不是获得再利用许可的证明。','Original holders and existing permissions remain; attribution is not evidence of a reuse licence.'))]
        rights+=''.join('<tr><td>'+a+'</td><td>'+v+'</td></tr>' for a,v in rows)+'</tbody></table>'
        rights+='<p>'+t(
            '法定版权例外、已经取得的第三方许可和适用的平台条款继续有效。不对数学事实、思想、公有领域材料或他人内容主张排他权利。未另行授权时，不开放对受保护且归作者所有内容的一般再利用权。',
            'Statutory exceptions, existing third-party permissions and applicable platform terms remain effective. No exclusive rights are claimed over mathematical facts, ideas, public-domain material or others’ content. No general reuse rights in protected author-owned material are granted without further authorization.')+'</p>'
        rights+='<h2 id="ai-assistance">'+t('AI 辅助创作','AI-assisted creation')+'</h2><p>'+t(
            '本项目使用 ChatGPT、Codex 等工具辅助资料检索、草拟、数学讨论、编辑、翻译与网站工程。Haobai Wang 统筹思想与叙事、选择和修订，并决定采用内容。AI工具不列为人类作者或审稿者。',
            'ChatGPT, Codex and related tools assist research, drafting, mathematical discussion, editing, translation and website engineering. Haobai Wang directs ideas and narrative, selection, revision and editorial adoption. AI tools are not listed as human authors or reviewers.')+'</p><p>'+t(
            '不将自动生成的文本、代码或图像一概声明为受版权保护。具体权利依适用法律、实际人类贡献及第三方权利分别判断；仅署名或采用一个输出，并不自动证明该输出获得版权。当前审核状态在版本页单独列出。',
            'No blanket copyright claim is made over automatically generated text, code or images. Rights depend on applicable law, actual human contributions and third-party rights. Attribution or adoption alone does not establish copyright in an output. Review states are recorded separately on the versions page.')+'</p>'
        rights+='<h2>'+t('第三方图片登记','Third-party image register')+'</h2><p>'+t('现有20张图片保留来源与文件指纹，许可仍待逐项核验；没有将其统一归属主作者，也没有新增再利用授权。','The 20 existing images retain sources and fingerprints. Their licences remain subject to verification; they are neither assigned wholesale to the primary author nor given new reuse permissions.')+'</p><div class="pub-table-scroll"><table><thead><tr><th>'+t('文件','File')+'</th><th>'+t('来源','Source')+'</th><th>'+t('权利状态','Rights status')+'</th></tr></thead><tbody>'
        for image in self.materials['third_party_images']:
            urls=' · '.join('<a href="'+esc(u)+'" rel="noopener noreferrer">'+esc(u.split('/')[2])+'</a>' for u in image['source_urls']) or t('来源待核','Source pending')
            rights+='<tr><td><code>'+esc(image['path'])+'</code></td><td>'+urls+'</td><td>'+t('原权利保留 · 许可未核实','Original rights retained · licence unverified')+'</td></tr>'
        rights+='</tbody></table></div><p><a href="/metadata/materials.json">'+t('完整材料清单与SHA-256','Complete material register and SHA-256')+'</a> · <a href="/metadata/LICENSE.md">LICENSE.md</a> · <a href="/metadata/licenses/markdown-it-LICENSE.txt">markdown-it licence</a> · <a href="/metadata/licenses/mathjax-full-LICENSE.txt">MathJax licence</a> · <a href="/metadata/licenses/beautifulsoup4-LICENSE.txt">Beautiful Soup licence</a> · <a href="/metadata/licenses/soupsieve-LICENSE.txt">Soup Sieve licence</a></p>'
        rights+='<h2>'+t('说明依据与隐私边界','Policy references and privacy')+'</h2><p>'+t(
            'AI与人类贡献的区分可参阅美国版权局2025年报告摘要（仅作为该法域的参考，不当作全球统一结论）；公开仓库与许可的关系参阅GitHub说明。私人写作记录、提示词、私下审稿通信及未发布研究不随公开下载导出。',
            'For a jurisdiction-specific reference on AI and human contributions, see the US Copyright Office’s 2025 summary; it is not presented as a universal legal conclusion. GitHub explains the relation between public repositories and licensing. Private writing records, prompts, private review correspondence and unpublished research are excluded from public downloads.')+'</p><p><a href="https://www.copyright.gov/newsnet/2025/1060.html">U.S. Copyright Office</a> · <a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository">GitHub licensing guidance</a></p>'

        versions='<h1>'+t('版本与发布快照','Versions & publication snapshots')+'</h1><p class="pub-lead">'+t('正式发布、公开源码快照与本地预览分别记录。内容哈希和Git记录用于核验版本，不能替代作者身份认证、版权登记或独立可信时间戳。','Formal publication, public source snapshots and local previews are recorded separately. Hashes and Git history verify content versions; they are not identity certification, copyright registration or independently trusted timestamps.')+'</p>'
        r=self.formal
        deployment_hash=r.get('original_deployment_archive_sha256')
        versions+='<h2>'+t(f"已有正式网页：{r['chapter_count']}章，第{r['hosting_version_number']}版",f"Existing formal website: {r['chapter_count']} chapters, version {r['hosting_version_number']}")+'</h2><p><a href="'+b['canonical_url']+'">'+t('正式网页','Official website')+'</a> · '+esc(r['published_date'])+'</p><p>'+t('部署源提交','Deployed source commit')+': <code>'+r['source_commit']+'</code></p>'
        if deployment_hash:
            versions+='<p>'+t('原部署包SHA-256','Original deployment archive SHA-256')+': <code>'+deployment_hash+'</code></p>'
        versions+='<p>'+t(f"下面的正文快照保留对应正式版本的{r['chapter_count']}章及登记的进阶/配套材料，共{len(r['files'])}个原稿文件。它不含私人记录，不是原始部署包的镜像，两个包的哈希不能混用。",f"The manuscript snapshot retains {r['chapter_count']} chapters and the registered advanced/supporting material: {len(r['files'])} source files. It excludes private records and is not a mirror of the original deployment archive; their hashes must not be confused.")+'</p><p><a href="/releases/'+r['archive_file']+'" download>'+t('正式正文快照 ZIP','Formal manuscript snapshot ZIP')+'</a> · <a href="/releases/'+r['release_id']+'.json">'+t('发布回执与逐文件清单','Release evidence and file manifest')+'</a></p><p>'+t('正文快照SHA-256','Manuscript snapshot SHA-256')+': <code>'+r['archive_sha256']+'</code></p>'
        versions+='<h2>'+t('公开八章源码快照','Public eight-chapter source snapshot')+'</h2><p><a href="'+b['repository_url']+'/tree/b64f4abd06db8bb17e64b7aa1ed343995bff3a26">GitHub · b64f4ab</a> — '+t('源码公开不等于正式书籍版本发布，也不表示数学或史料终审通过。','Public source does not imply a formal book release or final mathematical or historical approval.')+'</p>'
        versions+='<h2>'+t('当前逐章预览版本','Current chapter preview versions')+'</h2><p>'+esc(self.preview)+' · '+t('所有下列条目均为本地预览；英文翻译仍待作者审阅。','All entries below are local previews; English translations await author review.')+'</p>'
        for row in self.chapters:
            zh=row['languages']['zh-CN'];eng=row['languages']['en'];v=eng if en else zh
            versions+='<details class="chapter-version" id="chapter-'+str(row['chapter'])+'"><summary>'+esc(v['title'])+'</summary><p>'+t('主作者','Primary author')+': Haobai Wang</p>'
            for lang,d in [('中文',zh),('English',eng)]:
                versions+='<p>'+lang+' · <code>'+d['version']+'</code><br>SHA-256: <code>'+d['sha256']+'</code><br>'+t('最近正文Git提交（可能仅本地可查）','Last content Git commit (may be local only)')+': <code>'+esc(d['last_content_commit'] or 'uncommitted')+'</code></p>'
            versions+='<p>'+t('工程构建','Engineering build')+': '+t('本地网页已生成（不代表学术审校通过）','Local pages generated (not academic approval)')+'<br>'+t('作者阅读状态','Author reading state')+': '+esc(row['author_reading_approval'])+'<br>'+t('数学审校','Mathematical review')+': '+esc(row['mathematical_review'])+'<br>'+t('史料核验','Historical verification')+': '+esc(row['historical_verification'])+'</p></details>'
        versions+='<p><a href="/metadata/chapter-versions.json">'+t('下载机器可读逐章版本清单','Machine-readable chapter versions')+'</a></p><h2>'+t('后续正式发布规则','Future formal releases')+'</h2><p>'+t('先取得作者明确发布授权，再冻结指定Git提交，生成不覆盖旧ID的原稿快照与逐文件SHA-256，保存部署回执并校验归档。作者认可章节不自动等于发布授权。本轮没有新正式发布。','Obtain explicit publication authorization, freeze a specified Git commit, create a new immutable snapshot ID and file hashes, retain deployment evidence, and verify the archive. Chapter approval is not automatic publication authorization. No new formal publication occurred in this update.')+'</p>'

        contributors='<h1>'+t('贡献与审阅署名','Contributors & review credits')+'</h1><p class="pub-lead">'+t('按实际贡献范围署名，不把所有参与方式合并成“共同作者”。','Credit the actual contribution scope rather than treating every form of participation as coauthorship.')+'</p>'
        role_names={'primary_author':t('主作者','Primary author'),'chapter_contributor':t('章节贡献者','Chapter contributor'),'reviewer':t('审稿者','Reviewer'),'technical_contributor':t('技术贡献者','Technical contributor')}
        for role,label in role_names.items():
            contributors+='<h2>'+label+'</h2>'
            selected=[r for r in self.credits['credits'] if r['role']==role and r['status']=='CONFIRMED' and r['public_attribution_approved']]
            for credit in selected:
                person=next(p for p in self.credits['people'] if p['id']==credit['person_id'])
                assert person['public_name_approved'];contributors+='<p>'+esc(person['display_name'])+' · '+esc(t('全书','Whole book') if credit['scope']=='whole_book' else credit['scope'])+'</p>'
            if not selected:contributors+='<p>'+t('目前没有经确认并同意公开署名的人类名单。','No confirmed human names approved for public credit have been recorded for this role.')+'</p>'
        contributors+='<h2>'+t('采用前确认','Before accepting contributions')+'</h2><p>'+t('分别确认贡献范围、本人公开署名同意及必要权利。投稿、Git提交或技术协助不自动转让著作权，不自动采用开放许可。审稿不等于对全书背书；AI工具另作披露，不列入人类作者或审稿者。','Confirm contribution scope, consent to public attribution and necessary rights separately. A submission, Git commit or technical contribution does not automatically transfer copyright or adopt an open licence. Review is not endorsement of the whole book. AI tools are disclosed separately, not credited as human authors or reviewers.')+'</p><p><a href="/metadata/CONTRIBUTING.md">'+t('贡献规则','Contribution policy')+'</a> · <a href="/metadata/contributors.json">'+t('公开署名登记','Public credit register')+'</a></p>'
        contributors+='<p>'+t('出版呈现参考《动手学深度学习》的作者/章节贡献者分工与可复制引用入口，未复制其正文或采用其许可。','Publication presentation takes inspiration from D2L’s author/chapter-contributor distinctions and copyable citation entry, without copying its prose or adopting its licence.')+' <a href="https://zh.d2l.ai/">D2L 中文</a> · <a href="https://d2l.ai/">D2L English</a></p>'
        privacy=(self.root/'publication'/('privacy.en.html' if en else 'privacy.zh.html')).read_text('utf-8')
        return {'author':author,'citation':citation,'copyright':rights,'versions':versions,'contributors':contributors,'privacy':privacy}

    def export_metadata(self):
        dist=self.root/'dist';folder=dist/'metadata';folder.mkdir(exist_ok=True)
        write_json(folder/'chapter-versions.json',{'schema_version':1,'preview_id':self.preview,'formal_release':self.formal['release_id'],'chapters':self.chapters})
        for name in ['book.json','contributors.json','materials.json']:shutil.copyfile(self.root/'publication'/name,folder/name)
        for name in ['LICENSE.md','CONTRIBUTING.md','CITATION.cff']:shutil.copyfile(self.root/name,folder/name)
        (folder/'book-citation.bib').write_bytes((self.bib()+'\n').encode())
        shutil.copytree(self.root/'licenses',folder/'licenses',dirs_exist_ok=True)
        shutil.copytree(self.root/'publication/releases',dist/'releases',dirs_exist_ok=True)
