# T-LAMBDA-COALESCENT: Consistent Rates, Poisson Construction, Dust and Reversal Boundaries

This page proves the single-group multiple-merger theory of [Chapter 56](../chapters/56-fragmentation-hierarchies.md#coalescent-rates), without repeating Chapter 47’s Kingman main line. Λ is a finite nonnegative measure on [0,1]. A jump merges one group of any size; simultaneous multi-group Ξ-type jumps are outside this proof.

## 1. The recursion forced by deleting one block

<a id="lambda-recursion"></a>

\[ \lambda_{b,k}=\lambda_{b+1,k}+\lambda_{b+1,k+1},
\qquad 2\le k\le b. \]

All rates are finite nonnegative numbers. Here λ is the rate of one specified k-tuple, not the total rate of all such jumps. After adding an invisible block, that tuple may merge alone or together with the extra block. These disjoint events give the same restricted jump, forcing the recursion. Conversely nonnegative rates satisfying it intertwine finite generators under deleting extra blocks. Matrix exponentials and repeated conditional expectations give path consistency.

## 2. Proving the measure representation rather than naming a moment theorem

<a id="lambda-moment"></a>

Put aₙ=λₙ₊₂,₂ and let E shift the sequence forwards. Recursion gives λ(b,k)=E^(b−k)(1−E)^(k−2)a₀, so these differences are nonnegative. For m≥1 define finite measures Mₘ.

\[ w_{m,j}=\binom mj\lambda_{m+2,m-j+2},\qquad
M_m=\sum_{j=0}^m w_{m,j}\delta_{j/m},\qquad
\sum_jw_{m,j}=a_0. \]

The last identity is [E+(1−E)]ᵐa₀=a₀. Likewise, with (j)ᵣ=j(j−1)…(j−r+1), the binomial identity gives Σ(j)ᵣ/(m)ᵣ wₘ,ⱼ=aᵣ. Uniformly for 0≤j≤m, (j/m)ʳ differs from this factorial ratio by Oᵣ(1/m), so the r-th moments of Mₘ tend to aᵣ. Fixed mass a₀ and compactness give a weak limit M with these moments. If a₀=0 all rates vanish and use the zero measure.

\[ \sum_{j=r}^m
\frac{(j)_r}{(m)_r}\binom mj
E^j(1-E)^{m-j}a_0
=E^r[E+(1-E)]^{m-r}a_0=a_r. \]

Bernstein polynomial approximation from Chapter 13 makes finite measures on a compact interval with identical moments equal. Thus M is unique. Push y to x=1−y to obtain Λ. The difference identity then yields the full rate representation, without invoking an unproved Hausdorff moment theorem.

\[ \lambda_{b,k}=\int_{[0,1]}
x^{k-2}(1-x)^{b-k}\Lambda(dx),\qquad
q_b=\sum_{k=2}^b\binom bk\lambda_{b,k}.
\quad 0^0=1. \]

## 3. All finite chains on one random space

<a id="lambda-construction"></a>

Write a=Λ{0}. For positive x use a Poisson measure of intensity dt x⁻²Λ(dx) du, where u∈[0,1]ᴺ has product-uniform law. At an atom mark current block B active exactly when \(u_{\min B}\)≤x, merging all active blocks; fewer than two gives no change. On [n], every effective event requires at least two of the first n uniforms below x, with probability at most binom(n,2)x². Effective rate is therefore at most binom(n,2)Λ((0,1]). The rate for a specified k-tuple active and all other current blocks inactive is precisely the positive-x part of the formula.

Independently put a rate-a Poisson clock on each integer pair i<j, acting only when i,j are current least representatives. Only finitely many such clocks matter on [n], supplying the Kingman atom at 0. Use the same noise for every n. A block meeting [n] has the same least representative there, so both constructions commute pathwise with restriction. Each finite chain has at most n−1 jumps. Their common construction gives a càdlàg path in the compact partition space.

Permutation covariance of finite generators gives path exchangeability. Cylinder semigroups are finite matrix semigroups, yielding Feller continuity, strong continuity and the grid-approximation strong Markov proof: first cylinders, then uniform approximation of continuous functions, then bounded limits along upper grid approximations of stopping times. These steps are the same finite-cylinder argument proved in T-HOMOGENEOUS-FRAGMENTATION. Mergers decrease block count, but finite projections remain nonexplosive.

## 4. A Kingman atom guarantees coming down from infinity

<a id="lambda-cdi"></a>

For a>0 let Nₙ(t) count blocks on [n] and τₘ be the first time at most m remain. Put f(b)=Σⱼ₌ₘ₊₁ᵇ1/[a binom(j,2)], and 0 for b≤m. For b>m the binary Kingman part gives Lf≤−1, and additional multiple jumps only decrease f. Finite-chain Dynkin with stopping gives Eτₘ≤f(n)≤2/(am). Markov’s inequality and monotonicity of Nₙ in n yield

\[ P(N(t)>m)
=\lim_nP(N_n(t)>m)\le\frac{2}{amt},\qquad t>0. \]

Let m increase: block count is finite almost surely at positive times. Intersect rational times and use nonincreasing block count for all positive times. For Λ=δ₁, all blocks remain singletons until the first rate 1 clock, then merge into one. Thus P(N(t)=∞)=e⁻ᵗ, so arbitrary Λ processes do not automatically come down from infinity. The most general integral criterion is not proved here.

## 5. Dust under finite marking intensity

<a id="lambda-dust"></a>

\[ a=0,\qquad
\beta=\int_{(0,1]}x^{-1}\Lambda(dx)<\infty
\quad\Longrightarrow\quad
D(t)=\prod_{(u,x):\,u\le t}(1-x),\qquad ED(t)=e^{-\beta t}. \]

Condition on Poisson event times and x values. Until its first marking each original singleton i uses its own uᵢ. Never-marked events are independent across i and have the displayed product probability. On bounded time intervals the Poisson sum of x is finite almost surely, so the product is positive before an x=1 event. At i’s first marking, simultaneously marked never-marked labels have positive frequency xD(u−), so i joins a positive-frequency nonsingleton block. An x=1 event merges all remaining singletons. Dust is exactly the frequency of never-marked labels. Conditional strong laws give the product formula and the Poisson functional gives its expectation.

For \(\Lambda=\delta_{1/2}\), D(t)=2⁻ᴷ⁽ᵗ⁾ with K a rate 4 Poisson count. Zero-frequency singletons collectively have positive dust, and merging can move them into positive-mass blocks. Their zero individual frequencies were not added as a countably additive measure on N. The full dust criterion when β is infinite does not follow automatically from this integrable formula.

## 6. Even two labels expose the conditions for reversal

<a id="lambda-reversal"></a>

Start two singletons with pair rate 1 and merger time E∼Exp(1). Reverse the path on a fixed interval [0,T]. Given that it is merged at reverse time u, its infinitesimal splitting rate is the ratio of forward state probabilities at s=T−u.

\[ r_{\rm rev}(u)=
\lim_{h\downarrow0}
\frac{P(s-h<E\le s)}{hP(E\le s)}
=\frac{e^{-(T-u)}}{1-e^{-(T-u)}},\qquad 0\le u<T. \]

This rate depends on time and diverges at the terminal point. Reversal has not automatically produced constant-rate homogeneous fragmentation. The observation interval and initial law were specified. Other initial laws, models and time changes may give genuine dualities, but require proofs of their own. General Ξ classification, CRT-cutting/additive-coalescent duality and population scaling are not proved here. Return to the [main text](../chapters/56-fragmentation-hierarchies.md#fragment-reversal).
