# T-VERVAAT: From Lattice-Bridge Cuts to the Normalized Brownian Excursion

Companion to [Chapter 53](../chapters/53-tree-scaling.md#scaling-vervaat). We prove continuity of cutting a bridge, identify the limit by reflection counts for simple walks, then check the three-dimensional bridge-norm convention of Chapter 37. Neither Vervaat’s theorem nor a conditioned-tree height limit is assumed.

## 1. The bridge minimum is unique and interior

<a id="vervaat53-minimum"></a>

On an initial interval ending strictly before one, the standard bridge has the positive Gaussian density relative to Brownian motion proved in T-CONDITIONED-BRIDGE. Brownian motion started at zero has probability zero of staying nonnegative for any positive duration, by the reflection principle with a negative threshold tending to zero. The bridge minimum is therefore strictly negative and is attained at neither endpoint.

Take two rational closed intervals inside (0,1), separated by a positive gap. For Brownian motion, condition on the path up to the end of the first interval and the relative increments after the start of the second. The difference between their minima still contains the independent nondegenerate Gaussian increment across the gap, so equality has probability zero. Absolute continuity on a strict bridge prefix transfers this conclusion to the bridge. Two distinct minimizers could be enclosed by such intervals. Their countable union proves uniqueness.

\[ \rho=\operatorname*{arg\,min}_{0\le t\le1}b(t)\in(0,1)\quad\text{a.s.} \]

## 2. The cut and the path must converge together

<a id="vervaat53-continuity"></a>

\[ V_r f(t)=f((r+t)\bmod1)-f(r)\quad(f(0)=f(1)=0),\qquad V f=V_{\rho(f)}f. \]

Extend a closed bridge periodically and interpret seams and endpoints by continuity. If closed bridges converge uniformly to a continuous bridge with a unique interior minimum, and grid cuts have values approaching the grid minimum, the cuts converge to that minimizer. Indeed, outside any fixed neighborhood of the unique minimum, compactness gives a strictly positive gap above it. Uniform error, endpoint correction, and grid oscillation eventually become smaller than this gap.

\[ \|V_{r_n}f_n-V_r f\|_\infty
\le2\|f_n-f\|_\infty+2\omega_{\mathrm{circle}}(f,|r_n-r|)\longrightarrow0. \]

The first grid minimum is a Borel function of finitely many readings. The first minimum of a continuous function is measurable as well: minima on rational closed subintervals and comparison with the global minimum locate it; on the uniqueness set it is also the limit of increasingly fine grid near-minima. Exceptional functions may receive any fixed cut. The mapping principle and Skorokhod realization of Chapter 24 therefore give joint limits, rather than separately chosen limits pasted together.

## 3. Discrete cuts with endpoint defect minus one

<a id="vervaat53-discrete"></a>

\[ r_n=\frac1n\min\operatorname*{arg\,min}_{0\le j<n}S_j,\qquad
W^{(n)}=\text{the cyclically shifted increments of }S\text{ at }nr_n. \]

Under bridge conditioning the total increment is minus one. Chapter 52 proved that the first-minimum shift gives exactly the Łukasiewicz path of the size-conditioned GW tree. The corrected bridge differs from the original path by at most its endpoint defect, making these cuts near-minima of the corrected bridge. The strict interior minimum removes the omitted-endpoint issue.

\[ (b_n,r_n,\ W^{(n)}(n\,\cdot)/(\sigma\sqrt n))
\ \Rightarrow\ (b,\rho,Vb)\quad\text{in }C([0,1])\times[0,1]\times C([0,1]). \]

The last coordinate is linearly interpolated. After wrapping an unclosed path, add its old endpoint and subtract the cut value; do not use the closed-loop formula unchanged. Its difference from the corrected rotation is at most twice the closing error and vanishes. The preceding deterministic argument applies pathwise in a joint realization from Chapter 24 and gives the displayed weak convergence. Denote the candidate cut-bridge limit below. It is positive inside and zero at both ends, but its excursion law remains to be identified.

\[ e^*=Vb. \]

## 4. Simple walks give an exactly countable Dyck experiment

<a id="vervaat53-dyck"></a>

Choose offspring zero and two with equal probabilities, so increments are symmetric plus or minus one and sizes are two m plus one. All bridge words are equally likely. The unique legal cut and its n distinct preimages from Chapter 52 make all legal first-passage words equally likely after rotation. Delete the final minus-one step. The result is a uniform nonnegative simple walk returning from zero to zero in two m steps, a Dyck path.

Normalize time by two m and space by its square root. Deleting the final step changes the time ratio to one and the endpoint defect to zero. The preceding continuous limit and tightness control this time change through the modulus, so these Dyck paths already converge to the cut-bridge candidate. Reflection will now calculate its finite-dimensional laws.

\[ K_l(x,y)=p_l^{\mathrm{sym}}(y-x)-p_l^{\mathrm{sym}}(y+x+2),\quad x,y\ge0. \]

This is the transition probability for simple walk killed at minus one. Reflect the path up to its first hit there, giving a bijection between forbidden paths from x to y and unrestricted paths from minus x minus two to y, leaving the later segment unchanged. A conditioned Dyck finite-dimensional probability is the product of the entrance K, intermediate K factors, and final K back to zero, divided by the full-duration K from zero to zero. Only permitted parity sites are used.

## 5. The factors of two in entrance, exit, and lattice density

<a id="vervaat53-density"></a>

\[ g_t(y)=\frac{e^{-y^2/(2t)}}{\sqrt{2\pi t}},\quad
q_t(x,y)=g_t(y-x)-g_t(y+x),\quad
k_t(y)=\frac{2y}{t}g_t(y),\quad h_t(y)=\frac{y}{t}g_t(y),\quad c_1=\frac1{\sqrt{2\pi}}. \]

Let the Dyck duration be an even integer N, with observation indices divided by N tending to strictly interior times. Normalize positive positions by the square root of N and restrict them to compact sets away from zero. Chapter 13 gives the intermediate-kernel asymptotic below. The entrance difference needs greater precision than subtracting two local-CLT approximations; use the exact binomial ratio instead.

\[ K_l(x,y)\sim\frac2{\sqrt N}q_t(x/\sqrt N,y/\sqrt N),\quad l/N\to t>0;\qquad
\frac{p_l^{\mathrm{sym}}(y+2)}{p_l^{\mathrm{sym}}(y)}=\frac{l-y}{l+y+2}. \]

\[ K_l(0,y)=p_l^{\mathrm{sym}}(y)\frac{2(y+1)}{l+y+2}
\sim\frac2N k_t(y/\sqrt N),\quad
K_l(y,0)=K_l(0,y),\qquad K_N(0,0)\sim4c_1N^{-3/2}. \]

These asymptotics hold uniformly on the stated compact sets, and the full denominator follows by the same exact ratio at position zero. Allowed sites at each observation time are spaced by two divided by the square root of N. Dividing joint probabilities by these cell volumes gives the density

\[ Q_1(dy_1\cdots dy_j)=
\frac{k_{t_1}(y_1)\prod_{i=2}^j q_{t_i-t_{i-1}}(y_{i-1},y_i)\,h_{1-t_j}(y_j)}{c_1}
\,dy_1\cdots dy_j. \]

The raw exit contributes k, but division by grid volumes and the total denominator leaves an additional factor one half, turning the exit into h. This is the essential normalization factor. Riemann sums give local convergence on compact sets. The next section proves that the density has total mass one; truncation to high-mass compact sets and then enlargement gives full finite-dimensional weak convergence, without discarding mass near zero or infinity.

## 6. Agreement with the three-dimensional bridge norm and Chapter 37

<a id="vervaat53-normalization"></a>

\[ e(t)=\sqrt{b_1(t)^2+b_2(t)^2+b_3(t)^2},\qquad b_1,b_2,b_3\ \text{independent standard Brownian bridges}. \]

This is the normalized duration-one excursion version of Chapter 37. We check the needed finite-dimensional identification again, without relying on other final-review questions in excursion Poisson theory. For three-dimensional Brownian motion started at radius x, integrate the Gaussian density over angles, equivalently integrate its exponential in the polar cosine from minus one to one. Direct integration gives q multiplied by y divided by x. The limit from zero gives

\[ r_t(x,y)=\frac yx q_t(x,y)\quad(x>0),\qquad
r_t(0,y)=\sqrt{\frac2\pi}\,y^2t^{-3/2}e^{-y^2/(2t)}=y k_t(y). \]

The vector bridge contributes an additional Gaussian weight at the last observation: remaining time to power minus three halves times the radial Gaussian exponential. Multiplying the radial kernels telescopes the successive y-over-x factors; the terminal weight then gives exactly the preceding Q density. Because it comes from three actual continuous bridges, that density has total mass one.

\[ (1-t_j)^{-3/2}\exp\!\left(-\frac{y_j^2}{2(1-t_j)}\right)
=\frac{h_{1-t_j}(y_j)}{c_1 y_j},\qquad Vb\overset d=e\quad\text{in }C([0,1]). \]

The Dyck limit and bridge norm have the same finite-dimensional laws. Rational readings identify a law on continuous paths, proving Vervaat’s identity. Interior positivity of the bridge norm also follows. Chapter 37’s lifetime intensity, indexed by symmetric local time, has coefficient one divided by the square root of two pi; conditioning on duration one gives this Q law. That intensity coefficient must not be multiplied into normalized path heights. Brownian increments here have variance equal to elapsed time and excursion duration is one.

Every finite-variance offspring law gives the same standard cut-bridge candidate, hence this normalized excursion. This identifies function laws only, not a real tree or convergence of metric trees. Return to [Chapter 53](../chapters/53-tree-scaling.md#scaling-excursion).
