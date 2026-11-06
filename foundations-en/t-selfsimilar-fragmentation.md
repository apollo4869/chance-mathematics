# T-SELFSIMILAR-FRAGMENTATION: All Real Indices, Erosion and Explosion for Finite Dislocation Measures

This page proves the precise scope used in [Chapter 56](../chapters/56-fragmentation-hierarchies.md#fragment-selfsimilar): finite ν with ν{(1,0,…)}=0, c≥0 and arbitrary real α, allowing countably many children, dissipative splits and finite-time shattering. The block-dependent stopping-line time change for infinite ν is not proved here and is not replaced by this finite-ν theorem.

## 1. A local clock constructs each fragment path

<a id="selfsim-clock"></a>

Put λ=ν(S↓). On countably many Ulam–Harris vertices choose independent Eᵥ∼Exp(λ) and sᵥ∼ν/λ; if λ=0 set E=∞ and draw no s. A fragment born with mass m>0 has remaining mass m e⁻ᶜᵘ at operational age u and physical age Aₘ(u). At u=E it gives children of mass m e⁻ᶜᴱsᵢ, with the remainder becoming dust.

\[ A_m(u)=\int_0^u(me^{-cr})^{-\alpha}\,dr
=m^{-\alpha}
\begin{cases}
(e^{\alpha cu}-1)/(\alpha c),&\alpha c\ne0,\\
u,&\alpha c=0 .
\end{cases} \]

While mass is positive A is continuous and strictly increasing; its inverse determines mass at physical time. If u tends to infinity while A has a finite endpoint, put mass 0 at and after that endpoint. Differentiation gives x′(t)=−c x(t)^(α+1). The operational exponential clock has physical jump rate λx(t)^α, not λx(t)^(−α). Children repeat the same independent construction.

## 2. An interval realization makes mass and exchangeability checkable

<a id="selfsim-intervals"></a>

Start from [0,1). Each vertex has a half-open interval J whose length is its birth mass. At operational age u retain its leftmost length m e⁻ᶜᵘ and erode the right end. At a split partition the remaining interval into countably many half-open child intervals in the order of s; the unallocated tail is dust. Birth intervals and endpoints are measurable functions of finitely many random variables, and tree addresses are countable, so the environment is measurable.

Independently draw iid uniform Uᵢ. At t, labels in one current positive-length interval share a block and all others are singletons. A tag following infinitely many births in finite time becomes dust when its mass tends to zero. Two distinct U values cannot lie in the same zero-length intersection of nested intervals, so no zero-mass nonsingleton block is created. Half-open conventions remove a tag exactly when the moving erosion boundary reaches it.

## 3. Explosion requires an actual construction

<a id="selfsim-explosion"></a>

First truncate at a finite generation. At any time at most 1/ε intervals have mass at least ε; each has split rate at most λ max(1,ε^α). Total large-block rate is bounded by a constant Cε. Finite-generation exponential competition, or bounded-rate Poisson clocks with null jumps, bounds the expected number of such splits by Cεt. These event counts increase with the generation cutoff, so monotone convergence proves finiteness in the full construction. Erosion decreases mass and cannot violate the bound.

Consequently infinitely many ancestral splits in finite time must have masses tending to zero; otherwise some ε-large block would split infinitely often. If two distinct tags never separate, they lie in one nested interval throughout. At a finite accumulation time its length tends to zero and would force their U values equal, an event of probability zero. Intersect over countably many label pairs. Each pair then has a legitimate separation time, and [n] has at most n−1 effective refinements, giving a right-continuous finite path. All restrictions use the same U values and environment, hence are consistent. The infinite partition path is càdlàg and exchangeable.

Apply the uniform empirical-distribution strong law proved in T-HOMOGENEOUS-FRAGMENTATION to the uniform samples on the whole interval. Frequencies converge to length simultaneously for all intervals, including these random endpoints and all times. Thus positive block masses really are interval lengths, not a separately guessed assignment. The separation-time proof on that page gives simultaneous ranked-mass and dust versions; càdlàg is asserted in the coordinate topology only.

## 4. Markov branching and the self-similar identity

<a id="selfsim-markov"></a>

Given the positive-interval environment revealed up to the current time and the past, unused descendant environments remain independent, and residual operational exponential waits are memoryless. Conditional on this past environment and past label classifications, surviving tags remain conditionally independent uniform in their current intervals: past ancestral constraints contain the current interval and impose no smaller restriction. Prove this first for finitely many tags and past times by product-Lebesgue conditioning, then extend by the monotone class theorem. No internal label order is privileged.

\[ \mathcal L\big(X^{(x)}(t)\big)
=\mathcal L\!\left(
\operatorname{rank}\{x_i X_j^{(i)}(x_i^\alpha t):i,j\ge1\}
\right),\qquad X^{(i)}\ \text{independent unit copies}. \]

The clock identity Aₘ=m⁻ᵅA₁ makes the independent future of a mass-m block equal to m times a unit process sped up by m^α. Block frequencies are Borel functions of the current infinite partition. Its future kernel depends on these frequencies and current membership, not interval positions. Conditioning again gives the partition Markov property and, after ranking, the mass Markov property. Dust singletons are absorbing. For α≠0 finite observations alone generally are not Markov, since they need not reveal true block masses. Consistency means path restriction of one process, not a fictitious family of mass-blind finite Markov generators.

## 5. A computable mass-generator relation

<a id="selfsim-generator"></a>

\[ \begin{aligned}
F_q(x)&=\sum_i x_i^{q+1},\qquad q>0,\quad q+\alpha\ge0,\\
\mathcal A_\alpha F_q(x)
&=-\left[c(q+1)+\int(1-\sum_j s_j^{q+1})\nu(ds)\right]
\sum_i x_i^{q+1+\alpha}.
\end{aligned} \]

This is the pointwise right derivative at 0 of the expectation semigroup. Starting from mass 1, no split gives erosion derivative −c(q+1). The first split has probability λt+o(t), and its conditional offspring contribution tends to Σsⱼ^(q+1); subsequent small pieces are controlled by a nonnegative sum at most 1. This yields the negative bracketed coefficient. Exchanging infinitely many initial blocks with differentiation still requires proof. Write f(t)=E Fq(X(t)) for the unit process. Locally bounded initial positive-mass rates give |f(t)−1|≤Ct for small t; f∈[0,1] extends the bound to all t after enlarging C.

Branching gives expectation Σxᵢ^(q+1)f(xᵢ^αt). Its difference quotient is dominated by CΣxᵢ^(q+1+α). Since q+α≥0 this is at most CΣxᵢ≤C, proving the formula by dominated convergence. Zero masses contribute 0 without evaluating negative powers of 0. Without that integrability condition the sum may diverge; no finite derivative is asserted.

## 6. Conservation at nonnegative indices and shattering at negative indices

<a id="selfsim-conservation"></a>

If Σsᵢ=1 for ν-almost every s and c=0, then α≥0 gives conservation at all times. A typical uniform tag chooses children by size bias and never chooses dust. Its successive operational waits are iid Exp(λ) with divergent sum almost surely. Physical waits m⁻ᵅE≥E prevent infinitely many splits in finite time. Exchangeability and paintbox give ES(t)=P(the typical tag is still in a positive block)=1. Rational times and monotonicity give all-time conservation; λ=0 is immediate.

\[ \nu=\delta_{(1/2,1/2,0,\ldots)},\quad c=0,\quad\alpha<0:
\qquad
\zeta_{\rm tag}=\sum_{k\ge0}2^{\alpha k}E_k<\infty\quad\text{a.s.} \]

Every binary split conserves mass, but a negative index accelerates small blocks and the typical tag undergoes infinitely many splits in finite time. In fact the entire tree becomes dust in finite time. Let Mₖ be the maximum of the 2ᵏ independent Exp(1) waits at generation k. Tail integration of P(Mₖ>u)≤min(1,2ᵏe⁻ᵘ) gives EMₖ≤1+k log 2. The variable Z=Σ2^{αk}Mₖ has finite expectation and is almost surely finite, dominating all genealogical lifetimes. After Z no positive block remains and S=0. This fully proves that conservative dislocations need not conserve total process mass.

## 7. The three conditions do not replace one another

<a id="selfsim-counterexamples"></a>

Unit dislocation mass at (1/3,1/3,0,…), α=0 and c=0 gives an exchangeable self-similar but nonconservative process. Conversely use binary equal splitting with rate r(x)=1+x for a block of absolute mass x. Blocks are independent, exchangeable and mass-conservative: rates are bounded by 2, so a typical tag cannot split infinitely often in finite time. Self-similarity would require r(x)=r(1)x^α. At x=1/2,1/4 this requires.75 and .625 to be the first and second powers of the same number, but.75²≠.625.

If one specifically isolates label 1 while keeping all other labels together, total positive frequency stays 1 but the law is not exchangeable: the three-label pattern {1}|{2,3} changes under swapping 1,2. Conservation does not repair label preference. Infinite-ν self-similar extensions, general conservation equivalences and special CRT fragmentation indices do not follow from this proof. Return to the [main text](../chapters/56-fragmentation-hierarchies.md#fragment-three-conditions).
