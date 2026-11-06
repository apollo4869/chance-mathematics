# T-KARY-UNIVERSALITY: Offspring Counts, Continuum Degrees and Sampled Mass

This companion returns to [Chapter 58](../chapters/58-multifurcation.md). It uses published Brownian CRT and conditioned GW theory, and contains no unpublished research.

## 1. The precise fixed-k probability model

<a id="ku-model"></a>

Fix an integer \(k\ge2\), with \(p_0=(k-1)/k,p_k=1/k\) and all other probabilities zero. Then \(E\xi=1\) and \(\operatorname{Var}\xi=k-1>0\). A full plane k-ary tree with \(I\) internal vertices has \(kI\) edges, \(n=kI+1\) vertices and \((k-1)I+1\) leaves. Its unconditioned probability is \(p_k^I p_0^{(k-1)I+1}\), depending only on I. Conditional on n, these rooted plane trees are therefore uniform.

The feasible sizes are exactly \(n=1+kI\). Necessity follows from counting; sufficiency follows by repeatedly replacing one leaf by k leaves. Each resulting finite tree has positive probability. The support of \(\xi-1\) is \(\{-1,k-1\}\), with maximal lattice span k. This periodicity matters when conditioning on total size.

## 2. The spatial limit and its actual input

<a id="ku-limit"></a>

\[ \left(T_n,\frac{\sqrt{k-1}}{2\sqrt n}d,\rho,\frac1n\sum_{v\in T_n}\delta_v\right)\ \Rightarrow\ (\mathcal T_e,d_e,\rho_e,\mu_e),\qquad n\in1+k\mathbb N,\quad n\to\infty. \]

Proof: Chapter 55 requires a fixed critical, nondegenerate offspring law with finite positive variance, and convergence along feasible sizes. The preceding section verifies each hypothesis; substitution gives the formula. Here e is the standard duration-one Brownian excursion of Chapter 54, not 2e. This application retains Chapter 53’s conditioned bridge and height estimates as explicit inputs; ordinary Donsker cannot replace them. A primary classical source is Aldous, The Continuum Random Tree III (1993), [public text](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf).

## 3. Why finite samples exclude four directions

<a id="ku-degrees"></a>

Chapter 54 gives binary reduced trees spanned by the root and finitely many independent \(\mu_e\)-samples; the mass \(\mu_e\) is diffuse, fully supported and carried by leaves. A countable iid sample is dense, by a countable base and full support. All its finite reduced trees are binary on one common event of probability one. If removal of a point b left at least four components, those nonempty open components would each contain a sample. Their spanning tree would have at least four directions at b, contradicting a finite binary reduced tree. Thus every branch point has unrooted degree 3.

The root is not a branch point. At another branch point the direction towards the root must be subtracted from the unrooted degree. “Binary” means two descendant directions, not unrooted degree 2. The limit of the discrete k-ary model has this property for every fixed k. GHP convergence does not preserve individual vertex degrees: chains of vanishing length may be identified, and a direction without persistent positive length need not survive.

## 4. A three-way mass law under a specified sampling rule

<a id="ku-mass"></a>

Take root 0 and two independent mass samples 1 and 2, and let b be their common junction. Write \(M_0,M_1,M_2\) for the masses of the three components after deleting b, oriented by these labels. Then

\[ (M_0,M_1,M_2)\sim\operatorname{Dirichlet}(1/2,1/2,1/2). \]

Proof starts from reduced shapes. The unrooted binary shape with label 0 and n sampled leaves is uniform, because Chapter 54 assigns the same density to every labeled shape. Its extension chooses one of the \(2n-1\) edges uniformly, inserts a junction and adds the new leaf. Deleting that leaf and suppressing the degree-two vertex uniquely reverses the operation. Initially each of the three directions contains one edge. A direction containing a labeled leaves has \(2a-1\) edges, and gains two edges upon an insertion. The three edge counts thus form a Pólya urn with initial counts \((1,1,1)\) and reinforcement 2.

After division by 2, Chapter 44’s Pólya representation has Dirichlet parameters \(1/2\). Its conditional strong law gives a Dirichlet limit for the three proportions. In the actual CRT, conditional on the tree and the first two samples, subsequent samples remain iid with law \(\mu_e\). The components are open and b has zero mass, so their empirical proportions converge to \(M_i\). Uniqueness of the limit proves the claim. This specifies a junction chosen by the root and two typical leaves. It assumes no uniform distribution on all branch points, and makes no assertion that other sampling rules give the same Dirichlet law.
