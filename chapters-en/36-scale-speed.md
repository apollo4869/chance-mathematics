# Chapter 36: What Determines the Fate of a One-Dimensional Diffusion? — Scale, Speed and Boundaries

A particle is continually pushed to the right. The drift arrow suggests rightward motion, yet fluctuations may first carry it to a barrier on the left. Even two models with identical left-versus-right hitting probabilities can reach a barrier in finite versus infinite time. Directional chance and the clock of motion have not yet been separated.

## 36.1 Why a Rightward Push Can Still Lead Left First

<a id="diffusion-question"></a>

Begin with dX=μdt+σdW, where μ,σ>0, from x between a and b. Which endpoint is reached first? The mean x+μt does not answer: the hitting time is random. Substituting a random time into the mean would return to the sampling conditions distinguished in Chapter 16.

Seek a position reading h with no predictable drift along the motion. Its mean reading stays unchanged before stopping. Set h(a)=0,h(b)=1: at exit it records which endpoint was reached. The hitting problem asks for a suitable coordinate, rather than a guessed time.

## 36.2 Specify the Path Being Followed

<a id="diffusion-setting"></a>

Our main setting is a time-homogeneous SDE on an open interval I=(ℓ,r), allowing infinite endpoints. Assume b,σ are locally Lipschitz in I and σ(x)>0. On compact subintervals coefficients are bounded and σ is bounded away from zero. Chapter 35 gives a maximal continuous strong solution unique up to leaving I. The filtration is usual and W is Brownian relative to it.

\[ dX_t=b(X_t)dt+\sigma(X_t)dW_t,\qquad Lf(x)=a(x)f^{\prime\prime}(x)+b(x)f^\prime(x),\qquad a=\sigma^2/2>0. \]

Define lifetime ζ as the increasing limit of compact-interval exit times. The minimal process is sent to a cemetery afterward; its interior equation holds only for t<ζ. Hitting a finite endpoint or escaping to an infinite endpoint in finite time may end lifetime. Reflection, absorption and entrance from an endpoint require additional rules; they are not implicit in the open-interval SDE.

## 36.3 Making Position a Fair Reading

<a id="diffusion-scale-discovery"></a>

For C² h, the established Itô formula gives reading drift Lh. Thus we need ah″+bh′=0. First solve for h′: its logarithmic rate of change must cancel b/a.

\[ p(x)=\exp\!\left(-\int_c^x\frac{b(z)}{a(z)}dz\right),\qquad S(x)=\int_c^xp(y)dy,\qquad LS=0,\qquad c\in I. \]

Since p>0, S preserves order. It does not remove physical drift from the original path. It chooses a reading in which the same motion is a continuous local martingale. Scale is born from a specific stopping problem: represent directional asymmetry by a nonuniform coordinate.

\[ dS(X_t)=p(X_t)\sigma(X_t)dW_t\quad(t<\zeta),\qquad \widetilde S=AS+B\ (A>0)\text{ is an equivalent scale}. \]

## 36.4 A Stopped Identity Becomes a Hitting Probability

<a id="diffusion-hitting"></a>

