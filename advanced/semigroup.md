# 进阶阅读：从随机运动到半群与生成元

> 本模块完整迁移自调整前第四章，保留旧节号和全部原文。它是供后续章节接续的技术工作稿，不属于当前第四章的必读证明。

**目的章节：**第20章《只记住现在的系统》；第31章《概率演化与确定性方程》。

**前置：**Lebesgue 积分、条件分布、Markov 性、算子半群与生成元定义域。

**证明边界：**半群与生成元原推导完整后移；本模块以已经构造的 Brownian motion 为前提，不声称第四章已建立半群理论。

[返回第四章阅读主线](#chapter-4) · [查看旧第四章完整快照](/downloads/04-brownian-before-restructure.md)

---

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

