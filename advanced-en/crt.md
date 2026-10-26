# Advanced Reading: From Brownian Paths to Random Trees

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapters:** Chapter 25, excursions and path decomposition; Chapter 43, path encoding; Chapter 45, real trees; Chapter 46, the Brownian CRT (following the locations in the existing draft).

**Prerequisites:** Excursions, pseudometrics and quotient spaces, properties of real trees, normalization, and weak convergence in function spaces.

**Scope of the proof:** The list of topics “already developed” at the start of the old section reviews the former manuscript, rather than recording what the current reading edition has completed. The tree-encoding formulas and SVG illustration are preserved; the CRT construction and limit theorems have not been proved within the six chapters.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.12 Why Is Brownian Motion So Important for the Future of Probability Theory?

Starting from a very simple random walk, we have gradually developed:

- probability measures on infinite-dimensional function spaces;
- continuous Gaussian processes;
- the functional central limit theorem;
- Markov semigroups and the heat equation;
- random paths that are continuous but nondifferentiable;
- quadratic variation and the need for stochastic calculus;
- first-passage times and path events.

These concepts seem to span probability theory, functional analysis, partial differential equations, and differential geometry.

But their appearance together is no accident.

They all center on one fundamental question:

**How can we understand an object that continually generates fresh randomness over time?**

Brownian motion provides a particularly precise and rich mathematical model for this question.

More importantly, it teaches us for the first time to treat a random function as a basic object in a probability space.

The significance of this extends far beyond Brownian motion itself.

### 4.12.1 From Brownian Paths to Random Trees

Let us glimpse a construction that will return later.

Suppose we have a nonnegative continuous function

\[
e:[0,1]\to[0,\infty)
\]

satisfying

\[
e(0)=e(1)=0.
\]

For example, \(e\) might be a Brownian excursion.

We can define

\[
m_e(s,t)
=
\inf_{u\in[s\wedge t,s\vee t]}e(u).
\]

and then set

\[
\boxed{
d_e(s,t)
=
e(s)+e(t)-2m_e(s,t).
}
\]

This expression is worth examining closely.

It is the sum of the heights at two times, minus twice the lowest common height encountered between them.

If the rises and falls of the continuous function represent a depth-first traversal of a tree, the expression has the meaning of distance in that tree.

By identifying times satisfying

\[
d_e(s,t)=0
\]

we can construct a quotient space.

For suitable excursions, this quotient space has the structure of a real tree.

When \(e\) is a suitably normalized Brownian excursion, this connects with the classical construction of the Brownian CRT; the precise scale factor depends on the normalization convention.

Illustrating the idea of passing from a continuous function to tree geometry

<svg viewBox="0 0 340 185" width="100%" xmlns="http://www.w3.org/2000/svg">
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130 L325 130 L15 130 Z" fill="#168782" opacity="0.12"/>
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130" fill="none" stroke="#168782" stroke-width="2.6" stroke-linecap="round"/>
    <line x1="15" y1="130" x2="325" y2="130" stroke="currentColor" opacity="0.4"/>
    <text x="170" y="158" font-size="12" fill="currentColor" text-anchor="middle">Continuous excursion function e(t)</text>
    <text x="170" y="177" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">Height changes encode branches and distances in a tree</text>
  </svg>

Conceptual diagram: This is a schematic continuous excursion curve, not an actual simulation of a Brownian excursion.

Brownian motion therefore gives us more than a continuous stochastic process.

It also supplies important material for passing from discrete combinatorial structures to continuous random geometry.

In our future study of the CRT, we will encounter many of today's ideas again:

random walks, weak convergence in function spaces, tightness, excursions, quotient spaces, and geometric structures induced by random functions.

This is a deep unification that we can already foresee.

---

