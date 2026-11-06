# Pólya Prediction, Gamma Normalization and Finite Dirichlet Theory

## 1. Local prediction is not yet order symmetry

<a id="polya-proof-rule"></a>

Let the colors be 1 through d, with aⱼ≥0 and α=Σaⱼ>0. After n draws let Nⱼ(n) count color j. The next-color kernel is (aⱼ+Nⱼ(n))/(α+n), including n=0. The numerators sum to the denominator and the finite-state kernels are measurable. The sequential construction in Chapters 8 and 10 gives a unique infinite record law. A zero-mass color never appears.

\[ P(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_{j=1}^d(a_j)^{\uparrow n_j}}{(\alpha)^{\uparrow n}},\qquad (a)^{\uparrow r}=\prod_{i=0}^{r-1}(a+i),\quad (a)^{\uparrow0}=1. \]

Multiply the sequential probabilities. Each occurrence of color j contributes the next factor aⱼ,aⱼ+1,…, whereas the denominator depends only on length. Word probabilities depend only on counts, so finite permutations preserve them; cylinder uniqueness gives infinite exchangeability. Summing a normalized final kernel also proves consistency. If initial red and blue masses are both one, a red draw adds two reds but a blue draw adds one blue, the probabilities of red-blue and blue-red are 1/8 and 1/6. These are legitimate infinite predictive kernels, but not exchangeable.

## 2. Why Gamma variables produce a probability vector

<a id="polya-proof-gamma"></a>

For a>0 define Γ(a)=∫₀∞xᵃ⁻¹e⁻ˣdx. Positivity of a controls the origin; exponential decay controls infinity. Integration by parts, with vanishing boundary terms, gives Γ(a+1)=aΓ(a). Gamma(a,1) has density xᵃ⁻¹e⁻ˣ/Γ(a). Shape zero is separately defined as the constant zero. Rate is always one here, distinct from the shape parameter.

Restrict first to positive parameters. Let independent Yⱼ have these Gamma laws, S=ΣYⱼ, and Dⱼ=Yⱼ/S. Then S>0 almost surely. In the change yⱼ=suⱼ with \(u_d\)=1−Σⱼ<d uⱼ, the Jacobian is sᵈ⁻¹. Substitution gives the factorization below. For d=1 simply use D₁=1 instead of a zero-dimensional density.

\[ \frac{e^{-s}s^{\alpha-1}}{\Gamma(\alpha)}\,ds\;\frac{\Gamma(\alpha)}{\prod_j\Gamma(a_j)}\prod_j u_j^{a_j-1}\,du_1\cdots du_{d-1},\qquad u_j>0,\quad\sum_j u_j=1. \]

The original joint density integrates to one, as does the first factor. Tonelli proves normalization of the second and independence of S and D; S has law Gamma(α,1). Define the vector law to be \(\operatorname{Dir}(a_1,\ldots,a_d)\). Restore zero-parameter coordinates as zeros. With two positive coordinates the first coordinate is Beta(a,b), placing the earlier Beta example inside this construction.

## 3. Moments, aggregation and zero parameters

<a id="polya-proof-aggregate"></a>

For nonnegative integers rⱼ multiply the density by the monomial and normalize with parameters aⱼ+rⱼ. This gives the moment formula. If aⱼ=0 and rⱼ>0 the moment is zero; if both are zero its factor is one. Do not write Γ(0)/Γ(0).

\[ E\prod_j D_j^{r_j}=\frac{\prod_j(a_j)^{\uparrow r_j}}{(\alpha)^{\uparrow\sum_jr_j}},\quad ED_j=\frac{a_j}{\alpha},\quad \operatorname{Cov}(D_i,D_j)=\frac{\mathbf1_{\{i=j\}}a_i/\alpha-a_i a_j/\alpha^2}{\alpha+1}. \]

The Gamma-sum law was proved by the density of S. Sum disjoint coordinate groups: their sums remain independent Gamma variables with aggregated shapes. Dividing by the common total proves aggregation of Dirichlet parameters, including zero-mass groups. This proves consistency under every finite partition refinement. Two different partitions have a common refinement, so compatibility is not restricted to a selected partition chain.

## 4. Finite posterior and prediction are one calculation

<a id="polya-proof-posterior"></a>

Draw D∼Dir(a), then conditionally sample colors iid. A particular n-word has likelihood ∏Dⱼⁿʲ. Multiplying and normalizing the Dirichlet density gives posterior Dir(a+n). A word containing a zero-mass color has prior probability zero and allows an arbitrary conditional version. There is no multinomial coefficient because we condition on the actual word, not only its counts.

\[ \mathcal L(D\mid X_{1:n}=x)=\operatorname{Dir}(a_1+n_1,\ldots,a_d+n_d),\qquad P(X_{n+1}=j\mid X_{1:n})=\frac{a_j+n_j}{\alpha+n}. \]

Integrating the word likelihood reproduces the rising-factorial formula. Forward prediction and a Dirichlet mixture of iid records therefore have exactly the same law. In the latter construction the Chapter 12 strong law makes empirical color frequencies converge to D. Chapter 43 uniqueness identifies the same director in the predictive model, without assuming that reinforced draws are unconditionally independent.

## 5. Reinforcement scales and proof responsibility

<a id="polya-proof-scope"></a>

If every draw adds the same mass c>0, divide all initial masses by c to obtain shapes aⱼ/c. With c=0 there is no reinforcement and the result is iid with fixed probabilities; substitution into aⱼ/c is invalid. Total shape must be positive: an all-zero Gamma vector has not been normalized. The proof uses finite-dimensional change of variables, nonnegative integration, sequential kernels, the strong law and Chapter 43 uniqueness.

Return to [finite prediction in Chapter 44](../chapters/44-dirichlet-process.md#dirichlet-finite).
