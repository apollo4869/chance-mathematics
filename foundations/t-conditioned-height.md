# T-CONDITIONED-HEIGHT：仅有限方差的高度、轮廓与联合极限

配套[第53章](../chapters/53-tree-scaling.md#scaling-height-problem)。沿实际可行规模，后代律固定、临界、非退化，方差有限且正。前置为52章有限编码/分枝/Dwass、13章一致局部CLT、12章可积iid强大数律、24章连续路径紧性，以及本章已经证明的条件Łukasiewicz游程极限。本页不用后代指数矩，不调用未来树空间定理。

## 1. 右侧兄弟数与有限层的加权祖先链

<a id="height53-spine"></a>

\[ P_n=P(\,\cdot\mid N=n),\qquad a=\frac{\sigma^2}{2}>0,\qquad
W_j=\sum_{u\prec v_j}\bigl(k_T(u)-J_u(v_j)\bigr),\quad H_j=|v_j|,\quad H_n=0,\quad W_n=-1. \]

求和沿根到该节点的严格祖先，孩子指标表示下一步走向第几个孩子。访问该节点前，待访问列表只有该节点及各祖先尚未访问的右侧兄弟，故52章列表身份给出上式。终点高度0只是闭合插值，不是一名额外节点。

\[ P_*(D=k,J=j)=p_k\quad(k\ge1,\ 1\le j\le k),\qquad
R=D-J,\quad Z=D-1,\qquad E_*R=a,\quad E_*Z=\sigma^2. \]

这些权重的总和为后代均值1，所以确是一份概率。对一条长h的被标记祖先链，各层取这份独立成对分布；将所有深度h节点逐个标记再相加，原树的每个祖先生育权重恰为对应的后代概率。因此对任意非负链泛函，有下式多对一期望身份。证明直接对孩子数与选中孩子编号逐项求和；未被标记的子树积分为1，Tonelli合法。

\[ E\!\left[\sum_{|v|=h}F(\text{ancestral pairs of }v)\right]
=E_*F((D_i,J_i)_{1\le i\le h}). \]

两个均值由有限方差直接计算：对每个孩子数，右侧兄弟数从0加到孩子数减1；总兄弟数则是孩子数减1在孩子数偏置下的均值。这里只有有限层加权身份，没有把一个正局部鞅当密度，也没有断言无限层密度等于某个鞅极限。

## 2. 给定总规模后，祖先链旁边是一片森林

<a id="height53-forest-density"></a>

\[ A_h=\sum_{i=1}^h Z_i,\qquad R_h=\sum_{i=1}^h R_i,\qquad
q_l^{(r)}=P(N_1+\cdots+N_r=l),\qquad q_n=q_n^{(1)}. \]

沿长h的标记链，h个严格祖先已经计入人口；每层未选中的孩子各带一棵子树，链末节点再带一棵完整子树。因此余下恰为兄弟总数加1棵独立GW树，所需总规模是n减h。将根分枝性质在有限条链上逐层使用，得精确身份

\[ E\!\left[\sum_{|v|=h}F(v)\mathbf1_{\{N=n\}}\right]
=E_*\!\left[F((D_i,J_i)_{i\le h})\,q_{n-h}^{(A_h+1)}\right]\qquad(0\le h<n). \]

为严格验证，可固定链上每个孩子数和编号，树的乘积权重分成祖先权重与侧森林权重；侧森林的左右排列由编号唯一确定，概率只依赖其棵数。先对有限规模侧树求和，再对可数多个链数据求和，得到式子。不存在被遗漏的整树条件或额外归一化因子。

\[ q_l^{(r)}=\frac rl P(S_l=-r)\le C r\,l^{-3/2}\quad(l\ge1,\ r\ge1),\qquad
q_n\sim\frac{d}{\sigma\sqrt{2\pi}}\,n^{-3/2}. \]

森林上界用52章Dwass与13章统一局部上界；若根数超过总节点数，左边为0，所以上界仍成立。最后的单树渐近沿可行规模。它将被用来控制随机选中节点的条件祖先链，而不是无理由地把条件链当成独立同分布。

## 3. 所有长祖先链，不能同时几乎没有右侧兄弟

<a id="height53-lower"></a>

\[ c=a/2,\qquad
\exists\theta>0,\ \eta<1:\quad e^{\theta c}E_*e^{-\theta R}=\eta,\qquad
P_*(R_h<ch)\le\eta^h. \]

右侧兄弟数非负且有正有限均值，负指数变换在0的右导数为负均值，故可选上述参数；Markov不等式给最后的指数下尾。这里没有假设正指数矩，巨大后代完全允许。

要控制树中每一段祖先链，固定起始深度b与链长h。根分枝性质及临界条件下第b代期望人数为1，再用多对一，坏链的期望个数至多该指数下尾。在规模n的树中，两深度均不超过n。对所有起始深度、所有不短于固定正数乘平方根n的链长作并集，再除以总规模概率，得到

\[ P(\mathcal E_{n,\delta}^{\,c}\mid N=n)
\le\frac{n^2\eta^{\lceil\delta\sqrt n\rceil}}{q_n}\longrightarrow0,\qquad
\mathcal E_{n,\delta}:
\ \sum_{\text{segment}}R_i\ge c\,(\text{length})\quad\text{if length}\ge\delta\sqrt n. \]

对每个固定正δ，事件中的所有长段同时受控。对短段，长度小于阈值且兄弟数非负，于是无论长短，都有段长度不超过阈值加右侧兄弟总数除以c。这个逐段结论比只控制一条典型链强，正是下面模连续证明需要的。

## 4. 从祖先段到高度曲线的模连续

<a id="height53-tightness"></a>

取先序中的两个不同节点。若前者为后者祖先，直接用上节的段界。否则令共同祖先的两个有关孩子为x、y，先访问x的子树，再访问y的子树。两次访问之间的路径最低值不高于x的起点，因为x子树会先结束，也不高于y的起点，因为该起点已经出现在区间里。

\[ I_{ij}=\min_{i\le k\le j}W_k,\qquad
|H_i-H_j|\le d_T(v_i,v_j)
\le2+2\delta\sqrt n+\frac{W_i+W_j-2I_{ij}}c
\quad(0\le i<j<n,\ \mathcal E_{n,\delta}). \]

从共同祖先的孩子到各节点应用祖先段界，再各补一条边，得到式子；前者为祖先时同一较宽上界也成立。最后一项至多为对应区间路径振幅的两倍除以c。根到任意节点的段界还给出高度上界。

\[ \frac{H_i}{\sqrt n}\le\delta+\frac{W_i}{c\sqrt n}\quad(i<n,\ \mathcal E_{n,\delta}). \]

定义第n项高度为0。靠近时刻1时，前式中的路径值因路径末值−1及连续游程极限而一致小，所以最后的闭合也受控。节点间线性插值的模连续由相邻网格读数控制，时间范围最多多两个网格。已证Łukasiewicz折线在一致拓扑紧且趋连续游程；先固定δ，用上述界取网格模连续，再令δ下降到0，得到高度除以平方根n在连续函数空间的紧性。

## 5. 典型节点只需要一阶可积的脊柱平均

<a id="height53-typical"></a>

\[ E_n\!\left[\frac1n\sum_{j<n}
\mathbf1_{\{|W_j-aH_j|>\varepsilon\sqrt n\}}\right]
=\frac1{nq_n}\sum_{h=0}^{n-1}
E_*\!\left[\mathbf1_{\{|R_h-ah|>\varepsilon\sqrt n\}}\,
q_{n-h}^{(A_h+1)}\right]. \]

这就是先在规模条件树中均匀选一名节点的坏事件概率。等式来自第2节的标记链身份；根的项为0。高度超过A乘平方根n的部分，由整树最大高度的紧性统一控制。其余部分取固定A，剩余森林规模至少n的一半（n充分大）。森林界与单树分母因此使每一项的系数至多常数除以n，再乘兄弟总数加1。

极短链的总贡献至多常数乘δ平方：对长度不超过δ乘平方根n求和，用兄弟总数的期望为方差乘链长。对中间长度，12章强大数律给右侧兄弟平均趋于a；与此同时总兄弟平均组成一致可积族。后一结论不能靠二阶矩，因为偏置后的后代未必有二阶矩，下面给出只用一阶矩的证明。

\[ \overline Z_h=\frac1h\sum_{i=1}^hZ_i,\qquad
E_*[\overline Z_h;\overline Z_h>2L]\le2E_*[Z;Z>L]\longrightarrow0
\quad\text{uniformly in }h. \]

因为每项截在L以内的平均至多L，若整个平均大于2L，其尾部平均至少占一半，逐路径便有此界。故一致可积性与强大数律结合，给出下式；不要求右侧兄弟与总兄弟彼此独立。

\[ \sup_{\delta\sqrt n\le h\le A\sqrt n}
E_*\!\left[\frac{A_h+1}{h};
\left|\frac{R_h}{h}-a\right|>\frac{\varepsilon}{A}\right]\longrightarrow0. \]

中间链的系数求和是链长之和除以n，有界于只依赖A的常数，故乘上述趋零项仍趋0。短链给δ平方，长链由高度紧性给可任意小的尾部。依次令n趋无穷、A趋无穷、δ下降到0，得到坏节点比例的期望趋0，因而比例本身趋0依概率。所有极限均在规模条件树律下，不曾用无条件强大数律直接替代条件分布。

## 6. 从绝大多数节点到整条曲线

<a id="height53-uniform"></a>

\[ D_n(t)=\frac{W(nt)-aH(nt)}{\sqrt n}. \]

两条折线都在连续函数空间紧，所以其差也模连续紧。若一致范数大于两倍固定ε，而长度η上的振幅至多ε，那么至少一段长度η的一半上，绝对值大于ε；当n充分大，这段含至少η乘n除以4个网格点。于是

\[ P_n(\|D_n\|_\infty>2\varepsilon)
\le P_n(\omega(D_n,\eta)>\varepsilon)
+\frac4\eta E_n\!\left[\frac1n\sum_{j<n}
\mathbf1_{\{|W_j-aH_j|>\varepsilon\sqrt n\}}\right]. \]

先以紧性选择η使第一项任意小，再由上一节令第二项趋0，证明一致范数趋0依概率。末端高度0和路径末值−1造成的误差为平方根n的倒数，不能制造一个遗漏的坏端点。由此识别高度极限及与Łukasiewicz的共同极限。

\[ \sup_{0\le j\le n}\frac{|W_j-\frac{\sigma^2}{2}H_j|}{\sqrt n}
\xrightarrow{P_n}0,\qquad
\left(\frac{W(n\,\cdot)}{\sigma\sqrt n},\frac{\sigma H(n\,\cdot)}{2\sqrt n}\right)
\Rightarrow(e,e). \]

## 7. 轮廓的实际时钟与误差

<a id="height53-contour"></a>

\[ b_j=2j-H_j,\quad s_j=j/n,\quad t_j=b_j/(2(n-1))\ (j<n),\qquad
s_n=t_n=1,\qquad
\max_j|t_j-s_j|\le\frac1{n-1}+\frac{\max_j H_j}{2(n-1)}
\xrightarrow{P_n}0. \]

只考虑n至少为2，根单点例外不影响极限。52章证明这些首次访问时刻严格递增，最后首次访问仍在真正终点之前。以节点时刻与轮廓时刻的对应作分段线性同胚，记为λ。它与恒等映射一致接近，逆映射的一致距离相同。

\[ h_n(t)=\frac{\sigma H(nt)}{2\sqrt n},\qquad
c_n(t)=\frac{\sigma C(2(n-1)t)}{2\sqrt n},\qquad
\|c_n\circ\lambda-h_n\|_\infty
\le\frac{\sigma}{2\sqrt n}\left(1+\max_{j<n}|H_{j+1}-H_j|\right)
\xrightarrow{P_n}0. \]

在两个首次访问之间，轮廓先退到后一节点的父亲，再上升一步；它与两个高度读数的直线段相差至多高度差加1。最后一段完全退到根，是线性的，满足同一上界。高度连续极限的紧性已经使最大网格跳差除以平方根n趋0，故右边趋0。再用高度模连续及λ逆趋恒等，消除时间变换，得到两条原参数曲线一致接近。这里不是仅凭时钟接近便忽略曲线振荡。

## 8. 联合定理、插值与严格责任边界

<a id="height53-joint"></a>

\[ \boxed{\quad
\left(\frac{W(n\,\cdot)}{\sigma\sqrt n},
\frac{\sigma H(n\,\cdot)}{2\sqrt n},
\frac{\sigma C(2(n-1)\,\cdot)}{2\sqrt n}\right)
\Rightarrow(e,e,e)\quad\text{in }C([0,1])^3.\quad} \]

这是同一条件树的三条曲线的联合弱收敛，极限三分量是同一份规范游程，不是三个独立副本。两次一致概率比较与已证的第一分量极限给出结论。所有映射由有限编码可测；联合性不要求先在原空间上实现逐路径收敛。

高度阶梯与折线的差由最大网格高度跳控制，已证趋0；Łukasiewicz对应结论由T-CONDITIONED-BRIDGE及循环不改变增量给出。阶梯版本在D的J₁拓扑收敛，连续极限下这些比较实际更强。若把轮廓时钟写成2n，必须先在真正终点以后补零，再由已证模连续控制这个趋零的相对时间误差；用节点数减1的平方根替代平方根n也须先有范数紧性。

这里没有证明编码商空间是实树，没有断言GH/GHP收敛，也没有处理无限方差或一般Lévy高度；这些仍按蓝图由54–55及58承担。52章的精确有限编码本身不足以得本页定理，新增的核心是条件桥控制、切桥识别、所有祖先段与典型节点的两种互补估计。回到[第53章](../chapters/53-tree-scaling.md#scaling-joint)。
