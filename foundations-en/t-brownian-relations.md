# T-BROWNIAN-RELATIONS: Complete Proofs for Weights, Clocks and Information

This companion links back to [Chapter 33](../chapters/33-brownian-relations.md). Filtrations satisfy the usual conditions; continuous local martingales start at zero, and T denotes a finite horizon. Inputs are conditional expectation, optional sampling, continuous-martingale integration/brackets and Chapter 32’s continuous-semimartingale Itô formula. The proofs establish finite-horizon equivalent measure change, scalar DDS, the specified Wiener translations, representation in the natural Brownian filtration and stopping-time embedding of centered finite-second-moment laws. The conclusions are not extended to general jump versions or arbitrary Banach Gaussian spaces.

## 1. Density and the Stopped Product

<a id="t-br-change"></a>

Let Z be a strictly positive continuous true P-martingale with Z₀=1, and define Q on \(\mathcal F_T\) by \(Z_T\). Testing bounded \(\mathcal F_t\)-measurable X on A∈\(\mathcal F_s\), with the factor \(Z_s\), proves the Bayes identity in Section 33.2. Monotone truncation extends it to nonnegative X; positive and negative parts give Q-integrable X. Every bounded stopping value of Z is a conditional expectation of \(Z_T\), so these values form a UI family. This applies the closed-martingale stopping result of Chapter 16, not a claim about arbitrary local martingales.

Let M be a continuous local P-martingale and put N=M−∫Z⁻¹d[M,Z]. On compact intervals continuity and strict positivity bound Z⁻¹ pathwise; covariation has finite variation, so the integral exists. First take M₀=0. Let \(\tau _n\) be the first time |N| reaches n, capped at T. The required product is Z times the stopped N, not a simultaneous stopping of the whole product. Integration by parts gives

\[ d(Z_tN_{t\wedge\tau_n})=N_{t\wedge\tau_n}\,dZ_t+\mathbf1_{\{t\le\tau_n\}}Z_t\,dM_t. \]

Before \(\tau _n\), the finite-variation correction cancels the cross bracket. Afterwards N is fixed while Z continues, leaving \(N_{\tau _n}\)dZ. Both predictable local integrals were constructed in Chapter 31. At any stopping time σ≤T the absolute product is bounded by nZ\_σ. The UI stopping family of Z makes this a class-D local martingale. Stop along a true-martingale localizing sequence and pass conditional expectations in L¹ using UI; the product is therefore a true martingale. Bayes now makes stopped N a Q-martingale. Continuity bounds N on every compact path, so \(\tau _n\) eventually equals T; equivalence transfers the common exceptional set. Thus N is a continuous local Q-martingale. A nonzero integrable initial value may be restored: it is measurable in the initial sigma-algebra, and Z₀=1 makes P and Q agree there, so the initial value is Q-integrable as well.

For B and Z=𝓔(∫θ·dB), Chapter 31’s bracket transformation gives [B^i,Z]=∫Zθ\_i ds. Finite-horizon equivalence preserves convergence in probability and ucp: Q(E)≤K P(E)+E[\(Z_T1\)\_{\(Z_T\)>K}], with the second term made small before the first. Square-sum limits consequently agree, and subtracting finite variation leaves brackets unchanged. The conditional-characteristic-function proof in Section 33.5 identifies B−∫θds as Q-Brownian motion relative to the same filtration. Section 33.4 proves the full critical-coefficient Novikov criterion without assuming its own conclusion.

## 2. A Strictly Positive Strict Local Density

<a id="t-br-strict"></a>

Take standard three-dimensional Brownian motion W, x≠0, r=|x| and \(R_t\)=|x+\(W_t\)|. First prove that the entire path avoids zero. The function f(y)=1/|y| has zero Laplacian away from zero. Stopped between radii ε and L, where 0<ε<r<L, Itô’s formula gives a bounded true martingale. Exit from the annulus is finite: a coordinate has a uniformly positive probability of moving more than 2L in a fixed time block; independent blocks give a geometric survival bound inside the ball. Optional sampling and bounded convergence yield

\[ P_x(\tau_\varepsilon<\tau_L)=\frac{r^{-1}-L^{-1}}{\varepsilon^{-1}-L^{-1}}. \]

For fixed L let ε decrease to zero along reciprocal integers. The probability tends to zero, excluding a hit of zero before \(\tau _L\). A path hitting zero at finite time must, up to that time, lie inside some ball of integer radius. A countable union excludes every finite hit. Continuity then gives a strictly positive minimum of R on each compact interval, on one probability-one set.

