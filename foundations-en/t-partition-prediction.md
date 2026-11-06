# T-PARTITION-PREDICTION: EPPFs, Ewens and Two-Parameter Prediction

This proof does not repeat the Dirichlet-process construction of Chapter 44. It starts from partitions rather than labels to establish the relation between prediction, finite probabilities and frequencies. Return to [Chapter 47](../chapters/47-partitions.md#partitions-ewens).

## 1. Why the EPPF recursion constructs an infinite partition

<a id="partition-proof-eppf"></a>

Let p be a nonnegative symmetric function on all finite vectors of positive integers, with p(1)=1 and the addition rule below. Assign p of the block sizes to each specified partition of [n]. Its extensions to [n+1] add the new label to one old block or create a new block. The rule says their probabilities sum to the old probability. Induction establishes total mass one at every n. Symmetry gives exchangeability, recursion gives consistency, and the countable construction in T-PAINTBOX gives the unique infinite law.

\[ p(n_1,\ldots,n_k)=\sum_{j=1}^k p(n_1,\ldots,n_j+1,\ldots,n_k)+p(n_1,\ldots,n_k,1). \]

When p>0, extension probabilities are the right-hand terms divided by p. A zero-probability state can be completed by any legitimate extension kernel. Conversely, equal-sized specified partitions are related by a finite relabeling, so any infinite exchangeable partition defines such a p. Decomposing extension events proves the recursion. These are sufficient and necessary EPPF conditions, not merely a normalization check on one example.

## 2. From specified partitions to the Ewens sampling formula

<a id="partition-proof-ewens"></a>

Write θ>0 for the one-parameter concentration of Chapter 44, renaming that chapter’s α to avoid confusion with the discount below. Its already established probability of a specified partition is as follows. Now Aⱼ denotes the number of sample blocks of size j, not the index of a particular table.

\[ p_\theta(n_1,\ldots,n_k)=\frac{\theta^k}{\theta^{\uparrow n}}\prod_{i=1}^k(n_i-1)!,\qquad \theta^{\uparrow n}=\prod_{r=0}^{n-1}(\theta+r). \]

If Σj aⱼ=n, order the n labels and cut them into groups of the required lengths. Permuting the j members within a group, or the aⱼ equal-length groups, leaves the partition unchanged. Divide n! by these factors, multiply by the probability of each specified partition, and cancel j! against (j−1)! to obtain Ewens. Normalization follows from the CRP or the recursion above, not an unproved combinatorial identity.

\[ \mathbb P\{A_j=a_j,1\le j\le n\}=\frac{n!}{\theta^{\uparrow n}}\prod_{j=1}^n\frac{\theta^{a_j}}{j^{a_j}a_j!},\qquad \sum_{j=1}^n j a_j=n. \]

In paintbox terms its ranked masses are the decreasing rearrangement of Chapter 44’s discovery-order GEM(0,θ) masses, called PD(0,θ). The actual vanishing-residual proof is in T-STICK-BREAKING and T-CRP: no dust, but infinitely many positive-mass blocks. The probability that n specified labels share a block also gives EΣSⱼⁿ=(n−1)! divided by the rising factorial of θ+1 of order n−1. This sampling interpretation does not make ranked masses independent.

\[ \mathbb E\sum_jS_j^n=p_\theta(n)=\frac{(n-1)!}{(\theta+1)^{\uparrow(n-1)}},\qquad n\ge1. \]

## 3. A precise two-parameter extension

<a id="partition-proof-two-parameter"></a>

Take 0≤α<1, with θ>0 when α=0 and θ>−α when α>0. With n customers in k blocks, old block j has weight nⱼ−α and a new block has weight θ+αk, divided by θ+n. These probabilities are strictly positive and sum to one, so sequential kernels construct an infinite partition. Multiplying along a seating history gives factors 1−α through nⱼ−1−α for each block and θ+α through θ+(k−1)α for new blocks. This yields the symmetric EPPF below.

\[ p_{\alpha,\theta}(n_1,\ldots,n_k)=\frac{\prod_{i=1}^{k-1}(\theta+i\alpha)}{(\theta+1)^{\uparrow(n-1)}}\prod_{j=1}^k(1-\alpha)^{\uparrow(n_j-1)}. \]

The first customer has probability one, and empty products are one, so n=1 is nonsingular. Extension ratios equal the stated weights, proving recursion and exchangeability. The range includes zero or negative θ when α>0, but not arbitrary real parameters. This page does not classify negative-discount finite-species models, the α=1 endpoint or all Gibbs partitions. Local normalization alone does not guarantee exchangeability; symmetry of the whole history product proves it separately.

## 4. Deleting the first block proves independent residual allocation

<a id="partition-proof-deletion"></a>

When the first block contains n₁ customers and the rest r=n−n₁, the next customer enters it with probability (n₁−α)/(θ+n), and avoids it with probability (θ+α+r)/(θ+n). Starting with customer two, independently construct these indicators as a two-color Pólya scheme with initial masses (1−α,θ+α). Its uniforms are independent of a restaurant with parameters (α,θ+α).

Conditional on avoiding the first block, the other old blocks have weights (nⱼ−α)/(θ+α+r), and a new block has weight (θ+α+αk′)/(θ+α+r), where k′ counts the other blocks. These are exactly the residual restaurant rules. Interleaving its customers using the two-color indicators factors every finite history probability into the original kernels. Cylinder uniqueness proves equality of infinite laws, and genuine independence of the first-block indicator sequence and the residual partition.

The finite Dirichlet/Beta mixture and conditional strong law of Chapter 44 apply to arbitrary positive initial masses. Thus the first-block density V₁ is Beta(1−α,θ+α), strictly between zero and one. Infinitely many residual customers remain. Repeat the decomposition on their own time axis. Finite-level product induction and a countable common probability-one set give independent Vⱼ and the discovery-order frequencies Pⱼ.

\[ V_j\sim\operatorname{Beta}(1-\alpha,\theta+j\alpha)\ \text{independently},\qquad P_j=V_j\prod_{i<j}(1-V_i). \]

## 5. Why the frequencies really sum to one

<a id="partition-proof-total-mass"></a>

For α=0 the Vⱼ are iid with positive mean, so their sum diverges by the strong law. For α>0 put a=1−α. Beta integrals give EVⱼ=a/(θ+1+(j−1)α), whose sum diverges, and EVⱼ²=a(a+1) divided by (θ+1+(j−1)α)(θ+2+(j−1)α), whose sum is finite. Chapter 12’s finite-variance criterion for independent centered series gives convergence of Σ(Vⱼ−EVⱼ), hence divergence of ΣVⱼ. No future stable-subordinator construction is used.

\[ 0\le\prod_{j=1}^m(1-V_j)\le\exp\!\left(-\sum_{j=1}^m V_j\right)\longrightarrow0,\qquad \sum_{j\ge1}P_j=1\quad\text{a.s.} \]

Every recursively first block has positive density and appears at a finite time. Absolute frequencies of any fixed finite set of blocks follow by multiplying densities along the compressed time axes, giving Pⱼ. The displayed limit excludes any residual dust. Ranking defines PD(α,θ), while discovery order defines GEM(α,θ). This proves the frequency representation of this predictive law, not that every exchangeable partition belongs to the two-parameter family.

## 6. Consistency and identification boundaries

<a id="partition-proof-boundaries"></a>

Normalization is insufficient: make the first two customers share a block with probability one half. If they share, the third joins them; if they differ, the third joins the first customer’s block. Then the specified partition {1,3}|{2} has probability one half, whereas {1,2}|{3} has probability zero. Every step is a legitimate kernel, but the resulting partition is not exchangeable.

Ewens here concerns table partitions, or equality partitions with nonatomic labels. With an atomic base in Chapter 44, different tables can have equal labels; the observed partition is a coarsening and need not have the same EPPF. Two-parameter prediction is not automatically the law of a Kingman coalescent at a fixed time. The mutation relation is constructed separately in T-COALESCENT-MUTATION. General Λ/Ξ coalescents, fragmentation and hierarchies remain the responsibility of Chapter 56.
