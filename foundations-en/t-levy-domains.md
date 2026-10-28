# T-LEVY-DOMAINS: Stable Classification, Domains of Attraction and Discrete Ladder Factorization

This completes the real-valued limit theory used in [Chapter 27](../chapters/27-levy-processes.md#levy-stable). Chapter 14 constructed stable families and proved heavy-tail sufficiency. Here we establish exhaustive classification, necessary domain-of-attraction conditions, the infinite-variance Gaussian boundary and the discrete strict/weak ladder Wiener–Hopf product. LK and the array criterion are proved in [T-LEVY-CHARACTERISTICS](t-levy-characteristics.md#t-levy-arrays).

## 1. Scales cannot vary arbitrarily: convergence of types

<a id="t-levy-types"></a>

\[
V_n\Rightarrow V,\quad a_nV_n+b_n\Rightarrow W,\quad a_n>0,\quad
V,W\text{ nonconstant}
\ \Longrightarrow\
a_n\to a>0,\quad b_n\to b,\quad W\overset d=aV+b.
\]

Choose two regions of V separated by a positive distance, each with fixed positive probability. Unbounded scales would prevent both images from fitting in a common tight window for W. Scales are therefore bounded; tightness of V then bounds translations. Scales tending to zero along a subsequence would give a degenerate image, so they are bounded away from zero. Extract parameter limits and apply Slutsky.

The limiting parameters are unique. A nondegenerate probability cannot be invariant under a positive affine map except the identity: a scale below one contracts to a point under iteration; invert a scale above one; a nonzero translation with scale one violates tightness when iterated. Every parameter subsequence has the same limit, proving full convergence.

A useful consequence concerns nondegenerate i.i.d. sums converging after positive scaling and deterministic centering to a nondegenerate limit. Scales must tend to infinity: Chapter 14’s symmetrized budget bounds n times the truncated second moment of the independent difference divided by the scale. A bounded-scale subsequence would force that difference to vanish, making the original variable constant. One extra summand divided by the scale tends to zero in probability; applying the types lemma to consecutive normalizations gives adjacent scale ratio one.

\[
\frac{S_n-c_n}{a_n}\Rightarrow V
\quad\Longrightarrow\quad
a_n\to\infty,\qquad \frac{a_{n+1}}{a_n}\to1,\qquad
\frac{c_{n+1}-c_n}{a_n}\to0.
\]

The scale conclusion does not presume infinitesimality. The first half of Chapter 14’s budget proof uses only tightness of the sums and an independent product: the symmetrized normalized sum has a common lower bound on a fixed frequency interval. Sinc averaging then gives the last estimate.

\[
\begin{gathered}
D=Z-Z',\qquad
|\phi_Z(t/a_n)|^{2n}\ge1/4\quad(|t|\le\delta),\\
n\bigl(1-|\phi_Z(t/a_n)|^2\bigr)\le\log4,\qquad
nE\!\left[1\wedge(D/a_n)^2\right]\le C_\delta.
\end{gathered}
\]

If a subsequence had aₙ≤M, then E[1∧(D/M)²]≤Cδ/n would tend to zero, forcing D to vanish and Z to be constant. Thus scales diverge before one extra summand divided by the scale is shown negligible. Apply convergence of types to consecutive normalizations: the same nondegenerate limit forces scale ratio one and location difference zero. Budget boundedness precedes infinitesimality, so there is no circular argument.

## 2. All possible stable parameters

<a id="t-levy-stable-classification"></a>

Use Chapter 14’s full definition: every positive linear combination of independent copies is a positive scale and translate of the same law. Infinite divisibility of a nondegenerate stable law was proved there. LK supplies the continuous convolution family μ_t by multiplying its parameters by t. Integer stability makes μ_t a scale and translate of μ for rational t; uniqueness of continuous exponents identifies the chosen convolution roots.

Approximate any real t>0 by rational times. The law μ_t is nondegenerate, for otherwise LK uniqueness would make μ degenerate too. The types lemma extends the affine relation uniquely to real times. Multiply times first by s and then by t: uniqueness gives multiplicative scales, and time continuity makes them continuous. As time decreases to zero the law tends to a point mass, forcing its scale to zero. A continuous positive multiplicative function is a positive power.

\[
\mu_t=\mathcal L(a(t)Z+b(t)),\qquad
a(st)=a(s)a(t),\qquad a(t)=t^{1/\alpha},\quad\alpha>0.
\]

LK uniqueness is now more useful than directly solving a characteristic-function equation: Gaussian variance must scale linearly with time and quadratically with space, while the jump measure must be homogeneous.

\[
t\sigma^2=t^{2/\alpha}\sigma^2,\qquad
\nu(rA)=r^{-\alpha}\nu(A)\quad(r>0).
\]

A nonzero Gaussian part forces α=2. Nonzero jump tails on either half-line are constants times x to the power −α; subtract interval tails to obtain densities without assuming densities initially. The Lévy small-jump condition forces 0<α<2, hence no Gaussian part in that case. If both parts vanish only a deterministic shift remains, excluded by assumption.

\[
\begin{gathered}
0<\alpha<2:\quad
\nu(dx)=\bigl(c_+\mathbf1_{\{x>0\}}+c_-\mathbf1_{\{x<0\}}\bigr)|x|^{-1-\alpha}\,dx,
\quad c_\pm\ge0,\quad c_++c_->0,\quad\sigma^2=0,\\
\nu((x,\infty))=\frac{c_+}{\alpha}x^{-\alpha},\qquad
\nu((-\infty,-x))=\frac{c_-}{\alpha}x^{-\alpha}\quad(x>0),\\
\alpha=2:\quad \nu=0,\quad\sigma^2>0.
\end{gathered}
\]

These conditions are sufficient too: Sections 14.14–14.15 constructed these densities and proved stability by rescaling. Deterministic translation preserves stability. This exhausts all nondegenerate real stable laws. The c-parameters retain Chapter 14’s density convention and must not be mistaken for tail constants.

Check the multiplication of times, since convolution itself adds times. Integer stability explicitly supplies the affine qth root, identified by uniqueness of continuous exponents; taking p independent copies gives rational time p/q. After extension to real times, multiply the exponent identity by s and substitute scale a(t), obtaining

\[
\begin{gathered}
Z_1+\cdots+Z_q\overset d=A_qZ+B_q
\quad\Longrightarrow\quad
\mu_{1/q}=\mathcal L\!\left(Z/A_q-B_q/(qA_q)\right),\\
t\Psi(u)=\Psi(a(t)u)+iu b(t),\\
st\Psi(u)=\Psi(a(s)a(t)u)+iu\{a(t)b(s)+s b(t)\}.
\end{gathered}
\]

The last line and the existing affine expression for μ_{st} describe the same nondegenerate law. Uniqueness of types gives a(st)=a(s)a(t). Time continuity and the types lemma make a and b continuous. As μ_t tends to δ₀, two separated positive-mass regions of the original law cannot both fit in arbitrarily small windows if a(t) stays bounded below; hence a(t) tends to zero. For v=log t, log a(e^v) is continuous additive, so equals κv with κ>0. Only then set α=1/κ to obtain the power scale.

## 3. The centering at alpha one cannot be suppressed

<a id="t-levy-stable-centering"></a>

Use unit-ball truncation and let Ψ₀ be the integral exponent with drift zero, with Δ the difference of density constants. Retaining the linear contribution of the moved cutoff gives Chapter 14’s direct integral below, fixing conventions without depending on trigonometric parameterizations.

\[
\begin{gathered}
\Psi_0(ru)=r^\alpha\Psi_0(u)+iuD_\alpha(r),\qquad
D_\alpha(r)=
\begin{cases}
(c_+-c_-)(r^\alpha-r)/(1-\alpha),&\alpha\ne1,\\
-(c_+-c_-)r\log r,&\alpha=1.
\end{cases}
\end{gathered}
\]

Add ibu for arbitrary drift b. For α≠1, choosing b=Δ/(1−α) removes every rescaling discrepancy and yields a strict-stability center. At α=1 with nonzero Δ, drift scales linearly and no fixed translation removes the logarithm. The following shift for n copies is essential. Symmetry makes Δ zero and removes it; the Gaussian case has its usual mean center and square-root scale.

\[
\alpha=1:\qquad Z_1+\cdots+Z_n
\overset d=nZ+n(c_+-c_-)\log n.
\]

Check the centering sign directly on the truncation annulus. In Ψ₀(ru), substitute y=rx. The two linear cutoffs differ only between r and one; integrals are oriented negatively when r>1.

\[
\begin{gathered}
\Psi_0(ru)-r^\alpha\Psi_0(u)
=iu\,r^\alpha\!\int y
\bigl(\mathbf1_{\{|y|\le1\}}-\mathbf1_{\{|y|\le r\}}\bigr)\nu_\alpha(dy),\\
r^\alpha(c_+-c_-)\int_r^1 y^{-\alpha}dy
=D_\alpha(r).
\end{gathered}
\]

For α=1 the annular integral is −log r, giving D₁(r)=−Δr log r. Comparing nΨ(u) with Ψ(nu) moves this term to the other side and gives the positive location term Δn log n for n copies. The sign comes from rearranging the identity, not from changing either jump-density convention.

## 4. Heavy-tail attraction: how the conditions give the limit

<a id="t-levy-stable-domain-sufficient"></a>

Let the absolute tail F of a nonconstant real variable be regularly varying with index −α, 0<α<2, with positive and negative tail proportions tending to p₊,p₋ and summing to one. Choose C>0 and use Chapter 14’s generalized tail quantiles to obtain positive scales with nF(aₙ) tending to C. Monotonicity and regular variation make relative tail jumps vanish, justifying the quantile normalization. The limiting jump-density constants are αCp₊ and αCp₋.

\[
\begin{gathered}
F(x)=P(|Z|>x),\qquad
nF(a_n)\to C,\qquad c_\pm=\alpha C p_\pm,\\
c_n=a_n\left[nE h(Z/a_n)-\gamma\right],\qquad h(x)=\frac{x}{1+x^2},\\
\frac{S_n-c_n}{a_n}\Rightarrow\mathrm{ID}(\gamma,0,\nu_\alpha).
\end{gathered}
\]

The center integrates only a bounded function, so it is defined at α=1 and when the mean does not exist. The proof requires more than invoking a triplet criterion. Tail limits first identify ν off zero. Section 14.13’s dyadic bounds give the small-ball estimate for α<β<2 and the remote-tail estimate for 0<η<α. A fixed bounded region contributes nothing because n/aₙ² tends to zero, another consequence of the same power bounds.

\[
\begin{gathered}
\limsup_n nE[(Z/a_n)^2\mathbf1_{\{|Z|\le\varepsilon a_n\}}]
\le C_\beta\varepsilon^{2-\beta},\\
\limsup_n nP(|Z|>R a_n)\le C_\eta R^{-\eta}.
\end{gathered}
\]

The first estimate follows by bounding the truncated second moment by twice a tail integral and applying the dyadic bound. It excludes Gaussian mass at zero; the second excludes escape to infinity. Thus w times the raw row measure converges weakly to wν. Raw Poissonization still requires its logarithm error to vanish. Choose α/2<q<min(α,1); tail integration gives a finite q-moment and the scale bounds give n/aₙ^{2q} tending to zero.

\[
n|\phi_Z(u/a_n)-1|^2
\le C_{u,q}n a_n^{-2q}(E|Z|^q)^2\to0.
\]

The original row and its raw accompanying compound Poisson law consequently have the same characteristic limit. The selected center makes its continuous-truncation drift exactly γ; the real canonical criterion completes the proof. For another center, convergence of that drift to γ is the precise requirement. At α=1 it cannot be casually replaced by an undefined mean.

Verify Poissonization explicitly. Dyadic regular-variation bounds give F(t)≤Ct^{−η} for every η<α. Choose η between q and α to make the q-moment tail integral finite. Choose β between α and 2q; nF(aₙ) tending to a positive constant and the corresponding power bound give n/aₙ^{2q}→0. At fixed u the single characteristic function tends to one, allowing one local logarithm branch.

\[
\begin{gathered}
E|Z|^q=q\int_0^\infty t^{q-1}F(t)\,dt<\infty,\qquad
\alpha/2<q<\min(\alpha,1),\\
|\log(1+z)-z|\le C|z|^2\quad(|z|\le1/2),\\
n\left|\log\phi_Z(u/a_n)-(\phi_Z(u/a_n)-1)\right|\to0 .
\end{gathered}
\]

Deterministic centering multiplies by a modulus-one phase. The accompanying compound Poisson exponent has nonpositive real part, so vanishing logarithmic error implies vanishing characteristic-function error. Small-ball and tail estimates first give weak convergence of finite canonical measures; this error then transfers the limit to the original sums, without circular assumptions.

## 5. Necessity: recover the original tails from the limit

<a id="t-levy-stable-domain-necessary"></a>

Conversely assume normalized i.i.d. sums along the full n-sequence converge to a non-Gaussian α-stable law. Section 1 gives diverging scales with adjacent ratio one. Apply the correctly median- and sine-centered array criterion first; raw Poissonization is not yet justified. Each centering shifts Z/aₙ by a deterministic quantity tending to zero. Since the limiting jump measure has no nonzero atoms, squeezing moving thresholds yields the original-tail limits below.

\[
nP(Z>a_n x)\to\frac{c_+}{\alpha}x^{-\alpha},\qquad
nP(Z<-a_n x)\to\frac{c_-}{\alpha}x^{-\alpha}\quad(x>0).
\]

Why is this not merely a statement on sparse scales? For large y take the first index at which aₙ crosses y. The adjacent scale ratio gives aₙ/y tending to one. Squeeze monotone tails at (1±ε)aₙ and decrease ε to zero, extending the limits to regular variation and tail balance for all real y tending to infinity. The scale sequence itself need not be monotone.

Only now may Section 4’s q-moment and logarithm estimate return to the raw canonical drift, proving necessity of its center condition too. Regularly varying tails, tail balance, proper scaling and bounded-truncation centering form a complete necessary-and-sufficient criterion, not just an example construction.

\[
nE h(Z/a_n)-c_n/a_n\longrightarrow\gamma .
\]

Write the necessary-tail squeeze explicitly. Diverging scales make the first-crossing index exist and diverge. Even for nonmonotone scales, first crossing puts its preceding term below y. Adjacent ratio one prevents a fixed relative gap at the crossing.

\[
\begin{gathered}
n(y)=\min\{n:a_n\ge y\},\qquad
a_{n(y)-1}<y\le a_{n(y)},\qquad a_{n(y)}/y\to1,\\
F((r+\eta)a_{n(y)})\le F(ry)\le F((r-\eta)a_{n(y)})
\quad(0<\eta<r,\ y\text{ sufficiently large}),\\
n(y)F(y)\to C,\qquad
\frac{F(ry)}{F(y)}\to r^{-\alpha},\qquad
C=(c_++c_-)/\alpha .
\end{gathered}
\]

For fixed r and η, first let y increase and apply the already obtained limits at fixed thresholds; then decrease η to zero. This proves the last line. The same squeeze on each signed tail gives proportions c₊/(c₊+c₋) and c₋/(c₊+c₋). Although median/sine shifts vary with n, they tend to zero. At a nonzero threshold x, bracket the moving threshold by x±η; the stable jump measure has no atom there, allowing η to decrease to zero. Centered tails have therefore not been silently substituted for the original tails.

## 6. Three estimates for slowly varying truncated variance

<a id="t-levy-normal-tail"></a>

\[
H(x)=E[U^2\mathbf1_{\{|U|\le x\}}],\qquad F(x)=P(|U|>x).
\]

Suppose H is eventually positive and slowly varying; it may converge to a positive finite constant or grow without bound. Dyadic iteration bounds H by any small positive power. Decompose the tail into dyadic annuli as below. Each fixed annulus contributes a variance increment negligible relative to H, while a small-power bound dominates the series. DCT for the series makes the tail negligible.

\[
\begin{gathered}
\frac{x^2F(x)}{H(x)}
\le\sum_{j\ge0}4^{-j}
\frac{H(2^{j+1}x)-H(2^jx)}{H(x)}
\longrightarrow0,\\
H(x)=o(x^\eta)\quad(\eta>0),\qquad
\frac{x\,E[|U|\mathbf1_{\{|U|>x\}}]}{H(x)}\to0 .
\end{gathered}
\]

The last estimate follows by tail integration: make t²F(t)/H(t) uniformly small for t≥x and dominate with H(xu)/H(x)≤Cu^η for η<1. These bounds also prove finite absolute first moment. Conversely, if x²F(x)/H(x) tends to zero, then for r>1, H(rx)−H(x)≤r²x²F(x)=o(H(x)); invert for r<1. Slow variation and this tail condition are equivalent.

One more estimate comes from expanding cosine. On |U|≤ε/|u| the second-order error is bounded by a constant times ε²u² times the truncated second moment. Outside, use the preceding tail bound. First decrease u to zero and then ε to zero to obtain

\[
1-E\cos(uU)\sim\frac{u^2}{2}H(1/|u|).
\]

## 7. Gaussian attraction: sufficiency and an actual scale choice

<a id="t-levy-normal-sufficient"></a>

Let Z be nonconstant with mean μ and put Y=Z−μ. If V(x)=E[Y²;|Y|≤x] is slowly varying, choose positive scales tending to infinity with nV(aₙ)/aₙ² tending to one. The centered sum then converges to a standard Gaussian, including both positive finite and infinite variance. We verify every triplet condition.

\[
\begin{gathered}
nP(|Y|>\varepsilon a_n)\to0,\qquad
\frac n{a_n^2}V(\varepsilon a_n)\to1\quad(\varepsilon>0),\\
\gamma_n=nE h(Y/a_n)\to0,\qquad
n\,w(x)\mathcal L(Y/a_n)(dx)\Rightarrow\delta_0 .
\end{gathered}
\]

The first two follow from Section 6’s tail bound and slow variation. Drift needs a separate check. Since EY=0, subtract the identity from h. On the small ball the error is at most ε times the truncated second moment; outside it is bounded by |Y|/aₙ and Section 6’s first-tail-moment estimate removes it. Send n to infinity, then ε to zero. The weighted finite-measure mass concentrates entirely at zero with mass one.

Raw Poissonization must again be justified. Mean zero and first-moment integrability give φ_Y(u/aₙ)−1=o(1/aₙ), while n/aₙ² is bounded because V is eventually bounded below by a positive constant. The logarithm-square error tends to zero and the canonical criterion yields the Gaussian limit.

The scale is not an unspecified suitable normalization. Choose x₀ beyond which V is positive and define the continuous strictly increasing function below. Substitution, the dyadic slow-variation bound and DCT give its asymptotic; invert it to obtain the scale. The fixed lower part contributes a finite constant, negligible relative to x²/V(x).

\[
\begin{gathered}
Q(x)=\int_{x_0}^x\frac{2t}{V(t)}\,dt
\sim\frac{x^2}{V(x)},\qquad Q(a_n)=n,\\
\frac{S_n-n\mu}{a_n}\Rightarrow N(0,1).
\end{gathered}
\]

After substitution an integrable dominating function is a constant times u^{1−η}, 0<η<2. For example, the symmetric density |y|⁻³ on |y|≥1 is normalized, has mean zero and infinite variance, and V(x)=2log x. One may take √(n log n). Large jumps disappear at this scale while truncated second-order mass remains one.

## 8. Gaussian necessity cannot presume a mean

<a id="t-levy-normal-necessary"></a>

Suppose some centers and positive scales make the sum converge to a Gaussian of variance σ²>0, without presuming Z integrable. Let D=Z−Z′ for an independent copy. The symmetrized sum has limiting variance 2σ². Zero is a median of D, and its sine center and continuous-truncation drift vanish. Its canonical measure is n times the w-weighted law of D/aₙ and converges weakly to 2σ² mass at zero. For fixed ε test with the bounded function (1+x²) times the indicator of {|x|≤ε}; its boundary has no limiting mass. This yields actual truncated second moments, not merely vague convergence:

\[
\begin{gathered}
H_D(x)=E[D^2\mathbf1_{\{|D|\le x\}}],\qquad
\frac n{a_n^2}H_D(\varepsilon a_n)\to2\sigma^2\quad(\varepsilon>0),\\
\frac{H_D(\varepsilon a_n)}{H_D(a_n)}\to1 .
\end{gathered}
\]

Adjacent scale ratios tend to one by Section 1. Monotonicity and first-crossing indices extend these sequential ratios to all real x, so H_D is slowly varying. Explicitly, the first aₙ≥x has aₙ₋₁<x≤aₙ and aₙ/x tending to one; bracket rx between (r−η)aₙ and (r+η)aₙ, and bracket x likewise. This gives the slow-variation ratio for every r>0. Section 6 gives integrability of |D|. The median tail bound P(|Z−m|>x)≤2P(|D|>x) makes Z integrable too. Only now define μ=EZ and Y=Z−μ.

We must still prove V∼H_D/2. Choose a median m of Z. Integrating the median tail bound and controlling the fixed shift μ−m give

\[
\begin{gathered}
E[1\wedge((Z-m)/x)^2]\le2E[1\wedge(D/x)^2],\\
E\min((Z-m)^2,x^2)
\le2[H_D(x)+x^2P(|D|>x)]=O(H_D(x)),\\
\min((a+b)^2,x^2)\le2\min(a^2,x^2)+2b^2,\\
E\min(Y^2,x^2)=O(H_D(x)),\qquad
P(|Y|>x)\le2P(|D|>x/2)=o(H_D(x)/x^2)
\quad(x>2|\mu-m|).
\end{gathered}
\]

Since H_D is eventually bounded below by a positive constant, fixed-shift constants are absorbed in O(H_D). The tail estimate uses x−|μ−m|≥x/2 and slow variation. These bounds control Taylor remainders and the probability outside the ball; a claim that shifts do not matter would not suffice. Since EY=0 and Y is integrable, φ_Y(u)−1=o(u), and hence

\[
\begin{gathered}
1-|\phi_Y(u)|^2
=2(1-\operatorname{Re}\phi_Y(u))-|\phi_Y(u)-1|^2
\sim\frac{u^2}{2}H_D(1/|u|),\\
1-\operatorname{Re}\phi_Y(u)\sim\frac{u^2}{4}H_D(1/|u|).
\end{gathered}
\]

For 0<ε≤1, the fourth-order cosine remainder gives

\[
\begin{gathered}
\left|E[(1-\cos(uY))\mathbf1_{\{|Y|\le\varepsilon/|u|\}}]
-\frac{u^2}{2}V(\varepsilon/|u|)\right|
\le \frac{\varepsilon^2u^2}{24}V(\varepsilon/|u|)
\le C\varepsilon^2u^2H_D(1/|u|),\\
E[(1-\cos(uY))\mathbf1_{\{|Y|>\varepsilon/|u|\}}]
\le2P(|Y|>\varepsilon/|u|)
=o(u^2H_D(1/|u|))
\quad(\varepsilon>0\text{ fixed}).
\end{gathered}
\]

Fix ε before sending u to zero. Compare these bounds with the preceding real-part asymptotic: the limsup distance of V(ε/|u|)/H_D(1/|u|) from one half is at most Cε². Put |u|=ε/x. For fixed ε, slow variation replaces H_D(x/ε) by H_D(x); only afterwards decrease ε to zero. This proves V(x)∼H_D(x)/2, slow variation of V and nV(aₙ)/aₙ²→σ². The limits have not been interchanged and finite variance was never presumed.

Section 7 gives the same-scale limit N(0,σ²) after centering by nμ. Apply the types lemma once more: the difference of centers must tend to the specified limiting mean ℓ. This establishes the complete centering, scaling and necessary conditions, not just the possibility of an infinite-variance CLT.

\[
\frac{S_n-c_n}{a_n}\Rightarrow N(\ell,\sigma^2)
\quad\Longleftrightarrow\quad
\begin{cases}
E|Z|<\infty,\quad V\text{ slowly varying},\quad a_n\to\infty,\\
nV(a_n)/a_n^2\to\sigma^2,\quad
(n\mu-c_n)/a_n\to\ell .
\end{cases}
\]

## 9. Split a path at its first global maximum

<a id="t-levy-wiener-hopf"></a>

Fix the signs first: R is the signed displacement of the endpoint from its maximum; D is the usual nonnegative drawdown.

\[
M_n=\max_{0\le j\le n}S_j,\qquad
R_n=S_n-M_n\le0,\qquad D_n=M_n-S_n=-R_n\ge0.
\]

Finally address Chapter 18’s discrete ladder responsibility. Let a real random walk start at zero with i.i.d. increments, requiring no moments, symmetry or nonlattice assumption. Take independent geometric N with P(N=n)=(1−z)zⁿ, 0<z<1. Each finite path has a unique first global-maximum index k. Its endpoint is a strict record relative to the past, while every future relative partial sum is nonpositive. This strict-past, weak-future split remains unique in the presence of ties.

\[
\begin{gathered}
A_z(f)=\sum_{k\ge0}z^kE[f(S_k);
S_k>\max_{j<k}S_j],\\
B_z(g)=\sum_{l\ge0}z^lE[g(S_l);
\max_{1\le j\le l}S_j\le0],\\
E[f(M_N)g(R_N)]=(1-z)A_z(f)B_z(g).
\end{gathered}
\]

The events at k=0 and l=0 are true by convention. For fixed k,l the increments before and after are independent, and geometric weights factor as (1−z)zᵏzˡ. Tonelli first for nonnegative functions, then extension to bounded complex functions, proves the identity. With both functions one the normalization is one, so \(M_N\) is independent of the signed displacement \(R_N\) and also of the nonnegative drawdown \(D_N\). This fails at deterministic horizons: a one-step symmetric walk gives (M₁,R₁)=(1,0) or (0,−1), which are dependent.

Strict ascending ladders start at zero and restart on first exceeding the current record; weak descending ladders restart on first falling below or equal to the current low. Independence after discrete stopping restarts these cycles, allowing an infinite first ladder time. A’s strict records are exactly ascending ladder epochs. Reverse the l increments: B’s nonpositive-prefix event becomes a weak terminal low, enumerated by weak descending ladders.

\[
\begin{gathered}
T^+=\inf\{n\ge1:S_n>0\},\quad H^+=S_{T^+},\\
T^-=\inf\{n\ge1:S_n\le0\},\quad H^-=S_{T^-},\\
F_\pm(z,u)=E[z^{T^\pm}e^{iuH^\pm};T^\pm<\infty],\qquad
A_z(e^{iu\cdot})=\frac1{1-F_+(z,u)},\quad
B_z(e^{iu\cdot})=\frac1{1-F_-(z,u)},\\
1-z\phi_Z(u)=(1-F_+(z,u))(1-F_-(z,u)).
\end{gathered}
\]

Reversing the increments preserves their joint law because they are i.i.d. The exact event equivalence is displayed below. Weak descending records include ties; strict ascending records exclude them, matching the first-global-maximum split. Assign height zero when a ladder time is infinite, and integrate its transform only on the finite-time event, adding no probability mass.

\[
\begin{gathered}
\widehat S_j=S_l-S_{l-j}\quad(0\le j\le l),\\
\{\widehat S_l\le\widehat S_j\text{ for }0\le j<l\}
=\{S_k\le0\text{ for }1\le k\le l\},\\
E f(M_N)=A_z(f)/A_z(1),\qquad
E g(R_N)=B_z(g)/B_z(1).
\end{gathered}
\]

The last identities follow by taking g=1 or f=1 in the joint formula and using (1−z)A_z(1)B_z(1)=1; multiplication proves full independence. Both normalizers lie between one and 1/(1−z), so normalization is legitimate. The time-height renewal series may have defective mass.

Every finite ladder time is at least one, so transform moduli are at most z and the renewal series converge absolutely. The geometric-time endpoint transform is (1−z)/(1−zφ); substitute the path split to obtain the final identity. This proves the discrete strict/weak Wiener–Hopf product including ties. With both ladders strict, zero increments give F₊=F₋=0, making the right side one although the left is 1−z. The correct weak descending time is one, with F₋=z, restoring 1−z. We neither set z equal to one without justification nor claim all continuous-time fluctuation theory.
