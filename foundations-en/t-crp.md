# Table Partitions, Labels, EPPFs and Frequencies in Creation Order

## 1. Construct partitions before proving exchangeability

<a id="crp-proof-eppf"></a>

Fix α>0. Partition {1,…,n} into tables, indexed by least member, equivalently creation order. The first customer opens a table. At n≥1 the next joins table j with probability nⱼ/(α+n), or opens a new table with probability α/(α+n). The countable-state normalized kernels and Chapter 8 construction produce an infinite consistent partition.

\[ P(\Pi_n=\pi)=p(n_1,\ldots,n_k)=\frac{\alpha^k}{(\alpha)^{\uparrow n}}\prod_{j=1}^k(n_j-1)!,\qquad n\ge1. \]

For a specified partition π multiply probabilities in customer order. Each new table contributes α, later joins contribute 1 through nⱼ−1, and the denominator is (α)↑n. The first α cancels its denominator factor. Dependence only on unordered block sizes proves permutation invariance and defines the exchangeable partition probability function, or EPPF. It is the probability of a specific partition, not the probability of a list of block sizes, which requires counting partitions.

\[ p(n_1,\ldots,n_k)=\sum_{j=1}^k p(n_1,\ldots,n_j+1,\ldots,n_k)+p(n_1,\ldots,n_k,1). \]

The extension ratios are nⱼ/(α+n) and α/(α+n), summing to one. This proves sampling consistency when the last label is deleted; set the empty-partition probability to one. Consistency and finite permutations give exchangeability of the entire partition without a Chapter 47 paintbox theorem.

## 2. Labeling tables is not the same as partitioning equal observations

<a id="crp-proof-labels"></a>

Preassign iid labels Zⱼ∼H independently of Π; each customer receives the label of their table. Equivalently, use a fresh uniform variable for innovation, then either open a table or choose a previous customer uniformly and copy their table. Given the seating and used labels, the next value has law (αH+ΣδXᵢ)/(α+n), depending only on observed values. The tower therefore gives the same predictive kernel Qₙ, and sequential uniqueness identifies the Pólya record law.

\[ P(X_1\in A_1,\ldots,X_n\in A_n)=\sum_{\pi\in\mathcal P_n}\frac{\alpha^{|\pi|}}{(\alpha)^{\uparrow n}}\prod_{B\in\pi}\left[(|B|-1)!\int_E\prod_{i\in B}\mathbf1_{A_i}(z)H(dz)\right]. \]

This finite sum integrates independent table labels for each seating partition and remains valid for atomic H. When H is diffuse, countably many iid labels are almost surely distinct, so table blocks equal equal-value blocks. In general the latter is only the coarsening obtained by merging tables with repeated labels.

\[ c_H=P(Z_1=Z_2)=\int H(\{z\})H(dz),\quad P(X_1=X_2)=\frac1{\alpha+1}+\frac{\alpha}{\alpha+1}c_H. \]

The diagonal is measurable in a standard Borel space, and Tonelli gives the first identity. Positive-mass atoms are at most countable, so the collision probability is also the sum of squared atomic masses. The second identity separates same-table and different-table cases. The chance of a new table is α/(α+n); a new observed value instead has probability αH(E minus {X₁,…,Xₙ})/(α+n). With H=δz every observation equals z even while tables continue to appear.

## 3. Deleting the first table reveals the same residual problem

<a id="crp-proof-deletion"></a>

Let Iᵢ indicate membership in the first table, with I₁=1. With n₁ first-table customers and r=n−n₁ others, the next joins the first with probability n₁/(α+n) and avoids it with probability (α+r)/(α+n). Given avoidance, residual tables have probabilities nⱼ/(α+r) and α/(α+r), exactly the original CRP with r previous customers.

Independently generate a two-color Pólya sequence I₂,I₃,… with initial masses (1,α), and a separate CRP for the compressed non-first-table customers. Interleave them according to I. The one-step kernels just computed match the original CRP at every step, so the full laws coincide. This proves independence of the first-table indicator process and residual CRP, rather than inferring independence from marginal rules. Finite Dirichlet mixing and the strong law give first-table frequency V₁∼Beta(1,α), lying strictly between zero and one.

