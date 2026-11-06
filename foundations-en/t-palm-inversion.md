# T-PALM-INVERSION: Inversion, Mass Transport, and Time–Cycle Duality

Return to [Chapter 50](../chapters/50-palm-gibbs.md#palm-inversion). We first work with a stationary random Radon measure on \(\mathbb R^d\), with intensity \(0<\lambda<\infty\), and P⁰ constructed in T-PALM. The cycle theorem later is restricted to simple nonempty configurations on the line, not multiplicities or general groups.

## 1. Weighted Inversion Including Empty Configurations

<a id="palm-inversion-weighted"></a>

Choose a positive everywhere, continuous, bounded, integrable h with \(\int hdx=1\). The mean intensity gives EΞh=λ, so Ξh is finite almost surely and positive exactly when Ξ≠0. For nonnegative F, apply noncentered Campbell to \(F(\xi)h(x)/(\xi h)\), assigning zero when ξh is zero or infinite, to get

\[ \mathbb E[F(\Xi)\mathbf1_{\{\Xi\ne0\}}]=\lambda\int_{\mathbb R^d}\mathbb E^0\left[\frac{h(x)F(\theta_{-x}\eta)}{(\theta_{-x}\eta)h}\right]dx. \]

All maps are measurable by joint kernel integration. The denominator is positive and finite for dx×P⁰-almost every pair: the original Campbell measure gives no mass to realizations with anomalous Ξh, and the centered identity transfers this null set to the product. P⁰ also never sees zero measure, since zero realizations contribute no Campbell mass. Nonnegative Tonelli establishes the identity without integrability of F. It recovers the nonzero part of P; empty-configuration mass cannot be read merely by observing occurrences. Given λ and P⁰, setting F=1 also computes the nonzero probability.

## 2. Successors on the Line and Mass Transport

<a id="palm-cycle-transport"></a>

Now let Ξ be stationary, simple, nonempty almost surely, with finite positive intensity. Its support is unbounded in both directions almost surely. If it were nonempty and bounded above, a locally finite closed point set would have a largest point R. The event is translation invariant, so conditioning on it would give R a translation-invariant probability on the real line, which is impossible. The left endpoint is treated the same way. A positive event probability would permit normalization, so both probabilities must be zero. Campbell transfers this path property to P⁰.

Enumerate a rooted configuration by \(\cdots<T_{-1}<T_0=0<T_1<\cdots\), and put τ η=θT₁η. Positions are recovered from local counts and measurable enumeration. T₁ is finite and positive, τ is measurable, and moving to the predecessor is its inverse. For nonnegative measurable k(η,u), let the root send mass k to the point at displacement u. Apply Campbell and Tonelli to the same double sum, once from senders and once from receivers, with a nonnegative h of integral one, to obtain

\[ \mathbb E^0\sum_{u\in\eta}k(\eta,u)=\mathbb E^0\sum_{u\in\eta}k(\theta_u\eta,-u). \]

Explicitly, start from \(\mathbb E\sum_{x,y\in\Xi}h(y)k(\theta_x\Xi,y-x)\). Campbell at x, followed by u=y−x and \(\int h(x+u)dx=1\), gives λ times the left side. Campbell at y gives λ times the right side. Both may be infinite; no subtraction is used. Set \(k(\eta,u)=\mathbf1_{\{u=T_1\}}G(\theta_u\eta)\). Unique predecessors and successors give E⁰G∘τ=E⁰G. Thus P⁰ is invariant under moving to the next point, which differs from stationarity under all real-time translations.

## 3. Integrating from Cycles Back to Time

<a id="palm-cycle-inversion"></a>

Every real y belongs to a unique half-open cycle [x,x+gapₓ). Partition \(\int h(y)F(\theta_y\Xi)dy\) into these cycles and apply Campbell to their initial points x. This gives

\[ \mathbb EF(\Xi)=\lambda\mathbb E^0\int_0^{T_1}F(\theta_t\eta)dt,\qquad \lambda\mathbb E^0T_1=1. \]

Stationarity and ∫h=1 give the left side; the spatial integral ∫h(x+t)dx=1 gives the right. Nonnegative F only needs Tonelli. For bounded signed F, first set F=1 to obtain finite mean cycle length and then split signs. If empty configurations are allowed, replace the left side by E[F1nonempty], and λE⁰T₁=P(nonempty). The simpler theorem in the chapter explicitly assumes nonemptiness almost surely.

## 4. The Converse Construction: Suspending a Cycle Law

<a id="palm-cycle-suspension"></a>

Let Q be a probability on simple configurations unbounded in both directions and rooted at zero, invariant under τ, with \(m=E_QT_1\in(0,\infty)\). Define \(PF=m^{-1}E_Q\int_0^{T_1}F(\theta_t\eta)dt\). MCT gives countable additivity, and m gives total mass one. Equivalently, bias Q by T₁/m and choose t uniformly within the cycle, providing a measurable construction.

For bounded F and a>0, the difference of shifted cycle integrals is \(G_a(\tau\eta)-G_a(\eta)\), with \(G_a(\eta)=\int_0^aF(\theta_t\eta)dt\). Both terms are bounded by a‖F‖, and τ-invariance makes the expected difference zero. Hence P is stationary, with negative translations following by inversion. Its Palm law still needs verification:

\[ \mathbb E_P\sum_{x\in\Xi}h(x)G(\theta_x\Xi)=\frac1m\mathbb E_Q\int_0^{T_1}\sum_{k\in\mathbb Z}h(T_k-t)G(\theta_{T_k}\eta)dt=\frac1m\left(\int h\right)E_QG. \]

For the last equality substitute η′=τᵏη term by term; Q is invariant under all integer powers. The variable u=t−Tₖ turns that term’s interval into [T₋ₖ,T₁₋ₖ) of η′. These intervals partition the line as k varies, so their h(−u) integrals sum to ∫h. Nonnegative Tonelli justifies interchange, and invertibility of τ gives invariance under negative powers. The intensity is 1/m and the Palm law is Q: the time–cycle constructions are genuinely inverse.

## 5. What This Adds to Renewal Theory

<a id="palm-renewal"></a>

Take strictly positive two-sided iid gaps Lₖ with 0<m=EL₁<∞. The strong law from Chapter 12 sends both partial sums to infinity, giving a locally finite rooted configuration. Rerooting shifts iid indices, so Q is τ-invariant. Suspension gives a stationary renewal process of intensity 1/m and proves that its Palm law is precisely the original iid rooted record. Chapter 19 constructed that process; the new result is general Palm identification and invertibility. For age A and residual life R,

\[ \mathbb E_P\varphi(A,R)=\frac1m\mathbb E\int_0^{L_1}\varphi(t,L_1-t)dt. \]

The formula gives a length-biased containing gap and a uniform internal position. It includes arithmetic gaps: real-time stationarity randomizes phase and does not require nonarithmeticity. If EL₁=∞, Q may still be legitimate, but the cycle integral cannot normalize into a nonempty stationary probability of finite positive intensity. At λ=0, every rational window count has expectation zero, so a locally finite process is empty almost surely. This excludes the stated stationary probability construction, not all infinite-mean limits.
