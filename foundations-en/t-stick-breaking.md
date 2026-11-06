# Random Weights, Stick-Breaking and Dirichlet Identification

## 1. Why cutting the remainder leaves total mass one

<a id="stick-proof-mass"></a>

Fix α>0. Take independent Vⱼ∼Beta(1,α), of density α(1−v)ᵅ⁻¹ on (0,1), and iid labels Zⱼ∼H independent of all breaks. Chapter 8 supplies the product space. The jth weight is cut from the current remainder, not directly from the original unit mass.

\[ R_m=\prod_{j=1}^m(1-V_j),\qquad P_j=V_j\prod_{i<j}(1-V_i),\qquad \sum_{j=1}^mP_j=1-R_m. \]

Direct integration gives E(1−V)=α/(α+1). Independence yields ERₘ=(α/(α+1))ᵐ. The decreasing sequence has nonnegative limit R∞; bounded convergence gives ER∞=0, hence R∞=0 almost surely and Rₘ→0 in L¹. Positivity of all weights and total mass one hold on one common full set. Endless cutting alone would not prove this.

## 2. Pointwise probabilities and measurable evaluations

<a id="stick-proof-measure"></a>

\[ G=\sum_{j\ge1}P_j\delta_{Z_j}. \]

On the full set above this defines a countably additive probability at every sample point: nonnegative double series may be interchanged over disjoint Aₖ. The bad set is measurable and depends only on weights; use G=δe₀ there. Every G(A) is a measurable series limit, making G a P(E)-valued variable for the evaluation σ-field. Singletons are measurable in a standard Borel space, and G is concentrated on an at most countable random set.

Weight-label independence, Tonelli and ΣPⱼ=1 give EG(A)=H(A). A diffuse H is compatible with every G being discrete. Averaging random atom locations does not turn each realization into a continuous density.

## 3. Exact identification of a finite-dimensional fixed point

<a id="stick-proof-fixedpoint"></a>

For a partition \(A_1,\ldots,A_d\) put hⱼ=H(Aⱼ) and aⱼ=αhⱼ. After deleting the first break and label, the renormalized tail is an independent copy. Its mass vector satisfies the identity below, with V,J,Y′ independent and P(J=j)=hⱼ. Remove zero-hⱼ coordinates, whose masses are zero. A single remaining coordinate is deterministic.

\[ Y\overset d=V e_J+(1-V)Y^\prime,\qquad V\sim\operatorname{Beta}(1,\alpha). \]

Verify independently that Dir(a) is also a fixed point. Take independent Gamma(aⱼ,1) variables Uⱼ, S=ΣUⱼ, D′=U/S, and an independent Gamma(1,1) variable T. The finite Gamma proof gives independence of S and D′. Hence V=T/(T+S) is Beta(1,α), independent of D′. For fixed J=j, the vector V eⱼ+(1−V)D′ replaces Uⱼ by Uⱼ+T before normalization, so has law Dir(a+eⱼ).

\[ f_{a+e_j}(y)=\frac{\alpha}{a_j}y_jf_a(y),\qquad \sum_j h_j f_{a+e_j}(y)=\sum_j y_jf_a(y)=f_a(y). \]

The mixture weights are exactly the law of J, proving the fixed-point identity for Dir(a). Densities are interpreted on the positive-parameter face; no division by a zero shape is made.

## 4. Uniqueness makes the weighted measure a DP

<a id="stick-proof-unique"></a>

For two fixed-point laws ρ,ρ′ on the simplex, iterate m times with shared breaks and labels, then attach independent tail vectors U,U′ of those respective laws. The iterated identity keeps the two output laws unchanged; only the Rₘ-weighted tails differ.

\[ \left\|\sum_{j=1}^mP_je_{J_j}+R_mU-\sum_{j=1}^mP_je_{J_j}-R_mU^\prime\right\|_1\le2R_m,\qquad ER_m\longrightarrow0. \]

Every continuous f is uniformly continuous on the compact simplex, so this coupling makes the difference of expectations tend to zero. The two laws do not depend on m; their continuous integrals are equal. Approximate closed-set indicators by max(0,1−r dist(x,C)), then use π–λ to identify the laws. Thus every partition vector is Dir(a), and evaluation-cylinder uniqueness gives G∼DP(α,H). No partition-classification theorem is used.

## 5. Index order, collisions and the roles of the constructions

<a id="stick-proof-order"></a>

Weights are indexed in break order, not decreasing size. The event V₁<1/10,V₂>1/2 has positive probability and gives P₂>P₁. Labels may repeat when H has atoms; their weights must be added at the shared point. Break indices are not ranked atoms and cannot without proof be identified with newly observed categories.

The predictive–de Finetti route establishes a director for the updating rule. The Gamma fixed-point argument here supplies explicit random weights. T-CRP separately proves why frequencies in table-creation order have the same residual-allocation law; that ordering statement has not been assumed here. Return to [stick-breaking in Chapter 44](../chapters/44-dirichlet-process.md#dirichlet-stick).
