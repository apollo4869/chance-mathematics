import {env} from 'cloudflare:workers';
import {authorize,chapterCount,PRIVATE_HEADERS} from '../../../lib/reading-analytics.mjs';
import {dashboard} from '../../../lib/dashboard.mjs';
export const dynamic='force-dynamic';
export async function GET(request:Request){try{
  await authorize(request,env);
  const local=['127.0.0.1','localhost','[::1]'].includes(new URL(request.url).hostname);
  const chapters=Array.from({length:chapterCount(env)},(_,i)=>'<option value="'+(i+1)+'">第 '+(i+1)+' 章</option>').join('');
  const configured=dashboard.replace(/<select name="chapter">[\s\S]*?<\/select>/,'<select name="chapter"><option value="">全部章节</option>'+chapters+'</select>');
  const page=local?configured.replace('<main>','<main><div class="note">本地验收环境：使用 Sites 开发登录模拟及独立本地 D1；测试事件不是真实读者数据，也不会上传线上。</div>'):configured;
  return new Response(page,{headers:{...PRIVATE_HEADERS,'Content-Type':'text/html; charset=utf-8'}});
}catch(error:any){
  const status=error.status||503;
  const text=status===401?'请使用作者的 ChatGPT 账号登录。':status===403?'此后台仅向作者 Haobai Wang 开放。':'分析后台尚未配置完成，当前不开放访问。';
  return new Response('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>作者分析后台</title><body style="font:18px/1.8 sans-serif;max-width:650px;margin:12vh auto;padding:24px"><h1>作者专用 · 读者分析</h1><p>'+text+'</p>'+(status===401?'<a target="_top" href="/signin-with-chatgpt?return_to=%2Fadmin%2Fanalytics">使用 ChatGPT 登录</a>':'')+'<p><a href="/">返回公开教材</a></p></body></html>',{status,headers:{...PRIVATE_HEADERS,'Content-Type':'text/html; charset=utf-8'}});
}}
