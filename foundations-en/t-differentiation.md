# T-DIFFERENTIATION: Recovering Local Densities from Covering Estimates

Companion to [Chapter 38](../chapters/38-feynman-kac.md#potential-differentiation). Work in Rᵈ with open Euclidean balls and Lebesgue volume |·|. We prove the Lebesgue differentiation and finite-measure density recovery needed here, keeping abstract RN densities distinct from pointwise recovery.

## 1. Fivefold Covering and a Weak Estimate

<a id="differentiation-proof-cover"></a>

For a family of balls with bounded radii in a bounded region, choose disjoint balls in descending size: pick a radius exceeding half the current supremum, remove intersecting balls, and repeat. Every omitted radius-r ball meets a selected ball of radius at least r/2, or it would have been chosen before the supremum fell below r/2. It is contained in that selected ball’s fivefold enlargement. The disjoint family is countable because each ball contains a distinct rational point. For compact sets a finite subcover and finite greedy choice suffice, avoiding infinite selection details.

\[ M\nu(x)=\sup_{r>0}\frac{|\nu|(B(x,r))}{|B(x,r)|},\qquad |\{M\nu>\lambda\}|\le\frac{5^d}{\lambda}|\nu|(\mathbb R^d),\quad\lambda>0. \]

For a compact subset of {Mν>λ}, choose at each point a ball with mass exceeding λ times volume. Disjoint selected balls have total volume at most |ν|/λ; fivefold covering bounds the compact set by 5ᵈ|ν|/λ. The level set is measurable: ball integrals are Borel in center and radius, and rational radii increasing from below recover open-ball integrals by continuity from below, without inadvertently adding a charged boundary sphere. Inner regularity and exhaustion give the full result. Taking ν=f dx yields the weak (1,1) maximal-average bound.

## 2. Continuous Functions First, then Weak Control of the Error

<a id="differentiation-proof-functions"></a>

For continuous compactly supported g, averaged local oscillation tends to zero. Approximate any L¹ f by such g: truncate values and space, approximate by simple functions, then use Radon inner/outer regularity to choose compact K⊂A⊂open U with small |\(U\setminus K\)|. Replace the indicator by the explicit continuous cutoff 1−dist(x,K)/(dist(x,K)+dist(x,Uᶜ)). No unproved Lusin theorem is needed.

\[ Df(x):=\limsup_{r\downarrow0}\frac1{|B(x,r)|}\int_{B(x,r)}|f(y)-f(x)|dy\le M(f-g)(x)+|f(x)-g(x)|. \]

For ε>0, the set {Df>2ε} has measure at most (5ᵈ+1)‖f−g‖₁/ε by the preceding weak estimate and Markov. Send the approximation error to zero and intersect over rational ε: Df=0 almost everywhere. Truncate a locally integrable f on successively larger balls; sufficiently small averages agree on the smaller balls, giving the local version by countable exhaustion. Null-set changes do not affect the result, but the limit holds on a common full-measure set, not at every point.

## 3. Why Singular Measure Is Not Recovered as an Ordinary Density

<a id="differentiation-proof-measures"></a>

Let a finite positive ν=f dx+ν_s be the Chapter 10 Lebesgue decomposition. Its singular part is supported on a null set N. Choose compact K⊂N with ν_s(\(\mathbb R^d\setminus K\))<δ. For x outside K, sufficiently small balls avoid K, so the upper density equals that of ν_s restricted to Kᶜ. The weak estimate bounds the Lebesgue measure of upper density greater than ε by 5ᵈδ/ε; K is null. Let δ↓0 and use countably many rational ε: the singular density is zero almost everywhere. Total variation handles signed measures, and spatial truncation handles local finiteness.

\[ \lim_{r\downarrow0}\frac{\nu(B(x,r))}{|B(x,r)|}=f(x)\quad\hbox{for Lebesgue-a.e. }x,\qquad \nu_s\ne0\ \hbox{is still possible}. \]

This explains why compressing a local-time charge into an almost-everywhere function q loses information. For ν=δ_c the recovered f is zero almost everywhere, yet ν is not zero. Occupation measures, distributional second derivatives and Revuz measures must retain singular parts. [Return to the chapter](../chapters/38-feynman-kac.md#potential-differentiation).
