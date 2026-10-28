# T-SCHILDER: Finite Grids, Squared Energy and Full Path Large Deviations

Fix T>0, an integer d≥1 and standard d-dimensional Brownian motion B. The space of continuous paths starting at zero carries the uniform norm; it is separable and complete, with the measurable and compactness structures of Chapters 23–24. Put Xε=√ε B, at speed 1/ε. The proof is direct and uses no Girsanov, Dawson–Gärtner, stochastic integration or unproved RKHS representation.

## W.1 The Full LDP for a Finite Gaussian Vector

<a id="t-schilder-grid"></a>

Divide [0,T] into m intervals, Δ=T/m, and let zⱼ be the jth increment of Xε. Its density on Rᵈᵐ is given below, with positive-definite quadratic Qₘ. For fixed m the logarithm of the prefactor multiplied by ε tends to zero.

\[
p_\varepsilon(z)=(2\pi\varepsilon\Delta)^{-dm/2}e^{-Q_m(z)/\varepsilon},\qquad Q_m(z)=\frac1{2\Delta}\sum_{j=1}^m|z_j|^2.
\]

For z in open O choose a small closed ball inside O. Its positive volume times the minimum density gives the lower rate minus the ball’s maximal Qₘ. Shrink the ball and optimize over z. For compact K, integrate using a finite-volume containing ball and exp(−inf_K Qₘ/ε) to get the compact upper bound.

Arbitrary closed sets also need tail control. Multiplying the one-dimensional Gaussian integrals gives the following squared-norm exponential moment, hence exponential tightness. Compact upper bounds plus this tail estimate give every closed upper bound. The sublevels of Qₘ are compact, so the rate is good.

\[
E\exp\left\{\frac{|z|^2}{4\Delta\varepsilon}\right\}=2^{dm/2},\qquad P(|z|>R)\le2^{dm/2}e^{-R^2/(4\Delta\varepsilon)}.
\]

Cumulating increments and interpolating is a continuous injective finite-dimensional map Γₘ. Its image Vₘ consists of grid polygons, characterized by Πₘh=h, hence is closed. The contraction principle proved in the chapter gives a full LDP for ΠₘXε, with rate Eₘ on Vₘ and infinity outside. The grid reading Eₘ on arbitrary paths must not be mistaken for the polygon law’s rate on the whole space.

\[
E_m(h)=\frac12\sum_{j=1}^m\frac{|h(j\Delta)-h((j-1)\Delta)|^2}{\Delta}.
\]

## W.2 Dyadic Grids Identify All Finite-Energy Paths

<a id="t-schilder-energy"></a>

At level k take mₖ=2ᵏ and let vₖ be the polygon’s velocity. Refinement preserves each coarse cell’s velocity integral, so the L² inner product of fine and coarse velocities equals the squared coarse norm. This gives the identity below and monotonicity of grid energy.

\[
\langle v_\ell,v_k\rangle_2=\|v_k\|_2^2,\quad\|v_\ell-v_k\|_2^2=\|v_\ell\|_2^2-\|v_k\|_2^2\quad(\ell\ge k),\qquad\|v_k\|_2^2=2E_{2^k}(h).
\]

If the energy supremum is finite, the increasing bounded squared norms converge and vₖ is Cauchy in L². T-LP completeness gives g. Integration is continuous from L² to uniform paths; the next bound identifies its limit with h, whose polygons converge uniformly by continuity.

\[
\sup_{t\le T}\left|\int_0^t(v_k-g)(s)\,ds\right|\le\sqrt T\|v_k-g\|_2\longrightarrow0,\qquad h(t)=\int_0^tg(s)\,ds.
\]

Conversely, if h has L² integral velocity g, the vₖ are cell averages, bounded in squared norm by Jensen. The same Cauchy argument gives a limit w with integral h. In each coordinate (w−g)dt is a finite signed measure vanishing on every interval. T-MCLASS uniqueness gives w=g almost everywhere. The energy supremum is exactly half the squared L² norm of g.

\[
I_T(h):=\sup_{k\ge0}E_{2^k}(h)=\begin{cases}\tfrac12\int_0^T|g(s)|^2\,ds,&h(t)=\int_0^t g(s)\,ds,\ g\in L^2,\\\infty,&\text{otherwise}.\end{cases}
\]

L² velocity is defined here by its integral representation, uniquely determined by interval integrals; no differentiation of every path is assumed. Absolute continuity of the Lebesgue integral, proved in T-INTEGRAL, makes such h absolutely continuous: sums of displacements on disjoint small intervals are bounded by the integral of |g| over their union. A continuous non-absolutely-continuous path cannot have this representation and has infinite energy.

I is the supremum of continuous grid energies, hence lower-semicontinuous. I≤L supplies uniform bounds and a square-root modulus. Arzelà–Ascoli gives relative compactness and closedness makes the sublevel compact. Energy is a good rate without an unproved Hilbert weak-compactness or RKHS theorem.

