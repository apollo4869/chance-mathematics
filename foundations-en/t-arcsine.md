# T-ARCSINE: Arcsine Laws for Three Path Times

This completes the three arcsine laws used in [Chapter 26](../chapters/26-brownian-properties.md#brownian-arcsine). T>0 is always a fixed deterministic time. We use the chapter’s reflection principle, deterministic-time independent increments, Chapter 25’s Donsker theorem and first-return decompositions of simple random walk. Neither local time, Itô calculus nor a strong Markov assertion at a last-exit time is used.

## 1. Three measurable time functionals

<a id="t-arcsine-functionals"></a>

\[
\begin{gathered}
A_T=\int_0^T\mathbf1_{\{B_s>0\}}\,ds,\qquad
G_T=\max\{s\le T:B_s=0\},\\
\rho_T=\min\{s\le T:B_s=M_T\},\qquad
M_T=\max_{0\le s\le T}B_s.
\end{gathered}
\]

For a continuous path starting at zero, its zero set and maximizing set are nonempty and compact. Thus G and the earliest maximizer ρ are defined without assuming uniqueness. The event {G≥s} asks whether the infimum of the absolute path on [s,T] is zero; {ρ≤s} asks whether the maxima on [0,s] and [0,T] agree. These are closed path events, proving Borel measurability. Joint continuity of path evaluation and nonnegative integration give measurability of A.

The Brownian zero set has Lebesgue length zero almost surely: Tonelli makes its expected length ∫₀ᵀP(\(B_s\)=0)ds=0; the single time s=0 does not matter. Consequently, if continuous xₙ converge uniformly to x and the zero set of x has length zero, their positivity indicators converge for almost every s, and DCT makes occupation time continuous. This is exactly the continuity needed when passing from random walk to Brownian motion.

## 2. Last zero: cutting at a deterministic time

<a id="t-arcsine-last-zero"></a>

Fix 0<s<T. Given \(B_s\)=x, the future is independent Brownian motion started at x. For x≠0, reflection gives probability 2Φ(|x|/√(T−s))−1 of avoiding zero for T−s time units. Since P(\(B_s\)=0)=0, the boundary does not affect the formula below. We cut at s, not at \(G_T\).

\[
\begin{aligned}
P(G_T\le s)
&=E\!\left[2\Phi\!\left(\frac{|B_s|}{\sqrt{T-s}}\right)-1\right]\\
&=P\!\left(\sqrt{T-s}|Z_2|\le\sqrt{s}|Z_1|\right)
=\frac2\pi\arctan\sqrt{\frac{s}{T-s}}
=\frac2\pi\arcsin\sqrt{\frac{s}{T}},
\end{aligned}
\]

Here Z₁,Z₂ are independent standard normals. Polar coordinates in their joint Gaussian density make the angle uniform. In the first quadrant the permitted angular width is arctan√(s/(T−s)); quadrant symmetry gives the formula. Its limits as s decreases to zero and increases to T are zero and one, so there are no endpoint atoms.

This also shows that \(G_T\) is not a stopping time. For 0<s<T, P(\(G_T\)≤s|\(\mathcal F_s\))=2Φ(|\(B_s\)|/√(T−s))−1 is almost surely strictly between zero and one. Were {\(G_T\)≤s} in \(\mathcal F_s\), its conditional probability would be zero or one. To recognize a last visit one needs the as-yet-unseen future.

## 3. When the maximum is attained

<a id="t-arcsine-argmax"></a>

First prove uniqueness for this fixed T. Between two different maximizers one could insert a rational r∈(0,T). The past maximum M_r would then equal \(B_r\) plus the maximum future increment. That increment is independent of \(\mathcal F_r\) and has a continuous half-normal distribution, so equality to the \(\mathcal F_r\)-measurable difference has probability zero. A countable union over rational r completes the proof. No simultaneous uniqueness for all random T is asserted.

The global maximum is attained by s exactly when the future maximum increment does not exceed \(D_s\)=M_s−\(B_s\). Reverse the increments on [0,s]: u↦\(B_s\)−B_{s−u} is still Brownian, being continuous centered Gaussian with covariance min(u,v). Symmetry therefore identifies \(D_s\) in law with M_s, hence with √s|Z₁|. The future maximum increment is independent of \(D_s\), with law √(T−s)|Z₂|.

\[
P(\rho_T\le s)
=P\!\left(\sqrt{T-s}|Z_2|\le\sqrt{s}|Z_1|\right)
=\frac2\pi\arcsin\sqrt{\frac{s}{T}}.
\]

The same angular calculation reappears, not because \(\rho_T\) equals \(G_T\), but because two different path questions reduce to comparing independent half-normal quantities. Nor may one apply strong Markov at \(\rho_T\) without justification: the proof splits only at deterministic s.

## 4. Counting positive time on the lattice

<a id="t-arcsine-excursions"></a>

Let R_k be the symmetric ±1 walk from zero. For 2m steps put H₂ₘ=Σᵢ₌₁²ᵐ1_{Rᵢ₋₁+Rᵢ>0}, the number of edges on the positive half-line. A unit step cannot cross directly from a negative integer to a positive one, and zero endpoints have no time length. Thus the positive occupation fraction of the polygon is exactly H₂ₘ/(2m). Counting edges avoids arbitrary conventions for visits to zero.

\[
\begin{gathered}
u_{2j}=P(R_{2j}=0)=\frac{\binom{2j}{j}}{4^j},\qquad
U(z)=\sum_{j\ge0}u_{2j}z^j=(1-z)^{-1/2},\\
\tau=\inf\{k\ge1:R_k=0\},\qquad
F(z)=\sum_{j\ge1}P(\tau=2j)z^j.
\end{gathered}
\]

The binomial series gives U; alternatively its coefficient recursion solves (1−z)U′=U/2, U(0)=1. Decompose at the first return: the independent continuation starts anew at zero, giving U=1+FU. Hence F=1−√(1−z). For q_j=P(τ>2j), the tail generating function is Q(z)=Σq_jz^j=(1−F(z))/(1−z)=U(z). It includes the unfinished segment of length zero.

Every even-length path decomposes uniquely into completed excursions away from zero followed by an unfinished one. Each excursion keeps its sign until return, with equally likely signs conditional on length. Let z count pairs of steps and w count half the positive-edge count. A completed excursion contributes [F(zw)+F(z)]/2, and the terminal segment contributes [Q(zw)+Q(z)]/2. The zero-length terminal segment contributes two halves, totaling one. Summing over the number of completed excursions gives

\[
\begin{aligned}
\sum_{m,k\ge0}P(H_{2m}=2k)z^m w^k
&=\frac{Q(zw)+Q(z)}{2-F(zw)-F(z)}\\
&=\frac1{\sqrt{1-zw}\sqrt{1-z}}=U(zw)U(z),\\
P(H_{2m}=2k)&=u_{2k}u_{2m-2k},\qquad0\le k\le m.
\end{aligned}
\]

For 0≤z,w<1, the geometric series and Tonelli justify the operations, and nonnegative power series have unique coefficients. This is an exact probability formula, not a guess matching a few moments. H₂ₘ is even because completed excursions and the even-length terminal segment each contain an even number of edges.

## 5. Mass near the endpoints must not be discarded

<a id="t-arcsine-occupation"></a>

Chapter 13’s span-two local CLT gives u₂ⱼ∼1/√(πj), and this asymptotic plus finitely many initial terms gives u₂ⱼ≤C/√(j+1). On εm≤k≤(1−ε)m, the exact probabilities thus form Riemann sums for the arcsine density. The singular endpoints still require control; they cannot be silently omitted from the integral. For 0<ε≤1/2,

\[
\begin{gathered}
P(H_{2m}\le2\varepsilon m)
\le\frac C{\sqrt m}\sum_{k=0}^{\lfloor\varepsilon m\rfloor}
\frac1{\sqrt{k+1}}
\le C'\sqrt\varepsilon+\frac{C'}{\sqrt m},\\
\frac{H_{2m}}{2m}\ \Rightarrow\
\frac{\mathbf1_{(0,1)}(x)}{\pi\sqrt{x(1-x)}}\,dx.
\end{gathered}
\]

