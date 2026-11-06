# T-LEVY-HEIGHT: Consistent Genealogies, Compact Lévy Forests and the Height-Identification Boundary

Return to [Chapter 58](../chapters/58-multifurcation.md). We use the finite-mean critical/subcritical nonlinear mechanism and Grey condition of [T-CSBP-SEMIGROUPS](t-csbp-semigroups.md). We reconstruct reduced forests, compactness and mass from Sections 4–5 of Duquesne–Winkel’s [published 2007 paper](https://perso.lpsm.paris/~tduquesne/Documents/Duquesne_Winkel_PTRF_2007.pdf). A final section states the still incomplete classical Lévy-path height identification. The title is not evidence of full completion.

## 1. Colouring must include the genealogy

<a id="lh-colour"></a>

Fix b>0. Let \(\mathcal F_\lambda\) have Poisson\((b v_\lambda)\) independent ancestral trees, each with pgf \(g_\lambda\) and independent Exp\((c_\lambda)\) lifetime edges, joined at one root. Each is finite almost surely; with no ancestors the root alone remains. Give every terminal leaf an independent uniform mark in [0,λ]. Retain marks≤μ and their ancestral paths, suppressing vertices with one retained child by adding edge lengths. This gives an isometric subtree.

Let q be the probability that one ancestral tree has a retained leaf. If its leaf count is L, \(r=E(1-\mu/\lambda)^L\) satisfies \(r=g_\lambda(r)-p_0\mu/\lambda\). Derive this first for truncations by generation and then pass monotonically to the minimal nonnegative solution. Substitution gives \(\psi(v_\lambda(1-r))=\mu\), hence \(q=v_\mu/v_\lambda\).

## 2. Offspring and lifetime kernels of the retained tree

<a id="lh-thinning"></a>

Each original child survives independently with probability q. Before normalization, the probability of d≥2 retained children is \(q^d g_\lambda^{(d)}(1-q)/d!\); that of one is \(q g_\lambda'(1-q)\), and that of a retained terminal leaf is \(p_0\mu/\lambda\). Divide by q to condition on survival, then by \(1-g_\lambda'(1-q)\) to suppress unary chains. The resulting zero-offspring probability is

\[ \frac{p_0\mu/\lambda}{q(1-g_\lambda'(1-q))}
=\frac{\mu}{v_\mu c_\mu},\qquad
c_\lambda(1-g_\lambda'(1-q))=\psi'(v_\mu)=c_\mu. \]

For d≥2 the probabilities likewise become the coefficients of \(g_\mu\). Lifetimes and reproduction are independent. A retained path sums a geometric number of Exp\((c_\lambda)\) variables, stopping with probability \(1-g_\lambda'(1-q)\); its transform is \(c_\mu/(c_\mu+s)\), giving Exp\((c_\mu)\). Branching and independent lifetime marks give independence of the compressed edges and subtrees. Poisson thinning gives \(b v_\mu\) ancestors. Thus the retained forest has exactly the law of \(\mathcal F_\mu\).

For several levels, uniform thresholding composes exactly, so the reduction kernels compose. Finite plane trees, positive edge lengths and finite leaf marks form a countable disjoint union of Euclidean Borel spaces; reductions and isometric embeddings are measurable. Chapter 8 extends their consistent finite-dimensional laws at integer λ, retaining embeddings and marks, to nested forests \(\mathcal F_1\subset\mathcal F_2\subset\cdots\) on one space. Rational levels may also be included; integers suffice below.

## 3. Bounded height is not compactness: count long branches

<a id="lh-compact"></a>

Let \(Z_\lambda(h)\) count individuals alive at height h. The first-lifetime branching equation gives survival probability \(u_h(v_\lambda)/v_\lambda\) per ancestor, so the forest height \(H_\lambda\) has \(P(H_\lambda\le h)=\exp(-b u_h(v_\lambda))\). Heights increase under the coupling; their limit has distribution \(\exp(-b v(h))\). Since v(h)↓0, this height is finite almost surely.

Fix ε>0 and j≥0, and count points at height jε with a descendant path at least ε long. This count \(A_\lambda(j,\varepsilon)\) increases under inclusion. Vertices occur at deterministic heights with probability zero, uniformly over the countable levels used. Branching and \(E Z_\lambda(j\varepsilon)=b v_\lambda e^{-a j\varepsilon}\) give

\[ E A_\lambda(j,\varepsilon)
=b e^{-a j\varepsilon}u_\varepsilon(v_\lambda)
\le b e^{-a j\varepsilon}v(\varepsilon)<\infty. \]

Monotone convergence makes every limiting count finite almost surely. On H≤R, these points for j≤R/ε together with the root form a finite 2ε-net of the union: move a point above 2ε towards the root to the second preceding ε-grid level. The distance is below 2ε and the ancestor has a descendant at least ε away. Shallow points are covered by the root. Taking rational ε simultaneously shows total boundedness. The completion \(\mathcal F\) is compact.

Any two points of the union lie in a finite forest, with their unique arc and distance unchanged at later levels. Its completion remains a real tree: approximate endpoints, use compactness to obtain geodesics, and pass the four-point inequality to limits to exclude distinct arcs. This is Chapter 57’s completion lemma with its hypotheses now verified. Density of the nested compact subtrees implies \(d_H(\mathcal F_\lambda,\mathcal F)\to0\); otherwise a compact subsequence of points outside a fixed ε-neighbourhood contradicts density.

## 4. Mass cannot be guessed from lengths or means

<a id="lh-mass"></a>

Put one unit at each terminal leaf to obtain \(\xi_\lambda\), and write \(L_\lambda=\xi_\lambda(\mathcal F)\). The first-branch equation for a single tree gives \(\psi(v_\lambda(1-E s^L))=\lambda(1-s)\). Poisson superposition yields

\[ E e^{-qL_\lambda/\lambda}
=\exp\{-b\,\phi(\lambda(1-e^{-q/\lambda}))\}
\ \longrightarrow\ e^{-b\phi(q)}. \]

The limit is continuous at q=0, so the laws of \(L_\lambda/\lambda\) are tight. Their expectations may be infinite in the critical case; an L¹-bounded martingale is not available. Split leaf marks into unit-time bins, \(X_j=\xi_j-\xi_{j-1}\). Retained leaves remain leaves of all finer trees, so these are nonnegative finite point measures. Permuting finitely many bins preserves the joint laws of all finer forests, since fine-tree leaf marks are iid uniform. In particular bin counts are exchangeable. De Finetti and the truncated conditional strong law give \(L_N/N\to\Sigma\) almost surely. Infinite conditional mean would force the ratio to infinity, contradicting unconditional tightness. Thus Σ is finite almost surely, with transform \(e^{-b\phi(q)}\).

Positions also require control. Fix integer m and project onto the nearest ancestral point of the finite subtree \(\mathcal F_m\), using the 1-Lipschitz map \(\pi_m\). Conditional on all information in the first m bins, projected future-bin point measures remain exchangeable. Finite edge addresses and lengths give a standard Borel coding. Apply Chapter 43’s de Finetti theorem for random measures, then countably many continuous determining tests and truncated strong laws, to obtain \((\pi_m)_*\xi_N/N\Rightarrow\nu_m\) almost surely. This finite measure \(\nu_m\) has mass Σ. There are only countably many m, so one common event suffices.

For l≥m, composition of projections gives \((\pi_m)_*\nu_l=\nu_m\). Compactness gives \(\sup_{x\in\mathcal F}d(x,\pi_mx)\to0\). Uniform continuity makes \(\int f\,d\nu_m\) Cauchy for every continuous f on \(\mathcal F\). Riesz representation gives a unique finite measure m and \(\xi_N/N\Rightarrow m\): first fix m and take the projected weak limit, then let m increase; the error is bounded by Σ times the continuity modulus. The construction is measurable in finite-tree coordinates and countable tests. Chapter 55’s measurable rooted GHP structure therefore makes \((\mathcal F,m)\) a random compact measured tree.

Finite-mass measurability also reduces to Chapter 55’s probability-mass setting. The transform of Σ tends to zero as q→∞, so P(Σ=0)=0. Record \((\Sigma,\mathcal F,m/\Sigma)\) in the product of positive reals and rooted probability GHP space. Common-space Hausdorff convergence, total-mass convergence and normalized weak convergence make this a measurable limit.

## 5. Poisson sampling and support of mass

<a id="lh-poisson"></a>

To make tests compatible with a random space, retain plane order while forgetting unit-bin colours. The ε-tip-erased limit tree is finite: distinct terminal points have original descendants ε beyond them, yielding a 2ε-separated set, which compactness makes finite. Enumerate its vertices and rational edge points in plane depth-first order; the union over dyadic ε is a colour-independent countable dense set. Erasure changes Hausdorff distance by at most ε. Finite reduced-edge lengths are functions of distances and ancestral junctions; enumeration is measurable by limits of rational distance inequalities. Distance coordinates to this set give a measurable compact realization. Below f ranges over a countable bounded continuous determining class in these coordinates, measurable for every \(\Theta_N\); no early-bin leaf label is covertly retained in the conditioning field.

Fix integer t. Let \(\Theta_N\) contain the final uncoloured forest and all \(\mathcal F_j,\xi_j\), j≥N, without individual bin colours before N. These σ-fields decrease. Conditional on \(\Theta_N\), \(\xi_t\) is independent t/N-thinning of \(\xi_N\): prove this first from uniform marks at a finite finer level, then pass through increasing conditional σ-fields. For nonnegative continuous f,

\[ E(e^{-\xi_t f}\mid\Theta_N)
=\prod_{x\in\xi_N}\left[1-\frac tN(1-e^{-f(x)})\right]
\longrightarrow \exp\{-t\,m(1-e^{-f})\}. \]

The quadratic logarithmic error is bounded by \(C_t L_N/N^2\), which vanishes almost surely. Reverse martingale convergence identifies the conditional limit; m is determined by future empirical readings and is \(\Theta_\infty\)-measurable. Conditional on \(\Theta_\infty\), \(\xi_t\) is a Poisson random measure of intensity tm. A countable determining class gives a common kernel version. Each \(\xi_t\) is simple, hence m is diffuse: an atom would give positive conditional probability of repeated points. A marked terminal leaf stays terminal in every finer tree and its completion, for approximants to a descendant a positive distance beyond it would be Cauchy, so their pairwise ancestors would eventually lie strictly beyond that leaf, contradicting terminality at a finite level. Thus m is carried by leaves.

The support is full. Fix a nonempty rational subinterval J of a coarse edge and ε>0. Fine unary retained events along J form a Poisson process of rate \(c_\lambda-c_\mu\), by thinning exponential lifetime events. Each has at least one unretained child. Conditional on being unretained, that child is immediately terminal and uncoloured with probability \(p_0(1-\mu/\lambda)/(1-q)\). Also \(p_0\ge1/2\): termwise \(u\psi'(u)\le2\psi(u)\), with the integral inequality following from \(2(e^{-z}-1+z)-z(1-e^{-z})\ge0\) and its nonnegative derivative. Thus the probability is bounded below for large λ; the probability its exponential edge is shorter than ε tends to 1.

Grey’s condition implies \(c_\lambda\to\infty\). Independent branch marks bound the probability of no new leaf within ε of J by \(\exp[-C|J|(c_\lambda-c_\mu)]\to0\). Inclusion then gives a marked leaf in each such neighbourhood almost surely. There are countably many coarse edges, J and ε; density of the completion makes marked leaves dense in the whole tree. Conditional Poisson sampling and finite m imply that marks never lie outside its support. Thus m has full support. No skeleton-length measure was identified with leaf mass.

## 6. Stable branching does not stop at a fixed k

<a id="lh-degrees"></a>

For \(\psi(q)=q^\alpha,1<\alpha\le2\), the pgf is \(g_\lambda(s)=s+(1-s)^\alpha/\alpha\), independent of λ, and \(c_\lambda=\alpha\lambda^{(\alpha-1)/\alpha}\). At a branch point of coarse level μ with d≥2 retained children, the actual number D at fine level λ satisfies

\[ E[z^{D-d}\mid d]=\frac{g_\lambda^{(d)}((1-q)z)}{g_\lambda^{(d)}(1-q)}
=\left(\frac{q}{1-(1-q)z}\right)^{d-\alpha},\qquad q=(\mu/\lambda)^{1/\alpha},\quad1<\alpha<2. \]

The first expression follows by independent retention and d-th factorial tilting of offspring; its nonnegative coefficients sum to one. Differentiating \((1-s)^\alpha\) gives the second expression, a negative-binomial pgf. For fixed z<1 it tends to zero, so D tends to infinity in probability. D increases in the nested coupling, hence tends to infinity almost surely, simultaneously over all countably many coarse branch points.

Every nonroot branch point of the completion already branches at a finite level: choose points of the dense marked set in three open directions, using a finite-tree point towards the root when needed. Their junction appears in a common finite tree and is the same point. Thus for α<2 every nonroot branch point has countably infinite degree; separability bounds the number of disjoint open components by countability. At α=2 offspring are only 0 or 2, so finite-level branching stays binary, and the dense-point argument excludes new higher-degree branching. The artificial common root of the forest is excluded.

## 7. Scaling and normalization not silently assumed

<a id="lh-scaling"></a>

For the stable mechanism, multiplying lengths by r and masses by \(r^{\alpha/(\alpha-1)}\) gives the same forest law with initial parameter b'=\(b r^{1/(\alpha-1)}\). Verify the finite kernels at \(\lambda'=\lambda r^{-\alpha/(\alpha-1)}\): \(c_{\lambda'}=c_\lambda/r\) and \(b'v_{\lambda'}=b v_\lambda\). Colouring ratios agree as well. Consistent finite kernels, compact completion and the unique mass limit prove the assertion, rather than dimensional guessing.

The constructed object is a forest at fixed b with random total mass Σ and transform \(e^{-b q^{1/\alpha}}\). It is not automatically a single stable CRT of mass 1. Conditioning one excursion by duration requires a σ-finite excursion measure, disintegration by mass and a normalization check. Division by the probability-zero event \(\{\Sigma=1\}\) is invalid. That identification is not counted as completed here.

## 8. Lévy-path height: the precise unclosed proof obligation

<a id="lh-open"></a>

Published classical theory, under its spectrally positive, non-subordinator, infinite-variation critical/subcritical assumptions, constructs height using local time at the supremum of the reversed path. A usual normalization is, for each fixed t, convergence in probability:

\[ H_t=\lim_{\varepsilon\downarrow0}\frac1\varepsilon
\int_0^t\mathbf1_{\{X_s-\inf_{s\le r\le t}X_r<\varepsilon\}}\,ds. \]

[Duquesne–Le Gall, Astérisque281(2002)](https://arxiv.org/pdf/math/0509558), Sections 1.2–1.4, construct this process, its continuous version under Grey’s condition and the Ray–Knight connection. Their [published 2005 paper](https://www.imo.universite-paris-saclay.fr/~jean-francois.le-gall/Levy-final.pdf) studies the encoded trees. This formula is a sourced external result, not a definition already justified by the continuous-semimartingale Tanaka formula. Record-set local time of a spectrally positive pure-jump process needs new normalization and potential estimates.

Complete book proofs are still missing for reflected-process local time via potentials, the displayed occupation approximation, a common continuous version, identification with this reduced-forest construction, the full level-local-time CSBP/Ray–Knight theorem, and heavy-tailed conditioned GW height and contour limits. None is used by the preceding proofs of compact forests, mass, sampling or degrees. T-LEVY-HEIGHT must therefore record “reduced-forest version proved; canonical height and conditioned limits substantively unclosed,” not general Lévy height theory proved. In the Brownian convention \(\psi(q)=q^2/2\), classical height is twice the standard excursion; its metric must be halved to match the book’s \(e\).
