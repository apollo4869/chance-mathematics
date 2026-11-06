# T-LOCAL-TIME: From Convex Approximation to an Occupation Field

Companion to [Chapter 37](../chapters/37-local-time.md#local-smoothing). Work with a usual filtration and a continuous semimartingale X=X₀+M+V, where M starts at zero and V is continuous of finite variation starting at zero. Put A=[M]. Initially localize the initial value, path supremum, A and total variation of V to bounded levels; concatenate over integer horizons and localizers afterward. Inputs are Chapter 32 C² Itô, Chapter 31 isometry/brackets and Chapter 35 continuous-martingale moment bounds, not excursions or general Revuz theory.

## 1. What Smoothing the Absolute Value Produces

<a id="local-proof-tanaka"></a>

Take a nonnegative symmetric smooth kernel ρ supported in (−1,1) with integral one and convolve |·| with its ε-rescaling. The first derivative is bounded by one and the second is 2ρᵋ. At every fixed a the derivative tends pointwise to sgn, with sgn(0)=0. Isometry and Doob bound the squared maximal M-error by 4E∫|derivative error|²dA, tending to zero by DCT. Variation domination gives almost-sure uniform convergence of the V-error. The functions themselves differ from |·| by at most ε. Thus the following L is continuous and adapted for each a; the second-order convolution term converges ucp to it.

\[ L_t^{a,\mathrm{sym}}=|X_t-a|-|X_0-a|-\int_0^t\operatorname{sgn}(X_s-a)dX_s,\qquad \int_0^t\rho_\varepsilon(X_s-a)dA_s\ \xrightarrow{\mathrm{ucp}}\ L_t^{a,\mathrm{sym}}. \]

Every approximating term is nonnegative and increasing in t. An almost-sure uniformly convergent subsequence preserves both properties. Parameterized stochastic integrals admit a jointly measurable choice: approximate the bounded predictable-Borel map (s,ω,a)↦sgn(Xₛ(ω)−a) by simple maps in the product energy measure on bounded a-intervals, then use Fubini and isometry. For each fixed a this agrees with its usual integral. The stronger spatial version below removes the ambiguity of pointwise choices.

## 2. Occupation before Single-Level Bracket Statements

<a id="local-proof-occupation"></a>

Integrate the convolution terms against continuous compactly supported f. Ordinary Fubini gives ∫₀ᵗ(f*ρᵋ)(Xₛ)dAₛ. After localization the Tanaka right side has uniformly bounded p-th moments on compact a-intervals: the absolute-value terms are bounded, variation controls the V-integral, and the M-integral has bracket at most A and is controlled by Chapter 35 for every p≥2. The smooth approximants satisfy the same bound. Pointwise L¹ convergence therefore passes through the a-integral by DCT. Uniform continuity of f handles the other side.

\[ \int_{\mathbb R}f(a)L_t^{a,\mathrm{sym}}da=\int_0^tf(X_s)dA_s. \]

Use countably many dense compact continuous tests and rational t to obtain one exceptional set. Continuity and local integrability extend to all t; finite-measure uniqueness then extends pathwise to all nonnegative Borel f. The bracket occupation measure pushed forward by X is therefore absolutely continuous on every path, and has no atoms at any a. The integral ∫\(\mathbf1_{\{X=a\}}\)dM has zero bracket and is indistinguishably zero. This follows after occupation, avoiding a circular single-level argument.

## 3. Right Local Time and Spatial Jumps

<a id="local-proof-regularity"></a>

To choose coherent versions at all levels specify the derivative at the corner. Set sgn₋(0)=−1 and otherwise sgn₋=sgn. Define right local time Lᵃ⁺ by replacing sgn with sgn₋ in Tanaka’s expression. Convex approximants with curvature concentrated in (a,a+ε) also prove nonnegativity and monotonicity directly. Its difference from the symmetric version is ∫\(\mathbf1_{\{X=a\}}\)dV. The pushforward of total variation has only countably many atoms, so these versions agree for almost every a and have the same occupation formula.

\[ L_t^{a,+}=|X_t-a|-|X_0-a|-\int_0^t\operatorname{sgn}_{-}(X_s-a)dX_s,\qquad L_t^{a,+}-L_t^{a-,+}=2\int_0^t\mathbf1_{\{X_s=a\}}dV_s. \]

Spatial regularity needs a proof. Write Jᵃ=∫sgn₋(X−a)dM. For a<b its difference is −2 times the integral over [a,b); endpoints do not affect brackets. Occupation and the preceding uniform moment bounds give, for every integer p≥2,

\[ E\|J^b-J^a\|_{C[0,T]}^{2p}\le C_pE\left(\int_a^bL_T^{y,+}dy\right)^p\le C_{p,K,T}|b-a|^p. \]

The last step is integral Hölder: the p-th power is bounded by (b−a)^{p−1}∫(Lᵞ)ᵖdy. Apply Chapter 23’s dyadic argument to C[0,T]-valued variables. For neighboring differences with threshold \(2^{-n\alpha}\), the union probabilities are summable when 2pα<p−1; chaining gives spatial α-Hölder versions. Arbitrarily large p allow every α<1/2. Thus J is spatially continuous with values in continuous time paths.

The variation part is right-continuous with left limits in a, even in the C[0,T] norm: for aₙ↓a the signs tend pointwise to sgn₋, and variation DCT applies uniformly in t. Approaching from below gives the other corner value; their difference is exactly the displayed jump. Absolute-value terms are continuous. Hence L⁺ is spatially càdlàg and temporally continuous with the stated jump. Verify Tanaka first at rational a and extend using this regularity, outside one exceptional set. Localization is coherent because the stopped Tanaka expressions coincide.

For a continuous local martingale V=0, L⁺ is spatially continuous and agrees with symmetric local time. Brownian L is consequently jointly continuous. On compact rectangles occupation convolutions converge uniformly, by the occupation formula and uniform continuity of L. For general semimartingales one-sided averages converge in C[0,T] at each a to Lᵃ⁺; spatial jumps cannot be silently removed.

\[ L_t^a(B)=\lim_{\varepsilon\downarrow0}\frac1{2\varepsilon}\int_0^t\mathbf1_{\{|B_s-a|<\varepsilon\}}ds,\qquad L_t^{a,+}(X)=\lim_{\varepsilon\downarrow0}\frac1\varepsilon\int_0^t\mathbf1_{\{a\le X_s<a+\varepsilon\}}d[M]_s. \]

## 4. Support, Reflection and Inverse Local Time

<a id="local-proof-inverse"></a>

If X stays a positive distance from a on a closed time interval, sufficiently narrow curvature approximants vanish there, so local time does not increase. Countable rational intervals and spatial right continuity give support of dLᵃ⁺ on {X=a}. For Brownian motion at zero, Tanaka reads |B|=β+L with β=∫sgn(B)dB. Zero ordinary time at zero implies [β]ₜ=t, so Chapter 33’s Lévy characterization makes β Brownian.

The deterministic Skorokhod lemma is elementary. If r=w+k≥0 for continuous w starting at zero, k is continuous increasing from zero and increases only at r=0, then k(t)=supₛ≤ₜ(−w(s))⁺. Nonnegativity gives the lower bound; any first excess increase would occur when r was already positive, contradicting support. Thus L=−minβ and L∞=∞. Reflection or Chapter 26’s hitting probabilities show Brownian motion takes both signs in every positive initial interval, so local time increases immediately after any zero.

\[ \tau_\ell=\inf\{t:L_t^0>\ell\},\qquad E e^{-\lambda\tau_\ell}=e^{-\ell\sqrt{2\lambda}},\qquad \ell\ge0,\ \lambda>0. \]

The right-continuous inverse is finite and a stopping time, with Bτ=0 and Lτ=ℓ. These identities follow from continuity, unboundedness and support of L. For fixed ℓ its law under Skorokhod’s representation is the first β-hit of −ℓ. Solve ½h″=λh with bounded-interval stopping, or integrate Chapter 26’s hitting density, to get the transform. Strong Markov at τℓ and additivity of local time give stationary independent increments in ℓ. Additivity follows by subtracting the time-shifted Tanaka expressions; rational times and stopping-time grid approximations plus continuity give the required common versions.

## 5. Transformation and Predictability

<a id="local-proof-transform"></a>

For strictly increasing C² h with h′>0, [h(X)]=∫h′(X)²d[M]. Occupation on both sides and a change of variables give \(L^{h(a)}\)(h(X))=h′(a)Lᵃ(X) for almost every a. Continuity extends it to all levels when applicable, and one-sided regularity handles right local times. In Chapter 36’s nondegenerate SDE, variation on a level is b(a)∫\(\mathbf1_{\{X=a\}}\)dt=0: σ has a positive lower bound locally and single-level bracket occupation is zero. Its local times are therefore jointly continuous.

\[ \int_0^tf(X_s)ds=\int_I f(a)\frac{L_t^a(X)}{\sigma(a)^2}da,\qquad t<\zeta,\quad f\ge0. \]

The ordinary-time density is L/σ², rather than L for every diffusion. The indicator \(\mathbf1_{\{X=a\}}\) is predictable because X is continuous adapted and predictable measurability is preserved by Borel composition. Its integral against a continuous local martingale vanishes, while its dL-integral equals L. The integration measures differ; there is no contradiction. Return to [the two clocks](../chapters/37-local-time.md#local-two-clocks).
