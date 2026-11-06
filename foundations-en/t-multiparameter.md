# T-MULTIPARAMETER: Rectangular Averages of Commuting Preserving Maps

This page proves [the multiparameter result](../chapters/41-ergodic-theory.md#ergodic-multiparameter). Fix finite d and commuting probability-preserving T₁,…,T_d, not necessarily invertible. Let 1<p<∞ and f∈Lᵖ. All integer side lengths may vary independently; the limit means min n_i→∞.

## 1. Commuting projections and their identification

<a id="multiparameter-proof-projections"></a>

Put U_if=f∘T_i, let A^i_n be the one-dimensional averages and P_i=E[·|I_i]. T-ERGODIC proves strong Lᵖ convergence A^i_n→P_i, with all operator norms at most one. Commutation of the U_i gives commutation of their averages. First fix m and increase n, then increase m. Strong convergence and uniform boundedness give P_iP_j=P_jP_i; the same argument shows that P_i commutes with U_j.

On L² the P_i are commuting orthogonal projections. The range of P=P₁…P_d is precisely the joint fixed space: each P_i fixes its output and P retains every jointly fixed vector. P is self-adjoint and idempotent, hence projection onto L²(J), J=∩I_i. Bounded functions and Lᵖ approximation identify P=E[·|J] on every Lᵖ. Commutation matters: a product of arbitrary conditional expectations is not automatically projection onto the intersection sigma algebra.

## 2. Controlling every rectangle at once

<a id="multiparameter-proof-maximal"></a>

\[ M_i g=\sup_{n\ge1}A_n^i|g|,\qquad |A_{\mathbf n}f|\le M_1M_2\cdots M_d|f|,\qquad \|M_1\cdots M_d|f|\|_p\le\left(\frac p{p-1}\right)^d\|f\|_p. \]

The first inequality uses positivity: under each fixed outer average, bound every choice of an inner length by its supremum. Apply the one-dimensional strong bound successively. The M_i are nonlinear; they have not been treated as commuting linear projections, only composed in a fixed order. Countably many multi-indices make the maximal function measurable and almost surely finite.

## 3. A dense class, the joint limit and Lᵖ convergence

<a id="multiparameter-proof-limit"></a>

For bounded f, expand f−Pf=Σ_i P₁…P_{i−1}(I−P_i)f. The one-dimensional mean theorem approximates each residual by f−A^i_nf. Finite algebra gives f−A^i_nf=(I−U_i)g_{i,n}, with bounded g_{i,n}=Σ_{k=0}^{n−2}(n−1−k)U_i^kf/n. Earlier projections commute with U_i and preserve boundedness. Thus f is approximated in Lᵖ by bounded jointly fixed functions plus Σ_i(I−U_i)g_i with bounded g_i. Truncation gives density for arbitrary Lᵖ. We have not mistaken L² density for automatic density when p>2.

For each such coboundary, commutation lets the ith average telescope and the remaining averages do not enlarge the bound: its rectangular average is at most 2‖g_i‖∞/n_i. This proves a joint almost-sure limit on the dense class. For general f, the tail oscillation is bounded by 2M₁…M_d|f−h|. Markov’s inequality bounds the probability of exceeding ε by a constant times ε^{-p}‖f−h‖ₚ^p. Approximation and countably many ε prove one finite limit along all rectangles with min n_i→∞.

Identify the Lᵖ limit directly. Telescope the difference of the two products of A^i_{n_i} and P_i. Commutation and contraction bound its norm by Σ_i‖(A^i_{n_i}−P_i)f‖ₚ→0. Thus the limit is Pf=E[f|J], and uniqueness in probability identifies the pointwise limit as well. A joint limit has not been replaced by iterated limits. Endpoint L¹ for all rectangles, general-group Følner sequences and ratio theorems lie outside this page. [Return to the text](../chapters/41-ergodic-theory.md#ergodic-entropy).