Fix ℓ<a<x<b<r and τ=τₐ∧τᵦ. The stopped S(X) is bounded and hence a true martingale. We must still prove τ is finite before letting time tend to infinity. [Proof 1](../foundations/t-scale-speed.md#scale-compact-exit) obtains a uniform expectation bound from a nonnegative solution of Lu=−1 without presupposing the hitting result.

\[ P_x(\tau_b<\tau_a)=\frac{S(x)-S(a)}{S(b)-S(a)},\qquad P_x(\tau_a<\tau_b)=\frac{S(b)-S(x)}{S(b)-S(a)}. \]

These are scale distances, not ordinary distances. Continuity restricts exit values to a or b, with no jump overshoot; bounded martingales and bounded convergence justify expectation. For a jump process this last step fails, so the formula cannot simply be transplanted.

## 36.5 A Constant Drift Must Be Measured against Fluctuation

<a id="diffusion-drift-example"></a>

For constant μ,σ the scale density is exp(−2μx/σ²), up to an irrelevant positive factor. Calculation gives

\[ P_x(\tau_b<\tau_a)=\frac{1-e^{-2\mu(x-a)/\sigma^2}}{1-e^{-2\mu(b-a)/\sigma^2}}\quad(\mu\ne0),\qquad P_x(\tau_a<\infty)=e^{-2\mu(x-a)/\sigma^2}\quad(\mu>0,x>a). \]

For the second formula let b tend to infinity. A path that hits a at a finite time was bounded beforehand, so it hits a before some b; the increasing events exhaust the hitting event. Rightward drift reduces rather than abolishes left hitting, through the ratio of drift to squared fluctuation. Letting μ tend to zero recovers the ordinary distance ratio.

## 36.6 The Same Directional Chances with Different Clocks

<a id="diffusion-two-structures"></a>

Multiply b and a by the same positive function q. Their ratio and every compact-interval hitting probability stay unchanged, but quadratic-variation rate changes. In particular ordinary Brownian motion and dX=X dW both have scale S(x)=x. On the positive half-line the former can hit zero while the latter never does at finite time. The same directional chances do not determine boundary timing.

We need a quantity complementary to scale. Rewriting the generator as two different derivatives produces it.

\[ m(dx)=m^\prime(x)dx,\qquad m^\prime(x)=\frac1{a(x)p(x)}=\frac2{\sigma(x)^2p(x)},\qquad L=\frac d{dm}\frac d{dS},\quad \frac{df}{dS}=\frac{f^\prime}{p}. \]

## 36.7 Why a Larger Speed Measure Means Slower Motion

<a id="diffusion-speed"></a>

The term speed measure does not mean the particle’s velocity. It is the spatial weight in the second derivative of the generator. With scale fixed, decreasing a increases m: crossing the same scale region takes more ordinary time. The occupation formula below makes that statement precise.

Our normalization gives standard Brownian motion m(dx)=2dx, not dx, because its generator is ½d²/dx². Multiplying S by A divides m by A and multiplies the Green kernel by A, leaving probabilities and time formulas unchanged. A factor of two taken from another convention without checking its generator doubles every mean time incorrectly.

## 36.8 A Broken Line Records Occupation

<a id="diffusion-green"></a>

Still stop in (a,b). If f(Xₜ) accumulates per unit time, its expected total u should satisfy Lu=−f with zero exit values. In scale coordinates, a point-source solution joins two straight segments: no curvature away from the source, and a downward unit jump in scale slope at the source.

\[ G_{a,b}(x,y)=\frac{\{S(x\wedge y)-S(a)\}\{S(b)-S(x\vee y)\}}{S(b)-S(a)},\qquad u_f(x)=\int_a^bG_{a,b}(x,y)f(y)m(dy). \]

The kernel is symmetric in x,y. Differentiating its two pieces gives a jump −1 in the scale derivative at x=y. Integrating continuous f produces a C² \(u_f\) with \(Lu_f\)=−f. Stopped Itô therefore proves, rather than merely suggests,

\[ E_x\int_0^{\tau_a\wedge\tau_b}f(X_t)dt=\int_a^bG_{a,b}(x,y)f(y)m(dy),\qquad f\ge0\text{ Borel}. \]

Prove it first for continuous f and extend by finite-measure uniqueness and monotone classes. Nonnegative f may have infinite integral. For signed f the corresponding integral of |f| must be finite before subtraction. [Proof 2](../foundations/t-scale-speed.md#scale-green) supplies endpoint, integrability and extension details.

## 36.9 Separating Where from When

<a id="diffusion-mean-exit"></a>

Setting f=1 gives mean exit time. Brownian scale x and speed 2dx yield (x−a)(b−x). If coefficients are accelerated by q while scale is unchanged, the Green kernel stays fixed but the speed measure is divided by q, changing the time contributed by each region.

\[ E_x(\tau_a\wedge\tau_b)=\int_a^bG_{a,b}(x,y)m(dy),\qquad L_{\rm BM}=\tfrac12\partial_{xx}:\ E_x\tau=(x-a)(b-x). \]

As intervals expand toward the endpoints, exit times and nonnegative occupation integrals increase. Monotone convergence gives the Green potential before lifetime, possibly infinite. Infinite endpoints must not be substituted into an indeterminate ∞/∞ quotient. Nor does infinite mean prove that paths never exit.

## 36.10 An Expected Density Is Not a Pathwise Occupation Record

<a id="diffusion-occupation"></a>

For fixed y the speed measure gives {y} mass zero. Before compact-interval exit, time spent exactly at y is therefore almost surely zero, yet the probability of hitting y can be one. Hitting a point and spending positive ordinary time there are different facts.

The Green formula describes the expectation of a random occupation measure. It has not constructed a spatial density for each path or selected local time simultaneously at all y. We first use the expected information to study boundaries, then ask what individual paths retain.

## 36.11 Approaching a Boundary Is Not Reaching It in Finite Time

<a id="diffusion-access"></a>

At the right endpoint r fix c<x<r. If S(r)=∞, the hitting formula makes the chance of reaching arbitrarily high scale before c vanish. If S(r)<∞, rightward probability can survive. We must still decide whether successive approaches to r accumulate at a finite time or extend to infinity.

\[ \Sigma_r=\int_c^r\{m((c,y))\}\,dS(y)=\int_c^r\{S(r)-S(y)\}\,m(dy)\quad\text{when }S(r)<\infty. \]

The first nonnegative iterated integral is always meaningful and is infinite if S(r)=∞. The second is used only for finite S(r), by Tonelli. Changing the interior reference point c does not change finiteness. At the left endpoint reverse the directions.

## 36.12 Why an Expectation Test Is Not Enough

<a id="diffusion-feller-test"></a>

We prove that the right endpoint is reachable at finite time before c if and only if Σᵣ is finite. Sufficiency follows by combining a Green expectation bound with scale probability. Necessity needs a stronger tool: a finite random time may have infinite mean, so divergence of a Green integral alone does not show inaccessibility.

Find a positive λ-harmonic reading v with Lv=λv,v(c)=1,v′(c)=0. Its twice-integrated equation makes v bounded when Σ is finite and divergent when Σ is infinite. Stopping e⁻λᵗv(Xₜ) provides an actual probability bound excluding finite-time arrival.

\[ v(x)=1+\lambda\int_c^x\{S(x)-S(y)\}v(y)m(dy),\qquad P_x(\tau_b\le T,\tau_b<\tau_c)\le e^{\lambda T}\frac{v(x)}{v(b)}. \]

This separates an excessively large mean time from zero probability of finite-time arrival. [Boundary proof 1](../foundations/t-feller-boundaries.md#boundary-access) proves the Volterra bound, lifetime limit and exit direction without using future general diffusion time changes.

## 36.13 Can a Boundary Be an Initial State?

<a id="diffusion-entrance"></a>

An endpoint inaccessible from inside need not be meaningless as a starting state. Three-dimensional Brownian motion from the origin has strictly positive radius immediately, whereas from a positive radius it never hits zero. The same point has different roles in the two directions.

To test entrance from the right, interchange the roles in the preceding iterated integration. The new quantity measures the clock needed to return inward from remote states, rather than to travel out from inside.

\[ N_r=\int_c^r\{S(y)-S(c)\}m(dy),\qquad N_\ell=\int_\ell^c\{S(c)-S(y)\}m(dy). \]

For an inaccessible right endpoint, Nᵣ is finite exactly when a continuous instantaneous entrance exists, formulated first with stopping at an interior c. This is more than naming an integral. [Boundary proof 2](../foundations/t-feller-boundaries.md#boundary-entrance) sends initial x toward r, constructs the entrance by monotone coupling with the same Brownian noise, and controls positive-time tightness by return-time bounds. Conversely the Laplace reading of the c-hitting time excludes infinite Nᵣ.

## 36.14 Four Boundary Types from Two Different Tests

<a id="diffusion-boundary-table"></a>

For the left endpoint use \(\Sigma_\ell=\int_\ell^c m((y,c))\,dS(y)\), the mirror of the right test. Feller’s basic classification uses finiteness of Σ and N. A regular boundary here is an endpoint type, distinct from regular diffusion meaning mutual accessibility of interior points.

|Σ|N|Type|Distinction established here|
|---|---|---|---|
|finite|finite|regular|Accessible from inside; a boundary rule still has to be chosen|
|finite|infinite|exit|Accessible from inside; the entrance test fails|
|infinite|finite|entrance|Inaccessible from inside but admits continuous instantaneous entrance|
|infinite|infinite|natural|Inaccessible and has no such continuous instantaneous entrance|

The table specifies the integral types and the accessibility and inaccessible-endpoint entrance theorems proved above. It does not construct every reflecting, sticky or killed extension at regular endpoints, or the full theory for singular speed measures. Under the blueprint those general constructions follow Chapter 37’s local time and time changes. We now construct computable representatives, distinguishing classification tests from construction of all boundary processes.

## 36.15 Seeing the Four Types in Concrete Models

<a id="diffusion-examples"></a>

Brownian motion on (0,1) has regular endpoints: p=1,m′=2 make both integrals finite. For dZ=2√Z dW on (0,∞), zero is exit: scale x and m′=1/(2x) give finite Σ and infinite N. Extending the same square-root SDE from zero gives only the zero process, by Chapter 35’s modulus uniqueness.

The three-dimensional Bessel radius solves dR=dβ+R⁻¹dt in the interior. With p=x⁻²,S=−1/x,m′=2x², zero has infinite Σ and finite N and is entrance. R=|B⁽³⁾| actually constructs the process from zero. [Boundary proof 3](../foundations/t-feller-boundaries.md#boundary-examples) checks Itô away from time zero and drift integrability near zero.

For geometric Brownian motion dX=X dW, zero is natural: p=1,m′=2/x² make both tests diverge. It may approach zero as t→∞ but never reaches it at finite time; the same SDE started at zero cannot enter the positive half-line. These are two distinct temporal statements, not a rhetorical equation of very slow with impossible.

## 36.16 Larger Noise Can Prevent Upward Explosion

<a id="diffusion-explosion-example"></a>

Compare two equations on the positive half-line, both with drift x². The deterministic equation explodes in finite time, but the two noise coefficients give different fates.

\[ dX=X^2dt+X\,dW:\quad p(x)\asymp e^{-2x},\quad m^\prime(x)\asymp e^{2x}/x^2;\qquad dY=Y^2dt+Y^2dW:\quad p(x)\asymp e^{2/x},\quad m^\prime(x)\asymp e^{-2/x}/x^4. \]

The first has finite scale at infinity and (S(∞)−S(x))m′(x) proportional to x⁻², so Σ∞ is finite: upward finite-time explosion has positive probability before a fixed interior lower level. The second has infinite scale at infinity and negative infinite scale at zero; both endpoints are inaccessible, giving infinite lifetime in the positive half-line. Neither the common drift arrow nor larger noise alone decides explosion. This compares fates, not the same-noise path-order theorem below.

## 36.17 One Interior Operator Can Have Different Boundary Futures

<a id="diffusion-boundary-rules"></a>

On the interior half-line, Brownian motion has generator ½f″. Killing at zero, absorbing at zero, and reflecting back give different processes. Stopping constructs the first two; |x+B| constructs the third. Its future law depends only on the current absolute value because Brownian increments are symmetric, so it is Markov without an advance use of Tanaka’s formula.

\[ p_t^{\rm ref}(x,y)=\frac1{\sqrt{2\pi t}}\left[e^{-(y-x)^2/(2t)}+e^{-(y+x)^2/(2t)}\right],\qquad x,y\ge0. \]

If f′(0)=0, the even extension f(|z|) is C² and Itô gives the reflecting model’s Neumann condition. Continuous killed-model tests have Dirichlet condition f(0)=0. The absorbing model has generator zero at state zero, interpreted on the state space retaining that endpoint. The interior differential expression is unchanged; its domain and boundary rule change the future. [Proof 4](../foundations/t-feller-boundaries.md#boundary-rules) verifies kernels, strong Markov and boundary calculations.

## 36.18 What a Comparison Theorem Actually Compares

<a id="diffusion-comparison"></a>

If two equations use the same Brownian motion and the same locally Lipschitz diffusion coefficient σ, with b₁≤b₂ and x₁≤x₂, then X¹≤X² before their common lifetime. With identical coefficients, continuous paths cannot exchange order without first meeting, after which uniqueness keeps them together. Different drifts require additional control of the positive difference’s second-order term.

Use the smooth absolute-value approximations established in Chapter 35 to approximate the positive part, then apply stopped Itô and Gronwall. This does not borrow Chapter 37’s Tanaka formula. [Long-term proof 1](../foundations/t-diffusion-longtime.md#diffusion-order) gives the estimates. If diffusion coefficients differ, W and 2W from zero already exchange order with the sign of W; the ordering cannot be retained.

## 36.19 From Interval Hitting to Infinite-Time Fate

<a id="diffusion-recurrence"></a>

If both endpoints of the minimal process are inaccessible, lifetime is infinite. When S(ℓ)=−∞ and S(r)=∞, sending an endpoint outward in the hitting formula shows that every interior point is eventually hit from every other. Strong Markov makes the crossings recur, yielding one-dimensional recurrence.

If both endpoint scales are finite, S(X) is a bounded martingale converging to an endpoint scale. An interior limit would trap the path in a nondegenerate compact interval, forcing infinite quadratic clock, incompatible with bounded-martingale convergence. Thus

\[ P_x(X_t\longrightarrow r)=\frac{S(x)-S(\ell)}{S(r)-S(\ell)}\qquad\text{if both scales are finite and }\zeta=\infty. \]

If only the right scale is finite and the left is −∞, convergence of the nonnegative local martingale S(r)−S(X) gives X→r almost surely; the other direction is symmetric. These statements concern the specified conservative interior process, not reflecting or killed variants. [Long-term proof 2](../foundations/t-diffusion-longtime.md#diffusion-recurrence-proof) supplies the clock argument.

## 36.20 When the Speed Measure Becomes a Stationary Probability

<a id="diffusion-invariant"></a>

When m(I) is finite and both endpoints are inaccessible, normalized m is invariant. The formal equation L*π=0 alone is not a proof. Construct discounted Green kernels on compact intervals and establish symmetry with respect to m. Exhaust the interval, use conservativity Rλ1=1/λ, and recover stationarity at every time by Laplace uniqueness.

\[ \pi(dx)=\frac{m(dx)}{m(I)},\qquad \int_I P_tf(x)\pi(dx)=\int_I f(x)\pi(dx). \]

In the recurrent case with infinite scales at both ends, any invariant probability must be π. Compactly supported tests give a constant-flux equation with solutions (C+JS(x))m(dx). Since S ranges over the real line, nonnegativity forces J=0. Thus recurrence with infinite total speed does not yield a normalizable stationary probability. [Long-term proof 3](../foundations/t-diffusion-longtime.md#diffusion-invariance-proof) treats the measure equation and uniqueness.

## 36.21 How a Path’s Long-Time Average Recovers Speed Weight

<a id="diffusion-time-average"></a>

Choose interior a<b and treat a→b→a as a complete return cycle. Strong Markov gives iid cycles. The Green formula computes outward and return rewards separately; adding them cancels the two sides of the broken line, leaving the speed measure itself.

\[ E_a\!\int_{\rm cycle}f(X_t)dt=\{S(b)-S(a)\}\int_If(y)m(dy),\qquad E_aT_{\rm cycle}=\{S(b)-S(a)\}m(I). \]

For finite m, the iid cycle law of large numbers gives time-average convergence to πf for bounded Borel f. The incomplete final cycle is controlled by integrable cycle length. [Long-term proof 4](../foundations/t-diffusion-longtime.md#diffusion-cycle-proof) proves this without Chapter 41’s ergodic theorem. With infinite m but infinite endpoint scales, bounded nonnegative compactly supported f still has integrable cycle reward while mean cycle length is infinite, giving time average zero. Recurrence is thus distinguished from spending a positive long-term fraction in a region.

## 36.22 OU, Brownian Motion and Geometric Motion toward Zero

<a id="diffusion-longtime-examples"></a>

For OU, dX=−θXdt+σdW with θ>0, p=exp(θx²/σ²) and m′=(2/σ²)exp(−θx²/σ²). Both scales are infinite and total speed is finite, yielding the centered Gaussian with variance σ²/(2θ). Chapter 32’s explicit solution also gives convergence in law from a fixed state. The new result here is a scale-speed explanation of recurrence and path occupation fractions.

Ordinary Brownian motion has infinite scales but m(R)=∞: it is recurrent without invariant probability, and its time fraction in each fixed bounded region tends to zero. Driftless geometric Brownian motion has finite left scale and infinite right scale; it tends to zero without reaching it at finite time. Return, long-term occupation and boundary arrival are distinct properties, not one undifferentiated stability.

## 36.23 Turning Fate into Computable Relations

<a id="diffusion-insight"></a>

We did not read the future from a drift arrow. A scale making the reading fair, followed by speed measure restoring ordinary time, separated directional chance from occupation. Two boundary integrals distinguished finite-time arrival from starting at an endpoint. Reflection showed that a valid unique interior rule still leaves the boundary future unspecified.

Hitting identities, Green kernels, boundary probability tests and return-cycle calculations support these distinctions. More noise need not promote explosion; recurrence need not provide stationary probability; approaching a point need not mean hitting it at finite time. Their fate depends on how drift, fluctuation, scale, clock and boundary rules combine, not on the magnitude of any one alone.

Yet the speed formula still gives expected occupation. Decomposing time spatially along an individual path encounters the fact that each point has zero ordinary occupation time. The next tool must record cumulative passage intensity at a location without confusing it with ordinary time spent at that point.

### Sources and Scope

Feller’s [1954 original paper](https://doi.org/10.1090/S0002-9947-1954-0063607-6) is a primary source for boundary theory. We reorganize proofs with modern SDEs, stopping and ODEs rather than claiming its original discovery order. Compare speed normalizations with [Etheridge’s public notes](https://www.stats.ox.ac.uk/~etheridg/orsay/notes3.pdf): those notes keep a factor ½ outside the speed derivative, whereas we absorb it into m. Our core formulas are derived with the convention L=a∂²+b∂.

Complete proofs are in [T-SCALE-SPEED](../foundations/t-scale-speed.md), [T-FELLER-BOUNDARIES](../foundations/t-feller-boundaries.md) and [T-DIFFUSION-LONGTIME](../foundations/t-diffusion-longtime.md). Chapter 37 continues general singular scale/speed, all Markov extensions at regular endpoints, stickiness and local-time constructions. General Harris/mixing and the broadest ergodic theory are not counted as completed here.
