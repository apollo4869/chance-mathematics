# Chapter 31: How Can We Integrate Along a Nondifferentiable Random Path? — Itô Integral and Quadratic Variation

Multiply each small change by the position before the change, then add over the pieces. This seems familiar: integrating position times velocity should leave half the square of position. Even without a velocity we can first write finite sums and ask whether continuity is enough to preserve that answer.

For a Brownian path, the finite sum itself identifies what cannot be discarded. It is not an error term added afterward to repair a calculation. It is already present in multiplication on each interval and persists when the partition is refined.

## 31.1 The Missing Term Is Not an Error Tending to Zero

<a id="ito-left-sums"></a>

Let B be standard Brownian motion starting at zero and π a deterministic partition of [0,t]. Before defining a stochastic integral, the difference-of-squares identity alone gives

\[ \sum_i B_{t_i}(B_{t_{i+1}}-B_{t_i})=\frac12\left(B_t^2-\sum_i(\Delta_iB)^2\right). \]

For a continuous finite-variation path, the sum of squares is bounded by its largest increment times its total variation, and tends to zero. But [§26.11](26-brownian-properties.md#brownian-dyadic-variation) establishes the Brownian square-sum limit t at a fixed endpoint along dyadic grids. Applied here, that result makes the limit of the left sum half the square minus t/2. We do not repeat the independent-increment calculation; the new task is to make this limit into an integration operation stable for random coefficients.

Right endpoint values add the whole sum of squares to the finite sum. Using the average of the two endpoint positions gives half the square by exact finite algebra. These are not merely different notations for the same calculation.

\[ \begin{aligned} \sum_i B_{t_{i+1}}\Delta_iB&=\sum_i B_{t_i}\Delta_iB+\sum_i(\Delta_iB)^2,\\ \sum_i\frac{B_{t_i}+B_{t_{i+1}}}{2}\Delta_iB&=\frac12B_t^2. \end{aligned} \]

An ordinary Riemann–Stieltjes integral requires the answer to be independent of tagging, whereas these endpoint choices leave limits differing by t. Continuity has not failed. What fails is treating every second-order term as something that must eventually disappear.

## 31.2 What Is Known Before a Coefficient Meets an Increment

We retain Chapter 30's usual conditions on the filtration: completeness and right continuity. Brownian motion is always relative to this filtration: B is adapted, and future increments are independent of current information with the appropriate Gaussian variances. Gaussian marginal distributions alone do not suffice. If a future \(B_t\) is disclosed at the start, the conditional-mean calculations below fail.

Choose bounded ξ using information at s, then multiply it by the increment on (s,t]. Its conditional mean is zero, while its conditional mean square retains exactly ξ²(t−s).

\[ E[\xi(B_t-B_s)\mid\mathcal F_s]=0,\qquad E[\xi^2(B_t-B_s)^2\mid\mathcal F_s]=\xi^2(t-s). \]

Chapter 30 explains why the predictable σ-algebra describes such rules; we use its rectangular-generator result without retelling the example. The new fact is that prior measurability not only preserves conditional fairness but also makes errors from different intervals orthogonal in mean square. That becomes the control needed to extend integration.

## 31.3 First Add Finitely Many Legitimate Choices

<a id="ito-isometry"></a>

Take bounded elementary predictable H, with a random coefficient on each interval measurable at its left endpoint. Its value at time zero does not affect the integral. Define I(H) by finite sums, letting the current interval’s increment evolve continuously with the current time.

\[ H_s=\sum_{i=0}^{m-1}\xi_i\mathbf1_{(t_i,t_{i+1}]}(s),\quad\xi_i\in L^\infty(\mathcal F_{t_i}),\qquad I_t(H)=\sum_i\xi_i(B_{t\wedge t_{i+1}}-B_{t\wedge t_i}). \]

This process is continuous and adapted. For s<t, split each interval at s: completed intervals no longer change; an interval straddling s has its coefficient already in Fₛ; intervals starting later are conditioned first at their own left endpoints and then at Fₛ. Every future increment has conditional mean zero. Thus I(H) is a genuine martingale, not merely a variable with mean-zero terminal value.

In the terminal square, the later increment is orthogonal to everything known before it, so cross terms disappear. This leaves the isometry. At a non-grid terminal time, simply cut the last interval.

\[ E I_T(H)^2=\sum_i E\xi_i^2(t_{i+1}-t_i)=E\int_0^T H_s^2\,ds. \]

The isometry is an existence mechanism: if two elementary rules are close in mean square over time and samples, their integral terminal values are equally close. Its right side does not require an integral already to exist along each Brownian path.

## 31.4 How Completeness Preserves Both Continuity and the Martingale Property

<a id="ito-extension"></a>

Let H be predictable with finite E∫H²ds. Predictable rectangles generate P, so bounded elementary predictable processes are dense in its L² space: first approximate indicators using the algebra generated by rectangles, then truncate and step-approximate general functions. The measure is ds·P(dω) restricted to the predictable σ-algebra; H need not be deterministic.

Approximate H by elementary Hⁿ. The isometry and Doob’s maximal inequality control the whole time interval, not merely each fixed time.

\[ E\sup_{t\le T}|I_t(H^n)-I_t(H^m)|^2\le4E\int_0^T|H^n-H^m|^2\,ds\longrightarrow0. \]

Choose a subsequence with summable successive maximal-norm differences to obtain almost surely uniformly convergent continuous paths. Measurable fixed-time limits and completeness preserve adaptedness; continuity of conditional expectation in L² preserves the martingale relation. The original sequence converges in the same maximal norm to this process, so the limit is independent of approximation. This defines the Itô integral using only conditional orthogonality, L² completeness and a maximal estimate.

\[ I_t(H)=\int_0^t H_s\,dB_s,\qquad E I_t(H)^2=E\int_0^t H_s^2\,ds,\qquad E\sup_{t\le T}|I_t(H)|^2\le4E\int_0^T H_s^2\,ds. \]

The same ds·P equivalence class gives indistinguishable integral processes. General approximating sequences converge in the L² maximal norm, hence also ucp. Almost sure uniform convergence has been proved only for a chosen summable-error subsequence, not for every approximation sequence. Ucp means that on every finite T the probability of a maximal error exceeding any ε tends to zero.

The Brownian clock has no time atoms, which also lets square-integrable progressive H have a predictable ds·P representative. The [full past-time-averaging proof](../foundations/t-ito-bracket.md#t-ito-progressive) supplies this extension. Choosing predictable representatives does not claim a uniquely possible formal language; it supplies a framework consistent with temporal information and extendible to other clocks.

## 31.5 The Opening Finite Sum Becomes an Identity of Processes

Take H=B. It is continuous and adapted, hence predictable, with E∫₀ᵀB²ds=T²/2. The energy error of left step approximations is at most T times the mesh, so the newly constructed theory gives convergence of their integrals. At each fixed t, the opening finite identity and the Chapter 26 dyadic quadratic variation identify the limit. Take a common null set over rational t and use continuity of both sides to obtain the identity up to indistinguishability.

\[ \int_0^t B_s\,dB_s=\frac12(B_t^2-t). \]

This is not an example deduced from Itô formula; it is a fact that the future formula must explain. The left side is a martingale, while the right side would not have constant expectation without subtracting t. Growth of the path’s square cannot all be accounted for as fair fluctuation obtained after choosing position in advance.

We also obtain control beyond the fixed-endpoint result of Chapter 26. For any deterministic partition π, let Qᵖₜ include the squared increment on the unfinished current interval. The exact identity and isometry give

\[ E\sup_{t\le T}|Q^\pi_t-t|^2\le16E\int_0^T|B_{\pi(s)}-B_s|^2ds\le16T|\pi|, \]

Here π(s) is the left endpoint of the interval. Thus square sums converge to time in the L² maximal norm, hence ucp. For a sequence with summable mesh sizes, Chebyshev and Borel–Cantelli also give almost sure uniform convergence. Dyadic grids satisfy this condition; an arbitrary refining sequence does not receive an almost sure conclusion merely from this estimate.

## 31.6 Why Approximating B Can Still Produce the Wrong Integral

Both the left step process Hᴸ and the right step process Hᴿ converge to B in L²(ds·P), since Brownian increment variance within a cell is at most the mesh. But the right step process uses a value not yet revealed before the cell ends; it is not a predictable approximation. Their sums differ precisely by the quadratic sum, and have the following two limits in L² at fixed t.

\[ \sum_i B_{t_i}\Delta_iB\longrightarrow\frac12(B_t^2-t),\qquad \sum_i B_{t_{i+1}}\Delta_iB\longrightarrow\frac12(B_t^2+t). \]

There is no contradiction. The isometry controls rules in its domain; closeness in the larger product L² space does not bring illegitimate finite sums into the same extension. The information condition is not an ethical gloss added to an existing integral. It determines which linear operator is being extended. Symmetric endpoint sums have another meaningful answer, but this does not yet establish general Stratonovich theory.

## 31.7 When Growth of Squares Is Not Deterministic Time

<a id="martingale-bracket"></a>

The ds in Brownian isometry comes from conditional variance of future increments. For a general continuous martingale that growth may depend on the path and need not have a density with respect to dt. We cannot mechanically replace ds by a guessed volatility. First find an accumulated process compensating M². We initially write M₀=0; the reduction for general square-integrable initial values is proved at the end of the companion.

Fix finite T and square-integrable M. Conditional Jensen bounds every stopped square Mτ² by \(E[M_T^2\mid\mathcal F_\tau]\); the latter is uniformly integrable, so M² is class D. Chapter 30 genuinely applies: there is a unique predictable increasing càdlàg A, starting at zero, such that M²−A is a martingale. Denote A by ⟨M⟩, the predictable bracket.

\[ M_t^2-\langle M\rangle_t\text{ is a martingale},\qquad E\langle M\rangle_T=E M_T^2. \]

This definition first solves a conditional-mean problem. It has not yet proved continuity of A or its identification with a limit of squared path increments. On a first reading, the next two sections explain how these objects meet. The [companion proof](../foundations/t-ito-bracket.md#t-ito-bounded) develops the complete bounded estimates, stopping extension and covariation arguments without exchanging omitted proofs for a shorter main line.

## 31.8 Controlling Square Sums Before General Integration Exists

First assume |M|≤c. We can still define Jᵖ by finitely summing left values of M times its increments. Conditional orthogonality gives E(\(J^\pi_T\))²≤c⁴; the square-sum identity then gives a uniform L² bound. No integral for general integrands has yet been defined.

\[ Q^\pi_t=M_t^2-2J^\pi_t,\qquad \|Q^\pi_T\|_2\le3c^2. \]

Compare two grids by finite orthogonality on their common refinement. The coefficient difference is bounded by the oscillation of M over the larger mesh δ. Cauchy–Schwarz separates the oscillation from the square sum and makes the error vanish.

\[ E|J^\pi_T-J^\eta_T|^2\le3c^2\bigl(E\omega_M(\delta)^4\bigr)^{1/2}\longrightarrow0. \]

Doob’s maximal inequality gives a continuous martingale limit J. Set Q=M²−2J to obtain continuous paths. Removing the unfinished interval from each square sum changes it by a vanishing squared oscillation and leaves an increasing function, so Q increases too. Being continuous and adapted, Q is predictable; M²−Q=2J is a martingale. Uniqueness from Chapter 30 finally gives Q=⟨M⟩. This also proves continuity of the predictable bracket rather than assuming it.

## 31.9 Pathwise Quadratic Variation and Predictable Bracket Are Proved Equal Here

<a id="quadratic-variation"></a>

For general continuous square-integrable M, stop when |M| reaches c and apply the bounded result; uniqueness makes the stopped brackets consistent. Refine the mesh first, then send c to infinity to obtain a ucp limit of square sums. For continuous local martingales, patch at bounded exit times in the same way. Denote this limit by [M], its quadratic variation.

\[ \sum_i(M_{t\wedge t_{i+1}}-M_{t\wedge t_i})^2\xrightarrow{\mathrm{ucp}}[M]_t,\qquad [M]=\langle M\rangle\quad\text{for continuous local martingales}. \]

The precise scope is arbitrary deterministic finite partition sequences with mesh tending to zero, without nesting. The companion also covers partitions with a deterministic finite number of stopping points and maximum gap tending to zero in probability. It does not cover arbitrary non-stopping partitions selected from the future path. For bounded M the proof gives L² maximal convergence; for general square-integrable M, fixed-terminal L¹ and ucp; for continuous local martingales, ucp after localization. Almost sure convergence requires a separately specified grid or summable-error subsequence.

The two symbols arise from different requirements: [M] is identified by squared changes along refined paths, whereas ⟨M⟩ is identified by conditional compensation of the squared process. Continuous martingales make the routes meet, but equality is a theorem, not a naming convention.

## 31.10 A Jump Example Prevents Treating Equality as a Definition

Return only to the compensated Poisson martingale L=N−λt established in Chapter 30, without retelling the arrival story. Independent increments give conditional second moment λ(t−s), so L²−λt is a martingale and its predictable bracket is λt. On the other hand every finite-time path has finitely many unit jumps. With sufficiently fine mesh each cell contains at most one jump; square sums retain N, while the continuous drift’s squares and cross errors vanish uniformly.

\[ [L]_t=N_t,\qquad\langle L\rangle_t=\lambda t,\qquad [L]-\langle L\rangle=L. \]

These square sums include the current interval, so a jump already observed by t is counted immediately. The error is at most 2λ|π|\(N_T\)+λ²T|π|, tending to zero pathwise. Counting only complete cells would delay a jump until the next grid point and would not give the same conclusion in uniform distance. The new test distinguishes realized squared changes from their prior mean accumulation; general jump integration remains the responsibility of Chapter 34.

## 31.11 Replacing dt by a Random Clock Whose Existence Is Proved

Now A=⟨M⟩ is a continuous increasing process. Square integrability of predictable H should be measured against A rather than dt. For finite T and square-integrable M, define the finite measure m_M on predictable space. Conditional variance may accumulate at different rates on different intervals, even without a dt density.

\[ m_M(E)=E\int_0^T\mathbf1_E(\omega,s)\,dA_s,\qquad \|H\|_{M,T}^2=E\int_0^T H_s^2\,dA_s. \]

Define the same finite increment sums for elementary rules. Since M²−A is a martingale, conditional averaging replaces each squared increment by the increment of A; cross-interval orthogonality still holds. Therefore,

\[ E\left(\int_0^T H_s\,dM_s\right)^2=E\int_0^T H_s^2\,d\langle M\rangle_s. \]

Density of predictable rectangles in \(L^2(m_M)\), the isometry and Doob’s estimate give the complete extension into continuous square-integrable martingales. Density for a random measure must not silently assume a product measure; the [full proof](../foundations/t-ito-bracket.md#t-ito-clock-integral) uses finiteness of m_M itself and the generators of P. The Brownian case A=t is exactly the earlier construction, and the integrals agree by agreement on elementary rules.

This clock distinction has a concrete example. Take standard Cantor probability ν, supported on a length-zero set C with ν(C)=1. Its continuous distribution function c(t)=ν([0,t]) is a clock without a dt density. The deterministic time change Mₜ=\(B_{c(t)}\) is a continuous square-integrable martingale, and conditional increment variance directly proves ⟨M⟩=c. The [full construction](../foundations/t-ito-bracket.md#t-ito-singular-clock) uses only the set and independent-sequence tools already available in Chapters 5 and 8, not a future random-time-change theorem.

Thus deterministic predictable H=\(\mathbf1_C\) equals zero dt-almost everywhere, but not dc-almost everywhere: its energy is one and H·M is M, not zero. A null set of ordinary time can carry all quadratic growth. Equivalence classes for general integration must therefore be chosen using the established bracket clock.

## 31.12 How Integration Reweights Growth of Squares

For I=H·M, multiplying increments by \(H_i\) on one interval multiplies squared changes by \(H_i^2\). Expand interval by interval for elementary H, and use conditional compensation by M²−A to show that I²−∫H²dA is a martingale. Uniqueness from Chapter 30 identifies the integral’s predictable bracket.

\[ \langle H\mathbin{\cdot}M\rangle_t=\int_0^t H_s^2\,d\langle M\rangle_s,\qquad [H\mathbin{\cdot}M]=\langle H\mathbin{\cdot}M\rangle. \]

Passing from elementary to general H needs stability. A covariation Cauchy–Schwarz bound controls changes of the integral martingales’ brackets, while energy L² convergence controls integration of the squared functions on the right. Both sides can therefore pass to limits. The [bracket transformation proof](../foundations/t-ito-bracket.md#t-ito-transform) gives the estimates. The formula must not first be assumed as a definition and then used backward to prove existence of the integral.

## 31.13 What Two Motions Leave Together

<a id="ito-covariation"></a>

Separate squared changes cannot determine the joint contribution of two noises acting together. For continuous local martingales M,N, define [M,N] through cross-increment sums on common grids. Polarization of square sums gives existence, and bilinearity of finite cross sums passes to the ucp limit.

\[ [M,N]=\frac14([M+N]-[M-N])=\langle M,N\rangle,\qquad MN-\langle M,N\rangle\text{ is a local martingale}. \]

Covariation can have either sign and is not an increasing process. It has locally finite variation, however, and MN−⟨M,N⟩ is a genuine martingale for square-integrable M,N. The companion obtains interval Cauchy–Schwarz from nonnegative increments of ⟨M+aN⟩ and then a pathwise total-variation bound. This makes the mixed integral formula legitimate:

\[ \langle H\mathbin{\cdot}M,K\mathbin{\cdot}N\rangle_t=\int_0^t H_sK_s\,d\langle M,N\rangle_s. \]

Products of independent Brownian coordinates are martingales, so their cross brackets vanish while each individual bracket is t. Independence does not make the pathwise product zero. The coordinates still fluctuate together in time; what vanishes is the limiting accumulated cross-increment sum.

## 31.14 Stopping at a Random Time Must Preserve the Same Accumulation

<a id="ito-localization"></a>

Before localizing we must prove the stopping identity. Finite sums verify it for finite-grid stopping times. For arbitrary τ, approximate by grid stopping times from the right and use continuity of the integral and its energy isometry to obtain

\[ (H\mathbin{\cdot}M)_{t\wedge\tau}=\bigl(H\mathbf1_{(0,\tau]}\mathbin{\cdot}M\bigr)_t,\qquad\langle M^\tau\rangle=\langle M\rangle^\tau. \]

The bracket identity comes from Doob–Meyer uniqueness, so using the stopped integrator gives the same process. The [stopping proof](../foundations/t-ito-bracket.md#t-ito-stopping) supplies the full consistency argument.

Now let M be a continuous local martingale and H predictable, with ∫H²d⟨M⟩ finite almost surely on every finite T. Stop when |M| or accumulated energy first reaches n, and cap time at n; continuity prevents overshoot. After stopping expected energy is finite, so L² theory constructs each integral. The stopping identity makes them agree on overlaps, producing a continuous local martingale. Almost sure finiteness has not simply been substituted into a theorem requiring finite expectation.

## 31.15 Two Integrability Conditions Cannot Share an Unqualified “Finite”

Let Z be known initially, independent of B, finite almost surely but with E|Z|=∞, and take Hₛ=Z. Pathwise energy Z²T is finite on each finite interval, and the local integral is ZB. Yet for t>0, E|ZBₜ|=∞; it is not even integrable, so is not a genuine martingale. Local square energy permits a local construction, whereas finite expected energy gives the earlier square-integrable martingale conclusion.

An explicit localization stops at zero on {|Z|>n} and at time n otherwise. For every path with finite Z, the stopping times eventually tend to infinity. Adding independent Z to initial information preserves the Brownian property relative to the filtration; the same reason would not apply to a Z depending on future B.

Another boundary is infinite energy at an endpoint. Take deterministic Hₛ=(T−s)⁻¹ᐟ² for s<T. For every t<T the integral exists and is Gaussian with variance log(T/(T−t)), by deterministic elementary approximation, Gaussian characteristic functions and isometry. The diverging variance makes the probability of any fixed bounded interval tend to zero, excluding a finite limit in probability at T. Local existence does not authorize crossing an energy-explosion endpoint.

## 31.16 Total and Quadratic Variation Measure Different Structures

If a continuous local martingale also has locally finite total variation, its square sums are bounded by the largest increment times total variation and tend to zero pathwise. Their proved ucp limit is [M], so [M]=0. After bounded stopping, E Mₜ²=E[M]ₜ=0, making a process starting at zero identically zero. This is a continuous-case result; deleting continuity would incorrectly rule out the compensated Poisson martingale in 31.10.

Adding a continuous adapted finite-variation process V to a continuous martingale leaves quadratic variation unchanged. The square sums of V vanish, and finite Cauchy–Schwarz bounds the mixed sums, which vanish ucp too. Linear accumulation and second-order fluctuation are thus distinguished rather than canceled. This mechanism supplies mathematics needed for nonlinear changes of variables; it is not borrowed from a future formula.

## 31.17 An Integral Retaining Temporal Order and Second-Order Change

The opening left sums did not approach the half-square suggested by ordinary calculus. We now know that the difference comes from genuinely surviving squared changes. Left endpoints are not an arbitrary notation choice either: coefficients are determined before increments, so conditional orthogonality can extend finite sums into a stable continuous martingale.

For general continuous martingales, conditional compensation and path refinement identify the same random clock. It specifies the quantity controlling accumulation errors, why square integrability of rules is not always governed by ordinary time, and how changing a rule reweights growth of squares. We have not supplied an imaginary velocity to each rough path. We have built an integral depending jointly on path changes, probabilistic averaging and the order of information.

This also limits the conclusions. Equality of the two brackets for continuous processes does not erase the difference between realized and prior-average variation at jumps. Nor do L² or ucp limits automatically become pathwise limits on arbitrary grids. The change in understanding is not that stochastic integration has a magical rule. Evaluation times, second-order terms and modes of convergence, once discarded together, must now all be part of calculation.

What will a first-order approximation miss when the same motion is put through a nonlinear function? The square function has already left the evidence t. We need to explain how that contribution changes with the function, rather than dismiss every second-order term as error.

### Sources and Scope of Proof

Itô’s Stochastic Integral appeared in 1944; see the [journal archive](https://www.jstage.jst.go.jp/article/pjab1912/20/8/20_8_519/_article/-char/ja/) and the English works list maintained by the [Mathematical Society of Japan](https://math.or.jp/meeting/ito100/works.html). We use modern filtrations, predictable domains and Hilbert extensions, not a claimed stepwise reenactment of the original paper. Continuous-martingale arguments can be checked against [Tehranchi’s author notes](https://www.statslab.cam.ac.uk/~mike/StoCal/notes.pdf); the chapter and companion actually supply the estimates and limits used, rather than replacing proofs with external references.

The proved scope is predictable square-energy integration for Brownian motion and continuous (local) martingales, their brackets, covariation, stopping and localization, together with the finite-variation calculation distinguishing Poisson brackets. Full Itô formula, SDEs, general jump semimartingales and the full BDG range are not automatically obtained here. General measurable projection, section and début are not hidden prerequisites.
