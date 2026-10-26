# 《偶然的数学》
第一卷 · 偶然可以计算吗？

# 第四章：当随机性进入时间——从随机游走到 Brownian motion

一条连续却几乎处处无法用速度描述的路径，是如何从最简单的随机跳跃中诞生的？

第三章，我们发现了概率论中一个极为深刻的现象。

大量独立随机变量的和，在适当的中心化与标准化之后，可能收敛到正态分布：

\[
\frac{X_1+\cdots+X_n-n\mu}{\sigma\sqrt n}
\xrightarrow{d}N(0,1).
\]

但是，我们此前始终将随机实验看作一个整体。

我们只关心前 \(n\) 个随机变量相加的最终结果。

现在，假设我们不只观察最后的总和，而是在每一步都记录随机系统的位置。

于是，原本的单个随机变量

\[
S_n=X_1+\cdots+X_n
\]

便成为了一整列随机变量：

\[
S_0,S_1,S_2,\ldots
\]

我们开始关注一个新的问题：

**随机性如何随着时间发展？**

这一问题将使概率论离开单个随机数字的世界，进入随机路径、随机过程，最终进入随机函数空间。

而在这条道路上，我们将遇到现代概率论中最重要的对象之一——Brownian motion（布朗运动）。

---

## 4.1 一位植物学家发现了一个数学问题

![母稿历史配图](../assets/images/07-01.img)

