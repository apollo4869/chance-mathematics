# The Mathematics of Chance

Volume II · Probability in an Infinite World

# Chapter 14: Not Every Limit Is Gaussian—Triangular Arrays, Stable Laws and Infinite Divisibility

A loss ledger can grow in two very different ways. More and more entries may each be small, leaving a deviation resembling continuous noise. Or most cells may remain empty while an occasional entry changes the total for the whole page. Knowing only that many terms have been added does not distinguish these possibilities.

The experiment itself may also change. The number of insurance contracts, their individual risks and their loss ceilings need not grow in the same proportion. Treating every entry as a copy of one fixed random variable excludes these changes before calculation starts.

Small fluctuations form a bell-shaped law only if exceptional terms do not quietly take over its scale. When the tail refuses to yield, we should seek a different scale rather than insist on a square root.

## 14.1 One row need not copy another

Write experiment \(n\) as a finite row of length \(r_n\):

\[
Z_{n1},\ldots,Z_{nr_n},\qquad S_n=\sum_{k=1}^{r_n}Z_{nk}.
\]

Independence within each row is fundamental below. Different rows may live on different probability spaces or be dependent on one another. Distributional limits of their sums require no coupling of experiments into sample paths. The name triangular array emphasizes increasing scale; a row need not contain exactly n terms.

For finite-variance problems put \(m_{nk}=\mathbb EZ_{nk}\) and use the standard deviation of the whole row:

\[
s_n^2=\sum_k\operatorname{Var}(Z_{nk})\in(0,\infty),\qquad X_{nk}=\frac{Z_{nk}-m_{nk}}{s_n},\qquad T_n=\sum_kX_{nk}.
\]

Then \(\mathbb EX_{nk}=0\) and \(\sum_kv_{nk}=1\), where \(v_{nk}=\mathbb EX_{nk}^2\). Normalization fixes the total budget without identifying who carries it. Zero-variance terms are allowed; a row of total variance zero is deterministic and cannot be standardized this way.

For heavy-tailed laws, means and variances may not exist. We shall retain independent rows but specify a different spatial scale and a deterministic centering. The present variance convention must not be imposed on stable limits later.

## 14.2 Small probabilities and small variances differ

On the chosen scale, **infinitesimality** means that for every fixed threshold,

\[
\max_{k\le r_n}P(|X_{nk}|>\varepsilon)\longrightarrow0\qquad(\varepsilon>0).
\]

A finite-variance array has a different condition, the **Feller maximal-variance condition**:

\[
\max_kv_{nk}\longrightarrow0.
\]

Chebyshev shows that Feller implies infinitesimality: \(P(|X_{nk}|>\varepsilon)\le v_{nk}/\varepsilon^2\). The converse fails. Let one term in each row take \(\pm\sqrt n\), each with probability \(1/(2n)\), and otherwise be0; all other terms vanish. The array is infinitesimal, centered and has total variance1, but maximal variance stays1 and the sum tends to0 in probability. Second-moment mass escaping far away disappears from the weak limit.

Feller alone does not produce a Gaussian law either. Take n independent terms per row, each taking±1 with probability \(1/(2n)\) apiece and0 otherwise. Individual variance is \(1/n\), total variance1, but

\[
\mathbb Ee^{itT_n}=\left(1+\frac{\cos t-1}{n}\right)^n\longrightarrow\exp(\cos t-1).
\]

This is a compound Poisson law of intensity1 with symmetric±1 marks, already constructed in Chapter 13. Almost every cell is empty, yet the row retains a finite number of unit jumps. Preventing one entry from dominating variance does not exclude this mechanism.

## 14.3 What must disappear is the second-moment contribution of large terms

To leave continuous small fluctuations, we must budget the variance carried by large terms, not merely count how often they occur. For centered arrays of total variance1 define

\[
L_n(\varepsilon)=\sum_k\mathbb E[X_{nk}^2\mathbf1_{\{|X_{nk}|>\varepsilon\}}].
\]

The **Lindeberg condition** is \(L_n(\varepsilon)\to0\) for every \(\varepsilon>0\). The threshold is measured in units of the row standard deviation, not a fixed amount in the original ledger. Before standardization it reads

\[
\frac1{s_n^2}\sum_k\mathbb E[(Z_{nk}-m_{nk})^2\mathbf1_{\{|Z_{nk}-m_{nk}|>\varepsilon s_n\}}]\longrightarrow0.
\]

It implies Feller automatically, since \(v_{nk}\le\varepsilon^2+L_n(\varepsilon)\). Take the upper limit in n and then let ε decrease to0. It also gives \(P(\max_k|X_{nk}|>\varepsilon)\le L_n(\varepsilon)/\varepsilon^2\to0\): the chance of any visible large term in the entire row vanishes. This is stronger than infinitesimality of individual terms.

