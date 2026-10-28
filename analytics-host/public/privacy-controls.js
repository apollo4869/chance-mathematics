(() => {
  const button=document.querySelector('[data-analytics-optout]');if(!button)return;
  const en=document.documentElement.lang==='en';
  function show(){let off=false;try{off=JSON.parse(localStorage.getItem('chance-analytics-opt-out'))===true;}catch{}
    button.textContent=off?(en?'Reading statistics disabled on this browser · Enable':'此浏览器已停用阅读统计 · 点击启用'):(en?'Disable reading statistics on this browser':'停用此浏览器的阅读统计');button.setAttribute('aria-pressed',String(off));return off;}
  button.addEventListener('click',()=>{try{localStorage.setItem('chance-analytics-opt-out',JSON.stringify(!show()));localStorage.removeItem('chance-anonymous-day');for(let i=sessionStorage.length-1;i>=0;i--){const k=sessionStorage.key(i);if(k.startsWith('chance-reading-')||k==='chance-previous-reading')sessionStorage.removeItem(k);}show();}catch{}});show();
})();
