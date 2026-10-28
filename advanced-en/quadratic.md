# Advanced Reading: Path Roughness, Quadratic Variation, and the Motivation for Itô Calculus

> Working topic material; see the page for the scope of each argument.

**Primary chapter:** 31

**Prerequisites:** Existence of Brownian motion, L2 convergence, Borel–Cantelli, stochastic integration, and Itô’s formula.

**Proof scope:** A written quadratic-variation proof is available for fixed T along dyadic grids, assuming Brownian motion exists. Fixed-time difference-quotient scaling motivates nondifferentiability; it is not a complete almost-sure nowhere-differentiability proof. Chapter 26 handles path regularity; Chapter 31 develops general variation and integration, and Chapter 32 proves Itô’s formula. Chapter 26 adds a uniform-mesh nowhere-differentiability proof and deterministic dyadic square sums; general brackets and stochastic integration remain for Chapter 31. Chapter31 and T-ITO-BRACKET contain complete working proofs for continuous-local-martingale integration, brackets and ucp square sums; author review and human final review remain open; the legacy body is preserved.

[Return to Chapter 4](#chapter-4) · [Topic and proof index](#reading-routes)

---

## 4.10 Continuous Yet Not Differentiable: Another Paradox of Brownian Motion

We have now actually constructed Brownian motion.

It has continuous sample paths:

\[
t\longmapsto B_t(\omega).
\]

At first glance, since the particle’s position changes continuously with time, it seems we should be able to define its instantaneous velocity:

\[
v(t)=\lim_{h\to0}\frac{B_{t+h}-B_t}{h}.
\]

But matters are not that simple.

By the definition of Brownian motion,

\[
B_{t+h}-B_t\sim N(0,h)
\]

for \(h>0\).

Thus

\[
\frac{B_{t+h}-B_t}{h}
\sim N\left(0,\frac1h\right).
\]

As \(h\downarrow0\), the variance of this difference quotient actually tends to infinity.

The difference quotient therefore does not become increasingly concentrated near any finite value.

Indeed, for any fixed \(M>0\),

\[
P\left(
\left|\frac{B_{t+h}-B_t}{h}\right|\le M
\right)\longrightarrow0.
\]

These difference quotients cannot therefore even converge in probability to a finite random variable.

But this is still not the strongest conclusion.

Brownian sample paths are in fact almost surely **nowhere differentiable**.

This is a surprising fact:

\[
\boxed{
\text{sample paths are continuous}
\quad\text{but almost surely nowhere differentiable}.
}
\]

In calculus, we became accustomed to an intuition:

Continuous functions represent smooth motion, and velocity should be obtained by differentiating position.

Brownian motion overturns this intuition completely.

It is continuous motion with a rigorous mathematical existence, yet its paths are too rough to describe using ordinary differentiation. For proofs and the historical development of path regularity, see modern probability texts on Brownian motion.〔[45](#ref-turn516523search41), [46](#ref-turn288123search37)〕

We can, however, understand this roughness through a more structural quantity.

### 4.10.1 How Rough Is a Path?

On the interval \([0,T]\), consider the dyadic grid

\[
t_k=\frac{kT}{2^m},
\qquad k=0,\ldots,2^m.
\]

Define the sum of squared increments:

\[
Q_m=
\sum_{k=0}^{2^m-1}
(B_{t_{k+1}}-B_{t_k})^2.
\]

Since the increments are independent and

\[
B_{t_{k+1}}-B_{t_k}
\sim N\left(0,\frac{T}{2^m}\right),
\]

we have

\[
\mathbb E[Q_m]
=
2^m\cdot\frac{T}{2^m}
=T.
\]

A normal random variable with mean 0 and variance \(v\), denoted by \(Z\), satisfies

\[
\operatorname{Var}(Z^2)=2v^2.
\]

Therefore

\[
\begin{aligned}
\operatorname{Var}(Q_m)
&=
2^m\cdot2\left(\frac{T}{2^m}\right)^2\\
&=\frac{2T^2}{2^m}.
\end{aligned}
\]

Thus

\[
Q_m\longrightarrow T
\]

in \(L^2\).

Furthermore, Chebyshev’s inequality gives

\[
P(|Q_m-T|>\varepsilon)
\le
\frac{2T^2}{\varepsilon^2 2^m}.
\]

The right-hand side is summable in \(m\).

The Borel–Cantelli lemma therefore yields

\[
\boxed{
Q_m\xrightarrow{\mathrm{a.s.}}T.
}
\]

This is a rigorous statement of Brownian motion’s quadratic variation along dyadic grids.

We usually write

\[
\boxed{[B]_T=T.}
\]

### 4.10.2 Why Is This Completely Different from Ordinary Smooth Functions?

Suppose \(f:[0,T]\to\mathbb R\) is continuously differentiable.

The mean value theorem gives

\[
|f(t_{k+1})-f(t_k)|
\le M(t_{k+1}-t_k)
\]

where

\[
M=\sup_{0\le t\le T}|f'(t)|<\infty.
\]

Hence

\[
\begin{aligned}
\sum_k(f(t_{k+1})-f(t_k))^2
&\le
M^2\sum_k(t_{k+1}-t_k)^2\\
&=M^2\frac{T^2}{2^m}\\
&\longrightarrow0.
\end{aligned}
\]

For a smooth function, the sum of squared increments along increasingly fine grids therefore tends to zero.

Brownian motion, however, satisfies

\[
\sum_k(B_{t_{k+1}}-B_{t_k})^2
\longrightarrow T.
\]

In other words:

\[
\boxed{
\begin{aligned}
\text{smooth paths：}&\quad [f]_T=0,\\
\text{Brownian paths：}&\quad [B]_T=T.
\end{aligned}
}
\]

This goes deeper than saying that “the paths are somewhat unsmooth.”

It shows that Brownian motion has a cumulative second-order effect that ordinary calculus cannot disregard.

### 4.10.3 Why Must Stochastic Calculus Be Reinvented?

In ordinary calculus, we often disregard second-order infinitesimals.

Indeed, if

\[
dx=O(dt),
\]

then

\[
(dx)^2=O(dt^2),
\]

which tends to zero after division by \(dt\).

For Brownian motion, however, typical increments have the scale

\[
dB\sim O(\sqrt{dt})
\]

shown above.

Thus

\[
(dB)^2\sim O(dt).
\]

The accumulated contribution of squared increments is therefore of the same order as the first-order time increments.

We can no longer disregard it as in ordinary calculus.

This is the fundamental reason why the formal relationship

\[
\boxed{(dB_t)^2=dt}
\]

will appear in Itô calculus.

This is not algebra that treats \(dB_t\) as an ordinary real differential; it is concise notation for the quadratic-variation structure within the theory of stochastic integration.

For example, ordinary calculus might lead us to expect

\[
d(B_t^2)=2B_t\,dB_t.
\]

whereas Itô’s formula actually gives

\[
\boxed{
d(B_t^2)=2B_t\,dB_t+dt.
}
\]

The additional \(dt\) arises precisely from Brownian motion’s nonzero quadratic variation.

We have not yet established stochastic integration rigorously, so this remains a preview of the theory to come.

But it already reveals a very important pattern in the development of probability:

**New theories of integration arise because new random objects cannot be fully described by existing calculus, rather than simply because mathematicians want more complicated formulas.**

---

