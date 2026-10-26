/* Portable, deterministic offline build: Node.js + dependencies in package.json. */
const fs=require('fs'),path=require('path');
const MarkdownIt=require('markdown-it');
const {mathjax}=require('mathjax-full/js/mathjax.js');
const {TeX}=require('mathjax-full/js/input/tex.js');
const {SVG}=require('mathjax-full/js/output/svg.js');
const {liteAdaptor}=require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler}=require('mathjax-full/js/handlers/html.js');
const {AllPackages}=require('mathjax-full/js/input/tex/AllPackages.js');
const root=path.resolve(__dirname,'..'),english=process.argv.includes('--english');
const aliases={'写作约定与全书编排.md':'translations/en/writing-rules.md','校订与证明补充.md':'translations/en/proofs.md','延伸阅读与证明路线.md':'translations/en/reading-routes.md','引用与配图来源.md':'translations/en/references.md'};
const sourcePath=p=>english?(aliases[p]||(p.startsWith('chapters/')?p.replace('chapters/','chapters-en/'):p.startsWith('advanced/')?p.replace('advanced/','advanced-en/'):p)):p;
const read=p=>fs.readFileSync(path.join(root,sourcePath(p)),'utf8')+(p==='style.css'?'\n'+fs.readFileSync(path.join(root,'enhancements.css'),'utf8'):'');
const suffix=english?'-en':'';
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);
const mathDocument=mathjax.document('',{InputJax:new TeX({packages:AllPackages}),OutputJax:new SVG({fontCache:'none'})});
const input=JSON.parse(read('provenance/build-inputs.json'));
function chineseNumber(n){const d='零一二三四五六七八九';return n<10?d[n]:n<20?'十'+(n%10?d[n%10]:''):d[Math.floor(n/10)]+'十'+(n%10?d[n%10]:'');}
const chapterCountLabel='前'+chineseNumber(input.chapters.length)+'章';
const chartData=JSON.parse(read('provenance/charts.json'));
const md=new MarkdownIt({html:true,typographer:false,linkify:false});
let mathCount=0,mathErrors=[],headingCount=0,blockCount=0,toc=[],search=[];
const mathCache=new Map();
const formulaRecords=[];let currentSection=null;
function math(tex,display){
  mathCount++;formulaRecords.push({section:currentSection,ordinal:formulaRecords.filter(f=>f.section===currentSection).length+1,tex,display});const key=display+'|'+tex;
  if(!mathCache.has(key)){
    try{
      const html=adaptor.outerHTML(mathDocument.convert(tex,{display}));
      if(/data-mjx-error|<merror/.test(html))mathErrors.push(tex);
      mathCache.set(key,html);
    }catch(e){mathErrors.push(tex);mathCache.set(key,'<code>'+escape(tex)+'</code>');}
  }
  return `<${display?'div':'span'} class="formula ${display?'display':'inline'}" data-tex="${escape(tex)}" aria-label="${escape(tex)}">${mathCache.get(key)}<code class="tex-source">${escape(tex)}</code></${display?'div':'span'}>`;
}
function imageData(src){
 if(src.startsWith('../assets/'))src=src.slice(3);
 if(!fs.existsSync(path.join(root,src)))throw Error('Missing image: '+src);
 return '/'+src;
}

