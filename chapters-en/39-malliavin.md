# Chapter 39: How Can We Differentiate Randomness? — Malliavin Calculus

An instrument reports only the square of Brownian position at time one. The position is Gaussian, but the output is not: a positive reading can come from either sign, and readings accumulate near zero. For an output depending on an entire path, perhaps with no explicit formula, how can we decide whether its law has a density? The response we want is not a path’s slope at the next second, but how the output changes when its driving noise is perturbed.

## 39.1 A Squared Reading Reveals Two Different Questions

<a id="noise-output"></a>

Let Z=B₁ and F=Z². For x>0, sum the Gaussian densities at ±√x with their change-of-variable Jacobians. The result is below. There is no atom at zero, yet the density is unbounded there. Having a density and having a smooth density are already different questions.

\[ p_F(x)=\frac{e^{-x/2}}{\sqrt{2\pi x}}\mathbf1_{\{x>0\}}. \]

Direct computation works because one function can be inverted. For a random equation’s output at time t, inverting the whole Brownian trajectory is usually meaningless. The useful clue is that squaring responds weakly near its zero preimage. Can response to noise identify a law without inverting the output?

## 39.2 A Rough Path Can Still Be Shifted

<a id="noise-directions"></a>

Take h∈L²[0,1] and add the same deterministic curve k_h(t)=∫₀ᵗh(s)ds to every path. Chapter 33 proves equivalence with Wiener measure for these shifts, with energy ‖h‖₂². Outside the Cameron–Martin class, path laws can be singular, losing the common weighting needed for response comparisons. This motivates H; Brownian paths themselves are not required to belong to H.

\[ \left.\frac d{d\varepsilon}(B_1+\varepsilon k_h(1))^2\right|_{\varepsilon=0}=2B_1\int_0^1h(s)ds,\qquad \left.\frac d{d\varepsilon}\int_0^1(B_s+\varepsilon k_h(s))ds\right|_0=\int_0^1(1-s)h(s)ds. \]

The first response is represented by \(2B_1\mathbf1_{[0,1]}\), the second by the deterministic function 1−s. These are H-valued sensitivities, not dBₜ/dt. Brownian nowhere differentiability remains intact: the differentiated object and direction have changed.

## 39.3 Gaussian Weight Participates in Integration by Parts

<a id="noise-ibp"></a>

For standard Gaussian ξ and smooth polynomial-growth f, ordinary integration by parts gives E∂ᵢf(ξ)=E[ξᵢf(ξ)]. The measure is not flat volume: differentiating its density leaves ξᵢ. This term may let us transfer derivatives of outputs onto an integrable weight, studying their law before knowing its density.

\[ E[G\langle DF,h\rangle_H]=E\left[F\left(GW(h)-\langle DG,h\rangle_H\right)\right]. \]

Write DF for the Hilbert representation of these responses and first interpret F,G as smooth finite Gaussian-coordinate functions. The formula is coordinatewise integration by parts. Every infinite-dimensional extension must retain this identity; it says much more precisely what is being differentiated.

## 39.4 Recording Directions with a Hilbert Structure

<a id="noise-isonormal"></a>

Use Chapter 23’s real separable H and isonormal family W, with covariance E W(h)W(k)=〈h,k〉, and only σ(W)-measurable variables. For a smooth cylinder F=f(W(h₁),…,W(hₙ)) with polynomial-growth value and derivatives, define the display below. Putting all directions into one finite orthonormal span and using full Gaussian support proves representation independence.

\[ DF=\sum_i\partial_if(W(h_1),\ldots,W(h_n))h_i,\qquad D_hF=\langle DF,h\rangle_H. \]

This is not the ordinary gradient of an H-valued “standard Gaussian point”: Chapter 23 explained why identity covariance does not produce such a sample in infinite dimensions. Yet each cylinder output has a genuine H-valued sensitivity. Differential structure can live in output responses without treating noise itself as a bounded linear functional.

## 39.5 Approximating Values Does Not Approximate Sensitivity

<a id="noise-closed"></a>