Itô’s formula and Chapter 32’s exponential solution of a linear equation give the following identities. The integrand has finite square energy on compact intervals, without using future Bessel-process theory.

\[ Z_t=\frac r{R_t},\qquad dZ_t=-Z_t\frac{x+W_t}{R_t^2}\cdot dW_t,\qquad Z=\mathcal E\left(-\int\frac{x+W}{R^2}\cdot dW\right). \]

The expectation can be checked directly. In spherical coordinates around the axis x, the angular integral of the three-dimensional Gaussian is 4πt sinh(rρ/t)/(rρ). Including the radial Jacobian and 1/ρ and completing squares gives

\[ E_x\frac1{R_t}=\frac1{r\sqrt{2\pi t}}\int_0^\infty\left(e^{-(\rho-r)^2/(2t)}-e^{-(\rho+r)^2/(2t)}\right)d\rho=\frac{2\Phi(r/\sqrt t)-1}{r}. \]

Thus \(EZ_t\)<1, so Z is a strict local martingale. Conditional on \(\mathcal F_s\), future three-dimensional increments are independent Gaussian; replacing r by \(R_s\) gives E[\(Z_t\)|\(\mathcal F_s\)]/\(Z_s\)=2Φ(\(R_s\)/√(t−s))−1. For s>0 this is not deterministic: \(R_s\) is nondegenerate and the expression is strictly increasing in \(R_s\). Normalizing each terminal value separately therefore fails to restore temporal consistency.

## 3. Bounded Quadratic Clocks, Infinite Stopping and Flat Intervals

<a id="t-br-clock"></a>

We first prove the closure lemma needed for DDS, rather than using the desired time change to prove integrability. If a continuous local martingale M has bracket A with \(A_\infty \)≤C for a deterministic finite C, stop at amplitude and localizing bounds. Chapter 31’s martingale identity for M²−A and Doob’s inequality give E \(sup_t\)|\(M_t\)|²≤4C: first use a finite time interval, remove localization by Fatou, then increase the horizon. The original process is consequently a true L²-martingale. All stopping values of M² and A are dominated respectively by the integrable sup|M|² and C, so M²−A is a class-D true martingale.

At integer times orthogonal increments make \(M_n\) Cauchy in L²: E(\(M_m\)−\(M_n\))²=\(EM_m\)²−\(EM_n\)², with increasing bounded second moments. Write its L² limit as \(M_\infty \); then \(M_t\)=E[\(M_\infty \)|\(\mathcal F_t\)] for every t. Doob applied to the tail of this closed martingale gives E \(sup_{t≥n}\)|\(M_t\)−\(M_n\)|²≤4E|\(M_\infty \)−\(M_n\)|². Choose a subsequence with summable bounds and use Markov and Borel–Cantelli to obtain \(M_t\)→\(M_\infty \) almost surely in full continuous time. Domination by sup|M|² gives L¹ convergence of squares; A converges boundedly and increasingly. Thus M²−A is also closed by its terminal value. Chapter 16’s closed-martingale sampling, allowing infinity and completed \(\mathcal F_\infty \)=σ(∪\(\mathcal F_t\)), is now legitimate; the terminal variable was proved to exist.

For general locally finite A, fix rational r<s. Subtract \(M_r\) after time r and stop when \(A_t\)−\(A_r\) first exceeds 1/n. The stopped quadratic clock is at most 1/n. The preceding lemma and the weak maximal inequality for |M|² give

\[ P\left(A_s=A_r,\ \sup_{r\le t\le s}|M_t-M_r|>\varepsilon\right)\le\frac1{n\varepsilon^2}. \]

Let n tend to infinity and take a countable union over r, s and rational ε>0. Continuity then makes M constant on every flat interval of A: interior points are approached by rational interior points and endpoints by continuity. This is the reason an inverse clock may skip original time without skipping a spatial displacement.

## 4. DDS, Including a Finite Terminal Clock

<a id="t-br-dds"></a>