function render(source,id){
  currentSection=id;
  let formulas=[];
  source=source.replace(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g,(full,block,inline)=>{
    const n=formulas.length;formulas.push(math((block??inline).trim(),block!==undefined));
    return block!==undefined?`\n\nMATHBLOCKTOKEN${n}END\n\n`:`MATHINLINETOKEN${n}END`;
  });
  const tokens=md.parse(source,{});
  tokens.forEach((t,i)=>{
    if(t.type==='heading_open'){
      const text=tokens[i+1].content;
      const anchor=`${id}-h${++headingCount}`;t.attrSet('id',anchor);
      const chapterNumber=id.startsWith('chapter-')?chineseNumber(Number(id.slice(8))):null;
      const namedChapter=text.match(english?/^Chapter\s+(\d+)\b/i:/^第([一二三四五六七八九十]+)章/);
      const preview=id.startsWith('chapter-')&&((namedChapter&&namedChapter[1]!== (english?id.slice(8):chapterNumber))||(english?/^Next chapter/i:/^下一章/).test(text));
      if(preview)t.attrSet('class','draft-preview');
      toc.push({id:anchor,text,htmlText:md.renderInline(text).replace(/MATH(?:INLINE|BLOCK)TOKEN(\d+)END/g,(_,n)=>formulas[+n]),level:Number(t.tag.slice(1)),section:id,preview});
    }
    if(t.type==='paragraph_open'){
      const anchor=`p${++blockCount}`;t.attrSet('id',anchor);
      if(tokens[i+1]?.type==='inline')search.push({id:anchor,text:tokens[i+1].content.replace(/MATH(?:INLINE|BLOCK)TOKEN\d+END/g,'公式'),section:id});
    }
  });
  let html=md.renderer.render(tokens,md.options,{});
  html=html.replace(/<p[^>]*>MATHBLOCKTOKEN(\d+)END<\/p>/g,(_,n)=>formulas[+n]);
  html=html.replace(/MATH(?:INLINE|BLOCK)TOKEN(\d+)END/g,(_,n)=>formulas[+n]);
  html=html.replace(/(<img\b[^>]*\bsrc=")([^"]+)(")/g,(_,a,src,b)=>a.replace('<img','<img id="image-'+path.basename(src).replace(/\./g,'-')+'"')+imageData(src)+b);
  html=html.replace(/(<a\b[^>]*\bhref=")assets\/images\/([^"/]+)(")/g,(_,a,file,b)=>a+'#image-'+file.replace(/\./g,'-')+b);
  return html;
}
function chart(obj,index){
 const width=720,height=320,L=60,R=25,T=25,B=55;
 const rows=obj.data,xs=rows.map(d=>d[obj.xKey]);
 const xmin=Math.min(...xs),xmax=Math.max(...xs);
 const ymax=Math.max(...rows.flatMap(d=>obj.series.map(s=>d[s.dataKey])))*1.08;
 const x=v=>L+(v-xmin)/(xmax-xmin)*(width-L-R),y=v=>height-B-v/ymax*(height-T-B);
 const colors=['#087e83','#b65d31','#765ab0'];
 let svg=`<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="${escape(obj.meta.title||obj.meta.description)}">`;
 for(let i=0;i<=4;i++){let v=ymax*i/4;svg+=`<path d="M${L} ${y(v)}H${width-R}" stroke="#9aa5a5" opacity=".23"/><text x="${L-10}" y="${y(v)+4}" text-anchor="end">${Number(v.toPrecision(3))}</text>`;}
 svg+=`<path d="M${L} ${T}V${height-B}H${width-R}" stroke="currentColor" fill="none"/>`;
 for(let i=0;i<=4;i++){const v=xmin+(xmax-xmin)*i/4;svg+=`<text x="${x(v)}" y="${height-B+25}" text-anchor="middle">${Number(v.toPrecision(4))}</text>`;}
 obj.series.forEach((s,i)=>{
  svg+=`<polyline points="${rows.map(d=>`${x(d[obj.xKey])},${y(d[s.dataKey])}`).join(' ')}" fill="none" stroke="${colors[i]}" stroke-width="2.5"/>`;
  rows.forEach(d=>svg+=`<circle cx="${x(d[obj.xKey])}" cy="${y(d[s.dataKey])}" r="3" fill="${colors[i]}"><title>${escape(obj.xKey)}=${d[obj.xKey]}，${escape(s.label)}=${d[s.dataKey]}</title></circle>`);
 });
 svg+=`<text x="${width/2}" y="${height-4}" text-anchor="middle">${escape(obj.xAxisLabel||obj.xKey)}</text></svg>`;
 const header=`<tr><th>${escape(obj.xKey)}</th>${obj.series.map(s=>`<th>${escape(s.label)}</th>`).join('')}</tr>`;
 const table=rows.map(d=>`<tr><td>${d[obj.xKey]}</td>${obj.series.map(s=>`<td>${d[s.dataKey]}</td>`).join('')}</tr>`).join('');
 return `<figure class="chart"><figcaption>${escape(obj.meta.title||'位移尺度比较')}</figcaption>${svg}<div class="legend">${obj.series.map((s,i)=>`<span style="color:${colors[i]}">● ${escape(s.label)}</span>`).join('　')}</div><p>${escape(obj.meta.description||'')}</p><details><summary>查看母稿数值表</summary><div class="table-scroll"><table>${header}${table}</table></div></details></figure>`;
}
const chapterTitles=input.chapters.map(p=>{
const txt=read('chapters/'+p);return (txt.match(english?/^#{1,2} Chapter\s+\d+[：:,].+$/im:/^#{1,2} 第[一二三四五六七八九十]章[：:].+$/m)||[])[0]?.replace(/^#+ /,'')||p;
});
const parts=[['rules',english?'Writing Principles and Book Plan':'写作约定与全书编排',read('写作约定与全书编排.md')],...input.chapters.map((p,i)=>['chapter-'+(i+1),chapterTitles[i],read('chapters/'+p)]),['supplement',english?'Corrections and Supplementary Proofs':'校订与证明补充',read('校订与证明补充.md')],['reading-routes',english?'Further Reading and Proof Routes':'延伸阅读与证明路线',read('延伸阅读与证明路线.md')],...(input.advanced_modules||[]).map(m=>[m.id,english?(read(m.file).match(/^#\s+(.+)$/m)||[])[1]||m.slug:m.title,read(m.file)]),['references',english?'References and Image Sources':'引用与配图来源',read('引用与配图来源.md')]];
const combined=(english?'# The Mathematics of Chance\n\nThe History, Ideas and Mathematical Structures of Probability\n\nComplete English working translation · 2026-10-26\n\n':'# 偶然的数学\n\n概率论的历史、思想与数学结构\n\n'+chapterCountLabel+' · 本地工作稿 · 2026-10-26\n\n')+parts.map(p=>p[2].replaceAll('../assets/','assets/')).join('\n\n---\n\n');
fs.mkdirSync(path.join(root,'build'),{recursive:true});
fs.writeFileSync(path.join(root,'build/combined-manuscript'+suffix+'.md'),combined);
let content=parts.map(([id,title,text],i)=>`<section id="${id}" class="book-section" data-title="${escape(title)}"><div class="section-kicker">${id.startsWith('chapter')?(english?'CHAPTER · ':'正文 · ')+id.split('-')[1]+' / '+input.chapters.length:(english?'Notes and resources':'编排与资料')}</div>${render(text,id)}<div class="chapter-links">${i?`<a href="#${parts[i-1][0]}">← ${escape(parts[i-1][1])}</a>`:''}${i<parts.length-1?`<a href="#${parts[i+1][0]}">${escape(parts[i+1][1])} →</a>`:''}</div></section>`).join('');
content=content.replace(/<div class="numeric-chart" data-chart="(\d+)"><\/div>/g,(_,n)=>chart(chartData[+n],+n));
let tocHTML=parts.map(([id,title])=>`<details ${id==='chapter-1'?'open':''}><summary><a href="#${id}">${escape(title)}</a></summary><div>${toc.filter(t=>t.section===id&&t.level<=3&&!t.preview&&!['《偶然的数学》','The Mathematics of Chance'].includes(t.text)&&!/（续）/.test(t.text)&&t.text!==title).map(t=>`<a class="toc-sub" href="#${t.id}">${t.htmlText}</a>`).join('')}</div></details>`).join('');
const html=`<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="偶然的数学：${chapterCountLabel}长篇工作稿分章审阅版，含故事、推导、历史引用及离线交互。"><title>偶然的数学 · ${chapterCountLabel}本地工作稿</title><style>${read('style.css')}</style></head><body><div class="progress" id="progress"></div><header class="topbar"><a href="#cover" class="brand">偶然的数学<span>CHANCE / MATHEMATICS</span></a><div class="tools"><button id="menu" aria-controls="sidebar" aria-expanded="false">目录</button><button id="search-toggle">检索</button><button id="font-down" aria-label="缩小正文字号">A−</button><button id="font-up" aria-label="放大正文字号">A＋</button><button id="theme">夜间</button><button id="tex-toggle">公式原码</button><button id="print">打印</button></div></header><aside id="sidebar"><div class="side-label">阅读目录 / CONTENTS</div><nav>${tocHTML}</nav><a class="aside-end" href="#edition">版本说明</a></aside><dialog id="search-dialog"><form method="dialog"><button class="close" aria-label="关闭检索">×</button></form><label for="search-input">检索全部正文</label><input id="search-input" type="search" placeholder="输入人物、概念或一句原文"><p id="search-count"></p><div id="search-results"></div></dialog><main><section id="cover" class="cover"><div class="eyebrow">概率论的历史、思想与数学结构</div><div class="cover-mark" aria-hidden="true">P</div><h1>偶然的数学</h1><p class="cover-en">THE MATHEMATICS OF CHANCE</p><p class="cover-lead">从一场没有结束的赌博，<br>到能够容纳随机路径的数学世界。</p><div class="edition-stamp">${chapterCountLabel} · 第${chineseNumber(input.chapters.length)}章创作 · 本地审阅候选 / 2026-10-26</div><p class="cover-note">保留故事展开、严格推导与思想之间的联系。${input.chapters.length}章正文、写作约定、历史来源、三项交互实验及校订补证均可离线阅读。</p><a class="start" href="#chapter-1">开始阅读 <span>→</span></a><button id="resume" hidden>继续上次阅读</button><a class="cover-secondary" href="#rules">先读写作约定与整体编排</a><div class="cover-line"></div></section><section id="edition" class="edition"><h2>版本与核对范围</h2><p>第一、二章已由作者完整阅读并认可，是叙事风格基准。第四章主体也已获作者认可，此前已更新结语及必要衔接；第三、五、六章仍待作者正式验收，第七章整体写作方向已获认可并完成定点小修，第八章待首次阅读。本候选依作者明确指令保留 Brownian motion 为第四章，将高级技术完整后移至独立模块；第三章仅添加理论依赖提示，第五、第六章主体不变。</p><p>来源档案、转换记录和既有校订分别保留。原聊天完整导出尚未独立核实；不能核实的地方在来源报告中标为待核。正文完整性、数学正确性、史料真实性和网页质量分别审计。</p><p>本候选包含第七章小修及第八章完整长篇工作稿，仅供本地阅读讨论，第八章尚未获作者采用，本轮无发布授权；线上仍为先前已发布的六章版本。工程构建不表示数学证明或史料核验已终审通过。原第四章完整快照随离线包保留；打印分页与断网双击运行仍待实测。外部来源链接需联网。</p></section>${content}<footer>《偶然的数学》 · ${chapterCountLabel}本地工作稿 · 2026-10-26<br>编辑原稿、母稿档案、变更清单和复核结果随离线包提供。</footer></main><button id="back-top" aria-label="返回顶部">↑</button><script>const BOOK_SEARCH=${JSON.stringify(search).replace(/</g,'\\u003c')};</script><script>${read('experiments.js')}</script><script>${read('app.js')}</script></body></html>`;
fs.writeFileSync(path.join(root,'build/book-source'+suffix+'.html'),html);
fs.writeFileSync(path.join(root,'build/render-check'+suffix+'.json'),JSON.stringify({mathCount,uniqueMath:mathCache.size,mathErrors,headingCount,blockCount,htmlBytes:Buffer.byteLength(html)},null,2));
fs.writeFileSync(path.join(root,'build/formulas'+suffix+'.json'),JSON.stringify(formulaRecords,null,2));
const approvedFiles=JSON.parse(read('baseline-manuscript.json')).files;
const inputHashes=Object.fromEntries(Object.keys(approvedFiles).map(p=>[p,require('node:crypto').createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')]));
fs.writeFileSync(path.join(root,'build/input-sha256'+suffix+'.json'),JSON.stringify(inputHashes,null,2));
if(english)fs.writeFileSync(path.join(root,'build/translation-render-inputs.json'),JSON.stringify(Object.fromEntries(parts.map(p=>sourcePath(p[0].startsWith('chapter-')?'chapters/'+input.chapters[Number(p[0].slice(8))-1]:(input.advanced_modules||[]).find(m=>m.id===p[0])?.file||({'rules':'写作约定与全书编排.md','supplement':'校订与证明补充.md','reading-routes':'延伸阅读与证明路线.md','references':'引用与配图来源.md'}[p[0]]))).map(p=>[p,require('node:crypto').createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),null,2));
console.log({mathCount,mathErrors:mathErrors.length,headingCount,htmlMB:(Buffer.byteLength(html)/1048576).toFixed(2)});
if(mathErrors.length)process.exitCode=1;
