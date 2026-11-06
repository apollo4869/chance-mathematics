# T-SDE-SMALL-NOISE: Path Large Deviations for Feedback Equations

A companion to [Chapter 35](../chapters/35-sde-wellposedness.md#sde-small-noise). We prove Freidlin–Wentzell for finite T, fixed initial x and globally bounded Lipschitz b:Rᵈ→Rᵈ, σ:Rᵈ→Rᵈˣᵐ, allowing degeneracy. Noise is εW and speed ε⁻²; with √εW the speed becomes ε⁻¹. Inputs are Chapter 29’s Schilder and contraction principle, Chapter 32’s Itô formula, Chapter 33’s nonnegative exponential supermartingale, and this chapter’s strong construction and stability estimates.

## 1. The Continuous Euler Map

<a id="sde-proof-euler-map"></a>

For mesh h let η_h(s) be the left endpoint of the containing interval, retaining a shorter final interval. For continuous w starting at zero define F_h(w) recursively: from grid state y use y+b(y)(t−tᵢ)+σ(y)(wₜ−wₜᵢ) within the interval. Finitely many recursions and coefficient continuity make F_h continuous between uniform-path spaces. X^{ε,h}=F_h(εW) is the frozen Euler process. Chapter 29 gives its good LDP with cost

\[ I_h(\phi)=\inf\left\{\tfrac12\|u\|_{L^2}^2:F_h\left(\int_0^\cdot u_sds\right)=\phi\right\}. \]

Continuity of F_h is asserted for fixed h. We have not proved a uniformly continuous Itô map as the mesh vanishes. Exponential approximation below bridges that gap.

## 2. Compactness of Control Energy and the Controlled Equation

<a id="sde-proof-control"></a>

For u∈L²([0,T],Rᵐ), interpret φ=x+∫b(φ)ds+∫σ(φ)u ds as an ordinary integral equation. Its Lipschitz constant is integrable relative to (1+|u|)ds. Contract on intervals with this measure less than 1/(2L), then concatenate finitely many intervals to obtain a unique absolutely continuous solution. Bounded coefficients give the needed oscillation bound

\[ |\phi_t-\phi_s|\le B|t-s|+B\sqrt{|t-s|}\,\|u\|_2,\qquad \|\phi\|_T\le|x|+BT+B\sqrt T\|u\|_2. \]

On ||u||²₂≤2R the paths are uniformly bounded and equicontinuous. Frozen controlled solutions ψ_h=F_h(∫u) satisfy the same bounds, with within-cell oscillation ≤B(h+√(2Rh)). Compare to φ and apply Gronwall relative to (1+|u|)ds to obtain

\[ \sup_{\|u\|_2^2\le2R}\|\psi_h-\phi(u)\|_T\le C_{R,T}\sqrt h\longrightarrow0. \]

Weak-control convergence also needs proof. If uₙ⇀u in L², every uniformly convergent subsequence of φ(uₙ) has a limit φ. Uniform convergence of σ(φₙ) and Cauchy–Schwarz give ∫(σ(φₙ)−σ(φ))uₙ→0. Weak convergence passes the remaining ∫₀ᵗσ(φ)uₙ at each t. Equicontinuity upgrades rational-time convergence to uniform convergence. DCT passes the drift. Uniqueness identifies the limit with φ(u) and gives full-sequence convergence.

A closed L² energy ball is weakly sequentially compact: diagonal extraction on a countable orthonormal basis and Bessel’s inequality give a limit with no increase in norm. Its image under the controlled solution map is compact by the preceding argument. A minimizing control sequence for a finite-cost φ has a weak subsequence; weak lower semicontinuity attains the infimum. Thus the level sets of I(φ)=inf{||u||²₂/2:φ(u)=φ} are exactly these compact images, so I is a good rate function.

## 3. An Exponential Bound Does Not Require a Probability Density

<a id="sde-proof-exp-bound"></a>

If a continuous local martingale starts at zero and [M]ₜ≤v, stop exp(θM−θ²[M]/2) at the first M≥a and at T. Nonnegativity and localized Fatou make it a supermartingale, yielding probability ≤exp(−θa+θ²v/2). Optimize at θ=a/v for exp(−a²/(2v)); if v=0 then M=0. No strict local-martingale exponential is being used as a probability density. Coordinatewise bounds and a union bound for m-dimensional Brownian motion give

\[ P\!\left(\sup_{s\le h}|W_s|>r\right)\le2m\exp\left(-\frac{r^2}{2mh}\right). \]

## 4. Superexponential Distance between True and Frozen Solutions

<a id="sde-proof-exponential-approximation"></a>

Let Y=X^{ε,h}, e=Xε−Y and V_s=Y_s−Y_η(s), with coefficient bound B and Lipschitz constant L. Fix target r>0 and small ρ>0. Put τ_e=inf{|e|≥r} and τ_V=inf{|V|≥ρ}; define τ_V via continuous first passages within grid cells, where V resets to zero at boundaries. A countable union over cells gives a stopping time. Before τ_V, drift error β and diffusion error Γ obey |β|+||Γ||≤L(|e|+ρ).

Apply Itô to F(e)=log(1+|e|²/ρ²), stopped at τ=τ_e∧τ_V∧T. Its gradient is 2e/(ρ²+|e|²) and Hessian 2I/(ρ²+|e|²)−4eeᵀ/(ρ²+|e|²)². Drift is bounded above by C(1+ε²), since (|e|+ρ)²/(|e|²+ρ²)≤2; discard the negative Hessian contribution. The martingale K has bracket ≤Cε²T. Hence for 0<ε≤1, F(eₜ∧τ)≤C_T+Kₜ∧τ and [K]ₜ∧τ≤C_Tε².

\[ P(\|e\|_T\ge r,\tau_V>T)\le\exp\left[-\frac{\bigl(\log(1+r^2/\rho^2)-C_T\bigr)_+^2}{2C_T\varepsilon^2}\right]. \]

The other error is excessive motion of the frozen path inside a cell. If Bh≤ρ/2, the explicit cell formula, ||σ||≤B and the Brownian bound above give

\[ P(\tau_V\le T)\le2m(1+T/h)\exp\left(-\frac{\rho^2}{8mB^2\varepsilon^2h}\right). \]

If B=0 the probability is zero and is treated separately. Set ρ=h¹ᐟ⁴. Then ρ²/h→∞ and log(1+r²/ρ²)→∞. For fixed mesh, first let ε→0 so the ε² logarithm of the finite-grid prefactor vanishes. Then let h→0; both errors become superexponential. This proves

\[ \lim_{h\downarrow0}\limsup_{\varepsilon\downarrow0}\varepsilon^2\log P(\|X^\varepsilon-X^{\varepsilon,h}\|_T>r)=-\infty\qquad(r>0). \]

The error is continuous, so r is attained exactly at stopping; there is no jump overshoot. Itô and exponential arguments may first be boundedly localized and then released, with bracket bounds independent of localization. The proof assumes neither uniform-path continuity of the Itô map nor that an L²-small error is exponentially negligible.

## 5. Transferring the Open and Closed Bounds

<a id="sde-proof-fw"></a>

For the lower bound choose a finite-cost φ(u) in open G and r>0 with its 2r ball inside G. Section 2 puts ψ_h(u) within r/2 for fixed sufficiently small h. The Euler LDP gives lower exponent at least −||u||²₂/2 for its r/2 ball. If the true solution is outside G while Euler is in that ball, their error exceeds r. Choose h so the error exponent is strictly larger than ||u||²₂/2. If a_ε has lower exponent ≥−c and b_ε upper exponent ≤−M with M>c, then (a_ε−b_ε)₊ has the same lower exponent, since b_ε/a_ε→0. Optimize over u to obtain the open lower bound.

For the upper bound use the closed r-neighborhood Fʳ={ψ:dist(ψ,F)≤r} of closed F. Then P(Xε∈F)≤P(Y∈Fʳ)+P(||e||>r). The Euler closed bound and exponential approximation control the maximum of the two exponents. We must rule out an artificial drop of cost as h,r vanish. Suppose hₙ,rₙ→0 admit controls uₙ of energy ≤A with ψ_hₙ(uₙ) at distance ≤rₙ from F. Extract a weak L² subsequence. Section 2 gives φ(uₙ)→φ(u) uniformly and ||ψ_hₙ(uₙ)−φ(uₙ)||→0. Closedness yields φ(u)∈F and weak lower semicontinuity bounds its cost. Therefore

\[ \lim_{r\downarrow0}\liminf_{h\downarrow0}\inf_{\psi\in F^r}I_h(\psi)\ge\inf_{\phi\in F}I(\phi). \]

If the right side is infinite, apply the same contradiction for arbitrary finite A. For fixed r let h vanish to make the approximation exponent tend to −∞, then let r vanish. This gives the upper bound for every closed set, not merely compact sets. Together with section 2’s compact level sets it completes the good LDP.

## 6. Exact Scope, Degeneracy and the Meaning of Cost

<a id="sde-proof-fw-scope"></a>

If a(x)=σ(x)σ(x)ᵀ is invertible, the pointwise minimum-norm control for absolutely continuous φ from x is σᵀa⁻¹(φ′−b). The rate is half the integral of (φ′−b)ᵀa⁻¹(φ′−b), provided that control belongs to L². With degenerate a, φ′−b must lie in the range of σ and admit an L² control; other paths have infinite cost. A finite pseudoinverse expression alone does not enforce the range condition.

For σ=0 the only finite-cost path is the deterministic ODE solution, with cost zero. For b=0,σ=I we recover Schilder’s quadratic energy. The common structure is control energy transmitted through an actually constructed dynamic rule, not identical accessibility for every stochastic model. We prove only the bounded-Lipschitz finite-time version. Unbounded coefficients, explosion, infinite-time exit asymptotics, non-Lipschitz selection and jump small-noise LDPs are not counted as proved here.

Return to the [chapter’s control energy and resulting insight](../chapters/35-sde-wellposedness.md#sde-fw). This is a working proof, not a substitute for independent mathematical final review; upstream T-SCHILDER and other final-review statuses remain open.
