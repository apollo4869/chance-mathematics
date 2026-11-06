# Chapter 38: Random Motion Meets Partial Differential Equations Again — Feynman–Kac and Potential Theory

A particle moves inside an interval. Every additional second incurs another second of storage cost; the account closes at the boundary. Someone who sees no individual trajectory asks for the average bill when starting at x. That average is a deterministic function. The path’s irregularity has not disappeared, but an equation may organize what survives averaging.

## 38.1 An Account that Closes at the Boundary

<a id="fk-discovery"></a>

Take standard Brownian B stopped at its first exit τ from I=(0,1). Chapter 36’s Green kernel computes mean occupation; now charge one unit per second everywhere. Integrating the kernel gives u(x)=Eₓτ=x(1−x), with second derivative −2. The important observation is not the polynomial: the average of a random exit time is determined by a local differential condition and two boundary values.

\[ u(x)=E_x\tau=x(1-x),\qquad -\frac12u^{\prime\prime}=1,\qquad u(0)=u(1)=0. \]

If costs depend on position, or the endpoints pay different rewards, does the same relation survive? Existing paths and integral tools let us examine the mechanism instead of guessing a new differential equation.

## 38.2 The Remaining Bill after a Short Time

<a id="fk-local-equation"></a>

Let f(Xₛ) be the reward rate and g(Xτ) the terminal payment. Without discount, reward before a short time S plus the expected future account at \(X_S\) must equal the initial account. Use a local exit stopping time to stay inside the state interval. Strong Markov is what makes “restart the calculation here” mathematically legitimate.

\[ u(x)=E_x\left[\int_0^S f(X_s)ds+u(X_S)\right],\qquad Lu=-f\quad\hbox{if }u\hbox{ has the required regularity}. \]

If u is smooth enough, Itô reads its short-time mean change as Lu. The minus sign now has a meaning: remaining reward decreases as current reward is paid. This calculation has not proved smoothness or attainment of boundary values. Keeping those questions separate prevents an attractive formal computation from masquerading as an existence theorem.

## 38.3 How an Accumulated Cost Changes Weights

<a id="fk-cost"></a>

Suppose each position has instantaneous failure rate q(x)≥0. Whether an account survives depends on the path accumulated so far. Take an independent mean-one exponential threshold E and stop when cumulative q exceeds E. Conditional on the path, survival is exp(−Qₜ). Chapter 21 supplied the exponential law; the new object is path-dependent accumulated hazard, not another fixed-rate Poisson clock.

\[ Q_t=\int_0^tq(X_s)ds,\qquad P(E>Q_t\mid X)=e^{-Q_t},\qquad Q_{s+t}=Q_s+Q_t\circ\theta_s. \]

The same exponential can represent discounting rather than actual death. A signed q bounded below can be shifted to a nonnegative potential on a finite horizon, extracting a deterministic exponential. Infinite horizons require a new integrability check; finite-time bounds do not automatically control the entire future.

## 38.4 The Formula Grows from Restarting the Account

<a id="fk-dynamic"></a>

On a fixed horizon t, pay h at maturity and f along the way. After a short S, costs already incurred are fixed and the remaining account is multiplied by their survival factor. This gives the full dynamic relation. Looking for a function whose derivatives express it is more informative than first memorizing a formula.

\[ u(t,x)=E_x\left[e^{-Q_t}h(X_t)+\int_0^te^{-Q_s}f(X_s)ds\right],\qquad u(t,x)=E_x\left[\int_0^S e^{-Q_s}f(X_s)ds+e^{-Q_S}u(t-S,X_S)\right]. \]

