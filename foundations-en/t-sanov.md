# T-SANOV: Polish Empirical Measures, Entropy Variation and Exponential Tightness

Let E be Polish, μ any Borel probability, Xᵢ iid with law μ, and Lₙ the empirical measure with the weak topology on probability laws. The finite-sample map to Lₙ is continuous: every bounded continuous test has a continuous sample average, and these readings define the weak topology. Thus Lₙ is a measurable random probability measure.

## S.1 Relative Entropy and Bounded Borel Exponential Tests

<a id="t-sanov-entropy"></a>

For ν≪μ choose density ρ and put H=∫ρ logρ dμ; otherwise H=∞. With 0 log0=0 its negative part is at most 1/e, so the definition is unambiguous. Integrating r log r−r+1≥0 gives H≥0, with equality exactly when ν=μ. For bounded Borel f, Z=μeᶠ is strictly positive and finite; set μf=eᶠμ/Z. When H is finite each term in the log-density decomposition is integrable; when H is infinite the resulting inequality is trivial.

\[
0\le H(\nu\mid\mu_f)=H(\nu\mid\mu)-\nu f+\log\mu e^f,\qquad\nu f-\log\mu e^f\le H(\nu\mid\mu).
\]

For the reverse inequality when ν≪μ, truncate logρ to [−M,M], truncating log0=−∞ from below. The density is positive and finite ν-almost surely. Monotone convergence for the positive part and domination by the integrable negative log-density give νfᴹ→H, including infinite H. Also exp(fᴹ)→ρ μ-almost surely with bound ρ+1, hence μ exp(fᴹ)→1. If ν is not absolutely continuous, choose μ(A)=0<ν(A) and f=M1_A, whose expression is Mν(A)→∞.

\[
H(\nu\mid\mu)=\sup_{f\in B_b(E)}\{\nu f-\log\mu e^f\}.
\]

## S.2 Why Continuous Tests Suffice

Fix the finite measure η=μ+ν. For open U, min(1,k times distance to Uᶜ) increases to its indicator; use one for U=E. These continuous [0,1] functions approximate the indicator in L¹(η). The class admitting such approximation is closed under complements using one minus the approximation and under finite unions using maxima. For countable unions, truncate to a finite union using continuity from below, then diagonalize the approximations. Thus it is a σ-algebra containing the open sets and all Borel sets.

Quantize a bounded Borel |f|≤M into simple functions, approximate their finitely many indicators continuously, and clip the result to [−M,M]. This gives equally bounded gₖ∈C_b converging in L¹(η). The exponential is Lipschitz on this fixed bounded interval, so μeᵍᵏ→μeᶠ and νgₖ→νf. Approximate at fixed f and M first, then take the supremum from S.1; no single Lipschitz constant is used while M increases.

\[
H(\nu\mid\mu)=\sup_{f\in C_b(E)}\{\nu f-\log\mu e^f\}.
\]

Thus H is a supremum of weakly continuous affine functions, hence weakly lower-semicontinuous and convex. This approximation uses only a metric and finite measures, not Chapter 28’s locally compact C₀ representation theorem outside its scope.

## S.3 Compact Entropy Sublevels, Separately from Sample Exponential Tightness

<a id="t-sanov-goodness"></a>

For A with 0<p=μ(A)<1 use f=log(1/p)1_A in the B_b variational expression. Since μeᶠ=2−p≤2, it gives the following bound. If p=0, finite-entropy absolute continuity directly gives ν(A)=0.

\[
\nu(A)\log(1/p)\le H(\nu\mid\mu)+\log2.
\]

Given an entropy bound M and tail tolerance ε, tightness of μ on Polish E supplies compact K with very small μ-tail. The bound makes every ν with H≤M have tail at most ε. These laws are uniformly tight; S.2 makes the sublevel closed, and Chapter 24’s Prokhorov theorem makes it compact. The zero-cost law μ ensures a nonempty rate.

For the underlying tightness mechanism, cover E at each scale 2⁻ᵏ by balls centered at a countable dense set. Retain finitely many with omitted mass at most ε2⁻ᵏ; enlarge to closed balls of comparable radius and intersect their finite unions over all scales. The intersection is closed and totally bounded, hence compact by completeness. The union bound gives mass at least 1−ε.

## S.4 Sanov’s Open Lower and Compact Upper Bounds

<a id="t-sanov-proof"></a>

Let G be weakly open and ν∈G have finite entropy. A basic neighborhood inside G uses finitely many bounded continuous tests. Under ν-sampling their empirical readings converge to νf by laws of large numbers, so Lₙ enters G with probability tending to one. Mean logρ also converges to H. Apply [T-LDP’s finite likelihood lemma](t-ldp.md#t-ldp-likelihood) on the intersection to get a μ lower rate at least −H. Optimize over ν for the open lower bound.

For the compact upper bound fix compact C and b<inf_C H. For each ν∈C, S.2 supplies f with νf−log μeᶠ>b, defining a weak neighborhood Uν. Independence gives Eμ exp(nLₙf)=(μeᶠ)ⁿ, and exponential Markov gives Pμ(Lₙ∈Uν)≤e⁻ⁿᵇ. A finite subcover bounds C by a finite multiple of e⁻ⁿᵇ. Increase b to the infimal entropy, arbitrarily far when it is infinite.

## S.5 Empirical Exponential Tightness with Explicit Parameters

<a id="t-sanov-exponential-tightness"></a>

For L>0 and j≥1 choose δⱼ and θⱼ below. Tightness supplies compact Kⱼ with pⱼ=μ(Kⱼᶜ)≤e⁻ᶿʲ; take finite unions to make Kⱼ increasing. Define the following set of probability measures.

\[
\delta_j=2^{-j},\qquad\theta_j=\frac{L+j+1}{\delta_j},\qquad\mathcal K_L=\bigcap_{j\ge1}\{\nu:\nu(K_j^c)\le\delta_j\}.
\]

Since Kⱼᶜ is open, Portmanteau makes ν↦ν(Kⱼᶜ) lower-semicontinuous, so each upper constraint is closed. As δⱼ→0 the family is uniformly tight; Prokhorov makes the closed set compact. For actual empirical measures, nLₙ(Kⱼᶜ) is binomial with parameter pⱼ, and Chernoff gives the full bound.

\[
\begin{aligned}P\{L_n(K_j^c)>\delta_j\}&\le\exp\{-n[\theta_j\delta_j-\log(1+p_j(e^{\theta_j}-1))]\}\\&\le e^{-n(L+j)},\\P\{L_n\notin\mathcal K_L\}&\le\sum_{j\ge1}e^{-n(L+j)}=\frac{e^{-nL}}{e^n-1}\le e^{-nL}.\end{aligned}
\]

The middle step uses only log(1+u)≤u and pⱼ exp(θⱼ)≤1. No integrality or lower bound on nδⱼ is assumed. All tail constraints are controlled together; an infinite union has not been treated as finite.

## S.6 The Full Closed Upper Bound and Its Topology

Split closed F into F∩𝒦ᴸ and escape from 𝒦ᴸ, using S.4 and S.5. The finite-sum upper rate is at most max{−inf_F H,−L}. Let L increase for the closed bound. S.4 and S.3 already provide the lower bound and goodness, completing Sanov.

No moment condition is imposed on μ. Both the rate and exponential tightness concern the weak topology, not arbitrary unbounded moments or Wasserstein topologies. The chapter’s escaping-mass example shows why the distinction matters.
