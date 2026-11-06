# T-POINT-TRANSFORMS: Marking, Mapping and Means

Return to [Chapter48](../chapters/48-point-processes.md#points-marking). We use the measurable enumeration with multiplicities from [T-POINT-MEASURES](t-point-measures.md#point-space-measurable) and the functional for all nonnegative measurable tests from [T-POISSON-SPACE](t-poisson-space.md).

## 1. Marking each occurrence separately

<a id="point-transform-mark"></a>

Let N be locally finite on E, let F be a standard-Borel mark space, and let κ be a probability kernel from E to F. Assign a fresh independent uniform to each enumerated occurrence and use Chapter10 randomisation to obtain its mark, forming M=\(\sum_i\delta_{(x_i,y_i)}\). Distinct occurrences at the same location must receive independent marks. M is finite in each ground window A×F with relatively compact A. If F is also locally compact and second countable, projections of product compacts are compact, so M is locally finite on the product. For merely standard-Borel F we use evaluation measurability and ground-local finiteness, without claiming a vague topology on F.

\[ \mathbb E[e^{-Mf}\mid N]=\prod_{x\text{ occurrence in }N}\kappa(x,e^{-f(x,\cdot)})=\exp\{-N h\},\qquad h(x)=-\log\kappa(x,e^{-f(x,\cdot)}). \]

Compute the product first for finite enumeration prefixes and pass by bounded convergence; h may be infinite. If N is Poisson(μ), its functional gives exp{−∫∫(1−e⁻ᶠ)κ(x,dy)μ(dx)}. Thus M is a PRM with intensity μ(dx)κ(x,dy). Independent Poisson counts on disjoint finite-intensity sets follow from the functional, not from individual mark marginals.

## 2. Mapping requires checking target windows

<a id="point-transform-map"></a>

Let T:E→F be measurable, with F locally compact and second countable. The map \(T_*N(A)=N(T^{-1}A)\) is evaluation-measurable but need not be locally finite. For Poisson(μ), if ν=\(T_*\mu\) is finite on every compact, it is Radon: regularity of locally finite Borel measures on this space follows by the same open/compact approximation as T-RIESZ. Then \(T_*N\)∈Mₚ(F) almost surely. Substituting f∘T into the functional proves Poisson(ν). If ν(K)=∞ for some compact K, its count is infinite almost surely and the result is not locally finite.

For an arbitrary, not necessarily Poisson, N, a sufficient condition is that T be continuous and proper, meaning compact preimages are compact; check this pathwise. For Poisson processes the weaker intensity-preimage condition suffices. Mapping need not preserve simplicity: collapsing a finite-intensity interval to zero creates a Poisson multiplicity there; collapsing the whole Lebesgue-intensity real line creates infinitely many points at zero. Random displacement is marking followed by mapping and still requires local finiteness of the output intensity.

## 3. Independent thinning and superposition

<a id="point-transform-thin"></a>

Give each occurrence an independent Bernoulli(q(x)) mark and call the two retained configurations N₁ and N₀. For nonnegative tests f,g use the product-space test f(x)\(\mathbf1_{\{1\}}\)+g(x)\(\mathbf1_{\{0\}}\). The marking functional factors as exp{−μ(q(1−e⁻ᶠ))}exp{−μ((1−q)(1−e⁻ᵍ))}. Joint Laplace uniqueness proves that N₁ and N₀ are independent PRMs, not merely separately Poisson.

A countable superposition of independent Poisson(μⱼ) processes is Poisson(Σμⱼ) when the sum intensity is locally finite, by finite products and monotone convergence. Without that condition it can fail to be locally finite. Dependent deletion has no thinning guarantee: retaining only the leftmost point in a finite window, when one exists, gives a count in {0,1}, generally not Poisson. With atoms, ties must additionally be resolved at the occurrence level.

## 4. Campbell means and compensated second moments

<a id="point-transform-campbell"></a>

Any evaluation-measurable point process Ξ has intensity measure ν(A)=EΞ(A); Tonelli proves countable additivity. It need not be locally finite or even sigma-finite. Linearity for nonnegative simple functions followed by monotone convergence proves Campbell’s mean formula. Signed f requires ∫|f|dν<∞. Here f is deterministic. A function depending on the whole configuration cannot simply be integrated against ν instead; Palm and Mecke structures belong to Chapter50.

\[ \mathbb E\int f\,d\Xi=\int f\,d\nu.\qquad \mathbb E\left[\left(\int f\,d(N-\mu)\right)\left(\int g\,d(N-\mu)\right)\right]=\int fg\,d\mu. \]

The second identity first holds for simple f,g on disjoint finite-intensity cells: centred independent counts eliminate cross terms and Var N(A)=μ(A). Approximate general L²(μ) functions by finite-window simple functions. The isometry gives a unique extension in L²(P), with mean zero and the stated covariance. If f is also L¹, the extension agrees with the ordinary signed random-measure integral because Campbell controls L¹ approximation. For merely L² functions it must not be interpreted as subtracting two potentially infinite ordinary integrals.
