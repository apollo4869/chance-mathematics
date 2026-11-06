# T-MALLIAVIN: Closed Derivatives, Sobolev Domains, Divergence and Higher-Order Control

Companion to [Chapter 39](../chapters/39-malliavin.md#noise-closed). Fix real separable H and isonormal W, and use only σ(W)-measurable variables. S consists of f(W(h₁),…,W(hₙ)) with smooth f whose derivatives and value have polynomial growth. Hilbert- and tensor-valued cylinders are finite sums of deterministic vectors times S. None of these results presupposes chaos.

## 1. Intrinsic Directional Derivatives and Gaussian Integration by Parts

<a id="malliavin-proof-ibp"></a>

\[ DF=\sum_{i=1}^n\partial_if(W(h_1),\ldots,W(h_n))h_i,\qquad E\langle DF,h\rangle=E[F W(h)]. \]

For two cylinder representations, put every h into one finite-dimensional orthonormal span. Its Gaussian law has strictly positive density; smooth functions equal almost everywhere are equal everywhere, as are their derivatives. Thus DF and higher derivatives are representation independent. Coordinate integration against the Gaussian density, whose derivative is −xᵢ times itself, gives the first identity; polynomial growth removes boundary terms. Ordinary product differentiation then gives the central test identity.

\[ E[G\langle DF,h\rangle]=E\big[F(GW(h)-\langle DG,h\rangle)\big],\qquad F,G\in S. \]

S is dense in every Lᵖ, 1≤p<∞: countable orthonormal coordinates generate σ(W); finite-coordinate conditional means approximate bounded variables by Chapter 15. Tight regularity of finite Gaussian measures and smoothing give smooth cylinder approximation, and truncation handles general Lᵖ variables. For H-valued or separable Hilbert tensor-valued variables, truncate deterministic bases and apply scalar density.

## 2. Why the Cylinder Derivative Has a Closed Extension

<a id="malliavin-proof-closed"></a>

Let 1<p<∞, Fₙ→0 in Lᵖ and DFₙ→U in Lᵖ(H). Test against G∈S and h∈H. The right side of the preceding identity tends to zero because its test factor has every Gaussian moment. Hence E[G〈U,h〉]=0. Lᑫ density and Hölder extend to bounded tests; a countable orthonormal basis gives U=0. Thus D is closable, without assuming samplewise directional derivatives of arbitrary representatives. The tensor-valued proof is componentwise identical.

\[ \|F\|_{k,p}^p=E|F|^p+\sum_{j=1}^k E\|D^jF\|_{H^{\otimes j}}^p,\qquad \mathbb D^{k,p}=\overline S^{\,\|\cdot\|_{k,p}},\qquad \mathbb D^\infty=\bigcap_{k\ge1,\,p>1}\mathbb D^{k,p}. \]

Iterated closability embeds this completion in Lᵖ with unique derivatives. Bochner Lᵖ completeness follows by a summable subsequence: summable norm differences give almost-everywhere absolute convergence in the complete Hilbert target, and Minkowski controls tails. No Banach compactness theorem is needed. For C¹ φ with bounded derivative, apply the cylinder chain rule; bounded φ′ and Lᵖ control of DF pass to the closure, giving Dφ(F)=φ′(F)DF. Iterate for bounded higher derivatives and vectors.

Products need moment conditions: for example F,G∈\(\mathbb D^{1,4}\) ensure FG∈\(\mathbb D^{1,2}\) and D(FG)=F DG+G DF by Hölder and closure; merely \(\mathbb D^{1,2}\) is insufficient. Finite products, contractions and smooth polynomial-growth compositions in D∞ are handled by cutoffs, Hölder and iterated chain rules, choosing a larger p before returning to the desired one. A smooth function of one Gaussian coordinate with all derivative moments is also in D∞: cut it off by χ(x/n), dominate product derivatives by sums of its original derivatives, and use DCT and closure. Thus e^Z need not be incorrectly placed in the polynomial-growth core.

## 3. Divergence Is an Adjoint, Not an Integral of Every L² Process

<a id="malliavin-proof-divergence"></a>

For U∈L²(H), require |E〈DG,U〉|≤C‖G‖₂ for every G∈S. Hilbert Riesz gives unique δU∈L² satisfying E[GδU]=E〈DG,U〉. This defines Domδ; density gives uniqueness. If Uₙ→U and δUₙ→Y in L², testing the limit proves U∈Domδ and δU=Y, so δ is closed.

\[ \delta(Gh)=G W(h)-\langle DG,h\rangle,\qquad E\delta U=0. \]

For smooth finite-rank U,V in a common finite Gaussian basis, δU=Σᵢ(ξᵢUᵢ−∂ᵢUᵢ). Two integrations by parts give the identity below. The transposed term may be negative, but Hilbert–Schmidt Cauchy–Schwarz gives the bound. Density of finite-rank cylinders in \(\mathbb D^{1,2}\)(H) and closedness extend δ to that space.

\[ E(\delta U)(\delta V)=E\langle U,V\rangle+E\sum_{i,j}(D_iU_j)(D_jV_i),\qquad \|\delta U\|_2^2\le\|U\|_{L^2(H)}^2+\|DU\|_{L^2(H^{\otimes2})}^2. \]

This is not a general isometry. For H=L²[0,T] and U=\(B_T\mathbf1_{[0,T]}\), δU=B_T²−T has variance 2T² while E‖U‖²=T². Treating the random coefficient as an already known deterministic value loses the adjoint correction. For K-valued fields, take divergence componentwise and sum with the K-inner product to obtain the same L² bound.

## 4. Commuting Derivative and Divergence

<a id="malliavin-proof-commutation"></a>

\[ D_h\delta U=\langle U,h\rangle+\delta(D_hU). \]

Differentiate the finite-coordinate formula: differentiating ξᵢ gives Uⱼ, while the other terms are δ(∂ⱼU). For tensor-valued output retain the H-divergence index and regard other indices as parameters. Thus DᵏδU is δ(DᵏU) plus k index permutations of \(D^{k-1}U\), each an isometry. This starts on smooth cylinders; extension requires derivative and divergence integrability, supplied by the sufficient, nonoptimal bound next.

## 5. Higher Moments Do Not Follow from an L² Bound Alone

<a id="malliavin-proof-moments"></a>

\[ E\|\delta U\|_K^{2r}\le C_r\sum_{j=0}^{2r}E\|D^jU\|_{H^{\otimes(j+1)}\otimes K}^{2r},\quad r\in\mathbb N. \]

First let U depend on finitely many Gaussian coordinates with finite-dimensional H,K. Expand ‖δU‖^{2r} as a full contraction of 2r divergence factors, pairing K-indices. Apply adjointness to one remaining δ, differentiating the other factors. Hitting an ordinary coefficient removes one divergence. Hitting another δ uses the commutation formula, yielding either an ordinary term or that same δ with an extra derivative. Either way the number of remaining divergences decreases by at least one. After at most 2r repetitions neither divergences nor Gaussian multipliers remain. Each original U still occurs once and is differentiated at most 2r times; the number of terms depends only on r.

All final indices are paired between two distinct factors, without a free trace within one factor: adjoint differentiation never hits the field being removed. Hence contraction bounds have no dimension constant. Regard factors as vertices and paired indices as edges. Apply Cauchy–Schwarz over every incident index of one vertex. Neighboring factors separate into groups; square-integrating along the removed edges creates new factors with the same full Hilbert norms as before. Remove the vertex and induct: every complete contraction is bounded by the product of Hilbert–Schmidt norms. Multiple edges cause no change. Self-loops would invalidate this bound, explaining the preceding check.

Apply Hölder to the 2r factors in each term and sum finitely many terms. The constant is dimension independent. For smooth approximants in \(\mathbb D^{2r,2r}\)(H⊗K), the difference satisfies the same bound, so δUₙ are Cauchy in L^{2r}(K); closedness identifies the L² limit. Combine with commutation: derivatives of U through k+2r control DᵏδU. Thus δ:D∞(H⊗K)→D∞(K). This is the sufficient result actually needed, not a claim of the optimal Meyer inequality.

## 6. The Closed Derivative Still Responds to Actual Noise Shifts

<a id="malliavin-proof-shift"></a>

Realize the noise by countable Gaussian coordinates; τ_{sh} shifts ξⱼ to ξⱼ+s〈h,eⱼ〉. Chapter 33 gives the strictly positive density exp(sW(h)−s²‖h‖²/2). Hölder then bounds ‖G∘τ_{sh}‖_q≤C‖G‖_p for 1<q<p, uniformly on bounded s-intervals. Prove translation continuity first on cylinders and then by this bound on Lᵖ→Lᑫ. Translation is not asserted to be a bounded Lᵖ operator on arbitrary Lᵖ variables.

\[ F\in\mathbb D^{1,p},\ h\in H,\ 1<q<p\quad\Longrightarrow\quad \frac{F\circ\tau_{\varepsilon h}-F}{\varepsilon}\longrightarrow\langle DF,h\rangle_H\quad\hbox{in }L^q. \]

For cylinders, ordinary calculus writes the quotient as ∫₀¹〈DF,h〉∘τ_{θεh}dθ. Graph-norm approximation and the uniform Hölder bound extend this identity to D^{1,p}; measurability of the Bochner integral is immediate in coordinate realization. Strong continuity gives the limit. This is a Cameron–Martin energy direction, not a Brownian time difference quotient, and does not assert pathwise Fréchet differentiability of every representative. [Return to the chapter](../chapters/39-malliavin.md#noise-directions).
