# Regenerative Ratios and a Conservative Hopf Theorem

## 1. Reward ratios without finite mean cycles

<a id="ratio-cycles"></a>

Use T-HARRIS-REGENERATION, allowing μ=∞. Assume m|f|<∞, g≥0 and 0<mg<∞. The half-open cycle rewards \(F_i\),\(G_i\),\(A_i\) for f,g,|f| are iid and integrable, with means mf,mg,m|f|. For any integrable nonnegative Y, ΣP(Y>εi)<∞, hence \(Y_i\)/i→0; this step needs equal distributions, not independence. It controls the absolute reward and g-reward of the last incomplete cycle.

Each cycle has finite length, so the completed count N(n) tends to infinity even when N(n)/n→0. Strong laws for the partial sums \(\sum _{i\le k}\)\(F_i\) and the corresponding sums of \(G_i\) give the mean rewards mf and mg per cycle. The initial prefix is finite for everywhere finite versions of f,g, and the remainders are bounded by \(A_{N+1}\),\(G_{N+1}\)=o(N). If functions are only m-almost everywhere finite, one must specify versions and starting exceptions. We instead use everywhere finite measurable functions here.

\[ \frac{\sum_{j=0}^{n-1}f(X_j)}{\sum_{j=0}^{n-1}g(X_j)}\longrightarrow\frac{mf}{mg}\quad\mathbb P_x\text{-a.s. for every }x. \]

The denominator is eventually positive and diverges, because its mean cycle reward is positive. Aperiodicity is not used. If μ<∞, \(R_k\)/k→μ converts this into the time-average theorem for π-integrable f. If μ=∞, integrable bounded g has time average zero since N(n)/n→0; this was used to exclude invariant probabilities.

## 2. A complete σ-finite measure-preserving Hopf version

<a id="ratio-hopf"></a>

Here is a second ratio theorem, for an invertible ergodic σ-finite measure-preserving transformation T with T and T⁻¹ conservative: almost every point in each positive-measure set returns infinitely often in both time directions. Choose 0<m(A)<∞. Ergodicity makes the two-sided saturation of A conull, and forward/backward conservativity supplies visits in both directions. Let τ be first return and \(T_A\)=T^τ the induced map.

Partition by the most recent visit to A: the sets Tʲ(A∩{τ>j}) are disjoint and cover modulo null sets. Partitioning B⊂A by its previous return similarly gives m(\(T_A\)⁻¹B)=m(B). Lifting a \(T_A\)-invariant B along these towers yields a T-invariant set, so \(T_A\) is ergodic for normalized m|A.

For integrable f and nonnegative integrable g, set \(f_A\)=\(\sum _{j<\tau }\)f∘Tʲ and likewise \(g_A\). Tower partition and Tonelli give ∫A \(f_A\)=mf, ∫A \(g_A\)=mg and ∫A\((|f|)_A\)=m|f|. Birkhoff on the induced probability system gives the reward ratio mf/mg. The last cycle reward divided by cycle count tends to zero by equal distributions, integrability, summable tails and Borel–Cantelli. A finite entrance delay is harmless. This yields the ratio limit in the original system.

This is not a theorem for arbitrary nonconservative or nonsingular transformations. The shift T(k)=k+1 on counting measure on Z is measure preserving and ergodic but dissipative. For f=\(\mathbf1_{0}\),g=\(\mathbf1_{1}\), the integrals agree, yet from k=2 the future denominator is always zero. Conservativity matters. General noninvertible positive-operator, nonsingular and continuous-time ratio theorems are not claimed here.

## 3. Random ratios in probability systems

<a id="ratio-probability"></a>

For a probability-preserving but nonergodic T, f,g∈L¹ and g≥0, Chapter41 gives the ratio E[f|I]/E[g|I] on {E[g|I]>0}. These random conditional averages cannot in general be replaced by global integrals. Different noncommunicating environments can retain different limiting ratios.

Return to [Chapter42](../chapters/42-harris-coupling.md#harris-ratio). The scopes differ: regenerative chains allow infinite m and every starting state; the conservative Hopf version is almost everywhere for invertible ergodic σ-finite systems; the probability version allows random conditional limits.
