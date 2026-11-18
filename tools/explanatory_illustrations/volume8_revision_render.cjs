// Static before/after renders of existing SVG assets. No browser screenshots.
const fs=require('fs'),path=require('path'),cp=require('child_process');
const sharp=require('C:/Users/golde/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),out=path.join(root,'reports/volume8-visual-revision-2026-11-07/static-renders'),a='assets/visuals/explanatory-volume8-v1/';
fs.mkdirSync(out,{recursive:true});
const git='C:/Program Files/Git/cmd/git.exe';
async function board(id,lg,k){
 const pieces=[];let h=0;
 for(const [layout,width,left] of [['desktop',700,0],['mobile',360,720]]){
  const file=`${a}V58-${lg}-${k}-2-${layout}.svg`,buf=await sharp(path.join(root,file)).resize({width}).flatten({background:'#fffefa'}).png().toBuffer(),m=await sharp(buf).metadata();
  pieces.push({input:buf,left,top:40});h=Math.max(h,m.height);
 }
 const note=Buffer.from(`<svg width="1090" height="38"><text x="12" y="26" font-family="sans-serif" font-size="15" fill="#173f39">V58 ${lg} k=${k} — static SVG render, NOT browser screenshots</text></svg>`);
 await sharp({create:{width:1090,height:h+50,channels:4,background:'#fffefa'}}).composite([{input:note,left:0,top:0},...pieces]).png().toFile(path.join(out,`V58-${lg}-k${k}-wide-narrow.png`));
}
async function compare(id,lg){
 const oldkey=id==='V56'?'iid-1':'3-2',newkey=id==='V56'?'balanced-2':'3-2';let h=0;const pieces=[];
 for(const [version,key,left] of [['before',oldkey,0],['after',newkey,720]]){
  const file=`${a}${id}-${lg}-${key}-desktop.svg`,src=version==='before'?cp.execFileSync(git,['-c','safe.directory='+root.replaceAll('\\','/'),'show','56f537d4:'+file],{cwd:root,maxBuffer:5e6}):fs.readFileSync(path.join(root,file));
  const buf=await sharp(src).resize({width:700}).flatten({background:'#fffefa'}).png().toBuffer(),m=await sharp(buf).metadata();pieces.push({input:buf,left,top:40});h=Math.max(h,m.height);
 }
 const note=Buffer.from(`<svg width="1430" height="38"><text x="12" y="26" font-family="sans-serif" font-size="15" fill="#173f39">${id} ${lg} BEFORE</text><text x="735" y="26" font-family="sans-serif" font-size="15" fill="#173f39">AFTER — static SVG render, NOT browser screenshots</text></svg>`);
 await sharp({create:{width:1430,height:h+50,channels:4,background:'#fffefa'}}).composite([{input:note,left:0,top:0},...pieces]).png().toFile(path.join(out,`${id}-${lg}-before-after.png`));
}
(async()=>{for(const lg of ['zh','en']){for(const k of [2,3,4])await board('V58',lg,k);for(const id of ['V56','V58'])await compare(id,lg);}console.log('6 all-k composition boards and 4 static before/after boards rendered; not browser QA.');})().catch(e=>{console.error(e);process.exitCode=1;});
