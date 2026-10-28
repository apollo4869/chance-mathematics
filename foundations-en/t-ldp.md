# T-LDP: Exponential Scales, Finite-Dimensional Convex Closure and Cramér’s Full Lower Bound

Use Chapter 29’s definition of an LDP with speed aₙ→∞. The Cramér part concerns iid samples in finite-dimensional Rᵈ, with Λ finite near zero. Neither Gärtner–Ellis, Sanov nor an unproved convex duality theorem is used.

## L.1 Exponential Sums, Differences and Compact Truncation

<a id="t-ldp-elementary"></a>

For finitely many nonnegative terms, the sum lies between the maximum and the number of terms times the maximum. Divide its logarithm by aₙ; the extra constant disappears. Thus the upper exponential rate of a finite sum is at most the maximum of the upper rates, and retaining one term gives a lower bound.

Subtraction needs a strict exponential gap. If liminf log Aₙ/aₙ≥−a and limsup log Bₙ/aₙ≤−b with 0≤a<b, choose η>0 with a+η<b−η. Eventually Aₙ≥exp(−(a+η)aₙ) and Bₙ≤exp(−(b−η)aₙ), so Bₙ/Aₙ→0. Thus Aₙ−Bₙ is eventually positive with lower rate at least −a. Merely knowing that both terms vanish does not suffice.

Open lower bounds, compact upper bounds and exponential tightness give closed upper bounds by splitting closed F into F∩Kᴸ and escape from Kᴸ. Their rates are at most −inf_F I and −L. Let L increase. No assertion that a neighborhood of a compact set is compact is needed.

## L.2 The Exact Finite-Sample Change-of-Measure Inequality

<a id="t-ldp-likelihood"></a>

Let ν≪μ with density ρ. Integrating r log r−r+1≥0 proves nonnegative relative entropy. If H is finite, logρ is ν-integrable: its negative integral is at most 1/e, and finite H then controls its positive part. The set 0<ρ<∞ has full ν-mass, making the finite-product likelihood well-defined there.

\[
\int_{\{0<\rho<1\}}\rho|\log\rho|\,d\mu\le1/e,\qquad \mu^{\otimes n}(A)\ge E_{\nu^{\otimes n}}\!\left[\mathbf1_A\exp\left\{-\sum_{i=1}^n\log\rho(X_i)\right\}\right].
\]

The right side equals the μ-product mass of A restricted to {0<ρ<∞}ⁿ; the set where ρ is infinite is μ-null. The support of ν need not cover μ, so this is generally an inequality. If a ν-integrable vector g has mean in open G, the law of large numbers for g and logρ gives the following lower bound. Chapter 12’s integrable iid strong law is available, though convergence in probability would suffice.

\[
\liminf_n\frac1n\log\mu^{\otimes n}\left\{\frac1n\sum_i g(X_i)\in G\right\}\ge-H(\nu\mid\mu).
\]

Intersect the event with mean logρ≤H+δ, whose ν-product probability tends to one. Pull out exp(−n(H+δ)) and finally let δ decrease. This makes no Radon–Nikodym assertion between infinite product measures.

## L.3 Convex Closure from Nearest-Point Separation

<a id="t-ldp-convex"></a>

Let J:Rᵈ→[0,∞] be convex and finite somewhere. Define its lower-semicontinuous closure below. Its epigraph is the closure of the original epigraph in Rᵈ⁺¹: local infima give one direction, and nearby points with heights above J give the other. The closure is convex and all heights are nonnegative.

\[
\overline J(x)=\lim_{\delta\downarrow0}\inf_{|y-x|<\delta}J(y),\qquad J^*(\theta)=\sup_y\{\langle\theta,y\rangle-J(y)\}.
\]

For r<the closure value at x, z=(x,r) lies outside the closed convex epigraph C. A nearest point p exists: restrict a minimizing sequence to a bounded ball and use finite-dimensional compactness. Comparing squared distances to p+t(w−p) gives (p−z)·(w−p)≥0. Thus some (α,β) and c satisfy α·y+βs≥c throughout C but α·x+βr<c.

The upward-unbounded epigraph forces β≥0. If β=0, add a sufficiently small positive vertical coefficient. All s≥0, so the epigraph side cannot decrease and strict separation at z persists. Thus β>0 is possible, yielding a continuous affine minorant ℓ(y)=(c−α·y)/β with ℓ≤J and ℓ(x)>r.

