# T-LEVY-CHARACTERISTICS: Triplets, Tightness and Infinitesimal Arrays

This completes the distribution-level proofs of [Chapter 27](../chapters/27-levy-processes.md#levy-khintchine) for finite-dimensional real vectors. It uses characteristic-function uniqueness and continuity from Chapters 11 and 14, tight selection of finite measures from Chapter 24, and the median-centering mechanism of Chapter 14. Stochastic integration, the Lévy–Itô decomposition and Chapter 49’s general random-measure limits are not used.

## 1. A continuous truncation and a finite replacement measure

<a id="t-levy-canonical"></a>

\[
\begin{gathered}
h(x)=\frac{x}{1+\|x\|^2},\qquad w(x)=\frac{\|x\|^2}{1+\|x\|^2},\qquad x\in\mathbb R^d,\\
\Psi(u)=i\langle\gamma,u\rangle-\tfrac12u^\top Au+
\int_{x\ne0}(e^{i\langle u,x\rangle}-1-i\langle u,h(x)\rangle)\nu(dx),\\
A=A^\top\ge0,\qquad \nu(\{0\})=0,\qquad
\int(1\wedge\|x\|^2)\nu(dx)<\infty.
\end{gathered}
\]

The small-jump measure can have infinite total mass, preventing direct use of probability tightness. Multiplication by w makes it finite. For vectors, directions of approach to zero must also be retained: write nonzero points as radius r and unit direction θ, and lift wν to the product of [0,∞) and the unit sphere, initially with no mass at radius zero.

\[
\begin{gathered}
K_u(r,\theta)=
\frac{e^{ir\langle u,\theta\rangle}-1-
i\,r\langle u,\theta\rangle/(1+r^2)}{r^2/(1+r^2)}\quad(r>0),\\
K_u(0,\theta)=-\tfrac12\langle u,\theta\rangle^2.
\end{gathered}
\]

Taylor’s remainder makes this kernel continuous and bounded. For r≤1, subtract the linear term: the remainder is bounded by a constant times r², while the truncation differs from rθ by O(r³). For r≥1 the denominator is at least one half and the numerator is uniformly bounded. Bounded sets of frequencies give a common bound, and as frequency tends to zero the kernels tend uniformly to zero on compact radius-direction sets.

Represent a Gaussian matrix on the zero layer by placing its spectral eigenvalues at their unit eigenvectors. Conversely, integrate θθ-transpose against a zero-layer measure to obtain a nonnegative matrix. The angular distribution on that layer need not be unique; the matrix A is the unique parameter. It is not an atom of the jump measure at the origin.

## 2. First prove that given parameters produce a probability

<a id="t-levy-sufficiency"></a>

Restrict ν to radii exceeding ε, obtaining a finite measure. A compound Poisson sum from Chapters 13 and 21, an independent Gaussian vector and a deterministic shift construct the following characteristic function. The truncated drift integral is finite.

\[
\exp\!\left\{i\left\langle\gamma-\int_{\|x\|>\varepsilon}h(x)\nu(dx),u\right\rangle
-\tfrac12u^\top Au+
\int_{\|x\|>\varepsilon}(e^{i\langle u,x\rangle}-1)\nu(dx)\right\}.
\]

As ε decreases to zero, second-order domination makes the exponent converge to Ψ. The finite polar measure and bounded kernels from Section 1 let DCT establish continuity of Ψ at zero and value zero there. Chapter 14’s multivariate continuity theorem supplies a genuine probability with characteristic function exp Ψ. Divide every parameter by any positive integer and repeat the construction; multiplication gives infinite divisibility. A formal exponential has not simply been declared a probability.

## 3. How probability tightness controls jumps and Gaussian mass

<a id="t-levy-budget"></a>

Suppose distributions with such triplets converge weakly; finite compound Poisson laws plus shifts are special cases. Tightness makes their characteristic functions uniformly approach one near zero: restrict vectors to a common large ball, use the Lipschitz bound for exponentials there, and bound the outside error by twice the tail probability. Thus the following quantity is finite for small δ and tends to zero, with finitely many initial terms included.

\[
\begin{gathered}
a(\delta)=\sup_n\sup_{\|u\|_\infty\le\delta}
[-\log|\phi_n(u)|]\longrightarrow0,\\
\frac{\delta^2}{6}\operatorname{tr}(A_n)+
\int\left[1-\prod_{j=1}^d\operatorname{sinc}(\delta x_j)\right]\nu_n(dx)
\le a(\delta).
\end{gathered}
\]

The second line averages the negative log modulus over a frequency cube. Tonelli applies because the Gaussian quadratic form and one minus cosine are nonnegative; sinc at zero means one. The bracket is at least a positive dimension-dependent constant times min(δ²‖x‖²,1): use Taylor near zero, one large coordinate far away, and strict inequality on the intermediate compact annulus. Fixing a small δ bounds both the Gaussian trace and w-weighted jump mass.

\[
\sup_n\left[\operatorname{tr}(A_n)+\int w\,d\nu_n\right]<\infty,\qquad
\nu_n(\|x\|>2\sqrt d/\delta)\le2a(\delta).
\]

The second estimate controls remote tails separately; bounded total mass alone does not imply it. Radius times sphere is Polish and the sphere compact. Add missing mass up to a fixed constant at an isolated point, reducing to probabilities; Chapter 24’s Prokhorov theorem gives a weakly convergent subsequence of polar measures. The isolated point only handles missing total mass and is not counted as Gaussian mass.

## 4. The drift cannot escape either

<a id="t-levy-drift"></a>

Write J for the kernel integral against the polar measure. Bounded mass and tight remote tails make these J uniformly small near frequency zero: use the common kernel bound outside a large radius and uniform continuity inside. Hence exp(i〈u,γ〉)=φ(u)exp(−J(u)) uniformly approaches one too. If drift norms diverged along a subsequence, take u=πγ/‖γ‖²: the frequency tends to zero but the exponential equals minus one. Thus drifts are bounded.

Extract a joint subsequence of convergent drifts and weakly convergent polar measures. Each fixed-frequency kernel is bounded continuous, so the limiting exponent retains the form in Section 1: positive radii yield ν and the zero layer yields A. Finite polar mass gives the Lévy condition. Closure under weak limits is proved before uniqueness of the limiting parameters is assumed.

## 5. Every infinitely divisible law enters this limit

<a id="t-levy-necessity"></a>

First extend Chapter 14’s accompanying compound Poisson argument explicitly to vectors. Each row has finitely many terms k=1,…,rₙ, with rₙ<∞. Terms within a row are independent, and infinitesimality means that the largest probability of exceeding any fixed η>0 tends to zero. If the row sums centered by deterministic cₙ converge, each coordinate sum is tight. Choose coordinatewise medians and use Section 14.20’s sinc budget for independent differences. The last inequality below converts coordinate control into vector control.

\[
\begin{gathered}
Y_{nk}=Z_{nk}-m_{nk},\quad
v_{nk}=E(1\wedge\|Y_{nk}\|^2),\quad b_{nk}=E(\sin Y_{nk}),\quad
W_{nk}=Y_{nk}-b_{nk},\\
\sup_n\sum_kv_{nk}<\infty,\qquad\max_kv_{nk}\to0,\qquad
1\wedge\|y\|^2\le\sum_j(1\wedge y_j^2)\le d(1\wedge\|y\|^2).
\end{gathered}
\]

Sine is coordinatewise. The median bound follows because an independent copy lies on the other side of the median with probability at least one half; the truncated second moment is at most twice the independent-difference budget. Infinitesimality makes the medians and Y uniformly small, giving the maximal budget limit. No mean or variance is required.

\[
\begin{gathered}
|e^{i\langle u,y\rangle}-1-i\langle u,\sin y\rangle|
\le C_u(1\wedge\|y\|^2),\qquad \|b_{nk}\|^2\le d\,v_{nk},\\
\theta_{nk}(u)=Ee^{i\langle u,W_{nk}\rangle},\qquad
|\theta_{nk}(u)-1|\le C'_u v_{nk},\qquad
\sum_k|\theta_{nk}(u)-1|^2\to0 .
\end{gathered}
\]

Inside the unit ball Taylor cancels the linear part; outside, bounded sine gives the first estimate. Multiplication by the centering phase preserves its order. Choose logarithms only near one; the sum of real parts is nonpositive, so Section 14.21’s error estimate applies to vector inner products. The following genuine finite compound Poisson law plus drift has the same weak limit as the original row sum.

\[
\begin{gathered}
d_n=\sum_k(m_{nk}+b_{nk})-c_n,\\
Q_n(u)=\exp\left\{i\langle u,d_n\rangle+
\sum_k(\theta_{nk}(u)-1)\right\}.
\end{gathered}
\]

For any infinitely divisible vector law take an nth convolution root. Global absence of characteristic-function zeros is not presumed. On a fixed small interval on each coordinate axis, the original modulus exceeds one half and the root’s independent difference satisfies the next bound. Sinc averaging gives coordinatewise symmetrized truncated moments O(1/n), so the median-centered root tends to zero. A row of n such roots, with its deterministic median shift restored, has exactly the original law.

\[
1-|\phi_{\mathrm{root},n}(t e_j)|^2
=1-|\phi_\mu(te_j)|^{2/n}
\le-\frac2n\log|\phi_\mu(te_j)|
\quad(|t|\le\delta).
\]

The accompanying compound Poisson laws therefore converge to the original law. Sections 3–4 extract an LK representation, proving necessity. Global absence of characteristic-function zeros is now a consequence of the representation, not a hidden premise.

The root’s location must be retained. Let Vₙ have the nth root law, let mₙ be a coordinate-median vector, and put Yₙ=Vₙ−mₙ, bₙ=E sin Yₙ and Wₙ=Yₙ−bₙ. The local sinc bound gives vₙ=E(1∧‖Yₙ‖²)=O(1/n). For fixed u we obtain the exact identity and error bound below.

\[
\begin{gathered}
\theta_n(u)=Ee^{i\langle u,W_n\rangle},\qquad
\phi_\mu(u)=e^{i\langle u,n(m_n+b_n)\rangle}\theta_n(u)^n,\\
n|\theta_n(u)-1|^2=O(n^{-1}),\qquad
\left|\phi_\mu(u)-
e^{i\langle u,n(m_n+b_n)\rangle+n(\theta_n(u)-1)}\right|\to0 .
\end{gathered}
\]

Choose log near one; its remainder is bounded by a constant times |θₙ−1|². The accompanying exponent has nonpositive real part, so the characteristic-function error is at most exp(Cn|θₙ−1|²)−1. The deterministic phase always has modulus one; n mₙ need not be bounded. For μ=δₐ its root is a point mass at a/n and Wₙ is zero: n mₙ=a retains the whole location. Dropping the phase would incorrectly replace δₐ by δ₀.

## 6. Identify unique parameters without second moments

<a id="t-levy-uniqueness"></a>

If a characteristic function has two continuous exponents, their difference lies in 2πi times the integers and vanishes at zero. Connectedness makes the exponents identical. Use a finite difference, not a second derivative.

\[
\begin{gathered}
-\{\Psi(u+v)+\Psi(u-v)-2\Psi(u)\}=\widehat M_v(u),\\
M_v=(v^\top Av)\delta_0+2(1-\cos\langle v,x\rangle)\nu(dx).
\end{gathered}
\]

These measures are finite: their small-jump weights are O(‖x‖²) and large-jump weights bounded. Chapter 14’s finite-measure Fourier uniqueness identifies each M. Take v to be every coordinate unit vector and its √2 multiple. The sum of the weights is strictly positive off zero: a nonzero coordinate cannot be both a 2π integer and a 2π/√2 integer. Summing and dividing by that positive weight uniquely recovers all of ν, even when its total mass is infinite.

After removing the identified jump integral, the real part uniquely determines the whole quadratic form, including off-diagonal entries of A; the imaginary part determines γ. Coordinate-direction atoms alone would not identify off-diagonal entries. Uniqueness concerns the triplet, not an artificially chosen angular distribution at radius zero.

## 7. How triplets converge

<a id="t-levy-convergence"></a>

Use the same continuous truncation h for every drift. Vague convergence off zero means convergence of integrals against every continuous compactly supported function on the punctured space. It neither prevents escape to infinity nor records second-order fluctuations concentrating at zero. The complete criterion consists of the next four conditions, with small radii restricted to spheres having zero ν-mass.

\[
\begin{gathered}
\mathrm{ID}(\gamma_n,A_n,\nu_n)\Rightarrow
\mathrm{ID}(\gamma,A,\nu)\\
\Longleftrightarrow\
\gamma_n\to\gamma,\quad \nu_n\xrightarrow{v}\nu\text{ on }\mathbb R^d\setminus\{0\},\\
\lim_{R\to\infty}\limsup_n\nu_n(\|x\|>R)=0,\\
\lim_{\varepsilon\downarrow0}\limsup_n
\left\|A_n+\int_{\|x\|\le\varepsilon}xx^\top\nu_n(dx)-A\right\|=0.
\end{gathered}
\]

For sufficiency split the exponent integral into a small ball, a middle annulus and the far tail. On the ball the unweighted kernel is −〈u,x〉²/2 plus O_u(‖x‖³); the integrated error is at most C_u ε times the second moment there. The covariance condition bounds that moment. Vague convergence and mass-free boundaries control the annulus; the tail condition and bounded numerator remove the remote part. First send n to infinity, then ε down and R up. Exponents converge and the continuity theorem finishes.

For necessity extract polar-measure and drift limits from any subsequence using Sections 3–4. Uniqueness in Section 6 forces every extracted limit to have the same γ,A,ν. The a(δ) estimate already controls remote tails. At a radius whose sphere has zero limiting mass, test (1+r²)θθ-transpose on r≤ε including r=0. Its integral is exactly Aₙ plus the small-ball jump covariance. This whole quantity converges; shrinking the radius gives the double limit. The positive-radius part alone need not converge separately. Failure of any condition would supply a contradicting subsequence and extraction. This also explains why convergence of a particular angular measure at radius zero cannot be required in several dimensions.

Make the quantifiers explicit. At a fixed mass-free radius ε, test the polar measure with (1+r²)θθ-transpose times the indicator of r≤ε, including the zero layer. Approximate the indicator by continuous radial cutoffs. The error is controlled by mass in a thin shell, which vanishes because the limiting sphere has zero mass. Every subsequence has a further extraction with the same matrix limit. A subsequence staying a fixed distance away would contradict this, so convergence holds for the whole sequence at fixed ε. Only then decrease ε:

\[
\begin{gathered}
Q_n(\varepsilon)=A_n+\int_{0<\|x\|\le\varepsilon}xx^\top\nu_n(dx),\\
Q_n(\varepsilon)\longrightarrow
A+\int_{0<\|x\|\le\varepsilon}xx^\top\nu(dx),\\
\limsup_n\|Q_n(\varepsilon)-A\|=
\left\|\int_{0<\|x\|\le\varepsilon}xx^\top\nu(dx)\right\|
\longrightarrow0\quad(\varepsilon\downarrow0).
\end{gathered}
\]

The last term vanishes by Lévy second integrability and dominated convergence, without reversing the limits in n and ε. A check is the real measure with mass n²/2 at each of ±1/n and Gaussian parameter zero. Its exponent n²(cos(u/n)−1) tends to −u²/2: purely jump laws leave Gaussian variance one.

## 8. The finite canonical measure on the real line

<a id="t-levy-real-canonical"></a>

\[
\begin{gathered}
\rho=\sigma^2\delta_0+w(x)\nu(dx),\qquad
K_u(x)=\frac{e^{iux}-1-iu x/(1+x^2)}{x^2/(1+x^2)},\
K_u(0)=-u^2/2,\\
\mathrm{ID}(\gamma_n,\rho_n)\Rightarrow\mathrm{ID}(\gamma,\rho)
\quad\Longleftrightarrow\quad
\gamma_n\to\gamma,\quad \rho_n\Rightarrow\rho
\quad\text{as finite measures on }\mathbb R.
\end{gathered}
\]

On the line, the two directions at zero yield the same square and merge into one unique atom. Sufficiency follows by integrating bounded continuous K. Necessity follows from tight extraction and uniqueness. Weak convergence tests every bounded continuous function, including the constant one, and records total mass. It permits mass to approach zero without requiring atom masses at zero to converge: these are zero and one in the preceding symmetric-small-jump example. It records mass and concentration near zero; vague convergence of ν off zero does not.

## 9. An exact criterion for general infinitesimal arrays

<a id="t-levy-arrays"></a>

Use the coordinatewise medians, sine centers and W of Section 5. Each row measure below has finite total mass but can concentrate heavily near zero. Removing an atom at zero changes no exponent integral.

\[
\begin{gathered}
\nu_n=\sum_k\mathcal L(W_{nk})\big|_{\mathbb R^d\setminus\{0\}},\qquad
\gamma_n=d_n+\int h(x)\nu_n(dx),\qquad A_n=0.
\end{gathered}
\]

The original centered row sums converge to a given LK law exactly when these triplets satisfy Section 7’s four conditions. Necessity follows from the accompanying compound Poisson convergence. Sufficiency must recover Section 5’s budget rather than circularly assume tight original rows. In sufficiently late rows every sine-center coordinate has magnitude at most one; its negative is the corresponding median of W, giving

\[
\begin{gathered}
Ew(\|W_{nk}\|)\ge b_{nk,j}^{\,2}/4,\qquad
v_{nk}\le(4+8d)\,Ew(\|W_{nk}\|).
\end{gathered}
\]

The first bound uses probability at least one half on a median side and w(b)≥b²/2. For the second use Y=W+b, the truncated-square triangle bound and min(‖W‖²,1)≤2w(‖W‖). The four conditions bound weighted total mass on a small ball and its complement, hence the total budget. Infinitesimality sends the maximal budget to zero and the logarithm error disappears. On the real line this is equivalent to Section 8’s canonical-measure criterion.

Centering cannot be omitted. A row of n deterministic entries 1/√n sums to √n and becomes identically zero after subtraction. Direct Poissonization of the raw entries manufactures limiting random variance one. Correct median centering makes every W zero and leaves the genuine zero limit.

The erroneous limit follows from a direct calculation, not a guess based on variance:

\[
\exp\!\left\{n(e^{iu/\sqrt n}-1)-iu\sqrt n\right\}
\longrightarrow e^{-u^2/2}.
\]

The budget recovery is a three-region estimate. Choose a sufficiently small continuity radius 0<ε<1 so that Qₙ(ε) is eventually bounded in norm. These matrices are nonnegative, so their traces are bounded too. Choose R large enough that the remote tail is eventually less than one. Take a continuous compactly supported f on the punctured space, with 0≤f≤1 everywhere and f=1 on ε≤‖x‖≤R. Since w≤‖x‖² on the small ball and w≤1 elsewhere,

\[
\int w\,d\nu_n\le
\operatorname{tr}Q_n(\varepsilon)+\int f\,d\nu_n+
\nu_n(\|x\|>R).
\]

The small-ball condition, vague convergence and remote-tail condition bound the three terms respectively. Finitely many initial rows have finite measures and can be included in the common bound. The (4+8d) estimate then bounds Σₖvₙₖ. With the largest vₙₖ tending to zero, Σₖ|θₙₖ−1|² really vanishes. This proves sufficiency without assuming tightness of the original sums. Finite rows are an explicit hypothesis; countably infinite rows would require separate series and infinite-product arguments.

## 10. Changing the truncation changes drift accounting, not jumps

<a id="t-levy-truncation"></a>

\[
\begin{gathered}
\chi(x)=x\mathbf1_{\{\|x\|\le1\}},\qquad
b=\gamma+\int(\chi-h)\,d\nu,\\
\Psi(u)=i\langle b,u\rangle-\tfrac12u^\top Au+
\int(e^{i\langle u,x\rangle}-1-i\langle u,\chi(x)\rangle)\nu(dx).
\end{gathered}
\]

The conversion integral is absolutely convergent: χ−h is O(‖x‖³) on the small ball, while h is bounded and ν finite outside. More generally both truncations must be globally bounded Borel functions, each differing from x by O(‖x‖²) near zero. Their difference is second-integrable on a small ball and bounded on the finite-mass region away from zero, so the same calculation gives an absolutely convergent drift difference. Continuous truncation suits parameter convergence; unit-ball truncation suits the path decomposition. They cannot share an unconverted drift.