Put ζ=\(A_\infty \) and \(\tau _s\)=inf{t≥0:\(A_t\)>s}, taking infinity for an empty set. Continuity of A and right continuity of the filtration make \(\tau _s\) a stopping time: {\(\tau _s\)<t} is the union over rational q<t with \(A_q\)>s, and right continuity supplies the ≤t event. If \(\tau _s\) is finite, continuity and inverse-clock properties give \(A_{\tau _s}\)=s. If \(\tau _s\) is infinite, ζ≤s. For every integer K stop M at \(\tau _K\). Its quadratic clock is at most K, so the preceding section supplies a terminal value at infinity and closure.

On {ζ<∞}, the countable cover {ζ<K} defines a consistent \(M_\infty \). Put W̃\_s=\(M_{\tau _s}\), using this terminal value when \(\tau _s\) is infinite. The flat-interval lemma, continuity of M and its convergence on a finite terminal clock make W̃ continuous, including at s=ζ. The inverse relation gives \(M_t\)=W̃\_{\(A_t\)}. If A is already constant at ζ after t, the flat-interval lemma also gives \(M_t\)=\(M_\infty \).

Set \(G_s\)=\(\mathcal F_{\tau _s}\). It is complete and right-continuous: when \(s_n\)↓s, \(\tau _{s_n}\)↓\(\tau _s\), allowing infinity, and decreasing stopping times satisfy ∩F\_{\(\tau _{s_n}\)}=\(\mathcal F_{\tau _s}\). To check the latter, for E in the intersection write E∩{\(\tau _s\)<t}=∪\_n(E∩{\(\tau _{s_n}\)<t})∈\(\mathcal F_t\), then decrease t+1/m to t and use the original right continuity. The reverse inclusion follows from the order of stopping times.

For 0≤s≤t≤K sample the closed martingales M^{\(\tau _K\)} and (M^{\(\tau _K\)})²−A^{\(\tau _K\)} at \(\tau _s\) and \(\tau _t\), using the terminal values already established at infinity. Thus W̃ is a G-martingale in L² on [0,K], and W̃²−min(s,ζ) is a martingale. Also ζ is a G-stopping time: {ζ≤s}={\(\tau _s\)=∞} belongs to \(\mathcal F_{\tau _s}\), since its intersection with {\(\tau _s\)≤t} is empty. Hence [W̃]\_s=min(s,ζ), and W̃ is constant after ζ.

If ζ=∞ almost surely, Lévy’s characterization immediately makes W̃ Brownian. This is scalar DDS for a divergent quadratic clock, relative to G rather than merely equality in law. If ζ can be finite, the original space may lack spare randomness: the zero martingale may live on a one-point space. On an independent product space add Brownian motion β and let \(H_s\) be the usual augmentation of \(G_s\) and β’s information up to s. Testing independent product events shows that W̃ remains an H-martingale and β remains H-Brownian. Their product is a local martingale, by bounded stopping and conditional independence, so their cross bracket is zero.

\[ W_s=\widetilde W_s+\int_0^s\mathbf1_{\{u>\zeta\}}\,d\beta_u,\qquad [W]_s=\min(s,\zeta)+(s-\zeta)^+=s,\qquad M_t=W_{A_t}. \]

The process 1\_{u>ζ} is left-continuous and adapted, hence predictable. Its integral was constructed in Chapter 31, with zero cross bracket. Lévy’s characterization makes W H-Brownian. Since \(A_t\)≤ζ, the added integral vanishes at \(A_t\) and the final identity holds as a process identity. Only independent noise after the terminal clock is added; no unproved randomly shifted filtration is used.

## 5. The Exact Energy Boundary for Deterministic Translation

<a id="t-br-cm"></a>

First compare Wiener measure μ on C₀[0,T] with the law \(\mu _h\) of a continuous translation h with h(0)=0. Sufficiency was proved in Section 33.11 by deterministic-integrand Girsanov. Its Wiener integral I(g) is a measurable version of an L² limit: from step approximations \(g_n\) choose an almost surely convergent subsequence of I(\(g_n\)), and set the limit to zero on the measurable null set of failure. The density identity is required only μ-almost everywhere. Strict positivity gives equivalence and consistent versions under \(\mu _h\); no ordinary integral on every continuous curve is asserted.

For necessity use the real Haar orthonormal basis on [0,T]: the constant T⁻¹ᐟ² and normalized step functions of opposite signs on the halves of each dyadic interval. Every dyadic step function lies in a finite linear span of these vectors. They are dense in L²: approximate interval indicators by dyadic endpoints, use the set monotone-class theorem and dominated convergence for finite measure to obtain Borel simple functions, and finally use the integral definition to approximate L² functions. Each coordinate \(\xi _k\)(x)=∫\(e_k\) dx is just a finite linear combination of path increments, hence a continuous measurable reading.

