# Chapter 49: When a Random Outcome Is a Measure

Place points on an interval, each carrying a small amount of mass. When their number doubles, halve the mass carried by each. The record can still be drawn as dots, but counting how many dots occur no longer explains its limit.

\[ \mu_n=\frac1n\sum_{k=1}^n\delta_{k/n},\qquad \mu_n f=\frac1n\sum_{k=1}^nf(k/n)\longrightarrow\int_0^1f(x)\,dx\quad(f\in C[0,1]). \]

Every record charges only finitely many locations, whereas its limit charges no singleton. No missing point needs to be recovered: the amount carried by a point has changed. The integer-preservation argument of Chapter 48 cannot determine the limit of these weighted records. Continuous tests still read meaningful amounts of mass; they need a larger state space.

## 49.1 Atoms Have Not Fallen Outside the Calculation

<a id="mass-from-atoms"></a>

The limit above is merely a Riemann sum, with no randomness, but it already exposes the state-space problem. A space containing only integer counting measures cannot even accommodate this deterministic sequence. Positive real weights allow atoms, continuous densities, or mixtures of both. A random probability distribution is the special case with total mass one.

We do not replace the definition by “having a density.” A density may not exist and depends on a reference measure. What survives is nonnegative, countably additive mass assigned to sets. Throughout, E is a locally compact second-countable metric space, all measures are Borel, and \(\mathcal M_+(E)\) denotes the nonnegative Radon measures finite on compact sets. Radon includes inner and outer regularity; local finiteness does imply that regularity here, as proved in [T-RIESZ](../foundations/t-riesz.md#riesz-space).

These space assumptions provide finite observation windows around every location and enough countable observations to organize measurability. They make no assertion about arbitrary non-locally-compact spaces. Total mass may be infinite; mass in each compact window must be finite.

## 49.2 First Make Every Reading a Random Variable

<a id="mass-evaluations"></a>

If an experiment leaves \(\Xi\), we should at least be able to ask for \(\Xi(A)\). A random Radon measure is therefore a map into \(\mathcal M_+(E)\) for which \(\omega\mapsto\Xi_\omega(A)\) is measurable for every Borel A, with infinity allowed. Each realization must first be a measure. Choosing an unrelated random variable for each A does not make countable additivity hold simultaneously.

There is a usable test for this simultaneous structure. Fix a compact exhaustion \(K_m\subset\operatorname{int}K_{m+1}\), choose \(\chi_m\in C_c^+(E)\) with \(\chi_m\ge1\) on \(K_m\), and take a countable family \((f_j)\) of nonnegative continuous tests uniformly dense within common larger compact supports, including the cutoffs. Measurability of every \(\Xi f_j\) suffices for every evaluation to be measurable, and conversely.

The reason does not use integer masses. Approximate indicators of open sets from below by continuous compactly supported functions. Inside a relatively compact window, finite mass permits subtraction and a π–λ argument for every Borel set; then exhaust the space. When reconstructing a measure from positive linear readings, first remove one null set for a countable rational linear family, extend using local bounds, and apply Riesz representation. This avoids incompatible versions chosen separately for uncountably many tests. See [T-RADON-SPACE](../foundations/t-radon-space.md#radon-evaluation) for the details.

## 49.3 Closeness Seen Through Finite Windows

<a id="mass-vague"></a>

The Riemann sums suggest following \(\mu f\), rather than individual atoms. On general E, first restrict to \(f\in C_c(E)\). This defines vague convergence: \(\mu_n\xrightarrow{v}\mu\) exactly when every such integral converges. It allows changes outside each fixed observation window to remain unrecorded.

\[ d_v(\mu,\nu)=\sum_{j=1}^{\infty}2^{-j}\bigl(1\wedge|\mu f_j-\nu f_j|\bigr). \]

The countable tests separate measures, so this is a metric. If their coordinates converge, cutoff coordinates first bound mass uniformly on each compact window. Uniform approximation with a common support then extends convergence to every continuous compactly supported test. Conversely, the tail of the series controls the metric. Local mass bounds are essential: a countable dense family of functions alone does not control integration errors.

## 49.4 How Local Bounds Produce a Limit Measure

<a id="mass-polish"></a>

Suppose a family has a uniform finite bound on mass in every \(K_m\). Extract subsequences successively for the countable readings, then extend the coordinate limits to arbitrary tests of fixed compact support using those bounds. The resulting L is positive and linear, and bounded on each fixed support. Riesz representation gives a unique \(\mu\in\mathcal M_+(E)\) with \(Lf=\mu f\). The family is therefore vaguely relatively compact.

Conversely, every continuous reading \(\mu\chi_m\) is bounded on a vaguely compact set, so local masses are bounded. Relative compactness is exactly local mass control. A \(d_v\)-Cauchy sequence has finite limits in all coordinates; the preceding argument gives a convergent subsequence, and the Cauchy property gives convergence of the whole sequence. The metric is complete. Truncating to finite windows, concentrating mass in fine cells at points of a countable dense set, and approximating cell masses by nonnegative rationals gives a countable dense family. Thus \(\mathcal M_+(E)\) is Polish.

The evaluation σ-algebra equals the Borel σ-algebra of this topology. These are compatible constructions, rather than competing definitions of a random measure. [T-RADON-SPACE](../foundations/t-radon-space.md) supplies every step concerning completeness, separability, positive extension, and evaluations.

## 49.5 Integer Measures Form One Layer

<a id="mass-integers"></a>

The space \(\mathcal M_p(E)\) of Chapter 48 is closed in \(\mathcal M_+(E)\). Under vague convergence of integer measures, continuity balls retain integer masses, and shrinking those balls recovers integer atoms. The weighted example does not contradict this result: \(\mu_n\) does not belong to the integer space for n>1. The hypotheses describe different sequences.

Finite weighted atomic measures are dense in the entire nonnegative Radon space. Atomicity is not closed: \(\mu_n\) approaches diffuse length measure. Nor is non-atomicity closed: \(n\mathbf1_{(0,1/n)}(x)\,dx\) approaches \(\delta_0\) on the real line. The same continuous tests accommodate both directions. The topology preserves readings of mass, rather than a prescribed granular or continuous appearance.

## 49.6 Random Mass Requires Joint Readings

<a id="mass-laplace"></a>

Now let the measure be random. Its Laplace functional remains \(L_\Xi(f)=\mathbb E e^{-\Xi f}\), for \(f\in C_c^+(E)\). Substituting \(f=\sum a_jf_j\), \(a_j\ge0\), gives the joint Laplace transform of \((\Xi f_1,\ldots,\Xi f_r)\). The nonnegative-vector uniqueness proof in Chapters 13 and 48 does not require integer values: exponentiation sends the vector into a compact cube, where Bernstein polynomials identify all continuous tests.

The countable readings generate the Borel σ-algebra, so equality of all Laplace readings is equivalent to equality in law of random measures. Allowing nonnegative linear combinations is crucial. Separate marginal distributions for a few locations or regions do not supply the joint structure. No moment assumption or finite mean mass is needed.

## 49.7 A Diffuse Mean Does Not Make Each Realization Diffuse

<a id="mass-mean"></a>

Let U be uniform on [0,1], and compare \(\Xi=\delta_U\) with the deterministic measure \(\eta=dx|_{[0,1]}\). Their mean measures agree, but every realization of the former is an atom, whereas every realization of the latter is diffuse. Strict convexity gives different Laplace readings for any nonconstant nonnegative continuous f.

\[ \mathbb E\Xi(A)=\eta(A),\qquad \mathbb E e^{-f(U)}>\exp\!\left\{-\int_0^1f(x)\,dx\right\}. \]

Tonelli makes the mean \(\nu(A)=\mathbb E\Xi(A)\) a measure, but it need not be locally finite. If Z is positive and finite almost surely with infinite expectation, then \(\Xi=Z\delta_0\) is Radon in every realization, while its mean puts infinite mass at one point. Local finiteness concerns realizations; finite mean mass is an additional integrability condition.

## 49.8 Before Passing Transforms to the Limit

<a id="mass-law-limits"></a>

A family of random-measure laws is tight in the vague space exactly when its masses in every compact window are uniformly tight. One direction uses bounded cutoff readings on compact subsets of the measure space. For the other, allocate exceptional probability \(\varepsilon2^{-m}\) to window m, choose mass bounds, and combine deterministic local compactness with the union bound.

For an already existing random Radon measure \(\Xi\), convergence \(\Xi_n\Rightarrow\Xi\) is equivalent to convergence of the Laplace readings for all nonnegative continuous compactly supported f. Necessity uses a bounded continuous map. Sufficiency still needs tightness. With \(\chi\ge1_K\),

\[ \mathbb P\{\Xi_n(K)>R\}\le\frac{1-L_{\Xi_n}(a\chi)}{1-e^{-aR}}. \]

First make a small enough for the limiting numerator to be small, then take R large, and finally handle finitely many initial n. Local tightness and Prokhorov give subsequences; the functional uniquely identifies every subsequential limit. Full details and the random continuity-set version appear in [T-RANDOM-MEASURE-LIMITS](../foundations/t-random-measure-limits.md#mass-law-convergence). To claim that an abstract functional is a limit, one must additionally prove that it represents a random Radon measure. Existence of the limit object is a substantive hypothesis.

## 49.9 Where Mass Can Go Beyond the Windows

<a id="mass-weak-vague"></a>

On the real line, \(\delta_n\xrightarrow v0\): every fixed compact support eventually misses the atom. Yet every measure has total mass one and the limit has mass zero. In the open interval E=(0,1), starting at n≥2, likewise \(\delta_{1/n}\xrightarrow v0\), since a compact subset stays a positive distance from the boundary. If the space is [0,1] instead, the limit is \(\delta_0\). The state space and its boundary belong to the statement.

For finite nonnegative measures, weak convergence in this chapter means convergence against every \(C_b(E)\) test. It is equivalent to vague convergence together with convergence of total masses to the finite limiting mass. Necessity is immediate. For sufficiency, choose a cutoff χ with small \(\mu(1-\chi)\). Convergence of total masses and of \(\mu_n\chi\) makes \(\mu_n(1-\chi)\) small too; split any bounded continuous f into χf and its tail.

## 49.10 Random Probabilities Must Retain Their Total Mass

<a id="mass-normalization"></a>

A random probability measure \(P_n\) takes values in \(\mathcal P(E)\). There are two probability levels: each realization is a probability on E, while its outer law is a probability on the measure space. If its vague distributional limit P also has total mass one almost surely, then \(P_n\Rightarrow P\) in the weak probability space as well. The weak topology on \(\mathcal P(E)\) is exactly the vague subspace topology. The limit must remain in that subspace.

For general finite random mass, a safe normalization hypothesis is joint convergence \((\Xi_n,\Xi_n(E))\Rightarrow(\Xi,\Xi(E))\), with all total masses positive and finite, including the limit. It then yields weak distributional convergence of \(\Xi_n/\Xi_n(E)\) to \(\Xi/\Xi(E)\). Local convergence alone is insufficient: \(\delta_0+\delta_n\xrightarrow v\delta_0\), whereas the local limit after normalization is \(\delta_0/2\), rather than the normalized limit \(\delta_0\).

## 49.11 Spreading Mass Rather Than Moving a Point

<a id="mass-smoothing"></a>

Let one unit of mass at x be distributed across another space F according to a probability kernel K(x,dy). This is not one random draw: the whole unit is spread proportionally, with \((\mu K)(A)=\int K(x,A)\mu(dx)\). Thus \((\mu K)f=\mu(Kf)\). This is kernel smoothing; even a single input atom can produce diffuse output.

For random \(\Xi\) and fixed K, monotone approximation proves measurability of \(\omega\mapsto\Xi_\omega K(A)\) and gives \(\mathbb E(\Xi K)=(\mathbb E\Xi)K\), with infinity allowed. For the output to be a random Radon measure on F, one additionally needs \(\Xi K(K_m^F)<\infty\) almost surely simultaneously for a countable compact exhaustion. A probability kernel alone does not ensure this: sending every integer point on the real line to zero destroys local finiteness.

If K depends on a random environment Z, the map is \((z,\mu)\mapsto\int K(z,x,A)\mu(dx)\). [T-MASS-KERNELS](../foundations/t-mass-kernels.md#mass-kernel-measurable) proves joint measurability from rectangular indicators and the functional monotone-class theorem. Separate measurability for each fixed z does not suffice. Nor may the mean generally be written as \((\mathbb E\Xi)(\mathbb E K)\).

## 49.12 What Smoothing Recovers

<a id="mass-convolution"></a>

On Euclidean space, let \(K_\varepsilon(x,dy)=\rho_\varepsilon(y-x)dy\), where ρ is nonnegative, continuous, compactly supported, and integrates to one, with \(\rho_\varepsilon(z)=\varepsilon^{-d}\rho(z/\varepsilon)\). Smoothing any locally finite μ gives a locally continuous density \(y\mapsto\int\rho_\varepsilon(y-x)\mu(dx)\). A compact y-window uses only a slightly larger compact x-window, so domination and uniform continuity prove continuity.

As \(\varepsilon\downarrow0\), Kεf approaches f uniformly within a common compact support, giving \(\mu K_\varepsilon\xrightarrow v\mu\), realization by realization. Total variation convergence does not follow: if \(\mu=\delta_0\), every smoothed measure gives zero mass to the singleton zero, while the limit gives it mass one. Fine smoothing approximates integral readings without preserving singularity. This concerns general random mass, rather than merely renaming the Poisson marking theorem.

## 49.13 Independent Scattering Still Produces Points

<a id="mass-scattering"></a>

Now perform a different experiment. Given an integer point measure \(\xi=\sum_i\delta_{x_i}\), independently draw \(Y_i\sim K(x_i,\cdot)\) for every occurrence and output \(S_K\xi=\sum_i\delta_{Y_i}\). This is independent point scattering. Multiplicities at one location receive separate draws. Conditional on ξ, the smoothing \(\xi K\) is the mean of the scattered configuration, rather than that configuration itself.

\[ \mathbb E[e^{-(S_K\xi)f}\mid\xi]=\prod_i\bigl[1-K(1-e^{-f})(x_i)\bigr],\qquad \mathbb E[S_K\xi(A)\mid\xi]=\xi K(A). \]

Measurable enumeration and kernel randomization from Chapter 10 give the conditional construction. If the smoothed intensity is finite on each target compact, finite conditional expectation makes the scattered configuration locally finite; a countable exhaustion unifies null sets. More precisely, in a fixed window the independent Bernoulli hits are finite almost surely exactly when their probabilities are summable, with Borel–Cantelli supplying the converse. This use of scattering differs from the independently scattered property of independent masses on disjoint sets; scattering a general input need not have that property.

## 49.14 When Every Source Is Small

<a id="mass-scattering-bound"></a>

The bridge from scattering to Cox laws is not visual randomness. Each source must be small within the observation window. Allow a random input \(\Xi_n\) with arbitrary dependence among its points; displacements are independent conditional on the input. Put \(\Lambda_n=\Xi_nK_n\), and require \(\epsilon_n(B)=\sup_xK_n(x,B)\to0\) for every compact B. This dissipativity condition prevents even one source from retaining a fixed positive chance of hitting a given window.

\[ d_{\rm TV}\!\left(\mathcal L(S_{K_n}\Xi_n|_B\mid\Xi_n),\operatorname{PRM}(\Lambda_n|_B)\right)\le\min\left\{1,\sum_iK_n(x_i,B)^2\right\}\le\min\{1,\epsilon_n(B)\Lambda_n(B)\}. \]

For each source, use the Bernoulli–Poisson coupling of Chapter 13, sharing the conditional location when a hit occurs. The error per source is at most the squared hit probability. A union bound over independent couplings controls the whole configuration in the window, not merely its count. Infinitely many sources are handled by finite truncations and summable window tails. If the smoothed masses in B are uniformly tight, the expectation of the bound tends to zero; bounded expectations are unnecessary.

## 49.15 Why a Scattering Limit Can Retain Random Intensity

<a id="mass-cox-criterion"></a>

This yields a substantive limit theorem. Under dissipativity and local finiteness, if \(\Lambda_n\Rightarrow\Lambda\) in the general Radon space, then \(S_{K_n}\Xi_n\Rightarrow\operatorname{Cox}(\Lambda)\). Its Laplace functional is

\[ \mathbb E\exp\{-\Lambda(1-e^{-f})\}. \]

Conditional coupling makes scattering asymptotically indistinguishable, on each window, from a Poisson configuration with random intensity Λₙ. Continuous compactly supported tests pass the convergence of Λₙ to its displayed functional. Ordinary Poisson law results directly only when Λ is deterministic. Many independent displacements can erase an individual point’s special contribution while retaining a common environment.

There is converse information: the scattered laws are tight exactly when the smoothed random-measure laws are tight. Conditional on the input, a window count has variance at most its mean m; for large m its probability of falling below m/2 is at most 4/m. Huge smoothed mass therefore cannot remain hidden by scattering. Every scattered subsequential limit is Cox with the corresponding smoothed subsequential limit, and the Cox law uniquely determines the law of its directing measure. This last identification requires Laplace uniqueness on a short parameter interval; [T-SCATTERING](../foundations/t-scattering.md#scattering-cox) proves the extension and the precise two-way criterion.

The criterion also answers a question without spatial motion: a locally finite point process is Cox exactly when, for every positive integer n, it is an independent 1/n-thinning of some larger locally finite point process. In one direction, multiply the directing intensity by n. In the other, view thinning as subprobability scattering, with dissipativity at most 1/n. The fixed output law makes smoothed intensities tight, producing a directing random measure. This characterizes a probability structure, rather than merely approximating one Poisson example.

## 49.16 When Long-Range Averaging Becomes Constant

<a id="mass-averaging"></a>

Consider a fully provable stationary averaging version. Let \(\Xi\) be stationary on the real line with \(\mathbb E\Xi[0,1)<\infty\), and spread every location uniformly across [x−R,x+R]. The smoothed measure has density \(q_R(y)=\Xi([y-R,y+R])/(2R)\), with endpoint conventions immaterial for dy. Apply Chapter 41 to the translated unit-window masses to get \(\Xi([-R,R])/(2R)\to C\) in L¹, where C is nonnegative, integrable, and \(\mathbb EC=\mathbb E\Xi[0,1)\).

For fixed y, the symmetric difference of the two windows has length at most 2|y|, so its expected mass divided by 2R tends to zero. Hence \(q_R(y)\to C\) in L¹. Integrating against compactly supported tests and using the stationary mean density gives \(\Xi K_R\to C\,dy\) vaguely in probability. C is invariant under every real translation; it is constant if the stationary measure law is ergodic under all translations. The dedicated proof treats two-sided averages, common tests, and invariant versions in [T-SCATTERING](../foundations/t-scattering.md#scattering-averaging).

## 49.17 How a Lattice Scatters to Poisson

<a id="mass-lattice"></a>

Take the random-phase lattice \(\Xi=\sum_{k\in\mathbb Z}\delta_{k+U}\), with U uniform on [0,1). Every realization is highly regular, but the count in a window of length 2R differs from 2R by at most two, so smoothing approaches dy. Independent uniform displacements satisfy \(\epsilon_R(B)\le |B|/(2R)\). The criterion therefore proves convergence of scattering to a unit-intensity Poisson process. It explains why a regular input can acquire a Poisson limit under a particular independent long-range perturbation.

If spacing one or one-half is selected randomly before choosing a uniform phase, the limiting smoothed density is randomly one or two. Scattering then approaches a mixed Poisson law, not a Poisson law of intensity three-halves. If all points share one displacement, they remain a translated lattice and the independent-scattering conclusion fails completely. Each source must lose its concentrated contribution to a window, and displacements must be conditionally independent. Broad marginal displacement laws alone do not suffice.

## 49.18 Approximating Any Mass by Fine Random Grains

<a id="mass-poissonization"></a>

General mass cannot be enumerated as unit points, but a different construction approximates it. Given a random Radon measure Λ, on an enlarged space let \(N_n\mid\Lambda\sim\operatorname{PRM}(n\Lambda)\), and put \(\widehat\Lambda_n=N_n/n\). This is a weighted measure obtained by conditional Poissonization, not independent displacement of the atoms of Λ.

\[ \mathbb E[\widehat\Lambda_n f\mid\Lambda]=\Lambda f,\qquad \operatorname{Var}(\widehat\Lambda_n f\mid\Lambda)=\frac{\Lambda(f^2)}n. \]

For each test, truncate the conditional Chebyshev bound to Λ(f²)≤A, take n to infinity, and then A to infinity. This gives convergence of the reading in probability. Countable tests and the metric tail give vague convergence in probability of the whole measure. Local finiteness of the mean intensity is unnecessary. Integer structure has left the state space, while point-process tools still construct approximations to general random mass.

## 49.19 One Arrival Can Leave a Whole Daughter Measure

<a id="mass-clusters"></a>

Generalize a source further. Parent locations form a Poisson random measure of σ-finite intensity a; each occurrence at x independently carries a random nonnegative Radon measure ζ with probability kernel Q(x,dζ). Add all daughter mass: \(\Psi=\sum_i\zeta_i\). A daughter may be a cluster of points, a density, or length carried by a line. The Polish and evaluation structures of the random-measure space now provide a legitimate mark space for this kernel.

\[ L_\Psi(f)=\exp\left\{-\int\!\int(1-e^{-\zeta f})\,Q(x,d\zeta)\,a(dx)\right\}. \]

First restrict the parent space and daughter mass; finite sums give the formula directly. Nonnegative monotone limits restore all occurrences. The formula permits infinite output at this intermediate stage, but that output is not yet a random Radon measure. Local finiteness remains a separate question.

## 49.20 The Actual Boundary Between Finite and Infinite Mass

<a id="mass-zero-infinity"></a>

For a fixed compact B, the Poisson sum of daughter measures is finite on B almost surely exactly when the following integral is finite. If it diverges, the sum on B is infinite almost surely:

\[ \int\!\int(1\wedge\zeta(B))\,Q(x,d\zeta)\,a(dx)<\infty. \]

Split sources into those with mass exceeding one and those with mass at most one. There are finitely many of the former; the latter have finite expected total mass. Conversely, 1−exp(−z) is comparable to 1∧z on the nonnegative half-line. Divergence makes the expected exponential of the total mass zero, forcing infinite mass almost surely. Applying this to a countable compact exhaustion gives a necessary and sufficient condition for the random Radon construction.

Finite mean \(\int\!\int\zeta(B)Q(x,d\zeta)a(dx)<\infty\) is sufficient but unnecessary. Finitely many parents, each carrying finite random mass of infinite mean, still give locally finite realizations. This 0–∞ statement is a criterion for a given Poisson parent intensity and independent marks, not a universal zero–one law for arbitrary dependent clusters. See [T-MASS-CLUSTERS](../foundations/t-mass-clusters.md#cluster-finiteness) for the proof, truncation limits, and mean formula.

## 49.21 Continuous-Sized Mass Can Have Independent Increments

<a id="mass-gamma"></a>

An important example places Poisson points on \(E\times(0,\infty)\) with intensity \(\theta H(dx)s^{-1}e^{-s}ds\), where θ>0 and H is a Radon probability. Replace (x,s) by mass \(s\delta_x\) and add to obtain Γ. Infinitely many small-s points occur, but the truncated mass integral is finite, so Γ has finite total mass almost surely. Disjoint spatial regions use disjoint Poisson inputs, giving independent masses.

\[ \mathbb E e^{-\Gamma f}=\exp\left\{-\theta\int\log(1+f(x))\,H(dx)\right\},\qquad \Gamma(A)\sim\operatorname{Gamma}(\theta H(A),1). \]

The identity \(1-e^{-as}=\int_0^a s e^{-us}du\) and Tonelli give the logarithm. A zero shape denotes zero mass. Total mass is a positive Gamma(θ,1) variable, so normalization is legal. On a finite partition, normalized independent Gamma variables give the Dirichlet vector of Chapter 44; hence \(\Gamma/\Gamma(E)\) is the Dirichlet random probability with parameter θH. The new construction uses random mass directly, rather than repeating the predictive proof. Γ is a Gamma random measure: independent scattering of mass is not exclusive to integer Poisson counts.

## 49.22 Line Mass Can Average to Area

<a id="mass-lines"></a>

Parameterize unoriented lines in the plane by \(\ell_{\vartheta,r}=\{x:x\cdot(\cos\vartheta,\sin\vartheta)=r\}\), with \(0\le\vartheta<\pi\) and \(r\in\mathbb R\). On this parameter space take a Poisson random measure of intensity \((c/\pi)d\vartheta\,dr\), each occurrence carrying one-dimensional length measure along the line. The sum Λ is a random Radon measure of line length.

A bounded disk meets only finitely many parent lines, ensuring local finiteness. Parameterizing integration along each line proves measurability. For each fixed angle, normal and tangential coordinates have Jacobian one, and Tonelli gives

\[ \mathbb E\Lambda f=\frac c\pi\int_0^\pi\!\int_{\mathbb R}\!\int_{\ell_{\vartheta,r}}f(x)\,d\mathcal H^1(x)\,dr\,d\vartheta=c\int_{\mathbb R^2}f(x)\,dx. \]

Every realization is carried by countably many lines and is singular with respect to area, yet its mean is c times area. Conditional on Λ, placing \(\operatorname{PRM}(\rho\Lambda)\) gives a Cox point process clustered along random lines. Its mean intensity is ρc times area, which does not make it an ordinary planar Poisson process. Line processes, random mass, and point processes retain different levels of information.

## 49.23 Clusters and Cox Laws Are Different

<a id="mass-cluster-cox"></a>

If each parent first carries a random intensity measure and then independently generates Poisson daughters with that intensity, their superposition is Poisson conditional on all parents and intensities. If the intensity sum is locally finite, the result is Cox. This is a conditional structural theorem; local finiteness cannot be inferred from the picture of daughter points.

The converse fails. At a fixed location x₀ take the parent measure Nδₓ₀, where N∼Poisson(λ) and 0<λ<∞. Each parent occurrence leaves two daughters at x₀, so the daughter measure is 2Nδₓ₀; its count at x₀ is always even and is positive with positive probability. Every nonzero mixed Poisson count has positive probability of equalling one, since that probability is strictly positive conditional on positive intensity. This valid Poisson cluster is therefore not Cox. Clustering, common random intensity, and independent scattering of mass are different mechanisms.

## 49.24 From Finite Truncations to Full Random Mass

<a id="mass-truncation"></a>

In the cluster construction, restrict parents to finite-intensity pieces and retain finite daughter mass within specified windows. Under increasing nonnegative truncations, the local criterion ensures finite limiting mass in every compact window. Every \(C_c^+\) reading then converges monotonically, giving almost-sure vague convergence of the measure. If the criterion fails, mass becomes infinite inside a window; this is not a generalized limit still belonging to the same Radon space.

This differs substantially from the point limits of Chapter 48. Weighted small grains can form diffuse mass, and the Gamma construction permits infinitely many small-weight atoms within a finite window. We control the sum of truncated masses, rather than requiring finitely many supporting points in that window. State space, topology, and integrability have separate responsibilities.

## 49.25 Readings of Mass Outlast the Appearance of Grains

<a id="mass-insight"></a>

The opening Riemann sums did more than make a collection of dots denser. They forced us to release the hidden unit-mass assumption. Continuous tests, measurable evaluations, Riesz representation, and local compactness make the new objects legitimate. Joint Laplace readings identify their laws; retaining total mass permits passage from local closeness to global closeness of random probabilities.

Comparing smoothing with scattering establishes another distinction: the same conditional mean can underlie different random realizations, while dissipativity relates them precisely through Cox limits. Random line length shows that a mean area density does not tell us where mass is carried in each realization. Statements about density need not concern the same level of object.

One observation scheme remains unbuilt. So far we have viewed mass through fixed spatial windows. Looking outward from a random occurrence, or from a location selected according to random mass, may reweight the surrounding environment. An average spatial position and a typical occurrence need not agree. Making that distinction into a legitimate conditional probability requires a further measure decomposition.

## 49.26 Proofs and Scholarly References

<a id="mass-sources"></a>

The complete arguments appear in [T-RADON-SPACE](../foundations/t-radon-space.md), [T-RANDOM-MEASURE-LIMITS](../foundations/t-random-measure-limits.md), [T-MASS-KERNELS](../foundations/t-mass-kernels.md), [T-SCATTERING](../foundations/t-scattering.md), and [T-MASS-CLUSTERS](../foundations/t-mass-clusters.md). The setting is locally compact second-countable metric spaces; Γ, stationary averaging, and line examples have their additional stated assumptions. Arbitrary non-locally-compact measure topologies do not follow automatically.

Kallenberg’s [1973 paper](https://doi.org/10.1007/BF00736004) already specifically studied characterization and convergence of random measures and point processes. The organization here is not presented as his personal discovery sequence. We compare the scope with the third-edition chapter on [random measures, smoothing and scattering](https://doi.org/10.1007/978-3-030-61871-1_31), while rebuilding proofs from this book’s dependencies. For marking, Cox and cluster constructions, another scholarly reference is the [Last–Penrose author manuscript](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf).

The smoothing and scattering results here are the stated kernel constructions, dissipative window total-variation comparison, two-way Cox limit criterion, and finite-intensity stationary averaging on the real line. The cluster 0–∞ criterion is local mass finiteness under Poisson parent structure. General convolution-power averaging, classification of arbitrary constant-velocity flows, spanning and density criteria for general flat processes, and Palm-tree criteria for iterated clusters are not established by these specialized proofs. The observation and conditioning required there are not borrowed as tools here.
