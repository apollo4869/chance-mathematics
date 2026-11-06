# Chapter 37: How Much Has a Path Accumulated at One Position? — Local Time, Occupation and Excursions

Sort a Brownian record by position. Every crossing of zero really occurred, yet the total length of times with Bₜ=0 is zero. Neither the record nor the repeated returns are fictitious. The loss lies in the measure used to count them.

## 37.1 What a Zero Answer Has Lost

<a id="local-question"></a>

Chapter 36 distinguished hitting from ordinary occupation. For standard Brownian motion from zero, each Bₜ at t>0 has a density, so Tonelli makes ordinary time at one point zero. Continuity and recurrence nevertheless give repeated crossings. Rather than reprove recurrence, ask whether that zero answer can be refined to retain contact information.

\[ \int_0^t\mathbf1_{\{B_s=0\}}ds=0\quad\text{a.s.},\qquad \Lambda_t^\varepsilon=\frac1{2\varepsilon}\int_0^t\mathbf1_{\{|B_s|<\varepsilon\}}ds. \]

A sensor can record time inside a band of width 2ε, then divide by width. This ratio is not the time-length of a singleton; it is a candidate spatial density. The Gaussian kernel makes EΛᵋ tend to √(2t/π), rather than zero. A converging expectation, however, does not construct a density for individual paths.

## 37.2 The Corner of an Absolute Value Detects Contact

<a id="local-smoothing"></a>

Chapter 32 Itô handles smooth observations. To isolate contact with a, |x−a| is more useful: its slope is constant away from a and curvature is concentrated at a. It is not C², so setting its ordinary second derivative to zero would illegitimately discard the correction. Smooth the corner first.

\[ F_\varepsilon(B_t-a)-F_\varepsilon(B_0-a)=\int_0^tF_\varepsilon^\prime(B_s-a)dB_s+\frac12\int_0^tF_\varepsilon^{\prime\prime}(B_s-a)ds,\qquad F_\varepsilon=|\cdot|*\rho_\varepsilon. \]

Fᵋ converges uniformly to absolute value; its bounded derivatives tend to sgn. Isometry and Doob give maximal L² convergence of stochastic integrals. The curvature terms consequently have a nonnegative increasing ucp limit. The existing change-of-variable formula forces us to retain this accumulation, rather than inventing a symbol and searching afterward for its meaning.

\[ |B_t-a|=|B_0-a|+\int_0^t\operatorname{sgn}(B_s-a)dB_s+L_t^a,\qquad \operatorname{sgn}(0)=0. \]

