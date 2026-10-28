# Chapter 28: Why Does Random Motion Produce Deterministic Equations? — Semigroups, Generators and Resolvents

The next step of a single particle may be unpredictable. Yet if many particles start at the same position, the average of an observable at a later time often has a definite answer. The observable might be a temperature profile, a terminal payoff, or a smooth approximation to a region. Varying the starting position produces a new function: the expected future observation from each starting point.

For a while we follow the changing functions rather than each individual path. Evolution through two time intervals must agree with evolution through the first followed by a fresh start from the new position. Short-time changes should reveal the local motion. Recovering an entire motion from these traces requires much more information than a differential expression alone.

## 28.1 Tomorrow’s Average as a Function Today

<a id="feller-observables"></a>

Let E be the state space and Pₜ its transition kernels. For a bounded Borel function f define Tₜf. Its argument is the starting position, not time. We choose the observable; the motion transforms every such choice into a new function.

\[
T_t f(x)=\int_E f(y)P_t(x,dy)=E_x f(X_t).
\]

For an indicator this is the probability of reaching an event. General functions preserve linearity, positivity and bounds: averaging cannot make a nonnegative payoff negative or increase its largest possible value. Two distributions with equal integrals against every bounded Borel function are equal. Passing from kernels to observables loses no transition probabilities.

For a countable chain this is matrix multiplication on a column vector. For Brownian motion it is Gaussian convolution. For Chapter 27’s jump motion it is still averaging, with a displacement law accommodating continuous fluctuations and jumps. We need a language in which these are instances of the same operation.

## 28.2 Joining Time Intervals Means Composing Operators

\[
P_{s+t}(x,B)=\int_E P_t(y,B)P_s(x,dy),\qquad T_{s+t}=T_sT_t,\qquad T_0=I.
\]

Chapter 17’s Chapman–Kolmogorov equation becomes the semigroup law. First average over the last t units conditional on the intermediate state, then average over the first s units. Fubini proves the identity for nonnegative functions; decomposition proves it for bounded functions. Time homogeneity matters: calendar-dependent rules require a two-parameter evolution, not dependence solely on elapsed time.

The algebraic law does not yet say whether short times produce small changes. An instantaneous resampling rule may satisfy it while failing to approach the initial state. We must choose a function space in which a short time really gives a small change.

## 28.3 Why Not Use Every Bounded Function?

Even deterministic translation is not norm-continuous on discontinuous observables. Translating a half-line indicator by any positive distance changes its value by one somewhere. The motion is not discontinuous; the instrument has a sharp edge.

\[
T_t f(x)=f(x+t),\qquad f=\mathbf1_{[0,\infty)},\qquad \|T_t f-f\|_\infty=1\quad(t>0).
\]

Throughout E is a locally compact Polish space. We use the real Banach space C₀(E): continuous functions whose absolute value is at least any positive ε only on a compact set, with the supremum norm. Observations fade at infinity, and nonzero absolute extrema are attained. If E is compact this is C(E). Uniform Cauchy sequences have uniform continuous limits still vanishing at infinity, proving completeness.

A C₀-Feller semigroup satisfies the semigroup law, is positive and contractive, preserves C₀, and has the following strong continuity. “Strong” refers to norm convergence for each fixed function, not operator-norm convergence uniformly over the unit ball.

\[
\lim_{t\downarrow0}\|T_t f-f\|_\infty=0\qquad(f\in C_0(E)).
\]

Positivity and contraction allow mass below one, so our operator convention initially permits killing. We separately call the semigroup conservative if the corresponding kernels have mass one from every starting point. Operator norm one cannot replace this pointwise requirement.

## 28.4 From Lévy Displacements to a Feller Semigroup

Let Tₜf(x) be the expected value of f at x plus a Lévy displacement. Independent stationary increments give the semigroup law. A Euclidean C₀ function is uniformly continuous: use uniform continuity on a large compact neighborhood and small function values outside. This yields a modulus estimate.

\[
\|T_t f-f\|_\infty\le\omega_f(\delta)+2\|f\|_\infty P(|X_t|>\delta).
\]