An output may only be accessible through finite-coordinate approximations. If Fₙ→F in L², can any limit of DFₙ simply be called DF? The sequence sin(nZ)/n warns otherwise: values tend to zero but the squared derivative norm tends to one half; separated frequencies are not Cauchy. Values and sensitivities must be controlled together.

The key is closability: if Fₙ→0 in Lᵖ and DFₙ→U in Lᵖ(H), 1<p<∞, then U=0. This is a theorem, not a convention. Test the identity of §39.3 against G h. Hölder sends the right side to zero and the left to E[G〈U,h〉]. Dense cylinder tests and countably many separating directions force U=0. The [complete proof](../foundations/t-malliavin.md#malliavin-proof-closed) yields a closed derivative independent of approximation.

## 39.6 What Kind of Differentiability the Sobolev Domain Describes

<a id="noise-sobolev"></a>

\[ \|F\|_{k,p}^p=E|F|^p+\sum_{j=1}^kE\|D^jF\|_{H^{\otimes j}}^p,\qquad \mathbb D^{k,p}=\overline S^{\|\cdot\|_{k,p}},\quad1<p<\infty. \]

Write D∞ for the intersection over all k≥1 and p>1. Closability is what makes this completion an actual space of Lᵖ random variables. It records weak noise derivatives and their integrability, not sample-path time derivatives. Chain and product rules begin on cylinders and extend by graph norms, Hölder and cutoffs. For example, multiplying two \(\mathbb D^{1,2}\) variables need not stay in \(\mathbb D^{1,2}\); \(\mathbb D^{1,4}\) is sufficient.

The closed derivative retains its shift meaning: for F∈D^{1,p}, fixed h and 1<q<p, the Cameron–Martin difference quotient converges in Lᑫ to 〈DF,h〉. The [precise proof](../foundations/t-malliavin.md#malliavin-proof-shift) explains q<p and avoids asserting pathwise Fréchet differentiability of arbitrary representatives.

## 39.7 Transferring a Derivative Requires an Adjoint

<a id="noise-divergence"></a>

To write E〈DG,U〉 as E[G times a random variable], its dependence on G must be bounded by ‖G‖₂. Only then is U in the domain of divergence δ. Hilbert representation gives δU. This is not an automatically available integral for every square-integrable random process.

\[ E[G\delta U]=E\langle DG,U\rangle_H,\qquad \delta(Gh)=GW(h)-\langle DG,h\rangle_H. \]

For deterministic h, δh=W(h); random G needs the extra term. The finite-coordinate formula bounds ‖δU‖₂² by E‖U‖²+E‖DU‖², so \(\mathbb D^{1,2}\)(H) is a sufficient domain. We now need to connect finite-coordinate calculus with every Gaussian output instead of remaining among easy cylinders.

## 39.8 What Remains after Squaring Is More than a Mean

<a id="noise-hermite"></a>

Subtract the mean from Z² to get Z²−1. From Z³ subtract 3Z to make it orthogonal to lower orders. Hermite polynomials systematically remove those projections. Repeated Gaussian integration by parts gives EHₙHₘ=n!1_{n=m}, with H₀=1, H₁=x and H₂=x²−1. The n! normalization will determine derivative and integral constants.

\[ e^{tx-t^2/2}=\sum_{n\ge0}\frac{t^n}{n!}H_n(x),\qquad H_n^\prime=nH_{n-1}. \]

This is not an ordinary Taylor series for arbitrary random variables. Orthogonality is in probabilistic L², not a pointwise path expansion. Different orders are not independent: Z and Z²−1 still depend on the same Z.

## 39.9 Why Wiener Chaos Exhausts L²

<a id="noise-chaos"></a>

In an orthonormal basis of H the noise has countably many independent coordinates. Group Hermite products by total degree, collecting order-n coefficients into a symmetric tensor fₙ. Define Iₙ first on these products and extend by its n! isometry to the whole symmetric tensor space.

\[ F=\sum_{n=0}^\infty I_n(f_n),\quad E|F|^2=\sum_{n=0}^\infty n!\|f_n\|^2,\qquad E[I_n(f)I_m(g)]=\mathbf1_{n=m}n!\langle f,g\rangle. \]

Completeness does not follow from orthogonality alone. Hermite partial sums converge in L² to Gaussian exponentials, whose totality was proved in Chapter 33. A variable orthogonal to every chaos must therefore vanish. [T-GAUSSIAN 1–2](../foundations/t-gaussian.md#gaussian-proof-chaos) establishes this step and basis independence.

## 39.10 Ordered Integrals and Symmetric Kernels Describe the Same Order

<a id="noise-multiple"></a>

For Brownian H=L²[0,T], Iₙ can also be obtained by iterating Chapter 31’s Itô integral over the time simplex and multiplying by n!. The factor is not arbitrary: a symmetric kernel contributes equally on n! orderings, with zero-volume time diagonals.

\[ I_n(f)=n!\int_{0<t_1<\cdots<t_n<T} f(t_1,\ldots,t_n)\,dB_{t_1}\cdots dB_{t_n}. \]

Compare the deterministic exponential’s Picard series with the Hermite generating function, first for pure tensors and then by polarization/isometry. The [full identification](../foundations/t-gaussian.md#gaussian-proof-multiple) does not define divergence first and circularly recover Itô. Chaos order describes Gaussian combinations in outputs, not the number of sample-path time derivatives.

## 39.11 Why Higher Chaos Costs More Derivative Energy

<a id="noise-number"></a>

\[ E\|DF\|_H^2=\sum_{n\ge1}n\,n!\|f_n\|^2,\qquad F\in\mathbb D^{1,2}\ \Longleftrightarrow\ \sum_{n\ge1}n\,n!\|f_n\|^2<\infty\quad(F\in L^2). \]

Differentiation lowers order n but multiplies by n; orthogonality turns this sensitivity cost into an exact series weight. Not every L² output is differentiable: Σₙ≥₁Hₙ(Z)/(n√n!) has finite L² norm but derivative energy Σ1/n diverges. Computable finite-coordinate approximations do not automatically retain derivatives in their limit.

Mix W with an independent copy using \(e^{-t}\) and √(1−\(e^{-2t}\)), then average: the Mehler semigroup multiplies order n by \(e^{-nt}\). Its generator is −N, where N multiplies order n by n, and δD=N on the stated L² domain. OU structure reappears as attenuation of high-order noise response, not a speed change of physical Brownian time. [Coefficients and domains are proved here](../foundations/t-gaussian.md#gaussian-proof-number).

## 39.12 Random Coefficients Change the Isometry

<a id="noise-divergence-bounds"></a>

For U=\(B_T\mathbf1_{[0,T]}\), the coefficient uses information after increments occur. Adjointness gives δU=B_T²−T, not B_T² obtained by pulling out B_T as if deterministic. Its variance 2T² differs from E‖U‖²=T². Divergence permits some nonadapted inputs with new domains and corrections; it does not abolish Itô’s information-order requirement.

On smooth fields D_hδU=〈U,h〉+δ(D_hU). Repeated derivative transfer will need higher sensitivities because of this identity; a single L² estimate cannot simply be reused indefinitely. [Domains and commutation](../foundations/t-malliavin.md#malliavin-proof-divergence) are both established from finite Gaussian integration by parts.

## 39.13 When First Sensitivity Excludes Singular Laws

<a id="noise-absolute"></a>

For scalars a precise first-order result holds: if F∈\(\mathbb D^{1,2}\) and ‖DF‖>0 almost surely, its law is absolutely continuous, without inverse-gradient moments. Slice along one Gaussian coordinate; Sobolev closure makes almost every section absolutely continuous. An absolutely continuous real function has derivative zero almost everywhere on the preimage of a null set: otherwise local inverse-Lipschitz bounds would make that preimage null too.

\[ E\big[\mathbf1_{\{F\in N\}}\|DF\|_H^2\big]=0\quad\hbox{for every Lebesgue-null }N,\qquad \|DF\|_H>0\ \hbox{a.s.}\ \Longrightarrow\ \mathcal L(F)\ll dx. \]

Summing over countably many Gaussian directions gives the identity. The [section and null-set argument](../foundations/t-malliavin-density.md#density-proof-scalar) is complete rather than an appeal to intuition about nonzero derivatives. It excludes singular mass but does not control sharp features of a density.

## 39.14 Covariance Records Independent Output Responses

<a id="noise-covariance"></a>

A vector may report the same information twice. F=(B₁,2B₁) has two coordinates but lies on a line. We must ask whether noise directions can move each output component independently. The Gram matrix of DFᵢ is the Malliavin covariance.

\[ \gamma_F=(\langle DF_i,DF_j\rangle_H)_{i,j\le m},\qquad F=\left(B_1,\int_0^1B_sds\right)\Longrightarrow\gamma_F=\begin{pmatrix}1&1/2\\1/2&1/3\end{pmatrix},\quad\det\gamma_F=1/12. \]

One path can produce a full-rank two-dimensional output. What matters is independence of sensitivity directions, not the number of Brownian paths. For Fᵢ∈∩ₖ\(\mathbb D^{k,2}\), detγ>0 almost surely implies vector absolute continuity: finite-direction Gram matrices eventually have full rank; condition on other coordinates, construct C¹ finite-dimensional sections and use local inverse maps to preserve null preimages. The [full proof](../foundations/t-malliavin-density.md#density-proof-vector) includes the C¹ construction and does not label this the weakest \(\mathbb D^{1,2}\) vector theorem.

## 39.15 Almost-Sure Nondegeneracy Still Allows Sharp Densities

<a id="noise-degeneracy"></a>

Return to the squared reading without recomputing its density. DF=2Z and γ=4Z² are almost surely nonzero but can be arbitrarily small. Those weak-response samples permit the density to accumulate near zero. Nondegeneracy excludes actual loss of direction, not how often near-loss occurs.

Conversely, many derivatives alone do not suffice. Let φ(x)=0 for x≤0 and exp(−1/x²) for x>0. Every derivative is bounded, yet φ(Z) has a zero atom of mass one half: half the samples do not respond at all. Smoothness, full rank and inverse-covariance integrability must therefore be checked separately.

## 39.16 Inverse Covariance Selects the Required Directions

<a id="noise-weights"></a>

To transfer ∂ᵢφ(F) from output coordinates to noise space, find a random direction Uᵢ with 〈DFₖ,Uᵢ〉=δᵢₖ. This is a linear system, not a guessed weight. Invert the Gram matrix to obtain the display; the chain rule turns the output derivative into an inner product, and divergence transfers it off the test.

\[ U_i=\sum_j(\gamma_F^{-1})_{ij}DF_j,\qquad E[(\partial_i\varphi)(F)G]=E[\varphi(F)\delta(GU_i)]. \]

Yet \(\gamma^{-1}\) can be large, and GUᵢ may be outside Domδ. Moment conditions come from this obstacle rather than a theorem’s appearance. If Fᵢ belong to the D∞ space of §39.6 and detγ has every inverse moment, reciprocal cutoffs, chain rules and Hölder keep \(\gamma^{-1}\),Uᵢ in D∞. The [cutoff proof](../foundations/t-malliavin-density.md#density-proof-weights) tracks every derivative and moment.

## 39.17 Repeated Integration by Parts Needs Higher-Order Control

<a id="noise-higher"></a>

After δ(GUᵢ) appears, another round must differentiate that weight. One L² estimate would leave a proof gap here. We establish a sufficient higher-divergence bound: its 2r-th moment is controlled by Hilbert-tensor derivative moments through order 2r, uniformly in finite-coordinate dimension.

Repeated adjointness and commutation remove at least one divergence each time. Only tensor contractions between distinct factors remain, controlled by Cauchy–Schwarz and Hölder. The [finite algorithm and limiting proof](../foundations/t-malliavin.md#malliavin-proof-moments) show δ sends D∞ fields back to D∞. Integration by parts can genuinely be iterated without an unproved optimal inequality as a black box.

## 39.18 Smooth Density Follows from Controlled High Frequencies

<a id="noise-smooth-density"></a>

We can now state the theorem: if components of F belong to D∞, γ is almost surely positive definite and E(detγ)^{-p}<∞ for every p>1, then F has a C∞ density. Insert exp(i〈θ,x〉) into repeated integration by parts. Powers of θ become integrable weights; choosing the largest coordinate gives characteristic-function decay of arbitrary polynomial order.

\[ |\varphi_F(\theta)|\le C_k(1+|\theta|)^{-k},\qquad p_F(x)=(2\pi)^{-m}\int e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta. \]

Fourier inversion and every differentiated integral are absolutely integrable. To avoid assuming density first, add small Gaussian noise, obtain genuine densities and identify p_F by uniform and weak limits. [T-DENSITY 4](../foundations/t-malliavin-density.md#density-proof-smooth) completes the argument. Inverse moments are explicit sufficient conditions, not necessary for every smooth density.

## 39.19 Nondegeneracy Is Not a Uniform Lower Bound

<a id="noise-lognormal"></a>

For F=e^Z, γ=e^{2Z} has no deterministic positive lower bound, yet all inverse moments are finite. F and its noise derivatives also have all positive moments. The theorem gives a smooth density on the whole line, zero on the negative half-line and smoothly attached at zero. What matters is probabilistic/integrability control near degeneracy, not necessarily a uniform pathwise separation.

It also shows that a smooth density need not be strictly positive everywhere. Support, positivity and smoothness remain different questions; the word “nondegenerate” cannot replace all their proofs.

## 39.20 Sensitivity Can Be Computed without an Explicit Solution

<a id="noise-sde"></a>

Consider Xₜ=x+σBₜ+∫₀ᵗb(Xᵣ)dr with deterministic initial state, constant σ≠0 and smooth b having bounded positive-order derivatives; linear growth of b is allowed. Chapter 35 gives existence and uniqueness. Now investigate response to the driving path. Dyadic Brownian interpolation produces ordinary integral equations smooth in finitely many Gaussian coordinates. Differentiate them, use Gronwall and finally closability before removing the grid.

\[ D_sX_t=\sigma\exp\!\left(\int_s^t b^\prime(X_r)dr\right)\mathbf1_{\{s\le t\}},\qquad \gamma_{X_t}\ge\sigma^2t e^{-2\|b^\prime\|_\infty t}. \]

Each fixed t>0 therefore has a smooth density, for example with b=−tanh, without an explicit transition kernel. This is not a restatement of Chapter 35’s existence/uniqueness: it adds regularity of the output law. [All derivative orders, grid limits and nondegeneracy](../foundations/t-malliavin-density.md#density-proof-sde) are proved. General multiplicative noise and Hörmander bracket theory have not thereby been established.

## 39.21 How Future Sensitivity Becomes an Available Integrand

<a id="noise-clark"></a>

Chapter 33 represents an L² terminal in the Brownian natural filtration by an Itô integral, but existence alone does not identify the coefficient. DF generally depends on the future. To make it available beforehand, retain only the component identifiable from current information.

\[ F\in\mathbb D^{1,2}\quad\Longrightarrow\quad F=EF+\int_0^T E[D_tF\mid\mathcal F_t]\,dB_t. \]

This is Clark–Ocone. The conditional mean denotes a predictable dt⊗P version, not arbitrary timewise choices. For cylinders, conditioning future Gaussian increments constructs it explicitly; L² contraction extends it to the closed domain. For every predictable U, δU equals its Itô integral, and adjointness together with Chapter 33’s representation isometry identifies the coefficient uniquely. [Versions and proof](../foundations/t-clark-ocone.md) are complete.

For the squared reading DₜF=2B_T, whose conditional mean is 2Bₜ. Chapter 31’s square identity now gains a new interpretation: its integrand is not terminal sensitivity itself, but its projection onto current information. The old quadratic-variation proof need not be repeated.

## 39.22 The Same Noise with Different Information Can Represent Less

<a id="noise-information"></a>

Reveal an independent coin at time T. Its terminal conditional-mean martingale jumps at T; continuous Brownian Itô integrals cannot represent it. This terminal is not a σ(W)-measurable Gaussian output and lies outside the preceding theorem.

Thus representation by a noise depends on both noise and information. The Malliavin derivative measures response to perturbation; Clark–Ocone identifies which part can legally be used in temporal order. Sensitivity is not prediction, and conditioning does not make future events known.

## 39.23 Cameron–Martin Structure Is Not Limited to Wiener Coordinates

<a id="noise-banach"></a>

For centered Radon Gaussian X in a separable Banach space, take H as the L² closure of continuous linear readings and define i(h)=E[XW(h)]. Gaussian rotation yields exponential norm moments, making this B-valued integral legitimate. The map i embeds noise-energy directions into the state space. Its range is determined by the Gaussian law itself, not prescribed as all continuous paths.

\[ \frac{d\mathcal L(X+i(h))}{d\mathcal L(X)}=e^{W(h)-\|h\|^2/2},\qquad b\notin i(H)\Longrightarrow\mathcal L(X+b)\perp\mathcal L(X). \]

[T-GAUSSIAN 5–6](../foundations/t-gaussian.md#gaussian-proof-fernique) prove exponential moments, the embedding, equivalence and outside-range singularity, completing the Banach translation extension left in Chapter 33. The new point is that Hilbert energy can be recovered intrinsically from a Gaussian space, not merely chosen through convenient time coordinates.

## 39.24 Changing Output Coordinates Does Not Create Directions

<a id="noise-coordinates"></a>

Where chain-rule and integrability assumptions apply, a smooth output coordinate change ψ gives the covariance relation below. An invertible Jacobian preserves rank. But D∞ and inverse moments are global integrability requirements that an arbitrarily fast-growing ψ need not preserve. Structural invariance and preservation of particular sufficient estimates are different claims.

\[ \gamma_{\psi(F)}=D\psi(F)\gamma_FD\psi(F)^{\mathsf T},\qquad p_{\psi(F)}(y)=p_F(\psi^{-1}(y))\,|\det D\psi^{-1}(y)|. \]

The second identity is ordinary change of variables for a smooth diffeomorphism of Rᵐ and an existing density. It preserves smoothness without re-proving noise nondegeneracy from scratch. A geometric question becomes concrete: in overlapping coordinate charts, what depends on notation and what belongs to the motion itself?

## 39.25 Roughness Remains; a Different Differential Structure Emerges

<a id="noise-insight"></a>

Brownian paths remain nondifferentiable in ordinary time. What has been established is a different structure: comparable Cameron–Martin perturbations, a closed derivative compatible with approximation, divergence transferring derivatives onto probabilistic weights, and covariance identifying output directions. Chaos also turns sensitivity energy into an exactly calculable order cost.

None of this makes every random output smooth. Flat response can leave atoms; almost-sure nondegeneracy still allows sharp densities; repeated integration by parts needs real integrability; extra information can break Brownian representation. These boundaries do not weaken the theory: they identify what it can reliably answer.

The same rough trajectory can now be accumulated through time integrals and studied through responses in noise directions. In curved space, the representation of differentiation must also pass coordinate-consistency tests. The next distinction is not merely whether differentiation is possible, but whether stochastic differentials in different coordinates describe the same object.

### Sources and Proof Scope

This chapter is a modern reconstruction through finite Gaussian calculations, closed operators, orthogonal expansion and identification of laws, not a claimed reenactment of discovery. Conditions are compared with the Gaussian/Malliavin parts of [Hairer’s author-hosted notes](https://hairer.org/notes/StochasticAnalysisCourse.pdf) and the [Nualart–Nualart publisher contents](https://assets.cambridge.org/97811070/39124/frontmatter/9781107039124_frontmatter.pdf), without copying their prose.

Actual proofs: [T-GAUSSIAN](../foundations/t-gaussian.md), [T-MALLIAVIN](../foundations/t-malliavin.md), [T-MALLIAVIN-DENSITY](../foundations/t-malliavin-density.md), [T-CLARK-OCONE](../foundations/t-clark-ocone.md). The weakest vector \(\mathbb D^{1,2}\) absolute-continuity theorem, optimal Meyer estimates and general Hörmander theory are not claimed as completed here.
