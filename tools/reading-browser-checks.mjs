// Invoked only inside cua_repl with the supported bound Tab API.
// Filesystem I/O records evidence; all UI actions use the supplied browser tab.
import fs from 'node:fs/promises';

export const readPage=()=>({url:location.href,title:document.title,lang:document.documentElement.lang,mode:document.body.dataset.readingMode,heading:document.querySelector('.book-section')?.querySelector('h1,h2')?.textContent,units:document.querySelectorAll('.book-section>.reading-unit').length,formulas:document.querySelectorAll('.formula').length,figures:[...document.querySelectorAll('figure[id^="visual-"]')].map(e=>({id:e.id,unit:e.closest('.reading-unit')?.getAttribute('data-reader-title'),width:e.getBoundingClientRect().width})),brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),pendingImages:[...document.images].filter(i=>!i.complete).map(i=>i.getAttribute('src')),publicationOrder:[...document.querySelectorAll('.book-section,details.chapter-edition')].map(e=>e.className),metadata:[...document.querySelectorAll('details.chapter-edition')].map(e=>({open:e.open,summary:e.querySelector('summary')?.textContent})),readingStatus:document.querySelector('#reader-status')?.textContent,mathErrors:document.querySelectorAll('mjx-merror,[data-mjx-error]').length,viewport:{w:window.innerWidth,h:window.innerHeight},pageWidth:document.documentElement.scrollWidth});
export const readMode=()=>({mode:document.body.dataset.readingMode,selected:document.querySelector('#reader-section').value,status:document.querySelector('#reader-status').textContent,pressed:[...document.querySelectorAll('#reader-controls button[data-reading-mode]')].map(e=>({mode:e.getAttribute('data-reading-mode'),pressed:e.getAttribute('aria-pressed')})),visibleUnits:[...document.querySelectorAll('.book-section>.reading-unit')].filter(e=>!e.hidden).length});
const read=async(p)=>JSON.parse(await fs.readFile(p,'utf8'));
const save=async(p,x)=>fs.writeFile(p,JSON.stringify(x,null,2)+'\n');

