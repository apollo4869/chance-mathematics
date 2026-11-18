// Static SVG inspection only, never browser screenshots.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const sharp=require('C:/Users/golde/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),a=path.join(root,'assets/visuals/explanatory-volume8-v1'),o=path.join(root,'reports/volume8-visual-batch1-2026-11-06/static-renders');fs.mkdirSync(o,{recursive:true});
const defaults={V54:'1-4',V55:'0',V56:'balanced-2',V57:'1-1-1',V58:'3-2'};
(async()=>{for(const lg of ['zh','en'])for(const [id,key] of Object.entries(defaults)){
 let height=0;const pieces=[];
 for(const [size,width,left] of [['desktop',700,0],['mobile',360,720]]){const data=await sharp(path.join(a,`${id}-${lg}-${key}-${size}.svg`)).resize({width}).flatten({background:'#fffefa'}).png().toBuffer(),m=await sharp(data).metadata();height=Math.max(height,m.height);pieces.push({input:data,left,top:40});}
 const note=Buffer.from(`<svg width="1090" height="38"><text x="12" y="26" font-family="sans-serif" font-size="15" fill="#173f39">${id} ${lg} — static SVG raster / NOT browser screenshots</text></svg>`);
 await sharp({create:{width:1090,height:height+50,channels:4,background:'#fffefa'}}).composite([{input:note,left:0,top:0},...pieces]).png().toFile(path.join(o,`${id}-${lg}-wide-narrow.png`));
 }for(const id of ['P04','P05'])await sharp(path.join(root,`assets/visuals/explanatory-v2/${id}.zh.svg`)).resize({width:1200}).flatten({background:'#fffefa'}).png().toFile(path.join(o,`${id}-adopted-reference.png`));
 console.log('10 bilingual composition boards and 2 unchanged reference renders created. NOT browser tests.');})().catch(e=>{console.error(e);process.exitCode=1;});
