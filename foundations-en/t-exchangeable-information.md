# Permutation-Invariant Information, Tails, Zero-One Laws and Prediction

## 1. Why three information σ-fields agree modulo null sets

<a id="exchange-info-fields"></a>

Work on the standard Borel canonical record space. J consists of events exactly invariant under all finite permutations, and T is the raw tail σ-field. A tail event can be expressed beyond the support of any such permutation, so T⊂J. Use the tail-measurable directing version constructed in T-DIRECTING-MEASURE, giving σ(ν)⊂T.

The reverse inclusion requires proof. For each fixed A∈J, the full-record conditional kernel gives K(ν,A)=E[1A|J]=1A almost surely. The left side is σ(ν)-measurable, so A equals a σ(ν)-event modulo P. This proves equality of the three P-completions.

\[ \overline{\sigma(\nu)}^{\,P}=\overline{\mathcal T}^{\,P}=\overline{\mathcal J}^{\,P}. \]

Each fixed A is compared with its own σ(ν)-version; no universal null set for uncountably many events is asserted. If invariance holds only modulo P for each finite permutation, taking the union of its inverse images under the countable group produces an exactly invariant representative equal modulo P. Thus the completed formulation includes this convention.

## 2. A direct proof of the Hewitt–Savage zero-one law

<a id="exchange-info-hs"></a>

Assume now that the coordinates are iid under the original probability. For A∈J and ε>0 choose a first-n-coordinate event B with P(A△B)<ε. Such an approximation follows from upward conditional expectation convergence in Chapter15, thresholding at one half.

Swap the first n coordinates with the next n and let B′ be the inverse image of B. Invariance of A and of the iid law gives P(A△B′)<ε. The two events depend on disjoint iid blocks, so they are independent and equally distributed. The following estimate forces PA to be zero or one.

\[ |P(A)-P(A)^2|\le |P(A)-P(B\cap B^\prime)|+|P(B)^2-P(A)^2|\le2\varepsilon+2\varepsilon. \]

The first term uses A△(B∩B′)⊂(A△B)∪(A△B′); the second uses |PB−PA|<ε and probabilities at most one. Let ε decrease to zero. Independence factors the blocks, while identical distribution preserves the approximation after swapping. This direct proof does not use de Finetti and creates no circular dependence.

## 3. Why iid cannot be omitted

<a id="exchange-info-counterexamples"></a>

Independence without identical distribution is insufficient. Let X₁ be fair Bernoulli and all other coordinates zero. The variables are independent, yet the exactly permutation-invariant event that the whole record contains precisely one one has probability one half. The permuted law is different, so the approximation-transfer step fails.

Nor does general exchangeability imply an unconditional zero-one law. Choose Θ=1/4 or3/4 with equal chances and then iid Bernoulli(Θ). The tail event that the limiting frequency exceeds one half has probability one half. Its conditional probability given Θ is zero or one. This distinguishes conditional iid from unconditional iid rather than contradicting the theorem.

For each fixed invariant event A, conditional product laws and Hewitt–Savage also give K(ν,A)∈{0,1}, consistently with the first section. Kolmogorov for tail events and Hewitt–Savage for permutation-invariant events have different event classes, even though both completed information fields are trivial for iid records.

## 4. Shifts, ergodicity and extreme exchangeable laws

<a id="exchange-info-extreme"></a>

Infinite exchangeability implies strict stationarity: a bijection between a finite set of distinct indices and its translate extends to a finite permutation. The converse fails. The alternating two-point system with uniform initial phase is stationary, but the words010 and its permutation001 have different probabilities. Independent records with unequal marginals need not be exchangeable either.

Let I be the shift-invariant σ-field modulo P. Empirical code limits are unchanged by shifting, so σ(ν)⊂I modulo null sets. For fixed A∈I, integrate P(A△T⁻¹A)=0 through the mixture. For M-almost every μ it is shift invariant modulo the product law. The iid shift is ergodic by Chapter41, so K(μ,A)∈{0,1}. A conditional probability taking only zero and one forces A to be σ(ν)-measurable modulo null sets.

\[ \overline{\mathcal I}^{\,P}=\overline{\sigma(\nu)}^{\,P},\qquad \text{an infinite exchangeable law is shift-ergodic iff }\nu\text{ is deterministic a.s.} \]

For the equivalence, trivial I makes all countably many determining evaluations constant, hence ν a fixed μ almost surely and the record iid(μ). The converse is the established iid-shift result. If ν is nondegenerate, some determining A has Varν(A)>0. Conditional iid makes the covariance of its indicators at any two distinct times equal to this positive number; it does not decay with separation.

\[ \operatorname{Cov}(\mathbf1_A(X_i),\mathbf1_A(X_j))=\operatorname{Var}(\nu(A))\qquad(i\ne j). \]

The extreme points of the convex set of exchangeable laws are precisely the iid products. A non-Dirac directing distribution can be split by a parameter event of probability strictly between zero and one, yielding two distinct exchangeable components. Conversely a convex decomposition of an iid product would decompose its uniquely determined Dirac mixing law, forcing both components to be the same product.

## 5. Updating predictions without redrawing the directing law

<a id="exchange-info-prediction"></a>

Let Fₙ contain the first n observations. Conditional iid first gives νf as the expectation of the next observation given both ν and the past. Prove this by testing against g(ν) times a bounded past function and integrating the conditional product law. Only then take the tower to Fₙ. The identity conditioned on ν alone would not by itself justify enlargement of the conditioning field.

\[ E[f(X_{n+1})\mid\mathcal F_n]=E[\nu f\mid\mathcal F_n]\longrightarrow\nu f\quad\text{a.s. and in }L^1\qquad(f\text{ bounded Borel}). \]

Upward martingale convergence applies because ν is measurable from the whole record, giving E[νf|F∞]=νf. The assertion is for each fixed f, or simultaneously for a countable determining class, not for all measurable f outside one universal null set.

For Bernoulli observations let M be the law of Θ. After a particular n-word containing k ones, the posterior is as below when the denominator is positive. A zero denominator corresponds to an impossible word and admits an arbitrary version. The Beta case returns to Chapter2 without repeating its integration.

\[ M_{n,k}(dp)=\frac{p^k(1-p)^{n-k}M(dp)}{\int_0^1 q^k(1-q)^{n-k}M(dq)},\qquad P(X_{n+1}=1\mid\mathcal F_n)=E[\Theta\mid\mathcal F_n]. \]

Arbitrary labels may remain unidentified: let Θ take ±a, 0<a<1, and generate Bernoulli(Θ²). The directing probability is the fixed Bernoulli(a²), and no amount of data reveals the sign. Uniqueness and empirical identification concern ν, not every extraneous parameterization. Return to [Chapter43](../chapters/43-exchangeability.md#exchange-prediction).
