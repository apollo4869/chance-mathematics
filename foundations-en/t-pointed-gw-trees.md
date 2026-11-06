# T-POINTED-GW-TREES: Typical Individuals, Ancestral Regeneration and a Critical Local Limit

This page supplies [Chapter 57’s spinal sampling](../chapters/57-regenerative-growth.md#growth-pointed-spine), using Chapter 52’s independent-address plane GW construction and Chapter 20’s extinction classification and finite-variance critical survival asymptotic. It does not repeat the supercritical L log L argument; the new objects are different sampling weights and conditioning limits.

## 1. First specify what typical individual means

<a id="pointed-total-palm"></a>

\[ 0<m=E\xi<1,\qquad E|T|=\sum_{h\ge0}EZ_h=\frac1{1-m},\qquad \widehat P(T=t,V=v)=(1-m)P(T=t),\quad v\in t. \]

Tonelli justifies the nonnegative sum, and finite expectation ensures T is finite almost surely. The last expression sums to one over finite plane trees and their vertices. It chooses the tree with total-population bias, then a uniform vertex within it. Choosing an original P-tree first and a uniform vertex afterward instead gives P(t)/|t|. These are different experiments. A typical vertex need not be a leaf or belong to the last generation.

## 2. The product density along a finite spine

<a id="pointed-many-to-one"></a>

\[ \widehat p_\ell=\frac{\ell p_\ell}{m},\quad\ell\ge1;\qquad Q_h(t,v)=m^{-h}P(t)\mathbf1_{\{|v|=h\}}. \]

Construct Qₕ by taking h independent size-biased offspring counts, selecting one child uniformly to continue the spine and attaching independent original GW trees to all other children. Attach a whole original GW tree below the terminal marked vertex. A specified ancestor count ℓ and specified continuing child contribute (ℓpℓ/m)(1/ℓ)=pℓ/m, not ℓpℓ/m. Multiplying h factors gives the density; its total mass is E Zₕ/mʰ=1. Thus every nonnegative tree-vertex test satisfies the many-to-one identity.

\[ E_P\sum_{|v|=h}F(T,v)=m^h E_{Q_h}F(T,V). \]

Use independent integer variables, uniform child choices and original GW environments at countably many addresses, with Chapter 52’s measurable coding. Conditional on the spinal counts and chosen children, all side trees and the terminal tree are independent. This is an explicit conditional-independence statement, not a conclusion read from a picture.

## 3. A random endpoint gives a computable regenerative representation

<a id="pointed-geometric-spine"></a>

\[ P(H=h)=(1-m)m^h,\qquad h\ge0,\qquad \widehat P=\sum_{h\ge0}(1-m)m^h Q_h. \]

For a pair (t,v), the mixture contributes (1−m)mʰm⁻ʰP(t), exactly the first section’s law. Thus typical depth is geometric; conditional on depth, ancestral environments are iid size-biased, while side trees and descendants of the marked vertex retain the original GW law. Generate an independent H and an infinite candidate environment, then stop at H. Conditional on not yet stopping, the remaining geometric depth has the same law and side trees restart. This is regeneration in generation count, not an unproved claim that physical birth intervals form Chapter 19’s renewal process.

Bias occurs at ancestors required to lead to the sampled individual, not at every vertex. The marked individual’s offspring still have law p. The product density proves the distinction. Dropping the 1/ℓ child-choice factor would destroy normalization and the interpretation.

## 4. Looking far ahead in a critical tree gives a different infinite spine

<a id="pointed-critical-limit"></a>

\[ m=1,\quad0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad a_N=P(Z_N>0)\sim\frac2{\sigma^2N}. \]

Now expected total population is infinite, so total-population bias cannot be normalized. For fixed observed height h and N≥h, independence of the descendant families gives conditional survival probability 1−(1−a(N−h))^{Zₕ} on Fₕ. Chapter 20’s proved survival asymptotic yields the following density limit.

\[ \frac{dP(\,\cdot\mid Z_N>0)|_{\mathcal F_h}}{dP|_{\mathcal F_h}}=\frac{1-(1-a_{N-h})^{Z_h}}{a_N}\longrightarrow Z_h\quad\text{in }L^1(P). \]

Pointwise convergence follows from (1−(1−a)ᶻ)/a→z and a(N−h)/a(N)→1. The bound 1−(1−a)ᶻ≤za dominates the density by CZₕ for large N, with E Zₕ=1. Dominated convergence proves L¹ and hence total variation convergence of the first h generations. The limiting densities Zₕ are consistent because population is a mean-one martingale. An infinite spine with counts ℓpℓ, uniform continuing children and independent critical GW side trees realizes them by the same product calculation.

Original critical side trees are almost surely finite. There are countably many of them, so on a common good set all are finite and the spine is the unique infinite ancestral line. This local limit, commonly called the Kesten tree, uses the explicitly assumed finite-variance survival asymptotic. No general infinite-variance extension is counted.

## 5. A local spinal limit is not a compact CRT limit

<a id="pointed-scope"></a>

Survival to generation N with unit edges and fixed h gives the infinite local tree above. Conditioning total size n and scaling edges by σ/(2√n) gives Chapter 55’s compact CRT. Conditioning, scale and topology all differ. Sharing a spine does not make these limits equivalent. Subcritical total-population Palm sampling, critical survival bias and Brownian mass sampling are distinct experiments. This page proves discrete ancestral regeneration and two precise biases, not a general classification of continuous regenerative CRTs. [Return to the chapter](../chapters/57-regenerative-growth.md#growth-local-global).
