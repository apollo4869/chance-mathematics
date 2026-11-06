# T-FELLER-BOUNDARIES: Accessibility, Entrance and Boundary Rules

A companion to [Chapter 36](../chapters/36-scale-speed.md#diffusion-access). Use the nondegenerate locally Lipschitz one-dimensional SDE and the compact hitting and occupation formulas proved in T-SCALE-SPEED. Local strong Markov follows from Chapter 35’s globally cutoff equations before compact exit and then by countable exhaustion. All regular-boundary extensions and singular-speed time changes are not constructed here; Chapter 37 continues those tasks.

## 1. Finite-Time Exit, a Volterra Solution and Feller’s Test

<a id="boundary-access"></a>

First verify that finite lifetime implies a limit at an endpoint, not infinitely many crossings of two interior points. For compact interior a<b and a slightly larger compact interval, the stopped SDE’s second maximal estimate bounds the chance of crossing from a to b within δ by Cδ/(b−a)². Choose δ to make this less than 1/2; reverse crossings have the same bound. Exiting the larger interval already requires the necessary displacement, so the bound still applies. Strong Markov makes each alternating crossing take at least δ with probability at least 1/2, hence its conditional negative-exponential factor is ≤q=(1+e⁻δ)/2<1. The negative-exponential expectation of n crossing times is ≤qⁿ. Infinitely many crossings therefore cannot accumulate at finite time.

If finite ζ had no endpoint limit, a continuous path would either remain eventually in a compact interval, contradicting Chapter 35’s extendibility, or cross two rational interior levels infinitely often, excluded above. Thus Xₜ tends to ℓ or r at finite lifetime, in the extended-real topology. Right accessibility means Pₓ(ζ<\(\tau_c\),ζ<∞,X_ζ−=r)>0 for some x>c. Its truth is independent of c,x by compact hitting probabilities and strong Markov connections.

\[ \Sigma_r=\int_c^r m((c,y))p(y)dy,\qquad \Sigma_r(x)=\int_c^x m((c,y))p(y)dy. \]

If S(r)=∞, positivity of m((c,y₀)) forces Σ=∞. Finite Σ implies finite S(r), and Tonelli gives Σ=∫_cʳ(S(r)−S(y))m(dy). For c<x<b↑r, \(\tau_c\wedge\tau_b\) increase. Their Green expectations are uniformly bounded: the part y≤x is compactly integrable, while \(G_{c,b}\)(x,y)≤S(r)−S(y) for y≥x. Thus their limiting exit time τ* is finite almost surely.

The events {\(\tau_b<\tau_c\)} decrease with b, with probability tending to (S(x)−S(c))/(S(r)−S(c))>0. On their intersection the endpoint-limit lemma, or the bounded scale-martingale limit, identifies exit at r rather than c. Finite Σ therefore gives positive probability of finite-time arrival, not merely finite expected exit with an unjustified choice of direction.

For the converse, divergent expectation is insufficient. Solve Lv=λv with v(c)=1,v′(c)=0 by local linear ODE theory. Its integral equation is below. The solution stays positive and nondecreasing: while v>0, v′/p=λ∫_cˣv dm≥0, so it cannot first fall below one.

\[ v(x)=1+\lambda\int_c^x(S(x)-S(y))v(y)m(dy),\quad v(x)\ge1+\lambda\Sigma_r(x),\quad \frac{v^\prime(x)}{v(x)}\le\lambda p(x)m((c,x)). \]

The last bound gives v(x)≤exp(λ\(\Sigma_r\)(x)). Thus v stays bounded at r for finite Σ and diverges for infinite Σ. Stopped at t∧\(\tau_c\wedge\tau_b\), e⁻λᵗv(Xₜ) has zero Itô drift and bounded compact coefficients, hence is a true martingale. On \(\tau_b\le T\),\(\tau_b<\tau_c\) its stopped value is at least e⁻λᵀv(b); positivity yields the chapter’s probability bound. If Σ is infinite let b↑r and take integer T to exclude all finite-time arrivals. Apply the same proof to −X at the left endpoint.

Changing c adds finite compact integrals and a finite constant times a scale tail. An infinite scale tail already made Σ infinite; a finite one cannot alter finiteness. For N, finiteness first implies finite speed tail, so adding a constant is harmless. Accessibility’s probabilistic definition provides another check of reference independence.

## 2. Entrance at an Inaccessible Endpoint: Construction and Necessity

<a id="boundary-entrance"></a>

Fix an inaccessible right endpoint, \(\Sigma_r\)=∞, and absorb at c after reaching it. An entrance starts at the extended endpoint r, is continuous in the order compactification [c,r], is strictly below r at every positive time before hitting c, and follows the original strong Markov law inside. Permanently staying at r is not an entrance. Such a continuous instantaneous entrance exists and is unique in law exactly when \(N_r\)=∫_cʳ(S(y)−S(c))m(dy)<∞.

Finite N implies finite speed tail. If S(r) were finite too, Σ≤(S(r)−S(c))m((c,r)) would be finite, a contradiction. Thus S(r)=∞. The one-sided Green formula gives the following bound for every a>c and x≥a. \(N_r(a)\) tends to zero as a↑r, dominated by the integrable tail of the original N.

\[ E_x\tau_a=\int_a^x(S(y)-S(a))m(dy)+(S(x)-S(a))m((x,r))\le N_r(a):=\int_a^r(S(y)-S(a))m(dy)\downarrow0. \]

Solve from xₙ↑r on one Brownian space, stopping at c. Path order for identical coefficients follows from local pathwise uniqueness in Chapter 35: continuous paths must meet before exchanging order, and uniqueness after the meeting identifies their continuations. Absorption at c preserves the order. Thus Xⁿ increases at each time. Finiteness and continuity of its limit still need proof.

\[ \sup_nP\!\left(\sup_{\delta\le t\le T}X_t^n\ge b\right)\le\frac{2N_r(a)}{\delta}+\frac{S(a)-S(c)}{S(b)-S(c)},\qquad c<a<b<r,\quad 0<\delta<T. \]

For starting states above a, wait for a; Markov’s inequality bounds P(\(\tau_a>\delta/2\)) by 2\(N_r(a)\)/δ. After reaching a, strong Markov and the hitting formula bound any later b-hit by the second term. Lower initial states are dominated by the process from a. First choose a near r to reduce the first term, then b near r to reduce the second. Positive-time paths cannot retain positive mass at r.

On [δ,T], stopping in [c,b] bounds coefficients uniformly and the continuous-martingale fourth-moment bound gives E|Xₜ−Xₛ|⁴≤C|t−s|². Remove the event of already exceeding b at δ using the preceding probability bound, then apply the stopped estimate on \(\mathcal F_\delta\) events. This gives tightness in C([δ,T]). Monotone limits at rational times are finite, and every continuous weak limit has those rational-coordinate laws, yielding a unique continuous version Z. Reconstruction uses only countably many rational coordinates: check the countable rational-grid uniform-continuity conditions on each rational compact window and extend the rational values continuously. These conditions have probability one under the coordinate law of the continuous weak limit, hence also for the original rational limits, giving a measurable reconstruction of Z.

The continuous law must be realized on the common space. Rational coordinates of Z are the original monotone limits. Tightness makes every subsequential limit of (Xⁿ,Z) diagonal, since rational differences vanish in probability. Hence ||Xⁿ−Z||_[δ,T]→0 in probability. A summable subsequence converges uniformly almost surely; monotonicity and Dini then give uniform convergence of the full sequence on that compact interval. Rational δ and integer T give one common null set and a continuous adapted Z at positive times.

After δ and until leaving any interior compact interval, local stability and isometry pass the SDE to Z. Restrict finite initial values \(X^n_\delta\)→\(Z_\delta\) to bounded \(\mathcal F_\delta\) events first. When Z reaches c all lower Xⁿ are already absorbed there. For a>c choose a′>a. Order makes the r-started first-a time at least the a′-started one, strictly positive almost surely. Thus Z leaves r continuously in the order topology at time zero. Hitting times must also pass to the limit: \(\tau_a^{x_n}\) increase, have means bounded by \(N_r(a)\), and tend to a finite L>0, using the lower bound from a′. Uniform convergence on positive-time windows and Xⁿ equals a at its corresponding hitting time give \(Z_L\)=a; order gives \(\tau_a^{x_n}\)≤\(\tau_a^Z\), hence L=\(\tau_a^Z\). MCT retains the mean bound, tending to zero as a↑r. After c, Chapter 35 restarts the original equation from the interior state c, extending the entrance through I until its other-endpoint lifetime. At positive stopping times strong Markov follows from the interior equation and uniqueness, completing the construction.

For any other entrance, first-a times tend to zero as a↑r, and the subsequent law is the unique interior law from a. Strong Markov and DCT for bounded continuous cylinders at positive times force expectations to equal \(\lim_{a\uparrow r}E_aF\). The entrance law is unique without guessing an additional boundary distribution.

For necessity put u(x)=\(E_x\)[e⁻λ\(\tau_c\);\(\tau_c<\infty\)]. It is positive, bounded by one and nonincreasing by same-noise path order. To prove local C² regularity, solve Lu=λu on compact (α,β) with the expectation’s endpoint values. The linear boundary-value problem has a unique solution: a zero-boundary solution vanishes by the maximum principle. Stopped Itô gives the same discounted-exit representation, which the expectation satisfies by strong Markov. Thus they agree.

If an entrance exists, strong Markov at first a gives u(r)=u(a)E_r e⁻λ\(\tau_a\). Continuous instantaneous entry makes \(\tau_a\)↓0, so d=lim_{a↑r}u(a)=u(r)>0. Positivity follows by conditioning at a positive time and positive interior chance of hitting c. Put w=u′/p≤0, so w′=λum′. If S(r)<∞, d>0 forces finite speed tail, otherwise w eventually becomes positive. This would make Σ finite, a contradiction. Thus S(r)=∞.

\[ w(r-)=0,\quad -w(x)=\lambda\int_x^r u(y)m(dy),\quad 1-d=\lambda\int_c^r(S(y)-S(c))u(y)m(dy)\ge\lambda dN_r. \]

The increasing w cannot have a strictly negative limit, which would make u negative along infinite scale; its limit is zero. Tonelli gives the final identity and finite N. This closes necessity; the left case is symmetric. All extension and entrance-equivalence theorems for accessible regular/exit endpoints do not follow automatically and remain with Chapter 37. The inaccessible-endpoint criterion has been proved here.

## 3. Computing Four Types and the Explosion Counterexample

<a id="boundary-examples"></a>

At a finite Brownian endpoint p=1,m′=2 make both quadratic integrals finite, giving regularity. For dZ=2√Z dW at zero, p=1,m′=1/(2x); Σ₀=c/2 is finite while N₀=∞, giving exit. Extend the coefficient as 2√|x|. Chapter 35’s modulus criterion makes the zero-started solution uniquely zero, so this SDE cannot enter the positive half-line from zero.

For the three-dimensional radius R=|B| from zero, Bδ≠0 almost surely for every δ>0. Chapter 33 proved nonhitting of the origin from nonzero states using harmonic 1/|x|. Condition on Bδ and take rational δ to obtain Rₜ>0 for all t>0. Also E(1/Rₛ)=C/√s: the three-dimensional Gaussian radial density behaves as a constant times r² at zero, giving a finite integral. Hence E∫₀ᵀRₛ⁻¹ds<∞.

Apply Itô to |x| after δ, localized away from zero, giving dR=(B/R)·dB+R⁻¹dt. Let δ↓0; the drift passes by the preceding integrability and Tonelli/DCT, and the martingale by L² isometry. The process β=∫₀ᵗ(Bₛ/Rₛ)·dBₛ, set to zero at R=0, has bracket t and is Brownian by Lévy. Thus the zero entrance satisfies the positive-time equation. Here p=x⁻²,S=−1/x,m′=2x²; Σ₀=∞ and N₀=c²/3<∞, verifying entrance.

For driftless geometric Brownian motion p=1,m′=2/x² make Σ₀=∞ and N₀=∞, giving natural. The positive explicit solution exp(Wₜ−t/2) never hits zero at finite time, while the globally Lipschitz equation from zero has only the zero solution. More generally Bessel drift (δ−1)/(2x),σ=1 gives \(p=x^{1-\delta}\),\(m^\prime=2x^{\delta-1}\); power integrals classify zero as exit for δ≤0, regular for 0<δ<2 and entrance for δ≥2. This does not construct every extension at the singular boundary.

For the two x²-drift examples use irrelevant positive normalization constants. With σ=x, p=e⁻²ˣ,m′=2e²ˣ/x² and S(∞)−S(x)=e⁻²ˣ/2, so the Σ∞ tail is ∫x⁻²dx<∞ and explosion before an interior c has positive probability. With σ=x², p=e²ᐟˣ gives infinite scale at infinity; ∫₀ᶜe²ᐟˣdx=∞ by u=1/x gives negative infinite scale at zero. Both endpoints are inaccessible, so the maximal solution remains in (0,∞) for all time. The coefficients are locally Lipschitz there; nonexplosion was not assumed from a global growth theorem inapplicable to superlinear coefficients.

## 4. Different Boundary Processes with the Same Interior Operator

<a id="boundary-rules"></a>

Let Y=x+B,x≥0 and τ₀ be its first zero. The absorbing process is \(A_t=Y_{t\wedge\tau_0}\); the killed process enters a separate cemetery at τ₀. Both have interior generator ½f″, but the retained-endpoint absorbing model stays at zero. Reflection R=|x+B| has a folded Gaussian kernel integrating to one. Brownian sign symmetry makes every conditional future absolute-value finite-dimensional law depend on |Yₛ| alone.

Stopping times for R are stopping times for Y since its natural filtration is contained in Y’s. Brownian strong Markov and sign symmetry of the entire future increment path give strong Markov for R, not merely deterministic-time Markov. From zero it immediately has a half-normal distribution, unlike absorption. Stopped Brownian strong Markov likewise handles absorption and killing.

For f∈C²([0,∞)) with f,f″ vanishing at infinity and f′(0)=0, the even extension F(z)=f(|z|) is C². A fixed-length Taylor difference quotient bounds f′ using f and f″, so the Itô martingale is integrable on finite horizons. Taking expectations gives Pₜ^{ref}f−f=½∫₀ᵗPₛ^{ref}f″ds. Folded Gaussian kernels preserve C₀ and are strongly continuous: |Rₜ−x|≤|Bₜ|, and C₀ functions are uniformly continuous; combine small increments with Gaussian tails. Divide by t in C₀ norm to obtain Af=½f″. Thus Neumann is an actual domain condition.

The killed semigroup acts on C₀((0,∞)); continuous tests vanish at zero, giving Dirichlet. Interior compactly supported C² functions, for example, lie in its generator domain. The absorbing semigroup acts on C₀([0,∞)) with Af(0)=0. For the corresponding C² functions with f″(0)=0, stopped Itô and strong continuity give ½f″ inside and zero at the endpoint. These are verified domain subclasses and boundary requirements, not a classification of all three maximal generator domains.

General extensions at accessible regular/exit endpoints, sticky or elastic boundaries and singular speed atoms require local time and fuller operator-domain theory. They remain with Chapter 37 and related companions under the approved division. Return to the [chapter’s boundary classification](../chapters/36-scale-speed.md#diffusion-boundary-table).