Under μ these readings are independent N(0,1): every finite collection is a linear transform of Gaussian increments, with identity covariance by orthogonality, so the joint characteristic function factors. Under \(\mu _h\) their means are \(m_k\)=∫\(e_k\) dh. This is still a finite increment sum and assumes no prior bounded variation of h. If Σ\(m_k\)² is finite, L² completeness constructs g=Σ\(m_ke\)\_k. The finite Haar expansion of every dyadic interval indicator gives h(t)−h(s)=∫\_s^t g. Continuity of h and of the integral extends this to all endpoints. Thus h is absolutely continuous, h′=g∈L² and its energy is Σ\(m_k\)².

If h is outside this energy space, \(s_n\)=Σ\_{k≤n}\(m_k\)² must diverge. Choose \(s_{n_j}\)≥2^j and set \(D_j\)=\(s_{n_j}\)⁻¹Σ\_{k≤\(n_j\)}\(m_k\)ξ\_k. Under μ it has mean zero and variance 1/\(s_{n_j}\); under \(\mu _h\) its mean is one and its variance the same. Chebyshev and Borel–Cantelli give \(D_j\)→0 and \(D_j\)→1 respectively almost surely. These disjoint Borel limit events prove μ⊥\(\mu _h\). The energy requirement is therefore not merely convenient smoothness. If h(0)≠0, the initial-value event already separates the laws.

On C₀[0,∞), failure of the energy condition on a finite window already yields singularity by projection. Otherwise use the preceding Haar basis on each unit interval to obtain a countable basis of L²[0,∞). Infinite total energy gives singularity through the same \(D_j\) test. For finite total energy, \(M_t\)=∫₀ᵗg dB has a bounded deterministic quadratic clock, so Section 3 gives \(M_\infty \). The exponential satisfies E \(Z_t\)²=exp(∫₀ᵗg²)≤exp(∫₀∞g²); it is UI and converges to the strictly positive exp(\(M_\infty \)−∫g²/2), of mean one. On each finite window it is the deterministic Girsanov density. The Borel σ-algebra of \(C_loc\) is generated by rational-time readings; π–λ uniqueness identifies the full translated path law and gives equivalence for all time.

The same reasoning proves the translation criterion for a countable Gaussian product. For independent standard Gaussian coordinates \(\xi _k\) shifted by \(m_k\), if Σ\(m_k\)² is finite Chapter 12’s independent-series criterion gives convergence of Σ\(m_k\)\(\xi _k\) in L² and almost surely. The limit of the finite-coordinate densities exp(Σ\_{k≤n}\(m_k\)\(\xi _k\)−Σ\_{k≤n}\(m_k\)²/2) is therefore strictly positive. Their second moments are bounded by exp(Σ\(m_k\)²); UI gives mean one, and cylinder uniqueness identifies the translated law. If the series diverges, the \(D_j\) test separates the laws. This is a specific result available to Chapter 39, not a claim to have proved all Gaussian Banach-space theory or a chaos expansion.

## 6. The Usual Natural Filtration and Local Representation

<a id="t-br-local-representation"></a>

Representation first requires checking that the usual augmentation has not secretly added future information. Let \(H_t\) be the completion of the raw Brownian natural σ-algebra, and \(H_\infty \) the completion of all path readings. We prove ∩\_{u>t}\(H_u\)=\(H_t\). Start with a bounded continuous finite-coordinate function X=f(\(B_{r₁}\),…,\(B_{r_k}\)). As ε↓0, avoiding the finitely many positive time gaps, conditioning on \(H_{t+\varepsilon }\) leaves readings before t known and represents future readings by \(B_{t+\varepsilon }\) plus an independent Brownian motion at times \(r_i\)−t−ε. Couple these Gaussian vectors with one independent continuous Brownian path. Continuity and bounded dominated convergence give

\[ E[X\mid H_{t+\varepsilon}]\longrightarrow E[X\mid H_t]\quad\text{in }L^2. \]

