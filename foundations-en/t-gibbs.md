# T-GIBBS: Papangelou Densities, Finite-Volume Kernels, and an Infinite-Volume Existence Theorem

Return to [Chapter 50](../chapters/50-palm-gibbs.md#palm-papangelou). The density part uses LCSC point spaces, σ-finite reference m, and σ-finite mean intensity ν. The finite-volume part explicitly requires m(B)<∞. Infinite-volume existence is proved only for bounded continuous nonnegative symmetric finite-range pair potentials on Euclidean space with constant activity; arbitrary Gibbs interactions are not asserted to exist or be unique.

## 1. Papangelou Is an Absolute-Continuity Statement

<a id="gibbs-papangelou"></a>

For the law P of Ξ, T-PALM gives reduced Campbell measure \(C^!(dx,d\eta)\). A measurable nonnegative c satisfying

\[ \mathbb E\int F(x,\Xi-\delta_x)\Xi(dx)=\int m(dx)\int F(x,\eta)c(x,\eta)P(d\eta) \]

for every nonnegative F exists exactly when \(C^!\ll m\otimes P\). This follows directly from Chapter 10’s Radon–Nikodym theorem, since both measures are σ-finite; c may be chosen finite m×P-almost everywhere. It is the Papangelou conditional intensity, and the displayed identity is GNZ. It is not a predictable intensity relative to a time filtration, nor a density possessed by every point process.

If \(\nu(dx)=\rho(x)m(dx)\), then \(\rho(x)=E_Pc(x,\Xi)\), and on the common full-m part with 0<ρ(x)<∞,

\[ Q_x^!(d\eta)=\frac{c(x,\eta)}{\rho(x)}P(d\eta). \]

First test F=1A(x) to identify the intensity density. Combine null sets for a countable generating environment class and use T-PALM kernel uniqueness. At ρ=0 the identity does not determine the kernel, so fix a version. If Ξ=\(\delta_U\) with U uniform on [0,1], its mean has length density, but reduced Palm is always empty while P only sees singleton configurations. Testing whether the remainder is empty makes the GNZ left side one and right side zero, proving failure of Papangelou absolute continuity.

## 2. A Finite Poisson Reference and Hereditary Densities

<a id="gibbs-finite-density"></a>

Let πₘ be the finite-intensity Poisson law on B. Take measurable p≥0 with \(\int p\,d\pi_m=1\) and heredity: p(η)=0 implies p(η+δₓ)=0. Define P=pπₘ. Mecke gives \(C^!(dx,d\eta)=m(dx)p(\eta+\delta_x)\pi_m(d\eta)\). Heredity eliminates a singular remainder on p=0, so c=p(η+δₓ)/p(η) on p>0, with zero on p=0, satisfies GNZ.

Having a density relative to Poisson alone is insufficient. Conditioning π on total count one produces a nonhereditary density and exactly the preceding counterexample. Heredity is an explicit sufficient condition, not a property of every constraint.

Concretely take 0≤z(x)≤z̄<∞ and a symmetric measurable pair potential φ≥0, allowing φ=∞ for hard exclusion. Given an exterior locally finite configuration ξ, define

\[ w_B(\eta\mid\xi)=\prod_{x\in\eta}z(x)\exp\left\{-\sum_{\{x,y\}\subset\eta}\phi(x,y)-\int_B\int_{B^c}\phi(x,y)\xi(dy)\eta(dx)\right\}. \]

The internal sum is over unordered pairs of different occurrences; diffuse m makes configurations simple almost surely. Empty products are one, \(e^{-\infty}=0\), and nonnegative measurable sums and integrals define all energies. The partition function \(Z_B(\xi)=\int w_B(\eta\mid\xi)\pi_{m|B}(d\eta)\) satisfies \(e^{-m(B)}\le Z_B(\xi)\le\exp\{(\bar z-1)m(B)\}\), so it is positive and finite; the upper bound is the Poisson count generating function. The normalized density is hereditary, and a Papangelou version is

\[ c_B(x,\eta\mid\xi)=\mathbf1_B(x)z(x)\exp\left\{-\int\phi(x,y)(\eta+\xi|_{B^c})(dy)\right\}\le\bar z. \]

Values on zero-density configurations may differ without changing the P-identity. On positive-density configurations the formula is the exact additional-point energy ratio. No ∞−∞ subtraction is made: weights factor multiplicatively, and a forbidden addition has weight zero.

## 3. How GNZ Recovers a Finite-Volume Law

<a id="gibbs-janossy"></a>

Fix B and ξ, and suppose another probability P on finite configurations satisfies GNZ with this \(c_B\). Let \(J_n\) be the expected factorial measure of all ordered n distinct occurrences on the event of total count n, with J₀=P(N=0). Its total mass is n!P(N=n), hence finite. Test GNZ by requiring remainder count n−1 and enumerating all remaining n−1 occurrences. Tonelli gives

\[ J_n(dx_1\cdots dx_n)=J_{n-1}(dx_1\cdots dx_{n-1})c_B\!\left(x_n,\sum_{i<n}\delta_{x_i}\mid\xi\right)m(dx_n). \]

Iteration gives \(J_n=q_0w_B(\sum_i\delta_{x_i}\mid\xi)m^n\). If q₀=0, every Jₙ vanishes, contradicting total probability one on finite configurations. Thus q₀>0. Reconstruct every nonnegative configuration test by \(E_PF=\sum_n(n!)^{-1}\int F(\sum_i\delta_{x_i})dJ_n\). Normalization uniquely fixes q₀; comparison with the Poisson density series gives the same Gibbs law. The proof does not first assume this other P has a Poisson density, and does not invoke GNZ by name as a substitute for uniqueness.

For a pair potential, the products of weights for adding x and then y equal those for the reverse order, because φ is symmetric. This gives multiplicative cocycle compatibility and shows why an arbitrary configuration-dependent nonnegative c need not integrate into consistent Gibbs weights. The claim concerns the displayed potential-based version, not arbitrary almost-everywhere Papangelou representatives at every configuration.

## 4. Exterior Conditioning Kernels and Consistency

<a id="gibbs-specification"></a>

Define \(\Gamma_B\)(ξ,·) by retaining ξ outside B and resampling inside B with the normalized Poisson density above. Joint measurability of exterior integrals follows from Chapter 49. The finite Poisson reference makes the parameter integral measurable, and positive finite \(Z_B\) gives a probability kernel. Adding the exterior restriction is evaluation-measurable and preserves local finiteness.

If A⊂B, the reference Poisson measures on A and B∖A are independent, and the weights factor exactly as \(w_B(\eta_A+\eta_{B\setminus A}\mid\xi)=w_{B\setminus A}(\eta_{B\setminus A}\mid\xi|_{B^c})w_A(\eta_A\mid\eta_{B\setminus A}+\xi|_{B^c})\). Fubini for nonnegative tests and normalization show that, conditional on B∖A and the exterior, the law inside A is \(\Gamma_A\). Hence

\[ \Gamma_B\Gamma_A=\Gamma_B,\qquad P\Gamma_B=P\quad\hbox{for a Gibbs probability }P. \]

The second identity is the DLR requirement, not automatic existence of an infinite P from finite-kernel consistency. Conversely, suppose a locally finite P satisfies global GNZ with this potential’s c. Multiply tests by arbitrary exterior events and disintegrate inside a fixed B given the exterior. A common null set for countable generating tests gives finite-volume GNZ for the conditional law. The preceding uniqueness theorem makes it \(\Gamma_B\). In the other direction, DLR and finite-volume GNZ in successive windows, followed by a countable exhaustion, recover global GNZ. For each fixed B the conditional statement holds almost surely under its exterior marginal; no simultaneous version for an arbitrary uncountable boundary family is asserted.

## 5. An Actual Infinite-Volume Existence Proof

<a id="gibbs-infinite-existence"></a>

Now restrict to \(E=\mathbb R^d\), m=dx, constant z>0, and \(\phi(x,y)=\psi(x-y)\), with ψ nonnegative, continuous, symmetric, and compactly supported. Exhaust space by bounded boxes Bₙ and let Pn=\(\Gamma_{B_n}\)(empty), empty outside the box. It satisfies global GNZ with cₙ=c1Bₙ. Write \((n)_r=n(n-1)\cdots(n-r+1)\), with value zero for n<r and \((n)_0=1\). Repeated GNZ gives \(E_{P_n}(\Xi K)_r\le(z|K|)^r\) for every compact K and r≥1. Indeed, insert \(F(x,\eta)=\mathbf1_K(x)(\eta K)_{r-1}\) in GNZ to get \(E(\Xi K)_r\le z|K|E(\Xi K)_{r-1}\), and induct from r=1 using nonnegative integrals. The local first-moment bounds and Chapter 49 tightness give a vague weak subsequential limit P. Closedness of the integer subspace keeps the limit a point configuration.

GNZ must actually pass to the limit. First take F(x,η)=h(x)H(η), with h∈Cc and H bounded continuous. The function \(c(x,\eta)=z\exp\{-\eta\psi(x-\cdot)\}\) is jointly continuous: over compact x-windows the shifted ψ have a common compact support and vary uniformly, and local mass bounds apply. The right integral is bounded continuous, dominated by z‖H‖∫|h|. The left functional \(\sum_{x\in\eta}h(x)H(\eta-\delta_x)\) is also continuous. In a continuity window containing supp h in its interior, vague point convergence matches finitely many occurrences; moving and deleting one preserves vague convergence. Such windows exist because only countably many radii have charged spheres. Matching follows from stable integer counts in small disjoint balls, then shrinking them.

The left functional need not be bounded, but its absolute value is at most ‖h‖‖H‖Ξ(K). The second factorial bound gives uniformly bounded second moments and uniform integrability. For the limit, use a continuous cutoff χ≥1K and Portmanteau for a corresponding finite second-moment bound. Clip the continuous left functional, pass expectations, then remove clipping. GNZ therefore holds for product tests under P. Both sides are finite on compact spatial windows; Cc spatial tests and Cb configuration tests generate the Borel σ-algebras, so uniqueness of finite measures and monotone classes give all nonnegative joint F. No unjustified weak-limit exchange with unbounded counts is used.

The diffuse reference also forces P to be simple. In GNZ take F(x,η)=1{η{x}≥1}. The right side integrates over the countable atomic support of η and is zero. The left counts occurrences at repeated positions for which another occurrence remains after deletion; hence there are no multiplicities almost surely. Conditioning and finite-volume uniqueness from the preceding section give DLR. This constructs an infinite-volume Gibbs probability, rather than just naming consistent kernels.

## 6. A Stationary Version and the Limits of the Proof

<a id="gibbs-stationary-scope"></a>

Constant activity and a difference potential make c translation-covariant. Every translated P therefore satisfies the same GNZ and factorial bounds. Uniformly average its translates over growing boxes; these probabilities still satisfy GNZ and are tight. In a weak limit, the preceding continuity and uniform-integrability argument again preserves GNZ. For every fixed translation a, the symmetric-difference volume of the two averaging boxes divided by their volume vanishes, making expectations of bounded continuous tests asymptotically equal. Continuity of translations makes the limit stationary. Thus a stationary infinite-volume Gibbs law exists.

Infinite-volume uniqueness is not proved. Discontinuous hard-core potentials, unstable attractive potentials, arbitrary long-range energies, and all group spaces are not included in this limit argument. Finite-volume kernels for nonnegative measurable potentials and hard exclusion were proved to exist and be consistent above. Their broadest infinite-volume existence, phase behavior, and uniqueness require additional tools and remain separately recorded outside the proved scope.