Lindeberg’s 1922 paper appeared in Mathematische Zeitschrift 15, pages 211–225; see the [original publication record](https://link.springer.com/article/10.1007/BF01494395). We reconstruct the proof with characteristic functions established in this book. The normalization is modern and is not presented as a transcription of the original.

## 14.4 Why small terms leave the same quadratic shape

**Lindeberg central limit theorem.** Suppose each row is independent, \(\mathbb EX_{nk}=0\), and \(\sum_k\mathbb EX_{nk}^2=1\). Under the Lindeberg condition, \(T_n\Rightarrow N(0,1)\). Independence between rows and third moments are not required.

The proof protects a simple mechanism: centering removes the linear term, variance retains the quadratic term, and all remainders together must vanish. A separate uncontrolled little-o for each term cannot simply be summed across a growing row.

\[
e^{iu}=1+iu-\frac{u^2}{2}+R(u),\qquad |R(u)|\le\frac{|u|^3}{6},\qquad |R(u)|\le u^2.
\]

The first bound follows from the integral Taylor remainder; the second follows from \(|e^{iu}-1-iu|\le u^2/2\) after adding the quadratic term. For fixed t, split at \(|X_{nk}|\le\varepsilon\) to obtain

\[
\sum_k|\mathbb ER(tX_{nk})|\le\frac{|t|^3\varepsilon}{6}\sum_kv_{nk}+t^2L_n(\varepsilon).
\]

Let n tend to infinity and then ε to0; the bound vanishes. With \(z_{nk}=\mathbb Ee^{itX_{nk}}-1\),

\[
\sum_kz_{nk}\longrightarrow-\frac{t^2}{2},\qquad |z_{nk}|\le\frac{t^2v_{nk}}2,\qquad \sum_k|z_{nk}|^2\le\frac{t^4}{4}\max_kv_{nk}\longrightarrow0.
\]

For large n all \(|z_{nk}|\le1/2\). On the logarithm branch near1, its power series gives \(|\log(1+z)-z|\le2|z|^2\). Hence

\[
\prod_k\mathbb Ee^{itX_{nk}}=\exp\left\{\sum_k\log(1+z_{nk})\right\}\longrightarrow e^{-t^2/2}.
\]

Within-row independence identifies the product as the sum’s characteristic function. The real-line Lévy continuity theorem of Chapter 11 finishes the proof. Universality now has a precise meaning: individual laws may differ, but once large terms cease to carry the second-moment budget, the row remembers only a quadratic shape.

## 14.5 What a Gaussian limit tells us in return

Necessity must include its hypotheses. Under centering and total variance1, **if Feller holds, then \(T_n\Rightarrow N(0,1)\) if and only if Lindeberg holds**. Without Feller, let one term already be standard Gaussian and all others vanish. The sum is always Gaussian, but Lindeberg fails.

We prove the conditional converse. Feller and the preceding bound on z still make the sum of logarithmic errors vanish. If the sum tends to a standard Gaussian, the modulus of its characteristic function tends to the strictly positive Gaussian reading, so

\[
\sum_k\mathbb E[1-\cos(tX_{nk})]=-\log|\mathbb Ee^{itT_n}|+o(1)\longrightarrow\frac{t^2}{2}.
\]

Fix any nonzero t. Total variance1 also gives

\[
\sum_k\mathbb E\left[\frac{t^2X_{nk}^2}{2}-(1-\cos(tX_{nk}))\right]\longrightarrow0.
\]

The bracket is nonnegative. For every ε>0 it is at least \(c_{t,\varepsilon}x^2\) on \(|x|>\varepsilon\), for some \(c_{t,\varepsilon}>0\). Indeed, \(1/2-(1-\cos u)/u^2\) is strictly positive for nonzero u and tends to1/2 at infinity, so it has a positive lower bound on \(|u|\ge|t|\varepsilon\). Strictness follows from \(1-\cos u<u^2/2\) for nonzero u.

Thus the second-moment contribution above every fixed threshold vanishes. Sufficiency removes large terms and retains the quadratic part; necessity says that the Gaussian has already used the full variance budget, leaving none for visible large terms elsewhere. Feller excludes an entire pre-existing Gaussian block; it does not itself eliminate jumps.

## 14.6 Stronger moment assumptions are convenient routes, not the boundary

If for some \(\delta>0\) the **Lyapunov condition** holds,

\[
\sum_k\mathbb E|X_{nk}|^{2+\delta}\longrightarrow0,
\]

then \(L_n(\varepsilon)\le\varepsilon^{-\delta}\sum_k\mathbb E|X_{nk}|^{2+\delta}\to0\). This proves Lyapunov implies the CLT. For unstandardized variables the denominator is \(s_n^{2+\delta}\). Stronger moments simplify verification but are not necessary.

For example, take a symmetric law with density proportional to \(|x|^{-3}(\log|x|)^{-2}\) on \(|x|\ge e\), completing its mass with a symmetric density on a bounded interval. It has positive finite variance but no moment of order \(2+\delta\). Its standardized i.i.d. rows satisfy Lindeberg because the second-moment tail tends to0, yet satisfy none of these Lyapunov conditions.

The finite-variance logic is now closed. For random motion, however, a bell shape at one time is still insufficient. Several positions, errors or loss categories must be recorded together. Normality of separate coordinates does not identify their joint structure.

## 14.7 Marginal photographs do not determine a joint world

Let \(G\sim N(0,1)\) and let \(\epsilon\) be an independent symmetric sign. The vectors \((G,G)\), \((G,\epsilon G)\), and two independent standard Gaussians have identical one-dimensional marginals. The first lives on one diagonal, the second on two diagonals, while the third has a two-dimensional density.

For \(X\in\mathbb R^d\), read in every direction instead:

\[
\phi_X(t)=\mathbb Ee^{i\langle t,X\rangle},\qquad t\in\mathbb R^d.
\]

Boundedness, continuity and multiplication under independent vector addition follow directly from DCT or independence, just as on the line. Multivariate uniqueness cannot follow merely by applying the one-dimensional theorem coordinate by coordinate; the example shows what that would lose.

## 14.8 One Gaussian smoothing reveals the whole joint law

Let G be an independent standard d-dimensional Gaussian and \(\varepsilon>0\). Multiplying the one-dimensional Gaussian Fourier formulas coordinatewise shows that \(X+\varepsilon G\) has density

\[
p_\varepsilon(x)=(2\pi)^{-d}\int_{\mathbb R^d}e^{-i\langle t,x\rangle}\phi_X(t)e^{-\varepsilon^2\|t\|^2/2}\,dt.
\]

This is not an unjustified inversion for arbitrary densities. First express the Gaussian kernel by its absolutely integrable Fourier integral and then integrate over X. The integrable Gaussian factor justifies Fubini. Equal characteristic functions therefore give equal smoothed densities for every smoothing scale.

For bounded continuous f, \(f(X+\varepsilon G)\to f(X)\) almost surely on the independent product space, so DCT gives convergence of expectations. Letting ε decrease to0 yields equal integrals of every bounded continuous f. Continuous decreasing ramps approximate indicators of closed lower rectangles; [π–λ uniqueness](../foundations/t-mclass.md#t-mclass-uniqueness) then identifies the Borel probabilities. This proves multivariate uniqueness, including laws supported on lower-dimensional planes.

## 14.9 Building finite-dimensional compactness from small cells

To recover a limit from pointwise readings, probability must not escape. A family on \(\mathbb R^d\) is **uniformly tight** if for every η>0 some compact K leaves less than η probability outside K for every member. In finite dimensions one may take \(K=[-M,M]^d\); coordinate tail bounds and a union bound suffice.

We now prove that a uniformly tight sequence has a weakly convergent subsequence, without borrowing a later compactness theorem for general metric spaces. First work on a compact cube and then compress Euclidean space into it.

Partition \([0,1]^d\) at dyadic coordinate points, using half-open cells with the rightmost endpoint included in the last cell. Levels are compatible and diameters tend to0. Successive subsequence extraction and a diagonal choice make the probability of every cell at every level converge. Limiting masses are nonnegative, sum to1, and each parent mass is the sum of its children.

The finite-state consistent extension proved in Chapter 8 constructs a random nested cell address. Incompatible neighboring levels have probability0, so outside a countable union of null events the address is compatible at every level. Nested closures with vanishing diameter have exactly one common point. Representatives chosen in each cell are finite-valued measurable functions, and their coordinatewise limit is the measurable intersection point. This produces an actual cube probability ν. The point may lie on a cell boundary; that causes no gap.

Approximate continuous f by its representative value in each cell. The original integral differs from the finite weighted sum by at most the uniform oscillation of f at that diameter. The same bound compares the ν integral with the limiting weighted sum, since the intersection point lies in the cell closure. Fix a level, pass to the subsequence limit and then refine the partition. Integrals of every continuous f converge. We need not claim that ν assigns each half-open cell exactly its extracted mass: boundary assignment may change, while limits of continuous observations do not.

For \(\mathbb R^d\), apply \(q(x)=1/2+\arctan(x)/\pi\) coordinatewise, push the laws into the open cube, and extract in the closed cube. Original uniform tightness keeps the limit off the boundary. Given η, choose a common large cube whose image K lies inside the open cube. A continuous function equal to1 on the boundary and0 on K, with values in[0,1], has limiting integral at most η. Boundary mass is at most η and hence0.

Pull back by the inverse map. For bounded continuous f, first compose with the inverse on a common interior compact set, then multiply by a continuous cutoff vanishing near the boundary. The two tail probabilities control the error outside the compact set. Enlarge the set and let the error vanish. This proves weak subsequence existence on Euclidean space using only finite partitions, diagonal selection, Chapter 8 extension and continuous cutoffs.

## 14.10 Assembling directional limits into one law

**Multivariate Lévy continuity.** If \(\phi_n(t)\to\phi(t)\) for every \(t\in\mathbb R^d\), with \(\phi(0)=1\) and φ continuous at0, then a unique Borel probability μ has this characteristic function, and the original probabilities converge weakly to μ.

For the proof, first restrict to coordinate axes. Real-line continuity gives convergence, hence uniform tightness, of each coordinate family; finitely many initial terms are handled by enlarging the window. A union bound gives vector tightness. The preceding section supplies a subsequence limit. Testing bounded continuous exponentials identifies its characteristic function as φ; multivariate uniqueness makes all such limits equal. If one bounded continuous test failed to converge along the full sequence, a subsequence separated from this value would have a further weakly convergent subsequence, a contradiction.

**Cramér–Wold device.** For a specified random vector X, \(X_n\Rightarrow X\) if and only if \(\langle u,X_n\rangle\Rightarrow\langle u,X\rangle\) for every \(u\in\mathbb R^d\). The forward direction uses continuous composition. Conversely, evaluate each projected characteristic function at frequency1 and apply the preceding theorem.

Even without a specified X, if all linear projections of the same vector sequence converge to finite real laws, coordinate tightness first supplies vector subsequence limits. They share every projection and hence the same characteristic function, so the full sequence converges. Arbitrarily assigned incompatible projection laws are not thereby permitted; compatibility here comes from the common vector sequence.

Cramér and Wold published Some Theorems on Distribution Functions in 1936, in Journal of the London Mathematical Society 11, pages 290–294; see the [publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s1-11.4.290). Our Gaussian smoothing and finite-cell extraction prove the modern version needed here, without claiming to reproduce the original argument.

## 14.11 How joint fluctuations become a Gaussian vector

For a symmetric positive semidefinite matrix Σ, take a matrix square root A with \(AA^\mathsf T=\Sigma\), as supplied by finite-dimensional linear algebra. If G has independent standard Gaussian coordinates, define \(N_d(0,\Sigma)\) as the law of AG. Its characteristic function is

\[
\mathbb Ee^{i\langle t,AG\rangle}=e^{-\|A^\mathsf Tt\|^2/2}=e^{-t^\mathsf T\Sigma t/2}.
\]

Σ may be singular. The law does not depend on the square root chosen, by transform uniqueness. Projections in zero-variance directions are identically0; they must not be excluded merely to permit a density formula.

If \(V_1,V_2,\ldots\) are i.i.d. vectors with \(\mathbb E\|V_1\|^2<\infty\), mean m and covariance Σ, then

\[
\frac1{\sqrt n}\sum_{k=1}^n(V_k-m)\Rightarrow N_d(0,\Sigma).
\]

For each u the projected variance is \(u^\mathsf T\Sigma u\). If positive, apply the real-line CLT from Chapter 11; if zero, the centered projection vanishes almost surely. Cramér–Wold completes the vector proof.

More generally, for independent centered vector rows, suppose

\[
\sum_k\mathbb E[X_{nk}X_{nk}^\mathsf T]\longrightarrow\Sigma,\qquad\sum_k\mathbb E[\|X_{nk}\|^2\mathbf1_{\{\|X_{nk}\|>\varepsilon\}}]\longrightarrow0\quad(\varepsilon>0).
\]

For fixed nonzero u, \(|\langle u,x\rangle|\le\|u\|\|x\|\) bounds the projected Lindeberg tail by a vector tail. If projected total variance tends to a positive value, standardize and apply14.4; if it tends to0, apply Chebyshev. Cramér–Wold gives convergence of row sums to \(N_d(0,\Sigma)\). These explicit hypotheses establish finite-dimensional convergence, not convergence of whole paths.

## 14.12 When large terms persist, seek a new ruler

When a rare loss remains comparable with the entire sum, Lindeberg failure need not be a technical hole awaiting repair. A Gaussian model may have discarded the structure that matters. Cauchy already showed a summation scale n rather than√n. We must now move beyond one example and determine how tails select a scale.

Write \(F(x)=P(|Z|>x)\). If at large scales \(F(x)\) behaves like \(x^{-\alpha}\ell(x)\), the chance that one of n experiments exceeds a is governed by \(nF(a)\). Keeping this budget nonvanishing and finite suggests \(nF(a_n)\to1\). The extremes select the scale instead of a pre-assumed finite variance.

We must define this tail behavior and prove that it also controls the many small terms near zero. Comparing only the order of the maximum does not prove a limit for the sum.

## 14.13 Slow variation need not be constant, but preserves the exponent

A positive function ℓ is **slowly varying** at infinity if \(\ell(cx)/\ell(x)\to1\) for every fixed c>0. We use measurable functions and work mainly through monotone tails. If \(F(cx)/F(x)\to c^{-\alpha}\), F is regularly varying with index−α, and \(\ell(x)=x^\alpha F(x)\) is slowly varying. The functions \((\log x)^\gamma\) give nonconstant examples.

Only two elementary scale bounds are needed below. Fix \(0<\gamma<\alpha<\beta<2\). For sufficiently large x, the ratio limit at scale2 gives

\[
F(2x)\le2^{-\gamma}F(x),\qquad F(x/2)\le2^\beta F(x).
\]

Iterating and using monotonicity between successive dyadic scales yields a fixed C: when a and au exceed a fixed starting point, \(F(au)/F(a)\le Cu^{-\gamma}\) for u≥1 and \(F(au)/F(a)\le Cu^{-\beta}\) for0<u≤1. No unjustified uniform upgrade of pointwise slow variation is being made; dyadic iteration supplies the required control. For0<u≤1, choose m with \(2^{-m-1}<u\le2^{-m}\) and bound F(au) by the tail at the next lower dyadic point. Each step costs at most \(2^\beta\), giving a common C independent of a and u. The u≥1 case uses the same argument with exponent γ.

The eventual lower bound \(F(2x)\ge2^{-\beta}F(x)\) similarly gives \(x^2F(x)\to\infty\). Along dyadic points the multiplier is at least \(2^{2-\beta}>1\); monotonicity handles points between them. Consequently \(n/a_n^2\to0\).

Such a_n exist. For an eventually positive regularly varying tail take the generalized inverse \(a_n=\inf\{x\ge x_0:F(x)\le1/n\}\). Then a_n tends to infinity. Relative jumps of F vanish: for0<η<1, \(F(x-)\le F((1-\eta)x)\), so the upper limit satisfies \(F(x-)/F(x)\le(1-\eta)^{-\alpha}\); let η decrease to0. Squeezing at the quantile gives \(nF(a_n)\to1\). Here F is right-continuous and eventually positive, and a_n eventually exceeds x₀. Its generalized inverse satisfies \(F(a_n)\le1/n\le F(a_n-)\). The ratio of these two tail values tends to1, so the squeeze requires neither continuity nor strict decrease of the tail.

Monotone inverse squeezing also identifies the exponent: for fixed c>0, \(a_{\lfloor cn\rfloor}/a_n\to c^{1/\alpha}\). Choose positive u and v bracketing \(c^{1/\alpha}\). The limits of nF(a_nu) and nF(a_nv) lie on opposite sides of1/c, so the corresponding quantile is trapped between a_nu and a_nv. Thus \(a_n=n^{1/\alpha}\ell_1(n)\), with ℓ₁ slowly varying in the fixed-multiple, integer-rounded sense.

## 14.14 Construct large jumps first, then lower the threshold

A nondegenerate real law is **stable** if independent copies U,V satisfy \(aU+bV\overset d=cZ+d\) for every a,b>0, with deterministic c>0,d and Z of the original law. It is strictly stable when d can always be0. This is invariance of shape under independent summation, not a definition of a time process.

We construct a parameter family extending far beyond Cauchy. Take \(0<\alpha<2\), constants \(c_+,c_-\ge0\) with positive sum, and put

\[
\nu(dx)=\bigl(c_+\mathbf1_{\{x>0\}}+c_-\mathbf1_{\{x<0\}}\bigr)|x|^{-1-\alpha}\,dx,\qquad \Psi(t)=\int_{\mathbb R\setminus\{0\}}(e^{itx}-1-itx\mathbf1_{\{|x|\le1\}})\,\nu(dx).
\]

No general representation theorem is invoked. Near0 the subtraction of the linear term leaves a remainder bounded by a constant times x². At large x the subtraction vanishes and the remainder is bounded. The two ends are integrable because α<2 and α>0 respectively. A common integrable bound on bounded t intervals proves continuity of Ψ and Ψ(0)=0.

First extend compound Poisson construction to an arbitrary real Borel mark law Q. Chapter 8 product spaces supply i.i.d. marks J₁,J₂,… and an independent Poisson variable N of parameter λ. Since N is almost surely finite, the random finite sum is measurable by its countable decomposition according to N. Conditioning on N and using the bound1 in absolute value gives

\[
\mathbb E e^{it\sum_{j=1}^N J_j}=e^{-\lambda}\sum_{m=0}^\infty\frac{\lambda^m}{m!}\phi_Q(t)^m=\exp\{\lambda(\phi_Q(t)-1)\}.
\]

At λ=0 the sum is0. This directly extends the countable-mark calculation of Chapter 13, without requiring a density or moments for Q and without using a general Poisson random measure.

Fix \(0<\eta<1\) and discard \(|x|\le\eta\). The remaining intensity \(\lambda_\eta=\nu(|x|>\eta)\) is finite. Using Chapter 13 independent marking, form a compound Poisson sum of intensity λ_η with mark law \(\nu(\cdot\cap\{|x|>\eta\})/\lambda_\eta\), then subtract \(\int_{\eta<|x|\le1}x\nu(dx)\). Its characteristic function is precisely the truncated exponential \(e^{\Psi_\eta(t)}\).

As η decreases to0, integrable domination gives convergence of exponents to Ψ. Real-line Lévy continuity proves that e^Ψ is a probability characteristic function and that the truncated laws converge weakly. We have constructed a real distribution, not assumed pathwise convergence of a process of small jumps.

For every nonzero t, \(\operatorname{Re}\Psi(t)=-(c_++c_-)I_\alpha|t|^\alpha<0\), with the finite positive constant I_α written out in the next section. The characteristic function has modulus strictly below1, so the constructed law is nondegenerate.

## 14.15 The stable exponent and the shift that matters

Put \(\Delta=c_+-c_-\). Changing variables y=ax in the preceding integral, while retaining the truncation indicator, gives

\[
\Psi(at)=a^\alpha\Psi(t)+itD_\alpha(a),\qquad D_\alpha(a)=\begin{cases}\displaystyle\Delta\frac{a^\alpha-a}{1-\alpha},&\alpha\ne1,\\-\Delta a\log a,&\alpha=1.\end{cases}
\]

The difference comes only from the linear correction between1 and a: \(D_\alpha(a)=-\Delta a^\alpha\int_1^a y^{-\alpha}\,dy\), with oriented integration when a<1. This computes the shift and explains the logarithm at α=1.

Consequently, for U,V with characteristic function e^Ψ and \(c=(a^\alpha+b^\alpha)^{1/\alpha}\),

\[
aU+bV\overset d=cZ+D_\alpha(a)+D_\alpha(b)-D_\alpha(c).
\]

This proves stability rather than inferring it from a name. In the symmetric case Δ=0 the law is strictly stable. When α≠1, shifting Z by Δ/(1−α) also removes all D terms. When α=1 and the law is asymmetric, a fixed location shift generally cannot remove the logarithmic correction. Translation in the stable definition is essential.

The symmetric case is especially transparent. Set \(I_\alpha=\int_0^\infty(1-\cos y)y^{-1-\alpha}\,dy\in(0,\infty)\). Then

\[
\phi_Z(t)=\exp(-C|t|^\alpha),\qquad C=(c_++c_-)I_\alpha>0,\qquad Z_1+\cdots+Z_n\overset d=n^{1/\alpha}Z.
\]

Integrability of this same integral at0 and infinity has already been proved. The case α=1 includes symmetric Cauchy laws; continuously varying α between0 and2 gives a family of non-Gaussian scales. The endpoint α=2 is supplied separately by Gaussian laws with scale√n; it cannot be substituted into the divergent small-jump integral.

Nor can one simply write \(e^{-C|t|^\alpha}\) with α>2. If this were a characteristic function, Fatou applied to \((1-\cos(tZ))/t^2\) would give \(\mathbb EZ^2/2\le\liminf_{t\to0}(1-e^{-C|t|^\alpha})/t^2=0\), forcing degeneracy, a contradiction. Values α≤0 violate continuity at the origin. Probability itself restricts the parameter range.

## 14.16 From tail proportions to an actual sum limit

We prove a **stable domain-of-attraction theorem** with an explicit scope. Let Z be real, let \(F(x)=P(|Z|>x)\) be regularly varying of index \(-\alpha\), where \(0<\alpha<2\), and suppose

\[
\frac{P(Z>x)}{F(x)}\longrightarrow p_+,\qquad\frac{P(Z<-x)}{F(x)}\longrightarrow p_-,\qquad p_++p_-=1.
\]

Choose \(a_n\) from §14.13 with \(nF(a_n)\to1\), and let Z₁,Z₂,… be i.i.d. copies. Then

\[
\frac{Z_1+\cdots+Z_n}{a_n}-B_n\Rightarrow Z_\alpha,\qquad B_n=n\mathbb E\left[\frac Z{a_n}\mathbf1_{\{|Z|\le a_n\}}\right],
\]

Here \(Z_\alpha\) is the law constructed in14.14 with \(c_+=\alpha p_+\) and \(c_-=\alpha p_-\). This centering is valid for every α because the expectation is truncated. It neither assumes a nonexistent mean nor omits the logarithmic centering at α=1.

First record the jump budget away from0, then control the neighborhood of0. Let μ_n be n times the law of Z/a_n. At x>0 its positive and negative tails tend to p₊x^−α and p₋x^−α. Thus μ_n masses of bounded intervals away from0 converge to ν masses, by tail differences; endpoint atoms vanish because limiting tails are continuous. Finite step approximations then give convergence of integrals of continuous compactly supported functions away from0.

Near0 use the dyadic bound from14.13. Choose \(\alpha<\beta<2\). For0<δ<1, the layer-cake formula gives

\[
\limsup_n n\mathbb E\left[\left(\frac Z{a_n}\right)^2\mathbf1_{\{|Z|\le\delta a_n\}}\right]\le C\delta^{2-\beta}.
\]

Indeed, the truncated second moment is at most \(2\int_0^\delta u\,nF(a_nu)\,du\). Above the fixed starting scale the integral is bounded by a constant times \(\int_0^\delta u^{1-\beta}du\). The remaining interval contributes at most a constant times \(n/a_n^2\to0\). At infinity, \(\limsup_n nF(Ra_n)\le CR^{-\gamma}\) for0<γ<α. For \(u<x_0/a_n\), the bound F≤1 gives at most \(nx_0^2/a_n^2\). On the remaining interval use the dyadic bound and boundedness of nF(a_n). First fix δ,R and take the upper limit in n, with constants independent of δ,R; only then let δ decrease to0 and R increase to infinity.

For fixed t put \(g_t(y)=e^{ity}-1-ity\mathbf1_{\{|y|\le1\}}\). It is bounded by a constant times y² near0 and bounded at infinity. Its jumps at±1 cause no problem: ν has no atoms, and masses of small intervals enclosing those points can be made arbitrarily small. Cut off0 and infinity, apply the preceding integral convergence, and then use the endpoint budgets to control the error. Its upper limit is at most \(C_t(\delta^{2-\beta}+\delta^{2-\alpha}+R^{-\gamma}+R^{-\alpha})\): two terms control the neighborhoods of0 for μ_n and ν, and two control their far tails. For fixed δ,R first shrink neighborhoods of±1 to0, using continuity and absence of atoms of the limiting tails. Then let δ decrease to0 and R increase to infinity to obtain

\[
n\mathbb Eg_t(Z/a_n)\longrightarrow\int g_t\,d\nu=\Psi(t).
\]

The logarithmic remainder must still be checked. Put \(b_n=\mathbb E[(Z/a_n)\mathbf1_{\{|Z|\le a_n\}}]\). For fixed δ split the truncated mean at \(|Z|\le\delta a_n\). The square of the first part times n is bounded by the small-term second-moment estimate. The second part is at most F(δa_n) in absolute value, whose square times n tends to0. More explicitly, \(nb_n^2\le2n\mathbb E[(Z/a_n)^2\mathbf1_{\{|Z|\le\delta a_n\}}]+2nF(\delta a_n)^2\). For fixed δ, nF(δa_n) has a finite limit, so the last term vanishes. First let n increase to infinity and then let δ decrease to0. Therefore

\[
\limsup_n nb_n^2\le C\delta^{2-\beta},\qquad \lim_{n\to\infty}nb_n^2=0.
\]

Let \(z_n=\mathbb Ee^{itZ/a_n}-1=itb_n+\mathbb Eg_t(Z/a_n)\). Then \(n|z_n|^2\to0\), and the same logarithmic remainder estimate gives

\[
n\log(1+z_n)-itB_n\longrightarrow\Psi(t).
\]

Independence and the continuity theorem complete the domain-of-attraction proof. Small terms, far tails, linear centering and logarithmic errors have all been controlled; a power-law tail alone is not a substitute for these steps.

## 14.17 A computable heavy-tail model and the boundaries of the result

Take R≥1 with \(P(R>x)=x^{-\alpha}\) for x≥1, and assign an independent sign with probabilities p₊,p₋. For the signed variable Z, choose \(a_n=n^{1/\alpha}\); tail balance is exactly p₊,p₋, and every condition of the preceding theorem holds. In the symmetric case B_n=0. This gives an explicit attraction example for every0<α<2, not only Cauchy at α=1.

For this model, when α≠1 and a_n>1, direct integration gives \(B_n=n\Delta_p\alpha(a_n^{1-\alpha}-1)/((1-\alpha)a_n)\), where \(\Delta_p=p_+-p_-\). At α=1, \(B_n=\Delta_p\log n\). When α>1 one may instead subtract n times the true mean, changing the location of the limiting law. Unspecified centering conventions for a standard stable law can make two correct formulas appear contradictory.

We have proved sufficiency of regularly varying tails with limiting tail balance, and constructed the corresponding full range of α, skewness and location parameters. We have not proved the exhaustive assertion that every stable law has this representation, nor all necessity directions for attraction domains. Infinite-variance Gaussian attraction at α=2 requires slowly varying truncated-variance tools and is not a consequence of the preceding α<2 estimates. Finite-variance Gaussian limits are already established in Chapter 11 and here. Full representation and general array criteria belong to the unified theory of Chapter 27.

The scope must be explicit, but the structural gain is substantial. √n and n are two members of the scale family n^(1/α), rather than isolated calculations. Tail exponents determine how many visible jumps remain after rescaling, while centering determines their accumulated direction.

## 14.18 What it means to split a law into arbitrarily many independent pieces

Gaussian, Poisson and the stable laws just constructed have different shapes, yet all permit arbitrarily fine division. Division here does not mean arithmetically dividing one outcome; it means finding independent smaller experiments whose sum restores the original law.

A real Borel probability μ is **infinitely divisible** if for every integer m≥1 there is a probability ν_m with \(\mu=\nu_m^{*m}\). The m pieces for each m are independent and identically distributed. Roots for different m need not initially share a probability space.

The m-fold convolution root of \(N(b,\sigma^2)\) is \(N(b/m,\sigma^2/m)\). For a compound Poisson law with intensity λ and mark law Q, divide the intensity by m; a deterministic drift b is likewise divided by m. The truncated approximations of14.14 also have roots, but passing this property to their weak limit still requires proof of closure.

An ordinary Bernoulli(p),0<p<1, cannot even be split into two equal independent laws. If U+V∈{0,1} almost surely with U,V i.i.d., U cannot have an infinite essential upper or lower bound: independently restricting V to a bounded interval of positive probability would force the sum outside{0,1}. Let a,b be U’s essential infimum and supremum. Independence makes those of the sum2a,2b, so a=0,b=1/2. Positive mass for U in(0,1/2) gives positive mass for the sum in(0,1), impossible. Thus U takes only the endpoints; nondegeneracy gives both positive mass and hence positive mass at U+V=1/2, again impossible.

A Bernoulli law is not infinitely divisible, yet its independent rare-event accumulation tends to Poisson. The limit acquires a divisibility absent from each original entry. That is the phenomenon we must explain.

## 14.19 Why a weak limit remains arbitrarily divisible

First prove a step easily obscured by terminology: weak limits of infinitely divisible laws remain infinitely divisible. Convolution roots may move. Saying “take m-th roots and pass to a limit” leaves their tightness unproved.

A real variable Y has a median a with \(P(Y\le a)\ge1/2\) and \(P(Y\ge a)\ge1/2\). For an independent copy Y′, independence gives

\[
P(|Y-a|>R)\le2P(|Y-Y'|>R).
\]

For example, on Y>a+R and Y′≤a their difference exceeds R; the other side is analogous. The two events lie on disjoint positive and negative sides of the difference. Summing proves the inequality. Thus a tight family of differences yields a tight family of median-centered originals.

Suppose \(\mu_n\Rightarrow\mu\) with each μ_n infinitely divisible. Fix m and choose roots ν_n with characteristic functions ψ_n; let Y_n have these laws. The symmetrized differences have characteristic functions

\[
|\psi_n(t)|^2=|\phi_{\mu_n}(t)|^{2/m}\longrightarrow|\phi_\mu(t)|^{2/m}.
\]

The limit is continuous and equal to1 at0. Real-line continuity makes the differences tight, so the median-centered ν_n are tight. Sums of m independent centered roots are also tight. Adding m times the median gives the tight law μ_n. Deterministic translations between two tight families must be bounded: both variables fall in common bounded windows with probabilities greater than1/2, so these events overlap with positive probability and bound the translation.

The original roots ν_n are therefore tight. Extract a weak limit ν and pass to characteristic functions: ψ_ν^m=φ_μ. One-dimensional uniqueness identifies the m-fold convolution with μ. Since m was arbitrary, closure is proved. A separate subsequence may be used for each m.

This proves that the stable laws constructed in14.14 are infinitely divisible, since every truncated compound Poisson law with drift is. In fact every stable law as defined in14.14 is infinitely divisible: iterating the two-copy relation, if m copies sum to c_mZ+d_m in law, divide each copy by c_m and subtract d_m/(mc_m) to obtain an m-fold root. This uses stability itself, not a general exponent representation.

## 14.20 Why infinitesimal independent arrays cannot retain an indivisible block

Now allow absent means and variances. Let real rows \(Z_{nk}\) be independent and infinitesimal, and suppose deterministic c_n make \(\sum_kZ_{nk}-c_n\Rightarrow\mu\). We prove in full that **μ is infinitely divisible**. Equal-length blocks of a row need not have equal laws, since different positions may carry entirely different risks.

The mechanism is to replace the row by a sufficiently close compound Poisson ledger. Before replacement we need a finite budget ensuring that the accumulated errors remain small. Tightness of the sum supplies that budget, without inventing a finite variance.

Write φ_nk for individual characteristic functions and Φ_n for the uncentered row sum. Tightness must be applied to the centered sum, whose characteristic function is \(\widetilde\Phi_n(t)=e^{-itc_n}\Phi_n(t)\). Weak convergence makes those centered laws uniformly tight, so their readings are uniformly close to1 near0: use \(|e^{itx}-1|\le|tx|\) inside a common bounded window and2 outside. A deterministic translation changes only phase, so some δ∈(0,1) gives \(|\Phi_n(t)|\ge1/2\) for large n and all|t|≤δ. No tightness of the uncentered sums is asserted.

Take independent copies Z′_nk and put D_nk=Z_nk−Z′_nk. Independence and \(1-u\le-\log u\) give

\[
\sum_k(1-|\phi_{nk}(t)|^2)\le-\log\prod_k|\phi_{nk}(t)|^2=-\log|\Phi_n(t)|^2\le\log4\quad(|t|\le\delta).
\]

Average t over[−δ,δ]. The left side becomes \(\sum_k\mathbb E[1-\operatorname{sinc}(\delta D_{nk})]\), with sinc(0)=1. An absolute c>0 satisfies \(1-\operatorname{sinc}u\ge c\min(u^2,1)\): use Taylor near0, continuity and \(|\operatorname{sinc}u|\le1/|u|\) far away, and strict positivity on the intervening compact annulus. Also, since δ≤1, \(\min(\delta^2x^2,1)\ge\delta^2\min(x^2,1)\), so the required budget is at most \(\log4/(c\delta^2)\). The value of δ is already fixed here. Hence

\[
\sup_{n\ \mathrm{large}}\sum_k\mathbb E\min(D_{nk}^2,1)<\infty.
\]

Choose medians m_nk and set Y_nk=Z_nk−m_nk. Conditioning on either side of fixed Z_nk, the same argument as14.19 gives \(\mathbb E\min(Y_{nk}^2,1)\le2\mathbb E\min(D_{nk}^2,1)\). Denoting the left side by v_nk, we have

\[
\sup_{n\ \mathrm{large}}\sum_kv_{nk}<\infty,\qquad\max_kv_{nk}\longrightarrow0.
\]

The second conclusion uses infinitesimality. For every ε>0, all terms eventually assign more than1/2 probability to[−ε,ε], forcing every median into that interval; the centered Y remain infinitesimal. Now \(\mathbb E\min(Y^2,1)\le\varepsilon^2+P(|Y|>\varepsilon)\) proves the maximal bound. Here v is a truncated second-moment budget, not a variance.

## 14.21 Let each entry occur zero, one or several times

Continue with \(b_{nk}=\mathbb E\sin Y_{nk}\) and \(W_{nk}=Y_{nk}-b_{nk}\). This centering always exists. For fixed t,

\[
|e^{ity}-1-it\sin y|\le C_t\min(y^2,1),\qquad b_{nk}^2\le v_{nk}.
\]

For the first bound, subtract the linear exponential term on|y|≤1 and bound|y−sin y| by a constant times y²; outside that region all terms are bounded. The second follows from Cauchy–Schwarz and sin²y≤min(y²,1). Writing θ_nk(t)=E exp(itW_nk), multiplication by exp(−itb) cancels the linear term and gives

\[
|\theta_{nk}(t)-1|\le C_t v_{nk},\qquad\sum_k|\theta_{nk}(t)-1|^2\le C_t^2\max_kv_{nk}\sum_kv_{nk}\longrightarrow0.
\]

We now have summable errors. The logarithm estimate near1 compares the product with an exponential:

\[
\prod_k\theta_{nk}(t)-\exp\!\left\{\sum_k(\theta_{nk}(t)-1)\right\}\longrightarrow0.
\]

More explicitly, put \(A_n(t)=\sum_k(\theta_{nk}(t)-1)\) and \(R_n(t)=\sum_k[\log\theta_{nk}(t)-(\theta_{nk}(t)-1)]\). For fixed t, all θ eventually lie in one logarithm branch near1, and \(|R_n(t)|\le2\sum_k|\theta_{nk}(t)-1|^2\to0\). Since \(\operatorname{Re}A_n(t)\le0\), the difference of exponentials is at most \(|R_n(t)|e^{|R_n(t)|}\), without amplification by an arbitrarily large real exponential. A drift phase has modulus1 and changes nothing; convergence at each fixed frequency suffices.

Put \(d_n=\sum_k(m_{nk}+b_{nk})-c_n\). Construct a compound Poisson sum of intensity r_n whose mark law is the average of the W_nk laws, and add drift d_n. Its characteristic function is

\[
Q_n(t)=\exp\!\left\{itd_n+\sum_k(\theta_{nk}(t)-1)\right\}.
\]

Treat empty rows as deterministic drifts. For nonempty rows the estimate shows that Q_n differs pointwise by a vanishing amount from the characteristic function of the original centered sum. Thus Q_n tends to the characteristic function of μ. The continuity theorem makes these explicitly constructed compound Poisson laws with drift converge weakly to μ. Each is infinitely divisible; closure from14.19 proves the claim.

This replacement asserts neither total variation convergence nor identity of the fixed-count row experiment with the randomized one. Their readings differ by a vanishing amount at every fixed frequency, so they share a weak limit. Large jumps may remain and small terms may accumulate into a Gaussian. What cannot survive is an indivisible random block carried by one individual term.

## 14.22 Conversely, a divisible law can arise from infinitesimal rows

The connection also has a converse requiring no full representation theorem. Let μ be infinitely divisible. For each n choose an n-fold root ν_n with median m_n. We first prove that these roots, centered at their medians, tend to0.

The independent root difference D_n has characteristic function \(|\phi_\mu(t)|^{2/n}\). Since φ_μ is nonzero near0, this tends to1 on a fixed interval around0. Averaging t and using the tail lower bound for \(1-\operatorname{sinc}u\) shows tightness of D_n: its probability outside a sufficiently large fixed window tends to0, and finitely many initial terms are handled separately. Explicitly, fix a sufficiently small δ>0 with φ_μ nonzero on that interval. Then \(P(|D_n|>2/\delta)\le\delta^{-1}\int_{-\delta}^{\delta}(1-|\phi_\mu(t)|^{2/n})\,dt\to0\) by DCT. For arbitrary η>0 first choose N so this tail bound is below η for n≥N, then enlarge the same window to handle the finitely many n<N. This supplies the full tightness quantifiers without assuming that φ_μ is zero-free on the entire real line.

Any weak subsequence limit has characteristic function1 on that interval. For countably many dense t, E(1−cos(tD))=0 forces cos(tD)=1 almost surely. Continuity extends this to the whole interval, forcing D=0. Every subsequence limit is δ₀, so D_n tends to0. The median tail bound makes the centered roots tend to0 in probability as well.

Take n independent ν_n variables per row and subtract m_n from each. This is an infinitesimal array. Adding n m_n back to the row sum gives exactly μ for every n. Thus real weak limits of infinitesimal independent arrays, allowing deterministic centering, have precisely the range of infinitely divisible laws.

We also obtain a useful necessary property: infinitely divisible characteristic functions have no zeros. If φ_μ(t₀)=0, every root has modulus0 at t₀, but convergence of the centered roots to0 forces that modulus to tend to1, a contradiction. No converse is asserted here; zero-freeness is used only as the necessary property just proved.

## 14.23 A common mechanism, not a choice between two named laws

Place Gaussian and Poisson components in the same row. Let one group of small terms produce independent Gaussian fluctuations of total variance σ², and another group rare marks with total intensity tending to λ and mark law Q; add drift b. Independence multiplies their characteristic functions, yielding

\[
\exp\{itb-\sigma^2t^2/2+\lambda(\phi_Q(t)-1)\}.
\]

For an explicit infinitesimal realization, use n independent N(0,σ²/n) terms and n independent terms taking a Q mark with probability λ/n and0 otherwise, for sufficiently large n. The limit is neither purely Gaussian nor purely Poisson. Stable families combine jumps across all scales. Infinite divisibility captures their shared origin without imposing a common shape.

Writing down a jump integral has not classified all infinitely divisible laws. We have proved divisibility of infinitesimal array limits and their converse realization, closure, construction of stable families and a regular-variation attraction theorem. Uniquely separating the drift, Gaussian component and jump measure of an arbitrary law, and realizing those pieces through time, still requires full Lévy–Khintchine and process theory. Seeing their common outline does not settle those questions.

The hypotheses now have distinct jobs. Within-row independence multiplies frequency readings. Infinitesimality excludes individual blocks. Lindeberg removes the second-moment budget of visible large jumps. Regularly varying tails preserve large jumps on another scale. Without independence, one common sign can move an entire row together. Without infinitesimality, a single unchanged Bernoulli term can leave a non-infinitely-divisible limit. These boundaries explain the mechanism as much as the positive theorems do.

For a complete dependence counterexample, use one common symmetric sign ε and set \(Z_{nk}=\varepsilon/n\),1≤k≤n. Individual terms are infinitesimal but every row sum equals ε. If ε were infinitely divisible, so would its affine transform \((\varepsilon+1)/2\): divide each convolution root by2 and add1/(2m). This contradicts the Bernoulli example in14.18. If only infinitesimality is dropped, a single Bernoulli term with all remaining entries zero already gives the same obstruction, even with independent rows.

## Epilogue to Volume II: A Probability Begins to Have a Past

A ledger total no longer has to be drawn as a bell. We can distinguish entries absorbed into small fluctuations, entries retained as jumps, and tails that force a new scale. The limits are not competing empirical curves; they are answers left by the same summation problem under different tails, scales and independence structures.

To state these answers we had to decide which sets could be events, which functions could be integrated, and what a claim of convergence actually compared. Finite experiments were joined in spaces containing infinite records. Partial information became a measurable structure, and joint probability could be separated along an observation into conditional kernels. Transforms and limits now make these constructions identifiable, comparable and calculable. Questions about fairness and chance have acquired a language able to withstand infinity.

Yet this ledger has mostly been treated as already written, waiting for its total to be studied. Actual gambling, observation and random motion unfold differently. We revise a price as entries arrive, decide whether to stop using the past, and find that the next step’s chances depend on the present position. An unconditionally correct average need not remain the right judgment after the past has been observed.

The next question concerns more than the final limit of a random variable. As information grows, what remains fair, what must be remembered, and what is sufficient to determine the future? The unfinished game of Chapter 1 has not been left behind by the infinite world. We can now let it continue.

## History and Further Reading

Lindeberg’s 1922 paper: [publication record and DOI](https://link.springer.com/article/10.1007/BF01494395). Cramér and Wold’s1936 paper: [publication record and DOI](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s1-11.4.290). Publication records were checked; the present unified characteristic-function arguments are not presented as the original papers’ complete methods. The ledger, variance budgets and cell addresses are modern teaching reconstructions for this book.

Breadth continues to be guided by the [official listing of Kallenberg’s third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1); modern real-line tools may also be compared with [Durrett’s author-hosted textbook](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf). Our proofs depend on this book’s [real-line transforms](11-characteristic-functions.md), [independent series](12-infinite-sums.md), [rare counts and Laplace tools](13-rare-events.md), and [infinite experiments](08-infinite-experiments.md). Finite-dimensional selection is proved here, without borrowing general path-space compactness or the Lévy–Khintchine theorem.
