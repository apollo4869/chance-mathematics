# 进阶阅读：Donsker 与路径紧性

> 专题工作材料；分项证明范围以网页说明为准。

**主要归属：** 25

**前置：**第7章收敛、函数空间可测性、Arzelà–Ascoli、Prokhorov 与 Kolmogorov 紧性准则。

**证明范围：** 线性插值和原有四阶矩计算已写出，适用范围须按各段假设理解。 有限维识别及路径紧性仍依赖外部工具，现有材料不是自足的函数型CLT。 第25章与T-FCLT已写成一般有限二阶矩Donsker、经验桥与有限方差更新版本的完整证明；数学持续核验，非终审。

[返回第四章](#chapter-4) · [专题与证明索引](#reading-routes)

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

