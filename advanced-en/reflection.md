# Advanced Reading: First Passage and the Reflection Principle

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapter:** Chapter 25, “Hitting, Reflection, and Path Decomposition.”

**Prerequisites:** Continuous paths, stopping times, the natural filtration, the strong Markov theorem, and the measure-preserving property of the reflection transformation.

**Scope of the proof:** The original account of reflection, its formulas, and the first-passage-time calculation are all retained. The strong Markov property and the measure-preserving property of reflection still require systematic proofs; geometric symmetry is not treated as a complete proof.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.11 Why Does a Random Path Contain More Information Than a Random Variable?

So far, we know that

\[
B_T\sim N(0,T).
\]

This tells us where the particle is at time \(T\).

But suppose we want to ask:

By time \(T\), has the particle ever reached a height \(a>0\)?

This is a completely different question.

Define the first-passage time

\[
\tau_a=\inf\{t\ge0:B_t=a\}.
\]

What we really want is

\[
P(\tau_a\le T).
\]

This event depends on the whole path, as opposed to the final position \(B_T\) alone.

For example, the particle might reach height \(a\) and then return close to the origin.

Observing only the final position cannot tell us whether this happened.

But the special symmetry of Brownian motion allows us to calculate the probability of this path event.

### 4.11.1 The Reflection Principle

Consider all paths that, by time \(T\), reach height \(a\) but finish below \(a\).

For each such path, reflect the portion after its first arrival at height \(a\) across the horizontal line \(y=a\).

By the strong Markov property of Brownian motion after the first-passage time and the symmetry of its increments, this reflection gives a probability correspondence between the relevant path events.

We obtain the reflection principle:

\[
\boxed{
P\left(\sup_{0\le t\le T}B_t\ge a\right)
=
2P(B_T\ge a).
}
\]

Since

\[
B_T\sim N(0,T),
\]

we have

\[
P(B_T\ge a)
=
1-\Phi\left(\frac a{\sqrt T}\right),
\]

where \(\Phi\) is the standard normal distribution function.

Therefore

\[
\boxed{
P(\tau_a\le T)
=
2\left[
1-\Phi\left(\frac a{\sqrt T}\right)
\right].
}
\]

This formula deserves close attention.

The central limit theorem originally gave us a Gaussian distribution at a fixed time.

Path symmetry now lets us use it to calculate the probability of a first-passage event as well.

We can even derive the density of the first-passage time:

\[
\boxed{
f_{\tau_a}(t)
=
\frac{a}{\sqrt{2\pi t^3}}
\exp\left(-\frac{a^2}{2t}\right),
\qquad t>0.
}
\]

Interestingly,

\[
P(\tau_a<\infty)=1,
\]

but

\[
\mathbb E[\tau_a]=\infty.
\]

Thus the particle almost surely eventually reaches any fixed positive height, yet the expected waiting time to reach it is infinite.

This reminds us once again:

An event occurring almost surely does not imply that its waiting time has finite expectation.

From first-passage problems for discrete random walks to the reflection principle for continuous Brownian motion, probability theory begins to develop a theory of entire random trajectories.

---

