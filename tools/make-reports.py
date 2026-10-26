from pathlib import Path
import json,sys,subprocess,shutil,os
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'reports'
load=lambda n:json.loads((R/n).read_text(encoding='utf-8'))
content=load('content-integrity.json');formulas=load('formula-rendering.json');sources=load('source-provenance.json');blocks=load('source-block-map.json');assets=load('asset-migration.json');web=load('web-quality.json');browser=load('browser-check.json');reg=load('pipeline-regression.json')
def write(name,text):(R/(name+'.md')).write_text(text,encoding='utf-8')
intro='日期：2026-10-25。范围：阶段1本地候选，未发布、未进入下一阶段。\n\n'
table='|章|母稿字节|公式数|字节基准|正文/标题/图片/图示/互动|公式顺序|\n|---|---:|---:|---|---|---|\n'
for x in content['sections'][:6]:table+=f"|{x['section']}|{x['source_bytes']:,}|{x['formula_count']}|{'一致' if x['baseline_bytes_unchanged'] else '差异'}|{x['migration_status']}|{'一致' if x['formula_order_equal'] else '差异'}|\n"
write('六章完整性对照报告','# 六章完整性对照报告\n\n'+intro+'**对照基准是作者确认的重新整理长篇工作稿，不是已经认证的最初完整 ChatGPT 原文。**\n\n'+table+'\n本次六章字节合计 255,035，公式环境 1,580；三份原有附录也逐字保留，与网页一同核对，共九个内容单元。六章及附录均未精简、润色或应用新数学修改。\n\n检查分两层：源文件按 SHA-256 精确比较；网页从 Markdown 独立解析，比较有序可见文字、标题级别、公式、图片哈希、内嵌 SVG 和交互注册。可见文字忽略排版空白，公式仅统一 CRLF/LF。数值图的数据与交互模型另有检查，不能把组件占位存在等同于行为已验证。\n\n逐章 CSV：[chapter-integrity.csv](chapter-integrity.csv)。完整机器记录：[content-integrity.json](content-integrity.json)。资产状态：[asset-migration.json](asset-migration.json)。\n\n**本项不认证数学正确性和史料真实性，也不认证最初聊天无遗漏。**\n')
table='|内容单元|预期公式|实际公式|TeX及顺序|缺SVG|渲染错误|\n|---|---:|---:|---|---:|---:|\n'
for x in formulas['sections']:table+=f"|{x['section']}|{x['expected']}|{x['rendered']}|{'一致' if x['tex_exact_and_ordered'] else '差异'}|{x['missing_svg']}|{x['render_errors']}|\n"
write('公式渲染报告','# 公式渲染报告\n\n'+intro+table+f"\n共 {formulas['total']} 个公式环境，包含六章 1,580 个及附录 214 个；引擎未报告渲染错误，每个正文公式都有 SVG 与保留的 LaTeX。目录中重复展示的公式不计入正文数量。\n\n"+'公式按章另存于 `dist/assets/formulas/*.json`，不是从公式截图反推源代码。两种换行符被等价处理，公式内部空格及字符保留比较。桌面已验证公式原码开关，手机六章已检查整页无水平溢出；这不表示每个复杂长公式都完成视觉终审。打印版式本轮未逐页人工验收。\n\n渲染状态：[formula-rendering.json](formula-rendering.json)。**数学正确性：待审核，不由本报告的渲染通过推出。**\n')
unknown=[b for b in blocks if b['available_archive_mapping']=='NO_DIRECT_BLOCK_MATCH_REQUIRES_REVIEW']
table='|章|现存片段转换重放|最初完整聊天一致性|\n|---|---|---|\n'
for x in sources['chapters']:table+=f"|{x['chapter']}|{x['registered_transform_replay']}|未核实|\n"
text='# 来源与完整性核对报告\n\n'+intro+'**最初完整 ChatGPT 六章一致性：UNVERIFIED。**现有材料是本地聊天片段、mother 文本、组件转换账本和既有校订记录；即便它们彼此相符，也不能证明最初完整对话不存在遗漏、替换或缺页。\n\n'+table+'\n重放方法：在现存 mother 文本上逐条执行已登记的组件转换，对工作稿逆向还原已登记的既有校订，再比较非排版字符。这里的 MATCH 仅指这条本地材料链，不能升级为“原始完整正文认证”。\n\n分块映射：\n\n'
for key,n in sources['block_mapping_counts'].items():text+=f'- `{key}`：{n} 块。\n'
text+='\n所有分块对“最初完整聊天”的状态仍为未核实。下面的分块在档案中没有直接片段匹配；这不是本轮删减结论，也不代表它们是错误，应结合转换记录逐项复核。既有校订和组件转换另列，未在本轮偷偷改回或改写。完整记录：[source-block-map.json](source-block-map.json)。\n\n|章|分块|当前母稿行号|摘要|\n|---|---:|---:|---|\n'
for b in unknown:text+=f"|{b['chapter']}|{b['block']}|{b['line_start']}|{b['excerpt'].replace('|','／').replace('<','&lt;')}|\n"
text+='\n消除这些未知状态需要可定位的原始消息或完整对话导出，并与当前工作稿产生差异记录；不能用当前稿反推并冒称原文。当前稿作为阶段1迁移基准的作者确认不因来源未核实而失效。\n'
write('来源与完整性核对报告',text)
types={t:sum(x['type']==t for x in assets['assets']) for t in sorted(set(x['type'] for x in assets['assets']))}
text='# 资产迁移报告\n\n'+intro+'每章是独立 Markdown 单元；资产和组件均保留原始文件/源代码及迁移记录，不为排版删除内容。\n\n|类型|记录数|状态与限制|\n|---|---:|---|\n'
descs={'image':'20张独立图片，源/产物字节一致；许可待核','formula-source':'9份分单元TeX JSON，数学正确性另审','inline-diagram':'原内嵌图保留，并独立导出SVG','interaction':'3项互动，模型和页面实际操作分开验证','numeric-chart':'3份数据及SVG导出，数值模型单独校验','citation':'引用出现次数；链接迁移不等于史料真实'}
for t,n in types.items():text+=f'|{t}|{n}|{descs[t]}|\n'
text+='\n逐项记录：[asset-migration.json](asset-migration.json)。源码见 assets/images、experiments.js、app.js 与 provenance；生成后的独立资产见 dist/assets。原会话四个无法定位的引用保留明确待核标记。\n'
write('资产迁移报告',text)
text='# 网页质量验收报告\n\n'+intro+f"静态链接/锚点：{web['static_status']}，{web['pages']} 个页面、{web['local_references']} 个本地引用。\n\n"+'手机 390×844：六章逐页打开，每页恰有一个对应章节；图片加载正常，无整页横向溢出。手机目录打开和点选后关闭、夜间切换已验。跨章检索 Carathéodory 找到6处并从第一章进入第五章。\n\n三项互动已在浏览器操作：完全负相关显示胜率100%、64枚金币；尖峰 n=32 保持屏幕坐标面积4200；随机游走64步可切换线性插值。桌面公式原码开关已验。\n\n打印按钮和打印样式保留，**逐页打印排版未人工终审**；所有复杂公式未逐一视觉检查。数学结论、史料和图片许可不在此项认证范围。\n\n离线包已经核对内部相对路径、六章HTML和49个源文件字节。浏览器工具拒绝 file: 协议，因此**双击离线文件的实际浏览器行为尚未验收**，没有通过其他浏览器入口绕过此限制。HTTP模式的本地预览已验收；离线双击模式留给作者人工确认。\n\n![第六章手机预览](screenshots/mobile-chapter6.png)\n\n记录：[browser-check.json](browser-check.json)、[web-quality.json](web-quality.json)、[offline-package.json](offline-package.json)。\n'
write('网页质量验收报告',text)
text='# 阶段1交付说明\n\n'+intro+'作者的六条补充要求已写入项目约束。当前候选只迁移已确认的长篇工作稿，六章及既有附录没有新增正文修改；数学/史料意见只登记待审。\n\n|维度|本轮结论|\n|---|---|\n|正文迁移完整性|六章及三附录对照通过，源字节未改|\n|公式渲染|1,794个环境，TeX顺序保留，无引擎错误|\n|数学正确性|待审，未应用修订|\n|史料真实性|待审，四个原引用链接仍无法定位|\n|最初完整聊天一致性|未核实；仅现存档案转换重放相符|\n|网页质量|静态与已列HTTP浏览器检查通过；打印及file协议双击验收待做|\n\n'+f"管线回归：陈旧 HTML 被拒绝，隔离测试中已审定的 Markdown 改动确实到达网页（{reg['status']}）。独立比较器负向控制与互动数值测试另有记录。\n\n"+'工程保留 Node/MathJax/Markdown-it + Python 静态分章方式，输入改为每次读取 Markdown，不再把冻结 HTML 当母稿。新增相对路径、独立资产导出、独立比对与分维度报告。\n\n打开 [候选网站](../dist/index.html)，或下载 [离线分章包](../dist/downloads/complete-offline.zip) 和 [逐章可编辑源稿](../dist/downloads/editable-manuscript.zip)。Git 差异：[review.diff](review.diff)；变更统计：[review-stat.txt](review-stat.txt)。\n\n数学待审：[问题册](../docs/数学审校待审问题.md)。史料待审：[问题册](../docs/史料真实性待审问题.md)。各项结论互不替代，不提供“全书学术审校通过”的合并结论。\n\n本地候选交付后停在作者审阅点，不发布、不推送、不编写第七章、不进入下一阶段。\n'
write('阶段1交付说明',text)
names=['阶段1交付说明','六章完整性对照报告','公式渲染报告','来源与完整性核对报告','资产迁移报告','网页质量验收报告']
(R/'report-list.json').write_text(json.dumps(names,ensure_ascii=False),encoding='utf-8')
env=dict(os.environ);env.setdefault('NODE_PATH',str(ROOT.parent/'chance-mathematics-restored-v2/node_modules'))
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
subprocess.run([node,str(ROOT/'tools/render-reports.cjs')],env=env,check=True)
