# T-POISSON-CHAOS: Coincidences, Multiple Integrals and L² Decoupling

Return to [Chapter48](../chapters/48-point-processes.md#points-multiple). Fix sigma-finite μ on standard-Borel E and the constructed Poisson measure N. We establish L² multiple integrals with deterministic kernels and the complete chaos expansion, including atomic μ. The selected decoupling result is an exact L² identity, not a general Lᵖ or tail-probability theorem.

## 1. Repeated use of a cell requires new polynomials

<a id="poisson-chaos-polynomials"></a>

\[ e^{-\lambda t}(1+t)^k=\sum_{r\ge0}\frac{t^r}{r!}C_r(k,\lambda),\quad C_0=1,\ C_1=k-\lambda,\ C_2=(k-\lambda)^2-k. \]

This defines real polynomials Cᵣ; for each integer k the generating function is entire. If K∼Poisson(λ), summing its series shows that the expected product of two generating functions is exp(λst). In a small complex neighbourhood of s=t=0, absolute values are bounded by a constant times aᴷ. Poisson exponential moments justify differentiation and coefficient comparison.

\[ \mathbb E[C_r(K,\lambda)C_s(K,\lambda)]=\mathbf1_{\{r=s\}}r!\lambda^r. \]

In particular the second multiple integral is not simply the square of the centred count. Subtract K to obtain zero mean and orthogonality to first order. This removes reusing the same occurrence, not the entire spatial diagonal. With atomic μ, distinct occurrences can lie at the same position and the spatial diagonal can carry legitimate second-order terms.

## 2. Definition and exact isometry on finite partitions

<a id="poisson-chaos-step"></a>

Take disjoint finite-intensity cells A₁,…,Aₖ. For a multi-index a of total degree r, let fₐ be the averaged symmetrisation of the tensor having aᵢ copies of \(\mathbf1_{A_i}\). Define Iᵣ(fₐ)=∏ᵢ\(C_{a_i}\)(N(Aᵢ),μ(Aᵢ)). These kernels are orthogonal for distinct multi-indices, with squared norm (∏aᵢ!/r!)∏μ(Aᵢ)^{aᵢ}. Independence and the preceding identity give squared norm ∏aᵢ!μ(Aᵢ)^{aᵢ} for their random integrals. Thus linear combinations satisfy the following identity.

\[ \mathbb E[I_r(f)I_s(g)]=\begin{cases}r!\langle f,g\rangle_{L^2(\mu^{\otimes r})},&r=s,\\0,&r\ne s.\end{cases} \]

## 3. Refining a partition preserves the integral

<a id="poisson-chaos-refine"></a>

Splitting a cell into two and multiplying generating functions gives Cᵣ(K+L,λ+ρ)=\(\sum_{j=0}^r\) binom(r,j)Cⱼ(K,λ)Cᵣ₋ⱼ(L,ρ). This is exactly the tensor expansion obtained by assigning each coordinate to one subcell. Thus definitions agree under finite refinement; any two partitions have a common refinement. Finite-intensity rectangular simple functions are dense in the product L² space: truncate to finite windows, use a monotone class to approximate product-Borel indicators, then approximate general functions by simple ones. Symmetrisation is a contraction, so symmetric step kernels are dense in the symmetric subspace. The isometry and established L² completeness extend Iᵣ uniquely to every symmetric L² kernel. For general kernels define the integral through symmetrisation.

## 4. Why the chaoses exhaust L² outputs

<a id="poisson-chaos-complete"></a>

Let 𝓗ᵣ be the closed range of Iᵣ and 𝓗₀ the constants. For bounded finite-partition step h of finite-intensity support, define 𝓔(h)=exp(−μh)\(\prod_{x\text{ occurrence in }N}\)(1+h(x)); it suffices to take −1<h≤0. Its cell generating series converge in L² because the sum of squared norms of their orthogonal terms is exp(∫h²dμ). The L² sum equals the samplewise entire-function sum, by taking an almost-sure subsequence of partial sums. Hence the following expansion holds.

\[ \mathcal E(h)=\sum_{r=0}^\infty\frac1{r!}I_r(h^{\otimes r}),\qquad \mathbb E\mathcal E(h)^2=\exp\{\mu(h^2)\}. \]

If F∈L²(σ(N)) is orthogonal to every 𝓗ᵣ, it is orthogonal to these 𝓔(h). Taking h=e⁻ᶠ−1 gives E[F e⁻ᴺᶠ]=0 for nonnegative simple f supported on finite-intensity pieces. For any finite collection of finite-intensity sets, the finite measures on their count vectors weighted by F⁺ and F⁻ have identical Laplace transforms. Their masses agree as EF=0. Vector uniqueness gives \(\mathbb E[F\mathbf1_A]\)=0 for every finite count cylinder. Counts on sigma-finite pieces generate σ(N), so π–λ extends this to all events. Testing {F>0} and {F<0} gives F=0. Thus the orthogonal sum is complete and every F has the following unique expansion.

\[ F=\mathbb EF+\sum_{r\ge1}I_r(f_r),\qquad \operatorname{Var}F=\sum_{r\ge1}r!\|f_r\|_2^2. \]

## 5. The L² scope of independent-copy decoupling

<a id="poisson-chaos-decoupling"></a>

Take r independent PRMs N¹,…,Nʳ, all of intensity μ. For a product kernel f=f₁⊗⋯⊗fᵣ define Jᵣ(f)=∏ᵢI₁^{(i)}(fᵢ). Independence and first-order isometry give E[Jᵣ(f)Jᵣ(g)]=〈f,g〉. Extend finite sums by density and completeness to all product-L² kernels. This precisely assigns different coordinates to independent noise copies. For symmetric f, comparison with the coupled multiple integral gives the following identity.

\[ \mathbb E|I_r(f)|^2=r!\,\mathbb E|J_r(f)|^2=r!\|f\|_2^2. \]

This is second-moment decoupling, not equality in law. In one window I₂ is C₂ of a single Poisson count, while J₂ multiplies two independent centred counts. They are different constructions. General Lᵖ decoupling, tail comparisons, random-kernel multiple integrals and the full product formula are not proved here and are not counted within this scope.
