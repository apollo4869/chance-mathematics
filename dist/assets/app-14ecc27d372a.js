const BOOK_ROOT=document.body.dataset.bookRoot||'./';
(function(){
'use strict';
const $=s=>document.querySelector(s),all=s=>[...document.querySelectorAll(s)];
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const storage={get(k){try{return localStorage.getItem('chance-v2-'+k)}catch{return null}},set(k,v){try{localStorage.setItem('chance-v2-'+k,v)}catch{}}};
let font=Number(storage.get('font'))||19;document.documentElement.style.setProperty('--body-size',font+'px');
if(storage.get('theme')==='dark')document.body.classList.add('dark');
function themeLabel(){$('#theme').textContent=document.body.classList.contains('dark')?'Light mode':'Dark mode';}themeLabel();
$('#theme').onclick=()=>{document.body.classList.toggle('dark');storage.set('theme',document.body.classList.contains('dark')?'dark':'light');themeLabel();};
$('#font-up').onclick=()=>{font=Math.min(26,font+1);document.documentElement.style.setProperty('--body-size',font+'px');storage.set('font',font)};
$('#font-down').onclick=()=>{font=Math.max(15,font-1);document.documentElement.style.setProperty('--body-size',font+'px');storage.set('font',font)};
$('#tex-toggle').onclick=()=>{document.body.classList.toggle('show-tex');$('#tex-toggle').setAttribute('aria-pressed',document.body.classList.contains('show-tex'))};
$('#menu').onclick=()=>{document.body.classList.toggle('menu-open');$('#menu').setAttribute('aria-expanded',document.body.classList.contains('menu-open'));};
all('aside a').forEach(a=>a.onclick=()=>{document.body.classList.remove('menu-open');$('#menu').setAttribute('aria-expanded','false')});
$('#print').onclick=()=>window.print();$('#back-top').onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
const dialog=$('#search-dialog');$('#search-toggle').onclick=()=>{dialog.showModal();$('#search-input').focus()};
let searchTimer;
$('#search-input').addEventListener('input',()=>{clearTimeout(searchTimer);searchTimer=setTimeout(searchNow,160)});
function searchNow(){
const q=$('#search-input').value.trim().toLocaleLowerCase();
if(!q){$('#search-count').textContent='';$('#search-results').innerHTML='';return;}
const results=BOOK_SEARCH.filter(x=>x.text.toLocaleLowerCase().includes(q));
$('#search-count').textContent=`Found ${results.length} matches${results.length>60?', showing the first 60 matches':''}`;
$('#search-results').innerHTML=results.slice(0,60).map(r=>{const p=r.text.toLocaleLowerCase().indexOf(q);const snippet=r.text.slice(Math.max(0,p-35),p+q.length+80);return `<a href="${BOOK_ROOT}${BOOK_PAGES[r.section]}#${r.id}"><small>${esc(BOOK_SECTION_TITLES[r.section]||r.section)}</small>${esc(snippet)}</a>`}).join('');
all('#search-results a').forEach(a=>a.onclick=()=>dialog.close());
}
let reading=null;try{reading=JSON.parse(storage.get('reading')||'null')}catch{};const resume=$('#resume');if(resume&&reading&&reading.path&&reading.anchor){resume.hidden=false;resume.onclick=()=>{location.href=reading.path+'#'+reading.anchor}};
const heads=all('.book-section h1,.book-section h2,.book-section h3');let scrollTimer;
window.addEventListener('scroll',()=>{
const max=document.documentElement.scrollHeight-innerHeight;$('#progress').style.width=(max>0?100*scrollY/max:0)+'%';
clearTimeout(scrollTimer);scrollTimer=setTimeout(()=>{
let cur=null;for(const h of heads){if(h.closest("[hidden]"))continue;if(h.getBoundingClientRect().top<(document.getElementById("reader-controls")?.getBoundingClientRect().bottom||132)+20)cur=h;else break;}
if(cur){storage.set('reading',JSON.stringify({path:location.pathname,anchor:cur.id}));all('.toc-sub.active').forEach(x=>x.classList.remove('active'));const a=document.querySelector(`.toc-sub[href$="#${cur.id}"]`);if(a){a.classList.add('active');const group=a.closest('details');if(group)group.open=true;a.scrollIntoView({block:'nearest'});}}
},140);
},{passive:true});

function buttonGroup(values,selected,label){return `<div class="buttons" role="group" aria-label="${label}">${values.map(([v,t])=>`<button type="button" data-value="${v}" aria-pressed="${Number(v)===selected}">${t}</button>`).join('')}</div>`;}
function selectButtons(el,value){el.querySelectorAll('button[data-value]').forEach(b=>b.setAttribute('aria-pressed',Number(b.dataset.value)===value));}
function drawDependence(el,i){
const m=BookMath.dependence(i);selectButtons(el,i);
el.querySelector('.model-grid').innerHTML=m.p.map((p,j)=>`<div class="model-cell">${['AA','AB','BA','BB'][j]}<b>${100*p}%</b><small>${j===3?'B wins':'A wins'}</small></div>`).join('');
el.querySelector('output').innerHTML=`${m.name}: A ultimately wins ${(100*m.win).toFixed(0)}%; fair share ${m.stake} gold coins. `;
el.dataset.selected=String(i);el.dataset.win=String(m.win);
}
const dep=$('[data-widget=dependence]');
if(dep)dep.id='experiment-dependence';
if(dep){dep.innerHTML='<h4>A — probability of ultimately winning the prize</h4>'+buttonGroup([[0,'Independent'],[1,'Perfect positive correlation'],[2,'Perfect negative correlation']],0,'Dependence structure')+'<div class="model-grid"></div><p class="stat"><output aria-live="polite"></output></p><p class="caption">The three models have identical marginal distributions in both rounds; the joint distribution changes, so the eventual winning probability and fair share change accordingly. A wins for AA, AB, BA . </p>';dep.querySelectorAll('button').forEach(b=>b.onclick=()=>drawDependence(dep,Number(b.dataset.value)));drawDependence(dep,0);}
function drawSpike(el,n){
const v=BookMath.spike(n);selectButtons(el,n);let ticks='';
for(const x of [0,.25,.5,.75,1])ticks+=`<path d="M${65+600*x} 265v5" stroke="currentColor"/><text x="${65+600*x}" y="291" text-anchor="middle">${x}</text>`;
for(const y of [0,8,16,24,32])ticks+=`<path d="M65 ${265-7*y}H665" stroke="currentColor" opacity=".12"/><text x="53" y="${269-7*y}" text-anchor="end">${y}</text>`;
el.querySelector('svg').innerHTML=`<path d="M65 22V265H680" stroke="currentColor" fill="none"/>${ticks}<rect class="spike-rect" x="65" y="${265-v.svgHeight}" width="${v.svgWidth}" height="${v.svgHeight}" fill="#168782" fill-opacity=".25" stroke="#168782" stroke-width="2"/><text x="${Math.min(645,75+v.svgWidth)}" y="${Math.max(19,259-v.svgHeight)}" fill="currentColor">height ${n}</text><text x="690" y="290">x</text><text x="20" y="20">fₙ</text>`;
el.querySelector('output').textContent=`n = ${n}　｜　width 1/${n} = ${(1/n).toFixed(5)}　｜　height ${n}　｜　integral 1`;
el.dataset.n=String(n);el.dataset.area=String(v.svgWidth*v.svgHeight);
}
const spike=$('[data-widget=spike]');
if(spike)spike.id='experiment-spike';
if(spike){spike.innerHTML='<h4>Shrinking spike experiment</h4><svg viewBox="0 0 720 310" role="img" aria-label="Spike on fixed horizontal and vertical axes, width 1 divided by n, height n "></svg>'+buttonGroup([2,4,8,16,32].map(n=>[n,'n = '+n]),8,'Spike parameter')+'<p class="stat"><output aria-live="polite"></output></p><p class="caption">The horizontal axis is fixed at [0,1], the vertical axis is fixed at [0,32]. All selections use the same scale, the displayed rectangle always has the same area. Including or excluding the endpoints does not affect the integral. </p>';spike.querySelectorAll('button').forEach(b=>b.onclick=()=>drawSpike(spike,Number(b.dataset.value)));drawSpike(spike,8);}
const counts=[16,32,64,128,256];
function drawWalk(el){
const n=counts[Number(el.querySelector('input[type=range]').value)],values=BookMath.walk(n),linear=el.querySelector('input[type=checkbox]').checked;
const max=Math.max(3,Math.ceil(Math.max(...values.map(Math.abs))));
const x=i=>60+620*i/n,y=v=>165-v*130/max;
let d=`M${x(0)},${y(values[0])}`;
for(let i=1;i<=n;i++)d+=linear?`L${x(i)},${y(values[i])}`:`H${x(i)}V${y(values[i])}`;
let grid='';for(let i=-max;i<=max;i++)grid+=`<path d="M60 ${y(i)}H680" stroke="currentColor" opacity="${i===0?.3:.1}"/><text x="47" y="${y(i)+4}" text-anchor="end">${i}</text>`;
for(let t of [0,.25,.5,.75,1])grid+=`<text x="${60+620*t}" y="318" text-anchor="middle">${t}</text>`;
el.querySelector('svg').innerHTML=grid+`<path class="walk-path" d="${d}" fill="none" stroke="#168782" stroke-width="2"/><circle cx="680" cy="${y(values[n])}" r="3" fill="#168782"/>`;
el.querySelector('output').textContent=`${n} steps; time interval 1/${n}; step length 1/√${n}; terminal value ${values[n].toFixed(4)}. ${linear?'Linearly interpolated path':'Step path'}`;
el.dataset.steps=String(n);el.dataset.endpoint=String(values[n]);
}
const walk=$('[data-widget=walk]');
if(walk)walk.id='experiment-walk';
if(walk){walk.innerHTML='<h4>Scaling experiment for discrete random walks</h4><svg viewBox="0 0 720 340" role="img" aria-label="Rescaled symmetric random walk"></svg><label>Number of time steps <input aria-label="Number of time steps" type="range" min="0" max="4" step="1" value="2"></label><div class="range-labels"><span>16</span><span>32</span><span>64</span><span>128</span><span>256</span></div><label class="caption"><input type="checkbox"> Show linear interpolation (in the text, Wₙ is a step process)</label><p class="stat"><output aria-live="polite"></output></p><p class="caption">Fixed seed 918273, the same pseudorandom increment sequence as in the original manuscript. Different values of n use prefixes of different lengths, these are not successive approximations of one and the same path; Finite simulations cannot prove the Donsker theorem. </p>';walk.querySelectorAll('input').forEach(i=>i.addEventListener('input',()=>drawWalk(walk)));drawWalk(walk);}
window.BookUI={drawDependence,drawSpike,drawWalk};
})();
