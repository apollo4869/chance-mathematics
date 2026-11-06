# T-PALM-APPROXIMATION: Local Conditioning, Error, and Topology

Return to [Chapter 50](../chapters/50-palm-gibbs.md#palm-local). We distinguish exact window-weighted Palm identities, approximation by conditioning on nonemptiness, and almost-everywhere versions of nonstationary Palm kernels. No almost-everywhere version becomes a uniquely defined conditional probability at every location.

## 1. Choosing a Configuration or Choosing an Occurrence

<a id="palm-local-bound"></a>

Let Ξ be stationary and locally finite with 0<λ<∞. Take a bounded Borel window B with 0<|B|<∞, and put N=Ξ(B), m=EN=λ|B|, p=P(N>0)>0. Let \(Q_B\) be the law obtained by conditioning on N>0, selecting X uniformly among the N occurrences in B, and observing θXΞ. Let \(R_B\) first weight configurations by N/m and then use the same selection. Measurable enumeration supplies the sampling kernel, and stationary Campbell gives exactly \(R_B=P^0\), for every B.

\[ P^0=\frac pm Q_B+\frac{m-p}{m}D_B,\qquad d_{\rm TV}(Q_B,P^0)\le\delta_B:=\frac{m-p}{m}=\frac{\mathbb E(N-1)^+}{m}. \]

If m=p the second term vanishes; otherwise \(D_B\) weights configurations by (N−1)⁺/(m−p) and uses the same selection kernel. The identity is the pointwise decomposition N=1{N>0}+(N−1)⁺. Total variation is the supremum of event differences, so no factor of two is missing. Bounded F gives an expectation error at most 2‖F‖δB. The inequality (N−1)⁺≤N(N−1)/2 gives a second-moment sufficient bound, but the general theorem needs no second moment.

## 2. Simplicity Gives a Local Limit Without Second Moments

<a id="palm-local-simple"></a>

Assume Ξ is simple and B lies in the radius-r ball about zero. Since \(m-p\le\mathbb E[N\mathbf1_{\{N\ge2\}}]\), centered Campbell gives

\[ \delta_B\le\frac1{|B|}\int_B P^0\{\eta(B-x)\ge2\}\,dx\le P^0\{\eta(B(0,2r))\ge2\}\longrightarrow0. \]

Under P⁰ the root has exactly one occurrence, and local finiteness gives every realization a positive distance from zero to the other points. The final probability vanishes. Thus \(Q_B\) converges to P⁰ in total variation without any N² assumption. For homogeneous Poisson, p=1−exp(−m), so δB≤m/2 gives an explicit small-window error.

Without recentering, consider \(\mathcal L(\Xi\mid N>0)\). For bounded continuous F on the vague configuration space,

\[ \left|\mathbb E[F(\Xi)\mid N>0]-\mathbb E^0F(\eta)\right|\le2\|F\|_\infty\delta_B+\mathbb E^0\sup_{|x|\le r}|F(\theta_{-x}\eta)-F(\eta)|\longrightarrow0. \]

The first term uses the same mixture decomposition at configuration level. The weighted uncentered law is |B|⁻¹∫B Law(θ₋ₓη)dx. Joint continuity from T-PALM makes the second term vanish realization by realization, and the bound 2‖F‖ permits dominated convergence. The supremum can be taken over countably many dense x and is measurable. This gives weak convergence, not general TV convergence: a diffuse Poisson law conditioned on nonemptiness still has no point at the exact origin almost surely, whereas Palm law has one. Their TV distance remains one.

Simplicity cannot be omitted for multiplicities. Take Poisson parent locations as in Chapter 49, with shapes δ₀ or 2δ₀, each of probability one-half. Palm root multiplicity two has probability two-thirds. Conditional on a small window being nonempty, two or more parents have vanishing conditional probability, so the selected cluster’s multiplicity-two probability tends to one-half. The background has no point at the selected parent position almost surely. Even after recentering, the limiting event difference from P⁰ is at least one-sixth. Naive conditioning really gives the wrong weight here.

## 3. Local Averages of Nonstationary Kernels

<a id="palm-kernel-averages"></a>

Let \(C(dx,dz)=\nu(dx)Q_x(dz)\), with σ-finite ν and a Polish environment space S. Partition E into finite-ν pieces Dⱼ and refine each by the first n sets of a countable Borel base, obtaining increasing countable partitions \(\mathcal A_n\) generating the Borel σ-algebra. For cells of positive ν-mass define \(Q_A=C(A\times\cdot)/\nu(A)\), using a fixed probability on null cells. On each finite-ν piece, for every finite union G of base opens in S, \(Q_{A_n(x)}(G)\) is the conditional expectation of Qₓ(G) on the increasing partitions. Closed-martingale convergence in Chapter 15 gives Qₓ(G) for ν-almost every x. Combine the null sets for countably many G.

Every open U is exhausted from below by such finite unions, giving liminf \(Q_{A_n(x)}\)(U)≥Qₓ(U). Portmanteau from Chapter 24 yields \(Q_{A_n(x)}\)⇒Qₓ for ν-almost every x. This concerns specified refining partitions, not every shrinking set or every prescribed null location. For locally finite ν on its support one may add fine meshes so cell diameters vanish; otherwise the countable generating version suffices.

If additionally a fixed probability R dominates the kernels, with \(Q_x(dz)=k(x,z)R(dz)\), jointly measurable k, and ∫k(x,z)R(dz)=1 for ν-almost every x, convergence upgrades to TV. On each finite-ν piece, the averaged density kₙ is the conditional expectation of k on the increasing σ-algebras retaining partitioned x and full z. The density is L¹ on that piece×S, so closed-martingale convergence gives kₙ→k almost everywhere in the product. Fubini gives R-almost-everywhere convergence for ν-almost every x. Both densities integrate to one, and the Scheffé calculation \(\int|k_n-k|dR=2-2\int\min(k_n,k)dR\to0\) gives TV convergence.

Without domination the TV conclusion fails. Let Ξ=\(\delta_U\) for U uniform on [0,1], with environment Ξ. Then Qₓ=\(\delta_{\delta_x}\), while \(Q_A\) is the configuration law of a uniform point in a positive-length cell A. At fixed x, this average gives the singleton configuration {δₓ} probability zero and Qₓ gives it one, so TV=1. Refining cells still gives weak convergence to Qₓ. The marginal is finite and the versions legitimate; only the unjustified topology upgrade fails.
