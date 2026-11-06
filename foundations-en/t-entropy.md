# T-ENTROPY: Finite-Entropy Information Rates, SMB and Generating Partitions

This page proves [the information-rate results](../chapters/41-ergodic-theory.md#ergodic-information-rate). For SMB take a two-sided stationary process on a countable alphabet, H(X₀)<∞, and the invertible coordinate shift T. Nonergodic laws are allowed: the conditional information rate converges almost surely and in L¹, not merely in expectation. Finite-partition entropy is also defined for general probability-preserving maps; the generator theorem explicitly assumes invertibility.

## 1. Chain entropy, conditioning and block limits

<a id="entropy-proof-basics"></a>

For a countable distribution set H=Σ−p_a log p_a with 0 log0=0. An actual symbol has zero probability of landing on a zero-probability letter. Factoring joint probabilities gives −log p(X,Y)=−log p_X(X)−log p(Y|X). All terms are nonnegative, so Tonelli gives the entropy chain rule, allowing infinity. Conditional entropy is the expected entropy of a conditional distribution. Conditional Jensen for −u log u shows that finer conditioning reduces it. Coalescing a countable tail into one symbol, or summing nonnegative terms, extends the finite-alphabet assertions.

For a stationary process, H_n=H(X₀,…,X_{n−1}) is subadditive and bounded by nH(X₀)<∞. Fekete gives h=lim H_n/n=inf H_n/n. This deterministic block-entropy limit alone says nothing about the information rate of an actual word. The next sections supply that random control.

## 2. Zero conditional probabilities and an integrable logarithmic envelope

<a id="entropy-proof-envelope"></a>

\[ \mathcal G_k=\sigma(X_{-k},\ldots,X_{-1}),\quad p_k(a)=P(X_0=a\mid\mathcal G_k),\quad p_\infty(a)=P(X_0=a\mid\mathcal G_\infty),\quad I_k=-\log p_k(X_0). \]

G₀ is trivial. For each a, p_k(a) is a [0,1]-valued martingale, converging almost surely and in L¹ to p∞(a) by Chapter 15. Countably many letters admit a common null set. Since P(X₀=a,p∞(a)=0)=E[p∞(a)1_{p∞(a)=0}]=0, the limiting probability of the actual symbol is positive, as is every finite-stage probability. Thus I_k is finite, nonnegative and tends to I∞.

For p₀(a)>0 and t≥0, let τ_a be the first k with p_k(a)<e⁻ᵗp₀(a). Each event {τ_a=k} lies in G_k. Conditioning term by term gives P(X₀=a,τ_a≤N)=Σₖ≤N E[p_k(a)1_{τ_a=k}]≤e⁻ᵗp₀(a). Increase N and sum over a to obtain the exponential tail below. This is an explicit discrete stopping test, not an unproved logarithmic martingale inequality.

\[ R=\sup_{k\ge0}\left(\log\frac{p_0(X_0)}{p_k(X_0)}\right)^+,\qquad P(R>t)\le e^{-t},\qquad 0\le I_k,I_\infty\le I_0+R,\qquad E(I_0+R)\le H(X_0)+1. \]

Dominated convergence now gives I_k→I∞ in L¹. The chain rule and stationarity yield H_n=Σⱼ<n EI_j and h=EI∞. The same envelope controls the pathwise triangular average. Knowing only EI_k≤H(X₀) would not suffice, since L¹ boundedness does not guarantee uniform integrability.

## 3. Maker’s lemma and all limits in SMB

<a id="entropy-proof-smb"></a>

The triangular-average lemma is as follows. If f_j→f almost surely and sup_j|f_j|≤F∈L¹, then n⁻¹Σⱼ<n f_j∘Tʲ→E[f|I] almost surely and in L¹. Fix K. The first K terms vanish pathwise after division by n; the remaining error is bounded by A_ng_K, with g_K=sup_{j≥K}|f_j−f|≤2F. Birkhoff bounds its upper limit by E[g_K|I]. Since g_K decreases to zero, conditional dominated convergence makes the bound decrease to zero almost surely. For L¹, the error is at most n⁻¹Σ‖f_j−f‖₁→0, in addition to the L¹ convergence of A_nf.

The conditional probability chain rule holds for each length and each of its countably many words. Stationarity identifies the jth factor with the shifted version p_j(X₀)∘Tʲ. A countable intersection handles words, lengths and shifts; actually observed zero-probability words form one null set. The following is therefore an exact almost-sure identity. The lemma and integrable envelope prove SMB.

\[ -\log P(X_0,\ldots,X_{n-1})=\sum_{j=0}^{n-1}I_j\circ T^j,\qquad -\frac1n\log P(X_0,\ldots,X_{n-1})\to E[I_\infty\mid\mathcal I]\quad\text{a.s. and in }L^1. \]

Under ergodicity the limit is h=EI∞. For δ,ε>0 and large n, actual words of probability at least 1−ε satisfy e^{-n(h+δ)}≤P(word)≤e^{-n(h−δ)}. Their number lies between (1−ε)e^{n(h−δ)} and e^{n(h+δ)}. Use the upper word-probability bound for the count lower bound, and the lower probability bound plus total mass at most one for the count upper bound. This identifies an effective exponential number of records, not equiprobability of all words or a complete lossless-coding theorem.

## 4. Measure entropy and the generator theorem

<a id="entropy-proof-generator"></a>

For any probability-preserving T and a finite or countable finite-entropy partition P, put P^n=∨ⱼ<n T⁻ʲP and h(T,P)=lim H(P^n)/n. Subadditivity gives existence without invertibility. Define h(T) as the supremum over finite partitions. An invertible measure-preserving isomorphism modulo null sets matches partitions and all their preimages, hence preserves h(T); no topological dynamical theorem is needed.

Now assume T invertible, P countable with H(P)<∞, and that all its integer translates generate F modulo null sets. For any finite Q put R_m=∨_{j=-m}^mT⁻ʲP. Conditional probabilities of Q given R_m converge to its indicators by Chapter 15. Conditional entropy is bounded by log|Q|, so H(Q|R_m)→0 by domination. For n-block joins, the conditional chain rule and reduction by additional information give H(Q^n)≤H(R_m^n)+nH(Q|R_m).

R_m^n joins P from time −m to n−1+m. Invertibility and preservation make its entropy H(P^{n+2m}). Divide by n and increase n to obtain h(T,Q)≤h(T,P)+H(Q|R_m); then increase m, giving h(T)≤h(T,P). The reverse is immediate for finite P. For countable P, coalesce all but the first l atoms into P_l. Then H(P|P_l)=H(P)−H(P_l)→0. The same chain bound gives h(T,P)≤h(T,P_l)+H(P|P_l)≤h(T) plus this error. Increasing l proves the reverse inequality and completes the generator theorem.

## 5. Examples, dependencies and unproved extensions

<a id="entropy-proof-boundary"></a>

The coordinate partition of a two-sided independent Bernoulli process generates all information and H_n=nH(p), so its system entropy is H(p). Every joint partition of the two-point swap has at most two atoms, so its block entropy is at most log2 and system entropy is zero. For a mixture of biases, past frequencies recover Θ by the conditional strong law, giving p∞(1)=Θ and conditional information rate H(Θ). Biases 1/4 and 3/4 have equal entropies, so a constant information rate still does not imply ergodicity.

Dependencies are nonnegative integration and dominated convergence from Chapter 6, conditional probabilities from Chapters 9–10, conditional independent strong laws from Chapter 12, increasing-information martingale convergence from Chapter 15, and Birkhoff proved in this chapter. The logarithmic envelope is established here, without future exchangeability or an unproved entropy variational principle. General relative entropy, infinite-entropy and group-action variants and the topological variational principle are not claimed. Conditions and concepts can be compared with [Hochman’s author notes](https://math.huji.ac.il/~mhochman/courses/dynamics2014/notes.5.pdf); the proofs here are independently organized. [Return to the chapter’s conclusion](../chapters/41-ergodic-theory.md#ergodic-insight).