Bounded continuous finite-coordinate functions are dense in L²(\(H_\infty \)): in finite-dimensional Gaussian measure approximate indicators using closed-set distance functions and measure regularity, then apply the set monotone-class theorem to the path σ-algebra generated by countably many rational coordinates. Conditional expectation is an L² contraction, so the displayed limit extends to every X∈L²(\(H_\infty \)). If E∈∩\(H_{t+1/n}\), use X=1\_E: its conditional expectations on the left equal 1\_E, yielding 1\_E=E[1\_E|\(H_t\)], hence E∈\(H_t\). Thus H is already right-continuous; the usual natural Brownian filtration is exactly H. In particular H₀ contains only constants and null sets. No martingale representation was used, avoiding a circle.

Sections 33.19–33.21 already prove L² representation using a closed space and totality of exponentials. Its final density step is now justified: finite rational-time coordinates generate \(\mathcal F_T\), and completion does not change L² equivalence classes. For d-dimensional Brownian motion use deterministic step vectors h in every coordinate; the same finite-Gaussian exponential proof applies, with Itô isometry using Σ∫\(H_i\)². Uniqueness follows from isometry: equal terminal values imply E∫|H−K|²dt=0; Doob gives indistinguishable integral processes.

An L¹ terminal value cannot use an L² projection directly. Let \(X_n\) be bounded truncations of X and M^\(n_t\)=E[\(X_n\)|\(\mathcal F_t\)], choosing continuous versions from L² representation. Apply the weak L¹ maximal inequality to M^n−M^m on finite rational grids, then refine using continuity. This gives P(\(sup_{t≤T}\)|M^\(n_t\)−M^\(m_t\)|>ε)≤E|\(X_n\)−\(X_m\)|/ε. Choose a subsequence with summable probabilities for adjacent differences exceeding 2⁻ʲ. It converges uniformly almost surely to a continuous M. At each deterministic t, L¹ contraction gives \(M_t\)=E[X|\(\mathcal F_t\)]. Identify simultaneously at rational t; càdlàg paths then give indistinguishability from any pre-existing càdlàg version.

For a càdlàg local martingale first use a true-martingale localizing sequence. On finite T each stopped process is the conditional expectation of its integrable terminal value and therefore continuous by the preceding argument. Glue countably many stopped versions to make the original local martingale continuous. Before proving continuity, stopping at the first crossing of n would not justify boundedness: a general càdlàg process can overshoot.

Now stop the continuous local martingale M at amplitude n, together with existing localization if needed, to get bounded, hence L² true martingales and representations H^n. For m≥n compare the representations up to the earlier stop. Chapter 31’s stopping identity and isometry give H^m=H^n in P⊗dt there. Glue H on predictable stochastic intervals: indicators of (\(\sigma _n\),\(\sigma _{n+1}\)] are predictable because 1\_{t≤σ} is left-continuous and adapted. After countably many null sets are removed, H has locally finite square energy and M=M₀+∫H dB holds indistinguishably. Integer horizons give the half-axis version. This does not claim finite expected global square energy for every L¹ martingale.

## 7. Transfer of Representation Under Equivalent Weights

<a id="t-br-transfer"></a>

On finite T let the original filtration be the usual natural Brownian filtration, with Q equivalent to P through a strictly positive density \(Z_T\). If N is a true Q-martingale with Q-integrable terminal value, Bayes gives \(Y_t\)=\(Z_tN\)\_t=\(E_P\)[\(Z_TN\)\_T|\(\mathcal F_t\)]. Thus Y is a true P-martingale with P-integrable terminal value. Section 6 makes Y and Z continuous and locally represents dY=h·dB and dZ=Zθ·dB. Z has a positive minimum on each compact path. Apply Chapter 32’s time-space Itô formula to Y/Z, after localization, to obtain

\[ dN_t=H_t\cdot dB_t-H_t\cdot\theta_t\,dt=H_t\cdot d\widetilde B_t,\qquad H_t=\frac{h_t}{Z_t}-N_t\theta_t. \]

The local square energies of h and θ are finite, and Z⁻¹ and N are bounded on compact paths, so H has legitimate local energy. Equivalence transfers pathwise null sets between P and Q. Section 1 has already proved that B̃ is Q-Brownian, so the last integral is independently defined. To justify this integral identity, localize the square energies of H and θ and choose predictable simple approximations to H whose dt square error tends to zero in P-probability; finite-horizon equivalence transfers this to Q. Chapter 31’s localized isometry and maximal estimates give ucp convergence of the corresponding integrals under both measures, while Cauchy–Schwarz controls the drift-integral error. Simple integrals satisfy the decomposition term by term; only these limits justify the final identity, rather than a formal replacement of differentials. For a local Q-martingale first stop to true martingales, then glue using Q-isometry or its localized version. It is not assumed that F is B̃’s own natural filtration.

