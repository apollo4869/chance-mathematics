# T-CONDITIONED-BRIDGE：有限方差格点桥的函数极限

配套[第53章](../chapters/53-tree-scaling.md#scaling-bridge)。本页从13章的一致格点局部CLT、25章的有限二阶矩Donsker以及24章的连续路径紧性工具出发，实际证明终点条件桥的极限。这里的条件是和的终点，尚不是树的首次下降条件。

## 1. 固定后代律、可行规模与路径空间

<a id="bridge53-assumptions"></a>

\[ E\xi=1,\qquad0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad
X_i=\xi_i-1,\quad S_k=\sum_{i=1}^kX_i,\quad S_0=0,\quad
d=\gcd\{j\ge1:P(\xi=j)>0\}. \]

后代取有限非负整数，彼此iid，分布固定不随规模变化。条件迫使零后代概率为正，跨度定义有意义。增量支持在−1加d倍整数上。以下规模只沿终点−1正概率的序列趋无穷；52章已证明这等价于规模条件树存在，并且所有充分大的模d余1规模都可行。

\[ \mathbb P_n^{\mathrm{br}}=\mathbb P(\,\cdot\mid S_n=-1),\qquad
x_n(t)=\frac{S_{\lfloor nt\rfloor}+(nt-\lfloor nt\rfloor)X_{\lfloor nt\rfloor+1}}{\sigma\sqrt n}\ (t<1),\quad
x_n(1)=-\frac1{\sigma\sqrt n},\quad
b_n(t)=x_n(t)+\frac{t}{\sigma\sqrt n}. \]

插值、有限条件化及所有读数都可测。闭合后的桥两端均为0，与未闭合路径的一致距离至多该终点缺口。定理是闭合桥在带一致范数的连续函数空间中依分布趋于标准Brownian bridge；这项极限同时成立于未闭合路径。

## 2. 局部CLT提供的不只是一个分母

<a id="bridge53-local"></a>

\[ p_l(z)=P(S_l=z),\qquad p_n(-1)\sim\frac{d}{\sigma\sqrt{2\pi n}},\qquad
\sup_{z\in\mathbb Z}p_l(z)\le\frac{C}{\sqrt l}\quad(l\ge1). \]

第一式沿可行规模。后一个界来自13章一致局部CLT在允许格点上的估计，其他格点概率为0；有限多个初始步长扩大常数即可。对允许的整数终点，若剩余步数与总步数保持正比例，标准化终点限制在紧集内，局部CLT的误差一致趋零。这同时控制分子、分母与远处读数，不把逐点CLT冒充统一估计。

## 3. 前缀的精确密度

<a id="bridge53-density"></a>

\[ \mathcal F_k=\sigma(X_1,\ldots,X_k),\qquad
E_n^{\mathrm{br}}F=
E\!\left[F\,\frac{p_{n-k}(-1-S_k)}{p_n(-1)}\right]\quad(F\text{ bounded and }\mathcal F_k\text{-measurable}). \]

独立未来增量给出条件终点概率，故等式可先对前缀柱事件验证，再用单调类推广。固定a小于1，前缀长度不超过an时，上一节给密度统一有界，常数只依赖a和后代律。插值在最后一个小网格内还会用到下一个增量，改取向上取整的前缀长度，同一界仍成立。

\[ k=\lfloor an\rfloor,\quad z\in-k+d\mathbb Z,\quad |z|\le A\sqrt n:
\quad\frac{p_{n-k}(-1-z)}{p_n(-1)}
-\frac1{\sqrt{1-a}}\exp\!\left(-\frac{(z/(\sigma\sqrt n))^2}{2(1-a)}\right)\longrightarrow0
\quad\text{uniformly in }z. \]

相位并未消失：前缀若可实现，其剩余终点自动在剩余步的允许格点上，因总规模可行。局部CLT的分子与分母带同一个跨度因子，正好抵消。固定紧集上的一致极限，加上密度统一界与无条件Donsker的紧性，允许将任意有界连续前缀泛函连同密度一起取极限；先截在紧集，再令截断范围扩大。

## 4. 首尾两段为什么足以证明整桥紧性

<a id="bridge53-tightness"></a>

前缀密度界把无条件Donsker的模连续控制传给条件桥的任意固定初始比例区间。但仅这一点不控制终点附近。条件iid串在反转增量次序后同律，所以终段相对于终点倒读，也服从同一桥律；闭合后的反转路径是原桥的反向增量读数。

\[ \widehat b_n(t)=b_n(1)-b_n(1-t)=-b_n(1-t)\ \overset d=b_n(t). \]

分别在前2/3与后2/3用上述界。距离小于1/3的任意两时刻总同时落在其中一段；因此两段的模连续控制合起来就是全区间控制。起点固定、模连续紧，24章Arzelà–Ascoli概率判据给连续函数空间的紧性。这不需要四阶矩或后代指数矩。

## 5. 识别极限为Brownian bridge，而非一个新猜测

<a id="bridge53-identification"></a>

\[ b(t)=B_t-tB_1,\qquad
E[F(b|_{[0,a]})]=E\!\left[F(B|_{[0,a]})\,
\frac{\exp(-B_a^2/(2(1-a)))}{\sqrt{1-a}}\right]\quad(0<a<1). \]

右边的权重是Gaussian转移密度从当前值在剩余时间到0，与总时间从0到0的密度之比。对任意有限组前缀时刻，把独立Gaussian增量密度相乘并固定末端坐标0，就得到该比值；所成Gaussian向量协方差为两时刻较小者减其乘积，与左边显式构造相同。连续路径上的有理时刻生成Borel域，单调类给所有有界可测前缀泛函。这是指定的条件核版本，不是除以概率为0的事件。

前缀密度极限于是识别所有严格小于1的时刻的联合律，终点又趋0。紧性与有限维识别给整个桥的弱收敛。闭合误差确定性趋0，故与未闭合路径有相同共同极限。

## 6. 最大单步、阶梯插值与边界

<a id="bridge53-steps"></a>

\[ P_n^{\mathrm{br}}\!\left(\max_{i\le n}|X_i|>\varepsilon\sqrt n\right)
\le CnP(|X_1|>\varepsilon\sqrt n)\longrightarrow0. \]

单个坐标给定终点的密度比也由剩余n减1步的局部上界统一控制；交换性后作并集界得到不等式。有限二阶矩蕴含尾概率乘阈值平方趋0，因为该乘积不超过相应二阶尾积分。因此阶梯与折线桥的一致距离趋0依概率；阶梯在D的J₁拓扑也趋同一个连续极限。这里不需要T-J1最广紧性结论，因为直接有一致距离与连续折线极限。

任意原空间上的逐路径收敛未被断言。规模始终沿实际可行序列；后代律必须固定并满足所列条件。回到[第53章](../chapters/53-tree-scaling.md#scaling-bridge-tight)。
