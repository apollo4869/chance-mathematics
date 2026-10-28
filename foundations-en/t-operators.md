# T-OPERATORS: From Short-Time Rates to Positive Contraction Semigroups

These are the operator tools used in Chapter 28. Initially X is a real Banach space; for positivity and maximum principles take X=C₀(E) on a locally compact Polish space. Unless stated otherwise, operator convergence means norm convergence on each vector.

## O.1 Continuous Vector Integrals Without an Unbuilt Theory

<a id="t-operators-integrals"></a>

A continuous v:[a,b]→X is uniformly continuous. Refine two tagged partitions together; the norm difference of their Riemann sums is bounded by interval length times the appropriate continuity modulus. The sums form a Cauchy family as the mesh tends to zero. Completeness supplies their unique integral. Addition, linearity and interchange with a bounded linear operator follow from finite sums by limits.

\[
\left\|\int_a^b v(s)\,ds\right\|\le\int_a^b\|v(s)\|\,ds,\qquad \frac{d}{dt}\int_a^t v(s)\,ds=v(t).
\]

The norm bound follows from the sums; the fundamental theorem follows by bounding the difference quotient error by the local modulus. A vector function F with continuous derivative satisfies the integrated fundamental theorem as well. Subtract the integral of F′ to form H; the proved integral derivative gives H′=0. For fixed a the absolute increment of the real function ‖H(t)−H(a)‖ is at most ‖H(t+h)−H(t)‖, so its derivative is zero. The real mean-value theorem makes this norm identically zero, without importing a scalar mean-value equality into a vector space. On an infinite interval an integrable norm bound makes the finite integrals Cauchy. Semigroup Laplace integrals are of this type.

## O.2 Density, Closedness and Time Differentiation

<a id="t-operators-generator"></a>

Let T be a strongly continuous contraction semigroup. Strong continuity holds at every time: use Tₜ(Tₕ−I) for right differences and Tₜ₋ₕ(Tₕ−I) for left differences, with contraction. For f in D(A), these difference quotients prove domain invariance and the following identities.

\[
AT_tf=T_tAf,\qquad \frac{d}{dt}T_tf=T_tAf,\qquad T_tf-f=\int_0^tT_sAf\,ds.
\]

For arbitrary f let uₜ be its time average. Apply Tₕ, shift integration endpoints, divide by h and use continuity to compute its generator. The averages converge in norm to f, proving domain density.

\[
u_t=\frac1t\int_0^tT_sf\,ds,\qquad Au_t=\frac{T_tf-f}{t}.
\]

If fₙ→f and Afₙ→g, contraction permits passage through the integral identity to obtain Tₜf−f=∫Tₛg. Divide by t and use strong continuity to get Af=g. Thus A is closed.

## O.3 Both Resolvent Inverses and Their Consistency

<a id="t-operators-resolvent"></a>

\[
R_\lambda f=\int_0^\infty e^{-\lambda t}T_tf\,dt,\qquad\|R_\lambda\|\le1/\lambda.
\]

For a positive semigroup, the Riemann sums and norm limit for nonnegative f are nonnegative, so Rλ is positive. For positive h, apply Tₕ and change variables. The difference quotient in the identity below tends in X to λRλf−f, proving domain membership and (λ−A)Rλf=f.

\[
T_hR_\lambda f=e^{\lambda h}\left(R_\lambda f-\int_0^h e^{-\lambda s}T_sf\,ds\right).
\]

For a domain element, the derivative of the discounted Tₜf is the discounted Tₜ(A−λ)f. Integrate to N and let N tend to infinity to obtain Rλ(λ−A)f=f. Thus λ−A is bijective with inverse Rλ. Apply this bijection to the difference of two resolvents to obtain the next formula; exchanging λ and μ proves commutativity.

\[
(\lambda-A)(R_\lambda-R_\mu)f=(\mu-\lambda)R_\mu f,\qquad R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu.
\]

Finally λRλf−f is the exponential average of Tₜf−f. Split at δ: strong continuity controls the initial interval, and twice the norm times the exponential tail controls the rest. Let λ increase and then δ decrease to obtain λRλf→f.

## O.4 Closability and All Resolvents from the Maximum Principle

<a id="t-operators-maximum"></a>

Let A be densely defined on real C₀ and satisfy the positive maximum principle. At a positive norm extremum apply the principle to f, and at a negative one to −f. Applying it to −f at the most negative point also gives the negative-part estimate. For every positive λ one obtains both bounds.

\[
\lambda\|f\|\le\|(\lambda-A)f\|,\qquad\lambda\|f^-\|\le\|((\lambda-A)f)^-\|.
\]

