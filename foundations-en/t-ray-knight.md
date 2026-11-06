# T-RAY-KNIGHT: Identifying the Spatial Process by Laplace Readings

Companion to [Chapter 37](../chapters/37-local-time.md#local-spatial-profile). We prove two classical Ray–Knight theorems for standard real Brownian motion: first hitting a>0 and inverse zero-local-time τℓ. Local time uses the symmetric Tanaka normalization; BESQδ means dZ=δdx+2√Z dβ. General-diffusion or graph-valued Ray–Knight extensions do not follow automatically.

## 1. First Construct the Squared Bessel Processes

<a id="ray-proof-besq"></a>

Only δ=0,2 and a deterministic change from 2 to 0 are needed. Extend σ(z)=2√(z⁺) to the real line, with b=δ. Continuity and linear growth allow Chapter 35’s Euler tightness and Brownian reconstruction to give a weak solution. The bound |σ(x)−σ(y)|≤2√|x−y| satisfies its modulus uniqueness criterion, and its proved Yamada–Watanabe construction gives a strong solution. BESQ existence is not inferred backward from Ray–Knight.

Nonnegativity needs checking. The right-local-time band formula at zero bounds Lₜ^{0,+} by 4∫₀ᵗ\(\mathbf1_{\{0<Z_s<\varepsilon\}}\)ds→0; the left band has zero bracket. Negative-part Tanaka gives Z⁻≤−δ∫\(\mathbf1_{\{Z<0\}}\)ds≤0. Stopping at the first K-hit gives E Zₜ∧τK=z+δE(t∧τK), so explosion before T has probability at most (z+δT)/K, tending to zero. Fatou first gives EZₜ≤z+δt, hence E∫₀ᵀ4Zₛds<∞. The stochastic integral is a true martingale, yielding EZₜ=z+δt. For δ=0, path uniqueness makes zero absorbing. For δ=2, two squared independent Brownian coordinates provide another construction.

\[ dZ_x=\delta(x)dx+2\sqrt{Z_x}\,d\beta_x,\quad Z_0=z\ge0,\qquad \delta(x)=0\ \text{or}\ \delta(x)=2\mathbf1_{[0,a]}(x). \]

## 2. Why a Riccati Equation Appears

<a id="ray-proof-laplace"></a>

Take continuous φ≥0 supported in [0,R], initially with R beyond its support. Solve v″=2φv backward from v(R)=1,v′(R)=0. A backward Volterra iteration has nonnegative terms, giving v>0 and v′≤0. Divide by v(0), extend constantly after R, and put u=−v′/(2v). Then u is bounded nonnegative and solves the equation below. It converts a second-order linear equation into precisely the nonlinear reading canceled by square-root noise.

\[ u^\prime=2u^2-\varphi,\qquad u(R)=0,\qquad v(x)=\exp\!\left(-2\int_0^xu(y)dy\right). \]

For BESQ take F(x,z)=exp[−zu(x)−∫ₓᴿδ(y)u(y)dy]. Apply Itô on either side of a δ-change and join continuously. In \(\exp(-\int_0^x\varphi(s)Z_s\,ds)\)F(x,Zx), the dx-coefficient is z(−u′+2u²−φ), while δu cancels −δu. The result lies in [0,1], so localization and DCT make it a true martingale without global higher moments. At R, F=1, giving the transform below.

\[ E_z\exp\!\left(-\int_0^R\varphi(x)Z_xdx\right)=\exp\!\left[-zu(0)-\int_0^R\delta(x)u(x)dx\right]. \]

These readings determine the law of a nonnegative continuous spatial process. Continuous narrow hats approximate finitely many Dirac masses, so path continuity turns ∫φZ into nonnegative linear combinations of coordinates. Bounded exponentials allow DCT. Apply Chapter 13’s Laplace uniqueness coordinate by coordinate to identify finite-dimensional laws; rational evaluations generate the Borel structure of continuous paths.

## 3. First Ray–Knight at a Hitting Time

<a id="ray-proof-first"></a>

Let Tₐ be the first a-hit, a>0, for B₀=0, and define Zx=\(L_{T_a}^{a-x}\), x≥0. Joint continuity makes this a nonnegative continuous spatial process, with Z₀=0 since a had not been visited before. For R>a and φ as above, occupation writes its Laplace reading as weighted Brownian time before Tₐ.

\[ E_0e^{-\int_0^R\varphi(x)L_{T_a}^{a-x}dx}=E_0\exp\!\left[-\int_0^{T_a}\varphi(a-B_s)ds\right]=v(a). \]

The last equality does not borrow general Feynman–Kac from Chapter 38. For y≤a set h(y)=v(a−y); then 0<h≤1, h(a)=1 and ½h″=φ(a−y)h. Multiply by the exponential and use Itô, stopping at Tₐ, the first −n-hit and deterministic T. Drift vanishes and the process is bounded. The a-hit is finite; errors are bounded by P₀(τ_{−n}<Tₐ)=a/(a+n) and P(Tₐ>T). Let n,T increase and use DCT to obtain h(0)=v(a).

Since v(a)=exp[−2∫₀ᵃu], this is exactly the BESQ reading with z=0 and δ=2 up to a, then zero. Hence Z is BESQ2 from zero on [0,a]; beyond a it continues, conditionally on Za, as BESQ0 driven by an independent Brownian motion. This spatial conditional-Markov structure follows from equality of process laws, not from an expected profile.

\[ E L_{T_a}^{a-x}=2\min(x,a),\qquad x\ge0. \]

The mean follows by stopped BESQ expectation or directly from Chapter 36’s one-sided Green kernel, independently checking the factor two. The finite almost-sure Brownian hitting time Tₐ has infinite mean; these statements do not conflict.

## 4. Second Ray–Knight at Inverse Local Time

<a id="ray-proof-second"></a>

Fix ℓ>0. Positive and negative excursions before τℓ are independent PRMs, with positive intensity dl n(de)/2. Put \(A_\varphi(e)=\int_0^{\zeta(e)}\varphi(e_s)\,ds\). The zero set has zero ordinary time, so ∫φ(x)\(L_{\tau_\ell}^x\) dx is the sum of positive-excursion rewards. The Poisson functional gives

\[ Ee^{-\int_0^\infty\varphi(x)L_{\tau_\ell}^xdx}=\exp\left[-\frac\ell2n(1-e^{-A_\varphi})\right]. \]

Stopped Itô again gives v(ε)=Eε exp[−\(\int_0^{\tau_0}\)φ(B_s)ds]. Restrict n to ε-reaching excursions and apply strong Markov after their first ε-hit. Initial-segment reward error is at most ||φ||∞n[ρ;H≥ε]≤||φ||∞ε. For discarded low-height excursions, the entrance law gives nAφ=∫φ(y)∫₀∞kₜ(y)dt dy=2∫φ(y)dy<∞; DCT removes their rewards as ε↓0. Consequently

\[ n(1-e^{-A_\varphi})=\lim_{\varepsilon\downarrow0}\frac{1-v(\varepsilon)}\varepsilon=-v^\prime(0)=2u(0). \]

The time integral of k is two, not one, matching our n indexed by symmetric Brownian L. The Poisson exponent becomes exp[−ℓu(0)], exactly BESQ0 from z=ℓ. Thus (\(L_{\tau_\ell}^x\),x≥0) is BESQ0 from ℓ; (\(L_{\tau_\ell}^{-x}\),x≥0) is an independent copy. Their shared zero-level value is the deterministic initial value ℓ.

## 5. Critical Branching Structure and Scope

<a id="ray-proof-boundary"></a>

For BESQ0 use the terminal Laplace reading and u(x)=q/(1+2q(t−x)) in the same bounded exponential calculation. This yields the transition transform below. Multiplication shows that the process from z₁+z₂ has the law of the sum of independent processes from z₁,z₂; equal transition kernels and the Markov construction give the process statement. Let q→∞ for its zero probability; absorption then implies extinction at a finite spatial distance almost surely.

\[ E_ze^{-qZ_t}=\exp\!\left(-\frac{zq}{1+2qt}\right),\qquad P_z(Z_t=0)=e^{-z/(2t)},\qquad EZ_t=z\quad(t>0,q\ge0,z\ge0). \]

Brownian local-time profiles thus possess a continuous-state critical branching structure, beyond a visual analogy with family trees. Each profile eventually vanishes while retaining its mean at each finite spatial position, so this spatial martingale is not uniformly integrable. The new content is an actual branching transition law, not a repetition of Chapter 20’s spine argument. These stopped versions are not extended to arbitrary deterministic-time profiles or all Lévy height processes. Return to [Chapter 37](../chapters/37-local-time.md#local-ray-knight).