This is Tanaka’s formula in our normalization. L is local time. No additional ½ appears because the smoothed absolute value has total curvature two. Excursion rates, speed clocks and Bessel dimensions must respect this choice. The [complete construction](../foundations/t-local-time.md#local-proof-tanaka) includes parameter measurability and localization.

## 37.3 A Density Must Work across Positions

<a id="local-occupation"></a>

So far a process was built at each fixed a. Reconstructing spatial occupation needs more than pointwise existence. Multiply the smooth curvature term by continuous compactly supported f(a), integrate in a, and use Fubini. This becomes a convolution test along the path; then let ε decrease to zero.

\[ \int_0^tf(B_s)ds=\int_{\mathbb R}f(a)L_t^a da\qquad(f\ge0\text{ Borel}). \]

Continuous tests identify finite measures, then a monotone class extends to Borel functions. Outside one exceptional set the identity holds for all t and Borel sets. L is a spatial density of the path’s occupation measure, not unrelated random variables. A density may be nonzero at a point while that singleton still has zero measure.

Do not reverse the reasoning: zero time at every point does not imply existence of a density, since atomless measures can be singular. Density existence was proved through smoothed curvature, stochastic-integral limits and identification of measures.

## 37.4 Why the Local-Time Surface Is Continuous

<a id="local-joint"></a>

An occupation density permits changes on spatial null sets. If readings could jump arbitrarily at selected levels, accumulation at a would remain version-dependent. Brownian paths supply more structure. Subtract Tanaka integrals at a,b: only integrals while the path is between those levels remain.

\[ E\left\|\int_0^\cdot\bigl(\operatorname{sgn}(B_s-b)-\operatorname{sgn}(B_s-a)\bigr)dB_s\right\|_{C[0,T]}^{2p}\le C_{p,T}|b-a|^p,\qquad p\ge2. \]

Apply the continuous-martingale moment bound, rewrite bracket occupation as ∫ₐᵇLᵞdy, and use integral Hölder with uniform local-time moments. Dyadic chaining gives spatial continuity valued in continuous time functions. Thus L is jointly continuous and locally spatially Hölder of every order below 1/2. [Proof 3](../foundations/t-local-time.md#local-proof-regularity) supplies the steps; choosing a continuous version is not a proof.

\[ \sup_{t\le T,\ |a|\le K}\left|\frac1{2\varepsilon}\int_0^t\mathbf1_{\{|B_s-a|<\varepsilon\}}ds-L_t^a\right|\longrightarrow0\quad\text{a.s.} \]

The band limit now follows from occupation and uniform continuity on compact sets. The surface no longer needs a separately chosen exceptional set at every position.

## 37.5 What Changes for a General Continuous Semimartingale

<a id="local-semimartingale"></a>

For X=X₀+M+V, occupation uses d[M], not necessarily ds. The corner-derivative convention matters. Taking sgn₋(0)=−1 defines right local time and preserves Tanaka. It is continuous in t and spatially càdlàg; its jumps are determined by variation.

\[ \int_0^tf(X_s)d[M]_s=\int f(a)L_t^{a,+}da,\qquad L_t^{a,+}-L_t^{a-,+}=2\int_0^t\mathbf1_{\{X_s=a\}}dV_s. \]

This is substantive. Reflected Brownian pushing is concentrated at zero, so right local time there differs from its negative-level limit. Brownian joint continuity does not extend to all continuous semimartingales. If V=0, or in Chapter 36’s nondegenerate SDEs where drift has no single-level accumulation, the spatial jumps vanish.

## 37.6 How a Contact Set Becomes a Clock

<a id="local-two-clocks"></a>

The measure dLᵃ increases only at B=a: on an interval separated from a, narrow smooth curvature vanishes. The zero set supports all of L⁰ despite zero ordinary time. Tanaka also computes its size, rather than merely calling it nontrivial.

\[ |B_t|=\beta_t+L_t^0,\quad \beta_t=\int_0^t\operatorname{sgn}(B_s)dB_s,\quad [\beta]_t=t,\qquad L_t^0=\sup_{s\le t}(-\beta_s)^+\ \overset d=\ \sup_{s\le t}B_s. \]

Lévy’s characterization makes β Brownian. The regulator identity is deterministic: pushing continuous w into the nonnegative half-line, with pushing allowed only at zero, uniquely requires its negative running minimum. Reflection gives ELₜ⁰=√(2t/π), and L is unbounded over time. Contacts have no duration, yet have computable accumulated intensity.

Chapter 31’s Cantor clock showed that integral energy depends on its time measure. Here a path and a position jointly generate a clock. Predictable H=\(\mathbf1_{\{B=0\}}\) has zero dB-integral by zero energy, yet its dL⁰-integral is L⁰. Predictability does not make these the same integral.

## 37.7 Inverting the Clock Turns Gaps into Jumps

<a id="local-inverse"></a>

\[ \tau_\ell=\inf\{t:L_t^0>\ell\},\qquad Ee^{-\lambda\tau_\ell}=e^{-\ell\sqrt{2\lambda}}. \]

The finite stopping time τℓ records ordinary time needed for contact accumulation to exceed ℓ. Brownian motion is zero there. Strong Markov and additivity give stationary independent future clock increments. Skorokhod’s representation identifies its fixed-ℓ law with a Brownian first −ℓ-hit. This is a 1/2-stable increasing process, not a linear continuous clock change.

L stays constant during a whole trip away from zero. Inverting the clock compresses that motion into a jump of τ. We should retain the path hidden in the jump, not only its duration.

## 37.8 Cutting Excursions Does Not Prove Independence

<a id="local-excursion-path"></a>

The closed zero set has countably many disjoint complementary intervals (g,d). Each gives an excursion from zero, avoiding zero inside and returning at its end, with lifetime ζ=d−g and label \(L_g\). Enumerating by the first rational in each interval makes the decomposition measurable. [Proof 1](../foundations/t-excursions.md#excursion-proof-space) supplies standard-Borel coding.

This does not prove independence. Last zero g is generally not a stopping time, so strong Markov cannot be invoked there. Infinitely many small excursions cannot form an ordinary finite-rate arrival sequence. A legitimate regenerative experiment is needed.

## 37.9 Keep Only Excursions Large Enough to See

<a id="local-excursion-clock"></a>

Fix ε, wait for |B| to hit ε, then return to zero, and repeat. These are stopping times. Retain only the complete ε-reaching excursion in each cycle. Let U be L accumulated before that hit. Apply Tanaka to h=A+C|x|. Making \(e^{-qL}\)h(B) driftless requires C=qA; the boundary h(±ε)=1 determines A.

\[ Ee^{-qU}=\frac1{1+q\varepsilon}. \]

Thus U is exponential with mean ε. On {U>l}, \(\tau_l\) is a zero-state stopping time and the next ε-reaching excursion is the same unseen mark. Strong Markov makes its shape law independent of elapsed l. Waiting local time and full shape are independent; cycles are iid. Chapter 21’s exponential-renewal calculation now applies.

## 37.10 Why the Itô Measure Is Not a Probability

<a id="local-ito-measure"></a>

For positive R=|B| excursions, let n be intensity per unit L. Excursions reaching ε have rate 1/ε and probability shape law Qε. Thresholds only discard small paths from the same decomposition, so their consistent intensities uniquely assemble n.

\[ n(H\ge a)=\frac1a,\quad N=\sum_\ell\delta_{(\ell,e_\ell)},\quad Ee^{-N(f)}=\exp\left[-\int_0^\infty\!\int_E(1-e^{-f(\ell,e)})n(de)d\ell\right]. \]

Total n-mass is infinite, though every {H≥a} has finite mass. It is intensity per unit contact accumulation, not a uniform probability on excursions. The finite-threshold limit proves the Poisson property of the actual pieces. Independent fair signs give positive and negative B-excursions, each of intensity n/2 and independent of the other side.

## 37.11 Calibrating Lifetimes against the Clock

<a id="local-excursion-lifetime"></a>

\[ \tau_\ell=\sum_{s\le\ell}\zeta(e_s),\qquad n(1-e^{-\lambda\zeta})=\sqrt{2\lambda},\qquad n(\zeta\in dt)=\frac{dt}{\sqrt{2\pi}t^{3/2}}. \]

Zero ordinary time on the zero set makes the inverse clock a sum of lifetimes, with no extra chronological drift. The Poisson functional and independently computed clock transform identify intensity. Nonintegrability at zero explains infinitely many small excursions, while finite ∫(1∧ζ)n ensures finite total lifetime on bounded local-time windows almost surely.

Indexing by R’s right local time at zero, equal to 2L, would halve intensity. A local-time factor changes hitting, excursion and Ray–Knight constants simultaneously. One normalization is maintained.

## 37.12 Finding an Entrance Law for Excursions from Zero

<a id="local-entrance-law"></a>

Brownian motion from zero immediately visits both sides; its zero-state density is not a positive-excursion entrance law. Start at x>0 and kill at zero; reflection gives a difference-of-Gaussians kernel q. After its first ε-hit an excursion follows q, and its initial segment has mean duration at most ε². Time-shift errors remain controlled after multiplying by 1/ε, allowing ε↓0.

\[ q_t(x,y)=p_t(y-x)-p_t(y+x),\qquad n(e_t\in dy,t<\zeta)=\frac{2y}{\sqrt{2\pi}t^{3/2}}e^{-y^2/(2t)}dy,\quad y>0. \]

Later times use products of q. The entrance law incorporates departure from zero while avoiding zero inside. [Proof 4](../foundations/t-excursions.md#excursion-proof-entrance) controls the initial segment and low-height remainder instead of appealing vaguely to continuity from zero.

## 37.13 How to Select a Normalized Excursion

<a id="local-normalized"></a>

Though n is not a probability, disintegrate it by lifetime. Conditional finite-dimensional densities multiply entrance, killed interior and final zero-hit kernels, divided by lifetime density. Chapter 10 initially supplies versions only for almost every s. We still need an actual continuous positive path of lifetime one.

\[ e_t=\sqrt{(b_t^1)^2+(b_t^2)^2+(b_t^3)^2},\quad 0\le t\le1,\qquad b^1,b^2,b^3\text{ independent standard Brownian bridges}. \]

It is zero at both endpoints and strictly positive inside. Radial Gaussian kernels and the bridge terminal correction give exactly the lifetime-disintegrated finite-dimensional densities. This identifies normalized Brownian excursion; length s uses √s e(t/s). No undefined conditioning on a bridge remaining positive or future conditioned-tree limit is used. The [full check](../foundations/t-excursions.md#excursion-proof-normalized) keeps constants and measurable versions.

## 37.14 Treating Space as a New Evolution Parameter

<a id="local-spatial-profile"></a>

Lₜᵃ can be observed as a process in a. At suitable stopping times the entire occupation profile has its own Markov structure. This is stronger than a mean Green density: it concerns dependence across positions, not the shape of an expected curve.

Identify its joint law by E exp(−∫φL), with nonnegative spatial weight φ. Occupation turns this spatial reading into weighted Brownian time. A stopped fair reading leads to a second-order ODE. Before announcing Ray–Knight, inspect the process hidden in that equation.

## 37.15 Square-Root Noise Hidden in a Linear Equation

<a id="local-riccati"></a>

\[ \tfrac12v^{\prime\prime}=\varphi v,\quad v(0)=1,\quad v^\prime(R)=0,\qquad u=-\frac{v^\prime}{2v}:\quad u^\prime=2u^2-\varphi,\quad u(R)=0. \]

Let φ vanish outside [0,R]. Zero terminal derivative gives a constant reading beyond the penalty region. The solution v is positive and u nonnegative. Its logarithmic slope turns the linear equation into Riccati form. The term 2u² is exactly what diffusion coefficient 2√z produces on \(e^{-zu}\).

\[ dZ_x=\delta(x)dx+2\sqrt{Z_x}\,d\beta_x,\quad Z_0=z,\qquad E_ze^{-\int_0^R\varphi(x)Z_xdx}=\exp\left[-zu(0)-\int_0^R\delta(x)u(x)dx\right]. \]

Construct squared Bessel first by Chapter 35 existence and modulus uniqueness, then check its transform with a bounded exponential martingale. Ray–Knight is not used backward. δ=0 is continuous-state critical branching without immigration; δ=2 adds constant spatial immigration. Space takes the mathematical role of time, not a second physical motion of the particle.

## 37.16 First Ray–Knight at a First Hit

<a id="local-ray-first"></a>

Stop Brownian motion from zero at its first a-hit, a>0, and choose R>a containing the support of φ. Measure space backward, x=a−position, and put Zx=\(L_{T_a}^{a-x}\). No local time has accumulated at the newly reached a, so Z₀=0. Occupation and stopped Itô identify its Laplace reading as v(a).

\[ Ee^{-\int_0^R\varphi(x)L_{T_a}^{a-x}dx}=v(a)=\exp\left[-2\int_0^au(x)dx\right]. \]

This matches z=0 with δ=2 up to a, then zero. Laplace readings determine a nonnegative continuous field, hence Z is BESQ2 on [0,a] and continues conditionally on Za as BESQ0. The stopping rule and spatial direction matter: neither Tₐ nor a−x can be discarded, and a deterministic-time profile is not automatically this process.

[Proof 3](../foundations/t-ray-knight.md#ray-proof-first) obtains v(a) from stopped bounded exponentials without borrowing Chapter 38 Feynman–Kac, and checks Bessel constants against the Green mean 2min(x,a).

## 37.17 Second Ray–Knight after Fixed Contact Accumulation

<a id="local-ray-knight"></a>

At τℓ, sum positive-excursion rewards. The Poisson functional gives exp[−ℓn(1−\(e^{-A_\varphi}\))/2]. The same ODE yields n(1−\(e^{-A_\varphi}\))=−v′(0)=2u(0). The half from fair signs cancels the two exactly.

\[ (L_{\tau_\ell}^{x}:x\ge0)\ \overset d=\ \mathrm{BESQ}^{0}(\ell),\qquad (L_{\tau_\ell}^{-x}:x\ge0)\ \overset d=\ \mathrm{BESQ}^{0}(\ell),\quad\text{independently}. \]

The two profiles share the deterministic initial value ℓ, not another random variable. Their independence comes from the two excursion PRMs. BESQ0 transitions give explicit branching and extinction.

\[ E_ze^{-qZ_x}=\exp\left(-\frac{zq}{1+2qx}\right),\qquad P_z(Z_x=0)=e^{-z/(2x)},\qquad EZ_x=z\quad(x>0,q\ge0,z\ge0). \]

The law from the sum of initial masses equals that of summed independent processes: continuous-state branching. Every profile eventually dies while its mean at finite spatial positions stays constant. Chapter 20’s family-versus-mean distinction gains a new identified spatial process, rather than another expectation-loss story. [Proofs 4–5](../foundations/t-ray-knight.md#ray-proof-second) retain the matching and conditions.

## 37.18 A Diffusion’s Local Time Uses a Different Clock

<a id="local-diffusion-density"></a>

In Chapter 36’s nondegenerate SDE the quadratic clock is σ(X)²dt. Ordinary-time occupation therefore has density Lᵃ/σ(a)², not Lᵃ. A scale change also transforms local time because spatial units change a density.

\[ \int_0^tf(X_s)ds=\int_I f(a)\frac{L_t^a(X)}{\sigma(a)^2}da,\qquad L_t^{S(a)}(S(X))=S^\prime(a)L_t^a(X). \]

The first compares time measures and the second uses spatial change of variables. Chapter 36 Green occupation now links to individual paths: construct their densities first and then take expectations. A mean density was never each path’s occupation record.

## 37.19 Speed Can Be a Singular Measure

<a id="local-speed-clock"></a>

Requiring a speed density would exclude speed concentrated on sparse positions. Local time offers a construction: run Brownian motion, charge its contact accumulation against a measure, and invert that clock.

\[ A_s=\frac12\int_JL_s^y(B)m(dy),\qquad T_t=\inf\{s:A_s>t\},\qquad Y_t=B_{T_t}. \]

Take locally finite Radon speed charging every nonempty open subinterval, and stop Brownian motion on exit. Continuous local time makes A finite continuous; full support makes it strictly increasing. Thus Y is continuous; strong Markov and additivity give strong Markov. The half factor is essential: Brownian speed 2dy must give A=s.

The [construction and converse](../foundations/t-diffusion-time.md#time-proof-construction) specify Green kernels, singular speed and the natural-scale class. Without full support the clock may skip travel through a spatial interval and create jumps. Original Brownian continuity alone is insufficient.

For example enumerate rationals qₙ in (0,1) and put m=∑2⁻ⁿ\(\delta_{q_n}\). It is locally finite with full support, yet purely atomic; the construction still gives continuous paths. Occupation shows zero ordinary time at irrational positions, without saying those positions are never visited. A continuous crossing passes every intervening position. Speed support, time spent and the set of visited states are distinct.

## 37.20 Recovering Chapter 36’s Equation from Its Clock

<a id="local-speed-converse"></a>

For continuous positive m′=2/α², inverse substitution gives Tₜ=∫₀ᵗα(Y)²du, the bracket of Y. Dividing by α gives a bracket-t martingale and a Brownian driver, with dY=α(Y)dW. Applying S⁻¹ recovers Chapter 36’s drift and diffusion.

For a continuous regular strong Markov process in natural scale with finite mean compact exits, those means are concave. Their negative second Stieltjes measure uniquely determines m. Compare integrated Tanaka with the strong-Markov remaining-exit-time martingale to force t=½∫Lₜᵃm(da). DDS recovers the Brownian clock. The [converse proof](../foundations/t-diffusion-time.md#time-proof-converse) constructs this measure without assuming a density.

## 37.21 What Happens When Speed Has a Boundary Atom

<a id="local-sticky"></a>

Chapter 36 separated reflection from absorption. Now construct a sticky boundary between instantaneous reflection and trapping. For reflected Brownian R=x+β+K, K pushes only at zero and right local time there is 2K. Add an atom of mass θ to speed 2dy:

\[ A_s=s+\theta K_s,\qquad Y_t=R_{T_t},\qquad \int_0^t\mathbf1_{\{Y_u=0\}}du=\theta K_{T_t}. \]

For θ>0, zero gains ordinary occupation, without exponential holding intervals followed by restarts. There are no finite flat waits: the clock gives contacts positive total time. Killing at an independent exponential K-threshold adds an elastic boundary. The interior operator stays unchanged while smooth tests satisfy f′(0)=θAf(0)+κf(0).

The [boundary proof](../foundations/t-diffusion-time.md#time-proof-boundaries) identifies the parameters for continuous local Feller rules at finite regular endpoints. Removing excursions leaves continuous increasing boundary time in local time, hence deterministic drift θl; killing has a memoryless threshold. Jump-in boundaries and interior killing are excluded.

## 37.22 The Two Boundary Integrals Still Answer Different Questions

<a id="local-boundary-recovery"></a>

Scale-speed construction preserves Chapter 36’s Σ and N. Green extends to singular Radon speed and the λ-harmonic ODE becomes Stieltjes–Volterra. Tanaka still gives its discounted martingale. Σ tests finite arrival; N tests continuous instantaneous entrance at inaccessible endpoints.

A singular model need not have Lipschitz σ. Entrance instead uses ordered paths coalescing on meeting, Green return bounds and clock path-law continuity. [Proof 5](../foundations/t-diffusion-time.md#time-proof-feller) specifies the replacements. The four boundary types remain distinct, as do reachability, admissibility as an initial state and rules after arrival.

## 37.23 How a Spatial Measure Identifies an Accumulation

<a id="local-revuz"></a>

For positive Radon μ set Aᵗμ=∫Lₜᵃμ(da). It is finite continuous and additive by compact path ranges and joint continuity. A point mass gives local time, μ=q(a)da gives ∫q(B)ds, and singular μ charges sets negligible for ordinary time.

\[ \lim_{t\downarrow0}\frac1t\int_{\mathbb R}g(x)E_x\!\int_0^tf(B_s)dA_s^\mu dx=\int_{\mathbb R}f(a)g(a)\mu(da). \]

Here f is nonnegative continuous compactly supported, g nonnegative bounded continuous, reference dx. Support, Gaussian symmetry and DCT prove the identity and identify μ as Revuz measure. Reference 2dx doubles the right side. This constructs and identifies explicit Brownian functionals; arbitrary-PCAF/smooth-measure correspondence for general right processes and its exceptional-set theory remain Chapter 38, not established by this identity.

## 37.24 Zero-Length Contacts Leave an Entire Structure

<a id="local-insight"></a>

The original zero answer remains correct. Brownian ordinary time at one position is still zero. We now place that fact at the right level: construct spatial occupation density, measure contact, order excursions, change clocks, and identify the spatial profile as another diffusion.

Tanaka locates accumulation where curvature concentrates. Excursion theory lets a zero set organize independently occurring paths. Ray–Knight connects occupation with continuous-state branching. Speed atoms turn ordinarily negligible contacts into positive occupation. Distinct theorems support these links; there is no equation of zero with nonzero.

For a spatial charge, boundary and discount, what equation does expected path accumulation solve? If charge is concentrated at a point or on a singular measure, how should its source and boundary conditions be read? Local time supplies constructed random objects. Their potentials and deterministic equations are the next objects to identify.

### Sources and Proof Scope

Ray and Knight’s 1963 works studied sojourn densities and spatial Markov structure. This is a modern reconstruction through Tanaka, explicit ODEs and Poisson excursions, not the original discovery order. Bibliography: [Knight](https://doi.org/10.1090/S0002-9947-1963-0154337-6), [Ray reference verification](https://www.ams.org/books/surv/018/surv018-endmatter.pdf). Scaling is checked against the symmetric Brownian local-time convention in the [public author paper by Perman–Wellner](https://pmc.ncbi.nlm.nih.gov/articles/PMC4847753/). Their signed measure is pushed through absolute value here; each sign contributes one half.

Full proofs are in [T-LOCAL-TIME](../foundations/t-local-time.md), [T-EXCURSIONS](../foundations/t-excursions.md), [T-RAY-KNIGHT](../foundations/t-ray-knight.md) and [T-DIFFUSION-TIME](../foundations/t-diffusion-time.md). General-right-process Revuz correspondence is not claimed complete here.
