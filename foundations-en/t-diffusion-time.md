# T-DIFFUSION-TIME: Singular Speed, Boundary Clocks and the Proved Revuz Scope

Companion to [Chapter 37](../chapters/37-local-time.md#local-speed-clock). Local time follows T-LOCAL-TIME and speed follows Chapter 36’s \(L=D_mD_S\), requiring a factor ½ in the clock. First treat continuous regular diffusions without interior killing on an open interval, then continuous local rules at finite regular endpoints. Boundary jump-in processes are excluded. The full PCAF/Revuz correspondence for general right processes remains T-REVUZ in Chapter 38.

## 1. Constructing Every Full-Support Radon Speed

<a id="time-proof-construction"></a>

Take an open interval J and a Radon measure m charging every nonempty open subinterval. Start Brownian motion at x∈J, stop at its first exit H, and stop local times there. The displayed clock is finite and continuous before H: path ranges are compact, local time is bounded continuous, and m is locally finite. If u<v<H, ∫(Lᵃᵥ−Lᵃᵤ)da=v−u>0. The integrand is continuous nonnegative and positive on an open set, so full support gives Aᵥ>Aᵤ. Its inverse T is continuous and Y has continuous paths up to lifetime \(A_H\).

\[ A_s=\frac12\int_JL_{s\wedge H}^y(B)m(dy),\qquad T_t=\inf\{s:A_s>t\},\qquad Y_t=B_{T_t},\quad t<A_H. \]

Each Tₜ is a Brownian stopping time since {Tₜ<s}={Aₛ>t}. Additivity gives \(A_{T_t+s}-A_{T_t}=A_s\circ\theta_{T_t}\), hence \(T_{t+u}=T_t+T_u\circ\theta_{T_t}\). Brownian strong Markov gives Markov behavior. For a Y-stopping time S, \(T_S\) is a Brownian stopping time: verify this for upper dyadic approximations and pass through right-continuous filtrations. The same identity gives strong Markov. Locally bounded stopped-Brownian sampling makes Y a natural-scale continuous local martingale with bracket T.

\[ \int_0^tf(Y_u)du=\frac12\int_Jf(y)L_{T_t}^y(B)m(dy),\qquad E_x\int_0^{\tau_{a,b}(Y)}f(Y_u)du=\int_a^bG^{S=\mathrm{id}}_{a,b}(x,y)f(y)m(dy). \]

The first formula uses Stieltjes time substitution du=dAₛ, Tonelli and support of dLᵞ on {B=y}. For the second, Brownian local-time expectation before hitting a or b is 2G, by Chapter 36 Green and continuous occupation density. Alternatively stopped Tanaka gives E Lᵞ=E|B at exit−y|−|x−y|=2G for every y; finite mean exit makes its martingale integrable. Thus the speed is exactly m. Hitting probabilities retain distance ratios because the strictly increasing clock preserves level order.

The construction permits singular speed without a Lebesgue density. Initial-state continuity is also checkable: couple Bˣ=x+W, whose local time is \(L_s^{y-x}\)(W). Before a common compact stop, joint continuity and local finiteness of m make clocks converge locally uniformly with x; inverses of strictly increasing clocks also converge uniformly. Brownian first hitting is almost surely continuous at each fixed interior exit level. Stopped path laws therefore vary continuously with the initial state. Continuous paths and compact covers give the local Feller property, first on killed compact intervals without imposing unjustified C₀ conditions at infinity.

## 2. Recovering the SDE and the Converse Representation

<a id="time-proof-converse"></a>

For continuous positive density m′=2/α², occupation gives Aₛ=∫₀ˢα(Bᵤ)⁻²du and ordinary inverse substitution gives Tₜ=∫₀ᵗα(Yᵤ)²du. The integral W=∫α(Y)⁻¹dY has bracket t and is Brownian; associativity gives dY=α(Y)dW. For Chapter 36 use Y=S(X), α(y)=p(S⁻¹y)σ(S⁻¹y), then Itô for S⁻¹ recovers b,σ with m′=2/(σ²p).

The exact converse class consists of a continuous strong Markov process with no interior killing and finite mean compact-subinterval exit times, in a chosen natural scale: upper hitting probabilities are (x−a)/(b−a). Chapter 36 supplies that scale through S, and the preceding construction has it as well. An arbitrary Markov process with no specified scale is not silently included.

On (a,b), X stopped at exit equals the conditional mean of its terminal value and is a bounded martingale. Exhaustion gives a continuous local martingale. Put u(x)=Eₓ\(\tau_{a,b}\). For c<x<d inside, strong Markov gives u(x) minus the chord between u(c),u(d) equal to Eₓ\(\tau_{c,d}\)>0. Thus u is finite concave. Its right derivative is decreasing and defines Radon m=−du′. Potential functions on different larger intervals differ affinely on common interior intervals, so these measures agree. No open subinterval has zero mass, since that would give zero mean exit time.

Generalized Itô for this concave u follows directly from Tanaka. On each smaller compact interval write u as an affine function minus ½∫|x−y|m(dy). Their right derivatives have the same Stieltjes derivative −m, so their difference is affine; integrating the right derivative also verifies the representation. Integrate Tanaka, using ordinary Fubini and local finite-mass isometry/localization for the stochastic term. Then u(X) minus its martingale term equals −½∫L_Xᵞm(dy).

Meanwhile strong Markov and integrability of \(\tau_{a,b}\) make stopped u(X) plus elapsed time a closed martingale. Subtracting gives a continuous finite-variation local martingale, hence zero: t=½∫Lₜᵞ(X)m(dy). Chapter 33 DDS gives X=B_[X]; occupation and continuity identify Lₜᵞ(X)=L_[X]ₜᵞ(B). Therefore A_[X]ₜ=t, the inverse clock of the construction. Speed uniqueness follows from −du′, and Brownian motion plus its measurable clock determines the process law.

## 3. Atomic Speed and Genuine Stickiness

<a id="time-proof-sticky"></a>

Start with half-line reflection R=x+β+K≥0, K increasing only at zero, constructed by Skorokhod’s lemma and equal in law to Chapter 36’s |x+B|. Interior local times tend to 2K as a↓0, so set \(L_R^{0,+}\)=2K. Add θδ₀ to interior speed 2dy, θ≥0. The clock and time-changed process are

\[ A_s=s+\theta K_s,\quad Y_t=R_{T_t},\quad t=T_t+\theta K_{T_t},\quad \int_0^t\mathbf1_{\{Y_u=0\}}du=\theta K_{T_t}. \]

The last identity uses du=ds+θdK and zero ordinary time on R’s zero set. For θ>0 the boundary has positive ordinary occupation. This is not an independent exponential holding interval at zero: A is strictly increasing and T continuous, with no such finite flat waits. A contact set negligible for ds acquires time weight. θ=0 is instantaneous reflection. General interior Radon speed permits the same finite boundary atom, with A=½∫_{(0,b)}L_R m+θK.

Before an interior upper level b, a regular zero endpoint has finite m((0,b)) and finite scale length b. Green expectations make the pre-zero time vanish as x↓0, and the chance of reaching a fixed ε first is at most x/ε. Thus stopped path laws approach the zero-started construction continuously; with interior clock continuity this gives the finite-interval Feller property. Natural or exit boundaries have not been arbitrarily turned into reflecting entrances.

## 4. Scope and Identification of Continuous Local Boundary Rules

<a id="time-proof-boundaries"></a>

At finite natural-scale endpoint zero, localized before upper level b, consider Feller strong Markov extensions with continuous paths and no interior killing. Zero may be killed immediately or trapped; otherwise it can enter the interior. The boundary regeneration below starts at X₀=0; from inside, first hit zero under the already determined interior law. Continuity is meant before lifetime, with death entering a cemetery. Its continuous local rule is determined by boundary-time parameter θ≥0 and local-time killing rate κ≥0: add the preceding clock, then kill when K first exceeds an independent Exp(κ) threshold, with κ=0 meaning no killing. The following necessity argument makes this more than a list of models.

Set the cemetery coordinate to zero and absorb at b. The coordinate in [0,b] is a bounded submartingale: before hitting 0 or b it is a natural-scale martingale; afterward its expected coordinate is nonnegative from zero and equals b from b. Strong Markov decomposition gives the conditional inequality. Chapter 30 Doob–Meyer gives X=M+K, with K continuous increasing and supported at zero: on every interior compact interval X is already a martingale, so uniqueness makes the compensator constant there. Continuity follows because predictable compensator jumps have zero conditional mean when ΔX=0.

Positive-part Tanaka for nonnegative X and the zero single-level martingale integral give K=½\(L_X^{0,+}\). Thus K has a path-measurable additive version; additivity of the compensator is not assumed. DDS and the deterministic Skorokhod lemma represent X in its quadratic clock as reflected Brownian motion, with K its regulator; an independent Brownian motion completes any finite terminal bracket. At the inverse of each deterministic K-level l, X=0, so strong Markov restarts surviving future contacts, excursions and boundary time on the l-axis. For height≥ε marks, the local-time wait to the first mark or death is memoryless, hence exponential, independent of its type and shape. This is the half-line conditional argument of T-EXCURSIONS 2 with death as an additional mark type.

The mark rate is fixed. Let \(r_\varepsilon\) be the ε-reaching rate and κ the death rate. Stop at the first of them. The terminal K has mean 1/(\(r_\varepsilon\)+κ), while E X at termination is ε\(r_\varepsilon\)/(\(r_\varepsilon\)+κ). The stopped M is UI by |M|≤ε+K at termination, so these means agree: \(r_\varepsilon\)=1/ε. Here b is an upper localization: hitting b is a terminal interior mark of height at least b, of rate 1/b, separate from κ: for ε<b it first reaches ε, then hits b before zero with probability ε/b; multiplying by \(r_\varepsilon\)=1/ε gives 1/b. Zero-boundary death events are consistent across ε, giving the same κ. Independent thinning of finite marks makes the killing threshold independent of all surviving excursions, and the limit retains independence. Feller strong continuity at zero excludes a nontrivial instantaneous-death mixture at K=0; immediate killing is a separate Dirichlet case.

Subtract interior-excursion durations. The remaining boundary ordinary time, parametrized by K, is continuous increasing: inverse-K jumps are interior excursions during which boundary time stays constant. Strong Markov at inverse K gives independent stationary increments. Survival probabilities multiply as \(e^{-cl}\). Dividing finite-dimensional surviving subprobability kernels by that factor preserves convolution and projective consistency, giving a probability law. On every finite window it is the law conditioned on survival to that window end, hence continuous. Thus it is a continuous increasing Lévy process. Chapter 27’s continuous-part characterization makes it deterministic θl: a Gaussian part cannot be monotone, and there are no jumps. Hence boundary time is θK. If zero cannot be left at all, it is the separately listed trap. Section 2 uniquely determines internal excursion clocks; θ,κ and interior m determine the localized law.

Finite positive holding followed by departure must be excluded. If the first departure time D from zero were positive finite, D would be a stopping time with X_D=0. Strong Markov there would impose a fresh positive wait, contradicting departures arbitrarily close after D. The zero-time strong Markov zero-one law separates instantaneous departure from permanent trapping. Feller strong continuity proves that law directly: for an F₀⁺ event, Markov at ε and Pεf→f give independence from all future cylinders, hence probability zero or one. Sticky occupation is therefore not an ordinary holding interval.

For smooth interior speed, take compactly supported tests C² inside and C¹ up to zero with Lf extending continuously there. Itô multiplied by e^{−κK} verifies the generator boundary condition: the time atom contributes θAf(0)dK, the spatial term contributes f′(0)dK and killing contributes −κf(0)dK. This gives the formula below, including Neumann, Robin, sticky and combined cases. Immediate killing and trapping correspond separately to f(0)=0 and Af(0)=0. This identification concerns finite regular continuous local boundaries; jump-in boundaries, interior killing and general right processes are excluded.

\[ f^\prime(0)=\theta Af(0)+\kappa f(0). \]

## 5. How Singular Speed Inherits Boundary Tests

<a id="time-proof-feller"></a>

Use Chapter 36’s natural-scale tests Σ=∫m((c,y))dy and N=∫(y−c)m(dy), with left mirrors, for Radon speed. Green was proved here, so finite-Σ accessibility is unchanged. For necessity construct v=1+λ∫(x−y)v(y)m(dy) by local Volterra iteration. It is continuous with BV right derivative and second Stieltjes measure λv m. Generalized Itô from Section 2 makes e^{−λt}v(Yₜ) a local martingale: ½∫L v″=λ∫v(Y)dt. Chapter 36’s probability bound then excludes finite arrival when Σ is infinite.

Finite-N entrance at an inaccessible endpoint also closes without assuming a Lipschitz σ for a singular model. To couple xₙ↑r monotonically, introduce independent internal paths one by one and coalesce each new path with the first existing path it meets. Continuity prevents crossing; strong Markov preserves marginal laws, and earlier paths remain unchanged. This constructs a countable monotone coupling. Chapter 36’s Green return means and positive-time escape bounds remain valid.

For positive-time tightness, first use that bound to confine states at δ and subsequent paths to interior compacts. Section 1’s clock construction gives a continuous family of continuous-path laws over compact initial states, hence a tight family; strong Markov at δ preserves tightness under random-initial-state mixtures. Rational reconstruction, monotone subsequence uniform convergence and passage of hitting times then follow Chapter 36. Interior laws pass through continuous Feller kernels and Markov cylinder tests, rather than a nonexistent σ-SDE. Necessity again uses the generalized hitting-Laplace ODE and Tonelli, forcing finite N.

Exit endpoints must also be excluded as instantaneous starting points; necessity only at inaccessible endpoints is insufficient. Suppose a continuous local extension can enter immediately from right endpoint r. Let u(x) be its discounted first-c transform. A coalescing coupling makes u decreasing; the compact stopped generalized ODE gives u″=λu m. First-a times from r tend to zero as a↑r, and strong Markov gives d=lim u(a)=u(r)>0. Thus w=u′ is increasing and nonpositive.

If r is finite, w′=λu m and u≥d force a finite speed tail, hence finite N≤(r−c)m((c,r)). If r is infinite, w must tend to zero or u would eventually become negative. Tonelli gives 1−d=λ∫(y−c)u(y)m(dy)≥λdN, again forcing finite N. Thus exit and natural endpoints with infinite N cannot be such instantaneous entrances. Finite N with finite Σ permits reflection/stickiness at a regular boundary; finite N with infinite Σ permits the entrance constructed above.

This joins the four integral types, inaccessible-endpoint entrance and regular-endpoint continuous local rules in the declared scale–Radon-speed class. It does not cover arbitrary right processes or nonlocal boundary conditions.

## 6. The Revuz Relation Actually Proved Here

<a id="time-proof-revuz"></a>

For standard Brownian motion with reference measure dx, let μ be positive Radon and define Aᵗμ=∫Lₜᵃ μ(da). Compact path ranges and joint continuity make it finite, continuous, increasing and adapted; local-time additivity makes it a continuous additive functional. Its measure is supported on contacts with supp μ. A Lebesgue-null support may yield nonzero A even though its ordinary occupation is zero.

\[ \int_{\mathbb R}g(x)E_x\!\int_0^tf(B_s)dA_s^\mu\,dx=\int_0^t\!\int_{\mathbb R}f(a)(P_sg)(a)\mu(da)ds,\qquad \lim_{t\downarrow0}\frac1t\int g(x)E_x\!\int_0^tf(B_s)dA_s^\mu dx=\int fg\,d\mu. \]

Take continuous compactly supported f≥0 and bounded continuous g≥0. Support of dLᵃ, Tonelli and EₓdLₛᵃ=pₛ(a−x)ds prove the identity; the last equality follows from expected occupation and continuous density. Gaussian symmetry turns the x-integral into Pₛg(a). On the compact support of f, Pₛg→g with a uniform bound, and local finiteness gives DCT. Thus μ is the Revuz measure of this explicit functional and is uniquely identified by the tests fg.

In particular Lᵃ corresponds to δₐ and ordinary time ∫q(B)ds to q(a)da. Changing reference to Chapter 36’s Brownian speed 2dx doubles the left side and the Revuz measure. Reference normalization matters. We proved construction and identification for explicit Brownian functionals from Radon μ, not representation of every PCAF, exceptional-set theory or smooth measures for general right processes. Those scopes remain T-REVUZ in Chapter 38, so this section is not a proved general bijection. Return to [Revuz connections](../chapters/37-local-time.md#local-revuz).
