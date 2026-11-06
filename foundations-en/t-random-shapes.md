# T-RANDOM-SHAPES: Closed Sets from Measures, Paths, and Random Coverage

Return to [Chapter 51](../chapters/51-random-closed-sets.md#sets-examples). Use E from T-FELL and Euclidean space for coverage examples. We use Chapters 48–49 measure and marked-Poisson constructions and this chapter’s hyperspace results, not Chapter 52 trees.

## 1. Support Is Measurable but Need Not Be Continuous

<a id="shapes-support"></a>

The support of Radon μ consists of points all of whose open neighborhoods have positive mass. Its complement is the union of countably many zero-mass base opens, hence has μ-mass zero. For open U, \(\operatorname{supp}\mu\cap U\ne\varnothing\Longleftrightarrow\mu(U)>0\): use the definition in one direction and the countable zero-open cover in the other. Thus support is measurable from Chapter 49 evaluation Borel to Effros; zero mass has empty support.

Even preservation of probability mass does not give general continuity: \(\mu_n=(1-1/n)\delta_0+(1/n)\delta_1\Rightarrow\delta_0\) for n≥2, while all supports equal {0,1} and do not tend to {0}. The mass at one vanishes, but its existence does not. In contrast support on locally finite integer point measures is continuous from vague to Fell. If Nₙ tends vaguely to N, a support point x and its neighborhood admit nonnegative compactly supported f with Nf>0, so Nₙ eventually hits that neighborhood. If compact K avoids supp N, choose a cutoff χ≥1 on K supported in a relatively compact neighborhood disjoint from supp N. Then Nₙχ→0, and integer counts force eventual Nₙ(K)=0. Both Fell subbasic conditions hold. Integer counts and arbitrarily small masses behave differently.

## 2. Finite- and Infinite-Time Ranges

<a id="shapes-ranges"></a>

A continuous path γ:[0,t]→E has compact image. For uniform convergence in the proper metric, \(d_H^\rho(\gamma_n[0,t],\gamma[0,t])\le\sup_{s\le t}\rho(\gamma_n(s),\gamma(s))\). Images eventually lie in one compact neighborhood of γ’s image, where the proper and compactification metrics are uniformly compatible. Thus the finite-time range map is Fell-continuous. Random continuous paths have measurable random compact ranges, and Chapter 24 transfers path weak convergence to finite-time range convergence.

Infinite time first requires closure: γ(s)=1/(1+s) has nonclosed image (0,1]. Its closed range hits open U exactly when the path hits U, and continuity makes this equivalent to visiting U at some nonnegative rational time. The closed-range map is therefore measurable. It is not continuous for local uniform convergence: let γₙ be zero until n, rise linearly to one on [n,n+1], then stay one. These converge locally uniformly to the zero path, but all closed ranges equal [0,1], not {0}. Infinite and finite observation horizons are different limit operations.

## 3. Poisson and Cox Closed Point Sets

<a id="shapes-poisson"></a>

The support of a locally finite point measure is closed and hits compact K exactly when N(K)>0. Chapter 48 PRM gives \(T(K)=1-e^{-\mu(K)}\), including atomic intensity and multiplicities. Cox gives \(T(K)=1-Ee^{-\Lambda(K)}\), not \(1-e^{-E\Lambda(K)}\); mean intensity does not identify shape. The measures \(\delta_U\) and 2\(\delta_U\) have identical supports and capacities but different point-measure laws. Closed-set records are legitimate while intentionally forgetting multiplicities.

## 4. A Random Cover Must First Be Closed

<a id="shapes-boolean"></a>

On \(\mathbb R^d\), let the marked parent PRM with nonempty compact grain G have intensity a(dx)Q(dG), with σ-finite a. Compact grains form a Borel subset of Fell space: compact sets are precisely those contained in some exhaustion compact Kₘ, and containment is avoidance of its open complement; then remove ∅. Chapter 48 standard Borel marking therefore applies. Translations are jointly continuous: if xₙ→x and Gₙ→G, subtracting xₙ from lower approximating and upper-limit points reduces both sequence criteria of T-FELL to those for Gₙ; adding x gives the assertion. Thus hitting K by x+G is jointly Borel. Assume for every compact K that

\[ I_K:=\int a(dx)\int\mathbf1_{\{(x+G)\cap K\ne\varnothing\}}Q(dG)<\infty. \]

The number of grains hitting K has finite expectation \(I_K\) and is finite almost surely. A common null set over an exhaustion makes the family locally finite. Thus \(F=\bigcup_i(x_i+G_i)\) is closed: each position has a compact neighborhood meeting finitely many closed grains, and finite-union closedness applies inside that neighborhood. Open hits are positive PRM counts of measurable marked sets, so F is random closed. The Poisson probability that no grain hits K gives

\[ T(K)=1-e^{-I_K}. \]

For homogeneous rate κ on the line and fixed grain [−r,r], r≥0, one has I=κ(b−a+2r) on [a,b], an explicit coverage law rather than a scatter illustration. Local hit-integrability is sufficient here, not asserted necessary: infinitely overlapping grains may still have a closed union. Without control a union can fail to be closed. Put one unit of parent intensity at each position 1/n and use the fixed grain {0}; each position therefore has an independent Poisson(1) number of singleton grains. Independent Poisson counts give infinitely many occurring labels almost surely by Chapter 7 Borel–Cantelli. Their union omits zero but accumulates there. Closure adds a position absent from the original record; an infinite union is not automatically closed.