Let time tend to zero and then δ tend to zero to get strong continuity. For fixed time, restrict the displacement to a large ball with small probability outside. As the starting position goes to infinity, f is small at all endpoints inside that ball. Thus Tₜf stays in C₀. Only Chapter 27’s process construction and stochastic continuity are used, not its attraction-domain or Wiener–Hopf classifications.

## 28.5 Why the Short-Time Rate Needs a Domain

<a id="feller-generator"></a>

Translation leaves a first derivative; Brownian averaging leaves a second derivative. Continuous functions need not have either. Requiring a generator on all of C₀ would exclude the very motions we want to understand. We must record both the rule and the observables where it makes sense.

\[
D(A)=\left\{f\in C_0(E):\lim_{h\downarrow0}\frac{T_hf-f}{h}\text{ exists in }C_0(E)\right\},\qquad Af=\lim_{h\downarrow0}\frac{T_hf-f}{h}.
\]

This is a norm limit: errors become small uniformly over starting points, and the result remains continuous and vanishes at infinity. For a domain element, the semigroup law transports the derivative at zero to every time, and left and right difference quotients give the following identity. The Riemann construction and fundamental theorem for continuous Banach-valued integrals are proved in [T-OPERATORS](../foundations/t-operators.md#t-operators-integrals).

\[
T_t f-f=\int_0^tT_sAf\,ds,\qquad \frac{d}{dt}T_tf=AT_tf=T_tAf\quad(f\in D(A)).
\]

This is a precise meaning of random averages producing deterministic equations. Domain elements give classical norm-differentiable solutions. Other initial functions receive their continuous evolution from the semigroup, and cannot simply be differentiated without proof.

## 28.6 How a Partial Operator Controls the Whole Space

The domain contains more than a few smooth toy functions. Average any f over a short time interval and shift the interval to compute its generator.

\[
f_t=\frac1t\int_0^tT_sf\,ds\in D(A),\qquad Af_t=\frac{T_tf-f}{t},\qquad f_t\longrightarrow f.
\]

Thus the domain is dense. If fₙ and Afₙ converge in norm to f and g, pass to the limit in the integral identity, divide by t, and let t decrease to zero. Then f belongs to the domain and Af=g. This closedness prevents incompatible limits of observations and rates. Closed does not mean bounded: fixed-height functions can have increasingly large slopes. We need a bounded inverse operation, not an artificial bound on A itself.

## 28.7 A Random Inspection Time and Discounted Occupation

<a id="feller-resolvent"></a>

Let the instrument read f at an independent exponential clock. At rate λ its expected reading is λRλf. Removing λ gives accumulated observations with later payoffs exponentially discounted.

\[
R_\lambda f=\int_0^\infty e^{-\lambda t}T_tf\,dt,\qquad \|R_\lambda\|\le\lambda^{-1},\qquad\lambda>0.
\]

This is the resolvent. It first appears as a Laplace transform in time, not an arbitrary algebraic trick. Contraction controls the infinite tail and positivity is retained. Apply Tₕ, change variables, separate the initial short interval and take a difference quotient to get the first inverse relation. Integrating the derivative of discounted Tₜf for a domain element gives the second; exponential decay removes the endpoint at infinity.

\[
(\lambda-A)R_\lambda f=f\quad(f\in C_0),\qquad R_\lambda(\lambda-A)f=f\quad(f\in D(A)).
\]

The resolvent range is exactly the generator domain. An evolution difficult to differentiate is recorded by a bounded inverse on every continuous observable. The exponential clock turns time evolution into a linear equation.

## 28.8 Consistency Across Discount Scales

\[
R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu,\qquad R_\lambda R_\mu=R_\mu R_\lambda,\qquad \lambda R_\lambda f\longrightarrow f\quad(\lambda\to\infty).
\]

Subtracting the inverse relations gives the first two identities. The last says that increasingly fast inspection sees the initial state: split the integral near zero and into an exponential tail, using strong continuity and contraction. See [T-OPERATORS](../foundations/t-operators.md#t-operators-resolvent) for the full calculation. The entire family is constrained; inverses cannot be chosen independently for each λ.

Smaller λ lengthens the observation time but does not ensure equilibrium. Uniform rotation on a circle oscillates forever, although discounted averages converge to the circular average. For a unit circle one has the following identity.

\[
\lambda R_\lambda f(x)=\frac{\lambda}{1-e^{-\lambda}}\int_0^1e^{-\lambda s}f(x+s)\,ds\longrightarrow\int_0^1 f(s)\,ds\quad(\lambda\downarrow0).
\]

If Tₜf already converges in norm to g, substitution u=λt and dominated convergence give λRλf→g. Rotation disproves the converse. At λ=0 undiscounted occupation may even be infinite: for one-dimensional Brownian motion and a nonzero nonnegative compactly supported observable, the Gaussian density has a lower bound of order t⁻¹ᐟ² on a fixed compact interval.

## 28.9 Reconstructing a Semigroup from Local Rules

<a id="feller-hille-yosida"></a>

Reverse direction and start with a densely defined linear operator A, without assuming a process. Probabilistic averaging requires Af(x)≤0 whenever f attains a nonnegative global maximum at x. This positive maximum principle is the local trace of contraction, but it does not guarantee solvability of the rate equation.

The probabilistic Hille–Yosida theorem proved here says: if A maps a dense linear domain of real C₀ into C₀, satisfies the positive maximum principle, and λ₀−A has dense range for some positive λ₀, then A is closable and its closure generates a unique positive strongly continuous contraction semigroup. Mass loss is initially allowed; conservativity is separate.

Simply citing a generation theorem would hide the central difficulty. Applying the maximum principle at positive and negative extrema gives estimates controlling the inverse norm and positivity. The companion proves closability and surjectivity for every positive λ step by step; we now exhibit the construction itself.

\[
\lambda\|f\|_\infty\le\|(\lambda-A)f\|_\infty,\qquad\lambda\|f^-\|_\infty\le\|((\lambda-A)f)^-\|_\infty.
\]

## 28.10 Yosida Approximation: Random Inspections Replace an Unbounded Rate

<a id="feller-yosida"></a>

\[
A_\lambda=\lambda(\lambda R_\lambda-I),\qquad S_\lambda(t)=e^{tA_\lambda}=e^{-\lambda t}\sum_{k=0}^\infty\frac{(\lambda t)^k}{k!}(\lambda R_\lambda)^k.
\]

Each inspection updates by λRλ, and its count is Poisson, making the approximation positive and contractive automatically. More frequent inspections make Aλf approach Af on the domain. Commuting resolvents give commuting bounded approximations; differentiation and integration yield a direct Cauchy bound.

\[
\sup_{0\le t\le T}\|S_\lambda(t)f-S_\mu(t)f\|_\infty\le T\|(A_\lambda-A_\mu)f\|_\infty\longrightarrow0\quad(f\in D(A)).
\]

In this construction first replace the closable candidate by its closure; A henceforth denotes that closure. Take the limit on the dense domain, then extend by contraction. Uniform convergence on compact time intervals preserves the semigroup law and strong continuity. Surjectivity of λ−A finally rules out an extra domain in the limiting generator, identifying it exactly with the closure of A. [T-OPERATORS](../foundations/t-operators.md#t-operators-generation) proves this and uniqueness without stochastic integration or a preexisting path.

## 28.11 Which Test Functions Really Determine the Generator?

<a id="feller-core"></a>

Dense tests can identify measures without identifying unbounded operators. Af must be approximated alongside f. A subspace D₀ dense in the following graph norm is called a core. Equivalently its range under λ−A is dense for one positive λ.

\[
\|f\|_A=\|f\|_\infty+\|Af\|_\infty,\qquad D_0\text{ is a core}\iff\overline{(\lambda-A)D_0}=C_0(E).
\]

To prove it, approximate (λ−A)f and apply the bounded inverse Rλ, obtaining both approximations; the converse follows from graph-norm continuity. The maximum principle alone is insufficient. On (0,1), Af=f′ on compactly supported smooth functions has its range annihilated by the following nonzero continuous functional. The range is not dense: boundary information is missing.

\[
\int_0^1e^{-\lambda x}(\lambda f(x)-f^{\prime}(x))\,dx=0\qquad(f\in C_c^\infty(0,1)).
\]

## 28.12 One Second-Order Expression, Two Processes

<a id="feller-boundaries"></a>

On [0,∞), Brownian motion may stay at zero after reaching it, or reflect there. Both have interior rate one half of the second derivative. Starting at zero, one stays put while the other spreads out. Zero is a state; stopping there differs from killing by departure. With Gaussian density gₜ of variance t and standard normal distribution function Φ, reflection gives two semigroups.

\[
\begin{aligned}T_t^r f(x)&=\int_0^\infty[g_t(y-x)+g_t(y+x)]f(y)\,dy,\\T_t^a f(x)&=\int_0^\infty[g_t(y-x)-g_t(y+x)]f(y)\,dy+2\Phi(-x/\sqrt t)f(0).\end{aligned}
\]

Absorption retaining zero gives Af(0)=0, requiring f″(0)=0 for the continuous second-derivative expression. Reflection requires f′(0)=0. These are not domains assigned by intuition: the companion computes the full resolvent ranges through Green kernels to prove these equalities, with one-sided derivatives at zero.

\[
\begin{aligned}D(A_a)&=\{f\in C_0([0,\infty))\cap C^2([0,\infty)):f^{\prime\prime}\in C_0,\ f^{\prime\prime}(0)=0\},\\D(A_r)&=\{f\in C_0([0,\infty))\cap C^2([0,\infty)):f^{\prime\prime}\in C_0,\ f^{\prime}(0)=0\}.\end{aligned}
\]

Smooth compactly supported functions constant near zero give identical operators and form a dense class in C₀, but are a core for neither. [T-FELLER-EXAMPLES](../foundations/t-feller-examples.md#t-feller-boundary-domains) shows how graph norms retain boundary information. A formal differential expression can omit the entire fate at a boundary.

## 28.13 The Lévy Triplet as a Rule on Functions

For smooth compactly supported f, Chapter 27’s Gaussian fluctuation, drift and compensated jumps give the following generator. Q is the Gaussian covariance matrix and b uses unit-ball truncation.

\[
Af(x)=b\cdot\nabla f(x)+\frac12\operatorname{tr}(Q\nabla^2 f(x))+\int_{\mathbb R^d\setminus\{0\}}[f(x+y)-f(x)-\mathbf1_{\{|y|\le1\}}y\cdot\nabla f(x)]\,\nu(dy).
\]

Subtracting the first-order term makes the small-jump remainder quadratic. Without it absolute integrability can fail, just as ordinary small-jump summation failed. The proof truncates small jumps, differentiates a finite Poisson series and Gaussian Taylor expansion, then controls semigroup differences by the coupled L² maximal bound and generator differences by the Taylor remainder. Passing the integral identity to the limit proves genuine domain membership. See [T-FELLER-EXAMPLES](../foundations/t-feller-examples.md#t-feller-levy-generator). Complex exponentials outside C₀ are not domain elements, and smooth tests are not called a core without graph approximation.

## 28.14 Recovering Probability Kernels from Operators

<a id="feller-kernels"></a>

Operator generation has not constructed a random experiment. For fixed t and x, the bounded positive functional f↦Tₜf(x) must be shown to integrate a measure. We need only Riesz representation for bounded positive C₀ functionals on locally compact Polish spaces. The companion builds discrete measures from finite partitions on compact spaces, uses Chapter 24’s tightness theorem, and then one-point compactification. No future general random-measure theory is assumed.

Increasing nonnegative C₀ approximations to open-set indicators make the resulting subprobability measures measurable in the starting point. A monotone class extends this to Borel sets. The semigroup identity and uniqueness of representation give Chapman–Kolmogorov, recovering consistent transition probabilities.

Conservativity is separate. On compact E it is equivalent to one belonging to the domain with A1=0; on noncompact E, one usually is not in C₀. A sufficient condition is a domain sequence 0≤fₙ≤1 tending pointwise to one with generator norms tending to zero. The integral identity makes Tₜfₙ−fₙ uniformly small; bounded convergence gives mass one. In contrast A=−I gives exponential killing. Chapter 22’s pure birth process with rates 2ⁿ also shows that formally zero row sums do not exclude explosion; a formal A1=0 cannot replace conservativity.

## 28.15 Finite-Dimensional Rules Still Need Regular Paths

<a id="feller-paths"></a>

Assume conservativity from here. Chapter 8 gives a coordinate process with these finite-dimensional laws, but Chapter 23 shows that finite-dimensional rules cannot exclude pathological modifications at random times. We still owe E-valued càdlàg paths on one event of probability one. Resolvents provide controllable observations: for nonnegative f and λ>0, the process \(e^{-\lambda t}R_\lambda f(X_t)\) is a supermartingale, since waiting removes a nonnegative part of occupation.

\[
e^{-\lambda s}T_sR_\lambda f=\int_s^\infty e^{-\lambda r}T_rf\,dr\le R_\lambda f.
\]

Use a countable dense nonnegative class and integer λ. Chapter 15’s crossing inequalities on finite rational grids exclude infinite oscillations, giving rational side limits at every real time simultaneously. One-point compactification supplies cluster points and separating observables make them unique. A cluster point might still be infinity: no loss at each deterministic time does not exclude escape at a random time.

## 28.16 How Conservativity Controls a Whole Path Segment

Take increasing compactly supported cutoffs χₘ tending to one and put gₘ=αRαχₘ. Conservativity makes 0≤gₘ≤1 increase pointwise to one. One minus discounted gₘ(Xq) is a nonnegative submartingale; the finite-grid maximal inequality bounds escape from a superlevel set.

\[
P_\pi\!\left(\inf_{q\in\mathbb Q\cap[0,T]}g_m(X_q)<\delta\right)\le\frac{1-e^{-\alpha T}E_\pi g_m(X_T)}{1-\delta},\qquad0<\delta<1.
\]

Choose α small and then m large to make the bound arbitrarily small. Yet {gₘ≥δ} is compact inside E. Choose compact sets with error tending to zero and take finite unions to make them increasing. Almost every rational path on all of [0,T] is contained in one of them, so every side limit remains in E.

Define the new process by rational right limits. A compatible metric built from the countable observations, with finite-coordinate and series-tail control, proves càdlàg paths. Strong continuity makes observation increments converge in second mean, proving equality with the old process almost surely at fixed times. See [T-FELLER-PATHS](../foundations/t-feller-paths.md#t-feller-regularization). The scope is conservative C₀-Feller semigroups on locally compact Polish spaces, not arbitrary weak-Feller kernels.

## 28.17 Can We Restart at a Time Chosen by the Path?

<a id="feller-strong-markov"></a>

Fix an initial law π and complete the natural filtration. Markov recursion for continuous cylinder functions and Chapter 15’s reverse conditional-expectation limit prove right continuity of this completed filtration; details are in the companion. Completion is for π, not a single implicit completion for all initial laws. For a bounded stopping time use upward dyadic approximation. An event A in the stopped σ-algebra allows deterministic Markov on each grid slice.

\[
\tau_n=2^{-n}\lceil2^n\tau\rceil\downarrow\tau,\qquad E_\pi[\mathbf1_A f(X_{\tau_n+s})]=E_\pi[\mathbf1_A T_sf(X_{\tau_n})].
\]

First take f in C₀. The left side uses right-continuous paths; the right additionally needs continuity of Tₛf, precisely where the Feller property matters. After dominated convergence, constants and a monotone class extend to bounded Borel functions. Localize unbounded τ by τ∧m, stating the result only on finite τ.

\[
E_\pi[f(X_{\tau+s})\mid\mathcal F_\tau]=T_sf(X_\tau)\quad\text{on }\{\tau<\infty\}.
\]

Recursion handles several future times and a rational-coordinate π–λ argument handles the future path. The companion also proves stopped-state measurability and open-set entrance times. Closed-set entrance cannot simply be identified with limits of open-neighborhood entrances: a jump path’s left limit alone may touch the closed set.

## 28.18 Generator Error as a Fair Game

<a id="feller-dynkin"></a>

For a domain element f, subtract the time accumulation of Af from the actual change. The remainder is not zero pathwise, but is a conditionally fair fluctuation.

\[
M_t=f(X_t)-f(X_0)-\int_0^tAf(X_s)\,ds.
\]

The Markov property gives the conditional mean of f(Xₜ), and conditional Fubini gives that of the integral. The semigroup identity cancels them, so M is a càdlàg martingale. Bounded Af justifies the integrals. For bounded stopping τ, expand on finite grids into martingale increments with past-measurable indicators, then use right continuity and a deterministic bound. This gives Dynkin’s formula without importing later general continuous-time sampling.

\[
E_xf(X_\tau)-f(x)=E_x\int_0^\tau Af(X_s)\,ds.
\]

A stopping time with finite expectation is handled by τ∧n, since the integral is bounded by its length times the norm of Af. Without such a condition the undiscounted version cannot be used arbitrarily. See the grid proof in [T-FELLER-PATHS](../foundations/t-feller-paths.md#t-feller-dynkin).

## 28.19 What Remains of the Resolvent After Stopping?

Put u=Rλf, so (λ−A)u=f. The semigroup identity directly proves a discounted martingale; summation by parts against the finite-variation exponential is another route requiring no stochastic integral. Every stopping time τ, including infinite τ, then satisfies the following formula.

\[
R_\lambda f(x)=E_x\!\left[\int_0^\tau e^{-\lambda s}f(X_s)\,ds+\mathbf1_{\{\tau<\infty\}}e^{-\lambda\tau}R_\lambda f(X_\tau)\right].
\]

Prove this first for τ∧n. An integrable exponential tail dominates the integral, and discount removes the terminal term on infinite τ. The resolvent splits into observations earned before stopping and the remaining observation restarted from the stopped state. As both a linear-equation solution and an expected path occupation, it gives boundary problems a probabilistic meaning.

## 28.20 Exactly What Does a Generator Determine?

A closed densely defined operator with its domain and generation conditions uniquely determines a strongly continuous semigroup. Positivity gives subprobability kernels, conservativity gives probability kernels, local compactness and Feller structure give an E-valued càdlàg realization, and grid approximation gives strong Markov. Each step adds different content.

“Determining a process” means determining finite-dimensional laws for every initial law and the law on the coordinate σ-algebra of càdlàg paths. It does not assert pathwise uniqueness on an arbitrary prescribed probability space. Nor does a formal operator on a few tests automatically meet generation conditions. Boundary behavior and explosion expose false uniqueness claims caused by merging these levels.

Can a process be identified merely by requiring observations minus generator accumulations to be fair? This leads later to the martingale problem. Our existence and uniqueness proof has not assumed it.

## 28.21 The Deterministic Record Left by Random Paths

A particle may jump, or move continuously and nowhere differentiably. Its average action on continuous payoffs nevertheless forms a continuous operator semigroup. The generator does not erase randomness: it records short-time averages, while the domain retains which observations reliably read that rate, especially at boundaries.

The resolvent joins local readings to an entire span of time. Exponential-clock averaging, discounted occupation and the inverse generator are different roles of the same operation. Their constraints reconstruct kernels from operators and paths from kernels, rather than relying on a formal analogy between motion and equations.

This volume asks what discrete records retain and what shared control yields a genuine path. Random geometry now also has deterministic readings. If attention turns from typical paths to exceptionally unlikely deviations of whole trajectories, weak-convergence scales are still too coarse. With path space established, the new difficulty is measuring motions that become harder to observe without becoming impossible.

### Sources and Proof Scope

Mathematical comparisons use Engel and Nagel’s [A Short Course on Operator Semigroups](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/a_short_course_on_operator_semigroups-1.pdf) and Schilling’s author notes [An Introduction to Lévy and Feller Processes](https://arxiv.org/abs/1603.00251). This is a modern reconstruction for the book’s problem sequence, not a reconstruction of the original discovery order. General growth semigroups, non-locally-compact states, general martingale problems and arbitrary nonconservative path theories are outside the proved scope.
