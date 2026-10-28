# 进阶阅读：连续版本与 Wiener measure

> 专题工作材料；分项证明范围以网页说明为准。

**主要归属：** 23

**前置：**测度扩张、Gaussian 向量、一致有限维分布、Kolmogorov 连续修正及路径映射可测性。

**证明范围：** 第八章已建立坐标概率的扩张；这不等于连续路径构造。 现有材料给出由一致 Gaussian 有限维分布到连续版本的路线，调用了扩张与连续修正工具。 第23.6–23.12节已有连续修改、C/C_loc值可测性及Wiener存在唯一的完整书面证明；数学持续核验，非终审。

[返回第四章](#chapter-4) · [专题与证明索引](#reading-routes)

---

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