The residual proportion 1−V₁ is positive, so its compressed record is infinite. Repeat on the independent residual CRP to obtain independent Beta(1,α) variables V₂,V₃,…. Independence at each finite depth follows inductively from the product construction, and a countable common full set handles all depths. Every fixed table has positive limiting density and therefore appears at a finite time.

\[ \frac{N_j(n)}n\longrightarrow P_j=V_j\prod_{i<j}(1-V_i)\quad\text{a.s. for every }j,\qquad \sum_{j\ge1}P_j=1. \]

Multiply each compressed frequency by the density of its subsequence to obtain the formula. Total mass one follows from the residual-mass proof in T-STICK-BREAKING, not from existence of individual table frequencies alone. This identifies residual allocation in creation order; it does not claim independence of ranked frequencies. Frequencies are functions of Π alone and remain independent of all preassigned labels.

## 4. Identifying empirical probabilities with random atoms

<a id="crp-proof-identification"></a>

Put qⱼ(n)=Nⱼ(n)/n, zero for tables not yet created. Both q(n) and P are probabilities on the positive integers. For a fixed J the first J coordinates converge and each tail is one minus its head sum. Bound the ℓ¹ difference by the finite head error and the two tails; first let n grow, then J. This proves ℓ¹ convergence.

\[ \sum_{j\ge1}|q_j(n)-P_j|\longrightarrow0,\qquad d_{\rm TV}\!\left(\frac1n\sum_{i=1}^n\delta_{X_i},\sum_{j\ge1}P_j\delta_{Z_j}\right)\le\frac12\sum_{j\ge1}|q_j(n)-P_j|\longrightarrow0. \]

Pushing through the label map only merges coordinates and cannot increase total variation; splitting positive and negative errors proves the bound directly. Thus G*=ΣPⱼδZⱼ is the common empirical limit. It agrees with the Chapter 43 director on a countable determining algebra and hence as a measure almost surely; observations are conditionally iid given G*. With label collisions, individual table frequencies are not recoverable from values. The identifiable probability is the coarsened G*.

This does not contradict the continuous-uniform director counterexample in Chapter 43. Here every director is discrete, so a finite head captures arbitrarily much mass. The bound holds for all A at each good sample point because of countable ℓ¹ control, not an intersection of uncountably many strong-law full sets.

## 5. Table growth comes from independent innovations

<a id="crp-proof-count"></a>

Fresh uniform innovation decisions make the opening indicators Bᵢ independent Bernoulli(α/(α+i−1)), with B₁=1. These indicate innovation, not table membership. The divergent probability sum and the second Borel–Cantelli lemma give infinitely many tables. Their sum Kₙ has mean αlog n+O(1) and variance at most its mean.

\[ EK_n=\sum_{i=1}^n\frac{\alpha}{\alpha+i-1},\qquad \frac{K_n}{\log n}\longrightarrow\alpha\quad\text{a.s.} \]

The mean asymptotic follows by a summable comparison with α/i. For nₘ=⌊exp(m²)⌋, Chebyshev bounds the probability of |Kₙₘ−EKₙₘ|>εlog nₘ by O(m⁻²). Borel–Cantelli gives the subsequence limit. Monotonicity of Kₙ and log nₘ₊₁/log nₘ→1 extend it to all n. For diffuse H this also counts distinct observed values; for atomic H it need not.

## 6. Parameter range and the boundary of later partition theory

<a id="crp-proof-scope"></a>

Only α>0, zero-discount one-parameter CRP and DP are established here. Nonzero-discount two-parameter CRPs, Pitman–Yor, general paintboxes and EPPF classification belong to associated Chapter 47 partition work and are not counted as proved by naming them. The proof uses finite Dirichlet theory, sequential kernels, conditional probabilities, strong laws, Borel–Cantelli and countable weights. Return to [tables and labels in Chapter 44](../chapters/44-dirichlet-process.md#dirichlet-tables).
