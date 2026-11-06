# Small-Set Splitting, Cycle Measures and Harris Recurrence

## 1. Pointwise assumptions

<a id="regen-assumptions"></a>

Throughout this proof E is standard Borel, P is a probability kernel, C is a nonempty measurable set, ν is a probability and 0<ε<1. For every x∈C and measurable A, P(x,A)≥εν(A). From every x the chain visits C infinitely often almost surely. When ε=1 reduce it to ε/2. These are explicit regenerative hypotheses; irreducibility alone is not a proof of the inequality.

On C set \(R_x\)=(P(x,·)−εν)/(1−ε), and off C set \(R_x\)=P(x,·). At x∈C draw a fresh Bernoulli(ε) coin δ; on success draw the next state from ν, and otherwise from \(R_x\). Off C set δ=0 and use P. Kernel randomization with independent uniforms, or T-SEQUENTIAL for this measurable joint kernel, constructs the process. Marginalizing the coin gives exactly P.

A coin is tossed before leaving \(X_n\). The regeneration epoch is the endpoint n+1 of a successful transition, not the time n of the coin. Conditional on everything before that endpoint and on the success time, \(X_{n+1}\) has law ν. The probability of failing the first k visits is (1−ε)ᵏ, so all regeneration epochs are finite.

## 2. Half-open cycles and stopping information

<a id="regen-cycles"></a>

Start at a regeneration endpoint with X₀∼ν, and let L be the next endpoint. A cycle mark is (L,X₀,…,\(X_{L-1}\)); it excludes \(X_L\). Its space is the countable disjoint union \(\bigsqcup _{l\ge 1}\)({l}×Eˡ), again standard Borel. The new endpoint is independent of the previous half-open cycle, so these marks are iid. Starting at an arbitrary x adds only an almost surely finite initial delay.

Regeneration is a stopping construction in enlarged information. Strong Markov is used only at legitimate stopping times. In particular, one cannot inspect the next state and then declare the coin independent without correcting conditional laws. Our sampling order avoids this error. Disintegrating cycle marks given L=l is valid on the standard Borel mark space; only integers of positive probability matter.

## 3. Cycle occupation is invariant

<a id="regen-measure"></a>

\[ m(A)=E_\nu\sum_{n=0}^{L-1}\mathbf1_A(X_n),\qquad \mu=E_\nu L=m(E)\in[1,\infty]. \]

Countable additivity follows from Tonelli. The event \(S_n\)={L>n} says that the preceding n transitions have not regenerated; it does not inspect the new coin at time n. Hence E[\(\mathbf1_{S_n}\)f(\(X_{n+1}\))]=E[\(\mathbf1_{S_n}\)Pf(\(X_n\))]. For indicator f, summing shifts the half-open occupation one step, removing X₀ and adding \(X_L\). Both endpoints have law ν, so mP=m. If mf is infinite the identity still compares nonnegative series; endpoint expectations are at most one, and no ∞−∞ is used.

Every visit to C is a trial until the first success, so m(C)=1/ε. The sets \(A_{jk}\)={x:Pʲ(x,C)≥1/k}, j≥0,k≥1, cover E because C is accessible from every x. Invariance gives m(\(A_{jk}\))≤k mPʲ(C)=k/ε. Thus m is nonzero and σ-finite. This covering matters: an almost surely finite cycle need not have finite mean length.

If m(A)>0, a ν-cycle has positive probability of visiting A. Repeated independent cycles then visit A infinitely often from every initial state. Thus the chain is Harris recurrent for ψ=m. This is an assertion for each fixed positive-ψ set, with an exceptional null set possibly depending on A; it is not an uncountable simultaneous assertion.

## 4. Positive and null recurrence

<a id="regen-positive"></a>

If μ<∞, π=m/μ is invariant. Uniqueness does not require aperiodicity: the cycle reward strong law gives time averages πf for bounded f from every state. If η is another invariant probability, bounded convergence under the η-start yields ηf=πf. Applying this to indicators gives η=π.