With θ=−α/β, the minorant gives J*(θ)≤−c/β, hence θ·x−J*(θ)>r. Conversely every θ·x−J*(θ) is a continuous affine minorant of J and remains so on the closed epigraph. Increase r to the closure value, or arbitrarily far if it is infinite, to prove that the biconjugate equals the closure. Neither full-dimensional support nor exposed points are assumed.

\[
J^{**}=\overline J,\qquad \inf_GJ=\inf_G\overline J\quad\text{for every open }G.
\]

One direction of the second identity follows because the closure is at most J. For the other, approximate a finite closure value at x∈G by yₖ→x with J(yₖ) approaching that value. Eventually yₖ∈G; take infima. This identity does not hold generally on closed sets and is not used for the closed upper bound.

## L.4 Why Entropy Under a Mean Constraint Has Conjugate Λ

<a id="t-ldp-cramer-lower"></a>

Define J as in the chapter by minimizing entropy over laws with finite first moment and the specified mean. Exponential moments near zero give μ a finite first moment, so J vanishes at its mean. Convexity of r log r gives entropy convexity under density mixtures, and mixing approximate minimizers proves convexity of J. The previous section applies without existence of minimizing laws.

For finite Λ(θ), the tilted μθ has strictly positive density. If ν has finite entropy and first moment, its log density relative to μθ is logρ−θ·X+Λ(θ), each term ν-integrable. Nonnegative entropy gives the inequality below; infinite original entropy makes it trivial.

\[
H(\nu\mid\mu)\ge\langle\theta,E_\nu X\rangle-\Lambda(\theta),\qquad J^*(\theta)\le\Lambda(\theta).
\]

Conversely fix any θ without requiring finite Λ(θ). Let Mᴿ be the μ-integral of exp(θ·X) restricted to |X|≤R, positive for sufficiently large R. Normalize this restricted tilt to νᴿ. Its X and log density are bounded on its support, so its entropy is finite. For its mean xᴿ one has the next identity and inequality.

\[
H(\nu^R\mid\mu)=\langle\theta,x^R\rangle-\log M^R,\qquad J^*(\theta)\ge\langle\theta,x^R\rangle-J(x^R)\ge\log M^R\uparrow\Lambda(\theta).
\]

Monotone convergence includes infinite Λ, so J*=Λ throughout Rᵈ. The preceding section gives the closure of J as Λ*. The likelihood lemma now makes the open lower rate at least −inf_G J=−inf_G Λ*, proving Cramér’s lower bound at every point.

## L.5 Local Upper Bounds, Exponential Tightness and Goodness

Exponential Markov gives the chapter’s ball bound for x, δ and finite Λ(θ). If inf_K I>b for compact K, choose θ at each point and shrink the ball to make its bound exceed b in cost. A finite subcover bounds its probability by a finite multiple of e⁻ⁿᵇ. Increase b to inf_K I, arbitrarily far if that infimum is infinite.

Choose η>0 with finite exponential moments at every ±ηeⱼ, and let C be their largest Λ. Coordinate union bounds make escape from the R-cube at most 2d exp(−n(ηR−C)), proving exponential tightness. The same tests give I(x)≥η‖x‖∞−C, while the affine supremum makes I lower-semicontinuous. Its closed bounded sublevels are compact in finite dimensions. Thus exponential tightness and goodness are separately proved. L.1 gives closed upper bounds, completing the theorem with L.4.

## L.6 Full Open and Closed Proofs for Exponential Equivalence

<a id="t-ldp-equivalence"></a>

Suppose Zₙ has an LDP with good rate I and shares its metric and probability spaces with Yₙ. Assume every positive distance error is superexponentially unlikely. For closed F, its closed δ-neighborhood and the union bound give a Y upper rate at most −inf_Fδ I.

As δ decreases, these infima tend to inf_F I. Otherwise choose δₖ→0 and xₖ at distance at most δₖ from F with costs below a finite number strictly less than inf_F I. Goodness gives a convergent subsequence; continuity of distance puts its limit in F, and lower semicontinuity preserves the low cost, a contradiction. If inf_F I is infinite, argue at each finite cost level.

For open G and finite-cost x∈G choose r with B(x,2r)⊂G. If Z lies in B(x,r) and the distance error is less than r, then Y∈G. The ball has lower rate at least −I(x), while the error has arbitrarily negative upper rate. L.1’s subtraction lemma gives the same Y lower bound. Optimize over x; if no finite-cost point exists the lower bound is trivial. The good rate is unchanged.

Neither ordinary weak convergence nor a fixed-grid exponentially good approximation is treated here as an LDP or as exponential equivalence. T-SCHILDER proves that construction with its proper limit order.
