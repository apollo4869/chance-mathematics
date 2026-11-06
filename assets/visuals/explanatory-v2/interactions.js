// Local explanatory controls. Simulation is optional and never used as proof.
document.querySelectorAll('[data-explain]').forEach(root=>{
 const en=root.lang==='en',id=root.dataset.explain;
 const press=(attr,b)=>root.querySelectorAll('['+attr+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 root.querySelectorAll('[data-rule]').forEach(b=>b.addEventListener('click',()=>{
  press('data-rule',b);const k=Number(b.dataset.rule),v=[1,3,2][k],r=[2,6,4][k];
  const words=en?['Take the left value, 1','Take the right value, 3','Average both endpoints: 2']:['先取左端的1','取这格结束时的3','两个端点先平均，取2'];
  const img=root.querySelector('[data-rule-scene]');img.src=`/assets/visuals/explanatory-v2/P01-${root.lang}-${k}.svg`;img.alt=words[k];
  root.querySelector('[data-rule-words]').textContent=words[k];root.querySelector('[data-rule-calc]').textContent=`${v} × 2 = ${r}`;
 }));
 root.querySelectorAll('[data-env]').forEach(b=>b.addEventListener('click',()=>{
  press('data-env',b);const key=b.dataset.env;
  const img=root.querySelector('[data-env-scene]');img.src=`/assets/visuals/explanatory-v2/P02-${root.lang}-${key}.svg`;
  const supports={mixed:'±1, ±2; ¼ each',one:'±1; ½ each',two:'±2; ½ each'};img.alt=supports[key];
  const messages=en?{mixed:'With ν hidden, one observation reveals the magnitude and changes the next prediction.',one:'R=1 is already known. Observing X₁ leaves the law of X₂ unchanged.',two:'R=2 is known. Seeing |X₁|=1 would be impossible; no such conditional probability is assigned.'}:{mixed:'环境未知时，一次观察能揭示幅度，改变下一次预测。',one:'已经知道R=1；看到X₁不再改变X₂的条件律。',two:'已知R=2，不可能看到|X₁|=1；不对此事件填写条件概率。'};
  root.querySelector('[data-env-law]').textContent=en?{mixed:'R=1 or 2, each with probability ½. Bowls show marginal laws, not independence.',one:'All three bowls now contain only −1 and +1, with probability ½ each.',two:'All three bowls now contain only −2 and +2, with probability ½ each.'}[key]:{mixed:'R=1或2各半；三个碗显示边缘律，不表示无条件独立。',one:'三个碗都只剩−1与+1，各以1/2出现。',two:'三个碗都只剩−2与+2，各以1/2出现。'}[key];
  root.querySelector('[data-prob-before]').textContent={mixed:'½',one:'1',two:'0'}[key];
  root.querySelector('[data-prob-after]').textContent=key==='two'?'—':'1';
  root.querySelector('[data-after-label]').textContent=key==='two'?(en?'This observation is impossible':'此观察不可能'):(en?'After seeing |X₁|=1':'看到 |X₁|=1 后');
  root.querySelector('[data-p02-output]').textContent=messages[key];
 }));
 root.querySelectorAll('[data-sample]').forEach(b=>b.addEventListener('click',()=>{
  press('data-sample',b);const mode=b.dataset.sample;
  root.querySelectorAll('.ex-sampling').forEach(x=>x.classList.toggle('is-active',mode!=='both'&&x.classList.contains(mode)));
  root.querySelector('[data-p03-output]').textContent=en?{both:'Two long intervals: 2 of 4 events, but 6 of 8 time units.',event:'Choose a start uniformly: 2/4=1/2 lead to a long gap.',time:'Choose time uniformly in [0,8): 6/8=3/4 lie in long gaps.'}[mode]:{both:'两段长间隔占2/4个事件，却占6/8单位时间。',event:'均匀选起点：长间隔占2/4=1/2。',time:'在[0,8)均匀选时刻：长间隔占6/8=3/4。'}[mode];
 }));
 if(id==='P05'){
  const input=root.querySelector('[data-epsilon]'),ns='http://www.w3.org/2000/svg';let uniforms=[];
  function render(){
   const eps=Number(input.value),pct=x=>(100*x).toFixed(0)+'%';
   root.querySelector('[data-eps-label]').textContent=pct(eps);
   root.querySelector('[data-density="old"]').setAttribute('stroke-width',String(24*(1-eps)));
   root.querySelector('[data-density="new"]').setAttribute('stroke-width',String(12*eps));
   root.querySelector('[data-mass-label="old"]').textContent=pct(1-eps);
   root.querySelector('[data-mass-label="new"]').textContent=(en?'mass ':'质量 ')+pct(eps);
   root.querySelector('[data-miss-prob]').textContent=(100*(1-eps)**5).toFixed(1)+'%';
   const group=root.querySelector('[data-samples]');group.replaceChildren();let hits=0;
   for(const u of uniforms){
    const isNew=u<eps;hits+=Number(isNew);const path=root.querySelector(`[data-geometry="${isNew?'new':'old'}"]`);
    const q=isNew?u/eps:(u-eps)/(1-eps),p=path.getPointAtLength(q*path.getTotalLength());
    const dot=document.createElementNS(ns,'circle');dot.setAttribute('cx',p.x);dot.setAttribute('cy',p.y);dot.setAttribute('r','5');dot.setAttribute('fill','#7257a4');dot.setAttribute('stroke','white');dot.setAttribute('stroke-width','1.8');group.append(dot);
   }
   if(uniforms.length)root.querySelector('[data-sample-result]').textContent=en?`${hits} of 5 points on the long branch. Moving ε reuses these uniforms; Draw makes a fresh sample.`:`5个点中${hits}个落在长枝；拖动ε复用这组均匀数，按钮可重新抽样。`;
  }
  input.addEventListener('input',render);
  root.querySelector('[data-resample]').addEventListener('click',()=>{
   uniforms=Array.from(crypto.getRandomValues(new Uint32Array(5)),x=>(x+.5)/4294967296);render();
   root.querySelector('[data-resample]').textContent=en?'Draw 5 again':'重新抽取5个点';
  });
  render();
 }
});

// Volume-V batch: finite models and schematic density, never simulations as proof.
document.querySelectorAll('[data-explain]').forEach(root=>{
 const en=root.lang==='en',id=root.dataset.explain,base='/assets/visuals/explanatory-v2/';
 const press=(attr,b)=>root.querySelectorAll('['+attr+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 if(id==='V31'){
  let mode='jump',t='3';function draw(){const img=root.querySelector('[data-bracket-scene]');img.src=base+`V31-${root.lang}-${mode}-${t}.svg`;img.alt=mode==='continuous'?'[B]=⟨B⟩=t':`[M]=${Number(t)<2.2?1:2}, ⟨M⟩=${t}`;root.querySelector('[data-bracket-reading]').textContent=mode==='continuous'?(en?`At t=${t}, both Brownian brackets read ${t}. This is a proved identity, not a sampled path.`:`t=${t}时，Brownian的两种括号都等于${t}。这是已证身份，不是模拟。`):(en?`The arrivals at 0.6 and 2.2 give ${Number(t)<2.2?1:2} observed jumps by t=${t}; the predictable clock reads ${t}.`:`到达时刻为0.6与2.2；t=${t}前已发生${Number(t)<2.2?1:2}跳，可预测时钟为${t}。`);}
  for(const attr of ['data-bracket-mode','data-bracket-time'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr.endsWith('mode'))mode=b.getAttribute(attr);else t=b.getAttribute(attr);draw();}));
 }
 root.querySelectorAll('[data-weight]').forEach(b=>b.addEventListener('click',()=>{press('data-weight',b);const key=b.dataset.weight,img=root.querySelector('[data-weight-scene]');img.src=base+`V33-${root.lang}-${key}.svg`;const theta={25:'1/4',50:'1/2',75:'3/4'}[key];img.alt='P weights 1/4 each; Q uses theta='+theta;root.querySelector('[data-weight-reading]').textContent=en?`Under Q, each step is up with probability ${theta}. The same four records remain, with total probability 1.`:`Q下每一步向上概率为${theta}；四条记录不变，总概率仍为1。`;}));
 root.querySelectorAll('[data-jump-stage]').forEach(b=>b.addEventListener('click',()=>{press('data-jump-stage',b);const k=Number(b.dataset.jumpStage),img=root.querySelector('[data-jump-scene]');img.src=base+`V34-${root.lang}-${k}.svg`;img.alt='Cubic jump: selected increment '+[6,18,26][k];root.querySelector('[data-jump-reading]').textContent=en?['The linear prediction is 6; the full increment is 26. Missing: 20.','Adding the quadratic term gives 18. A finite residual 8 is still missing.','Full increment 26 = 6+12+8. The Itô jump correction after the linear term is 20.'][k]:['一阶只给6，完整增量为26；还缺20。','加上二阶得到18，有限跳跃还留下8。','完整增量26=6+12+8；扣除一阶后的Itô跳跃修正是20。'][k];}));
 root.querySelectorAll('[data-occupation]').forEach(b=>b.addEventListener('click',()=>{press('data-occupation',b);const key=b.dataset.occupation;for(const part of ['band','average'])root.querySelector('[data-occupation-'+part+']').src=base+`V37-${root.lang}-${key}-${part}.svg`;const messages=en?{half:'Band mass 3/4 ÷ width 1 = average density 3/4.',quarter:'Band mass 7/16 ÷ width 1/2 = average density 7/8.',eighth:'Band mass 15/64 ÷ width 1/4 = average density 15/16.',point:'A point has zero mass and zero width. 0/0 does not define the limiting density.'}:{half:'窄带总量3/4 ÷ 带宽1 = 平均密度3/4。',quarter:'窄带总量7/16 ÷ 带宽1/2 = 平均密度7/8。',eighth:'窄带总量15/64 ÷ 带宽1/4 = 平均密度15/16。',point:'单点总量0、宽度0。不能用0/0定义极限密度。'};root.querySelector('[data-occupation-reading]').textContent=messages[key];}));
});
document.querySelectorAll('[data-explain]').forEach(root=>{
 const en=root.lang==='en',base='/assets/visuals/explanatory-v2/';
 const press=(attr,b)=>root.querySelectorAll('['+attr+']').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 root.querySelectorAll('[data-occupation]').forEach(b=>b.addEventListener('click',()=>{for(const part of ['band','average'])root.querySelector('[data-mobile-occupation-'+part+']')?.setAttribute('srcset',base+`V37-${root.lang}-mobile-${b.dataset.occupation}-${part}.svg`);}));
 root.querySelectorAll('[data-rule-model]').forEach(b=>b.addEventListener('click',()=>{press('data-rule-model',b);const m=b.dataset.ruleModel;root.querySelector('[data-rule-model-scene]').src=base+`V35-${root.lang}-${m}.svg`;root.querySelector('[data-rule-equation]').textContent=m==='many'?(en?'x′=2√|x|, starting at 0':'x′=2√|x|，从0出发'):(en?'x′=x², starting at 1':'x′=x²，从1出发');root.querySelector('[data-rule-model-reading]').textContent=m==='many'?(en?'The same rule permits departure at 0, at 1, or never. All three solutions exist globally.':'同一规则允许立即出发、等到1再出发，或永远不离开；三条解都全局存在。'):(en?'A unique solution reads 1,2,4,8 at times 0,1/2,3/4,7/8. Its maximal lifetime is 1.':'唯一解在0、1/2、3/4、7/8时读到1、2、4、8，最大寿命却只有1。');}));
 root.querySelectorAll('[data-boundary]').forEach(b=>b.addEventListener('click',()=>{press('data-boundary',b);const k=b.dataset.boundary;root.querySelector('[data-boundary-scene]').src=base+`V36-${root.lang}-${k}.svg`;const finite={regular:[1,1],exit:[1,0],entrance:[0,1],natural:[0,0]}[k];root.querySelector('[data-boundary-tests]').textContent='Σ '+(finite[0]?'< ∞':'= ∞')+'; N '+(finite[1]?'< ∞':'= ∞');root.querySelector('[data-boundary-model]').textContent=en?{regular:'Regular: 0 for Brownian motion in (0,1)',exit:'Exit: 0 for dZ=2√Z dW',entrance:'Entrance: 0 for a three-dimensional Bessel radius',natural:'Natural: 0 for dX=X dW'}[k]:{regular:'正则：Brownian在(0,1)的0端',exit:'出口：dZ=2√Z dW的0端',entrance:'入口：三维Bessel半径的0端',natural:'自然：dX=X dW的0端'}[k];root.querySelector('[data-boundary-reading]').textContent=en?{regular:'Both directions are admissible, but the extension still needs a boundary rule.',exit:'The boundary can be reached, but it is not an instantaneous entrance into the interior.',entrance:'Unreachable from positive radii, yet a valid starting boundary for immediate entry.',natural:'Neither accessible from inside nor an immediate entrance. An absorbing zero process is not an entrance.'}[k]:{regular:'两个方向都允许，但延拓仍须另选边界规则。',exit:'内部可达，却不能从该端点即时进入内部。',entrance:'内部到不了，却可以从0即时进入正半轴。',natural:'内部不可达，也没有即时入口；吸收零过程不等于进入内部。'}[k];}));
 if(root.dataset.explain==='V38'){
  let ix=1,c=1;const frac=v=>{let n=Math.round(v*16),d=16;const gcd=(a,b)=>b?gcd(b,a%b):a;const g=gcd(n,d);n/=g;d/=g;return d===1?String(n):n+'/'+d;};
  function draw(){const x=[.25,.5,.75][ix],r=c*x*(1-x);root.querySelector('[data-account-scene]').src=base+`V38-${root.lang}-${ix}-${c}.svg`;root.querySelector('[data-account-reading]').textContent=en?`Boundary mean ${frac(x)} + running mean ${frac(r)} = u(x) ${frac(x+r)}`:`边界平均 ${frac(x)} ＋ 沿途平均 ${frac(r)} ＝ u(x) ${frac(x+r)}`;root.querySelector('[data-account-source]').textContent=`−½u″=${c}; u(0)=0, u(1)=1`;}
  for(const attr of ['data-account-x','data-account-c'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr.endsWith('-x'))ix=Number(b.getAttribute(attr));else c=Number(b.getAttribute(attr));draw();}));
 }
 if(root.dataset.explain==='V40'){
  let ti=2,ai=1;function draw(){const t=[.25,.5,1][ti];root.querySelector('[data-circle-scene]').src=base+`V40-${root.lang}-${ti}-${ai}.svg`;root.querySelector('[data-circle-reading]').textContent=en?`Correct radius: 1. Without the term: exp(${t}/2)≈${Math.exp(t/2).toFixed(3)}. Same angular reading, different process.`:`正确半径1；删项后的半径 exp(${t}/2)≈${Math.exp(t/2).toFixed(3)}。角度读数相同，过程已经不同。`;}
  for(const attr of ['data-circle-t','data-circle-angle'])root.querySelectorAll('['+attr+']').forEach(b=>b.addEventListener('click',()=>{press(attr,b);if(attr.endsWith('-t'))ti=Number(b.getAttribute(attr));else ai=Number(b.getAttribute(attr));draw();}));
 }
});
