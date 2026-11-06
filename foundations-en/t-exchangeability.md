# Finite Symmetry, Sampling without Replacement and Bernoulli Representation

## 1. The action of finite permutations

<a id="exchange-proof-average"></a>

Let Ω be the countable record product over a nonempty standard Borel space E, with coordinates X. A finite permutation π fixes all but finitely many positive integers; Sπ replaces coordinate i by coordinate π(i). An exchangeable law P is preserved by every Sπ. The finite permutations form a countable group, and Sₙ permutes only the first N coordinates. Here N is an integer, not a stopping time.

\[ \mathcal G_N=\{A:S_\pi^{-1}A=A\text{ for every }\pi\in S_N\},\quad \mathcal J=\bigcap_{N\ge1}\mathcal G_N,\quad A_NF=\frac1{N!}\sum_{\pi\in S_N}F\circ S_\pi. \]

These are sub-σ-fields of the raw record σ-field. The finite average AₙF is group invariant and hence Gₙ-measurable. Every A∈Gₙ gives the integral identity below by measure preservation. Thus symmetrization is genuinely conditional expectation. Monotone convergence extends the bounded case to nonnegative F.

\[ \int_A A_NF\,dP=\frac1{N!}\sum_{\pi\in S_N}\int_A F\circ S_\pi\,dP=\int_A F\,dP,\qquad E[F\mid\mathcal G_N]=A_NF. \]

As the group grows, its invariant σ-field shrinks. Chapter15 gives almost sure and L¹ convergence to E[F|J] for bounded F. We intersect the raw σ-fields first, and compare completions only afterwards; no general future group-invariance theorem or hidden null-set interchange is used.

## 2. The exact finite-population law

<a id="exchange-proof-urn"></a>

For an exchangeable Bernoulli vector of length N let K count its ones. Words with the same K have equal probability. Conditional on any K=j of positive probability, they are uniform. Conversely any distribution of K followed by a uniform word of that composition gives an exchangeable law. Conditional versions at zero-probability K-values are arbitrary.

\[ P(X_1=x_1,\ldots,X_k=x_k\mid K=j)=\frac{(j)_r(N-j)_{k-r}}{(N)_k},\quad r=\sum_{\ell=1}^k x_\ell,\quad (a)_r=a(a-1)\cdots(a-r+1). \]

This is the probability of drawing ordered positions without replacement, for k≤N. A zeroth falling factorial is one; impossible words have probability zero. It is not the independent Bernoulli formula with p=j/N, since the remaining composition changes after a draw.

## 3. The replacement error

<a id="exchange-proof-replacement"></a>

\[ L_N=\frac1N\sum_{i=1}^N\delta_{X_i},\qquad c_{k,N}=\min\left(1,\frac{k(k-1)}{2N}\right). \]

Fix 1≤k≤N and a record, and draw k independent uniform indices I. A union bound over equal pairs gives collision probability at most c. Conditional on no collision, I is uniform among ordered distinct indices. Set J=I on that event; after a collision draw an independent uniform distinct tuple. J has the without-replacement law and differs from I with probability at most c. Nothing here assumes that the record itself is independent.

\[ \left|\frac1{(N)_k}\sum_{\substack{i_1,\ldots,i_k\le N\\\text{all distinct}}}\prod_{\ell=1}^k f_\ell(X_{i_\ell})-\prod_{\ell=1}^k L_N f_\ell\right|\le c_{k,N}\qquad(0\le f_\ell\le1). \]

The same index coupling applies to arbitrary measurable vector events, not just products. Take the indices independent of the record. Exchangeability identifies the unconditional without-replacement law with the first k observations; conditional replacement sampling has the empirical product law.

\[ d_{\rm TV}\left(\mathcal L(X_1,\ldots,X_k),\,E[L_N^{\otimes k}]\right)\le c_{k,N}. \]

The bound also holds for a merely finite exchangeable N-vector. It is an approximation, not an exact infinite representation. For signed functions bounded in absolute value by one, the product discrepancy bound becomes 2c. The main proof uses indicators between zero and one, so no constant is silently changed.

## 4. The Bernoulli converse in full

<a id="exchange-proof-bernoulli"></a>

Now let the Bernoulli record be infinite and exchangeable. The finite averaging identity identifies its frequency with E[X₁|Gₙ]. Reverse martingale convergence gives a [0,1]-valued Θ. Set Θ=0 on records without a limit. Finite permutations or removal of a finite prefix change neither existence nor value of the frequency limit, so this version is raw J-measurable and tail-measurable.

\[ \frac{K_N}{N}=E[X_1\mid\mathcal G_N]\longrightarrow\Theta\quad\text{a.s. and in }L^1. \]

Fix a binary word x of length k with r ones. Let gₙ be its finite symmetrized conditional probability. The index coupling bounds its difference from (Kₙ/N)ʳ(1−Kₙ/N)ᵏ⁻ʳ by c, so gₙ converges to Θʳ(1−Θ)ᵏ⁻ʳ. Multiply the conditional identity by any bounded Borel h(Θ), which is Gₙ-measurable, and pass to the limit by DCT. This proves actual conditional iid.

\[ E[h(\Theta)\mathbf1_{\{X_{1:k}=x\}}]=E[h(\Theta)\Theta^r(1-\Theta)^{k-r}],\quad P(X_{1:k}=x\mid\Theta)=\Theta^r(1-\Theta)^{k-r}. \]

There are countably many finite binary words, so a common null set suffices. Product-kernel uniqueness extends the conditional identities to the whole record. The law M of Θ gives the de Finetti mixture. Conversely each iid product law is permutation invariant, and integrating it against M preserves exchangeability.

\[ P(X_{1:k}=x)=\int_0^1 p^r(1-p)^{k-r}M(dp). \]

For any alternative mixture M′, first sample p and then iid Bernoulli(p). Chapter12 gives frequency limit p for each fixed p. This is a jointly measurable event and hence remains almost sure after integration over M′. Its law is therefore both M′ and the law M already determined by the record. Thus M′=M, without an unproved moment theorem.

## 5. Finite counterexamples and dependencies

<a id="exchange-proof-boundaries"></a>

The length-two law assigning half to 01 and 10 is exchangeable with covariance −1/4. An exchangeable extension of length n would give sum variance n(2−n)/4, impossible already at n=3. Pairwise independence does not suffice either: the length-three law uniform on 000,011,101,110 is exchangeable and pairwise independent. An infinite extension would have VarΘ=Cov(X₁,X₂)=0, hence Θ=1/2 and P(111)=1/8 rather than zero.

Dependencies are Chapters9,15,12, finite sums and Chapter42’s coupling inequality. The finite-group averaging argument is proved here, not borrowed from Chapter45. Return to [Chapter43](../chapters/43-exchangeability.md#exchange-bernoulli).