Conversely, take any strictly positive terminal density L in the natural Brownian filtration, with E L=1. Section 6 gives a continuous version of \(Z_t\)=E[L|\(\mathcal F_t\)]. It cannot hit zero by T: if τ is the first hit, closed-martingale sampling gives E[L1\_{τ≤T}]=E[Z\_τ1\_{τ≤T}]=0; strict positivity of L forces P(τ≤T)=0. Thus Z has a positive compact minimum. Represent dZ=h·dB and put θ=h/Z. Chapter 32’s linear-equation uniqueness, or Itô applied to log, identifies Z=𝓔(∫θ·dB). This necessary representation does not make Novikov necessary.

There is a calculable counterexample to omitting the filtration restriction. Let C be another Brownian motion independent of B and observe the usual natural filtration of (B,C). B remains Brownian. If C=∫H dB, covariation with every coordinate B^i gives ∫\(H_i\) ds=[C,B^i]=0, hence H=0 almost everywhere and [C]=0, contrary to [C]\_t=t. Alternatively, revealing \(B_T\) at time zero leaves the original path law unchanged, but E[\(B_T\)|F₀]=\(B_T\)≠0, so B is no longer a Brownian martingale in the enlarged filtration. The examples separately change representation capacity and conditional fairness; neither justifies a vague assertion that observation changes reality.

## 8. Dyadic Stopping-Time Embedding Without Extra Initial Randomness

<a id="t-br-embedding"></a>

The precise theorem is this: for a real probability μ with ∫x μ(dx)=0 and v=∫x² μ(dx)<∞, there is an almost surely finite stopping time τ in the usual natural filtration of one-dimensional standard Brownian motion such that B\_τ has law μ, Eτ=v, and stopped B is UI. This embeds a specified law, not a pathwise identity with an arbitrary preassigned variable. No SDE or future BDG theorem is assumed.

Choose a deterministic nondecreasing quantile g:(0,1)→R with Lebesgue law μ. For each dyadic interval \(I_w\) of length 2⁻ⁿ, let \(m_w\) be its average. The parent mean is the average of the two child means, with \(m_{w0}\)≤\(m_w\)≤\(m_{w1}\); the distances to the two endpoints agree, say \(d_w\). For the dyadic σ-algebra \(D_n\) put \(X_n\)=E[g|\(D_n\)]. Dyadic step functions are dense in L², and conditional expectation contracts, so for a \(D_N\)-measurable step q and n≥N, ||\(X_n\)−g||₂≤2||g−q||₂. Hence \(X_n\)→g in L². The interval (0,1) only constructs a deterministic mean table; no U is inserted into Brownian F₀.

If \(d_w\)=0, the two half-interval means agree. For u in the left half and v in the right half, g(v)−g(u)≥0; its double integral is the difference of the two means times the interval lengths, hence zero. Almost every such difference vanishes, and Fubini makes g almost everywhere constant on \(I_w\). All descendant means are therefore equal; the node can be absorbed without further coin tossing. This monotonicity step prevents the gap of equal current means hiding later branching.

Start with τ₀=0 and B₀=m\_∅=0. After arriving at node w at \(\tau _n\), if \(d_w\)>0 wait until B first hits \(m_{w0}\) or \(m_{w1}\); call this \(\tau _{n+1}\) and select the child according to the hit endpoint. If \(d_w\)=0 keep \(\tau _{n+1}\)=\(\tau _n\). Node events lie in \(\mathcal F_{\tau _n}\); continuous hitting times and finite event splitting make \(\tau _{n+1}\) a stopping time. Chapter 26 proved Brownian strong Markov independently. Conditional on \(\mathcal F_{\tau _n}\), the subsequent Brownian displacement is therefore a fresh standard Brownian motion.

The waiting time needs its exact mean. Brownian exit σ from [−d,d], starting at zero, is almost surely finite: fixed blocks have a positive probability of displacement exceeding 2d, giving a geometric tail. B^{σ} is bounded, so optional sampling gives E B\_σ=0 and equal probabilities of the two endpoints. Sampling B²−t at σ∧k yields E(σ∧k)=E \(B_{\sigma ∧k}\)²≤d². Monotone and bounded convergence then give Eσ=d². This verifies finite stops, fair transitions and the time cost without assuming integrability before using unbounded sampling.

