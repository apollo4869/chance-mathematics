# T-GH: Common Spaces, Correspondences and Completeness of Compact Geometry

This page proves the deterministic geometry used in [Chapter 55](../chapters/55-metric-measure-limits.md#geometry-common). Spaces are nonempty and compact; rooted isometries preserve the root. No later metric-space limit theorem is used.

## 1. Putting different spaces together

<a id="gh-gluing"></a>

Suppose X and Y are embedded isometrically in Z₁ and Z₂, with the two copies of Y identified. Define a cross-distance as the infimum of lengths of routes through Y. Original distances are preserved: an excursion out of an original space and back has length at least the original distance between its two Y endpoints, so it can be replaced inside that space. Concatenation proves the triangle inequality. If Y is closed and a cross-distance vanishes, both points have distance zero from Y and are the same point of Y. Thus the quotient is a metric space. Finite or countable chain gluings of separable spaces remain separable; take the completion afterwards. A finite gluing of compact spaces is compact.

\[ \rho(x,z)=\inf_{y\in Y}\{d_{Z_1}(x,y)+d_{Z_2}(y,z)\}. \]

For a comparison of two compact objects we may restrict any witnessing ambient space to their union, which is compact. No nonseparable background is needed. All triangle inequalities below use this gluing, rather than assuming universal original coordinates.

## 2. Correspondences and a bridge metric

<a id="gh-bridge"></a>

A correspondence R is a relation in X×Y projecting onto both factors. Its distortion is the supremum of the discrepancy between paired distances. A rooted correspondence contains the root pair. Taking its closure preserves surjectivity and distortion by compactness and continuity. Write D for its distortion, choose c>D/2, retain internal distances and define the following cross-distance on the disjoint union.

\[ \begin{aligned}\operatorname{dis}R&=\sup_{(x,y),(x',y')\in R}|d_X(x,x')-d_Y(y,y')|,\\
\rho_c(x,y)&=\inf_{(a,b)\in R}\{d_X(x,a)+c+d_Y(b,y)\}.\end{aligned} \]

Only triangle inequalities crossing two bridges need attention. For a route from x through y in Y to x′, using bridges (a,b) and (a′,b′), its length is at least dX(x,a)+2c+dY(b,b′)+dX(a′,x′), and hence at least dX(x,a)+dX(a,a′)+dX(a′,x′), since 2c≥D. This is at least dX(x,x′). The other mixed inequalities follow from the infimum and original triangle inequalities. Cross-distances are at least c, so distinct copies are not collapsed. Every R pair has distance at most c. The Hausdorff distance and, when paired, the root distance are consequently at most c.

## 3. Two equivalent definitions of GH distance

<a id="gh-equivalence"></a>

\[ \begin{aligned}
d_{GH}(X,Y)&=\inf_{Z,\phi,\psi}d_H^Z(\phi X,\psi Y)
=\tfrac12\inf_R\operatorname{dis}R,\\
d_{rGH}(X,Y)&=\inf_{Z,\phi,\psi}
\max\{d_H^Z(\phi X,\psi Y),d_Z(\phi\rho_X,\psi\rho_Y)\}\\
&=\tfrac12\inf_{R\ \mathrm{rooted}}\operatorname{dis}R .
\end{aligned} \]

All embeddings are isometric. The bridge proves the upper bounds. Conversely, in an ambient space where both the Hausdorff and root distances are less than r, use all cross-pairs of distance at most r, allowing an arbitrarily small slack if needed. This is a surjective rooted correspondence, with distortion at most 2r by two triangle inequalities. Let r decrease to the relevant infimum. Gluing proves the triangle inequality; symmetry and nonnegativity are immediate.

Zero distance requires an isometry proof. Let correspondence errors rₙ tend to zero. Fix a dense sequence xⱼ in X containing its root and choose corresponding yₙⱼ, choosing the Y root explicitly for the X root. Diagonal compactness in Y gives convergence for every j. Distances of the limits equal the corresponding distances in X, so this map extends isometrically to X. It is onto: for y∈Y choose corresponding xₙ, pass to xₙ→x in compact X, and approximate x by dense points to obtain f(x)=y as the distortions vanish. The root pair preserves the root. The unrooted proof omits that designation.

## 4. Approximating a space by a finite net

<a id="gh-nets"></a>

If A is a finite ε-net in X, adding the root when needed, the original ambient space gives rGH(X,A)≤ε. Real finite distances can be replaced by rational ones without destroying triangle inequalities: for rational η>0 round each nonzero distance upwards to an integer multiple of η. The ceiling function is subadditive in this sense, so the result is a metric, differing by less than η in each entry. Matching identical labels bounds the GH error by η/2.

\[ d^\eta(i,j)=
\begin{cases}\eta\lceil d(i,j)/\eta\rceil,&i\ne j,\\0,&i=j.\end{cases} \]

There are countably many finite rational metric matrices with a distinguished root, and they are dense by this construction. This proves separability and explains why finite approximations preserve pairwise distances rather than drawing positions.

## 5. Completeness through a common space for a Cauchy sequence

<a id="gh-complete"></a>

Take a subsequence of the Cauchy sequence whose successive distances are below εᵢ=2⁻ⁱ. Glue witnessing embeddings successively along their common i-th space, realizing them all in one complete separable Z with successive Hausdorff and root distances below εᵢ. Their union is totally bounded: for δ>0 choose N so the tail sum is below δ/3. All later spaces lie within δ/3 of X(N), whose finite δ/3-net covers the tail with error below δ. The finitely many earlier compact spaces also have finite nets. The closure K of the union is therefore compact.

For completeness, Hausdorff completeness of nonempty compact subsets of K can be checked directly. If Aᵢ is Hausdorff Cauchy, the functions d(·,Aᵢ) converge uniformly to q. Its zero set A is nonempty by choosing aᵢ∈Aᵢ and using compactness. Failure of Hausdorff convergence in one direction would produce a cluster point outside the zero set; the other direction follows from uniform convergence of q on A. Roots form a Cauchy sequence with limit in A. The entire original Cauchy sequence then converges by the triangle inequality. Thus both compact isometry classes and rooted compact isometry classes are Polish.

## 6. A compactness criterion and measurable readings

<a id="gh-compactness"></a>

A family is relatively compact in GH or rooted GH precisely when its diameters are uniformly bounded and, for every r>0, the number N(r) of open r-balls needed to cover the whole space is uniformly bounded. Necessity follows by transferring finite nets from a finite GH approximation of a compact family; diameters differ by at most twice the GH distance. For sufficiency, use η-nets of uniformly bounded size and diameter. Rounding to a fixed rational mesh leaves only finitely many possible matrices. The family is totally bounded, and completeness gives relative compactness. Adding the root costs at most one point.

Diameter is continuous. The set N(r)≤m is open: for a finite open r-ball cover of compact X, the maximum over X of the minimum distance to a center is strictly less than r. Transferring the centers across a sufficiently small GH error still covers the nearby space. These readings are Borel measurable, so the criterion applies to random spaces, not merely deterministic pictures. Return to [geometric tightness in Chapter 55](../chapters/55-metric-measure-limits.md#geometry-polish).
