# Chapter 53: Why Do Discrete Random Trees Develop Continuous Shapes?

Keeping only families with exactly ten thousand members changes how offspring experiments are observed. If one vertex has extra children, the rest of the family must compensate or the total will miss the prescribed size. Previously independent reproduction records become a globally constrained string.

Chapter 52 found an exact operation: fix the sum of an iid offspring string, then cut it at the right place to obtain a conditioned tree. A finite sampling algorithm does not tell us how to rescale large-tree paths or guarantee a continuous contour. The pending-visit path and ancestral height determine one another, but need not respond equally stably to small path errors.

## 53.1 Fixing total population is more than changing an endpoint label

<a id="scaling-conditioning"></a>

\[ P(N=n)=\frac1n P(S_n=-1),\qquad S_k=\sum_{i=1}^k(\xi_i-1). \]

A tree requires first arrival at minus one at step n. The iid bridge requires only arrival there at step n and permits earlier visits. The cycle lemma relates them exactly without making either conditioning event less rare.

Ordinary Donsker describes unconditioned path laws. The probability of a fixed endpoint lattice site tends to zero, corresponding to a null restriction in the weak limit. A good approximation on most paths need not remain good among paths selected by such a rare event. What is needed is an explicit, controlled conditional weight.

## 53.2 First specify the trees and the sizes that actually exist

<a id="scaling-assumptions"></a>

\[ E\xi=1,\qquad0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad
d=\gcd\{k\ge1:p_k>0\},\qquad P(N=n)>0,\quad P_n=P(\,\cdot\mid N=n). \]

The fixed offspring law takes finite nonnegative integer values and is used independently at every potential vertex. The main theorem concerns this critical, nondegenerate, finite-variance class. Zero offspring has positive probability and d is its maximal lattice span. Sizes must be one modulo d; small sizes also need a genuine feasibility check. Chapter 52 proved feasibility of all sufficiently large sizes in the correct residue class.

Standard Brownian motion still has increment variance equal to elapsed time. The target excursion has duration one, with the convention of Chapter 37 given by the norm of three independent standard bridges. Keep these units fixed until the height constant has been derived, then align the three encodings.

## 53.3 The remaining population determines a prefix’s conditional weight

<a id="scaling-bridge"></a>

\[ p_l(z)=P(S_l=z),\qquad
E_n^{\mathrm{br}}F=
E\!\left[F\,\frac{p_{n-k}(-1-S_k)}{p_n(-1)}\right],\quad F\text{ bounded and }\mathcal F_k\text{-measurable}. \]

Given the first k readings, future increments remain independent. To end at minus one they must supply the remaining displacement. The numerator is that probability and the denominator normalizes the selection. This is legitimate finite-size conditioning, not division by the probability of a Brownian endpoint being zero.

