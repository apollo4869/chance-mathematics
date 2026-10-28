(() => {
  const $=id=>document.getElementById(id),form=$('filters');let data;
  const day=n=>new Date(Date.now()-n*86400000).toISOString().slice(0,10);
  form.elements.from.value=day(29);form.elements.to.value=day(0);form.elements.from.min=day(89);form.elements.to.max=day(0);
  const n=value=>Number(value||0).toLocaleString('zh-CN',{maximumFractionDigits:1});
  const percent=(a,b)=>b?(100*a/b).toFixed(1)+'%':'暂无数据';
  const sec=ms=>Number(ms||0)>=60000?(ms/60000).toFixed(1)+' 分钟':Math.round(Number(ms||0)/1000)+' 秒';
  function table(id,headers,rows){const target=$(id);target.replaceChildren();target.classList.toggle('empty',!rows.length);if(!rows.length){target.textContent='暂无数据';return;}
    const t=document.createElement('table'),head=t.createTHead().insertRow();headers.forEach(text=>{const th=document.createElement('th');th.textContent=text;head.append(th);});const body=t.createTBody();rows.forEach(row=>{const tr=body.insertRow();row.forEach(text=>{const td=tr.insertCell();td.textContent=String(text);});});target.append(t);}
  function chart(){const rows=data?.[$('period').value]||[],target=$('trend');target.replaceChildren();target.classList.toggle('empty',!rows.length);if(!rows.length){target.textContent='暂无数据';return;}
    const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 1000 230');svg.setAttribute('role','img');svg.setAttribute('aria-label','章节打开与有效阅读趋势');
    const maximum=Math.max(1,...rows.map(r=>r.opens)),width=900/rows.length;const node=(name,attrs,text)=>{const e=document.createElementNS(ns,name);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(text!==undefined)e.textContent=text;svg.append(e);return e;};
    [0,.5,1].forEach(t=>{const y=190-160*t;node('line',{x1:50,x2:950,y1:y,y2:y,stroke:'#e2e9e3'});node('text',{x:40,y:y+4,'text-anchor':'end',fill:'#6c7978','font-size':11},n(maximum*t));});
    rows.forEach((r,i)=>{const x=50+i*width;const total=node('rect',{x:x+width*.12,y:190-160*r.opens/maximum,width:Math.max(1,width*.32),height:160*r.opens/maximum,fill:'#157b77'});const title=document.createElementNS(ns,'title');title.textContent=r.period+'：打开 '+r.opens+'，有效 '+r.effective;total.append(title);node('rect',{x:x+width*.48,y:190-160*r.effective/maximum,width:Math.max(1,width*.32),height:160*r.effective/maximum,fill:'#ad8846'});
      if(i%Math.max(1,Math.ceil(rows.length/9))===0||i===rows.length-1)node('text',{x:x+width/2,y:214,'text-anchor':'middle',fill:'#6c7978','font-size':11},r.period);});target.append(svg);
  }
  function render(){const t=data.totals,any=t.opens>0;$('opens').textContent=any?n(t.opens):'暂无数据';$('effective').textContent=any?n(t.effective):'暂无数据';$('effective-rate').textContent=any?'占章节访问 '+percent(t.effective,t.opens):'暂无数据';$('readers').textContent=any?n(t.visitor_days):'暂无数据';$('active').textContent=any?sec(t.avg_active_ms):'暂无数据';$('active-total').textContent=any?'累计活跃 '+sec(t.active_ms)+' · 排除后台':'排除后台及超过 2 分钟无操作的时间';chart();
    table('chapters',['章节','打开','有效 / 占比','平均活跃','50% / 75% / 90%','下一章点击'],data.chapters.map(r=>['第 '+r.chapter+' 章',n(r.opens),n(r.effective)+' / '+percent(r.effective,r.opens),sec(r.avg_active_ms),[r.depth50,r.depth75,r.depth90].map(n).join(' / '),n(r.next_clicks)]));
    table('depth',['最高正文位置','访问次数','占比'],data.depth.map(r=>[r.bucket,n(r.visits),percent(r.visits,t.opens)]));
    table('transitions',['来源 → 目标','目标章打开','来源访问转化率'],data.transitions.map(r=>[r.from_chapter+' → '+r.to_chapter,n(r.opens),percent(r.opens,data.chapters.find(c=>c.chapter===r.from_chapter)?.opens)]));
    const sourceNames={direct:'直接访问',external:'外站推荐',internal:'站内继续',other:'其他 / 未登记'};
    table('sources',['渠道代码','打开','有效','有效率'],data.sources.map(r=>[sourceNames[r.source]||r.source,n(r.opens),n(r.effective),percent(r.effective,r.opens)]));
    const interests={history:'历史与思想',proofs:'数学证明',examples:'更多例子',applications:'应用联系'};table('feedback',['兴趣','匿名反馈次数'],data.feedback.map(r=>[interests[r.interest]||r.interest,n(r.votes)]));
    $('updated').textContent='更新于 '+data.updatedAt.replace('T',' ').slice(0,19)+' UTC · 当前日期范围内'+(any?'有阅读事件':'尚无阅读事件');
  }
  async function load(){const query=new URLSearchParams(new FormData(form));$('csv').href='/api/admin/analytics?'+query+'&format=csv&table='+$('export-table').value;$('status').textContent='正在读取…';$('status').classList.remove('error');
    try{const r=await fetch('/api/admin/analytics?'+query,{credentials:'same-origin',cache:'no-store'}),body=await r.json();if(!r.ok)throw Error(r.status===401?'登录已失效，请重新登录。':body.error);data=body;render();$('status').textContent='已更新 · '+body.range.from+' 至 '+body.range.to+' · UTC';}catch(e){$('status').textContent=e.message;$('status').classList.add('error');}}
  form.addEventListener('submit',e=>{e.preventDefault();load();});$('week').onclick=()=>{form.elements.from.value=day(6);load();};$('month').onclick=()=>{form.elements.from.value=day(29);load();};$('period').onchange=chart;$('export-table').onchange=()=>{const query=new URLSearchParams(new FormData(form));$('csv').href='/api/admin/analytics?'+query+'&format=csv&table='+$('export-table').value;};load();
})();