Inductively \(B_{\tau _n}\) has the law of \(X_n\). At absorbed nodes identical descendant values are combined with the correct total probability; no new random bits are required after absorption. The conditional waiting mean and conditional square increment both equal \(d_w\)². Telescoping over levels gives E\(\tau _n\)=E \(X_n\)²≤v. Thus \(\tau _n\)↑τ, Eτ=v, and τ is almost surely finite. Brownian continuity gives \(B_{\tau _n}\)→B\_τ almost surely; L² convergence \(X_n\)→g gives convergence of their laws to μ, so B\_τ has law μ. The identity Eτ=v follows from monotone convergence of times and the proved L² approximation, rather than passing square expectations before establishing UI.

For fixed n the stopped path stays between the minimum and maximum node values of a finite tree, so B^{\(\tau _n\)} is a bounded closed martingale. Doob gives E \(sup_{t≤\tau _n}\)|\(B_t\)|²≤4E|\(B_{\tau _n}\)|²≤4v. Fatou and \(\tau _n\)↑τ yield E \(sup_{t≤\tau }\)|\(B_t\)|²≤4v, making all stopping values of B^{τ} UI and bounded in L². The increasing limit τ is a stopping time in the same usual natural filtration. This proves all assertions.

## 9. Higher Time Moments for the Embedding

<a id="t-br-embedding-moments"></a>

If p≥1 and ∫|x|^{2p}μ(dx)<∞, the same τ satisfies Eτ^p≤\(C_p\)∫|x|^{2p}μ(dx), with \(C_p\) depending only on p. First prove this for finite-level \(\tau _n\) to avoid assuming the moment being sought. Its stopped path is bounded by a deterministic \(K_n\), so \(\tau _n\) is no later than exit from [−\(K_n\)−1,\(K_n\)+1]. That exit time has a geometric time-block tail: a displacement larger than twice the interval length in one fixed block has a uniformly positive probability. All positive moments are therefore finite.

Write \(V_n\)=\(sup_{t≤\tau _n}\)|\(B_t\)|. For u>0 the event {\(\tau _n\)>2u,\(V_n\)≤δ√u} forces |\(B_{2u}\)−\(B_u\)|≤2δ√u. The event {\(\tau _n\)>u} belongs to \(\mathcal F_u\) and the future increment is independent, so

\[ P(\tau_n>2u)\le P(V_n>\delta\sqrt u)+q_\delta P(\tau_n>u),\qquad q_\delta=P(|G|\le2\delta),\ G\sim N(0,1). \]

Multiply by p u^{p−1} and integrate. The tail-integral identity, using nonnegative Tonelli rather than an unchecked interchange, gives the following inequality. Choose δ small enough that q\_δ<2⁻ᵖ. Doob’s L^{2p} inequality applies to the bounded closed martingale B^{\(\tau _n\)}: first use Chapter 15 on finite grids, then refine by continuity and monotone convergence and increase the time horizon. Finally apply Jensen to the conditional mean \(X_n\).

\[ (2^{-p}-q_\delta)E\tau_n^p\le\delta^{-2p}EV_n^{2p}\le\delta^{-2p}\left(\frac{2p}{2p-1}\right)^{2p}E|X_n|^{2p}\le C_{p,\delta}E|g|^{2p}. \]

Let n tend to infinity; monotone convergence of \(\tau _n\)^p gives the desired bound. For p=1 the preceding section gives the sharper equality Eτ=v. The argument uses one-step control from independent Gaussian increments and the already proved Doob inequality. It invokes neither Chapter 34’s BDG nor a general moment theorem for all continuous local martingales.

### Dependencies and Scope

Sections 1–2 use Chapter 31’s brackets/stopped integrals and Chapter 32’s product and C² formulas. Sections 3–4 use Chapter 16’s closed-martingale sampling, Chapter 31’s quadratic brackets and the main text’s Lévy characterization. Section 5 uses Chapter 23’s measurable C-space, Chapter 14’s Gaussian uniqueness, T-LP completeness and this chapter’s Girsanov. Sections 6–7 use the main closed-space proof and established measurability/conditional expectation, not a future martingale problem. Sections 8–9 use Chapter 26’s dedicated Brownian strong Markov theorem and Chapter 15’s Doob inequality, not Chapter 25’s Donsker as a proof input.