For smooth candidate u, the product rule gives −∂ₜu from time, Lu from motion, −qu from cost and f from reward. No extra drift under restarting means ∂ₜu=Lu−qu+f. Feynman–Kac expresses this account structure, not a claim that averaging randomness produces any PDE. [Derivation and conditional Fubini](../foundations/t-feynman-kac.md#fk-proof-dynamic) are given step by step.

## 38.5 Verification Is Different from Existence

<a id="fk-verification"></a>

The precise verification statement is this: for a nonexplosive SDE with time-homogeneous locally Lipschitz coefficients, if bounded v∈\(C^{1,2}\) satisfies the equation and initial h, with q≥0 and bounded f,h, then v equals the path expression. Stop on large balls and integral-energy levels, apply Itô to \(e^{-Q_s}\)v(t−s,Xₛ), take expectations and remove the stops. This also proves uniqueness in that classical class.

Chapter 35 separated a rule from existence of its object. The same distinction matters here: verification cannot turn “if v exists” into “the expectation is differentiable.” We must construct a differentiable solution.

## 38.6 The Gaussian Kernel Gives Regularity as Well as Representation

<a id="fk-classical-existence"></a>

For Brownian motion on Rᵈ, assume h,q,f and derivatives through order two are bounded uniformly continuous, with q≥0. Solve the following mild equation first, without prematurely calling it classical. Gaussian convolution Pₜ preserves this regularity; successive substitutions have errors controlled by (Ct)ⁿ/n!, giving convergence on every finite horizon.

\[ u(t)=P_th+\int_0^tP_{t-s}(f-qu(s))ds,\qquad \partial_tu=\tfrac12\Delta u-qu+f. \]

The same Banach norm controls second derivatives, while heat-semigroup strong continuity supplies the time derivative. We now genuinely have a \(C^{1,2}\) solution, which verification identifies with the random expression. The [convergence and differentiation proof](../foundations/t-feynman-kac.md#fk-proof-parabolic) is complete in the companion. For merely h=1_{x>0}, the solution is smooth at t>0 but tends to 1/2 at x=0 as t↓0, not h(0)=0. A specified single-point initial or boundary value need not survive smoothing in the claimed classical sense.

## 38.7 Why Random Boundary Settlement Is Harmonic

<a id="fk-dirichlet"></a>

Replace maturity by exit from a bounded domain D. With no running reward or cost, h(x)=Eₓg(BτD). Restart after exit from any interior ball: h equals its spherical average. This is not an analogy with harmonicity. Combine the spherical averages into a smooth radial convolution to prove h itself smooth, then expand at small radii to obtain Δh=0.

With bounded locally Hölder source f and cost q≥0, the local account becomes u=H_Vu+G_V(f−qu). Integrability of the first Green derivative gives continuity and local Lipschitz regularity; cancellation in second derivatives together with the Hölder error then gives C². Thus −½Δu+qu=f. [Companion Sections 3–4](../foundations/t-feynman-kac.md#fk-proof-dirichlet) do not hide these two regularity steps behind a “standard PDE result.”

## 38.8 A Correct Interior Equation Can Still Miss Boundary Data

<a id="fk-irregular-boundary"></a>

The path expression knows which boundary points are actually visible from inside. A strict exterior-ball barrier controls the probability of escaping a neighborhood of z, so continuous boundary data are attained there. In a punctured planar unit disk, however, Brownian motion almost surely avoids the center and exits through the outer circle. Assign value one at the central boundary point and zero on the outer circle: the expectation remains identically zero.

\[ P_r(T_\varepsilon<T_1)=\frac{\log(1/r)}{\log(1/\varepsilon)}\longrightarrow0\quad(d=2),\qquad 0<\varepsilon<r<1. \]

The boundary data are continuous: zero is isolated in the boundary. What fails is regularity of that point as seen by interior paths, not smoothness of the assigned data. A Dirichlet problem therefore contains both an interior differential relation and constraints on boundary attainment. The latter cannot be erased from the equation’s notation.

## 38.9 Why Infinity Requires Its Own Settlement

<a id="fk-infinity"></a>

On the half-line, u(x)=x is harmonic with u(0)=0, but Brownian motion eventually hits zero and has terminal expectation zero. There is no contradiction: u is unbounded and stopping also at level n does not produce a UI family. Rare far-end events carry large values, so an almost-sure terminal limit does not justify removing n. UI now governs validity of an unbounded Dirichlet representation, rather than repeating the old spike sequence.

## 38.10 Unspent Reward Produces Excessiveness

<a id="potential-excessive"></a>

At time t only part of a future total reward U remains. For nonnegative charges, U≥PₜU; with discount α, U≥\(e^{-\alpha t}\)PₜU. We therefore need an object broader than preservation of local averages. A nonnegative u is α-excessive when this inequality holds for every t and its right side returns to u as t↓0. The limit condition selects a version compatible with the motion.

\[ U(x)=E_x\int_0^\zeta e^{-\alpha s}dA_s,\qquad U(x)-e^{-\alpha t}P_tU(x)=E_x\int_0^{t\wedge\zeta}e^{-\alpha s}dA_s\ge0. \]

The definition comes from splitting reward in time, not renaming harmonic functions. For continuous locally bounded u, \(e^{-\alpha t}\)u(Xₜ) is a localized supermartingale. Harmonicity preserves the unspent average; a potential records accumulation already occurring along paths. [Conditions and sampling](../foundations/t-potential.md#potential-proof-excessive) make clear that no unproved fine-version theorem for arbitrary Borel excessive functions is being used.

## 38.11 The Green Kernel Moves Path Time Back to Space

<a id="potential-green"></a>

Return to a bounded interval. The killed Brownian Green kernel relative to dx is below. Gf is expected ordinary-time reward. Replacing f(y)dy by a measure μ, Chapter 37 local time makes Gμ a genuine expected random accumulation, not just a formal integral.

\[ G_I(x,y)=2\frac{(x\wedge y-a)(b-(x\vee y))}{b-a},\qquad G_I\mu(x)=E_x\int_I L_\tau^y\mu(dy). \]

Chapter 36 used Green to measure average occupation. The new point is superposition of spatial sources: different charge measures yield different potentials under the same motion. Changing the source does not change the generator; changing the speed measure changes the motion itself.

## 38.12 Separating Sources from Boundary Information

<a id="potential-riesz"></a>

Fix Brownian motion killed at the interval endpoints and take α=0. A finite continuous nonnegative 0-excessive function is concave: stopping at the two ends of any subinterval puts u above their linear interpolation. Its second derivative need not be a function, but is a negative Stieltjes measure. This curvature is the interior source. Endpoint limits leave an affine harmonic function h.

\[ u=h+G_I\mu,\qquad \mu=-\tfrac12u^{\prime\prime}\ge0,\qquad h(x)=\frac{b-x}{b-a}u(a+)+\frac{x-a}{b-a}u(b-). \]

This is the 0-excessive one-dimensional Riesz decomposition proved here. For α>0 the discount term remains, so neither this concavity nor its affine harmonic remainder follows automatically. First integrate the second-derivative measure on compact interior intervals, then increase the intervals. Monotone Green limits handle source mass possibly infinite near the boundary. Curvature uniquely determines μ and endpoint limits uniquely determine h; h is also the greatest nonnegative harmonic minorant of u. The [full proof](../foundations/t-potential.md#potential-proof-riesz) does not substitute this argument for general Hunt-process Riesz theory.

## 38.13 Zero Length Can Still Carry a Nonzero Potential

<a id="potential-capacity"></a>

A point has zero length, yet one-dimensional Brownian motion can hit it and accumulate local time there. Lebesgue measure alone cannot decide which sets matter. Instead ask how much energy is needed to raise a potential to at least one on the set. On I, use absolutely continuous zero-endpoint v with energy ½∫|v′|²: this defines relative capacity.

\[ \operatorname{cap}_I(K)=\inf_{v\in H_0^1(I),\,v\ge1\ \text{on }K}\frac12\int_I|v^\prime|^2dx,\qquad \operatorname{cap}_I(\{c\})=\frac{b-a}{2(c-a)(b-c)}>0. \]

For a singleton c the minimizer is a piecewise linear tent; Cauchy–Schwarz proves optimality. For a general nonempty compact K, its equilibrium potential rises to one at minK, stays one through maxK, then falls. It equals the probability of hitting K before exit. The equilibrium measure consists of its two curvature atoms, with total mass equal to capacity. Energy, hitting and source strength are linked by [one explicit calculation](../foundations/t-potential.md#potential-proof-capacity), not three analogies.

## 38.14 Sweeping Retains a Source’s Effect on a Set

<a id="potential-sweeping"></a>

If observations are restricted to K, can an interior source be moved onto K without changing them? Redistribute each source point y according to where its motion first hits K. Mass whose paths exit without hitting is lost. The resulting μᴷ is the swept measure.

\[ \mu^K(C)=\int P_y(B_{T_K}\in C,T_K<\tau)\mu(dy),\qquad G_I\mu^K(x)=E_x[G_I\mu(B_{T_K});T_K<\tau]. \]

Strong Markov splits Green occupation before and after hitting; symmetry then interchanges x and y and proves the second identity. The swept potential is at most the original, equals it on K and is harmonic off K. Local observation retains not every original source location but its effect transmitted by the motion to the observed set. The [proof](../foundations/t-potential.md#potential-proof-balayage) identifies where symmetry and nonnegative Tonelli are used.

## 38.15 How an Equation Detects a Charge at One Point

<a id="fk-singular"></a>

Charge γ per unit of local time at an interior c: Aₜ=γLₜᶜ. The cost survives even though ordinary time at c is zero. Define discounted reward until exit. Forcing this cost into q(x)dt with q zero away from c would incorrectly erase it as an almost-everywhere function.

\[ -\tfrac12u^{\prime\prime}+u\mu=f\,dx,\quad \mu=\gamma\delta_c,\qquad u^\prime(c+)-u^\prime(c-)=2\gamma u(c). \]

The point cost appears as a derivative jump. Typically u is continuous but not C² across c; an everywhere classical equation is inappropriate. Changing the mathematical class of the source changes the required class of solution.

## 38.16 A Weak Solution Does Not Mean a Weaker Proof

<a id="fk-weak"></a>

For finite positive Radon μ and \(f\in L^2(I)\), multiply the equation by a zero-endpoint test φ and integrate by parts. For zero boundary data the unknown u belongs to H₀¹(I). For nonzero endpoint g, take the affine lift h with h(a)=g(a), h(b)=g(b), and seek u=h+v with v∈H₀¹(I). Then B(v,φ)=∫fφdx−B(h,φ), with B the form below. One cannot just add h to the zero-boundary solution with the same source: the measure term acts on the lift too. The form ½∫u′φ′+∫uφdμ is well defined because one-dimensional H¹ functions are continuous. It controls the derivative norm, so Hilbert representation constructs a unique weak solution. Its measure-valued second derivative then allows generalized Itô.

\[ \frac12\int u^\prime\varphi^\prime dx+\int u\varphi\,d\mu=\int f\varphi\,dx,\qquad u(x)=E_x\left[e^{-A_\tau}g(B_\tau)+\int_0^\tau e^{-A_s}f(B_s)ds\right],\quad A_t=\int L_{t\wedge\tau}^y\mu(dy). \]

The [complete proof](../foundations/t-feynman-kac.md#fk-proof-singular) constructs the weak solution first and identifies it with the path expression by integrating Tanaka. “Weak” describes testing, not proof quality. Connections among classical, distributional, energy-weak and probabilistic solutions require the appropriate regularity and uniqueness arguments.

## 38.17 What Local Averages Recover and What They Miss

<a id="potential-differentiation"></a>

Existence of an abstract RN density does not yet recover it from small-ball averages. Singular sources now make that distinction essential. Fivefold ball covering gives a weak maximal-average bound. Local averages of continuous functions converge directly; L¹ approximation and the weak bound control the error and prove Lebesgue differentiation.

\[ \nu=f\,dx+\nu_s\quad\Longrightarrow\quad\frac{\nu(B(x,r))}{|B(x,r)|}\longrightarrow f(x)\quad\hbox{for Lebesgue-a.e. }x. \]

The singular part has zero density almost everywhere yet may carry all the nonzero mass; δ_c is the smallest example. This explains the need for a measure equation. The [covering, function and measure steps](../foundations/t-differentiation.md) prove the result. It does not claim convergence at every point or use the RN theorem’s name as a substitute for differentiation.

## 38.18 Identifying the Same Kind of Accumulation across Paths

<a id="revuz-additive"></a>

Running reward and local time share additivity: the bill for s followed by t is the sum of the two bills. Pathwise increase alone is insufficient. Aₜ=t² does not restart using only the future shifted path; secretly carrying total elapsed time into the second part changes the state information. A PCAF requires continuity, nonnegative increase, adaptation, zero initial value and genuine shift additivity.

\[ A_{s+t}(\omega)=A_s(\omega)+A_t(\theta_s\omega). \]

Chapter 37 constructed Brownian A from μ. Now reverse the question: can a spatial measure identify an existing random accumulation? A single start in EₓAₜ may miss much of the state space. Average over starting points and record where the charge occurs.

## 38.19 A Revuz Reading Needs a Reference Measure

<a id="revuz-reference"></a>

Choose a reference m. Let f record the charging location and g weight the start. A short-time average per unit time can read spatial charge intensity. The reference is not a harmless notational choice: replacing m by cm multiplies the reading for the same A by c.

\[ \lim_{t\downarrow0}\frac1t\int g(x)E_x\int_0^t f(X_s)dA_s\,m(dx)=\int f(y)g(y)\mu_A(dy). \]

For one-dimensional Brownian motion, Lᵃ corresponds to δₐ relative to dx and to 2δₐ relative to speed 2dx. Both the clock factor in Chapter 37 and the reference factor here matter. The small-time identity is an identification condition; writing it down does not prove existence for every allowed measure or uniqueness.

## 38.20 Symmetry Moves Initial Weight to the Charging Location

<a id="revuz-correspondence"></a>

For an m-symmetric process the full identity is more useful than the small-time limit. If A=∫q(X)ds, interchange the starting integral and transition kernel: g becomes Pₛg. The calculation suggests the same structure for singular measures. The full identity precisely relates path accumulation to deterministic kernel action.

\[ \int g(x)E_x\int_0^t f(X_s)dA_s\,m(dx)=\int_0^t\int (P_sg)(y)f(y)\mu_A(dy)ds. \]

This revisit adds something new: Pₛ not only averages future functions back to a start; symmetry also carries initial observation weights onto a singular charge. Nonsymmetric processes need a dual semigroup or appropriate excessive-reference conditions. The displayed identity cannot simply be copied unchanged.

## 38.21 Declaring the Correspondence We Can Actually Prove

<a id="revuz-class"></a>

To make existence, versions and uniqueness independently checkable, fix a process class: compact metric E, finite full-support m, a conservative m-symmetric Feller Hunt process, and a finite jointly continuous symmetric resolvent kernel rλ for every λ>0. Measures are finite positive Borel μ; functionals are PCAFs with continuous bounded 1-potential U₁ᴬ. Between these exact classes there is a bijection, with U₁ᴬ=R₁μ.

\[ U_1^A(x)=E_x\int_0^\infty e^{-s}dA_s=R_1\mu(x). \]

This is not merely a single Brownian formula: reflecting Brownian motion on compact intervals and finite reversible continuous-time chains qualify. Kernel continuity is a real assumption; diagonal singularities for higher-dimensional Brownian motion warn against deleting it. [Companion Section 1](../foundations/t-revuz.md#revuz-proof-class) specifies paths, equivalence and nonempty examples.

## 38.22 Building an Actual Random Accumulation by Spatial Smoothing

<a id="revuz-construction"></a>

Given μ, set u=R₁μ and smooth it into densities \(f_n=nR_n\mu\). Ordinary integrals Aₙ=∫fₙ(X)ds are already legitimate, and their potentials uₙ=\(nR_nu\) converge uniformly to u. Potential convergence alone is insufficient: the accumulations themselves must converge. The key writes the square of a difference of charges as a resolvent.

\[ E_x\left(\int_0^\infty e^{-s}f(X_s)ds\right)^2=2R_2(fR_1f)(x). \]

When R₁f is small, the right side is controlled by potential error. Doob’s inequality turns terminal error into L² maximal error over a time interval. One subsequence on canonical path space then gives a locally uniform limit, retaining continuity, increase and all-time shift additivity together. The [complete construction](../foundations/t-revuz.md#revuz-proof-construction) handles kernel interchange for singular measures, atomless Stieltjes limits and one shift-invariant version; it does not skip construction by asserting that an additive functional exists.

## 38.23 Reverse Identification and the Actual Boundary of Generality

<a id="revuz-reverse"></a>

Starting from A, stationarity of m makes E_m∫₀ᵗf(Xₛ)dAₛ linear in t, defining finite \(\mu_A\). Recovering the potential at each start needs left-endpoint readings of future A-increments on fine grids, Markov and symmetry, followed by Stieltjes limits. Random charges cannot be assumed independent of their past. Finally \(u_A\)=R₁\(\mu_A\); two functionals with the same potential differ by a continuous finite-variation martingale and must agree. The [reverse and uniqueness proof](../foundations/t-revuz.md#revuz-proof-reverse) closes the correspondence in the stated class.

In broader theory, a smooth measure need not have a smooth density. It must avoid zero-capacity sets and admit an appropriate finite-measure nest. General Hunt or right processes also involve quasi-continuous potentials, exceptional starts and nest pasting. The continuous bounded-potential theorem is not presented as a proof of these broadest versions: approximation for arbitrary smooth measures and general PCAF version theory remain an [explicit unclosed range](../foundations/t-revuz.md#revuz-proof-boundary). Chapter 37 separately establishes the full explicit one-dimensional Radon local-time construction.

## 38.24 Changing Path Weights Changes the Evolution Operator

<a id="fk-additive-semigroup"></a>

A continuous additive cost gives Pₜᴬf=Eₓ[\(e^{-A_t}\)f(Xₜ)]. Additivity preserves the semigroup property, but generally not mass: the motion is killed. For A from qdt, the generator becomes L−q and the Laplace resolvent satisfies the ordered identity below.

\[ R_\lambda^A=R_\lambda-R_\lambda(qR_\lambda^A),\qquad P_{s+t}^A=P_s^AP_t^A. \]

As a multiplication operator, q cannot commute freely past Rλ. A singular A need not be represented by an ordinary bounded q, yet the path semigroup still makes sense; in one dimension it gives the measure-valued weak equation above. Random integrals, additive functionals and deterministic operators are linked by actual identities, not merely by the word “accumulation.”

## 38.25 Boundary Charges Differ from Interior Point Charges

<a id="fk-robin"></a>

Take Brownian R=x+W+K reflected at zero and stopped at one. Killing at rate κ along K gives, by Itô on \(e^{-\kappa K}\)u(R), boundary drift (u′(0)−κu(0))dK. Correct settlement requires u′(0)=κu(0). The interior operator remains ½u″ while reflection’s Neumann condition becomes Robin.

This is not a renamed interior δ-source jump condition: a boundary has only one derivative side and K uses a different normalization. Chapters 36–37 separated an interior operator from a complete process. We now see how boundary accumulation leaves a calculable condition in the deterministic equation. Ordinary time, local time and the boundary regulator have distinct roles.

## 38.26 Two Readings of One Structure, Each with Conditions

<a id="fk-insight"></a>

The original random bill is no longer just an exit-time example. Splitting time gives a dynamic relation and Itô reads it as an equation. Green transfers accumulation to space; Riesz separates interior sources and boundary information; capacity identifies zero-length sets that still affect motion; sweeping retains a source’s effect at specified observations. Singular charges force measures and weak solutions to remain visible, rather than compressing every problem into everywhere smooth functions.

Successive random motion and a deterministic equation can be two readings of one structure, but their equivalence rests on conditions: classical regularity, boundary regularity, UI at stopping, the reference measure and the functional class cannot be dropped. The new ability is to identify what path information a formula preserves and where another language is needed to see the rest.

One concrete difficulty remains. Gaussian averaging can smooth discontinuous data, whereas a general random equation need not. To decide whether a random output has a smooth density, rather than merely represent its expectation, can we perturb the driving noise and examine the response? Spatial derivatives have given equations; what perturbing randomness reveals is a different question worth pursuing.

### Sources and Proof Scope

Kac’s 1949 paper [On Distributions of Certain Wiener Functionals](https://www.jstor.org/stable/1990512) studies Wiener-functional distributions. This chapter is a modern reconstruction using established stochastic integration, stopping and semigroups, not a reenactment of discovery or an identification of real exponential weights with unjustified oscillatory quantum integrals. Revuz terminology and broader assumptions are compared with [§3 of the author’s public paper](https://www.kurims.kyoto-u.ac.jp/~nkajino/preprints/HTCRBM32a.pdf); the broader unproved range is separated in the chapter and companion.

Complete proofs: [T-FEYNMAN-KAC](../foundations/t-feynman-kac.md), [T-POTENTIAL](../foundations/t-potential.md), [T-REVUZ](../foundations/t-revuz.md), [T-DIFFERENTIATION](../foundations/t-differentiation.md).
