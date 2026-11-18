"""Summarize completed evidence, keeping browser/PDF/math review separate."""
from pathlib import Path
from collections import Counter
import hashlib,json,re
R=Path(__file__).resolve().parents[1];O=R/'reports/full-book-reading-2026-11-07';SITE=R/'work/reading-acceptance/site'
def read(n):return json.loads((O/n).read_text('utf8'))
def save(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')

def main():
 desktop=read('local-browser-desktop-final.json');mobile=read('local-browser-mobile-final.json');modes=read('reading-mode-browser-final.json')
 online=read('online-browser-chapters.json');fd=read('figures-browser-desktop.json');fm=read('figures-browser-mobile-confirmed.json');static=read('static-browser-pages.json')
 links=read('link-and-resource-check.json');integration=read('integration.json');offline=read('offline-package.json');frozen=read('frozen-content-check.json')
 assert len(desktop)==len(mobile)==len(modes)==116
 assert len(online)==58 and len(fd)==len(fm)==90
 assert len(static)==len(read('static-reading-targets.json'))
 assert all(x['pass'] for x in modes)
 assert all(not x['brokenImages'] and not x['mathErrors'] and x['pageWidth']<=x['viewport']['w'] for x in desktop+mobile)
 assert all(x['publicationOrder']==['book-section','chapter-edition'] and all(not d['open'] for d in x['metadata']) for x in desktop+mobile)
 assert not links['missing'] and not links['missing_anchors'] and not links['duplicate_ids']
 assert all(not x['brokenImages'] and not x['mathErrors'] for x in static)
 assert all(x['changed'] is not False and (x['after']['unit'] or '').startswith(x['section']+' ') for x in fd+fm)
 assert all(x['renderedSnapshotRefreshedBeforeCapture'] for x in fd+fm)
 privacy_denied=[]
 for p in SITE.rglob('*'):
  if p.is_file() and any(q in {'.git','author-work','reports','planning','node_modules','local-preview','__reading_html'} or q.startswith('.env') for q in p.relative_to(SITE).parts):privacy_denied.append(p.relative_to(SITE).as_posix())
 assert not privacy_denied
 # The final screenshots are browser JPEGs, not regenerated SVG rasterizations.
 shots=[]
 for p in sorted((O/'screenshots').rglob('*.jpg')):
  raw=p.read_bytes();assert raw[:2]==b'\xff\xd8'
  shots.append(dict(path=p.relative_to(O).as_posix(),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),kind='actual browser screenshot'))
 save('screenshot-manifest.json',dict(files=shots,SVG_rasterizations_used_as_browser_screenshots=False))
 save('privacy-and-scope.json',dict(input_sources=['retained public reading edition static files','root-level approved volume VII/VIII SVG/CSS/JS/JSON','existing authorized reading-footer implementation','targeted reader/layout repairs'],unpublished_papers_read=False,new_research_results_added=False,local_private_source_repository_exported=False,forbidden_candidate_paths=privacy_denied,production_feedback_submitted=False,production_backend_configuration_modified=False,offline_analytics_scripts='removed from the offline HTML copy only',hosting_access=read('hosting-access.json')))
 summary=dict(online_chinese_chapters=58,local_desktop_chapter_language_pages=116,local_mobile_chapter_language_pages=116,mode_round_trips=116,adopted_visual_groups=45,figure_language_views_each_layout=90,interactive_samples_each_layout=sum(x['changed'] is True for x in fd),static_reader_pages=len(static),html_pages_inventoried=links['all_html_parsed'],visual_asset_files=len(read('all-visual-assets.json')['files']),missing_resources=0,missing_anchors=0,duplicate_reader_ids=0,desktop_overflow=0,mobile_overflow=0,screenshots=len(shots),frozen_source_files=sum(frozen['files_by_tree'].values()),native_PDF='not verified',physical_devices='not verified',full_parameter_state_space='not exhausted',independent_expert_mathematics='open; no status upgrade',published=False,pushed=False)
 save('acceptance-summary.json',summary)
 rows='\n'.join(f'|{x["chapter"]}|{x["lang"]}|{", ".join(x["adopted_groups"]) or "保留既有正文／辅助图"}|通过|通过|页尾收起|' for x in read('chapter-inventory.json'))
 text=f'''# 八卷58章阅读验收：2026-11-07

本轮完成本地整合、真实浏览器验收和定点修复，**没有发布、推送或重新设计数学插图**。V54–V58最新修订按作者决定采用；全书45组高优先级解释图作为当前视觉工作稿冻结。最终作者审美、真机、原生PDF和独立专家数学终审继续开放。

## 实际版本与范围

线上58个中文章节已逐页用真实浏览器读取，其插图清单与此前35组发布版一致；第七、八卷10组新图此前只在本地候选中，这是未发布的版本差异。线上英文未逐章复测；完整中英验收在本轮整合版完成。

本地以保留的公开HTML为母本，加入已经采用的20份中英文图示片段，汇总为45组／90份语言版本。没有重新从Markdown生成或改写数学。116个章节页面全部保留原数学DOM，移除新增图示片段后可逐字还原原书内容。工程辅助图及P03、P04、P05等成熟图原样保留。第54、55章旧试点与新图分别解释不同问题，并非同图重复展示。

## 确认的问题与修订

|问题|确定证据|本轮处理|
|---|---|---|
|章节开头仍有作者／本地预览／内容指纹溯源区|线上58页和本地母本实际DOM顺序|接入此前已有的页尾折叠实现；116页默认收起，版本和引用链接在结尾；元数据不删除|
|第7章手机模式切换回到上一节|首次第2单元切到小节模式实际选择了第1单元，锚点落在旧typewriter图|当上一节已结束、阅读线处于下一节标题前空白时，保留下一个标题；116页以第二小节做往返回归|
|第13、14章长行内公式撑宽手机页面|390px浏览器中页面宽度分别到483／439px|仅屏幕窄布局限制行内公式容器宽度并允许内部滚动；原TeX和SVG不变，复测无整页横向溢出|
|新长图被旧340px图片上限压小|V58手机SVG自然大小360×948，却显示为327×340|仅在章节布局层解除V7/V8解释图的屏幕高度上限；恢复约327×861，保留图的原宽高比；图源及交互不改|
|原型打印页残留审阅专用链接|20个新打印入口中40处`/review/`链接在完整站点无目标|只将这些导航改为实际正文、另一语言打印页及SVG；打印正文和图示保持原样|
|当前离线验收包须包括新图及布局|原云端下载由Worker分片合成，保留的public目录没有单个完整ZIP|另建读者版ZIP，含58章中英、证明、图片、交互与打印页；不把本地静态文件缺失误报成线上下载故障|

本轮候选初次封装曾漏复制旧`.img`扩展的历史图片，发现后按原字节补回并重测；线上这些原图并未失效。原始失败记录保留，不把修订前结果删掉或登记为最终通过。

## 真正完成的验收

|检查|实际范围与结果|
|---|---|
|在线页面|58个中文章节；不是只测HTTP 200。记录实际标题、公式、图组与元数据位置|
|本地桌面／手机|各116个中英文章节；手机为390px浏览器视口，**不是实体手机**；已加载图片、公式错误节点、页面溢出检查均无失败|
|阅读模式|116页逐页选择第二小节，切换小节／整章并前后往返；首次指针自动化遇到原生下拉菜单干扰，最终回归包含键盘激活与可见状态等待。不能据此宣称所有触摸、缩放与任意滚动位置已穷尽|
|图示|桌面、手机各90份语言版本；88份可交互版本各触发一个非默认状态，P04中英是静态图；位置均与登记的小节相符；未穷举全部参数组合|
|截图|最终图示截图先刷新可见DOM再采集，防止键盘输入后旧画面尚未重绘；新V7/V8图提供实际视口及滚动截图。长页整页截图接口返回失败，不能将这些视口截图冒称原生整页。早期未同步的首帧只作原始记录，最终以confirmed记录为准|
|静态页|{{len(static)}}个卷级、首页／收束及打印HTML在浏览器读取，图片及MathJax错误检查无失败；这是屏幕中的打印页面，**不等于打印介质或原生PDF验收**|
|文件／链接|{{links['all_html_parsed']}}个HTML纳入清单；阅读页未发现缺失资源、锚点或重复ID；全部{{summary['visual_asset_files']}}份实际视觉资源列出哈希|
|离线|ZIP的CRC和每个文件哈希通过；解压后在独立目录启动本机服务器，实际抽查4个中英文页面并操作V48；没有模拟系统断网，没有验收完整file://模式|

原页面打印功能覆盖所有章节；现有独立章节打印HTML为48章中英96页，其他10章继续用原浏览器打印样式。本轮没有机械新建20份重复打印页。原生PDF的分页、裁切和印刷可读性仍需单独验收。

逐页覆盖表示实际打开页面、读取DOM、检查阅读模式及指定图组，**不是把58章每一屏逐字滚读或逐张审核全部旧图像素**。懒加载图片的pending列表保留在原始记录中；未进入视口的旧图只能结合资源存在性检查，不能冒称全部已加载实看。公式错误节点检查也不等于逐式数学正确性审查。

完成上述逐页与图示记录后，最后追加的语言切换点击和页尾展开／收起操作未能执行：新一轮浏览器绑定返回“Local browser use is disabled in Work settings”。此前实际完成的截图和记录保留有效；语言链接目标及页尾默认收起通过文件与DOM核验，但不冒称这两项追加交互已经点击实测。没有反复重试权限，也没有借此改动应用设置。

## 阅读判断与仍开放的事项

已验证图组嵌入对应数学小节，没有把标题拆成新正文小节，没有在公式内部插图；同组中英资源成对存在。V7/V8高度上限修复避免以缩小文字来压缩长图。V52、V53、V56、V58的手机内容仍较长，需要自然滚动；本轮保护已采用结构，未以统一卡片或删除条件来缩短它们。是否打断首次阅读的节奏，仍应由作者试读和真实设备补充判断，不能由DOM检查自动判为优秀。

数学核验、作者工作稿采用和独立专家终审保持分离。原书正文、证明、卷源及视觉源共{{summary['frozen_source_files']}}份文件与受保护工作树字节一致。本轮不重证定理，不关闭T-LEVY-HEIGHT、T-CONDITIONED-HEIGHT等原有证明责任，不宣称全书最终定稿。

未读取作者未发表论文，没有新增其定理、分裂概率、密度或研究机制。候选只取现有公开静态文件、已采用图源和阅读布局代码；不导出`.git`、私人档案、聊天、密钥或后台数据库。离线副本关闭统计脚本，线上统计／D1配置没有更改。

## 稳定作者阅读版的部署建议

建议下一次获明确发布授权后，沿用chancemathematics.org现有Sites／Cloudflare Worker工程及域名，不另建替代站点或改DNS。保留后台授权与D1。原构建依次运行`encode-reading-html.mjs`、`package-reading-offline.mjs`和框架构建：必须重新生成HTML gzip清单、资源映射及8MiB离线分片，不能只覆盖一个静态目录，也不能直接把本轮约66MiB的ZIP当作单个托管静态资产上传。

既有2026-11-05发布回执记载版本17和回滚版本16；它是历史回执。本轮只读`get_site`返回“Sites project not found”，说明当前连接不能确认原项目权限，不代表公开网站已下线。发布前需连接原拥有者账号／工作区，再确认项目、当前版本及可回滚快照；本轮不申请新项目、不修改受众或权限。

如需独立作者预览，优先使用原托管支持的服务端访问控制；公开工作稿则继续保留审校状态与noindex。noindex不等于访问控制。线上发布后的手机、下载、gzip路由、缓存和回滚验证必须另做，不能用本地通过替代。**本轮没有部署。**

## 文件入口

- `chapter-inventory.csv`：116份逐章语言清单；`visual-resources.csv`：正文中实际图片／canvas与上下文。
- `all-visual-assets.csv`及JSON：包括预生成交互状态的完整视觉文件清单。
- `integration.json`、`frozen-content-check.json`：母本恢复与保护记录。
- `local-browser-*-final.json`、`reading-mode-browser-final.json`：逐页实际浏览器状态。
- `figures-browser-desktop.json`、`figures-browser-mobile-confirmed.json`：最终图示交互与截图对应。
- `static-browser-pages.json`、`offline-browser.json`：实际页面检查；不充作原生PDF证明。
- `privacy-and-scope.json`、`hosting-access.json`：保密与部署边界。
- `screenshots/`：真实浏览器JPEG；`screenshot-manifest.json`逐份记录哈希。
- 先前的`initial`／`firstpass`记录保留为过程证据，不能当作最终验收结论。

完成后停止供作者审查，不自动发布、不推送、不开始下一轮全书重构。

## 逐章验收索引

|章|语言|已采用图组|桌面|手机与模式|技术资料|
|---|---|---|---|---|---|
{rows}
'''
 # Keep the long prose template readable while substituting evidence counts.
 text=text.replace("{len(static)}",str(len(static))).replace("{links['all_html_parsed']}",str(links['all_html_parsed'])).replace("{summary['visual_asset_files']}",str(summary['visual_asset_files'])).replace("{summary['frozen_source_files']}",str(summary['frozen_source_files']))
 (O/'REPORT.md').write_text(text,encoding='utf8',newline='\n')
 print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