If μ=∞, m cannot be normalized. Nor can some other invariant probability exist. Enumerate the countable finite-measure cover as \(B_j\) and construct measurable 0<g≤1 with m(g)<∞, for example Σ 2⁻ʲ\(\mathbf1_{B_j}\)/(1+m(\(B_j\))). Truncated strong laws for iid lengths give \(R_k\)/k→∞, hence completed cycle count N(n)/n→0. The g-reward of a cycle is integrable, and its final incomplete reward is bounded by \(Y_k\) with \(Y_k\)/k→0 by summable tails. Therefore total g-reward divided by n tends to zero. A finite initial delay has no effect.

An invariant probability η would give ηg=0 by bounded convergence, contradicting g>0 everywhere. Thus within this regenerative setting invariant probability is equivalent to finite mean cycle. Harris recurrence alone gives finite cycles, not finite mean cycles. Full reward and remainder arguments appear in [T-HARRIS-RATIO](t-harris-ratio.md).

## 5. Extracting a multistep small set

<a id="regen-small-extraction"></a>

On a standard Borel space one can also prove a substantive extraction lemma: ψ-irreducibility gives an m-step small set C of positive ψ-measure for some m≥1. It does not automatically prove Harris recurrence or aperiodicity of that skeleton from all starts; that remains a separate condition.

Choose a probability λ equivalent to ψ. Decompose λ(dx)Pᵏ(x,dy) relative to λ⊗λ, with AC density \(r_k\)(x,y), for each k≥1. The singular remainder has first marginal dominated by λ. Standard Borel disintegration and a countable determining algebra give Pᵏ(x,dy)=\(r_k\)(x,y)λ(dy)+\(S_k\)(x,dy) simultaneously for λ-almost every x. A joint singular witness N has λ-null sections, and \(S_k\) is concentrated on \(N_x\), so the rows of \(S_k\) are singular. This proves the required row decomposition rather than presuming a future general parameter theorem.

Set R=\(\sum _{k\ge 1}\)2⁻ᵏPᵏ. Irreducibility, with hits at positive times, gives λ≪R(x,·). Countably many singular remainders remain singular, so \(r_R\)=Σ2⁻ᵏ\(r_k\) is strictly positive λ⊗λ-almost everywhere. Some k therefore has nonzero row densities on a positive-λ set. The space L¹(λ) is separable, with rational simple functions from a countable generating algebra dense. The row map \(r_k\) is measurable through its distances to these simple functions. Choose a nonzero nonnegative g in the support of its distribution; every L¹-ball about g has a positive-λ preimage under \(r_k\).

For some l≥1, \(h_l\)(y)=∫g(z)min(\(r_l\)(z,y),1)λ(dz) is positive on a positive-λ set. Otherwise summing over l contradicts \(r_R\)>0 and g≠0. Choose δ>0 and a positive-λ B with \(h_l\)>2δ. Let C be the preimage of the radius-δ ball, removing the row-decomposition exceptional set. For every x∈C the following measure bound holds.

\[ P^{k+l}(x,dy)\ge\left[\int r_k(x,z)\min(r_l(z,y),1)\lambda(dz)\right]\lambda(dy)\ge\delta\,\mathbf1_B(y)\lambda(dy). \]

The first step uses row decomposition and kernel composition; the second uses the L¹ error ‖\(r_k\)(x,·)−g‖₁<δ and the bound min(\(r_l\),1)≤1. Set ν=λ|B/λ(B), ε≤δλ(B), and m=k+l. C has positive ψ-measure, so an original Harris chain repeatedly visits it. This alone has not shown that visits occur at the specified times modulo m, so skeleton recurrence still needs justification.

## 6. Constructing a shift coupling

<a id="regen-shift"></a>

From x and y generate the two half-open prefixes and first regeneration epochs R,S, leaving their endpoints unsampled. Each endpoint should independently have law ν relative to its own prefix. Draw one Z∼ν, set \(X_R\)=\(Y_S\)=Z, and use shared P-randomization thereafter. Independence from each prefix preserves each marginal path law. R,S are finite. The construction allows infinite mean cycles and periodicity.

Return to [Chapter 42](../chapters/42-harris-coupling.md#harris-split). Dependencies are Chapters 10,17 and12, not Chapter43. The small-set lemma does not claim the whole structure theorem for arbitrary aperiodic skeletons.
