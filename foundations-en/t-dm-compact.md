# T-DM-COMPACT: How Uniform Integrability Retains a Genuine Limit

On a probability space we prove the compactness tools used in Chapter 30: a convex-growth criterion for uniform integrability, weak L¹ subsequence selection, and L¹ convergence of finite forward convex combinations. The last tool applies directly to discrete compensators, without stochastic integration, a Banach-space weak compactness theorem, or the general Komlós theorem.

<a id="t-dm-convex-growth"></a>

## 1. Turning a Tail Condition into a Convex Function

Let a family of real random variables X be uniformly integrable. Choose strictly increasing Kⱼ tending to infinity such that E[|X|; |X|>Kⱼ]≤2⁻ʲ for every X. Define the nonnegative function below. Only finitely many terms are nonzero on a bounded interval, so Φ is finite, continuous and convex, with Φ(0)=0.

\[ \Phi(x)=\sum_{j\ge1}(x-K_j)^+,\quad x\ge0;\qquad \sup_X E\Phi(|X|)\le\sum_{j\ge1}2^{-j}<\infty. \]

For fixed m and x≥2Kₘ, the first m terms sum to at least mx/2, so Φ(x)/x tends to infinity. Conversely, if a nonnegative convex function has this superlinear growth and the displayed expectations are uniformly bounded, the tail expectation is bounded as below. The supremum tends to zero, proving uniform integrability. This is the de la Vallée-Poussin criterion used here.

\[ E[|X|;|X|>K]\le E\Phi(|X|)\sup_{x>K}\frac{x}{\Phi(x)}. \]

In particular, all finite convex combinations from one uniformly integrable family are uniformly integrable: convexity of absolute value, monotonicity of Φ, and Jensen preserve the same bound on the convex-growth expectation.

<a id="t-dm-weak-selection"></a>

## 2. The Required Weak L¹ Subsequence Result

If (fₙ) is uniformly integrable, some subsequence fₙⱼ and f∈L¹ satisfy E[h fₙⱼ]→E[h f] for every bounded measurable h. We prove this sequential statement, which suffices here, rather than substitute an unproved abstract compactness assertion.

Let G=σ(f₁,f₂,…). Enumerate rational threshold sets of these variables, form the increasing finite algebras they generate, and denote their union by the countable algebra A. It generates G. A diagonal extraction makes E[fₙⱼ1_B] converge for every B∈A. Uniform integrability gives the following uniform absolute continuity, by first truncating |fₙ| at K and then making P(B) small.

\[ \sup_n E[|f_n|;B]\le K P(B)+\sup_n E[|f_n|;|f_n|>K]\longrightarrow0\quad\text{as }P(B)\longrightarrow0. \]

Every B∈G can be approximated by sets in A in probability of symmetric difference. Indeed, the approximable sets form a σ-algebra: complements preserve errors, while increasing unions are first cut to finite unions and their probability tails controlled. Uniform absolute continuity then makes E[fₙⱼ1_B] Cauchy for every B∈G. Call the limit ν(B). It is finitely additive. For disjoint Bᵢ, the remaining union has probability tending to zero, and uniform absolute continuity sends its ν-mass to zero too. Thus ν is countably additive.

On every finite partition, the sum of the absolute ν-masses is at most supₙE|fₙ|, by first taking limits of finitely many integrals and then summing. Thus the total variation of ν is finite and ν≪P. The signed Radon–Nikodym result in Chapter 10 supplies a G-measurable f∈L¹. Approximation by simple functions proves weak convergence against all bounded G-measurable h. For bounded h in the original σ-algebra, replace it by E[h|G]: both integrals remain unchanged because fₙⱼ and f are G-measurable. This proves the asserted weak L¹ subsequence result.

<a id="t-dm-forward-convex"></a>

## 3. Beyond Weak Convergence: L¹-Convergent Forward Convex Combinations

First prove a geometric fact in a Hilbert space. Let (vₙ) be norm-bounded, let Cₙ consist of finite convex combinations of vectors from index n onward, and set aₙ=inf{‖v‖²:v∈Cₙ}. Then aₙ increases to a finite a. Choose uₙ∈Cₙ with ‖uₙ‖²≤aₙ+1/n. For i,j≥n their midpoint remains in Cₙ, so the parallelogram identity gives

\[ \|u_i-u_j\|^2=2\|u_i\|^2+2\|u_j\|^2-4\left\|\frac{u_i+u_j}{2}\right\|^2\le4(a-a_n)+\frac4n\longrightarrow0. \]

Thus uₙ converges in norm. Put all truncations into one Hilbert space simultaneously, rather than choose incompatible weights separately. Set fₙ⁽ʲ⁾=fₙ1{|fₙ|≤j} and take the vectors below. Their squared norms are at most Σ4⁻ʲ. The space is the square-summable direct sum of countably many copies of L². Its completeness follows from coordinatewise L² completeness and Fatou applied to the tail sum of squared norms.

\[ v_n=\left(\frac{2^{-j}}{j}f_n^{(j)}\right)_{j\ge1}\in\bigoplus_{j\ge1}L^2(P). \]

The Hilbert result supplies the same finite convex weights λₙ,ₖ, with k≥n, for which every truncated weighted sum converges in L². For the untruncated gₙ=Σₖλₙ,ₖfₖ, the L¹ distance between gₘ and gₙ is bounded by two uniform truncation errors plus the L¹ distance between the corresponding truncated combinations. Fix j large enough to make the tails small, then use L² convergence and its implication of L¹ convergence. Thus (gₙ) is L¹ Cauchy, and completeness from T-LP gives an L¹ limit.

\[ g_n\in\operatorname{conv}\{f_n,f_{n+1},\ldots\},\qquad \|g_n-g\|_1\longrightarrow0. \]

Every convex combination here has finitely many terms and deterministic coefficients. One may take a further subsequence with summable L¹ errors, obtaining almost sure convergence. If gₙ are martingale terminal values, the continuous-time maximal inequality also turns terminal errors into control in probability over the whole time interval. Chapter 30 uses the former fact on countable grids and separately proves predictability at jump times; it does not automatically identify the pointwise limit of left-continuous approximants with a right-continuous compensator.

Prerequisites: [Lᵖ completeness](t-lp.md#t-lp-complete), [Radon–Nikodym construction](../chapters/10-densities-and-kernels.md), and [return to Chapter 30](../chapters/30-predictability.md#dm-construction).
