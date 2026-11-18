// SVG raster inspection only. This does not launch a browser or create browser screenshots.
const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/golde/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),asset=path.join(root,'assets/visuals/explanatory-volume7-v1');
const out=path.join(root,'reports/volume7-visual-batch1-2026-11-06/static-renders');
fs.mkdirSync(out,{recursive:true});
const defaults={V48:'independent-0',V49:'real-0',V51:'0-10',V52:'A-3',V53:'1'};
const requested=new Set(process.argv.slice(2)),selected=Object.entries(defaults).filter(([id])=>requested.size===0||requested.has(id));
(async()=>{for(const lg of ['zh','en'])for(const [id,state] of selected){
 const sources=['desktop','mobile'].map(size=>path.join(asset,`${id}-${lg}-${state}-${size}.svg`));
 const images=[];let height=0;
 for(let i=0;i<sources.length;i++){const data=await sharp(sources[i]).resize({width:i===0?700:350}).flatten({background:'#fffefa'}).png().toBuffer();const info=await sharp(data).metadata();height=Math.max(height,info.height);images.push({input:data,left:i===0?0:720,top:45});}
 const label=Buffer.from(`<svg width="1080" height="40"><rect width="1080" height="40" fill="#eaf2ee"/><text x="15" y="26" font-family="sans-serif" font-size="16" fill="#173f39">${id} ${lg} — SVG raster QA, NOT browser screenshots — wide / narrow composition</text></svg>`);
 await sharp({create:{width:1080,height:height+60,channels:4,background:'#fffefa'}}).composite([{input:label,left:0,top:0},...images]).png().toFile(path.join(out,`${id}-${lg}-wide-narrow.png`));
 }console.log(`${selected.length*2} static raster QA boards updated. Browser screenshots remain pending.`);})();
