# T-FEYNMAN-KAC: Conditioning, Classical Solutions, Boundaries and Measure Sources

Companion to [Chapter 38](../chapters/38-feynman-kac.md#fk-discovery). Use usual filtrations, a cemetery after exit and zero test functions there. Stochastic integrals use Chapters 31–35; local time has Chapter 37’s symmetric Brownian normalization. Each theorem specifies its own process class.

## 1. Restarting the Account after a Short Time

<a id="fk-proof-dynamic"></a>

Let X be strong Markov, τ the exit from an open D, q≥0 bounded Borel and f bounded, with bounded terminal or boundary rewards. Put Qₜ=∫₀ᵗq(Xₛ)ds. Begin with a finite horizon T and bounded terminal h. Markov conditioning and ordinary Fubini give the following account identity, also at stopping times S≤T. The integral is bounded by T‖f‖∞, justifying conditional Fubini.

\[ u(t,x)=E_x\left[e^{-Q_t}h(X_t)+\int_0^te^{-Q_s}f(X_s)ds\right],\quad u(t,x)=E_x\left[\int_0^Se^{-Q_s}f(X_s)ds+e^{-Q_S}u(t-S,X_S)\right]. \]

A small deterministic S does not prove differentiability. Suppose X solves a nonexplosive Chapter 35 SDE with time-homogeneous locally Lipschitz coefficients. If bounded v∈\(C^{1,2}\) satisfies v(0)=h and ∂ₜv=Lv−qv+f, apply the Chapter 32 product and Itô formulas to \(e^{-Q_s}\)v(t−s,Xₛ). Stop on exiting large balls and when stochastic-integral energy reaches n. Only −\(e^{-Q_s}\)f remains in the drift. Take expectations and let n increase; boundedness gives DCT for the boundary terms and v=u. This verifies and uniquely identifies a classical solution; it does not assume the expectation is already \(C^{1,2}\). This statement is for time-homogeneous motion and potential. General time-dependent coefficients require a backward equation with both starting and terminal times; the current forward-time notation does not establish that extension.

## 2. Actually Constructing Classical Parabolic Solutions

<a id="fk-proof-parabolic"></a>

Now use standard Brownian motion on Rᵈ and its Gaussian convolution Pₜ. Assume h,q,f and their derivatives through order two are bounded uniformly continuous, with q≥0 and time-independent f. Call this Banach space C²_bu, normed by the sum of derivative suprema. Completeness follows from uniform derivative limits and integration along line segments. Gaussian convolution is a contraction there and Pₜv→v in its norm, by uniform continuity and Gaussian tail bounds.

\[ u(t)=P_th+\int_0^tP_{t-s}(f-qu(s))ds. \]

Iterate the right side in C([0,T];C²_bu). Multiplication by q is bounded on this space. The n-th successive difference is at most C(C_qT)ⁿ/n!, giving existence and uniqueness on every finite T. The Banach-norm convergence passes second derivatives through the integral. Gaussian integration by parts, or Itô verification, gives Pₜv−v=½∫₀ᵗPₛΔv ds for C²_bu. Difference quotients in the mild equation and strong continuity now yield ∂ₜu=½Δu−qu+f, continuously in C_bu. Thus a genuine \(C^{1,2}\) solution has been constructed before identifying it with the path expectation.

For merely bounded Borel h, smoothing at t>0 does not guarantee classical continuity at zero. If h=1_{x>0}, then u(t,0)=1/2 while h(0)=0. Feynman–Kac has not failed: initial data require an appropriate weak or almost-everywhere interpretation. A general degenerate SDE cannot inherit Gaussian smoothing without proof.

## 3. Harmonicity inside an Arbitrary Bounded Domain

<a id="fk-proof-dirichlet"></a>

Let D⊂Rᵈ be bounded open, τ=τ_D and g bounded Borel on its boundary. Continuity puts the exit point in ∂D. Enclose D in a radius-R ball; stopping |B|²−dt gives Eₓτ≤4R²/d, hence finite exit. For h(x)=Eₓg(Bτ), strong Markov on every ball V compactly contained in D gives h(x)=Eₓh(BτV). Rotational invariance makes the exit direction from the center uniform, yielding the spherical mean property.

This proves regularity instead of assuming it. Integrate spherical means against a smooth radial probability kernel η supported in a small ball: h=h*η. The right side is smooth, so h is C∞ inside D. A second-order expansion of the mean identity gives Δh=0. Conversely, bounded C² harmonic functions satisfy the same stopped Itô martingale identity. If continuous boundary values equal g, exhaust D by compact subdomains and use τₙ↑τ and bounded DCT to identify the function with h.

Boundaries need an additional condition. Suppose z∈∂D admits a local positive continuous superharmonic barrier b tending to zero at z and bounded below by c>0 on the artificial boundary away from z. Stopping the supermartingale bounds the chance of escaping the neighborhood before exiting D by b(x)/c. Split continuous g into its small near-z oscillation and a far contribution bounded by 2‖g‖∞: h(x)→g(z). Exterior tangent balls give barriers: ρ^{2−d}−|x−c|^{2−d} for \(d\ge3\), log(|x−c|/ρ) in d=2 and linear distance in one dimension, after shrinking the neighborhood so the artificial boundary has a positive lower bound.

A sphere tangent at other nearby boundary points may not isolate z; the strict exterior-ball condition suffices here, without silently claiming all exterior-cone domains. A counterexample is the punctured ball D={0<|x|<1}, \(d\ge2\). Set g(0)=1 and g=0 on the outer sphere; this is continuous on the boundary. Radial harmonic functions give the probability of hitting radius ε before 1 from r: log(1/r)/log(1/ε) in d=2, and (\(r^{2-d}\)−1)/(\(\varepsilon^{2-d}\)−1) in higher dimensions. Both tend to zero. The point is polar, so h≡0 cannot attain g(0)=1. A valid interior representation does not guarantee arbitrary boundary data.

## 4. Why the Source Representation Is Differentiable inside the Domain

<a id="fk-proof-elliptic"></a>

In D take bounded locally α-Hölder f,q, 0<α<1, q≥0 and bounded Borel g. Define u=E[e^{-Qτ}g(Bτ)+∫₀τ\(e^{-Q_s}\)f(Bₛ)ds]. The exit mean bound makes u bounded. Conditioning on exit from a ball V gives the same account identity. Expand the exponential and use conditional Fubini to remove the discount: u=H_Vu+G_V(f−qu). Integrability follows from C Eτ_V and Eτ_V²<∞; the latter follows from the uniformly bounded ball exit mean and the Markov geometric-tail argument.

The needed Green regularity is elementary. The fundamental solution of −½Δ is Φ=2|x|^{2−d}/((d−2)|S^{d−1}|) for \(d\ge3\), −log|x|/π in d=2, and −|x| in d=1; radial derivatives and small-sphere flux verify the constants. For bounded compactly supported w, the gradient kernel is locally integrable, so Φ*w is locally continuous and Lipschitz. A ball Green potential differs by a smooth harmonic correction. Prove this first for smooth compactly supported w: apply stopped Itô to v=Φ*w to obtain v(x)−Eₓv(BτV)=Eₓ∫₀τVw(Bₛ)ds. The two integration functionals in w define locally finite measures; density of smooth tests and measure uniqueness extend the kernel identity to bounded Borel w, using MCT for nonnegative functions and the exit-mean bound for signed ones. Identification of the Green kernel has not assumed differentiability of a general u. The account identity first makes u locally continuous and Lipschitz; hence w=f−qu is locally α-Hölder. In second derivatives, subtract w(x) from w(x−y) to cancel the singularity; ∫₀ʳs^{α−1}ds controls it. Integration by parts on punctured balls and the flux give −½Δ(Φ*w)=w. Thus u∈C²(D) and ½Δu−qu=−f. These are two separate regularity steps, not an assumption that expectations are C².

For a ball, take the exit average of the fundamental-solution potential on its boundary as the harmonic correction. Its interior smoothness was already proved in Section 3 by spherical means and radial convolution; no additional unproved Poisson-kernel theorem is needed. In one dimension interpolate the endpoints linearly. At a strict exterior-ball regular point, the source contribution vanishes because Eₓτ_D→0: the barrier bounds the chance of leaving a small neighborhood, a uniform second exit-time moment controls that contribution by Cauchy–Schwarz, and the remaining local exit time has the small-ball bound. Thus continuous g is attained.

Unbounded domains require a separate terminal/UI check. On (0,∞), h(x)=x is classically harmonic with boundary zero. Brownian hitting of zero is finite, yet Eₓh(Bτ)=0≠x. Stopping also at n leaves a rare far-end event carrying value n; the stopped family is not UI. A finite-stop Itô identity cannot simply pass to an unbounded exit time.

## 5. The Weak Equation for a Singular Charge

<a id="fk-proof-singular"></a>

Take I=(a,b), a finite positive Radon μ, \(f\in L^2(I)\) and finite endpoint values gₐ,g_b. Let H be absolutely continuous functions vanishing at the endpoints with L² derivative. The bound ‖v‖∞≤√(b−a)‖v′‖₂ gives Poincaré and continuous point evaluation. Completeness follows by integrating the L² derivative limit; the endpoint constraint is preserved. The inner product B(v,w)=½∫v′w′dx+∫vw dμ has norm equivalent to that of H. For linear endpoint interpolation h, ℓ(w)=∫fw dx−B(h,w) is continuous. Hilbert projection gives its Riesz representative: use a unit vector orthogonal to its kernel. Hence a unique v∈H satisfies B(v,w)=ℓ(w), and u=h+v.

\[ \frac12\int_Iu^\prime\varphi^\prime dx+\int_Iu\varphi\,d\mu=\int_If\varphi\,dx,\quad\varphi\in H,\qquad \frac12u^{\prime\prime}=u\mu-f\,dx\quad\hbox{as distributions}. \]

The continuous bounded u has a finite signed distributional second derivative, so u′ has a BV version and u is a difference of convex functions: integrate (x−y)⁺ against the positive and negative second-derivative measures, leaving an affine remainder. This does not assume C². Integrate Chapter 37’s Tanaka formula against that measure; local-time moment bounds and finite total variation justify stochastic Fubini. The generalized formula is u(Bₜ)=u(x)+∫u′₋(Bₛ)dBₛ+½∫Lₜʸu″(dy). Stop on exit from I. The derivative is bounded there and Eτ<∞ controls the stochastic-integral energy.

The clock Aₜ=∫L_{t∧τ}ʸμ(dy) is finite continuous, and dLʸ is supported where B=y. In e^{-A}u(B), the uμ term therefore cancels exactly. Take expectations and increase the stopping times to τ. The source is dominated by E∫|f(B)|ds=∫G_I|f|dx<∞ and the boundary term is bounded. This gives the representation below. Weak-solution uniqueness identifies the two constructions, without first assuming the expectation belongs to H.

\[ u(x)=E_x\left[e^{-A_\tau}g(B_\tau)+\int_0^\tau e^{-A_s}f(B_s)ds\right],\quad \mu=\gamma\delta_c\ \Longrightarrow\ u^\prime(c+)-u^\prime(c-)=2\gamma u(c). \]

A point charge produces a derivative jump, not a choice of an ordinary value q(c). Writing q=0 almost everywhere would erase the entire atom. It also differs from Chapter 37’s speed atom: that atom changes the motion’s clock, while μ here changes weights on the original Brownian clock. The same local time serves different mathematical roles.

## 6. Operator Identities for Additive Costs

<a id="fk-proof-resolvent"></a>

For a continuous PCAF A, define Pₜᴬf=Eₓ[\(e^{-A_t}\)f(Xₜ);t<ζ]. Additivity and Markov give the semigroup; Tonelli gives its Laplace resolvent for f≥0. If A=∫q(X)ds with bounded q≥0, use 1−\(e^{-A_t}\)=∫₀ᵗq(Xₛ)e^{-(Aₜ−Aₛ)}ds and condition to obtain Duhamel. Taking Laplace transforms yields Rλᴬ=Rλ−Rλ(qRλᴬ). Multiplication and operator order cannot be interchanged. A continuous A uses the corresponding Stieltjes integral. For bounded f and λ>0, nonnegative splitting or ‖f‖∞/λ provides integrability.

This page does not prove Schauder theory for arbitrary measurable-coefficient elliptic operators, nor identify all distributional solutions with classical ones. Return to [singular sources and boundaries](../chapters/38-feynman-kac.md#fk-singular).