A high prefix requires a larger future return and receives less weight. The amount must be determined by local probability estimates. See [T-CONDITIONED-BRIDGE](../foundations/t-conditioned-bridge.md#bridge53-density) for the density and measurability.

## 53.4 The local CLT turns vanishing probabilities into a finite density

<a id="scaling-local-clt"></a>

\[ p_n(-1)\sim\frac{d}{\sigma\sqrt{2\pi n}},\qquad
P(N=n)\sim\frac{d}{\sigma\sqrt{2\pi}}n^{-3/2},\qquad
\sup_zp_l(z)\le C l^{-1/2}. \]

The bridge denominator is of inverse square-root order; the tree denominator has one further inverse-size factor. They must not be confused. The uniform lattice local CLT of Chapter 13 evaluates the denominator and bounds all remaining positions. On a fixed initial fraction of the path, it makes the conditional weight uniformly bounded.

\[ k=\lfloor an\rfloor,\quad S_k/(\sigma\sqrt n)\approx x:
\qquad\frac{p_{n-k}(-1-S_k)}{p_n(-1)}
\approx \frac1{\sqrt{1-a}}\exp\!\left(-\frac{x^2}{2(1-a)}\right),\quad0<a<1. \]

The approximation is uniform on compact sets of normalized positions. Span factors cancel, but lattice phases still matter: feasible total size and a realizable prefix put the remaining endpoint in its allowed lattice. Truncate positions to a compact set, apply unconditional Donsker with the weight, then enlarge the truncation before concluding.

## 53.5 This weight identifies a bridge

<a id="scaling-gaussian-bridge"></a>

\[ b(t)=B_t-tB_1,\qquad
E F(b|_{[0,a]})=
E\!\left[F(B|_{[0,a]})\frac{e^{-B_a^2/(2(1-a))}}{\sqrt{1-a}}\right]. \]

The weight is the Gaussian density of returning to zero during the remaining time divided by the full-time return density. Multiplying Gaussian increment densities gives covariance equal to the smaller time minus their product, identifying the already constructed standard Brownian bridge.

This explains why the conditional limit is not the original Brownian motion: prefix readings are reweighted by the requirement to return. It is not yet a nonnegative excursion; the bridge can still take negative values.

## 53.6 How initial estimates control the bridge endpoint

<a id="scaling-bridge-tight"></a>

The bounded prefix density transfers Chapter 25’s path tightness to any strict prefix, but deteriorates near the endpoint. The conditioned string provides the remedy: reversing increment order preserves its conditional law. The terminal segment read backwards therefore satisfies the same estimates as the initial one.

Control moduli on the first two thirds and last two thirds. Any sufficiently close pair of times lies together in one interval, so the estimates combine into whole-bridge tightness. Tightness and the preceding finite-dimensional identification prove uniform-topology convergence of the interpolated bridge. Only a finite second moment is used, without adding fourth or exponential moments.

The largest step divided by the square root of size also vanishes: bound the conditional density of one coordinate, take a union bound, and use the second-moment tail. Thus step and linear interpolation do not yield different limits here. See [T-CONDITIONED-BRIDGE](../foundations/t-conditioned-bridge.md#bridge53-tightness).

## 53.7 Close the small endpoint gap before examining the cut

<a id="scaling-cut"></a>

\[ x_n(t)=S(nt)/(\sigma\sqrt n),\qquad
b_n(t)=x_n(t)+t/(\sigma\sqrt n),\qquad
r_n=\frac1n\min\operatorname*{arg\,min}_{0\le j<n}S_j. \]

Interpolate partial sums linearly between integers. The original endpoint is minus one divided by the standard deviation and square root of size. Adding the displayed line closes the bridge with a uniformly vanishing error. The discrete tree cut remains the first minimum of the original sums, not the last.

If the limit bridge had several equal minima, a tiny error could move the cut between them and change the rotated curve. A continuous limit for the finite cyclic operation first requires ruling out this instability.

## 53.8 The Brownian bridge has one interior minimum

<a id="scaling-minimum"></a>

On each strict prefix the bridge has a Gaussian density relative to Brownian motion. Brownian motion has negative values immediately after starting at zero, so the bridge minimum is strictly negative and cannot occur only at its endpoints. Two distinct minimizing times could be enclosed by rational intervals separated by a positive gap.

For Brownian motion, conditioning on the left interval’s past and the relative increments after the right interval’s start leaves an independent nondegenerate Gaussian gap increment in the difference of their minima. Equality has probability zero. Absolute continuity transfers this to the bridge; a countable union proves uniqueness. This is the probabilistic foundation of continuity of the cut; see [T-VERVAAT](../foundations/t-vervaat.md#vervaat53-minimum).

## 53.9 The minimum becomes the new starting point

<a id="scaling-vervaat"></a>

\[ \rho=\operatorname*{arg\,min}b,\qquad Vb(t)=b((\rho+t)\bmod1)-b(\rho). \]

Join the bridge into a circle, start at its minimum, and subtract that value. The result is zero at both ends and positive inside. These properties do not yet identify its probability law; many laws have positive continuous excursions.

Deterministic continuity can already be proved. Away from the unique minimum, compactness gives a strictly positive height gap. Near-minimum cuts of uniformly close bridges must therefore approach it, and uniform continuity on the circle makes their rotations uniformly close. For the unclosed path, wrapping adds its old endpoint, leaving a vanishing error after correction. Bridge, cut, and rotated path thus converge jointly, not as unrelated marginal limits assembled afterwards.

## 53.10 Why the cut bridge is the excursion of Chapter 37

<a id="scaling-excursion"></a>

Temporarily regard the cut bridge as a candidate. Choose offspring zero and two with equal probabilities, giving simple symmetric walk and odd sizes. All bridge words are equally likely, and Chapter 52’s cyclic count makes legal rotated words equally likely too. Removing the final step to minus one gives a uniform Dyck path.

The bridge limit and cut continuity already make these Dyck paths converge to the candidate, so no Dyck-to-excursion theorem is assumed. Reflection calculates their finite-dimensional probabilities independently for comparison with Chapter 37’s normalization.

\[ K_l(x,y)=p_l^{\mathrm{sym}}(y-x)-p_l^{\mathrm{sym}}(y+x+2),\qquad x,y\ge0. \]

This kernel kills at minus one. Reflection up to the first hit counts the forbidden paths to subtract. Multiplying entrance, intermediate, and final return kernels, then dividing by the full-duration return kernel, gives every conditioned Dyck joint probability.

## 53.11 An entrance constant that cannot come from subtracting approximations

<a id="scaling-normalization"></a>

For two interior points away from the boundary, Chapter 13 directly gives the killed Gaussian kernel. At an entrance from zero the two leading terms nearly cancel, so a local-CLT error alone is not accurate enough. Binomial coefficients supply an exact ratio:

\[ K_l(0,y)=p_l^{\mathrm{sym}}(y)\frac{2(y+1)}{l+y+2}. \]

This gives precise entrance, exit, and denominator asymptotics. Divide by the spacing of the allowed parity sites as well; this cancels an extra exit factor of two. The resulting finite-dimensional density agrees with the duration-one excursion in Chapter 37:

\[ q_t(x,y)=\frac{e^{-(y-x)^2/(2t)}-e^{-(y+x)^2/(2t)}}{\sqrt{2\pi t}}\quad(x,y>0). \]

\[ \frac{k_{t_1}(y_1)\prod_{i=2}^{j}q_{t_i-t_{i-1}}(y_{i-1},y_i)\,h_{1-t_j}(y_j)}{c_1},\qquad
k_t(y)=2h_t(y)=\frac{2y}{\sqrt{2\pi}t^{3/2}}e^{-y^2/(2t)},\quad c_1=\frac1{\sqrt{2\pi}}. \]

The radius of three-dimensional Brownian motion has transition density q multiplied by the next radius divided by the previous one. The bridge’s terminal Gaussian weight makes those radius ratios telescope into this density. The cut-bridge candidate therefore has the law of the norm of three independent standard bridges. See [T-VERVAAT](../foundations/t-vervaat.md#vervaat53-density) for entrance errors, Riemann sums, and total mass one.

## 53.12 The first conditioned-tree path limit is now proved

<a id="scaling-lukas-limit"></a>

\[ \frac{W^{(n)}(n\,\cdot)}{\sigma\sqrt n}\Rightarrow e,\qquad
e(t)=\sqrt{b_1(t)^2+b_2(t)^2+b_3(t)^2}
\quad\text{in }C([0,1]). \]

Every offspring law first gives the same standard bridge and cut. The simple-walk case identifies that cut law, so the conclusion is not restricted to binary trees. Paths are linearly interpolated. Their terminal value, minus one divided by the standard deviation and square root of size, tends to zero; finite paths are not required already to be zero-ended continuous excursions.

Vervaat proved this relation between bridge and excursion in 1979. Here it is reconstructed through finite cuts and explicit Dyck kernels rather than invoked by name. The pending-task path limit is established, but a genealogical problem still remains.

## 53.13 Close task paths can hide very deep trees

<a id="scaling-height-problem"></a>

A single-child chain has Łukasiewicz value zero until its final step, tending uniformly to zero after square-root scaling. Its height increases to the vertex count minus one and still diverges after that scaling. Recoverability of height from a path does not imply continuity of the recovery map in the uniform topology.

Even a sequence whose task paths converge to a nonzero continuous excursion can be prefixed with a single-child chain of length original size to power three quarters. The added zero segment has vanishing relative duration and preserves the continuous task-path limit, but raises heights by much more than square-root size. The conditioned GW law needs its own probabilistic argument excluding such chains.

\[ \ell_m=\lfloor m^{3/4}\rfloor,\quad N_m=m+\ell_m,\quad
\widetilde f_m(t)=\sqrt{m/N_m}\,f_m(g_m(t)),\quad
g_m(t)=\max\{0,(N_mt-\ell_m)/m\}. \]

Here the old task curve is normalized by the square root of its old size. The new clock tends uniformly to the identity and the coefficient tends to one, preserving a continuous limit. New height is at least the added chain length, which divided by the square root of the new size diverges. This failure mechanism works even at a nonzero limit, without claiming that artificially prefixed trees retain a fixed conditioned GW law.

## 53.14 The difference between depth and the number of right siblings

<a id="scaling-right-siblings"></a>

\[ W_j=\sum_{u\prec v_j}\bigl(k_T(u)-J_u(v_j)\bigr),\qquad H_j=|v_j|. \]

Before the current visit, the pending list contains the current vertex and the right children not yet visited at each ancestor. Removing the current slot gives this identity. Task value sums right siblings along ancestry, while height adds one for each ancestor.

Their macroscopic ratio must therefore come from average siblings along conditioned ancestry. The obstruction is concrete: a long line with almost no right siblings makes height large while task value stays small. First control such exceptional segments, then calculate the typical ratio.

## 53.15 Why marking a descendant changes ancestral offspring weights

<a id="scaling-spine"></a>

To sum an ancestral attribute over all depth-h vertices, mark each vertex in turn. An ancestor with k children contributes k possible directions. Offspring counts along the marked line are therefore no longer observed under their original law, but each offspring-count and selected-direction pair has a simple weight.

\[ P_*(D=k,J=j)=p_k\quad(1\le j\le k),\qquad
R=D-J,\quad Z=D-1,\qquad E_*R=\frac{\sigma^2}{2}=a,\quad E_*Z=\sigma^2. \]

Total weight is the offspring mean one, so this is a probability. Along a finite marked line take independent pairs with this law. The identity comes from summing over children, a finite-level many-to-one calculation, not an assumed infinite-level martingale density. Size bias from Chapter 20 has a new use: identifying the ratio between depth and pending lateral visits rather than loss of expectation in a population-growth limit.

The mean number of right siblings is half the variance because, for a given offspring count, its values run from that count minus one down to zero over selected children. Summing and weighting by original offspring probabilities gives the formula. The factor two in the height normalization first appears here, rather than being inserted to fit an excursion.

## 53.16 How total-size conditioning enters the marked line

<a id="scaling-spinal-forest"></a>

\[ A_h=\sum_{i=1}^hZ_i,\qquad R_h=\sum_{i=1}^hR_i,\qquad
q_l^{(r)}=P(N_1+\cdots+N_r=l). \]

A line of length h accounts first for its h ancestors. Every unselected child carries a subtree, and its terminal vertex carries one complete subtree. The remainder is total siblings plus one independent trees. Conditioning the whole tree to size n requires this forest to have n minus h vertices. For every nonnegative F depending only on ancestral offspring counts and directions,

\[ E\!\left[\sum_{|v|=h}F(v)\mathbf1_{\{N=n\}}\right]
=E_*\!\left[F\,q_{n-h}^{(A_h+1)}\right]. \]

This retains the global size reweighting of ancestry, so conditioned ancestors are not simply iid. The advantage is that the reweighting is now an explicit forest probability, exactly what Chapter 52’s multi-ancestor Dwass formula supplies. See [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-forest-density) for construction, factorization, and nonnegative summation.

## 53.17 Finite variance still permits one useful exponential estimate

<a id="scaling-long-lines"></a>

Large offspring may have no positive exponential moment, but the event to exclude is on the other side: too few right siblings along a long segment. A nonnegative variable always has a finite negative-exponential transform, whose slope at zero is determined by its positive mean. Hence

\[ c=a/2,\qquad P_*(R_h<ch)\le\eta^h\quad\text{for some }0<\eta<1. \]

Many-to-one bounds the expected number of bad lines at a fixed starting depth and length. Both are at most n in a size-n tree. A union bound with at most n squared terms, divided by the size probability, bounds the conditional probability of a bad segment longer than δ times the square root of n by

\[ \frac{n^2\eta^{\lceil\delta\sqrt n\rceil}}{P(N=n)}\longrightarrow0\qquad(\delta>0). \]

The denominator has the precise order n to power minus three halves, and the exponential lower tail dominates this polynomial cost. The conclusion controls all long ancestral segments simultaneously, rather than merely saying that one typical descendant is unlikely to be too deep.

## 53.18 Common ancestors convert path oscillation into height oscillation

<a id="scaling-height-tight"></a>

On the event with no bad long segment, an ancestral segment’s length is at most δ times the square root of n plus its right-sibling sum divided by c. Take two preorder vertices, return to their common ancestor, and apply this bound along the two child branches. The intervening task-path minimum is no higher than either branch’s starting value, giving

\[ |H_i-H_j|\le2+2\delta\sqrt n+
\frac{W_i+W_j-2\min_{i\le k\le j}W_k}{c}\qquad(i<j<n). \]

The final term is controlled by task-path oscillation over the same short window. The root-to-vertex version also bounds maximum height, and the vanishing task endpoint controls the appended terminal height zero. Use the task path’s continuous limit for modulus control, then let δ decrease to zero. This proves tightness of the square-root-scaled height path in continuous functions.

The exact height multiplier is not yet identified, but the short-time long chains of Section 13 have been excluded. This is the bridge from correctness at most vertices to correctness along the entire curve. See [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-tightness) for the ancestor decomposition.

## 53.19 Start with a typical vertex without assuming a second size-biased moment

<a id="scaling-typical-vertex"></a>

Choose a vertex uniformly from the size-conditioned tree. At height h its task value is the sum of right siblings, and the marked-line identity gives the exact weight of deviation from a times height. Forest Dwass and the local CLT provide

\[ q_l^{(r)}\le C r\,l^{-3/2}. \]

Maximum-height tightness lets us restrict first to lines no longer than A times the square root of n. Their remaining forest size is still of order n. Dividing by the single-tree size probability leaves at most a constant times total siblings plus one. Divide by vertex count and sum over possible depths.

For intermediate line lengths, the strong law makes average right siblings tend to a. Because this is multiplied by total siblings, convergence in probability alone is insufficient. The required uniform integrability uses only a first moment:

\[ \overline Z_h=\frac1h\sum_{i=1}^hZ_i,\qquad
E_*[\overline Z_h;\overline Z_h>2L]\le2E_*[Z;Z>L]\longrightarrow0. \]

If the average exceeds twice L, its part above L contributes at least half. Size-biased offspring may lack a second moment, but this tail argument still works. Very short lines contribute at most a constant times δ squared, very long lines are controlled by height tightness, and intermediate lines by the strong law and uniform integrability. Therefore

\[ \frac1n\#\{j<n:|W_j-aH_j|>\varepsilon\sqrt n\}\xrightarrow{P_n}0. \]

Every conditional weight and order of limits appears in [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-typical). The unconditioned spinal strong law has not been applied directly to conditioned ancestry.

## 53.20 How correctness at most vertices becomes uniform correctness

<a id="scaling-height-uniform"></a>

Both normalized curves have controlled moduli. A fixed discrepancy at one position cannot disappear immediately nearby; it persists on a small interval of fixed length, creating a positive proportion of bad vertices. The preceding result excludes that proportion, hence

\[ \sup_{0\le j\le n}\frac{|W_j-\frac{\sigma^2}{2}H_j|}{\sqrt n}
\xrightarrow{P_n}0,\qquad
\frac{\sigma H(n\,\cdot)}{2\sqrt n}\Rightarrow e. \]

Finite-tree heights are not asserted to be a constant multiple of task paths. The curves can differ greatly. The theorem says that under the specified conditioned GW laws and scaling their maximum discrepancy vanishes in probability. Averages along lines identify the constant; control of all ancestral segments protects the entire curve. Both arguments are needed.

## 53.21 Why the contour runs for twice the edge count

<a id="scaling-contour"></a>

\[ b_j=2j-H_j,\qquad
\left|\frac{b_j}{2(n-1)}-\frac jn\right|
\le\frac1{n-1}+\frac{\max_iH_i}{2(n-1)}
\xrightarrow{P_n}0. \]

Chapter 52’s clock now applies. The jth vertex is first visited at this edge-traversal time. Maximum height is of square-root order, so normalized contour and vertex clocks are uniformly close. Close clocks alone are not sufficient; returns between first visits still need an estimate.

The contour returns to the next vertex’s parent, then goes up one edge. Its discrepancy from the segment joining the two height readings is at most their height jump plus one. Height tightness with a continuous limit makes the largest scaled jump negligible, including the last return to the root. A piecewise linear clock correspondence, followed by the height modulus to remove its error, gives the same excursion limit for the contour.

See [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-contour) for the finite-path error bound. A tree with n vertices has n minus one edges, so its true contour duration is twice n minus one, not twice n.

## 53.22 Three paths converge jointly to the same excursion

<a id="scaling-joint"></a>

\[ \left(
\frac{W^{(n)}(nt)}{\sigma\sqrt n},
\frac{\sigma H^{(n)}(nt)}{2\sqrt n},
\frac{\sigma C^{(n)}(2(n-1)t)}{2\sqrt n}
\right)_{0\le t\le1}
\Rightarrow(e,e,e)\quad\text{in }C([0,1])^3. \]

This is the conditioned-tree functional limit theorem under the fixed critical nondegenerate finite-variance offspring law of Section 2, with sizes tending to infinity through positive-probability values. Append height zero at vertex index n and interpolate all paths linearly. The limit is the standard duration-one normalized excursion of Chapter 37.

The three limit coordinates are the same random curve, not independent excursions. The task path converges first, height is uniformly close to it, and contour uniformly close to height. These shared error estimates prove joint convergence, stronger than three marginal statements. See [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-joint).

## 53.23 What precisely this convergence means

<a id="scaling-topology"></a>

The linear versions live in continuous functions with the uniform norm. Step versions of Łukasiewicz and height are not continuous, but their uniform distance from interpolation is bounded by the largest grid jump, already proved negligible. They therefore have the same continuous limit in D with J₁. No claim is made that individual original-space paths approach a preselected excursion.

Using twice n instead of the true contour duration requires zero extension after completion and the proved modulus to control the relative time error. Replacing the square root of n by that of n minus one likewise uses norm tightness. These substitutions are valid asymptotically without making finite vertex counts, edge counts, and visits the same quantity.

## 53.24 One normalized shape with different microscopic scales

<a id="scaling-models"></a>

The critical full binary model has offspring zero and two with equal probabilities, variance one, and odd feasible sizes. Height and contour are multiplied by one divided by twice the square root of vertex count. Critical geometric offspring have variance two and give uniform plane trees conditional on size; height and contour are multiplied by one divided by the square root of twice vertex count.

\[ p_0=p_2=\tfrac12:\ \sigma^2=1;\qquad
p_k=2^{-k-1}:\ \sigma^2=2,\ d=1. \]

The models are not identical before normalization. Variance remains in the height unit and periodicity in the feasible sizes. After those factors are adjusted correctly, their whole-path laws approach the same standard excursion. By a continuous mapping, maximum height with the same scale converges to the excursion maximum. This is still a function-space result, not yet a CRT space limit.

## 53.25 Changing offspring laws without changing conditioned shape

<a id="scaling-criticality"></a>

Criticality centers the walk and normalizes finite marked-line weights to one. Without it, the constants and bridge estimates no longer follow. A simple counterexample is a nondegenerate offspring law on zero and one. At every finite conditioned size the tree is a chain, with height of order size rather than its square root.

That example does not make criticality an absolute necessity for conditioned shape. When an exponential tilt is available, distinct offspring laws can give exactly the same size-conditioned trees:

\[ p_k^{(\theta)}=\frac{\theta^k p_k}{f(\theta)},\quad0<f(\theta)<\infty,\ \theta>0:
\qquad P^{(\theta)}(\mathcal T=t)=
\frac{\theta^{n-1}}{f(\theta)^n}P(\mathcal T=t)\quad(|t|=n). \]

The ratio depends only on size, so positive-probability size-conditioned laws agree. If a tilted representative is critical with positive finite variance, this chapter applies using that representative’s variance. Chapter 52’s geometric laws all giving uniform conditioned plane trees are a concrete example. The original noncritical variance cannot simply be substituted.

## 53.26 Finite variance, a fixed law, and conditioning have separate roles

<a id="scaling-boundaries"></a>

The critical zero-variance law gives exactly one child forever and no finite tree. With infinite variance, the square-root units, local CLT, and sibling means used here lose their assumptions. More general stable height limits need separate proofs; an infinite variance cannot be inserted formally into these formulas.

Even finite variance in every individual model does not allow arbitrary size-dependent offspring laws. In model r, for r at least two, take offspring zero or r with probabilities one minus one over r and one over r. It is critical with variance r minus one. Conditional on total size r plus one, the only tree is a star with r leaves. Its variance-normalized maximum height tends deterministically to one half, and the task path retains a macroscopic jump, unlike the continuous excursion limit here.

Conditioning on total size exactly n differs from conditioning on at least n, survival to a generation, or a fixed number of leaves. Other limits may exist, but require recalculating weights and scales. Periodicity likewise cannot be hidden in a statement that n tends to infinity: the binary model has no even-size conditioned law.

## 53.27 The continuous limit has not yet constructed tree geometry

<a id="scaling-insight"></a>

At a fixed finite size we can recover the whole tree vertex by vertex. As size grows, three new tasks are required: controlling rare-event weights, stabilizing the cut, and ensuring that small task-path errors do not become deep macroscopic branches. Exact bijections and probabilistic limits are genuinely different levels of theorem.

A common excursion limit does not make individual reproduction details identical. Under a fixed law, specified conditioning, and variance scale, their effects on these global function readings are controlled. Biased ancestral averages explain the multiplier and estimates for all segments protect continuity. This universality has a concrete mechanism and definite boundaries.

What has been obtained is a probability law on continuous curves. To interpret their minima as common ancestors requires constructing a quotient space, proving it is a real tree, then choosing a topology to compare different tree spaces. Function convergence has not done those jobs. Chapters 54 and 55 have those distinct responsibilities; this chapter supplies their function-level foundation.

Complete proofs are in [T-CONDITIONED-BRIDGE](../foundations/t-conditioned-bridge.md), [T-VERVAAT](../foundations/t-vervaat.md), and [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md). Historical and scope checks use [Vervaat’s 1979 original issue record](https://www.jstor.org/stable/i312960), [Aldous’s 1993 author paper](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf), and [Duquesne’s 2003 conditioned-tree paper](https://perso.lpsm.paris/~tduquesne/Documents/Duquesne_AOP_2003.pdf). The bridge, finite marked-line, and uniform-control route is organized here as a modern reconstruction, not attributed as those papers’ original discovery narrative. Broader stable and metric-tree theorems are not counted as proved here.
