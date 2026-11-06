# T-CRT-SAMPLING: The Density of Finite Reduced Brownian CRT Subtrees

This companion proves the [finite sampling theorem in Chapter 54](../chapters/54-brownian-crt.md#crt-sampling-law). Fix the duration-one standard excursion e of Chapters 37 and 53, using Tₑ rather than T₂ₑ. Inputs are the killed Brownian kernel and first-passage density from Chapter 26, the excursion density rechecked in Chapter 53, and [T-REAL-TREE-CODE](t-real-tree-code.md). No Aldous edge-length theorem, CRT spatial limit or future line-breaking construction is assumed.

## 1. Fixing the excursion scale first

<a id="crt-sample-kernels"></a>

\[ g_t(z)=\frac{e^{-z^2/(2t)}}{\sqrt{2\pi t}},\quad
q_t(x,z)=g_t(z-x)-g_t(z+x),\quad
h_t(a)=\frac{a}{\sqrt{2\pi}t^{3/2}}e^{-a^2/(2t)},\quad c_1=(2\pi)^{-1/2}. \]

Here x,z,a are positive. The function hₜ(a) is the time density for standard Brownian motion started at a to hit 0, not a coding function; the code is always e in this companion. For 0<t₁<⋯<tₖ<1 the joint density at x₁,…,xₖ is below. Chapter 53 derives it by spherical Gaussian integration for the norm of three standard bridges. Its entrance factor is 2h and exit factor h, so the coefficient here is 2, not 4.

\[ \frac{2}{c_1}h_{t_1}(x_1)
\prod_{i=1}^{k-1}q_{t_{i+1}-t_i}(x_i,x_{i+1})
h_{1-t_k}(x_k). \]

Given these endpoints, the intervening segments have independent killed positive-half-line Brownian bridge laws. To see this, insert finitely many additional times and divide their joint density by the endpoint density. It factors across the segments into q-kernel bridges. Rational evaluations generate the continuous-path Borel field, so π–λ extends the factorization to conditional segment-path kernels. This is an identity for regular conditional laws at fixed positive times, not a definition by division on a zero-probability endpoint event.

## 2. Moving a barrier gives the minimum density

<a id="crt-sample-minima"></a>

Restrict a segment between x,z to remain above y, where 0≤y<min(x,z). Reflection from Chapter 26 gives the transition kernel killed at y. There is no additional atom hidden by the strict barrier convention: reflection gives a continuous minimum distribution, and the endpoint limits below verify the entire mass.

\[ q_t^{(y)}(x,z)=g_t(z-x)-g_t(x+z-2y),\qquad
-\partial_yq_t^{(y)}(x,z)=2h_t(x+z-2y). \]

The conditional bridge minimum exceeds y with probability q⁽ʸ⁾/q⁽⁰⁾. One may first impose the barrier on increasingly dense grids, then pass to paths by continuity and the atom-free minimum law from reflection; this also verifies measurability. The ratio tends to 1 as y decreases to 0 and to 0 as y increases to min(x,z). Thus the derivative accounts for the whole minimum law, with no endpoint mass.

Let yᵢ be the minimum between consecutive sample times, and put Δt₀=t₁, Δtᵢ=tᵢ₊₁−tᵢ, Δtₖ=1−tₖ. Conditional segment factorization allows differentiation of each barrier separately. This gives the following joint density. All factors are nonnegative, so subsequent integration exchanges are justified by Tonelli.

\[ \frac{2^k}{c_1}\prod_{i=0}^{k}h_{\Delta t_i}(r_i),\qquad
r_0=x_1,\quad r_i=x_i+x_{i+1}-2y_i\ (1\le i<k),\quad r_k=x_k,
\quad 0<y_i<\min(x_i,x_{i+1}). \]

## 3. Integrating out the sampling times

<a id="crt-sample-time"></a>

First-passage densities satisfy h(a)∗h(b)=h(a+b), with convolution in time. The special strong Markov theorem of Chapter 26 proves this: first hit b from a+b, then 0 from b. The two times are independent with densities h(a),h(b); almost-sure finiteness follows because the reflection tail tends to zero. The displayed density, extended by zero to negative times, is bounded and uniformly continuous and integrates to one. Bounded convergence, dominated by one probability density, makes the convolution continuous. The almost-everywhere identity therefore holds at every positive time. Iteration gives the k+1-factor identity, without a Laplace inversion black box.

\[ \int_{\substack{\Delta t_i>0\\\sum_{i=0}^{k}\Delta t_i=1}}
\prod_{i=0}^{k}h_{\Delta t_i}(r_i)\,d\Delta t_0\cdots d\Delta t_{k-1}
=h_1\!\left(\sum_{i=0}^{k}r_i\right),\qquad
\sum_{i=0}^{k}r_i=2L,\quad L=\sum_{i=1}^{k}x_i-\sum_{i=1}^{k-1}y_i. \]

The order statistics of k independent uniform times have density k!. The preceding identity therefore turns the joint density of ordered heights and minima into 2ᵏ⁺¹k! L exp(−2L²). This explains the appearance of total span length: a traversal starting at the root, visiting every sample and returning to the root crosses each reduced edge twice.

## 4. From height coordinates to edge lengths

<a id="crt-sample-jacobian"></a>

The joint law has a density with respect to (2k−1)-dimensional Lebesgue measure. Ties between distinct y-values, or between x and an adjacent y, therefore have probability zero. Recursive splitting at the smallest y gives a binary plane tree with k leaves and an initial root edge. Root and leaves have degree one, internal vertices degree three, and there are 2k−1 edges; for k=1 the convention is a single edge.

For a fixed plane shape, each x is a leaf’s absolute height and each y a branching vertex’s absolute height. Edge length is child height minus parent height, with root height 0. Ordering vertices after their parents makes this linear transformation triangular with diagonal 1, hence absolute Jacobian 1. Positive edge lengths are precisely the open coordinate region for that shape; no ordering of heights on unrelated branches needs to be imposed.

Restore the original sample labels 1,…,k. Conditional on the ordered times, their label permutation is independent uniform, dividing the density for each labeled plane shape by k!. Then forget the plane order. Each nonplane binary rooted shape with fixed leaf labels has 2ᵏ⁻¹ left–right orientations; fixed distinct labels prevent duplicated labeled orientations. This yields the sampling theorem:

\[ \boxed{\quad
P\{\operatorname{shape}(R_k)=\tau,\ (\ell_a)_{a\in E(\tau)}\in d\ell\}
=4^kL e^{-2L^2}\prod_{a\in E(\tau)}d\ell_a,\qquad
L=\sum_{a\in E(\tau)}\ell_a,\quad\ell_a>0.\quad} \]

## 5. Normalization, shape and total length

<a id="crt-sample-normalization"></a>

There are Nₖ=(2k−3)!! such nonplane labeled rooted shapes, with N₁=1. Indeed, add label k+1 by choosing one of the existing 2k−1 edges, subdividing it and attaching a new leaf. Deleting that leaf and suppressing the resulting degree-two vertex is the unique inverse. Thus Nₖ₊₁=(2k−1)Nₖ. Plane Catalan counts do not count these shapes.

For m=2k−1 positive edge lengths, integrating functions of their sum contributes Lᵐ⁻¹/(m−1)!. This follows by repeated integration, or by setting the last coordinate to L minus the others. The probability of one shape is therefore the following, exactly 1/Nₖ.

\[ \frac{4^k}{(2k-2)!}\int_0^\infty L^{2k-1}e^{-2L^2}\,dL
=\frac{2^{k-1}(k-1)!}{(2k-2)!}=\frac1{(2k-3)!!},\qquad 2L_k^2\sim\operatorname{Gamma}(k,1). \]

Thus shape is uniform and independent of total length. Conditional on both, edge proportions are uniform on the simplex, that is Dirichlet(1,…,1), independently of them. Coding by 2e instead multiplies every edge by 2. Its Jacobian is 2⁻⁽²ᵏ⁻¹⁾, turning the per-shape density into L exp(−L²/2). In particular a uniform mass point has root-height density 4r exp(−2r²) in Tₑ, and r exp(−r²/2) only in T₂ₑ.

## 6. Deletion consistency and adding one sample

<a id="crt-sample-consistency"></a>

Using one sequence of independent uniform times, deleting the last label plainly recovers Rₖ. The densities provide a further direct check. Given an old tree of length s, attach a branch of length b>0 at interior position a of an old edge. The transformation from the split edge and new edge to a,b has Jacobian 1. The ratio of new and old densities is

\[ \frac{4(s+b)}s\,e^{-2((s+b)^2-s^2)}\,da\,db,\qquad
\int_{T_{\rm old}}da=s,\qquad
2L_{k+1}^2-2L_k^2\mid R_k\sim\operatorname{Exp}(1). \]

Integrating a leaves density 4(s+b)exp{−2((s+b)²−s²)} for b, integrating to 1. The attachment is uniform in old edge length and conditionally independent of b. This is the conditional finite-sample growth law inside the CRT already constructed, not an assertion that a separate infinite growth space follows without proof. That construction remains for Chapter 57.

## 7. Scope of the proof

<a id="crt-sample-scope"></a>

Every density here was calculated from excursion kernels; convolution, coordinate changes, shape multiplicities and normalization were checked separately. The Brownian structure is used further in the [mass and randomness companion](t-crt-randomness.md#crt-random-leaves). This proof does not use the height-tightness argument of Chapter 53 to establish itself. Its input is the explicit excursion kernel of §53.11, whose radial Gaussian derivation agrees with the entrance constant here.

Le Gall’s [2005 author survey, §§2.5–2.6](https://arxiv.org/pdf/math/0511515) and Aldous’s [1993 paper](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf) provide historical and normalization checks. This proof is reconstructed through moving barriers and first-passage convolution for a fixed-duration excursion; it is not presented as a joint historical discovery. [Return to the sampling theorem in Chapter 54](../chapters/54-brownian-crt.md#crt-sampling-law).