Closability does not follow by merely asserting the first bound. Suppose fₙ→0 and Afₙ→g. Fix a domain element u, apply the first bound with parameter λ to u+λfₙ and let n tend to infinity. This gives the next inequality. Letting λ increase gives ‖u−g‖≥‖u‖; density then allows u→g, forcing g=0.

\[
\|u\|\le\|u-\lambda^{-1}Au-g\|.
\]

Let B be the graph closure. Both bounds persist under graph convergence. The range of λ−B is closed: Cauchy outputs make inputs Cauchy by the first bound, and their B-images Cauchy as well; closedness gives a limiting input. If the original range is dense at λ₀, then λ₀−B is surjective and injective with inverse norm at most 1/λ₀.

\[
R_\mu=R_\lambda[I+(\mu-\lambda)R_\lambda]^{-1}\quad\text{if }|\mu-\lambda|<\lambda.
\]

The Neumann series supplies inverses for nearby parameters. Starting at λ₀ covers (0,2λ₀); moving through 3λ₀/2 and successive factors of 3/2 covers the positive axis. Each inverse norm bound follows anew from the first inequality for B. Positivity is not guessed from an alternating Neumann series: the second inequality says (μ−B)f≥0 implies f⁻=0. Thus every resolvent is positive with norm at most 1/μ.

## O.5 Actual Semigroup Construction by Yosida Limits

<a id="t-operators-generation"></a>

Assume now that A is closed and densely defined, with bijective inverses Rλ and contraction bounds for all positive λ; on C₀ also assume their positivity. No semigroup is assumed. The inverse relations algebraically give the resolvent identity and commutativity. For a domain element, λRλf−f=RλAf→0, and the norm bound extends this by density. Define the following bounded operators.

\[
A_\lambda=\lambda^2R_\lambda-\lambda I,\qquad S_\lambda(t)=e^{-\lambda t}\sum_{k\ge0}\frac{(\lambda t)^k}{k!}(\lambda R_\lambda)^k.
\]

The series converges absolutely in operator norm, giving contraction semigroups and preserving positivity termwise. On the domain, Aλf=λRλAf→Af. The Aλ commute. Differentiate Sλ(t−s)Sμ(s) and integrate to get the next identity; contraction gives a bound involving only the fixed vector f.

\[
S_\mu(t)f-S_\lambda(t)f=\int_0^tS_\lambda(t-s)S_\mu(s)(A_\mu-A_\lambda)f\,ds,\quad\sup_{t\le T}\|S_\mu(t)f-S_\lambda(t)f\|\le T\|(A_\mu-A_\lambda)f\|.
\]

This is a Cauchy family on compact time intervals on the dense domain. Approximate an arbitrary f by a domain element and use contraction twice to extend it. The limit Tₜ is contractive and positive. Product limits give the semigroup law. Uniform approximation on compact time intervals by the strongly continuous Sλ gives strong continuity.

Let G generate T. For f in D(A), pass to the limit in the bounded-operator integral identity to get Tₜf−f=∫TₛAf, hence A⊂G. For equality take g in D(G) and put f=Rλ(λ−G)g. Then f lies in D(A) and (λ−G)(g−f)=0. Sections O.2–O.3 proved injectivity of λ−G for every contraction semigroup, so g=f. There is no extra domain, and G=A.

If T and S have the same generator, the derivative of s↦Sₜ₋ₛTₛf vanishes for domain elements by invariance and cancellation. Thus Tₜf=Sₜf, and density extends equality. Together with O.4 this proves the probabilistic Hille–Yosida theorem. Conversely, at a nonnegative maximum M, positivity gives Tₜf≤Tₜf⁺≤‖f⁺‖=M, giving the principle by difference quotients; O.3 gives all full ranges.

## O.6 A Core Criterion and a Useful Sufficient Condition

<a id="t-operators-core"></a>

Let D₀ be a linear subspace of D(A). If (λ−A)D₀ is dense, choose fₙ in D₀ whose outputs approximate (λ−A)f. Bounded Rλ gives fₙ→f; then Afₙ=λfₙ−output→Af. Conversely graph density immediately gives range density. This proves the core equivalence in the chapter.

A useful sufficient condition is that D₀ is dense in X and invariant under every Tₜ. For g in D₀, finite-time Riemann sums for Rλg belong to D₀, while their A-images converge to the integral of discounted TₜAg. Both tails are exponentially controlled, giving graph convergence to Rλg. Approximate arbitrary g by D₀ and use ARλ=λRλ−I for graph convergence again. Since Rλ ranges over the entire domain, D₀ is a core. Supremum-norm density alone, without invariance or range control, is insufficient.

This companion proves the contraction case and its positive C₀ version. A bound ‖Tₜ‖≤exp(ωt) with prefactor exactly one reduces to contraction by shifting the generator by ω. A general bound with prefactor M>1 cannot become contractive merely by that shift; its Hille–Yosida resolvent-power version is outside the proved scope.