[配图原来源](https://commons.wikimedia.org/wiki/File%3APortrait_of_Robert_Brown_Wellcome_L0011784.jpg?utm_source=chatgpt.com)

**Robert Brown（1773—1858）**

苏格兰植物学家，曾参与澳大利亚植物考察，也研究植物的微观结构。

1827年，他在研究花粉中的微小颗粒时，观察到这些颗粒在液体中持续而不规则地移动。

在十九世纪初，人们已经能够借助显微镜观察大量肉眼无法看到的结构。

Brown 研究花粉时注意到，那些非常细小的颗粒，即使悬浮在看起来静止的水中，也会不停地颤动和改变位置。

最开始，这种运动似乎可能与生命活动有关。

但是，Brown 进一步研究了非生命物质中的微粒，发现类似运动并不局限于有生命的材料。

因此，它不能简单地归因于花粉具有生命。

Brown 在1827年开展这些观察，并于1828年发表相关报告。更早的人也观察过类似现象，因此 Brown 的重要贡献并不是“第一个看见颗粒运动”，而是系统研究了这种运动在不同微小颗粒中的普遍性。〔[31](#ref-turn360592search6), [32](#ref-turn360592search7)〕

![母稿历史配图](../assets/images/08-01.img)

![母稿历史配图](../assets/images/08-02.img)

![母稿历史配图](../assets/images/08-03.img)

![母稿历史配图](../assets/images/08-04.img)

![母稿历史配图](../assets/images/08-05.img)

![母稿历史配图](../assets/images/08-06.img)

![母稿历史配图](../assets/images/08-07.img)

[配图原来源](https://masterymind.co.uk/study-guides/physics-ocr-gcse-brownian-motion)

[配图原来源](https://web.mit.edu/course/10/10.50/www/diffuse2.html)

[配图原来源](https://www.heurema.com/POFQ-Perrin.htm)

[配图原来源](https://www.iitianacademy.com/cie-igcse-physics-0625-particle-model-study-notes/)

[配图原来源](https://www.academia.edu/4000202/_Evident_atoms_visuality_in_Jean_Perrin_s_Brownian_motion_research_Studies_in_the_History_and_Philosophy_of_Science_39_2008_312_322)

[配图原来源](https://www.slideserve.com/darrius/introduction-to-the-experiments-of-physics-407)

[配图原来源](https://www.mvp.cufo.cz/materialy/9.html)

现在，我们试着站在当时的观察者角度思考。

假如水是静止的，微粒也没有自主运动能力，为什么它仍然会不停移动？

如果存在某种看不见的微观作用在持续推动这些颗粒，那么大量无法直接观察的微小运动，能否产生宏观上可以测量的统计规律？

这个问题后来与分子运动论、原子存在的证据以及统计物理紧密联系起来。

1905年，Einstein 对悬浮微粒的扩散给出了定量理论；Smoluchowski 在1906年也提出了相关理论。Jean Perrin 随后的实验为相关预测提供了重要支持。〔[33](#ref-turn360592search3), [34](#ref-turn360592search4), [35](#ref-turn360592search5)〕

不过，还有一个值得注意的历史插曲。

在物理学的 Brownian motion 理论成熟之前，法国数学家 Louis Bachelier 已经在1900年的金融数学论文 *Théorie de la spéculation* 中研究过类似的连续随机价格模型。

真正严格地建立这一连续随机过程的概率论基础，则与 Norbert Wiener 在1920年代，尤其1923年的工作密切相关。

今天，我们把数学上的标准布朗运动也称为 Wiener process。〔[36](#ref-turn360592search8), [37](#ref-turn360592search0)〕

但这些是后来的历史。

为了真正理解这种过程是如何出现的，我们必须首先忘记连续时间、连续轨道甚至正态分布。

我们从一个小得不能再小的模型开始。

---

## 4.2 一个每一步只能向左或向右移动的粒子

想象一个粒子站在整数直线上。

它从原点出发。

每经过一个单位时间，就随机向右或者向左移动一个单位。

设

\[
\xi_1,\xi_2,\ldots
\]

是一列独立同分布随机变量，其中

\[
P(\xi_i=1)=P(\xi_i=-1)=\frac12.
\]

定义

\[
S_0=0,\qquad
S_n=\sum_{i=1}^n\xi_i.
\]

于是

\[
S_n
\]

表示粒子经过 \(n\) 步之后的位置。

这就是最简单的一维对称随机游走（simple symmetric random walk）。

我们已经掌握了研究这个模型所需要的大部分知识。

因为

\[
\mathbb E[\xi_i]=0,
\qquad
\operatorname{Var}(\xi_i)=1,
\]

所以

\[
\boxed{
\mathbb E[S_n]=0,\qquad
\operatorname{Var}(S_n)=n.
}
\]

于是

\[
\mathbb E[S_n^2]=n.
\]

如果采用均方根位移来衡量粒子离开原点的典型距离，那么

\[
\boxed{
\sqrt{\mathbb E[S_n^2]}=\sqrt n.
}
\]

这其实非常奇怪。

如果粒子始终向右走，那么经过 \(n\) 步之后，它与原点的距离是 \(n\)。

但当方向由独立且对称的随机机制决定时，它的均方根位移只有 \(\sqrt n\)。

随机游走与确定性运动的位移尺度

<div class="numeric-chart" data-chart="2"></div>

这说明随机运动的位移尺度，与确定性的匀速运动完全不同。

匀速运动满足

\[
x(t)\propto t.
\]

而在这种随机游走模型中，典型的位移大小满足

\[
|S_n|_{\mathrm{typical}}\propto\sqrt n.
\]

当然，随机粒子的具体轨迹可以有非常大的偏差。

\(\sqrt n\) 不是对每一条样本路径都成立的确定性界限。

它首先是由二阶矩给出的统计尺度。

但这个尺度将成为我们理解连续随机运动的关键。

## 4.3 如果时间越来越细，随机游走会变成什么？

现在我们提出一个思想实验。

假设我们不再希望粒子每一秒移动一次。

而是让它在一秒钟内移动 \(n\) 次。

也就是说，每次移动所占用的时间变成

\[
\Delta t=\frac1n.
\]

同时，我们把每一步的空间长度缩小到

\[
\Delta x=\frac1{\sqrt n}.
\]

这样，在时间 \(t\) 内，粒子大约走了 \(nt\) 步。

因此总位移的方差大约是

\[
nt\cdot\frac1n=t.
\]

这意味着：

即使单步位移越来越小，单位时间内的步数越来越多，总位移的方差仍然保持非平凡的大小。

我们既不会得到一个完全静止的粒子，也不会得到一个在有限时间内无限发散的系统。

现在定义

\[
\boxed{
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n},
\qquad t\ge0.
}
\]

这里 \(\lfloor nt\rfloor\) 表示不超过 \(nt\) 的最大整数。

这是经过时间与空间共同缩放之后的随机游走。

我们不妨观察一下它的变化。

<div class="experiment" data-widget="walk"></div>

离散随机游走的缩放实验。细分时间步数：16、32、64、128、256。示意模拟：每个步长为 \(1/\sqrt n\)，时间间隔为 \(1/n\)。为便于比较，使用同一条预先生成的随机增量序列的不同长度前缀；图形并非严格展示同一路径的逐级逼近。

当 \(n\) 增加时，原来的大幅跳跃变成越来越密集的小幅跳跃。

我们开始期待，在某种极限意义下，这个过程会形成连续的随机路径。

但这立即产生了两个数学问题。

首先，这样的极限是否真的存在？

其次，即使它存在，我们应该在哪种意义下理解整条随机路径的收敛？

此前的中心极限定理只能回答单个随机变量的分布如何收敛。

而现在，我们希望收敛的对象是整个函数：

\[
t\longmapsto W_n(t).
\]

这种区别将极其重要。

## 4.4 为什么空间尺度必须是时间尺度的平方根？

先不假设缩放指数是 \(1/2\)。

假设时间仍以 \(1/n\) 缩小，但空间步长取为

\[
n^{-\alpha}
\]

其中 \(\alpha>0\)。

定义

\[
W_n^{(\alpha)}(t)
=
n^{-\alpha}S_{\lfloor nt\rfloor}.
\]

因为

\[
\operatorname{Var}(S_{\lfloor nt\rfloor})=\lfloor nt\rfloor,
\]

所以

\[
\operatorname{Var}(W_n^{(\alpha)}(t))
=
n^{-2\alpha}\lfloor nt\rfloor.
\]

对固定的 \(t>0\)，其渐近尺度为

\[
t n^{1-2\alpha}.
\]

现在产生三种完全不同的情况。

如果

\[
\alpha>\frac12,
\]

那么

\[
\operatorname{Var}(W_n^{(\alpha)}(t))\to0.
\]

随机位移在概率意义下趋向零，我们得到的是退化极限。

如果

\[
\alpha=\frac12,
\]

那么

\[
\operatorname{Var}(W_n^{(\alpha)}(t))\to t.
\]

波动在极限中保留非零且有限的尺度。

如果

\[
\alpha<\frac12,
\]

方差趋于无穷。对于这个对称随机游走，由中心极限定理还能进一步证明，在任意固定 \(M>0\) 下，

\[
P(|W_n^{(\alpha)}(t)|\le M)\to0.
\]

因此，固定时刻的分布不会在实数轴上形成紧的概率分布族。

所以，只有

\[
\boxed{\alpha=\frac12}
\]

能够给我们所寻找的非退化扩散极限。

这是一种非常深刻的尺度选择。

\[
\boxed{
\text{时间尺度}\sim\varepsilon^2,
\qquad
\text{空间尺度}\sim\varepsilon.
}
\]

它不同于确定性匀速运动中的

\[
\text{空间尺度}\sim\text{时间尺度}.
\]

在随机扩散问题中，时间和空间遵循的是平方关系。

我们将来研究随机树的 scaling limit、CRT 以及其他连续随机几何对象时，会再次遇到这样的思想：

**找到正确的缩放指数，往往就是发现极限对象的第一步。**

不过，那个指数究竟是多少，取决于模型中的随机结构。并不是所有随机系统都必须具有 Brownian motion 的 \(1/2\) 指数。

---

## 4.5 中心极限定理只能看见一个时刻

现在回到

\[
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n}.
\]

先固定一个时刻 \(t>0\)。

因为

\[
S_{\lfloor nt\rfloor}
=
\xi_1+\cdots+\xi_{\lfloor nt\rfloor},
\]

由中心极限定理，

\[
\frac{S_{\lfloor nt\rfloor}}{\sqrt{\lfloor nt\rfloor}}
\xrightarrow d N(0,1).
\]

所以

\[
W_n(t)
=
\frac{S_{\lfloor nt\rfloor}}{\sqrt{\lfloor nt\rfloor}}
\sqrt{\frac{\lfloor nt\rfloor}{n}}.
\]

由于

\[
\frac{\lfloor nt\rfloor}{n}\to t,
\]

我们得到

\[
\boxed{
W_n(t)\xrightarrow d N(0,t).
}
\]

于是我们发现，假如连续时间极限存在，那么它在每个固定时刻 \(t\) 的位置，应该具有均值为0、方差为 \(t\) 的正态分布。

因此，它的密度应当是

\[
\boxed{
p_t(x)
=
\frac1{\sqrt{2\pi t}}
\exp\left(-\frac{x^2}{2t}\right).
}
\]

但是请注意：

这个结论只描述了一个固定时刻。

它并没有告诉我们 \(t=1\) 与 \(t=2\) 的位置之间有什么关系，也没有告诉我们粒子在两个时刻之间会经过哪里。

一个随机过程，远远不只是每个时刻各自的概率分布。

### 4.5.1 为什么知道每个时刻的分布还不够？

考虑两个随机过程。

第一个过程是

\[
X_t=\sqrt t\,Z,
\]

其中

\[
Z\sim N(0,1).
\]

于是对于每个 \(t>0\)，

\[
X_t\sim N(0,t).
\]

第二个过程暂时记为 \(B_t\)，我们希望它也满足

\[
B_t\sim N(0,t).
\]

也就是说，两个过程在每一个固定时刻都具有相同的分布。

然而，对第一个过程，

\[
X_s=\sqrt{\frac st}X_t
\qquad(0<s<t).
\]

只要知道了一个非零时刻的位置，我们就能确定其他所有时刻的位置。

它的整条路径只是一条形如

\[
t\longmapsto \sqrt t\,z
\]

的确定函数，只不过系数 \(z\) 是随机的。

因此

\[
\operatorname{Cov}(X_s,X_t)=\sqrt{st}.
\]

而我们期待的 Brownian motion 将满足

\[
\operatorname{Cov}(B_s,B_t)=\min(s,t).
\]

两者显然不同。

尤其当 \(0<s<t\) 时，

\[
\sqrt{st}\ne s.
\]

所以，两个随机过程可以在每一个时刻具有完全相同的分布，却具有完全不同的时间结构。

**研究随机过程时，我们必须理解不同时间之间的联合分布，而不只是每个时间的边际分布。**

### 4.5.2 从一个时刻走向多个时刻

现在选定时间

\[
0=t_0<t_1<\cdots<t_m.
\]

我们研究随机向量

\[
(W_n(t_1),\ldots,W_n(t_m)).
\]

为了理解它，最自然的办法不是分别研究每个坐标，而是研究相邻时间之间的增量：

\[
\Delta_{n,j}=W_n(t_j)-W_n(t_{j-1}).
\]

对于这里定义的阶梯过程，这些增量精确等于不同时间区间上随机步长的和；若改用线性插值版本，才需控制边界项（见附录 F）。

例如，

\[
\Delta_{n,j}
=
\frac1{\sqrt n}
\sum_{k=\lfloor nt_{j-1}\rfloor+1}^{\lfloor nt_j\rfloor}\xi_k.
\]

因为不同区间使用互不重叠的随机变量，它们相互独立。

每个增量又满足中心极限定理：

\[
\Delta_{n,j}
\xrightarrow d
N(0,t_j-t_{j-1}).
\]

所以，整个增量向量应当收敛到一组相互独立的正态随机变量：

\[
(Z_1,\ldots,Z_m),
\]

其中

\[
Z_j\sim N(0,t_j-t_{j-1}).
\]

这一联合收敛可以通过特征函数严格证明：由于各增量独立，它们的联合特征函数可分解为乘积，而每个因子都收敛到对应正态分布的特征函数。

随后利用

\[
W_n(t_j)=\sum_{r=1}^j\Delta_{n,r},
\]

得到有限维分布的联合收敛。

因此我们找到了连续极限应当满足的结构：

\[
\boxed{
B_{t_j}-B_{t_{j-1}}
\sim N(0,t_j-t_{j-1}),
}
\]

并且在不重叠时间区间上的增量相互独立。

这已经比“每个时刻都服从正态分布”强得多。

### 4.5.3 协方差结构自然出现

由

\[
B_t=B_s+(B_t-B_s),
\qquad s<t,
\]

以及增量独立性，

\[
\begin{aligned}
\mathbb E[B_sB_t]
&=\mathbb E[B_s^2]
+\mathbb E[B_s(B_t-B_s)]\\
&=s+0\\
&=s.
\end{aligned}
\]

所以

\[
\boxed{
\operatorname{Cov}(B_s,B_t)=\min(s,t).
}
\]

我们得到了一种十分特殊的协方差核：

\[
\boxed{
K(s,t)=\min(s,t).
}
\]

它将整个过程不同时间之间的二阶关系编码在同一个函数之中。

更加重要的是，当过程是 Gaussian process 时，这个协方差核与均值函数一起，能够决定所有有限维联合分布。

于是，我们似乎已经找到 Brownian motion 的全部有限维概率结构。

但这里还隐藏着一个巨大的逻辑漏洞。

---

## 4.6 知道所有有限维分布，是否就等于构造出随机路径？

假设我们已经知道，对任意有限组时间

\[
t_1,\ldots,t_m,
\]

随机向量

\[
(B_{t_1},\ldots,B_{t_m})
\]

应当服从怎样的联合分布。

这是否已经意味着存在一条连续的随机路径

\[
t\longmapsto B_t?
\]

不一定。

首先，我们可以利用一致的有限维分布，通过概率测度的扩张定理构造一个随机过程。

但是，这种构造本身并不自动保证它的样本路径连续。

更进一步，即使两个过程在所有有限组时间上的联合分布都相同，也不能不加限定地认为它们具有相同的路径性质。

这是从随机变量转向随机过程时，一个极其容易被忽略的陷阱。

### 4.6.1 一个简单但致命的反例

令 \(U\sim\operatorname{Uniform}(0,1)\)，定义

\[
X_t=\mathbf1_{\{t=U\}},
\qquad 0\le t\le1.
\]

对每个固定的 \(t\)，

\[
P(X_t=1)=P(U=t)=0.
\]

所以

\[
X_t=0\quad\text{a.s.}
\]

对任意有限组确定时刻 \(t_1,\ldots,t_m\)，我们同样有

\[
P(X_{t_1}=\cdots=X_{t_m}=0)=1.
\]

因此，过程 \((X_t)\) 的所有有限维分布，都与恒等于零的过程

\[
Y_t\equiv0
\]

完全相同。

然而，观察完整路径时，差异巨大。

对于每一个 \(U\in(0,1)\)，函数

\[
t\longmapsto X_t
\]

在 \(t=U\) 处突然跳到1，其他地方为0。

因此，这条路径是不连续的。

而 \(Y_t\equiv0\) 的路径显然处处连续。

我们甚至有

\[
\sup_{0\le t\le1}X_t=1
\quad\text{a.s.},
\]

但

\[
\sup_{0\le t\le1}Y_t=0.
\]

请注意这件事有多么深刻：

\[
\boxed{
\text{所有有限维分布相同}
\not\implies
\text{路径性质相同}.
}
\]

这不是说有限维分布没有用。

恰恰相反，它们是描述过程的必要组成部分。

但如果我们希望研究连续路径，还必须说明自己在什么样的函数空间中构造随机对象，并且如何控制不同时间之间的波动。

否则，连续性可能只是我们在纸上画出的一条平滑曲线，而不是严格证明过的数学性质。

### 4.6.2 另一个问题：有限维收敛不是路径收敛

即使我们已经有一系列连续函数，也可能出现每个固定时刻都收敛、整条路径却并不收敛的情况。

例如，考虑定义在 \([0,1]\) 上的函数

\[
f_n(t)=\max\left\{1-2n\left|t-\frac1n\right|,0\right\}.
\]

当 \(n\) 越来越大时，这个三角形尖峰逐渐向0靠近，宽度逐渐缩小。

对于任何固定的 \(t\in[0,1]\)，

\[
f_n(t)\to0.
\]

但对每个足够大的 \(n\)，

\[
\sup_{0\le t\le1}|f_n(t)|=1.
\]

所以它们根本没有一致收敛到零函数。

这就是一个非常直观的警告：

研究路径时，只检查每个确定时刻发生什么是不够的。某些越来越短、越来越难在固定时刻捕捉的异常波动，仍然可能阻止整个函数的收敛。

因此，对于随机过程，我们需要一套新的收敛理论。

---

## 4.7 Donsker 的突破：中心极限定理不应该只属于随机变量

> 校订补注：本章调用的深层定理及完整证明范围列于附录 G；有限维联合极限补证见附录 F。

第三章的中心极限定理告诉我们

\[
\frac{S_n}{\sqrt n}\xrightarrow d N(0,1).
\]

而我们现在希望证明的是

\[
\left(
\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\right)_{0\le t\le1}
\]

作为一整个随机过程，能够收敛到 Brownian motion。

这正是后来所谓的函数型中心极限定理（functional central limit theorem）的核心思想。

在这一历史发展中，Monroe Donsker 于1951年发表的 *An Invariance Principle for Certain Probability Limit Theorems* 是一个重要里程碑。

这里需要与前面的历史区分：Donsker 的工作发生在 Wiener 对 Brownian motion 进行严格构造之后。我们现在采用的是从随机游走极限重新理解 Brownian motion 的现代数学路线，并不是说历史上先有 Donsker 定理、然后才发明 Brownian motion。〔[38](#ref-turn288123search2), [39](#ref-turn288123search41)〕

### 4.7.1 首先把阶梯路径变成连续路径

前面定义的

\[
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\]

是一条阶梯函数。

每个网格时刻，它都会发生大小为 \(1/\sqrt n\) 的跳跃。

因此，对任何固定的 \(n\)，它都不是连续函数。

如果我们想在连续函数空间中研究它，最自然的做法是进行线性插值。

设

\[
k=\lfloor nt\rfloor,\qquad r=nt-k.
\]

定义

\[
\boxed{
\widetilde W_n(t)
=
\frac{(1-r)S_k+rS_{k+1}}{\sqrt n},
\quad0\le t<1,
}
\]

并令

\[
\widetilde W_n(1)=\frac{S_n}{\sqrt n}.
\]

现在，每条 \(\widetilde W_n\) 路径都是连续的。

并且

\[
\sup_{0\le t\le1}
|\widetilde W_n(t)-W_n(t)|
\le\frac1{\sqrt n}.
\]

所以两种表示之间的差异在一致范数下趋于零。

但注意：线性插值只保证我们能够把这些过程放进连续函数空间。

它并不自动证明极限存在。

### 4.7.2 我们究竟要在哪个空间中收敛？

考虑

\[
C([0,1])
\]

即定义在 \([0,1]\) 上的所有实值连续函数组成的空间。

赋予它一致范数：

\[
\|f\|_\infty
=
\sup_{0\le t\le1}|f(t)|.
\]

于是每一个 \(\widetilde W_n\) 都可以看作一个取值于 \(C([0,1])\) 的随机元素。

这与前面研究的单个随机变量没有本质上的范畴区别。

只是随机变量现在不再取值于 \(\mathbb R\)，而是取值于一个无限维函数空间。

我们希望证明：

\[
\boxed{
\widetilde W_n\xrightarrow d B
\quad\text{in }C([0,1]).
}
\]

这里的依分布收敛可以用有界连续函数泛函来表述：

对于任意有界连续映射

\[
F:C([0,1])\longrightarrow\mathbb R,
\]

都有

\[
\mathbb E[F(\widetilde W_n)]
\longrightarrow
\mathbb E[F(B)].
\]

这不再只是某个时间点上的概率收敛。

它允许我们讨论整条路径的函数，例如

\[
F(f)=\max_{0\le t\le1}f(t).
\]

因为最大值泛函在一致范数下是连续的：

\[
|\max f-\max g|
\le\|f-g\|_\infty.
\]

所以一旦我们证明了函数空间中的弱收敛，便能通过连续映射定理得到关于最大值的极限定理。

这就是函数型中心极限定理比普通中心极限定理强大得多的原因。

### 4.7.3 有限维分布还缺少什么？

我们在4.5节已经证明了有限维分布的收敛。

但仅有这一点不够。

我们还需要排除那种越来越尖锐、越来越难控制的路径波动。

现代概率论用一个概念处理这件事：

**紧性（tightness）。**

直观而言，我们希望随机路径的大部分概率质量，不会逃向函数空间中越来越不规则、无法形成收敛子序列的区域。

在 \(C([0,1])\) 中，Arzelà–Ascoli 定理告诉我们：一族函数要具有相对紧性，除了在某点有界，还需要具有一致的等度连续性。

因此，随机过程的紧性，可以通过控制小时间间隔内的振荡来证明。

例如，我们希望获得某种与 \(n\) 无关的矩估计：

\[
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le C|t-s|^2.
\]

对于当前的对称随机游走，这样的估计确实成立。

我们甚至可以直接证明它。

把插值过程在 \([s,t]\) 上的增量写成

\[
\widetilde W_n(t)-\widetilde W_n(s)
=
\frac1{\sqrt n}\sum_j a_j\xi_j,
\]

其中系数 \(a_j\in[0,1]\)，并且

\[
\sum_j a_j=n(t-s).
\]

由于 \(\xi_j\) 是独立对称的 \(\pm1\) 随机变量，我们可以展开四次矩：

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
=
3\left(\sum_j a_j^2\right)^2
-
2\sum_j a_j^4.
\]

所以

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
\le
3\left(\sum_j a_j^2\right)^2.
\]

又因为 \(0\le a_j\le1\)，

\[
\sum_j a_j^2
\le\sum_j a_j
=n(t-s).
\]

由此得到

\[
\boxed{
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le3|t-s|^2.
}
\]

这个估计对于所有 \(n\) 都成立。

它给出了对整族随机路径的统一振荡控制。

利用相应的 Kolmogorov 紧性准则，结合

\[
\widetilde W_n(0)=0,
\]

便可以证明这些过程在 \(C([0,1])\) 中的分布是紧的。

最后，把紧性与有限维分布收敛结合起来，就得到了函数型中心极限定理。

\[
\boxed{
\widetilde W_n\Longrightarrow B
\quad\text{in }C([0,1]).
}
\]

这就是 Donsker 不变性原理在我们这个模型中的一个具体版本。

对于独立同分布、均值为0且方差为1的更一般的随机增量，Donsker 定理仍然成立。仅有有限二阶矩时，上面简便的四次矩证明未必能直接使用，需要更一般的紧性论证。

完整的函数型收敛理论与证明可以参考 [Encyclopedia of Mathematics: Donsker invariance principle](https://encyclopediaofmath.org/wiki/Donsker_invariance_principle)。〔[38](#ref-turn288123search2), [40](#ref-turn288123search39), [39](#ref-turn288123search41)〕

这里，我们终于能够说：

**Brownian motion 不只是随机游走某个时刻的正态极限，它可以作为整条随机游走路径的分布极限出现。**

这是一种比第三章的中心极限定理更深的普遍性。

不同的微观随机机制，在合适的时空缩放下，不仅可以拥有相同的最终分布，还可以拥有相同的连续随机过程极限。

---

## 4.8 我们终于可以定义 Brownian motion 了

经过前面的研究，现在才是正式引入定义的恰当时机。

**定义：标准 Brownian motion**

一个实值随机过程

\[
B=(B_t)_{t\ge0}
\]

称为标准 Brownian motion，如果：

1. \(B_0=0\) 几乎必然成立；
2. 对任意 \(0\le t_0<t_1<\cdots<t_m\)，增量
\[
B_{t_1}-B_{t_0},\ldots,B_{t_m}-B_{t_{m-1}}
\]
相互独立；
3. 对任意 \(0\le s<t\)，
\[
B_t-B_s\sim N(0,t-s);
\]
4. 几乎所有样本路径 \(t\mapsto B_t(\omega)\) 都连续。

现在这个定义不再突兀。

每一条要求，都是我们为了构造随机游走的连续极限而逐渐发现的。

第一条规定初始状态。

第二条保留了原先随机游走在不同时间区间内的独立性。

第三条是中心极限定理产生的 Gaussian 增量结构。

第四条则需要在函数空间层面证明，不能单靠固定时刻的分布来保证。

### 4.8.1 连续的 Brownian motion 真的存在吗？

我们刚才通过随机游走的函数型极限定理，已经找到了一条构造思路。

但还有另一种非常重要的方法。

我们可以先从协方差核出发：

\[
K(s,t)=\min(s,t).
\]

对任意有限个时刻 \(t_1,\ldots,t_m\)，矩阵

\[
\left(K(t_i,t_j)\right)_{i,j=1}^m
\]

是非负定的。

事实上，利用

\[
K(s,t)=\int_0^\infty
\mathbf1_{\{u\le s\}}\mathbf1_{\{u\le t\}}\,du,
\]

我们有

\[
\begin{aligned}
\sum_{i,j=1}^m a_ia_jK(t_i,t_j)
&=\int_0^\infty
\left(\sum_{i=1}^m a_i\mathbf1_{\{u\le t_i\}}\right)^2du\\
&\ge0.
\end{aligned}
\]

因此，这些矩阵可以作为中心 Gaussian 向量的协方差矩阵。

它们还满足删除、重排时间坐标时所要求的一致性条件。

所以，Kolmogorov 扩张定理允许我们构造一个具有这些有限维分布的 Gaussian process。

但还有最后一步。

我们需要证明它存在连续的修正版本（continuous modification）。

因为

\[
B_t-B_s\sim N(0,t-s),
\]

所以

\[
\mathbb E[|B_t-B_s|^4]
=
3|t-s|^2.
\]

这正好满足 Kolmogorov 连续性定理所要求的一类矩条件。

因此，可以构造一个具有连续样本路径的版本。

至此，我们才真正得到了连续时间的 Brownian motion。〔[41](#ref-turn288123search36), [42](#ref-turn288123search38)〕

这条证明路线同样展现了现代概率论的层次结构：

\[
\boxed{
\begin{gathered}
\text{一致的有限维概率分布}\\
\Downarrow\\
\text{随机过程的存在}\\
\Downarrow\\
\text{增量矩估计}\\
\Downarrow\\
\text{连续路径版本的存在}
\end{gathered}
}
\]

这几步不是同一个定理，也不能随意省略。

### 4.8.2 Wiener measure：整个函数也可以是随机变量

现在我们已经知道，Brownian motion 的样本路径几乎必然属于

\[
C([0,1]).
\]

那么最自然的想法就是：干脆直接把连续函数当作概率空间中的结果。

令

\[
\Omega=C_0([0,1])
=
\{f\in C([0,1]):f(0)=0\}.
\]

配备一致范数产生的 Borel \(\sigma\)-代数。

我们希望在这个函数空间上建立一个概率测度 \(\mathbb W\)，使坐标映射

\[
B_t(\omega)=\omega(t)
\]

成为标准 Brownian motion。

这个测度就称为 Wiener measure。

于是，我们能够对整个函数空间中的事件赋予概率。

例如：

\[
A=\left\{
\omega:\sup_{0\le t\le1}\omega(t)\ge1
\right\}.
\]

这不再是一个关于单个时刻的事件。

它研究的是整条路径是否曾经触及某个高度。

我们可以写：

\[
\mathbb W(A)
=
P\left(\sup_{0\le t\le1}B_t\ge1\right).
\]

请注意，这正好回应了第一章末尾留下的问题。

当我们不能再靠计数描述结果时，应该怎么办？

现在，我们面对的样本空间甚至不是一个区间，而是一个无限维函数空间。

概率依然可以定义，因为概率的真正基础不再是“有利结果数除以总结果数”，而是满足适当公理的测度。

在这里，随机变量可以是一个实数，也可以是一条连续函数，甚至可以是更加复杂的随机几何对象。

**现代概率论开始摆脱对随机结果具体形式的依赖。**

而这正是我们以后研究随机树和 CRT 必不可少的基础。

---

## 4.9 从随机游走到热方程：为什么随机运动会产生确定性的偏微分方程？

到目前为止，我们沿着随机路径的路线，建立了 Brownian motion。

但数学史上，还有另外一条重要路线通向同一个对象。

那就是热传导与扩散。

这一联系值得认真推导，因为它揭示了随机世界与确定性微分方程之间极其深刻的关系。

### 4.9.1 从离散随机游走重新开始

假设一个粒子在空间网格上移动，每次向左或向右跳跃 \(\Delta x\)，每次跳跃需要 \(\Delta t\) 时间。

设

\[
p(x,t)
\]

表示粒子在时间 \(t\) 位于网格点 \(x\) 的概率质量。

由于粒子只能从左右相邻位置到达 \(x\)，所以

\[
p(x,t+\Delta t)
=
\frac12p(x-\Delta x,t)
+
\frac12p(x+\Delta x,t).
\]

移项得到

\[
\begin{aligned}
&p(x,t+\Delta t)-p(x,t)\\
&=\frac12\left[
p(x-\Delta x,t)-2p(x,t)+p(x+\Delta x,t)
\right].
\end{aligned}
\]

两侧除以 \(\Delta t\)：

\[
\begin{aligned}
\frac{p(x,t+\Delta t)-p(x,t)}{\Delta t}
=
\frac{(\Delta x)^2}{2\Delta t}
\frac{
p(x-\Delta x,t)-2p(x,t)+p(x+\Delta x,t)
}{(\Delta x)^2}.
\end{aligned}
\]

现在观察这个式子。

左边具有时间方向的差商结构：

\[
\frac{\partial p}{\partial t}.
\]

右边则具有空间方向的二阶差商结构：

\[
\frac{\partial^2p}{\partial x^2}.
\]

如果让网格同时趋于零，并保持

\[
\frac{(\Delta x)^2}{2\Delta t}\to D,
\]

那么形式上，我们将得到

\[
\boxed{
\frac{\partial p}{\partial t}
=
D\frac{\partial^2p}{\partial x^2}.
}
\]

这就是一维扩散方程，也称为热方程。

这里的推导属于连续极限的形式推导。要严格证明离散概率质量适当归一化后的极限确实满足该偏微分方程，还需要使用局部极限定理、半群理论或其他收敛方法。〔[43](#ref-turn516523search36), [44](#ref-turn516523search1)〕

但是，它已经向我们展示了一种难以忽略的数学联系：

**一系列完全随机的微小运动，在概率分布层面上，竟然能够产生一个确定性的偏微分方程。**

### 4.9.2 为什么热方程的解又是正态密度？

对于标准 Brownian motion，

\[
B_t\sim N(0,t).
\]

所以位置密度为

\[
p_t(x)=
\frac1{\sqrt{2\pi t}}
e^{-x^2/(2t)}.
\]

直接对它求偏导，可以验证

\[
\boxed{
\frac{\partial p_t}{\partial t}
=
\frac12\frac{\partial^2p_t}{\partial x^2}.
}
\]

一般扩散系数为 \(D\) 时，密度为

\[
\boxed{
p_t(x)
=
\frac1{\sqrt{4\pi Dt}}
e^{-x^2/(4Dt)}.
}
\]

其方差为

\[
\operatorname{Var}(X_t)=2Dt.
\]

因此

\[
\boxed{
\mathbb E[(X_t-X_0)^2]=2Dt
}
\]

对于从原点出发、无漂移的一维扩散模型成立。

这正是 Einstein 1905年 Brownian motion 理论中与实验联系紧密的均方位移规律。

在适当的物理条件下，扩散系数还可以联系温度、流体黏度和粒子半径；这使得宏观可观测的随机位移能够用于推断微观物质的性质。〔[35](#ref-turn360592search5), [31](#ref-turn360592search6)〕

### 4.9.3 一个统一：随机路径与确定性演化

现在出现了两种完全不同的描述方式。

第一种是随机路径：

\[
t\longmapsto B_t(\omega).
\]

每一个 \(\omega\) 都对应一条不同的随机轨迹。

第二种是概率密度：

\[
(t,x)\longmapsto p_t(x).
\]

这个函数则由确定性的热方程控制。

对于足够规则的函数 \(f\)，定义

\[
P_tf(x)
=
\mathbb E[f(x+B_t)].
\]

由于 Brownian motion 具有独立且平稳的增量，

\[
P_{t+s}f=P_t(P_sf).
\]

所以 \((P_t)_{t\ge0}\) 形成一个 Markov 半群。

其无穷小生成元满足

\[
\lim_{h\downarrow0}
\frac{P_hf(x)-f(x)}{h}
=
\frac12f''(x),
\]

对例如 \(f\in C_c^\infty(\mathbb R)\) 成立。

因此

\[
\boxed{
L=\frac12\frac{d^2}{dx^2}.
}
\]

而相应的演化方程正是

\[
\frac{\partial u}{\partial t}=Lu.
\]

我们得到了一条极其重要的统一关系：

\[
\boxed{
\text{随机过程}
\longleftrightarrow
\text{Markov 半群}
\longleftrightarrow
\text{偏微分方程}.
}
\]

这不是简单的符号对应。

它意味着，我们可以用随机运动解释偏微分方程，也可以用偏微分方程研究随机过程的概率分布。

将来在随机微积分、Feynman–Kac 公式和随机微分方程中，我们会不断发现这条联系的重要性。

---

## 4.10 连续，却无法求导：Brownian motion 的另一个悖论

现在，我们已经真正构造出了 Brownian motion。

它具有连续样本路径：

\[
t\longmapsto B_t(\omega).
\]

乍看之下，既然粒子的位置随时间连续变化，我们似乎应该能够定义它的瞬时速度：

\[
v(t)=\lim_{h\to0}\frac{B_{t+h}-B_t}{h}.
\]

但事情没有这么简单。

根据 Brownian motion 的定义，

\[
B_{t+h}-B_t\sim N(0,h)
\]

对于 \(h>0\)。

因此

\[
\frac{B_{t+h}-B_t}{h}
\sim N\left(0,\frac1h\right).
\]

当 \(h\downarrow0\) 时，这个差商的方差反而趋于无穷。

这意味着差商在任何有限数值附近都不会越来越集中。

事实上，对于任意固定 \(M>0\)，

\[
P\left(
\left|\frac{B_{t+h}-B_t}{h}\right|\le M
\right)\longrightarrow0.
\]

因此，这些差商甚至不可能依概率收敛到一个有限的随机变量。

但这还不是最强的结论。

Brownian motion 的样本路径事实上几乎必然**处处不可导**。

这是一个令人惊讶的事实：

\[
\boxed{
\text{样本路径连续}
\quad\text{但几乎必然处处不可导}.
}
\]

我们在微积分中曾经习惯一种直觉：

连续函数代表平滑的运动，而速度应当是对位置求导得到的。

Brownian motion 则彻底打破了这种直觉。

它是一种数学上严格存在的连续运动，但其路径粗糙到无法使用普通微分来描述。关于其轨道正则性的证明和历史发展，可参见 Brownian motion 的现代概率论教材。〔[45](#ref-turn516523search41), [46](#ref-turn288123search37)〕

不过，我们还可以用一个更加结构性的量，理解这种粗糙性。

### 4.10.1 一条路径究竟有多粗糙？

在区间 \([0,T]\) 上，考虑二等分网格

\[
t_k=\frac{kT}{2^m},
\qquad k=0,\ldots,2^m.
\]

定义平方增量之和：

\[
Q_m=
\sum_{k=0}^{2^m-1}
(B_{t_{k+1}}-B_{t_k})^2.
\]

由于各个增量相互独立，且

\[
B_{t_{k+1}}-B_{t_k}
\sim N\left(0,\frac{T}{2^m}\right),
\]

所以

\[
\mathbb E[Q_m]
=
2^m\cdot\frac{T}{2^m}
=T.
\]

而一个均值为0、方差为 \(v\) 的正态随机变量 \(Z\)，满足

\[
\operatorname{Var}(Z^2)=2v^2.
\]

因此

\[
\begin{aligned}
\operatorname{Var}(Q_m)
&=
2^m\cdot2\left(\frac{T}{2^m}\right)^2\\
&=\frac{2T^2}{2^m}.
\end{aligned}
\]

所以

\[
Q_m\longrightarrow T
\]

在 \(L^2\) 中成立。

更进一步，由 Chebyshev 不等式，

\[
P(|Q_m-T|>\varepsilon)
\le
\frac{2T^2}{\varepsilon^2 2^m}.
\]

右侧关于 \(m\) 可求和。

利用 Borel–Cantelli 引理，可以得到

\[
\boxed{
Q_m\xrightarrow{\mathrm{a.s.}}T.
}
\]

这就是 Brownian motion 的平方变差（quadratic variation）性质，在二进网格上的一种严格表述。

我们通常记作

\[
\boxed{[B]_T=T.}
\]

### 4.10.2 为什么这与普通光滑函数完全不同？

假设 \(f:[0,T]\to\mathbb R\) 是一个 continuously differentiable 函数。

那么由均值定理，

\[
|f(t_{k+1})-f(t_k)|
\le M(t_{k+1}-t_k)
\]

其中

\[
M=\sup_{0\le t\le T}|f'(t)|<\infty.
\]

因此

\[
\begin{aligned}
\sum_k(f(t_{k+1})-f(t_k))^2
&\le
M^2\sum_k(t_{k+1}-t_k)^2\\
&=M^2\frac{T^2}{2^m}\\
&\longrightarrow0.
\end{aligned}
\]

所以光滑函数沿越来越细网格的平方增量之和趋于零。

但是 Brownian motion 却满足

\[
\sum_k(B_{t_{k+1}}-B_{t_k})^2
\longrightarrow T.
\]

也就是说：

\[
\boxed{
\begin{aligned}
\text{光滑路径：}&\quad [f]_T=0,\\
\text{Brownian 路径：}&\quad [B]_T=T.
\end{aligned}
}
\]

这件事比“路径有些不平滑”更加深刻。

它表明，Brownian motion 拥有一种普通微积分无法忽略的二阶累积效应。

### 4.10.3 为什么随机微积分必须重新发明？

在普通微积分中，我们经常忽略二阶无穷小。

因为如果

\[
dx=O(dt),
\]

那么

\[
(dx)^2=O(dt^2),
\]

在除以 \(dt\) 后趋于零。

但对于 Brownian motion，典型增量具有

\[
dB\sim O(\sqrt{dt})
\]

这样的尺度。

于是

\[
(dB)^2\sim O(dt).
\]

这意味着平方增量的累积贡献，与一阶时间增量处于相同数量级。

因此，我们不能再像普通微积分那样忽略它。

这就是后来 Itô calculus 中会出现形式关系

\[
\boxed{(dB_t)^2=dt}
\]

的根本原因。

这不是把 \(dB_t\) 当作普通实数微分进行的代数运算，而是平方变差结构在随机积分理论中的一种简洁记号。

例如，普通微积分可能让我们期待

\[
d(B_t^2)=2B_t\,dB_t.
\]

但 Itô 公式实际给出

\[
\boxed{
d(B_t^2)=2B_t\,dB_t+dt.
}
\]

那个额外的 \(dt\)，正是由 Brownian motion 的非零平方变差产生的。

我们现在还没有严格建立随机积分，因此这里只把它作为后续理论的预告。

但这已经让我们看到了概率论中一种非常重要的发展模式：

**不是因为数学家想研究更复杂的公式，才创造新的积分理论；而是因为新的随机对象根本无法被原有的微积分完整描述。**

---

## 4.11 为什么随机路径比随机变量包含更多的信息？

到目前为止，我们已经知道：

\[
B_T\sim N(0,T).
\]

这能够告诉我们时间 \(T\) 时粒子在哪里。

但是，如果我们想问：

在时间 \(T\) 之前，粒子是否曾经到达某个高度 \(a>0\)？

这就完全是另外一个问题。

定义首次到达时间

\[
\tau_a=\inf\{t\ge0:B_t=a\}.
\]

我们真正关心的是

\[
P(\tau_a\le T).
\]

这个事件依赖整条路径，而不仅仅是最终位置 \(B_T\)。

例如，粒子可能先到达高度 \(a\)，随后又回到原点附近。

如果我们只观察最终位置，就完全无法知道这件事是否发生。

但 Brownian motion 的独特对称性，让我们能够计算这个路径事件。

### 4.11.1 反射原理

考虑所有在时间 \(T\) 之前达到高度 \(a\)，但最终落在 \(a\) 以下的路径。

对于每一条这样的路径，我们在它首次达到高度 \(a\) 的时刻之后，将后续部分关于水平线 \(y=a\) 反射。

利用 Brownian motion 在首次到达时刻之后的强 Markov 性质，以及增量的对称性，这种反射建立了相应路径事件之间的概率对应。

于是得到反射原理（reflection principle）：

\[
\boxed{
P\left(\sup_{0\le t\le T}B_t\ge a\right)
=
2P(B_T\ge a).
}
\]

因为

\[
B_T\sim N(0,T),
\]

所以

\[
P(B_T\ge a)
=
1-\Phi\left(\frac a{\sqrt T}\right),
\]

其中 \(\Phi\) 是标准正态分布函数。

因此

\[
\boxed{
P(\tau_a\le T)
=
2\left[
1-\Phi\left(\frac a{\sqrt T}\right)
\right].
}
\]

这个公式非常值得注意。

我们原先通过中心极限定理得到的是某个固定时刻的 Gaussian 分布。

但通过路径对称性，我们又能用它计算首次到达事件的概率。

甚至可以进一步求出首次到达时间的密度：

\[
\boxed{
f_{\tau_a}(t)
=
\frac{a}{\sqrt{2\pi t^3}}
\exp\left(-\frac{a^2}{2t}\right),
\qquad t>0.
}
\]

有趣的是，

\[
P(\tau_a<\infty)=1,
\]

但

\[
\mathbb E[\tau_a]=\infty.
\]

也就是说，粒子几乎必然最终会达到任意固定的正高度，但达到这一高度的期望等待时间却是无穷大。

这再次提醒我们：

几乎必然发生，并不意味着等待时间具有有限期望。

从离散随机游走的首次到达问题，到连续 Brownian motion 的反射原理，概率论开始发展出研究整条随机轨迹的理论。

---

## 4.12 为什么 Brownian motion 对未来的概率论如此重要？

现在我们已经从一个非常简单的随机游走中，逐步发展出了：

- 无限维函数空间上的概率测度；
- 连续 Gaussian process；
- 函数型中心极限定理；
- Markov 半群与热方程；
- 连续但不可导的随机路径；
- 平方变差与随机微积分的必要性；
- 首次到达时间与路径事件。

这些概念看起来已经横跨概率论、泛函分析、偏微分方程和微分几何。

但它们并不是偶然堆积在一起的。

它们都围绕一个核心问题展开：

**怎样理解一个在时间中不断产生新随机性的对象？**

Brownian motion 提供了这个问题的一个特别精确、特别丰富的数学模型。

更重要的是，它让我们第一次真正学会将一个随机函数视为概率空间中的基本对象。

而这一点具有远远超出 Brownian motion 本身的意义。

### 4.12.1 从 Brownian path 到随机树

我们先提前看一个将来会再次出现的构造。

假设我们有一个非负连续函数

\[
e:[0,1]\to[0,\infty)
\]

满足

\[
e(0)=e(1)=0.
\]

例如，\(e\) 可以是一条 Brownian excursion。

我们可以定义

\[
m_e(s,t)
=
\inf_{u\in[s\wedge t,s\vee t]}e(u).
\]

再定义

\[
\boxed{
d_e(s,t)
=
e(s)+e(t)-2m_e(s,t).
}
\]

这个表达式非常值得观察。

它描述了两个时刻对应高度的总和，减去二者之间所经过的最低共同高度的两倍。

如果我们把连续函数的上升和下降解释成一棵树的深度优先遍历，那么这个表达式就具有树上距离的含义。

通过识别满足

\[
d_e(s,t)=0
\]

的时刻，我们能够构造一个商空间。

对于适当的 excursion，这个商空间具有实树（real tree）的结构。

当 \(e\) 是合适归一化的 Brownian excursion 时，便与 Brownian CRT 的经典构造联系起来；具体的尺度因子取决于采用的归一化约定。

从连续函数到树形几何的思想示意

<svg viewBox="0 0 340 185" width="100%" xmlns="http://www.w3.org/2000/svg">
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130 L325 130 L15 130 Z" fill="#168782" opacity="0.12"/>
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130" fill="none" stroke="#168782" stroke-width="2.6" stroke-linecap="round"/>
    <line x1="15" y1="130" x2="325" y2="130" stroke="currentColor" opacity="0.4"/>
    <text x="170" y="158" font-size="12" fill="currentColor" text-anchor="middle">连续 excursion 函数 e(t)</text>
    <text x="170" y="177" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">高度变化可以编码树上的分支与距离</text>
  </svg>

概念图：这是示意性的连续 excursion 曲线，并非 Brownian excursion 的真实模拟。

因此，Brownian motion 所带来的，并不只是一个连续随机过程。

它还为从离散组合结构走向连续随机几何提供了重要材料。

我们未来研究 CRT 时，将重新遇到今天的一系列思想：

随机游走、函数空间中的弱收敛、紧性、excursion、商空间以及由随机函数诱导的几何结构。

这是一个我们现在就可以预见的深层统一。

---

# 第四章结语：随机性终于拥有了形状

回顾我们的思想历程。

第一章，我们从一场没有结束的赌博开始，学会了计算不同结果的机会。

第二章，我们发现概率还能够被观察、估计和更新。

第三章，我们从大量独立随机变量的和中发现了 Gaussian 极限。

而这一章，我们把随机变量按照时间排列起来。

最开始，只是一系列整数：

\[
S_0,S_1,S_2,\ldots
\]

然后我们发现，时间与空间需要按照平方关系一起缩放：

\[
\Delta t\asymp(\Delta x)^2.
\]

经过这种缩放，随机游走在有限维分布上走向 Gaussian process。

但是，仅仅知道每个时间点的分布，还不足以得到随机路径。

我们不得不研究函数空间、紧性和路径的连续性。

最终，我们得到了 Brownian motion。

在这个过程中，概率论实现了一次重要的扩展：

\[
\boxed{
\text{随机数}
\quad\longrightarrow\quad
\text{随机向量}
\quad\longrightarrow\quad
\text{随机函数}
}
\]

更令人意外的是，这个随机函数虽然连续，却几乎必然处处不可导。

它的平方变差不是0，而是时间本身：

\[
[B]_t=t.
\]

因此，我们不仅创造了一种新的随机对象，也发现了旧的微积分语言无法完整描述它。

与此同时，它的概率分布又遵循确定性的热方程：

\[
\partial_t p=\frac12\partial_{xx}p.
\]

这为我们揭示了一种特别深刻的现象：

**随机路径在个体层面不可预测，却能在概率分布层面服从严格而确定的演化方程。**

但到这里，我们不能继续假装所有数学基础都已经解决。

事实上，我们在构造 Brownian motion 时，已经多次使用了尚未系统解释的概念：

\[
\sigma\text{-代数},\qquad
\text{概率测度},\qquad
\text{可测函数},\qquad
\text{测度的扩张}.
\]

我们已经看到这些对象能够做什么，却还没有认真回答它们为什么是必要的。

特别是，为什么无限空间上的概率不可能继续依靠简单计数？为什么不是每个子集都应当要求拥有概率？为什么有限可加性最终需要加强成可数可加性？

现在，我们必须回到这些问题。

不是为了机械地学习测度论定义，而是因为我们已经走到了一个无法再绕开它们的位置。

---

# 下一章：第五章《无限世界的代价——为什么概率需要测度论？》

我们将从一个看似无害的要求开始：

假设我们希望在区间 \([0,1]\) 上定义均匀概率，并且要求概率满足平移不变性与可数可加性。

那么，我们真的能给 \([0,1]\) 的所有子集赋予概率吗？

答案是否定的。

我们将发现：

\[
\boxed{
\text{概率不能随意赋予每一个集合。}
}
\]

这并不是因为数学家缺乏技巧，而是因为无限集合、选择公理、平移不变性与可数可加性之间存在真正的结构性冲突。

从这里，Borel 集、Lebesgue 测度、\(\sigma\)-代数与可测性，将不再是一串突然出现的抽象定义。

它们会成为我们不得不创造的数学语言。

《偶然的数学》· 第一卷第四章 · 工作稿 v0.1
