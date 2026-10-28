// Preserve only a coarse, short-lived referral code from a landing page. No request is sent.
(() => {
  if(location.protocol==='file:'||navigator.doNotTrack==='1'||navigator.globalPrivacyControl)return;
  try{
    if(JSON.parse(localStorage.getItem('chance-analytics-opt-out'))===true)return;
    const value=new URLSearchParams(location.search).get('utm_source');
    if(value)sessionStorage.setItem('chance-reading-campaign',JSON.stringify({source:/^[a-z][a-z0-9_-]{0,39}$/.test(value)?value:'other',at:Date.now()}));
    else{const old=JSON.parse(sessionStorage.getItem('chance-reading-campaign'));if(old&&Date.now()-old.at>1800000)sessionStorage.removeItem('chance-reading-campaign');}
  }catch{}
})();
