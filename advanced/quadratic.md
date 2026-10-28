# 进阶阅读：路径粗糙性、平方变差与 Itô 动机

> 专题工作材料；分项证明范围以网页说明为准。

**主要归属：** 31

**前置：**Brownian motion 的存在、L2 收敛、Borel–Cantelli、随机积分与 Itô 公式。

**证明范围：** 固定 T、沿二进网格的平方变差计算已有书面证明，须先有 Brownian motion。 固定时刻差商的尺度说明不可导的动机，不是几乎必然处处不可导的完整证明。 第二十六章处理路径正则性；第三十一章建一般变差与积分，第三十二章证明 Itô 公式。 第26章另有处处不可微的统一网格全证及确定二进平方和；这不完成第31章的一般括号/随机积分。 第31章与T-ITO-BRACKET已写成连续局部鞅积分、括号与ucp平方和的完整工作证明；作者待审、人工终审开放，旧模块原文保留。

[返回第四章](#chapter-4) · [专题与证明索引](#reading-routes)

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

