# From Predictive Kernels to Dirichlet Random Probabilities and Their Posterior

## 1. Construct the infinite record before assuming a random measure

<a id="dp-proof-sequence"></a>

Let E be nonempty standard Borel, H a probability, α>0 and β=αH. Define the following kernels for n≥0, with an empty sum at n=0. Each evaluation is measurable in the past, and every past record gives a probability. The sequential-kernel construction in Chapter 10 gives a unique law Qβ on Eᴺ.

\[ Q_n(x_{1:n},A)=\frac{\beta(A)+\sum_{i=1}^n\mathbf1_A(x_i)}{\alpha+n}. \]

For any finite measurable partition \(A_1,\ldots,A_d\), the color record has the finite Pólya kernel with shapes aⱼ=β(Aⱼ). Its word probabilities depend only on counts. Refine any finite collection of Borel tests into their Boolean atoms; each rectangle is a finite union of color words. Thus all finite-dimensional laws are permutation invariant. Cylinder uniqueness gives exchangeability of Qβ. Measurable normalization proves existence; the factorial calculation proves symmetry.

## 2. The director realizes every finite partition on one space

<a id="dp-proof-director"></a>

Chapter 43 supplies a P(E)-valued director G; its evaluation σ-field and standard Borel structure were actually constructed there. For a finite partition, the conditional color record is iid with director (\(G(A_1),\ldots,G(A_d)\)). The finite Pólya proof also represents this color law as a Dir(a) mixture. Uniqueness of the finite-state directing law identifies the two mixtures, yielding the formula below.

\[ (G(A_1),\ldots,G(A_d))\sim\operatorname{Dir}(\beta(A_1),\ldots,\beta(A_d)). \]

Define Dβ, also denoted DP(α,H), as the law of a random probability satisfying this condition. Each G(ω,·) is already countably additive. We have not applied Kolmogorov extension to an uncountable set index and then asserted countable additivity of its sample functions. Gamma aggregation proves finite-partition consistency, while the director gives a common probability-valued realization. A one-point space yields the deterministic point mass and is included.

## 3. Uniqueness and parameter measurability are proved

<a id="dp-proof-kernel"></a>

Finite evaluation cylinders generate the evaluation σ-field of P(E). Any finite set family has a common partition refinement, so the definition determines all cylinder laws; π–λ proves uniqueness of Dβ. A countable generating algebra suffices: a monotone-class argument extends measurable evaluations to all Borel sets and π–λ determines measures. This verifies the minimal random-probability structure inherited from Chapter 43.

The posterior changes β with the data, so Dβ must also be a parameter kernel. Use (0,∞)×P(E) for (α,H). The predictive kernels are jointly measurable in parameter and past. Iterated kernel integration makes every finite cylinder probability measurable in the parameter. A Dynkin-class argument extends this to all path events, making Qβ a kernel into Eᴺ. Existence holds parameter by parameter; cylinder measurability supplies the additional kernel assertion.

Fix the same Borel coding b:E↔B⊂[0,1] used in Chapter 43. For every record take empirical rational-CDF limsups, decode a valid probability code supported on B, and use δe₀ otherwise. The measurable decoding gives one Borel map Ψ:Eᴺ→P(E), independent of β. Under every Qβ it is almost surely the director. Hence Dβ(C)=∫1{Ψ(x)∈C}Qβ(dx) is measurable in β. This constructs the parameter kernel required by the posterior rather than selecting laws separately at each data point.

## 4. The complete posterior-kernel proof

<a id="dp-proof-posterior"></a>

Work on the joint space that first draws G∼Dβ and then takes an iid record from G via the product kernel. For every data vector x₁,…,xₙ let βₓ=β+Σδxᵢ, of mass α+n>0. Both mass and normalized base are measurable in x. Therefore Kₙ(x,·)=Dβₓ is an actual probability kernel, defined even at data points lying in null events of the original model.

\[ \mathcal L(G\mid X_1,\ldots,X_n)=\mathsf D_{\beta+\sum_{i=1}^n\delta_{X_i}}. \]

First take any bounded Borel function F of a finite partition evaluation of G, and a sample rectangle B₁×…×Bₙ. Refine the partition together with all Bᵢ into R₁,…,Rₘ. The vector (G(Rⱼ)) is Dirichlet and, conditionally on it, sample colors are iid: the full product-kernel probability of a color word depends only on that vector, and the tower verifies the assertion. Finite conjugacy gives posterior shapes β(Rⱼ) plus color counts for each positive-probability word. Aggregation back to the coarse partition makes the posterior expectation of F exactly ∫F(μ)Dβₓ(dμ), constant on each color word. Null words contribute zero.

\[ E[F(G)\mathbf1_{\{X_{1:n}\in A\}}]=E\!\left[\mathbf1_{\{X_{1:n}\in A\}}\int F(\mu)\mathsf D_{\beta+\sum_i\delta_{X_i}}(d\mu)\right]. \]

The identity first holds for sample rectangles and extends by a Dynkin class to every sample event A. A second monotone-class argument on finite evaluation cylinders extends it to every bounded Borel F on P(E). This is the defining conditional-law identity. We have not assumed that actual observations carry only one coarse partition count. Kₙ is everywhere a probability, and countable determining tests give a common null set when comparing other regular conditional versions.

## 5. Prediction, second-order structure and conditional iid

<a id="dp-proof-prediction"></a>

Gamma moments give EG(A)=β(A)/α. Apply this mean to the posterior kernel and then use the tower to obtain the predictive formula. The predictive-first and DP-first experiments consequently have the same sequential kernels and record law. Independence given both G and the past comes from the full conditional product kernel, not merely from equality of next-step marginals.

\[ E[G(A)\mid X_{1:n}]=P(X_{n+1}\in A\mid X_{1:n})=\frac{\alpha H(A)+\sum_{i=1}^n\mathbf1_A(X_i)}{\alpha+n}. \]

Refine A and B into their intersection, two differences and complement, then sum the Dirichlet moment identities to obtain the covariance. It measures dependence caused by the common director rather than treating reinforcement as unconditional independence.

\[ \operatorname{Cov}(G(A),G(B))=\frac{H(A\cap B)-H(A)H(B)}{\alpha+1},\quad \operatorname{Cov}(\mathbf1_A(X_i),\mathbf1_B(X_j))=\operatorname{Cov}(G(A),G(B))\quad(i\ne j). \]

Return to the [DP construction](../chapters/44-dirichlet-process.md#dirichlet-process) and [posterior](../chapters/44-dirichlet-process.md#dirichlet-posterior) in Chapter 44. No paintbox theorem from Chapter 47 or random Radon-measure theorem from Chapter 49 is used; the scope is standard Borel random probabilities with the evaluation structure and parameter kernels needed here.
