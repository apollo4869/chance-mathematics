# Advanced Reading: From Random Motion to Semigroups and Generators

> This module was transferred in full from Chapter 4 before its restructuring, retaining the old section numbers and all original text. It is a technical working draft for later chapters to build on, rather than a required part of the proofs in the current Chapter 4.

**Destination chapters:** Chapter 20, “Systems That Remember Only the Present”; Chapter 31, “Probabilistic Evolution and Deterministic Equations.”

**Prerequisites:** Lebesgue integration, conditional distributions, the Markov property, operator semigroups, and domains of generators.

**Scope of the proof:** The original derivations of the semigroup and generator have been moved here in full. This module assumes Brownian motion has already been constructed; it does not claim that Chapter 4 has established semigroup theory.

[Return to the main narrative of Chapter 4](#chapter-4) · [View the complete snapshot of the old Chapter 4](/downloads/04-brownian-before-restructure.md)

---

### 4.9.3 A Unification: Random Paths and Deterministic Evolution

We now have two entirely different descriptions.

The first is the random path:

\[
t\longmapsto B_t(\omega).
\]

Each \(\omega\) corresponds to a different random trajectory.

The second is the probability density:

\[
(t,x)\longmapsto p_t(x).
\]

This function is governed by the deterministic heat equation.

For a sufficiently regular function \(f\), define

\[
P_tf(x)
=
\mathbb E[f(x+B_t)].
\]

Since Brownian motion has independent, stationary increments,

\[
P_{t+s}f=P_t(P_sf).
\]

Thus \((P_t)_{t\ge0}\) forms a Markov semigroup.

Its infinitesimal generator satisfies

\[
\lim_{h\downarrow0}
\frac{P_hf(x)-f(x)}{h}
=
\frac12f''(x),
\]

for example, for \(f\in C_c^\infty(\mathbb R)\).

Therefore

\[
\boxed{
L=\frac12\frac{d^2}{dx^2}.
}
\]

The corresponding evolution equation is precisely

\[
\frac{\partial u}{\partial t}=Lu.
\]

We obtain an exceptionally important unifying relationship:

\[
\boxed{
\text{stochastic processes}
\longleftrightarrow
\text{Markov semigroups}
\longleftrightarrow
\text{partial differential equations}.
}
\]

This is more than a symbolic correspondence.

It means that random motion can explain partial differential equations, while partial differential equations can be used to study the probability distributions of stochastic processes.

In stochastic calculus, the Feynman–Kac formula, and stochastic differential equations, we will repeatedly encounter the importance of this connection.

---

