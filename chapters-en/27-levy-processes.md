# Chapter 27: What If Random Motion Jumps as Well as Diffuses? — Lévy Processes and Lévy–Khintchine Theory

Adding many independent small disturbances need not produce only a continuous rough curve. Consider independent clocks: clock k rings at rate 2ᵏ, and each ring moves the position right by 2⁻ᵏ. Later clocks make smaller but more frequent moves. Every layer contributes expected displacement t over time t.

Adding the layers without alteration gives no finite displacement. Subtract each layer’s expected displacement, however, and the remaining total fluctuation can form an actual random path. The difficulty is not merely allowing tiny jumps: it is deciding how infinitely many of them can coexist.

## 27.1 Every layer is finite; the whole sum need not exist

<a id="levy-clocks"></a>

\[
\begin{gathered}
N_k(t)\sim\operatorname{Poisson}(2^k t),\qquad
J_k(t)=2^{-k}N_k(t),\qquad k\ge1,\\
EJ_k(t)=t,\qquad
E[J_k(t)-t]^2=t\,2^{-k}.
\end{gathered}
\]

These independent Poisson clocks were constructed in Chapter 21 and can coexist on Chapter 8’s countable product space. Infinite total expectation alone would not prove almost sure divergence; the spikes of Chapter 7 warn against that inference. Here a stronger argument is available.

\[
P\{N_k(t)<2^{k-1}t\}
\le\frac{4}{2^k t}\quad(t>0).
\]

Chebyshev and Borel–Cantelli imply that, for each fixed positive t, eventually every layer contributes at least t/2. The uncentered positive series diverges almost surely. The centered variances are summable, so Chapter 12 gives convergence at a fixed time. There is no contradiction: we have changed the summands.

A separate answer at every fixed t is not enough. Such limits need not immediately form one right-continuous path with left limits, and uncountably many probability-one events cannot simply be intersected. This is the same quantifier difficulty encountered in constructing Brownian paths. We must identify admissible jump intensities and turn distributional limits into whole paths.

## 27.2 Preserve the increment structure, not continuity

<a id="levy-definition"></a>

Brownian and Poisson motion share a useful structure: disjoint time intervals give independent increments, and intervals of equal length give increments with the same distribution. Only Brownian motion is continuous. To study both, preserve the increment structure and require displacements over short times to vanish in probability.

\[
\begin{gathered}
X_0=0,\qquad X_t\in\mathbb R^d,\qquad
X_{t+s}-X_s\overset d=X_t,\\
X_{t_1}-X_{t_0},\ldots,X_{t_m}-X_{t_{m-1}}
\text{ independent}\quad(0=t_0<\cdots<t_m),\\
X_{t+h}-X_t\xrightarrow{P}0\quad(h\to0,\ t+h\ge0).
\end{gathered}
\]

In this chapter a Lévy process also has càdlàg paths: right continuity and a left limit at every positive time. This path requirement is part of our convention. We will construct such a version for every admissible parameter set, rather than silently treating an abstract family of finite-dimensional distributions as an already regular path.

Stochastic continuity is not path continuity. Poisson paths may jump on a finite interval, while the probability of a jump in a short interval around a specified time tends to zero. Together with càdlàg paths it excludes jumps at a fixed time: increments from the left converge almost surely to that jump and in probability to zero. Random jump times remain possible.

If only independent stationary increments are required, without either càdlàg paths or stochastic continuity, a discontinuous real additive function a gives a deterministic process Xₜ=a(t) with independent stationary increments but without the continuous-time exponent developed below. This is a mathematical boundary example, showing that regularity assumptions do real work.

## 27.3 A measure records both jump size and frequency

<a id="levy-measure"></a>

A finite-activity model needs one clock and a mark distribution: rate λ, independent jump sizes with law F. The finite measure λF records both. For the clocks at the beginning, a single total rate is no longer adequate: the total count can be infinite while jumps bounded away from zero still occur at a finite rate.

\[
\nu(B)=\text{mean number per unit time of jumps with size in }B,
\qquad B\subset\mathbb R^d\setminus\{0\}.
\]

For now this is a construction motive, not a fact already proved for every process. We first prescribe a Borel measure and construct clocks; later we recover it from any given Lévy path. Summability of the centered squared fluctuations suggests the condition

\[
\nu(\{0\})=0,\qquad
\int_{\mathbb R^d}(1\wedge\|x\|^2)\,\nu(dx)<\infty .
\]

This is a Lévy measure. Finite mass away from zero prevents infinitely many visible large jumps on a finite interval. Square weighting near zero allows centered fluctuations to be summed in L². Neither absolute first integrability nor finite total mass is required. The opening example places mass 2ᵏ at 2⁻ᵏ: its squared integral is finite, its first integral infinite.

The square condition is not merely a convenient proof assumption. With symmetric small-jump density |x|⁻³ on the line, the truncated characteristic-function modulus has a negative integral exponent. At every nonzero frequency, 1−cos(ux) is bounded below near zero by a constant times u²x², so that exponent tends to minus infinity. The candidate is one at zero and zero elsewhere, hence cannot be a weak probability limit. A deterministic drift changes only phase, not modulus.

