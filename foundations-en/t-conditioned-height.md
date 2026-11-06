# T-CONDITIONED-HEIGHT: Height, Contour, and Joint Limits under Finite Variance Alone

Companion to [Chapter 53](../chapters/53-tree-scaling.md#scaling-height-problem). Sizes are genuinely feasible; the fixed offspring law is critical and nondegenerate with positive finite variance. Inputs are finite coding, branching and Dwass from Chapter 52, the uniform local CLT from Chapter 13, the integrable iid strong law from Chapter 12, continuous-path tightness from Chapter 24, and this chapter’s proved Łukasiewicz excursion limit. No exponential offspring moment or future tree-space theorem is used.

## 1. Right siblings and a finite-level weighted ancestral line

<a id="height53-spine"></a>

\[ P_n=P(\,\cdot\mid N=n),\qquad a=\frac{\sigma^2}{2}>0,\qquad
W_j=\sum_{u\prec v_j}\bigl(k_T(u)-J_u(v_j)\bigr),\quad H_j=|v_j|,\quad H_n=0,\quad W_n=-1. \]

The sum runs over strict ancestors, and the child index specifies which child leads to the vertex. Just before its visit, the pending list contains that vertex and the unvisited right siblings along its ancestry, giving the identity by Chapter 52. The terminal height zero closes the interpolation; it is not an additional vertex.

\[ P_*(D=k,J=j)=p_k\quad(k\ge1,\ 1\le j\le k),\qquad
R=D-J,\quad Z=D-1,\qquad E_*R=a,\quad E_*Z=\sigma^2. \]

These weights sum to the offspring mean one, so they define a probability. For a marked ancestral line of length h, take independent pairs with this law. Summing over all marked depth-h vertices in the original tree leaves exactly the prescribed offspring factor at each ancestor. This gives the following many-to-one identity for nonnegative line functionals. Sum over offspring counts and selected child indices; unmarked subtrees integrate to one, justified by Tonelli.

\[ E\!\left[\sum_{|v|=h}F(\text{ancestral pairs of }v)\right]
=E_*F((D_i,J_i)_{1\le i\le h}). \]

Both means follow directly from finite variance. At a given offspring count, right-sibling counts run from zero to that count minus one. Total siblings have the offspring-size-biased mean of count minus one. This is only a finite-level weighted identity: no positive local martingale is treated as a probability density and no infinite-level density is identified with a martingale limit.

## 2. Conditioned on total size, the sides of the line form a forest

<a id="height53-forest-density"></a>

\[ A_h=\sum_{i=1}^h Z_i,\qquad R_h=\sum_{i=1}^h R_i,\qquad
q_l^{(r)}=P(N_1+\cdots+N_r=l),\qquad q_n=q_n^{(1)}. \]

A marked line of length h already accounts for its h strict ancestors. Every unselected child carries a subtree, and the terminal vertex carries one complete subtree. The remainder is therefore the total sibling count plus one independent GW trees, with required size n minus h. Applying the root branching property down the finite marked line gives the exact identity

\[ E\!\left[\sum_{|v|=h}F(v)\mathbf1_{\{N=n\}}\right]
=E_*\!\left[F((D_i,J_i)_{i\le h})\,q_{n-h}^{(A_h+1)}\right]\qquad(0\le h<n). \]

For a direct verification, fix every offspring count and child index on the line. The tree product weight splits into ancestral factors and side-forest factors. Their left/right order is determined by the indices, while the size probability depends only on the number of forest roots. Sum first over finite side trees, then over countably many line data. There is no missing whole-tree condition or extra normalization.

\[ q_l^{(r)}=\frac rl P(S_l=-r)\le C r\,l^{-3/2}\quad(l\ge1,\ r\ge1),\qquad
q_n\sim\frac{d}{\sigma\sqrt{2\pi}}\,n^{-3/2}. \]

The forest bound is Dwass from Chapter 52 plus the uniform local bound from Chapter 13. If the number of roots exceeds the vertex count, the left side is zero and the bound still holds. The single-tree asymptotic is along feasible sizes. These estimates control a uniformly chosen vertex’s conditioned ancestry; that ancestry is not simply declared iid.

## 3. Long ancestral segments cannot have too few right siblings

<a id="height53-lower"></a>

\[ c=a/2,\qquad
\exists\theta>0,\ \eta<1:\quad e^{\theta c}E_*e^{-\theta R}=\eta,\qquad
P_*(R_h<ch)\le\eta^h. \]

Right-sibling count is nonnegative with positive finite mean. Its negative-exponential transform has right derivative at zero equal to minus that mean, giving the parameters above. Markov’s inequality gives the exponential lower tail. No positive exponential moment is assumed, so very large offspring remain allowed.

To control every ancestral segment, fix a starting depth b and length h. Branching and expected generation size one in the critical case, followed by many-to-one, bound the expected number of bad segments by that exponential tail. In a tree of size n both depths are at most n. A union bound over starting depths and lengths at least a fixed positive multiple of the square root of n, divided by the size probability, gives

\[ P(\mathcal E_{n,\delta}^{\,c}\mid N=n)
\le\frac{n^2\eta^{\lceil\delta\sqrt n\rceil}}{q_n}\longrightarrow0,\qquad
\mathcal E_{n,\delta}:
\ \sum_{\text{segment}}R_i\ge c\,(\text{length})\quad\text{if length}\ge\delta\sqrt n. \]

For every fixed positive δ all long segments are controlled simultaneously. A short segment has length below the threshold and nonnegative sibling sum. Thus every segment length is bounded by the threshold plus its right-sibling sum divided by c. This is stronger than controlling a typical line and is exactly what the modulus argument needs.

## 4. From ancestral segments to the height modulus

<a id="height53-tightness"></a>

Take two distinct preorder vertices. If the earlier is an ancestor of the later, use the preceding segment bound directly. Otherwise let x and y be the relevant children of their common ancestor, with the x subtree visited first. The path minimum between the visits is at most the value at x because that subtree ends first, and at most the value at y because its starting point lies in the interval.

\[ I_{ij}=\min_{i\le k\le j}W_k,\qquad
|H_i-H_j|\le d_T(v_i,v_j)
\le2+2\delta\sqrt n+\frac{W_i+W_j-2I_{ij}}c
\quad(0\le i<j<n,\ \mathcal E_{n,\delta}). \]

Apply the ancestral-segment bound from each child to its respective vertex, then add the two edges from their common ancestor. This proves the inequality; the wider bound also covers the ancestor case. The last term is bounded by twice the path oscillation on the interval divided by c. The root-to-vertex segment also bounds the maximum height.

\[ \frac{H_i}{\sqrt n}\le\delta+\frac{W_i}{c\sqrt n}\quad(i<n,\ \mathcal E_{n,\delta}). \]

Set height at index n to zero. Near time one the path values in the last bound are uniformly small because the path ends at minus one and has a continuous excursion limit, so closure is controlled too. Linear-interpolation moduli are bounded by grid readings with at most two extra cells. The proved Łukasiewicz paths are tight in the uniform topology with a continuous excursion limit. Fix δ, use the displayed bounds with their path moduli, then let δ decrease to zero. This proves tightness of height divided by the square root of n in continuous functions.

## 5. A typical vertex requires only integrable spinal averages

<a id="height53-typical"></a>

\[ E_n\!\left[\frac1n\sum_{j<n}
\mathbf1_{\{|W_j-aH_j|>\varepsilon\sqrt n\}}\right]
=\frac1{nq_n}\sum_{h=0}^{n-1}
E_*\!\left[\mathbf1_{\{|R_h-ah|>\varepsilon\sqrt n\}}\,
q_{n-h}^{(A_h+1)}\right]. \]

This is the bad-event probability for a uniformly chosen vertex of the size-conditioned tree. It follows from the marked-line identity in Section 2, with zero contribution from the root. Heights exceeding A times the square root of n are uniformly controlled by maximum-height tightness. For fixed A, the remaining forest has at least half of n vertices for large n. Its bound and the single-tree denominator therefore leave a factor at most a constant divided by n times total siblings plus one.

Very short lines contribute at most a constant times δ squared: sum over lengths up to δ times the square root of n and use expected total siblings equal to variance times length. For intermediate lengths, the strong law from Chapter 12 makes average right siblings tend to a, while average total siblings form a uniformly integrable family. The latter must not use a second moment, which size-biased offspring may lack. Here is the argument using only a first moment.

\[ \overline Z_h=\frac1h\sum_{i=1}^hZ_i,\qquad
E_*[\overline Z_h;\overline Z_h>2L]\le2E_*[Z;Z>L]\longrightarrow0
\quad\text{uniformly in }h. \]

The average of terms truncated at L is at most L. If the full average exceeds twice L, its tail average contributes at least half, proving the bound pathwise. Uniform integrability and the strong law give the following estimate; independence between right and total sibling counts is not needed.

\[ \sup_{\delta\sqrt n\le h\le A\sqrt n}
E_*\!\left[\frac{A_h+1}{h};
\left|\frac{R_h}{h}-a\right|>\frac{\varepsilon}{A}\right]\longrightarrow0. \]

The middle-range coefficients sum to the sum of line lengths divided by n, bounded by a constant depending on A, so their product with the vanishing estimate tends to zero. Short lines give δ squared, and long lines are bounded by the tight height tail. First let n tend to infinity, then A to infinity, and finally δ to zero. The expected bad-vertex fraction vanishes, hence the fraction vanishes in probability. All conclusions concern the conditioned tree law; the unconditioned strong law was not substituted for that conditional law.

## 6. From most vertices to the whole curve

<a id="height53-uniform"></a>

\[ D_n(t)=\frac{W(nt)-aH(nt)}{\sqrt n}. \]

Both interpolated paths are tight in continuous functions, so their difference has tight moduli. If its supremum exceeds twice a fixed ε and its oscillation over length η is at most ε, then its absolute value exceeds ε on an interval of length at least half η. For large n that interval contains at least η times n divided by four grid points. Consequently

\[ P_n(\|D_n\|_\infty>2\varepsilon)
\le P_n(\omega(D_n,\eta)>\varepsilon)
+\frac4\eta E_n\!\left[\frac1n\sum_{j<n}
\mathbf1_{\{|W_j-aH_j|>\varepsilon\sqrt n\}}\right]. \]

Choose η by tightness to make the first term arbitrarily small, then use the preceding section to make the second vanish. This proves uniform convergence to zero in probability. The endpoint height zero and path value minus one contribute only an inverse square-root error, not an omitted bad endpoint. This identifies the height limit jointly with the Łukasiewicz path.

\[ \sup_{0\le j\le n}\frac{|W_j-\frac{\sigma^2}{2}H_j|}{\sqrt n}
\xrightarrow{P_n}0,\qquad
\left(\frac{W(n\,\cdot)}{\sigma\sqrt n},\frac{\sigma H(n\,\cdot)}{2\sqrt n}\right)
\Rightarrow(e,e). \]

## 7. The contour’s actual clock and error

<a id="height53-contour"></a>

\[ b_j=2j-H_j,\quad s_j=j/n,\quad t_j=b_j/(2(n-1))\ (j<n),\qquad
s_n=t_n=1,\qquad
\max_j|t_j-s_j|\le\frac1{n-1}+\frac{\max_j H_j}{2(n-1)}
\xrightarrow{P_n}0. \]

Take n at least two; the root-only exception does not affect limits. Chapter 52 proved that these first-visit times are strictly increasing, with the last still before the true endpoint. Join the vertex-time and contour-time pairs by a piecewise linear homeomorphism, denoted λ. It is uniformly close to the identity, and its inverse has the same uniform distance.

\[ h_n(t)=\frac{\sigma H(nt)}{2\sqrt n},\qquad
c_n(t)=\frac{\sigma C(2(n-1)t)}{2\sqrt n},\qquad
\|c_n\circ\lambda-h_n\|_\infty
\le\frac{\sigma}{2\sqrt n}\left(1+\max_{j<n}|H_{j+1}-H_j|\right)
\xrightarrow{P_n}0. \]

Between consecutive first visits, the contour returns to the next vertex’s parent and then ascends one edge. Its discrepancy from the segment between the height readings is at most their height difference plus one. The last segment returns straight to the root and satisfies the same bound. Tightness with a continuous height limit makes the largest grid jump divided by the square root of n vanish. The height modulus and convergence of the inverse clock then remove the time change. Close clocks alone were not used to ignore oscillations.

## 8. The joint theorem, interpolation, and precise scope

<a id="height53-joint"></a>

\[ \boxed{\quad
\left(\frac{W(n\,\cdot)}{\sigma\sqrt n},
\frac{\sigma H(n\,\cdot)}{2\sqrt n},
\frac{\sigma C(2(n-1)\,\cdot)}{2\sqrt n}\right)
\Rightarrow(e,e,e)\quad\text{in }C([0,1])^3.\quad} \]

This is joint weak convergence of the three curves from the same conditioned tree. The limit coordinates are the same normalized excursion, not three independent copies. The two uniform probability comparisons and the proved limit of the first coordinate establish the result. Finite coding makes all maps measurable; joint convergence does not require pathwise convergence on the original space.

Step and linear heights differ by the largest grid height jump, already proved negligible. For Łukasiewicz paths the same conclusion follows from T-CONDITIONED-BRIDGE and preservation of increments by rotation. Step versions converge in D with J₁, with the uniform comparisons stronger here because the limit is continuous. A contour clock of twice n first requires zero extension after its true endpoint and then the proved modulus to control the small relative time error. Replacing the square root of n by that of n minus one likewise uses norm tightness.

No real-tree property of the coding quotient, GH/GHP convergence, infinite-variance case, or general Lévy height process is proved here. Chapters 54–55 and 58 retain those responsibilities. Chapter 52’s exact finite coding does not itself imply this theorem. The new core consists of conditioned-bridge control, cut-bridge identification, and the complementary estimates for all ancestral segments and a typical vertex. Return to [Chapter 53](../chapters/53-tree-scaling.md#scaling-joint).
