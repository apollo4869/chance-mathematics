# T-CONDITIONED-BRIDGE: A Functional Limit for Finite-Variance Lattice Bridges

Companion to [Chapter 53](../chapters/53-tree-scaling.md#scaling-bridge). We prove the endpoint-conditioned bridge limit using the uniform lattice local CLT from Chapter 13, finite-second-moment Donsker from Chapter 25, and continuous-path tightness tools from Chapter 24. Endpoint conditioning is not yet the first-passage conditioning of a tree.

## 1. A fixed offspring law, feasible sizes, and path space

<a id="bridge53-assumptions"></a>

\[ E\xi=1,\qquad0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad
X_i=\xi_i-1,\quad S_k=\sum_{i=1}^kX_i,\quad S_0=0,\quad
d=\gcd\{j\ge1:P(\xi=j)>0\}. \]

Offspring are iid finite nonnegative integers with one fixed law, independent of size. The assumptions force positive probability of zero offspring and make the span well defined. Increments lie in minus one plus d times the integers. Sizes tend to infinity only along those for which endpoint minus one has positive probability. Chapter 52 proved equivalence with existence of a size-conditioned tree and feasibility of all sufficiently large sizes congruent to one modulo d.

\[ \mathbb P_n^{\mathrm{br}}=\mathbb P(\,\cdot\mid S_n=-1),\qquad
x_n(t)=\frac{S_{\lfloor nt\rfloor}+(nt-\lfloor nt\rfloor)X_{\lfloor nt\rfloor+1}}{\sigma\sqrt n}\ (t<1),\quad
x_n(1)=-\frac1{\sigma\sqrt n},\quad
b_n(t)=x_n(t)+\frac{t}{\sigma\sqrt n}. \]

Interpolation, finite conditioning, and all readings are measurable. The corrected bridge has zero endpoints and differs uniformly from the uncorrected path by at most the endpoint defect. The theorem is convergence in distribution in continuous functions with the uniform norm to the standard Brownian bridge; it holds for both corrected and uncorrected paths.

## 2. The local CLT supplies more than a denominator

<a id="bridge53-local"></a>

\[ p_l(z)=P(S_l=z),\qquad p_n(-1)\sim\frac{d}{\sigma\sqrt{2\pi n}},\qquad
\sup_{z\in\mathbb Z}p_l(z)\le\frac{C}{\sqrt l}\quad(l\ge1). \]

The first asymptotic is along feasible sizes. The uniform bound follows from Chapter 13 on allowed lattice points, with zero probabilities elsewhere; enlarging the constant covers finitely many small lengths. When the remaining length is proportional to the total and the normalized endpoint lies in a compact set, the local-CLT error is uniform. These estimates control numerators, denominators, and tails, not merely pointwise central-limit probabilities.

## 3. The exact density of an initial segment

<a id="bridge53-density"></a>

\[ \mathcal F_k=\sigma(X_1,\ldots,X_k),\qquad
E_n^{\mathrm{br}}F=
E\!\left[F\,\frac{p_{n-k}(-1-S_k)}{p_n(-1)}\right]\quad(F\text{ bounded and }\mathcal F_k\text{-measurable}). \]

Future increments are independent, so the conditional endpoint probability gives the identity first for prefix cylinders and then by a monotone class. For fixed a less than one and prefix lengths at most an, the preceding estimates bound the density uniformly by a constant depending only on a and the offspring law. Interpolation in a final grid cell uses one further increment; rounding the prefix length upward preserves the bound.

\[ k=\lfloor an\rfloor,\quad z\in-k+d\mathbb Z,\quad |z|\le A\sqrt n:
\quad\frac{p_{n-k}(-1-z)}{p_n(-1)}
-\frac1{\sqrt{1-a}}\exp\!\left(-\frac{(z/(\sigma\sqrt n))^2}{2(1-a)}\right)\longrightarrow0
\quad\text{uniformly in }z. \]

The lattice phase is still present: a realizable prefix leaves an endpoint in the allowed lattice for the remaining steps because the total size is feasible. Numerator and denominator have the same span factor, which cancels. Compact-uniform convergence, the uniform density bound, and unconditional Donsker tightness allow limits of bounded continuous prefix functionals multiplied by this density. First truncate to a compact range, then enlarge it.

## 4. Why two overlapping end segments give tightness of the whole bridge

<a id="bridge53-tightness"></a>

The prefix density bound transfers the modulus control of unconditional Donsker to any fixed initial proportion of the conditioned path. This alone does not control the terminal region. Conditional iid strings are invariant under reversing increment order, so the terminal segment, read backwards relative to its endpoint, obeys the same bridge law; the corrected reversal reads the bridge’s increments backwards.

\[ \widehat b_n(t)=b_n(1)-b_n(1-t)=-b_n(1-t)\ \overset d=b_n(t). \]

Apply the bound on the first two thirds and the last two thirds. Two times less than one third apart lie together in one of those intervals. Their two modulus estimates therefore control the whole interval. A fixed initial value and tight moduli give tightness in continuous functions by the Arzelà–Ascoli criterion of Chapter 24. Neither fourth moments nor exponential offspring moments are required.

## 5. Identifying the limit as a Brownian bridge

<a id="bridge53-identification"></a>

\[ b(t)=B_t-tB_1,\qquad
E[F(b|_{[0,a]})]=E\!\left[F(B|_{[0,a]})\,
\frac{\exp(-B_a^2/(2(1-a)))}{\sqrt{1-a}}\right]\quad(0<a<1). \]

The weight is the Gaussian transition density from the current position to zero in the remaining time, divided by the full-time density from zero to zero. Multiply independent Gaussian increment densities at finitely many prefix times and set the terminal coordinate to zero to obtain the ratio. The resulting covariance is the smaller time minus their product, agreeing with the explicit bridge on the left. Rational evaluations generate the Borel σ-algebra of continuous paths, and a monotone class gives the identity for bounded measurable prefix functionals. This specifies a conditional kernel version rather than dividing by a null event.

The prefix density limit identifies joint laws at all times strictly below one, while the endpoint tends to zero. Tightness and finite-dimensional identification prove weak convergence of the whole bridge. The deterministic closing error vanishes, so corrected and uncorrected paths have the same joint limit.

## 6. The largest step, step interpolation, and boundaries

<a id="bridge53-steps"></a>

\[ P_n^{\mathrm{br}}\!\left(\max_{i\le n}|X_i|>\varepsilon\sqrt n\right)
\le CnP(|X_1|>\varepsilon\sqrt n)\longrightarrow0. \]

The density ratio for one coordinate is uniformly bounded using the remaining n minus one steps. Exchangeability and a union bound give the estimate. Finite second moment makes tail probability times threshold squared vanish, bounded by the second-moment tail. Hence step and linear bridges differ uniformly by a quantity tending to zero in probability; the step bridge also converges in the J₁ topology to the same continuous limit. No most-general T-J1 tightness theorem is needed because a direct uniform comparison with a continuous limit is available.

No pathwise convergence on an arbitrary original probability space is asserted. Sizes always follow a genuinely feasible sequence, and the fixed offspring law must satisfy the stated assumptions. Return to [Chapter 53](../chapters/53-tree-scaling.md#scaling-bridge-tight).