## 27.4 Put the clocks for all scales on one space

<a id="levy-prm"></a>

Partition the nonzero space into the exterior of the unit ball and dyadic annuli. Every piece has finite measure. On each use a Poisson clock of that rate, with independent marks from the normalized restricted measure. Different bands are independent; zero-mass bands are empty. The countable product constructions of Chapters 8 and 10 put these choices on one space.

Each ring produces a pair consisting of time and jump size. Count these points in a random measure N. For nonnegative measurable f, N(f) is the sum of its values over all points, possibly infinite. Countable additivity holds path by path because the measure is a countable sum of Dirac masses.

\[
\begin{gathered}
\mu(ds,dx)=ds\,\nu(dx),\qquad
E e^{-N(f)}=\exp\!\left\{-\int(1-e^{-f})\,d\mu\right\},\\
E N(f)=\int f\,d\mu\quad(f\ge0).
\end{gathered}
\]

On one finite band and one finite time interval, condition on the count. Arrival times are ordered independent uniform points and marks are independent. The conditional Laplace transform is a single-point average raised to that count; averaging the Poisson count gives the first formula. Monotone convergence removes the finite-band restriction. The mean identity follows first for indicators, then simple functions and nonnegative limits.

For disjoint sets of finite intensity, insert a linear combination of their indicators. Factorization of the joint Laplace transform proves both Poisson counts and their independence. N is called a Poisson random measure with intensity μ. The name now abbreviates a constructed object. [The path proof, Section 1](../foundations/t-levy-paths.md#t-levy-prm), extends the argument to all measurable sets.

## 27.5 Compensation does not subtract an infinite constant

<a id="levy-compensation"></a>

Fix a positive cutoff ε. Add jumps larger than ε and at most one, then subtract the expectation on that finite band. Both terms are finite. Only then let ε tend to zero. There is no intermediate expression subtracting an infinite mean from an infinite jump sum.

\[
\begin{gathered}
M^\varepsilon_t=
\int_{(0,t]\times\{\varepsilon<\|x\|\le1\}}
x\,N(ds,dx)-t\int_{\varepsilon<\|x\|\le1}x\,\nu(dx),\\
E M^\varepsilon_t=0,\qquad
E\|M^\delta_t-M^\varepsilon_t\|^2
=t\int_{\delta<\|x\|\le\varepsilon}\|x\|^2\nu(dx),\qquad 0<\delta<\varepsilon\le1.
\end{gathered}
\]

The isometry follows because independent Poisson counts have variance equal to mean. Compute first for simple functions on disjoint finite-intensity sets, then extend using T-LP completeness to deterministic L² functions. The integral here is this deterministic L² extension, not a theory of predictable random integrands.

A finite-cutoff process is a martingale: future counts are independent of the past and compensation makes their conditional mean zero. Apply Chapter 15’s Doob inequality on dyadic time grids, then use right continuity to remove the grid. This gives more than a fixed-time isometry.

\[
\begin{gathered}
v(\varepsilon)=\int_{0<\|x\|\le\varepsilon}\|x\|^2\nu(dx)\downarrow0,\\
E\sup_{t\le T}\|M^\delta_t-M^\varepsilon_t\|^2
\le4T\,v(\varepsilon)\qquad(0<\delta<\varepsilon).
\end{gathered}
\]

## 27.6 How a square estimate constructs an entire path

<a id="levy-path-limit"></a>

Choose decreasing cutoffs whose remaining second integrals are at most 2⁻⁴ʲ. On [0,j], the probability that adjacent cutoffs differ in supremum norm by more than 2⁻ʲ is at most 4j2⁻²ʲ, a summable sequence. Borel–Cantelli and telescoping imply uniform convergence on every compact interval on one common probability-one event.

A uniform limit of càdlàg functions is càdlàg: approximate by one sufficiently close cutoff, then use its right continuity and left limits. Fatou extends the estimate to all cutoffs, not just the selected subsequence.

\[
\begin{gathered}
M^{\varepsilon_j}\longrightarrow M
\quad\text{locally uniformly a.s.},\\
E\sup_{t\le T}\|M_t-M^\varepsilon_t\|^2
\le4T\,v(\varepsilon)\to0 .
\end{gathered}
\]

Thus the full cutoff family converges uniformly on compact intervals in probability, abbreviated ucp. Fixed-time L² convergence preserves the martingale property. Factorization of joint increment characteristic functions passes to probability limits, preserving independent stationary increments. Vanishing short-time second moments give stochastic continuity. A common supremum estimate, rather than separate fixed-time answers, has constructed the path.

This is the missing step in the opening example. All its jumps are positive, yet the compensated process is not increasing. Each finite cutoff is deterministic downward motion plus finitely many positive jumps. The limit is defined by the whole sequence of compensated cutoffs, not by an ordinary infinite positive sum minus a finite descending line. It has mean zero and positive variance at each positive time. Increasing paths would make it nonnegative, forcing it to vanish by its zero mean, a contradiction.

## 27.7 Three independent kinds of motion

<a id="levy-model"></a>

Add an independent continuous Gaussian motion G with nonnegative covariance matrix A, a deterministic drift, and jumps outside the unit ball. Chapter 23 constructs G from independent Brownian coordinates and a matrix square root. There are only finitely many large jumps on each finite interval, even if their sizes have no mean.

\[
\begin{gathered}
X_t=bt+G_t+
\int_{(0,t]\times\{\|x\|>1\}}x\,N(ds,dx)+M_t,\\
E[G_sG_t^\top]=(s\wedge t)A,\qquad G\perp\!\!\!\perp N .
\end{gathered}
\]

This is already a Lévy process. At a finite cutoff, multiply the independent characteristic functions; compensation subtracts the jump term’s linear part. The Lévy condition dominates the quadratic remainder near zero. Removing the cutoff gives

\[
\begin{gathered}
E e^{i\langle u,X_t\rangle}=e^{t\Psi(u)},\\
\Psi(u)=i\langle b,u\rangle-\frac12u^\top Au+
\int_{\mathbb R^d\setminus\{0\}}
\left(e^{i\langle u,x\rangle}-1-
i\langle u,x\rangle\mathbf1_{\{\|x\|\le1\}}\right)\nu(dx).
\end{gathered}
\]

The subtracted linear term records centering at finite cutoffs; it does not alter jump sizes. The full small-jump first integral may not exist, so it cannot be treated as a finite mean transferred into drift. For a unit-jump Poisson process, the measure is λδ₁ and the Gaussian part is zero. Because the cutoff includes size one, b must equal λ: the compensated component is Nₜ−λt, and adding λt recovers the count. Thus b is not automatically the physical velocity or expectation.

We have proved that parameters construct a process. Lévy–Khintchine theory also asserts the converse: every regular motion with independent stationary increments has precisely this form. Without that converse we would have examples, not a classification.

## 27.8 Why not every law can be a unit-time increment

<a id="levy-khintchine"></a>

Divide unit time into n pieces. Its increment must be the sum of n independent identically distributed smaller increments, so its law is infinitely divisible. Chapter 14 proved that limits of infinitesimal independent arrays are infinitely divisible. We now turn that structural fact into explicit unique parameters.

The finite-dimensional Lévy–Khintchine theorem states that a real-vector probability law is infinitely divisible if and only if its characteristic function is the previous exponential at t=1, with a nonnegative symmetric matrix A, a Lévy measure ν and a real vector b. These parameters are unique under a fixed truncation convention. For a Lévy process, multiplying that exponent by time gives every increment law; independence then gives every finite-dimensional distribution.

The path construction proves sufficiency: dividing the parameters by n and adding n independent copies restores the original law. Necessity and uniqueness do not follow by reversing that construction. We develop the two difficult mechanisms: how tightness controls parameters and how to identify them without assuming second moments.

## 27.9 Replace an infinite measure by a finite object

<a id="levy-finite-measure"></a>

Taking subsequences of ν directly fails because its mass near zero may be infinite. But small jumps enter the exponent only quadratically. Weighting by a function that behaves like a square near zero and is bounded away from it produces a finite measure. A continuous truncation h is convenient for parameter convergence.

\[
\begin{gathered}
h(x)=\frac{x}{1+\|x\|^2},\qquad
w(x)=\frac{\|x\|^2}{1+\|x\|^2},\\
\Psi(u)=i\langle\gamma,u\rangle-\tfrac12u^\top Au+
\int(e^{i\langle u,x\rangle}-1-i\langle u,h(x)\rangle)\nu(dx),\\
b=\gamma+\int\left(x\mathbf1_{\{\|x\|\le1\}}-h(x)\right)\nu(dx).
\end{gathered}
\]

The drift-conversion integral is absolutely convergent: its integrand is cubic near zero and bounded away from zero, where ν has finite mass. Changing truncation does not change jumps, only the compensation assigned to the deterministic linear term.

On the line, place Gaussian variance at the origin to obtain a unique finite canonical measure. The associated integral kernel extends continuously there.

\[
\begin{gathered}
\rho=\sigma^2\delta_0+w\nu,\qquad
\Psi(u)=iu\gamma+\int K_u(x)\rho(dx),\\
K_u(x)=\frac{e^{iux}-1-iux/(1+x^2)}{x^2/(1+x^2)}
\quad(x\ne0),\qquad K_u(0)=-u^2/2.
\end{gathered}
\]

This explains how laws made entirely of jumps can leave a Gaussian limit: weighted mass concentrating at zero contributes the kernel’s quadratic value. Gaussian mass is not a jump of size zero. The atom belongs to the weighted replacement measure, not to ν.

For vectors, retain directions of approach to zero by lifting points into radius-direction space. The second directional moment of the zero layer gives the covariance matrix. Different angular measures may give the same matrix; the angular measure itself is not a unique parameter. [The parameter proof, Section 1](../foundations/t-levy-characteristics.md#t-levy-canonical), supplies the bounded continuous kernel and matrix details.

## 27.10 How tightness controls the parameters

<a id="levy-necessity"></a>

Start with a weakly convergent sequence of represented compound-Poisson-plus-Gaussian laws. Their characteristic functions are uniformly close to one near zero. Taking minus the logarithm of the modulus removes drift and leaves nonnegative terms. Averaging over a small frequency cube turns cosine into a product of coordinate sinc functions.

\[
\begin{gathered}
a(\delta)=\sup_n\sup_{\|u\|_\infty\le\delta}
[-\log|\phi_n(u)|]\longrightarrow0,\\
\frac{\delta^2}{6}\operatorname{tr}A_n+
\int\left[1-\prod_{j=1}^d\operatorname{sinc}(\delta x_j)\right]\nu_n(dx)
\le a(\delta).
\end{gathered}
\]

The kernel bounds δ²‖x‖² below near zero and a positive constant below far away. A fixed small δ bounds total weighted mass; decreasing δ also controls escape to infinity. The finite radius-direction measures are therefore tight, so Chapter 24’s selection applies. Drift cannot escape either: after removing the controlled integral, an unbounded drift admits a frequency tending to zero with phase minus one, contradicting common continuity at zero.

The limiting measure recovers ν at positive radii and A at the zero layer, while drift converges to γ. The continuous kernel transfers parameter limits to characteristic functions. Hence represented laws are closed under weak convergence. No independent jump/Brownian decomposition of a limiting process has been assumed.

To put every infinitely divisible law in that closure, take its nth convolution roots, subtract coordinate medians and then bounded sine means. Local characteristic functions of symmetrizations bound each truncated second moment by O(1/n), making correctly centered roots infinitesimal. Chapter 14’s budget bounds the row sum of those moments. Taylor remainders make the logarithmic difference between the original array and its accompanying compound Poisson law vanish. The original law is a weak limit of represented laws, proving necessity.

This step must not assume convolution roots have globally nonvanishing characteristic functions; the representation will imply that later. [The parameter proof, Sections 3–5](../foundations/t-levy-characteristics.md#t-levy-budget), starts with nonvanishing only near zero and completes centering, error estimates and parameter extraction.

## 27.11 Recover all jumps without second derivatives

<a id="levy-uniqueness"></a>

Without a second moment, differentiating the exponent twice is invalid. Finite differences remain legitimate: a second difference supplies a nonnegative weight that suppresses small jumps.

\[
\begin{gathered}
-\{\Psi(u+v)+\Psi(u-v)-2\Psi(u)\}=\widehat M_v(u),\\
M_v=(v^\top Av)\delta_0+
2(1-\cos\langle v,x\rangle)\nu(dx).
\end{gathered}
\]

M is finite, so Chapter 14’s Fourier uniqueness applies. Take each coordinate direction and its √2 multiple. Their combined weights are positive at every nonzero point: a nonzero coordinate cannot simultaneously be an integer multiple of 2π and 2π/√2. Add these measures and divide away from zero by that positive weight to recover all of ν.

After removing the jump integral, the real part identifies the entire quadratic form, including off-diagonal entries of A; the imaginary part identifies drift. Two continuous exponents of the same characteristic function differ by integer multiples of 2πi. Connectedness and their zero value at the origin force that difference to vanish. Uniqueness requires no additional moments.

## 27.12 Return to the original path, not just a new model

<a id="levy-ito"></a>

For a Lévy process already given on a probability space, the unit-time law now has a unique triplet. The ratio of the time-1/n characteristic function to the corresponding exponential is a continuous nth root of unity, equal to one at zero, so is identically one. Independence gives rational times, and stochastic continuity gives all times. Its finite-dimensional distributions match the constructed model.

Matching finite-dimensional laws does not by itself identify an independent Gaussian remainder on the original space. We must read jumps from that path and prove the reading measurable. A càdlàg path has finitely many jumps above a fixed threshold on a compact interval, or an accumulation would violate a one-sided limit. It can also be uniformly approximated by finite step functions.

\[
\begin{gathered}
N_X=\sum_{s>0:\Delta X_s\ne0}\delta_{(s,\Delta X_s)},\\
\sum_i a(t_i)f(X_{t_i}-X_{t_{i-1}})
\longrightarrow \sum_{0<s\le T}a(s)f(\Delta X_s)
\end{gathered}
\]

For the second formula use dyadic partitions, continuous time weight a and continuous compactly supported f vanishing near zero. A finite-step approximation leaves contributions only in cells containing its finitely many boundaries; one-sided limits identify their limits. First take integer T and rational dyadic grids. Each left side uses rational coordinates, so the jump measure is a measurable functional of them. A monotone-class argument gives all Borel counts.

In the constructed model, distinct bands almost surely never ring simultaneously. A uniform error bounds jump error by twice its norm, so actual model jumps are exactly the inserted Poisson points. The jump measure, compensated limit and continuous remainder are jointly measurable functionals. Equality of rational finite-dimensional laws and π–λ transfers these facts back to the given X, yielding the Lévy–Itô decomposition on its original space:

\[
\begin{gathered}
X_t=bt+C_t+
\int_{(0,t]\times\{\|x\|>1\}}x\,N_X(ds,dx)
+\lim_j\int_{(0,t]\times\{\varepsilon_j<\|x\|\le1\}}
x\,[N_X(ds,dx)-ds\,\nu(dx)],\\
C\text{ continuous centered Gaussian},\quad
E[C_sC_t^\top]=(s\wedge t)A,\quad C\perp\!\!\!\perp N_X .
\end{gathered}
\]

The equality holds for all times on one probability-one event. The chosen cutoff subsequence converges locally uniformly; all cutoffs converge ucp. If A is degenerate, the assertion is only that the continuous remainder has covariance A; no extra standard Brownian coordinates are invented on the original space. [The path proof, Sections 4–6](../foundations/t-levy-paths.md#t-levy-original-space), supplies measurability and common-null-set details.

## 27.13 What must converge when laws converge

<a id="levy-triplet-convergence"></a>

Poisson approximations may shrink jumps to zero, and a Gaussian limit can arise from those very jumps. The original Gaussian matrices therefore need not separately converge to the final one: unresolved small-jump covariance must be included. Convergence of jump measures away from zero also needs a separate condition excluding escape to infinity.

\[
\begin{gathered}
\mathrm{ID}(\gamma_n,A_n,\nu_n)\Rightarrow\mathrm{ID}(\gamma,A,\nu)
\quad\Longleftrightarrow\\
\gamma_n\to\gamma,\qquad
\nu_n\xrightarrow{v}\nu\text{ on }\mathbb R^d\setminus\{0\},\\
\lim_{R\to\infty}\limsup_n\nu_n(\|x\|>R)=0,\\
\lim_{\varepsilon\downarrow0}\limsup_n
\left\|A_n+\int_{\|x\|\le\varepsilon}xx^\top\nu_n(dx)-A\right\|=0 .
\end{gathered}
\]

All drifts use the same continuous truncation from Section 9. Small radii approach zero through spheres receiving no limiting jump mass. For sufficiency split the exponent into a small ball, compact annulus and remote tail: Taylor remainder is bounded by ε times second mass, vague convergence treats the annulus, and the tail condition treats infinity. Necessity extracts weighted measures along every subsequence and uses uniqueness to identify all limits. [The parameter proof, Section 7](../foundations/t-levy-characteristics.md#t-levy-convergence), records the double-limit order.

On the line this reduces to convergence of γ and weak convergence of finite canonical measures ρ. Removing jumps below ε and adjusting drift approximates the law by compound Poisson plus Gaussian laws. To use only compound Poisson, replace each Gaussian eigendirection by symmetric tiny jumps whose rate times squared size equals its eigenvalue.

\[
\frac{\lambda}{2a^2}\delta_{a e}+
\frac{\lambda}{2a^2}\delta_{-a e}
\quad(a\downarrow0)
\quad\Longrightarrow\quad
\text{Gaussian covariance }\lambda\,ee^\top .
\]

This proves distributional and finite-dimensional time-law approximation. It does not silently assert path-space J₁ convergence from triplet convergence; that additionally requires the path-tightness controls of Chapter 24.

## 27.14 Centering cannot be skipped in array limits

<a id="levy-array-limits"></a>

Triangular arrays from Chapter 14 now have a full identification tool. Rows are independent and infinitesimal; terms need not be identically distributed or integrable. Subtract coordinate medians, then bounded sine means. This choice cancels the first-order characteristic expansion while using only expectations of bounded functions.

\[
\begin{gathered}
k=1,\ldots,r_n,\quad r_n<\infty,\qquad \max_{k\le r_n}P(\|Z_{nk}\|>\eta)\to0\quad(\eta>0),\\
Y_{nk}=Z_{nk}-m_{nk},\quad
b_{nk}=E(\sin Y_{nk,1},\ldots,\sin Y_{nk,d}),\quad
W_{nk}=Y_{nk}-b_{nk},\\
d_n=\sum_k(m_{nk}+b_{nk})-c_n,\quad
\nu_n=\sum_k\mathcal L(W_{nk})\big|_{\mathbb R^d\setminus\{0\}},\\
\gamma_n=d_n+\int h\,d\nu_n,\qquad A_n=0 .
\end{gathered}
\]

The centered row sum converges to a specified infinitely divisible law if and only if these triplets satisfy the four conditions above. Replace each correctly centered term by a Poisson number of repetitions. A truncated second-moment budget controls its characteristic-function error, and the total logarithmic remainder is bounded by the largest budget times the total budget, hence vanishes. Conversely recover budget boundedness from the triplet conditions before asserting tightness. [The parameter proof, Sections 5 and 9](../foundations/t-levy-characteristics.md#t-levy-arrays), establishes both directions.

Why not Poissonize raw terms? A row of n deterministic values 1/√n has centered sum identically zero. Raw Poissonization randomizes the count and invents Gaussian variance one. Median centering makes every W zero and retains the correct degenerate limit. Deterministic position and genuine random fluctuation must first be separated.

## 27.15 Infinitely many jumps need not mean infinite variation

<a id="levy-variation"></a>

Activity and total variation describe different infinities. Finite total ν-mass is equivalent to finitely many jumps on every finite interval, by Poisson counts. With infinite mass, every positive-length rational time interval almost surely contains infinitely many jumps, yet their absolute sizes may still be summable.

\[
\begin{gathered}
X\text{ has finite variation on every compact interval a.s.}\\
\Longleftrightarrow\quad
A=0,\qquad
\int_{0<\|x\|\le1}\|x\|\,\nu(dx)<\infty .
\end{gathered}
\]

Sufficiency is concrete: Campbell’s identity makes the absolute small-jump sum finite, so compensation can be absorbed into finite linear drift. Necessity is more than the slogan that Brownian motion is rough. Infinite absolute small-jump integral makes the absolute jump sum infinite by the Poisson Laplace formula, and the variation of any càdlàg path dominates the sum of its jump norms.

If the Gaussian matrix is nonzero, project onto positive variance. Fix a jump path. If adding Gaussian motion has positive probability of finite variation, use two independent Gaussian copies with that same jump path. Both have finite variation with positive probability, so their difference would be a nonzero scaled Brownian motion of finite variation, contradicting Chapter 26. Fubini over jump paths completes the argument. [The path proof, Section 7](../foundations/t-levy-paths.md#t-levy-variation), supplies the details without invoking general quadratic variation.

\[
\begin{gathered}
d=b-\int_{\|x\|\le1}x\,\nu(dx),\qquad
X_t=dt+\sum_{s\le t}\Delta X_s
\quad\text{in the finite-variation case}.
\end{gathered}
\]

Positive-jump density 1/x on the unit interval has infinite total mass but finite first integral: infinite activity and finite variation. Density 1/x² satisfies the Lévy square condition but not the first-integrability condition, giving infinite variation after compensation. The same visible sign of jumps conceals a different summation mechanism.

## 27.16 No negative jumps does not imply an increasing path

<a id="levy-subordinator"></a>

Waiting and cumulative input often require increasing motion. A real Lévy process with nondecreasing paths is a subordinator; here it starts at zero, is not killed and has infinite lifetime. Monotonicity implies finite variation, removing the Gaussian part and non-absolutely-summable small jumps. Jumps must be positive, and the remaining actual linear drift must be nonnegative.

\[
\begin{gathered}
A=0,\quad \nu((-\infty,0))=0,\quad
\int_{(0,1]}x\,\nu(dx)<\infty,\quad
d=b-\int_{(0,1]}x\,\nu(dx)\ge0,\\
E e^{-qX_t}=
\exp\!\left[-t\left(dq+\int_{(0,\infty)}(1-e^{-qx})\nu(dx)\right)\right],
\quad q\ge0.
\end{gathered}
\]

These conditions suffice, since the ordinary positive jump sum constructs increasing paths. To prove the drift sign, split short-time jumps at size ηt. Both the probability of a larger jump and the expectation of the smaller jump sum divided by t vanish. Hence the jump sum divided by t tends to zero in probability, so Xₜ/t tends to d and nonnegativity forces d≥0. Only small-jump first integrability and finite large-jump mass are used.

For example, use density 1/x² only on (0,1), compensate it as above and take b=0. The process has mean zero, variance t and is nondegenerate. Nonnegativity would force a mean-zero variable to vanish, a contradiction. Positive jumps do not eliminate downward compensation: the Lévy measure describes jump directions, while the full path also depends on drift and compensation.

## 27.17 Stable laws become an exhaustive family

<a id="levy-stable"></a>

Chapter 14 constructed new stable laws through heavy-tail sums, leaving their exhaustive classification open. We can now let uniqueness constrain scaling instead of guessing a characteristic function. Sums of independent copies of a stable law change only location and scale; infinite divisibility supplies a continuous convolution family.

The convergence-of-types lemma prevents arbitrary scale and location changes under the same nondegenerate limit. Extend rational-time stability to real time; multiplication of times makes the scale a continuous multiplicative function, hence a power. Compare temporal and spatial scaling of covariance and jump measure:

\[
\begin{gathered}
a(t)=t^{1/\alpha},\qquad
t\sigma^2=t^{2/\alpha}\sigma^2,\qquad
\nu(rB)=r^{-\alpha}\nu(B),\\
0<\alpha<2:\quad
\nu(dx)=
\bigl(c_+\mathbf1_{\{x>0\}}+c_-\mathbf1_{\{x<0\}}\bigr)
|x|^{-1-\alpha}\,dx,\quad \sigma^2=0,\\
c_\pm\ge0,\quad c_++c_->0;\qquad
\alpha=2:\quad \nu=0,\quad\sigma^2>0.
\end{gathered}
\]

Scale multiplication comes from two operations on the same exponent. Start with the affine expression at time t, then multiply its convolution exponent by s:

\[
st\Psi(u)=\Psi(a(s)a(t)u)
+iu\{a(t)b(s)+s b(t)\}.
\]

This and the affine expression at time st describe one nondegenerate law. Uniqueness of positive scale and location forces a(st)=a(s)a(t). Time continuity turns multiplication into a power law; Gaussian covariance and jump measure must then obey the same scale rather than being chosen separately.

The density is a conclusion. Homogeneity first makes each tail a power; differences on intervals then give the density, and square integrability near zero forces α<2. Nonzero Gaussian variance forces α=2. Removing both leaves deterministic translation, excluded by nondegeneracy. This exhausts nondegenerate real stable laws, rather than treating Cauchy as the whole theory.

Centering at α=1 requires care. Let Δ be the difference of the two density constants. A change of scale moves the truncation boundary and leaves a logarithmic term. It is not an error and cannot be removed by a fixed location shift.

\[
\alpha=1:\qquad Z_1+\cdots+Z_n
\overset d=nZ+n(c_+-c_-)\log n .
\]

Symmetry removes the logarithm; for α≠1 a suitable fixed shift gives strict stability. Density and tail constants differ by a factor α. [The classification and centering proof](../foundations/t-levy-domains.md#t-levy-stable-classification) derives all parameters from convergence of types. Stability is distributional self-similarity under independent addition, not invariance of an individual magnified path.

## 27.18 Read tails back from the limit

<a id="levy-attraction"></a>

Constructing a stable law answers only half the question. Which original variables have sums attracted to it? Sufficiency exhibits a mechanism; necessity rules out other tails producing the same full-sequence limit. A non-Gaussian stable limit requires regular variation of the absolute tail together with balance between its two sides.

\[
\begin{gathered}
F(x)=P(|Z|>x)\text{ regularly varying with index }-\alpha,\quad0<\alpha<2,\\
\frac{P(Z>x)}{F(x)}\to p_+,\qquad
\frac{P(Z<-x)}{F(x)}\to p_-,\qquad p_++p_-=1,\\
nF(a_n)\to C>0,\qquad c_\pm=\alpha C p_\pm,\\
c_n=a_n\{nE h(Z/a_n)-\gamma\}
\quad\Longrightarrow\quad
\frac{S_n-c_n}{a_n}\Rightarrow\mathrm{ID}(\gamma,0,\nu_\alpha).
\end{gathered}
\]

The bounded-function center exists even without a mean. Tail limits identify ν away from zero; regular variation bounds small-jump second mass by a positive power of ε and remote tails by a negative power of R. The triplet criterion then gives sufficiency. Before raw Poissonization one must still control its logarithmic error; a suitable absolute q-moment makes n times the squared single-term characteristic error vanish.

For necessity, do not assume regular variation. Apply the correctly median-centered array criterion to convergent sums, obtaining scaled tail limits at every nonzero threshold. Convergence of types gives adjacent scale ratio one. The first scale crossing any large threshold extends those limits from the scale sequence to all real thresholds. Only then return to raw-term centering and prove the drift condition necessary.

This proves necessary and sufficient conditions for real stable attraction, not merely Chapter 14’s heavy-tail construction. [The domain proof, Sections 4–5](../foundations/t-levy-domains.md#t-levy-stable-domain-sufficient), includes quantile scales, truncation bounds, moving thresholds and centering. Oscillating tails may admit particular subsequential shapes without a full-sequence stable limit.

The exact equality specifying cₙ is a convenient choice; for general centers the necessary and sufficient condition is the following limit.

\[
nE h(Z/a_n)-c_n/a_n\longrightarrow\gamma.
\]

## 27.19 Infinite variance can still leave a Gaussian limit

<a id="levy-normal-domain"></a>

The division “finite variance means Gaussian, infinite variance means non-Gaussian” is false. The relevant objects are visible large jumps and unresolved small fluctuations at the chosen scale. Some infinite-variance tails are thin enough that large jumps disappear while truncated second mass accumulates into a nonzero atom at zero.

\[
\begin{gathered}
\mu=EZ,\qquad V(x)=E[(Z-\mu)^2\mathbf1_{\{|Z-\mu|\le x\}}],\\
\frac{S_n-c_n}{a_n}\Rightarrow N(\ell,\sigma^2),\quad\sigma^2>0\\
\Longleftrightarrow\
\begin{cases}
E|Z|<\infty,\quad V\text{ slowly varying},\quad a_n\to\infty,\\
nV(a_n)/a_n^2\to\sigma^2,\quad(n\mu-c_n)/a_n\to\ell.
\end{cases}
\end{gathered}
\]

Here Z is nondegenerate, summands are i.i.d. and scales positive; V on the right is defined after integrability is established. Slow variation includes finite positive limiting variance and slowly diverging V. Its tail meaning is that x² times the tail beyond x is negligible relative to V(x): visible large jumps disappear, leaving Gaussian second mass.

Necessity must not assume a mean. First use the independent difference Z−Z′, whose center is zero. Canonical mass concentrating at zero makes its truncated second moment slowly varying. Dyadic tail integrals prove first integrability of the difference; a median tail bound transfers this to Z. Only then subtract the mean and identify its truncated variance as asymptotically half that of the difference. Sufficiency uses the same tail bounds to control jumps, drift and logarithmic errors. [Sections 6–8 of the proof](../foundations/t-levy-domains.md#t-levy-normal-tail) establish both directions.

\[
\begin{gathered}
f(y)=|y|^{-3}\mathbf1_{\{|y|\ge1\}},\qquad
EY=0,\quad EY^2=\infty,\quad V(x)=2\log x\ (x\ge1),\\
a_n=\sqrt{n\log n}\quad(n\ge2),\qquad
\frac{Y_1+\cdots+Y_n}{a_n}\Rightarrow N(0,1).
\end{gathered}
\]

This density is normalized. Square-root time is not the only normalization leading to a Gaussian limit; it is the finite-variance input case. A slowly growing truncated variance changes the scale without leaving a jump measure away from zero. The same parameter-convergence mechanism explains Gaussian and heavy-tail stable limits while preserving their differences.

## 27.20 Why reflection cannot simply survive an overshoot

<a id="levy-ladders"></a>

At first contact Brownian motion is exactly at the target height, giving reflection an exact joining point. Jump motion can overshoot. The overshoot creates additional structure, so Brownian reflection formulas cannot be copied. A discrete random walk makes the distinction transparent.

Fix the signs first: R is the signed displacement of the endpoint from its maximum; D is the usual nonnegative drawdown.

\[
M_n=\max_{0\le j\le n}S_j,\qquad
R_n=S_n-M_n\le0,\qquad D_n=M_n-S_n=-R_n\ge0.
\]

Observe at an independent geometric time N with probabilities (1−z)zⁿ, 0<z<1. Every finite path has a unique first global maximum: it is a strict record from the past, followed by nonpositive relative partial sums. Geometric weights factor across that split, making \(M_N\) independent of \(R_N\) and therefore also of \(D_N\). At a deterministic one-step horizon, a symmetric walk gives (M₁,R₁)=(1,0) or (0,−1); using nonnegative drawdown gives (M₁,D₁)=(1,0) or (0,1). Independence fails in either convention.

\[
\begin{gathered}
T^+=\inf\{n\ge1:S_n>0\},\quad
T^-=\inf\{n\ge1:S_n\le0\},\\
F_\pm(z,u)=E[z^{T^\pm}e^{iuS_{T^\pm}};T^\pm<\infty],\\
1-z\phi_Z(u)=\bigl(1-F_+(z,u)\bigr)\bigl(1-F_-(z,u)\bigr).
\end{gathered}
\]

This is the discrete Wiener–Hopf product established here. One side is strict and the other weak because the split uses the first global maximum: ties belong to the later segment. Reversing that segment turns nonpositive prefixes into a weak record minimum at its endpoint. Independence after discrete stopping times gives strict ascending and weak descending ladder renewal series. Their transforms have modulus at most z, so the series converge absolutely. Comparing with the geometric endpoint characteristic function gives the identity.

Making both ladders strict fails for zero increments. [The ladder proof, Section 9](../foundations/t-levy-domains.md#t-levy-wiener-hopf), derives the transform from the unique path split, allowing lattice laws, ties and infinite ladder times. We do not set z to one without justification or claim all continuous-time fluctuation theory. Jumps require height and waiting-time information; continuous reflection is a special geometry.

## 27.21 Historical sources and the proof used here

<a id="levy-history"></a>

The representation connects limits of sums of independent random variables with independent-increment motion in time. Lévy’s 1934 paper, “Sur les intégrales dont les éléments sont des variables aléatoires indépendantes,” appeared in the Annali della Scuola Normale Superiore di Pisa and is digitized by Numdam. Khintchine’s 1937 “Zur Theorie der unbeschränkt teilbaren Verteilungsgesetze” addresses infinitely divisible laws; MathNet supplies its official record and original-paper entry.

These are verifiable primary-source entries, not claims that every intermediate lemma or present notation occurs in either original. Our proof is a modern reconstruction using measure theory, tightness, countable coordinates and L² tools. Finite-dimensional parameter compactness, transfer through path jump functionals and domain-of-attraction arguments are organized around this book’s established dependencies. The Poisson random-measure and compensation constructions can also be compared with Winkel’s own Oxford lecture notes.

**Primary sources and proofs.** [Lévy’s 1934 original](https://www.numdam.org/item/ASNSP_1934_2_3_3-4_337_0/); [Khintchine’s 1937 official archive](https://www.mathnet.ru/eng/sm5562); [Winkel’s own lecture notes](https://www.stats.ox.ac.uk/~winkel/ms3b10.pdf); [parameters, uniqueness and arrays](../foundations/t-levy-characteristics.md); [jump paths and original-space decomposition](../foundations/t-levy-paths.md); [stable classification, attraction and ladders](../foundations/t-levy-domains.md).

## 27.22 One increment structure, different kinds of paths

<a id="levy-conclusion"></a>

None of the opening clocks has been discarded. We changed how their contributions are combined: visible jumps are added as actual displacements; dense small jumps are compensated at finite cutoffs before a common supremum bound removes the cutoff. Second mass concentrating at zero leaves a continuous Gaussian part; mass remaining away from zero leaves identifiable jumps. Drift records the location convention for this sum.

Brownian and Poisson motion are not unrelated isolated examples. They reveal different components of one structure; stable laws show how tails and scales determine what survives magnification. Continuity, finite activity, finite variation, positive jumps and monotonicity remain distinct properties. A characteristic exponent places them on one verifiable map without erasing their differences.

Our increments still ignore current position. If entering a different region changes the next short segment’s law, one exponent no longer describes the evolution. The assembly based on independent increments must give way to state-dependent transitions, while continuity in time and path regularity still need proof. Having constructed motion from local jump frequencies, we can next investigate how local motion rules act on functions used to observe it.