export async function mobileBatch(tab,report,limit=12){
 const pages=(await read(report+'/integration.json')).chapters.map(r=>r.path),file=report+'/local-browser-mobile-final.json',mfile=report+'/reading-mode-browser-final.json';
 const results=await read(file),modes=await read(mfile),start=results.length;
 await fs.mkdir(report+'/screenshots/mobile-final',{recursive:true});
 for(const page of pages.slice(start,start+limit)){
  await tab.goto('http://127.0.0.1:8899/'+page);await tab.playwright.locator('.book-section').waitFor({state:'visible',timeoutMs:15000});
  await tab.playwright.locator('#reader-section').selectOption('2');await tab.playwright.locator('#reader-section').press('Escape');await tab.playwright.locator('#reader-status').filter({hasText:/^3 \//}).waitFor({state:'visible',timeoutMs:3000});
  await tab.playwright.locator('#reader-controls button[data-reading-mode="section"]').press('Space');await tab.playwright.locator('#reader-controls button[data-reading-mode="section"][aria-pressed="true"]').waitFor({state:'visible',timeoutMs:3000});const section=await tab.playwright.evaluate(readMode);
  await tab.playwright.locator('#reader-next-top').press('Space');await tab.playwright.locator('#reader-status').filter({hasText:/^4 \//}).waitFor({state:'visible',timeoutMs:3000});const next=await tab.playwright.evaluate(readMode);
  await tab.playwright.locator('#reader-previous-top').press('Space');await tab.playwright.locator('#reader-status').filter({hasText:/^3 \//}).waitFor({state:'visible',timeoutMs:3000});const previous=await tab.playwright.evaluate(readMode);
  await tab.playwright.locator('#reader-controls button[data-reading-mode="chapter"]').press('Space');await tab.playwright.locator('#reader-controls button[data-reading-mode="chapter"][aria-pressed="true"]').waitFor({state:'visible',timeoutMs:3000});const chapter=await tab.playwright.evaluate(readMode);
  modes.push({page,inputMethod:'keyboard activation (Space) after a real selection; actual pointer/touch remain separately sampled',section,next,previous,chapter,pass:section.selected==='2'&&next.selected==='3'&&previous.selected==='2'&&chapter.selected==='2'&&section.mode==='section'&&chapter.mode==='chapter'});
  results.push({...await tab.playwright.evaluate(readPage),requestedPage:page,layout:'mobile-browser-390px'});
  await fs.writeFile(report+'/screenshots/mobile-final/'+page.replaceAll('/','_')+'.jpg',await tab.screenshot({fullPage:false}));
  await save(file,results);await save(mfile,modes);
 }
 return {pages:results.length,modeFailures:modes.filter(r=>!r.pass).map(r=>r.page),overflow:results.filter(r=>r.pageWidth>r.viewport.w).map(r=>({page:r.requestedPage,width:r.pageWidth})),broken:results.filter(r=>r.brokenImages.length).map(r=>r.requestedPage)};
}

export async function desktopBatch(tab,report,limit=24){
 const pages=(await read(report+'/integration.json')).chapters.map(r=>r.path),file=report+'/local-browser-desktop-final.json',results=await read(file),start=results.length;
 for(const page of pages.slice(start,start+limit)){
  await tab.goto('http://127.0.0.1:8899/'+page);await tab.playwright.locator('.book-section').waitFor({state:'visible',timeoutMs:15000});
  await tab.playwright.locator('#reader-controls button[data-reading-mode="chapter"]').press('Space');
  await tab.playwright.locator('#reader-controls button[data-reading-mode="chapter"][aria-pressed="true"]').waitFor({state:'visible',timeoutMs:3000});
  results.push({...await tab.playwright.evaluate(readPage),requestedPage:page,layout:'desktop-browser'});await save(file,results);
 }
 return {pages:results.length,broken:results.filter(r=>r.brokenImages.length).map(r=>r.requestedPage),overflow:results.filter(r=>r.pageWidth>r.viewport.w).map(r=>r.requestedPage),wrongMetadata:results.filter(r=>r.publicationOrder[0]!=='book-section'||r.metadata.some(m=>m.open)).map(r=>r.requestedPage)};
}

export const readFigure=(e)=>({id:e.id,title:e.querySelector('h3')?.textContent,rect:e.getBoundingClientRect(),images:[...e.querySelectorAll('img')].map(i=>({src:i.currentSrc||i.src,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight,complete:i.complete,rect:i.getBoundingClientRect()})).filter(i=>i.rect.width>0&&i.rect.height>0),buttons:[...e.querySelectorAll('button')].map(b=>({text:b.textContent,pressed:b.getAttribute('aria-pressed'),disabled:b.disabled})),outputs:[...e.querySelectorAll('output,[aria-live]')].map(o=>o.textContent),unit:e.closest('.reading-unit')?.getAttribute('data-reader-title')});

export async function figuresBatch(tab,report,layout,limit=8){
 const rows=(await read(report+'/accepted-figures.json')).figures,file=report+'/figures-browser-'+layout+'.json',results=await read(file),start=results.length;
 await fs.mkdir(report+'/screenshots/figures-'+layout,{recursive:true});
 for(const row of rows.slice(start,start+limit)){
  const page=(row.lang==='en'?'en/':'')+'chapters/'+row.slug+'.html';
  await tab.goto('http://127.0.0.1:8899/'+page+'#visual-'+row.id);await tab.playwright.locator('#visual-'+row.id).waitFor({state:'visible',timeoutMs:15000});
  await tab.playwright.locator('#reader-controls button[data-reading-mode="section"]').press('Space');
  await tab.playwright.locator('#reader-controls button[data-reading-mode="section"][aria-pressed="true"]').waitFor({state:'visible',timeoutMs:3000});
  const fig=tab.playwright.locator('#visual-'+row.id),before=await fig.evaluate(readFigure);let interaction='static figure, no interactive controls',changed=null;
  const radio=fig.locator('button[aria-pressed="false"]:not([disabled])',{});
  if(await radio.count()){
   await radio.first().press('Space');interaction='keyboard activated one previously unselected comparison';
   const after=await fig.evaluate(readFigure);changed=JSON.stringify(before.buttons)!==JSON.stringify(after.buttons)||JSON.stringify(before.outputs)!==JSON.stringify(after.outputs)||JSON.stringify(before.images.map(i=>i.src))!==JSON.stringify(after.images.map(i=>i.src));
  }else if(await fig.locator('input[type="range"]',{}).count()){
   await fig.locator('input[type="range"]',{}).first().press('ArrowRight');interaction='keyboard moved one range control';
   const after=await fig.evaluate(readFigure);changed=JSON.stringify(before.outputs)!==JSON.stringify(after.outputs)||JSON.stringify(before.images.map(i=>i.src))!==JSON.stringify(after.images.map(i=>i.src));
  }
  const screenshot='screenshots/figures-'+layout+'/'+row.id+'.'+row.lang+'.jpg';
  // Refresh the rendered accessibility state before capturing. The screenshot
  // must not be a stale paint immediately following the keyboard event.
  await tab.playwright.domSnapshot();
  const longScene=['V48','V49','V51','V52','V53','V54','V55','V56','V57','V58'].includes(row.id);
  const fullPage=false;
  await fs.writeFile(report+'/'+screenshot,await tab.screenshot({fullPage}));
  let scrollScreenshot=null;
  if(longScene){
   await fig.locator('button[aria-pressed="true"]',{}).first().press('PageDown');await tab.playwright.domSnapshot();
   scrollScreenshot=screenshot.replace('.jpg','-scroll.jpg');await fs.writeFile(report+'/'+scrollScreenshot,await tab.screenshot({fullPage:false}));
  }
  const after=await fig.evaluate(readFigure);
  results.push({id:row.id,lang:row.lang,page,section:row.section,layout,before,after,interaction,changed,screenshot,scrollScreenshot,actualBrowserScreenshot:true,renderedSnapshotRefreshedBeforeCapture:true,fullPage,fullStateSpaceTested:false});await save(file,results);
 }
 return {figures:results.length,interactions:results.filter(r=>r.changed===true).length,noChange:results.filter(r=>r.changed===false).map(r=>r.id+'.'+r.lang),pendingImages:results.filter(r=>r.after.images.some(i=>!i.complete)).map(r=>r.id+'.'+r.lang),badAspect:results.filter(r=>r.after.images.some(i=>i.naturalWidth>0&&Math.abs((i.rect.width/i.rect.height)/(i.naturalWidth/i.naturalHeight)-1)>.04)).map(r=>r.id+'.'+r.lang)};
}

export const readStaticPage=()=>({url:location.href,title:document.title,lang:document.documentElement.lang,headings:[...document.querySelectorAll('h1,h2,h3,h4')].slice(0,4).map(e=>e.textContent),formulas:document.querySelectorAll('.formula').length,images:document.images.length,brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),pendingImages:[...document.images].filter(i=>!i.complete).map(i=>i.getAttribute('src')),mathErrors:document.querySelectorAll('mjx-merror,[data-mjx-error]').length,firstText:document.body.innerText.slice(0,400),viewport:{w:window.innerWidth,h:window.innerHeight}});
export async function staticBatch(tab,report,limit=24){
 const pages=await read(report+'/static-reading-targets.json'),file=report+'/static-browser-pages.json',results=await read(file),start=results.length;
 for(const page of pages.slice(start,start+limit)){
  await tab.goto('http://127.0.0.1:8899/'+page);await tab.playwright.waitForLoadState({state:'load',timeoutMs:15000});
  results.push({...await tab.playwright.evaluate(readStaticPage),requestedPage:page,nativePrintOrPdf:false});await save(file,results);
 }
 return {pages:results.length,broken:results.filter(r=>r.brokenImages.length).map(r=>r.requestedPage),mathErrors:results.filter(r=>r.mathErrors).map(r=>r.requestedPage)};
}
