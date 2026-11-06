# T-POINT-LAPLACE: Functional Identification and Point-Process Limits

Return to [Chapter48](../chapters/48-point-processes.md#points-laplace). The space and point-measure topology are established in [T-POINT-MEASURES](t-point-measures.md).

## 1. Laplace uniqueness for nonnegative vectors

<a id="point-laplace-vector"></a>

If finite nonnegative random vectors Y and Z have the same Laplace transform for every nonnegative parameter t, transform each coordinate to exp(−Yᵢ)∈(0,1]. Integer parameters give all mixed moments on the compact cube. Multivariate Bernstein polynomials approximate continuous functions uniformly: use independent binomial sampling in each coordinate, with total mean-square grid error at most the dimension divided by 4n; uniform continuity and Chebyshev control the error. This is the finite-product version of Chapter13. Thus the image measures agree on continuous functions. Distance cutoffs approximate opens and π–λ gives all Borel sets. The exponential map has a Borel inverse, giving equality in law of Y and Z. Finite nonnegative measures are handled by identifying total mass at parameter zero and normalising.

## 2. Identifying the whole point law

<a id="point-laplace-unique"></a>

\[ L_\Xi(f)=\mathbb E e^{-\Xi f},\qquad f\in C_c^+(E). \]

For deciding tests f₁,…,fₖ insert f=Σtᵢfᵢ. Vector uniqueness determines the joint law of (Ξf₁,…,Ξfₖ). The countable coordinates generate the Borel sigma-field of Mₚ, so cylinder π–λ determines the entire point-process law. Individual marginals do not suffice: finite linear combinations recover their joint structure. Testing only the countable rational cone selected in the preceding proof also suffices, by bounded convergence in the parameters.

## 3. Tightness must control local windows

<a id="point-laplace-tight"></a>

If the counts Ξₙ(Kₘ) are uniformly tight for each compact exhaustion window, choose integers aₘ with supₙP{Ξₙ(Kₘ)>aₘ}<ε2⁻ᵐ. Configurations satisfying all these bounds have compact closure by the preceding proof, so their laws are tight. Conversely, on each compact family the continuous integrals against χₘ are bounded and dominate the counts in Kₘ. Restrict probability to that compact family to obtain uniform tightness of local counts. This is therefore necessary and sufficient for tightness of the laws. Requiring a finite total count is unnecessarily strong and inappropriate on an unbounded space.

## 4. Laplace convergence to an existing point law

<a id="point-laplace-convergence"></a>

Theorem: for Mₚ-valued Ξₙ and Ξ, weak convergence Ξₙ⇒Ξ holds exactly when Lₙ(f)→L(f) for every \(C_c^+\) test. Necessity follows because exp(−ξf) is bounded continuous. For sufficiency tightness must first be proved; pointwise convergence of functionals alone is not an explanation. For χₘ≥1 on Kₘ and a>0 we have the following estimate.

\[ \mathbb P\{\Xi_n(K_m)>R\}\le\frac{1-L_n(a\chi_m)}{1-e^{-aR}}. \]

Since Ξχₘ is finite almost surely, L(aχₘ)→1 as a↓0. First choose a to make the limiting numerator small, then R to bring the denominator near one; enlarge R again for the finitely many initial n. This yields uniform local-count tightness. Mₚ is already proved Polish, so Chapter24 Prokhorov gives convergent subsequences. Every limit has the same test functionals L and hence the law of Ξ. A subsequence remaining outside a neighbourhood of that law would give a contradiction. Thus the argument uses Chapter24, not Chapter49.

Continuity-set counts give another practical collection of observations. If ξₙ→ξ vaguely, A is relatively compact and ξ(∂A)=0, inner and outer continuous approximation give ξₙ(A)→ξ(A). For a random limit require P{Ξ(∂A)=0}=1 and apply the continuous mapping theorem to finite collections of such sets. A countable ball base can be chosen this way: on {Ξ(K)≤l} inside a compact window at most l concentric spheres are hit, so only countably many radii have positive hitting probability. Take unions over l and windows, and choose dense radii avoiding them. Sets with boundary atoms cannot be used without qualification.

## 5. A limit of independent rare locations

<a id="point-laplace-rare"></a>

In each finite row take independent experiments: item j produces one point with probability pₙⱼ and conditional location law Qₙⱼ, or is empty. Write νₙ=ΣpₙⱼQₙⱼ. Assume νₙ converges vaguely to a locally finite Radon μ and maxⱼpₙⱼQₙⱼ(K)→0 for every compact K. Then their superposition converges to the Poisson point process of intensity μ. The hypothesis is local and allows experiments that almost surely occur far away.

\[ a_{nj}=p_{nj}\int(1-e^{-f})\,dQ_{nj},\quad L_n(f)=\prod_j(1-a_{nj}),\quad \sum_j a_{nj}=\nu_n(1-e^{-f})\longrightarrow\mu(1-e^{-f}). \]

When f is supported in K, max aₙⱼ→0 and Σaₙⱼ is bounded, hence Σaₙⱼ²≤max aₙⱼΣaₙⱼ→0. The bound |log(1−a)+a|≤2a² for 0≤a≤1/2 gives the Poisson Laplace limit. The preceding theorem completes process-level convergence. Independence cannot be removed: let all n experiments share a trigger of probability 1/n and produce n points when triggered. The expected count remains one, but the process is empty with probability tending to one, rather than approaching a Poisson law of intensity one.