\[
\|h\|_\infty\le\sqrt{2LT},\qquad |h(t)-h(s)|\le\sqrt{2L|t-s|}\quad(I_T(h)\le L).
\]

## W.3 Reflection Bounds Give Exponentially Good Approximation

<a id="t-schilder-approximation"></a>

Within one cell, subtract the linear fraction of the endpoint increment from the increment relative to the left endpoint. The chord error is at most twice the cell’s maximal increment. If its Euclidean norm exceeds δ, some coordinate exceeds δ/√d. Reflection and Gaussian Chernoff bound a coordinate’s absolute maximum over Δ by 4 exp(−u²/(2Δ)). Union over m cells and d coordinates and scale by √ε to obtain the bound.

\[
P\{\|X^\varepsilon-\Pi_mX^\varepsilon\|_\infty>\delta\}\le4dm\exp\left\{-\frac{\delta^2m}{8dT\varepsilon}\right\},\qquad\lim_{k\to\infty}\limsup_{\varepsilon\downarrow0}\varepsilon\log P\{\|X^\varepsilon-\Pi_{2^k}X^\varepsilon\|_\infty>\delta\}=-\infty.
\]

For each fixed grid the prefactor disappears after multiplying the logarithm by ε; then refinement sends the cost to infinity. This does not discard infinitely many prefactors in a union bound. The next section handles that step explicitly.

## W.4 An Explicit Exponentially Tight Path Set

<a id="t-schilder-exponential-tightness"></a>

For L>0 put δⱼ=2⁻ʲ. Choose increasing dyadic mⱼ satisfying the next inequality; its linear term eventually exceeds its logarithm, so the choice exists. Also choose M with M²/(2dT)−log(4d)≥L+2.

\[
\frac{\delta_j^2m_j}{8dT}-\log(4dm_j)\ge L+j+2,\qquad K_L=\{h:\|h\|_\infty\le M,\ \|h-\Pi_{m_j}h\|_\infty\le\delta_j\ \forall j\ge1\}.
\]

Kᴸ is closed. For any η>0 choose δⱼ<η/3. The grid values of every Πₘⱼh are bounded by M, giving a compact finite-dimensional polygonal set. A finite η/3-net there plus the δⱼ error gives a finite η-net for Kᴸ. Thus it is totally bounded and compact by completeness.

For 0<ε≤1 absorb each log-prefactor into the 1/ε exponent. The preceding bound makes failure of approximation constraint j at most exp(−(L+j+2)/ε). Coordinate reflection also makes failure of the norm bound at most exp(−(L+2)/ε). Summing gives the following uniform bound and actual exponential tightness.

\[
P(X^\varepsilon\notin K_L)\le e^{-(L+2)/\varepsilon}\left(1+\frac1{e^{1/\varepsilon}-1}\right),\qquad\limsup_{\varepsilon\downarrow0}\varepsilon\log P(X^\varepsilon\notin K_L)\le-(L+2).
\]

## W.5 The Complete Path Upper and Lower Bounds

<a id="t-schilder-full"></a>

For compact K, membership of Xε implies Π₂ᵏXε∈Π₂ᵏK. The latter is compact, so W.1 bounds the upper rate by −inf_K E₂ᵏ. The increasing continuous grid energies on compact K satisfy the identity below: if r<inf_K I, the decreasing closed sets K∩{E₂ᵏ≤r} have empty intersection. Compactness makes some level already empty. Vary r to prove the identity.

\[
\sup_k\inf_{h\in K}E_{2^k}(h)=\inf_{h\in K}\sup_kE_{2^k}(h)=\inf_K I_T.
\]

The compact upper bound follows. Split a closed F using Kᴸ from W.4 and the finite-sum rule to get at most max{−inf_F I,−L−2}. Let L increase for the full closed upper bound.

For open G and finite-energy h∈G choose a uniform r-ball inside G. Take a sufficiently large dyadic m so that ‖Πₘh−h‖<r/3 and bₘ=(r/3)²m/(8dT)>I(h)+1. If the polygon is within r/3 of Πₘh and its path error is at most r/3, the original path is in G, yielding the inequality below.

\[
P(X^\varepsilon\in G)\ge P(\|\Pi_mX^\varepsilon-\Pi_mh\|_\infty<r/3)-P(\|X^\varepsilon-\Pi_mX^\varepsilon\|_\infty>r/3).
\]

The first term has finite-dimensional lower rate at least −Eₘ(h)≥−I(h). W.3 gives the second upper rate at most −bₘ, strictly smaller. T-LDP’s subtraction lemma retains a lower rate of at least −I(h). Optimize over h for the open lower bound. If no finite-energy point exists, that bound is minus infinity and needs no further argument. Goodness was established in W.2, completing Schilder’s theorem.

In the final limit ε decreases while m has been chosen sufficiently large but fixed. No fixed-m error is called automatically superexponential, and finite-dimensional laws alone are never declared a path LDP. The theorem covers fixed finite T, standard d-dimensional Brownian motion and the uniform path topology.
