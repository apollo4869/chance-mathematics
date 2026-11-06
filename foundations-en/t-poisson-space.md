# T-POISSON-SPACE: Spatial Poisson and Cox Constructions

Return to [Chapter48](../chapters/48-point-processes.md#points-poisson-construction). Construction first works on a standard Borel space with sigma-finite intensity; becoming Mₚ-valued requires the additional local-finiteness condition.

## 1. Finite mass: count first, locations second

<a id="poisson-space-finite"></a>

For finite μ let λ=μ(E). If λ=0 put N=0. Otherwise choose K∼Poisson(λ), then independent iid locations of law μ/λ, and put N=\(\sum_{i\le K}\delta_{Z_i}\). Every Borel count is a measurable random sum. For any nonnegative measurable f, condition on K and sum the Poisson series to obtain the following expression, with infinite integrals allowed and exp(−∞)=0.

\[ \mathbb E e^{-Nf}=e^{-\lambda}\sum_{k\ge0}\frac{\lambda^k}{k!}\left(\frac1\lambda\int e^{-f}\,d\mu\right)^k=\exp\{-\mu(1-e^{-f})\}. \]

## 2. Sigma-finite assembly and independent scattering

<a id="poisson-space-sigma"></a>

Partition E into countably many disjoint Borel Dₘ of finite μ-mass. Chapter8 supplies independent finite-mass constructions Nₘ on one product space. Set N(A)=ΣNₘ(A∩Dₘ). This is a countably atomic counting measure, possibly infinite. The finite-piece Laplace products pass to the limit by bounded convergence, while their exponent integrals pass by monotone convergence. Inserting \(\sum_i t_i\mathbf1_{A_i}\) for disjoint sets factors the exponent. Vector Laplace uniqueness gives independent Poisson counts for finite-intensity sets. If μ(A)=∞, then Eexp(−tN(A))=0 for every t>0, so N(A)=∞ almost surely. This property for finite collections of disjoint finite-intensity sets is independent scattering.

For uniqueness first compare joint Laplace transforms of finite collections of counts within finite-intensity pieces Dₘ. These vectors are finite, so the preceding vector uniqueness applies directly. Every count N(A) is ΣₘN(A∩Dₘ), so these readings already generate the entire evaluation sigma-field. Cylinder π–λ gives uniqueness of the full law, independently of the partition chosen. Conversely, independent Poisson counts give the functional first for nonnegative simple f, then for general f by increasing simple approximation. Construction, independent-scattering characterisation and functional characterisation are therefore equivalent, rather than merely matching a total count.

## 3. Local finiteness and simplicity are different

<a id="poisson-space-local"></a>

Now let E be locally compact and second countable, and μ locally finite Radon. Since EN(Kₘ)=μ(Kₘ)<∞, all exhaustion-window counts are finite on one common full-probability set. The counting measure is then Radon and belongs to Mₚ. Conversely, infinite intensity on a compact K implies N(K)=∞ almost surely by the functional argument. Sigma-finiteness alone does not ensure local finiteness; an example on the real line is intensity \(\mathbf1_{(0,1)}(x)\,dx/x\).

In this locally finite setting N is simple almost surely exactly when μ is atomless. With atomless μ, any two sampled occurrences, within or across pieces, coincide with probability zero; take the countable union over pairs. If μ({x})=a>0, the Poisson(a) count at x has positive probability of being at least two. Local finiteness allows finite multiplicities and must not be confused with simplicity.

## 4. A measurable kernel for random intensities

<a id="poisson-space-cox"></a>

Let Λ be a random locally finite Radon measure, assuming only that each Borel evaluation Λ(A) is measurable. Use fixed exhaustion pieces Dₘ, each of finite Λ-mass. Set the intensity to zero on parameters with an infinite exhaustion-window mass; if local finiteness is only almost sure, this changes a measurable null set. Poisson inverse CDF sampling is measurable in its parameter and uniform input. For positive mass, Λ(·∩Dₘ)/Λ(Dₘ) is a probability kernel; at zero mass use a fixed cemetery distribution. Chapter10 kernel randomisation supplies locations from fresh independent uniforms.

Composing these measurable steps countably many times gives an evaluation-measurable map (Λ, fresh uniforms)↦N and hence a Poisson-law kernel measurable in Λ. Integrating the fresh uniforms and using the construction for each parameter proves the whole conditional law given Λ is Poisson(Λ), not just its window marginals. This is the Cox process.

\[ \mathbb E[e^{-Nf}\mid\Lambda]=e^{-\Lambda(1-e^{-f})},\qquad L_N(f)=\mathbb E e^{-\Lambda(1-e^{-f})}. \]

If Λ=Zμ with finite nonnegative random Z, N remains locally finite even when EZ=∞. For disjoint A,B and EZ²<∞, conditional independence and total covariance give Cov(N(A),N(B))=Var(Z)μ(A)μ(B), generally nonzero. Random intensity cannot simply be replaced by its mean. The full topology of random Λ is left to Chapter49; this construction uses evaluation measurability and the established standard-Borel kernel tools.
