# Advanced Reading: Donsker and Tightness of Paths

> Working topic material; see the page for the scope of each argument.

**Primary chapter:** 25

**Prerequisites:** Convergence from Chapter 7, measurability in function spaces, Arzelà–Ascoli, Prokhorov, and Kolmogorov tightness criteria.

**Proof scope:** Linear interpolation and the original fourth-moment calculations are written out, under their stated hypotheses. Finite-dimensional identification and path tightness still invoke external tools; this is not a self-contained functional CLT. Chapter25 and T-FCLT contain complete written finite-second-moment Donsker, empirical-bridge and finite-variance renewal proofs; continuing verification, not final review.

[Return to Chapter 4](#chapter-4) · [Topic and proof index](#reading-routes)

---

## 4.7 Donsker's Breakthrough: The Central Limit Theorem Should Extend Beyond Random Variables

> Editorial supplement: Appendix G lists the deeper theorems invoked in this chapter and the scope of the complete proofs; Appendix F supplies an additional proof of the joint finite-dimensional limit.

The central limit theorem in Chapter 3 tells us that

\[
\frac{S_n}{\sqrt n}\xrightarrow d N(0,1).
\]

What we now want to prove is that

\[
\left(
\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\right)_{0\le t\le1}
\]

can converge to Brownian motion as an entire stochastic process.

This is the central idea of what later became known as the functional central limit theorem.

Monroe Donsker's 1951 paper *An Invariance Principle for Certain Probability Limit Theorems* was an important milestone in this historical development.

The chronology needs to be distinguished from our earlier account: Donsker's work followed Wiener's rigorous construction of Brownian motion. We are taking the modern mathematical route of understanding Brownian motion anew through random-walk limits; we are not suggesting that Donsker's theorem historically preceded the invention of Brownian motion. 〔[38](#ref-turn288123search2), [39](#ref-turn288123search41)〕

### 4.7.1 First Turn Step Paths into Continuous Paths

The process defined earlier,

\[
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\]

is a step function.

At each grid time, it makes a jump of size \(1/\sqrt n\).

For any fixed \(n\), it is therefore not continuous.

To study it in a space of continuous functions, the most natural approach is linear interpolation.

Let

\[
k=\lfloor nt\rfloor,\qquad r=nt-k.
\]

Define

\[
\boxed{
\widetilde W_n(t)
=
\frac{(1-r)S_k+rS_{k+1}}{\sqrt n},
\quad0\le t<1,
}
\]

and set

\[
\widetilde W_n(1)=\frac{S_n}{\sqrt n}.
\]

Now every path of \(\widetilde W_n\) is continuous.

Moreover,

\[
\sup_{0\le t\le1}
|\widetilde W_n(t)-W_n(t)|
\le\frac1{\sqrt n}.
\]

The difference between the two representations therefore tends to zero in the uniform norm.

Notice, however, that linear interpolation only lets us place these processes in a continuous function space.

It does not automatically prove that a limit exists.

### 4.7.2 In Which Space Do We Want Convergence?

Consider

\[
C([0,1])
\]

the space of all real-valued continuous functions on \([0,1]\).

Equip it with the uniform norm:

\[
\|f\|_\infty
=
\sup_{0\le t\le1}|f(t)|.
\]

Each \(\widetilde W_n\) can then be regarded as a random element taking values in \(C([0,1])\).

This is fundamentally the same kind of object as the individual random variables studied earlier.

The difference is that the values now lie in an infinite-dimensional function space rather than in \(\mathbb R\).

We want to prove

\[
\boxed{
\widetilde W_n\xrightarrow d B
\quad\text{in }C([0,1]).
}
\]

Convergence in distribution here can be expressed using bounded continuous functionals:

for every bounded continuous map

\[
F:C([0,1])\longrightarrow\mathbb R,
\]

we have

\[
\mathbb E[F(\widetilde W_n)]
\longrightarrow
\mathbb E[F(B)].
\]

This goes beyond probabilistic convergence at a single time.

It allows us to discuss functions of an entire path, such as

\[
F(f)=\max_{0\le t\le1}f(t).
\]

The maximum functional is continuous in the uniform norm because

\[
|\max f-\max g|
\le\|f-g\|_\infty.
\]

Once we prove weak convergence in the function space, the continuous mapping theorem therefore yields a limit theorem for the maxima.

This is why the functional central limit theorem is so much more powerful than the ordinary central limit theorem.

### 4.7.3 What Is Missing from Finite-Dimensional Distributions?

In Section 4.5 we proved convergence of the finite-dimensional distributions.

But that alone is insufficient.

We must also exclude path fluctuations that become increasingly sharp and difficult to control.

Modern probability theory addresses this through one concept:

**Tightness.**

Intuitively, we want most of the probability mass of the random paths not to escape into increasingly irregular regions of function space where no convergent subsequence can be found.

In \(C([0,1])\), the Arzelà–Ascoli theorem tells us that relative compactness of a family of functions requires both boundedness at one point and uniform equicontinuity.

Tightness of stochastic processes can therefore be proved by controlling oscillations over small time intervals.

For example, we would like a moment estimate independent of \(n\):

\[
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le C|t-s|^2.
\]

For our symmetric random walk, such an estimate does hold.

We can even prove it directly.

Write the increment of the interpolated process over \([s,t]\) as

\[
\widetilde W_n(t)-\widetilde W_n(s)
=
\frac1{\sqrt n}\sum_j a_j\xi_j,
\]

where the coefficients satisfy \(a_j\in[0,1]\) and

\[
\sum_j a_j=n(t-s).
\]

Since the \(\xi_j\) are independent symmetric \(\pm1\) random variables, expansion of the fourth moment gives

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
=
3\left(\sum_j a_j^2\right)^2
-
2\sum_j a_j^4.
\]

Hence

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
\le
3\left(\sum_j a_j^2\right)^2.
\]

Also, since \(0\le a_j\le1\),

\[
\sum_j a_j^2
\le\sum_j a_j
=n(t-s).
\]

we obtain

\[
\boxed{
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le3|t-s|^2.
}
\]

This estimate holds for every \(n\).

It controls oscillations uniformly over the entire family of random paths.

Applying the corresponding Kolmogorov tightness criterion together with

\[
\widetilde W_n(0)=0,
\]

proves that the distributions of these processes are tight in \(C([0,1])\).

Finally, combining tightness with convergence of the finite-dimensional distributions yields the functional central limit theorem.

\[
\boxed{
\widetilde W_n\Longrightarrow B
\quad\text{in }C([0,1]).
}
\]

This is a concrete version of Donsker's invariance principle for our model.

Donsker's theorem also holds for more general independent, identically distributed random increments with mean 0 and variance 1. With only a finite second moment, the simple fourth-moment proof above may not apply directly; a more general tightness argument is required.

For the full theory of functional convergence and its proofs, see [Encyclopedia of Mathematics: Donsker invariance principle](https://encyclopediaofmath.org/wiki/Donsker_invariance_principle). 〔[38](#ref-turn288123search2), [40](#ref-turn288123search39), [39](#ref-turn288123search41)〕

We can finally say:

**Brownian motion is more than the normal limit of a random walk at a single time: it can arise as the limit in distribution of the entire random-walk path.**

This universality goes deeper than the central limit theorem of Chapter 3.

Under suitable scaling of space and time, different microscopic random mechanisms can have not only the same terminal distribution, but also the same continuous stochastic process as their limit.

---

