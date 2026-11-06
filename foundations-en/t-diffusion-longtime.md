# T-DIFFUSION-LONGTIME: Comparison, Recurrence and Speed Equilibrium

A companion to [Chapter 36](../chapters/36-scale-speed.md#diffusion-comparison). Work with the nondegenerate locally Lipschitz SDE on I. Comparison is stopped on common compact intervals. Unless stated otherwise, long-term results assume inaccessible endpoints and a conservative minimal process. Use this chapter’s hitting, Green and discounted kernels and Chapter 12’s iid law of large numbers, not Chapter 41 ergodic or Chapter 42 Harris theory.

## 1. Same-Noise Comparison without Tanaka

<a id="diffusion-order"></a>

Let dXᵢ=bᵢ(Xᵢ)dt+σ(Xᵢ)dW with common σ,W, b₁≤b₂ and ordered initial values. Stop at the first exit of either state from a common compact interval, with common Lipschitz constant L. Put Z=X¹−X². Use Chapter 35’s φₙ approximating |z| with ρ(u)=Lu; if L=0 the diffusion difference is zero and no second-order estimate is needed. Let ψₙ=(φₙ+z)/2. Then 0≤ψₙ′≤1,ψₙ→z⁺, and ψₙ′=0 for z≤−aₙ₋₁; in its remaining negative band |z|≤aₙ₋₁.

The drift difference is ≤b₁(X¹)−b₁(X²)≤L|Z|. After multiplying by ψₙ′, positive Z contributes at most LZ⁺ and the negative band at most Laₙ₋₁. The second-order diffusion contribution is ≤C/n because φₙ″(z)L²z²≤2/n. Stopped Itô and mean-zero martingales yield the inequality below. Since Z₀≤0, ψₙ(Z₀)≤0 and tends to zero; its absolute approximation error is at most aₙ₋₁.

\[ E\psi_n(Z_{t\wedge\tau})\le a_{n-1}+L\int_0^tE(Z_{s\wedge\tau})^+ds+La_{n-1}t+Ct/n. \]

Let n→∞ by stopped bounded DCT and apply Gronwall to get E Zₜ∧τ⁺=0. Rational times and countable compact exhaustion give path order before common lifetime. Different σ destroys it already for dX=dW,dY=2dW from zero with equal drift. With all coefficients identical, uniqueness after first meeting directly gives monotonicity in the initial value, the simpler case used in the entrance construction.

## 2. Recurrence and the Clock Argument for Endpoint Limits

<a id="diffusion-recurrence-proof"></a>

If S(ℓ)=−∞,S(r)=∞, then for x>a the probability P(\(\tau_b<\tau_a\))→0 makes \(\tau_a\) finite almost surely; use the mirror from below. Each a→b→a cycle is finite, and strong Markov iterates infinitely many cycles. Endpoints are inaccessible and lifetime infinite; these crossings cannot accumulate at finite time by boundary proof 1.

If both scales are finite, Y=S(X) is a bounded continuous martingale. First apply Chapter 15’s discrete martingale convergence at integer times. Also E[Y]ₜ=E(Yₜ−Y₀)²≤C, so MCT gives finite E[Y]∞. Doob bounds the expected squared oscillation relative to Yₙ on [n,n+1] by 4E([Y]ₙ₊₁−[Y]ₙ). These expectations are summable, so the oscillations vanish almost surely. Thus the full continuous-time process converges to finite Y∞ and [Y]∞ is finite almost surely. An interior limit would keep X eventually in a compact interval with pσ bounded below, forcing [Y]∞=∫₀∞p(X)²σ(X)²dt=∞. Thus only endpoint values occur. DCT preserves the mean S(x), giving the two-point mixture formula.

If S(r)<∞,S(ℓ)=−∞, put Z=S(r)−S(X)≥0. A nonnegative local martingale is a supermartingale converging finitely, by stopped Fatou and upcrossings, without global L². The maximal inequality gives P(supZ≥K)≤Z₀/K, hence finite supremum almost surely. Stopping on first Z≥K gives a bounded process by continuity, and the preceding argument gives finite total bracket. On paths never reaching K this is the original bracket; take the union over K. A positive finite Z∞ would yield an interior limiting X with infinite clock, a contradiction. Thus Z∞=0 and X→r. The opposite case is symmetric. No diffusion ergodic theorem or general DDS time change is required.

## 3. Invariant Probability: From Symmetric Resolvents to Stationarity

<a id="diffusion-invariance-proof"></a>

Assume inaccessible endpoints and m(I)<∞. T-SCALE-SPEED 4 proves m-symmetry of the minimal resolvent. Conservativity gives Rλ1=1/λ. For bounded nonnegative f, Tonelli and symmetry yield

\[ \int_I R_\lambda f\,dm=\int_I fR_\lambda1\,dm=\lambda^{-1}\int_If\,dm,\qquad \int_0^\infty e^{-\lambda t}\!\left(\int_IP_tf\,dm\right)dt=\lambda^{-1}\int_If\,dm. \]

For bounded continuous f, h(t)=∫Pₜf dm is bounded continuous by path continuity and two applications of DCT. Its Laplace transform for every positive λ is that of a constant, hence h is that constant. To verify uniqueness directly, for bounded continuous difference g use integer λ=n+1 and u=e⁻ᵗ. The finite signed measure g(−logu)du on [0,1] has all polynomial moments zero. Chapter 13’s Bernstein approximation makes it zero, and continuity gives g=0 everywhere. Thus normalized m is stationary for continuous tests at each t, and finite-measure uniqueness extends to bounded Borel f.

Finite m and inaccessible endpoints force S(ℓ)=−∞,S(r)=∞. Finite S(r) would imply finite \(\Sigma_r\)≤(S(r)−S(c))m((c,r)), a contradiction; likewise on the left. Thus this is the recurrent setting above. For uniqueness let ν be any invariant probability. For f∈\(C_c^\infty\), Lf is bounded and the Itô remainder is bounded on finite T by 2||f||∞+T||Lf||∞, hence a true martingale. Integrating ν gives ∫Lf dν=0.

Treat μ=aν as a locally finite measure and put q=b/a. The weak equation is ∫f″dμ+∫qf′dμ=0. Solve it explicitly without presupposing a density or using an unestablished distribution-theory theorem. A smooth compactly supported θ with ∫θdx=0 is the derivative of a smooth compactly supported f, so T(θ)=∫θ′dμ+∫qθdμ=0. Fix a unit-integral θ₀ and decompose θ−(∫θ)θ₀ to get T(θ)=C∫θdx.

Put η=qμ−Cdx, a locally signed measure, and let F(x) be its oriented cumulative integral from a fixed interior point. F has locally bounded variation and Fubini gives ∫θ′Fdx=−∫θdη. The preceding equation also gives ∫θ′dμ=−∫θdη. Thus μ−Fdx annihilates every θ′. Test arbitrary zero-integral smooth ψ=θ′; measure uniqueness gives μ−Fdx=Kdx. Therefore μ has a local BV density v=F+K, with dv=η=(qv−C)dx, and is actually locally absolutely continuous.

Since p′=−qp, the ordinary absolutely continuous product rule gives (pv)′=−Cp. Integrate to obtain pv=A−CS. Writing J=−C yields

\[ \nu(dx)=\{C+JS(x)\}\,m(dx). \]

Rename A as C in the displayed density. Since S ranges over R, nonnegativity and the continuous density factor force J=0; unit mass makes C=1/m(I). With infinite endpoint scales but m(I)=∞, no invariant probability exists. This local equation does not classify stationary laws for arbitrary reflecting or sourced boundaries, which may inject flux or atoms and need separate conditions.

## 4. Return Cycles, Time Averages and Infinite Means

<a id="diffusion-cycle-proof"></a>

Assume infinite scale at both ends. Choose a<b and D=S(b)−S(a). A cycle goes from a to b and back to a. Both hitting times are finite almost surely, so its length L is positive and finite almost surely. Strong Markov makes lengths and path rewards iid pairs. The one-sided Green kernel for a→b is D for y≤a, S(b)−S(y) for a<y<b and zero above b. For b→a it is zero below a, S(y)−S(a) between and D above b. Their sum is D, yielding

\[ ER_f=D\int_If\,dm\quad(f\ge0),\qquad EL=Dm(I). \]

For finite m and bounded Borel f, |\(R_f\)|≤||f||∞L is integrable. Put \(T_n\)=∑₁ⁿLᵢ and N(t)=max{n:\(T_n\)≤t}. The iid SLLN gives \(T_n\)/n→μ=EL>0 and (∑Rᵢ)/n→ER, hence N(t)/t→1/μ. Tail integration gives ∑P(L>εn)≤EL/ε, so Borel–Cantelli yields \(L_n\)/n→0. The incomplete-cycle error is at most ||f||∞\(L_{N(t)+1}\)/t→0. The time average is ER/EL=∫f dm/m(I).

If EL=∞, apply SLLN to L∧K to get liminf \(T_n\)/n≥E(L∧K); let K increase to obtain \(T_n\)/n→∞ and N(t)/t→0. For bounded nonnegative compactly supported f, ER=D∫f dm is finite. Thus ∑Rᵢ/n→ER and \(R_n\)/n→0. Incomplete reward is bounded by the entire next-cycle reward \(R_{N+1}\); divided by t it vanishes using \(R_n\)/n→0 and (N+1)/t→0. The time average is zero, without requiring an unjustified negligible remainder for the nonintegrable cycle length itself.

From any interior initial value, first wait until a, a finite almost-sure delay needing no finite mean. Its bounded-f contribution divided by t vanishes. The conclusions hold from every interior state for each fixed f on its corresponding full-probability set, without intersecting over all Borel f. Time averages are not substituted for distributional or total-variation mixing from arbitrary initial states, a separate responsibility of Chapter 42.

## 5. Computable OU and Brownian Conclusions

<a id="diffusion-stationary-examples"></a>

OU has \(p=e^{\theta x^2/\sigma^2}\),\(m^\prime=(2/\sigma^2)e^{-\theta x^2/\sigma^2}\), infinite scales and finite total speed. Normalization gives N(0,σ²/(2θ)). Chapter 32’s explicit solution from fixed x has mean e⁻θᵗx and variance σ²(1−e⁻²θᵗ)/(2θ), yielding convergence in law. Our cycle computation additionally gives almost-sure time averages for bounded Borel f; these are distinct conclusions.

Brownian speed 2dx has infinite mass. It is recurrent without invariant probability, and time fraction in each fixed bounded region tends to zero by the preceding proof, not merely by naming null recurrence. Geometric Brownian motion on (0,∞) has S=x, left scale zero and right scale infinity and is conservative, so it tends to zero. This agrees with Chapter 32’s exponential solution without repeating its integration. Return to [Chapter 36’s resulting insight](../chapters/36-scale-speed.md#diffusion-insight).
