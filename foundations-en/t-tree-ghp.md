# T-TREE-GHP: Coding Stability, Vertex Mass and the CRT Space Limit

This page proves all geometric and mass comparisons for the [final theorem of Chapter 55](../chapters/55-metric-measure-limits.md#geometry-crt-limit). Inputs are Chapter 53’s joint functional limit for conditioned finite-variance trees and Chapter 54’s deterministic real-tree construction. Space convergence is not used to prove the input functional limit. Independent expert final review of T-CONDITIONED-HEIGHT remains open.

## 1. Distortion of the same-time relation

<a id="treeghp-stability"></a>

Let E₀ be the space of continuous nonnegative functions on [0,1] vanishing at both endpoints, with uniform norm. Chapter 54 constructs pₕ:[0,1]→Tₕ, root pₕ(0) and μₕ=(pₕ)₊Leb. For h,g∈E₀ write δ for their uniform distance. Their minima over any interval differ by at most δ, so

\[ \begin{aligned}
m_h(s,t)&=\inf_{u\in[s\wedge t,s\vee t]}h(u),\\
d_h(s,t)&=h(s)+h(t)-2m_h(s,t),\\
|d_h(s,t)-d_g(s,t)|&\le4\delta .
\end{aligned} \]

The relation \(R=\{(p_h(t),p_g(t)):0\le t\le1\}\) is a compact rooted correspondence because both projections are continuous and onto. Its distortion is at most4δ. The two projections of the same U∼Uniform[0,1] define a mass coupling q with q(R)=1. Apply the joint criterion of T-GP-GHP with r=2δ, using positive slack if δ=0, to obtain

\[ d_{rGHP}(\Phi(h),\Phi(g))\le2\|h-g\|_\infty,\qquad
\Phi(h)=(T_h,d_h,p_h(0),(p_h)_*\mathrm{Leb}). \]

The constant uses the maximum convention; it cannot be transferred unchanged to a sum of three errors. Φ is Lipschitz into the rooted compact GHP space and therefore Borel measurable. This used an explicit simultaneous correspondence and coupling, not merely pointwise existence of quotients.

## 2. The contour quotient equals the edge-filled finite tree

<a id="treeghp-realization"></a>

Take a rooted plane tree with n≥2 vertices and edges of length a>0. Fill each edge by a closed interval to obtain a compact real tree T̄. Its depth-first contour traverses both directions of every edge, each in one time unit. Let q(u) be its position and C(u)=d(ρ,q(u)), for 0≤u≤2(n−1). Identifying the quotient with T̄ requires the minimum formula for times in edge interiors as well as for integer vertex times.

For any point z, the contour makes one uninterrupted depth-first visit to each component above z after z is deleted. Given x=q(u), y=q(v), u≤v, the continuous contour segment from x to y must pass their most recent common ancestor w. Its minimum height is at most |w|. For each strict ancestor z below w, both points belong to the same component above z and both times lie within its single visit interval; the contour cannot go below z between them. The minimum is at least |z|. Let z approach w along the ancestral segment. If w is the root, nonnegativity gives the same conclusion.

\[ d_{\overline T}(q(u),q(v))
=C(u)+C(v)-2\inf_{u\le r\le v}C(r). \]

The contour is continuous and onto. The identity makes zero pseudodistance equivalent to equality of visited points; factorization gives a rooted onto isometry from the coded tree to the edge-filled tree. With normalized time, the pushforward of Lebesgue measure is normalized edge-length measure: each edge is traversed twice at constant speed. It is not uniform vertex mass; for n≥2 those two measures are even mutually singular.

## 3. Vertex preorder and contour clocks

<a id="treeghp-clock"></a>

List preorder vertices v₀,…,vₙ₋₁ with edge-count heights Hⱼ. The first contour visit to vⱼ is at bⱼ=2j−Hⱼ, as established in Chapter 52. Directly, j downward steps have reached the nonroot vertices so far, while the Hⱼ steps on its ancestral chain have not been retraced; there have been j−Hⱼ upward steps. Write tⱼ for normalized visit times. For uniform U set J=⌊nU⌋; then vⱼ is selected with exactly uniform vertex probability.

\[ \begin{aligned}
t_j&=\frac{2j-H_j}{2(n-1)},\quad 0\le j<n,\\
\eta_n&=\frac1n+\max_{j<n}|t_j-j/n|\\
&\le\frac1n+\frac1{n-1}
+\frac{H_{\max}}{2(n-1)},\qquad |U-t_J|\le\eta_n .
\end{aligned} \]

Let h(t)=aC₀(2(n−1)t), where C₀ is the unit-edge contour. Under the isometry with the edge-filled tree, pₕ(tⱼ)=vⱼ. The distance between two contour positions is at most twice the height oscillation between their times. The same U thus couples vertex mass ν and contour mass λ with the deterministic bound

\[ \begin{aligned}
d(p_h(U),v_J)&\le2\omega(h,\eta_n),\\
\omega(h,\delta)&=\sup_{|s-t|\le\delta}|h(s)-h(t)|,\\
d_P(\nu,\lambda)&\le2\omega(h,\eta_n).
\end{aligned} \]

There is no claim that contour time samples vertices at a constant rate. The measures still have total variation distance1, yet their weak distance can be small because coupled positions are close in the tree metric. The Hausdorff distance from the vertex subspace to the edge-filled tree is at most a/2 and their roots agree. In the same background we obtain

\[ d_{rGHP}\big((V(T),ad_{\rm graph},\rho,\nu),\Phi(h)\big)
\le\max\{a/2,\ 2\omega(h,\eta_n)\}. \]

## 4. Rooted GHP convergence of conditioned finite-variance GW trees

<a id="treeghp-limit"></a>

Assume offspring law p has Eξ=1 and 0<Varξ=σ²<∞. Let n tend to infinity through the actual admissible sizes with P(|T|=n)>0, and let Tₙ be the conditioned tree. Maximal lattice span and admissibility are as in Chapter 53; no conditioning on zero-probability sizes is made. The case n=1 is irrelevant. Put aₙ=σ/(2√n) and give every vertex mass1/n. Chapter 53’s T-CONDITIONED-HEIGHT proves joint convergence of contour and height for the same conditioned tree, in particular

\[ h_n(t)=\frac{\sigma}{2\sqrt n}
C^{(n)}(2(n-1)t)\ \Rightarrow\ e(t)
\quad\text{in }C([0,1]),\qquad H_{\max}/\sqrt n=O_P(1). \]

Consequently ηₙ→0 in probability. Tightness in continuous-function space makes the following bound vanish by first choosing small δ and then letting n increase. This avoids assuming that a small random clock error automatically gives a small amplitude error.

\[ P(\omega(h_n,\eta_n)>\varepsilon)
\le P(\eta_n>\delta)+P(\omega(h_n,\delta)>\varepsilon),\qquad
\lim_{\delta\downarrow0}\limsup_nP(\omega(h_n,\delta)>\varepsilon)=0. \]

The simultaneous bound from the previous section therefore tends to zero in probability. The2-Lipschitz property of Φ and Chapter 24’s continuous mapping theorem give Φ(hₙ)⇒Φ(e). To return to vertex trees, use the metric small-perturbation lemma: if d(Xₙ,Yₙ)→0 in probability and Yₙ⇒Y, then every bounded Lipschitz f has expectation difference bounded by Lip(f)ε+2‖f‖∞P(d>ε). First let n increase and then ε decrease. Bounded Lipschitz tests characterize weak convergence on Polish spaces by Chapter 24.

\[ \boxed{\left(T_n,\frac{\sigma}{2\sqrt n}d_{T_n},
\rho_n,\frac1n\sum_{v\in T_n}\delta_v\right)
\ \Rightarrow\
(\mathcal T_e,d_e,\rho_e,\mu_e)
\quad\text{in }(K^r,d_{rGHP}).} \]

The root, whole-space geometry and original uniform vertex mass are controlled simultaneously in one comparison. Here e is the duration1 excursion with the standard Brownian normalization of Chapters 37,53,54, not2e. The factor n−1 occurs in the contour edge clock; spatial scaling uses √n. No almost sure convergence on the original probability spaces is asserted.

## 5. Dependency closure and unproved extensions

<a id="treeghp-boundary"></a>

The chain is: Chapter 53’s conditional bridge, cut and joint height limit to the clock coupling; Chapter 54’s real trees to coding stability; this chapter’s GH, Prokhorov and GHP results to a common topology and measurability; Chapter 24 to continuous mapping and small perturbations. The ancestral reweighting, tightness and uniform-error arguments of the Chapter 53 height proof were actually read for these inputs; no blocking gap was found in this round. This is not external expert final review. Infinite-variance conditioned trees, general Lévy heights, noncompact local GHP and dynamic tree processes are not proved here.

The main text’s [vertex-mass comparison](../chapters/55-metric-measure-limits.md#geometry-vertex-mass) gives the mechanism. This page retains all clock and error steps rather than replacing them with “coding convergence obviously implies tree convergence.”