The other endpoint is identical. First keep ε fixed for the interior Riemann sum, then decrease ε to zero, proving convergence against every bounded continuous test function. Chapter 25’s Donsker theorem sends the scaled walk polygon to Brownian motion in C([0,1]); Section 1 proves continuity of occupation time at almost every Brownian path. The continuous mapping theorem identifies the same limit with A₁. Brownian time scaling makes \(A_T\)/T equal in law to A₁.

## 6. Equal laws do not mean equal times

<a id="t-arcsine-conclusion"></a>

\[
\begin{gathered}
\frac{A_T}{T}\ \overset d=\ \frac{G_T}{T}\ \overset d=\ \frac{\rho_T}{T},\qquad
P(U\le x)=\frac2\pi\arcsin\sqrt x,\quad0\le x\le1,\\
EU=\frac12,\qquad \operatorname{Var}(U)=\frac18,\qquad
P\!\left(U\notin[1/4,3/4]\right)=\frac23.
\end{gathered}
\]

Substitute x=sin²θ to compute the moments. These times describe occupation, last return and maximum location; they are not equal on a path, nor have they been shown independent. In particular, the law of \(A_T\)/T does not concentrate at one half as T grows, so it does not converge in probability to one half. Brownian symmetry balances the mean without turning a path’s occupation into independent coin frequencies.
