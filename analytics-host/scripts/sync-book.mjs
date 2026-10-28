// Copy already-validated static output without rendering or rewriting chapter bodies.
import {cp,mkdir,readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve(fileURLToPath(new URL('../..',import.meta.url))),dest=path.join(root,'analytics-host/public');
const source=path.join(root,'dist');
await mkdir(dest,{recursive:true});
await cp(source,dest,{recursive:true,filter:p=>!p.includes('node_modules')});
const {glob}=await import('node:fs/promises');const manifest={source:'../dist',chapters:{}};
for await(const p of glob('**/chapters/*.html',{cwd:source})){const data=await readFile(path.join(source,p));manifest.chapters[p]=crypto.createHash('sha256').update(data).digest('hex');}
await writeFile(path.join(dest,'book-generated.json'),JSON.stringify(manifest,null,2));
console.log(JSON.stringify({copied_chapter_pages:Object.keys(manifest.chapters).length,chapter_bytes:'UNCHANGED'}));
