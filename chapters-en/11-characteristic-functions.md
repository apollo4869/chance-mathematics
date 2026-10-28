# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 11: How Can a Distribution Be Recorded by a Function?—Characteristic Functions, Independent Sums and Gaussian Limits

Add the scores of two independent dice, and the same total can arise from several pairs of scores. Even when both dice have known distributions, the probability of each total must gather the contributions of those pairs. With more random variables, direct enumeration soon becomes cumbersome.

The Gaussian limit in [Chapter 3](03-normal.md) showed that independent addition can also bring initially different distributions toward a common shape. To understand that change, we need a representation that makes calculation easier without discarding the original probability information.

What mathematical representation can identify a probability law completely while turning independent sums into a simple operation?

## 11.1 Why is a fair price not yet a distribution?

One payoff is certainly 32 coins; another is 0 or 64 with equal chances. Their expectations agree, but they are plainly different experiments. Expectation records the average position, not how the outcomes spread out.

So we also ask for variance. Yet even knowing the mean and dispersion does not end the story. Let one experiment take \(-1,1\) with equal chances. Let another take 0 with probability \(2/3\), and \(-\sqrt3,\sqrt3\) with probability \(1/6\) each. Both have mean 0 and variance 1, but their fourth moments are 1 and 3.

We could keep asking for third moments, fourth moments and further averages. But some random variables lack even a first absolute moment; even having all integer moments generally requires extra conditions for those moments to identify the distribution. We need more than a table of moments that may never end, with entries we sometimes cannot fill in at all.

## 11.2 Rather than magnify distant outcomes, let them rotate

The exponential seems a natural choice. For independent real-valued variables, it turns sums into products. But \(e^{sX}\) greatly magnifies outcomes far away in one direction, and its expectation need not be finite.

For the Cauchy distribution, whose density is proportional to \((1+x^2)^{-1}\), every nonzero real \(s\) makes \(\mathbb E e^{sX}\) diverge: on the side where the exponential grows, the quadratically decaying density cannot contain it. Chapter 3 already showed us the difficulties caused by such tails.

There is another use of the exponential, however. Replace real growth by rotation in the complex plane:

\[
e^{itx}=\cos(tx)+i\sin(tx),\qquad |e^{itx}|=1.
\]

No matter how distant the outcome, this reading stays on the unit circle. Heavy tails can no longer destroy its integrability.

For a probability measure \(\mu\) on the real line, define its **characteristic function** by

\[
\phi_\mu(t)=\int_{\mathbb R}e^{itx}\,\mu(dx),\qquad t\in\mathbb R.
\]

If \(X\) has law \(\mu\), we also write \(\phi_X\). A complex expectation here simply means integrating the real and imaginary parts separately; it introduces no “complex probabilities.” The integration developed in Chapter 6 already accommodates it.

At a fixed frequency, different positions can point in the same direction, so one reading cannot identify a position. Changing the frequency continually changes these coincidences. We hope that the mean rotations at all frequencies together will identify the distribution being averaged.

This idea has a deep connection with Fourier analysis. In his 1822 *Analytical Theory of Heat*, Fourier studied heat conduction and trigonometric expansions; Chapter 4 has already brought random motion into contact with the heat equation. Complex exponentials now bring related oscillatory tools into the study of distributions. This does not mean that Fourier established characteristic-function theory in this chapter's modern measure-theoretic language. The arguments below are a modern reconstruction on our existing probability foundations. [Original book and publication record](https://www.e-rara.ch/zut/doi/10.3931/e-rara-19706)

## 11.3 Readings at different frequencies must be compatible

Before guessing what these readings can do, notice that every legitimate distribution satisfies

\[
\phi_\mu(0)=1,\qquad |\phi_\mu(t)|\le1,\qquad
\phi_\mu(-t)=\overline{\phi_\mu(t)}.
\]

Its characteristic function is not merely continuous but uniformly continuous, since

\[
|\phi_\mu(t+h)-\phi_\mu(t)|
\le\int|e^{ihx}-1|\,\mu(dx)\longrightarrow0
\quad(h\to0).
\]

The right side is independent of \(t\). Its integrand tends pointwise to zero and is bounded by 2, so Chapter 6's dominated convergence theorem gives exactly what we need. No moment of \(X\) has been assumed. The arbitrary-measure-space version and its null-set treatment are proved in the [integral foundations](../foundations/t-integral.md#t-integral-dct).

A stronger compatibility is hidden here. For any finitely many frequencies \(t_1,\ldots,t_m\) and complex coefficients \(c_1,\ldots,c_m\),

\[
\sum_{j,k=1}^m c_j\overline{c_k}\,
\phi_\mu(t_j-t_k)
=\mathbb E\left|\sum_{j=1}^m c_je^{it_jX}\right|^2\ge0.
\]

A function with this property is called positive definite: every such matrix is Hermitian positive semidefinite. This does not mean that the function is pointwise nonnegative. Indeed, the fair \(\{-1,1\}\) experiment has \(\phi(t)=\cos t\), which certainly takes negative values.

Why must different frequencies constrain one another? Because they observe the same probability. We may combine readings freely, but the resulting squared modulus cannot have a negative expectation. Numbers that each look reasonable may fail to come from one common world. Chapter 10's problem of conditional versions has appeared in another form.

We will return to ask whether these conditions suffice. The more urgent question is what trace independent addition leaves behind.

## 11.4 When worlds add, their readings multiply

Let \(X,Y\) be independent with laws \(\mu,\nu\). Chapter 8's product probability and Chapter 10's kernel integration tell us that the law of \(X+Y\) is

\[
(\mu*\nu)(A)=\int_{\mathbb R}\int_{\mathbb R}
\mathbf1_A(x+y)\,\mu(dx)\nu(dy).
\]

This is convolution. It does not simply add probabilities at the same position: it assembles every combination that produces the total displacement. The integrand is measurable and nonnegative, and Tonelli's theorem ensures that it defines a probability.

On the frequency side, this complicated assembly leaves only

\[
\phi_{X+Y}(t)
=\mathbb E(e^{itX}e^{itY})
=\phi_X(t)\phi_Y(t).
\]

Independence separates the joint integral into two integrals. Repetition gives \(\phi_{X_1+\cdots+X_n}=\phi_X^n\) for independent identically distributed \(X_1,\ldots,X_n\). Translation and scaling are equally direct:

\[
\phi_{aX+b}(t)=e^{itb}\phi_X(at).
\]

Independence cannot quietly disappear from this statement. If \(X=Y=Z\), where \(Z\) is standard Gaussian, then \(X+Y=2Z\) has variance 4; the sum of two independent standard Gaussians has variance 2. Identical marginals need not give identical sums.

Nor can we reverse the claim and infer independence merely because the characteristic function of one particular sum happens to factor. Identifying joint independence requires sufficiently rich joint or conditional readings; we will return to this at the chapter's end.

A route back to Chapter 3 has opened: understand the reading of one small error, then ask what survives many multiplications.

## 11.5 In frequency, the bell curve is still a bell curve

Before proceeding, we must find the Gaussian distribution's readings without hiding the answer in an unproved Fourier formula.

Write

\[
\gamma_1(x)=\frac1{\sqrt{2\pi}}e^{-x^2/2},\qquad
\psi(t)=\int_{\mathbb R}e^{itx}\gamma_1(x)\,dx.
\]

Chapter 3 evaluated the Gaussian integral, so \(\psi(0)=1\). Since \(\int|x|\gamma_1(x)\,dx<\infty\), dominated convergence allows differentiation under the integral. Integration by parts with \(\gamma_1'(x)=-x\gamma_1(x)\), whose boundary terms vanish by Gaussian decay, gives

\[
\psi'(t)=i\int x e^{itx}\gamma_1(x)\,dx
=-i\int e^{itx}\gamma_1'(x)\,dx
=-t\psi(t).
\]

Thus \(e^{t^2/2}\psi(t)\) has derivative zero, and the initial value yields

\[
\phi_{N(0,1)}(t)=e^{-t^2/2},\qquad
\phi_{N(m,\sigma^2)}(t)=e^{imt-\sigma^2t^2/2}.
\]

The second identity follows by an affine transformation; when \(\sigma=0\), it means the point mass \(\delta_m\). No general inversion theorem has been used.

The Gaussian's special character is striking. Multiplying the readings of two independent Gaussians simply adds the coefficients of the linear and quadratic terms. Once we prove that readings identify distributions, we can conclude rigorously that independent Gaussian sums remain Gaussian, with means and variances adding separately.

But we still owe the central step. Being able to compute readings does not yet show that they never lose the world.

## 11.6 Cover a distribution with a mist that can gradually be lifted

A smooth density might seem easy to recover from an oscillatory integral. But we may face a point mass, a singular distribution, or a mixture of all three. Chapter 10 warned us against assuming every probability has a density simply because densities are convenient.

One remedy is to add a little independent Gaussian noise. Let \(Z\sim N(0,1)\) be independent of \(X\), and consider \(X+\varepsilon Z\), with \(\varepsilon>0\). Its density is

\[
g_\varepsilon(x)=\int\gamma_\varepsilon(x-y)\,\mu(dy),\qquad
\gamma_\varepsilon(u)=\frac1{\sqrt{2\pi}\varepsilon}
e^{-u^2/(2\varepsilon^2)}.
\]

Each original position becomes a narrow Gaussian hill. Tonelli gives total integral 1, and bounded dominated convergence gives continuity in the translation parameter. Even when the original law has no density, the noisy law has a continuous one.

Rescaling the preceding Gaussian calculation also gives a directly verifiable identity:

\[
\gamma_\varepsilon(u)=\frac1{2\pi}
\int_{\mathbb R}e^{-itu}e^{-\varepsilon^2t^2/2}\,dt.
\]

Substitute this into \(g_\varepsilon\). Since \(\int e^{-\varepsilon^2t^2/2}\,dt<\infty\), Fubini permits exchanging the integrals, yielding

\[
g_\varepsilon(x)=\frac1{2\pi}
\int_{\mathbb R}e^{-itx}\phi_\mu(t)
e^{-\varepsilon^2t^2/2}\,dt.
\]

This is a recovery formula we have actually proved. We used a Gaussian integral identity followed by absolutely integrable interchange, rather than borrowing the general Fourier inversion that remains to be established.

The noise supplied a density but changed the distribution. Could lifting the mist leave a different world? For any bounded continuous \(f\),

\[
\int f(x)g_\varepsilon(x)\,dx
=\int\!\int f(y+\varepsilon z)\,\mu(dy)\gamma_1(z)\,dz
\longrightarrow\int f(y)\,\mu(dy).
\]

Pointwise continuity and a bounded dominator suffice; \(f\) need not be uniformly continuous on the whole line. In Chapter 7's language, the noisy laws converge weakly back to the original law.

We finally have a bridge: the frequency readings determine every layer of mist, and those layers can become arbitrarily thin.

The same operation has two faces: adding independent noise in position convolves the original probability with a Gaussian kernel, while in frequency it multiplies by \(e^{-\varepsilon^2t^2/2}\). This factor damps high frequencies, making potentially nonintegrable readings absolutely integrable. As \(\varepsilon\downarrow0\), continuous observations recover the original probability; we do not require a density to return pointwise at every position.

## 11.7 Why all frequencies together omit no probability

Suppose \(\mu,\nu\) have identical characteristic functions. The recovery formula then says that for every \(\varepsilon>0\), their noisy distributions have identical densities.

Letting \(\varepsilon\downarrow0\), every bounded continuous function has the same integral under the two original probabilities. One detail remains: event indicators need not be continuous. How do we know the probabilities themselves agree?

Fix any real \(a\). Let continuous \(f_m\) equal 1 on \(( -\infty,a]\), equal 0 on \([a+1/m,\infty)\), and decrease linearly between them. Then \(0\le f_m\le1\) and this function tends pointwise to \(\mathbf1_{(-\infty,a]}\). Dominated convergence gives

\[
\mu(( -\infty,a])=\lim_m\int f_m\,d\mu
=\lim_m\int f_m\,d\nu=\nu(( -\infty,a]).
\]

The distribution functions agree everywhere. Half-lines generate the Borel sets of the real line, so [generating-class uniqueness](../foundations/t-mclass.md#t-mclass-uniqueness) gives \(\mu=\nu\).

This is the uniqueness theorem for characteristic functions. It assumes no density and no moments, and overlooks no atoms.

Recall our opening question. Mean and variance read only two entries in an account; a characteristic function turns the entire probability into bounded readings. Each reading makes some positions coincide, but changing all frequencies together prevents two different distributions from remaining hidden forever.

Only now does the computation for independent Gaussian sums become a conclusion about distributions rather than merely a functional identity.

## 11.8 When can we read off a density directly?

Our recovery always included a Gaussian factor. If \(\phi_\mu\) itself belongs to \(L^1(\mathbb R,dt)\), can we simply remove that factor?

Define

\[
g(x)=\frac1{2\pi}\int e^{-itx}\phi_\mu(t)\,dt.
\]

This is continuous, and

\[
\sup_x|g_\varepsilon(x)-g(x)|
\le\frac1{2\pi}\int|\phi_\mu(t)|
|e^{-\varepsilon^2t^2/2}-1|\,dt\longrightarrow0.
\]

Consequently \(g\ge0\). For a continuous compactly supported \(f\), the noisy laws converge weakly to \(\mu\), while uniform convergence makes the corresponding local integral tend to \(\int fg\,dx\). These two quantities are therefore equal.

Choose continuous compactly supported cutoffs \(0\le\chi_R\uparrow1\) to obtain \(\int g\,dx=1\). Using these cutoffs and the tails of both finite measures, extend equality from compactly supported continuous functions to every bounded continuous function. The preceding ramp approximation then gives \(\mu(dx)=g(x)\,dx\). This proves density inversion for integrable characteristic functions.

Lifting the mist here has an extra guarantee beyond the uniqueness proof: the original readings are integrable, so the Gaussian factor can be removed inside an absolutely convergent integral, even giving uniform convergence of the densities. Uniqueness for an arbitrary probability needs recovery only through bounded continuous observations, without requiring such a density.

The condition is sufficient, not necessary. The uniform law \(U[-a,a]\) has a perfectly good density, yet

\[
\phi(t)=\frac{\sin(at)}{at},\qquad \phi(0)=1,
\]

Its absolute value is not integrable on the line: in every sufficiently distant half-period, a fixed proportion satisfies \(|\sin(at)|\ge1/2\), and those intervals contribute a divergent harmonic series. Having a density and having an integrable characteristic function are different properties.

We also need a small tool in the other direction. Suppose \(h\) is bounded, continuous and integrable. Put \(g(x)=(2\pi)^{-1}\int e^{-itx}h(t)\,dt\), and additionally assume \(g\) is integrable. A Gaussian cutoff in position gives

\[
\int e^{isx}e^{-\delta^2x^2/2}g(x)\,dx
=\int h(t)\gamma_\delta(s-t)\,dt.
\]

Fubini applies because both \(h\) and the position Gaussian are absolutely integrable. As \(\delta\downarrow0\), the left side is dominated by \(|g|\); writing the right side as \(\int h(s-\delta z)\gamma_1(z)\,dz\), bounded continuity gives its limit \(h(s)\). Thus \(\int e^{isx}g(x)\,dx=h(s)\).

This reciprocity is useful: when a candidate function's inverse integral is a nonnegative \(g\) of total integral 1, we have genuinely found its probability, rather than guessed two formally similar formulas.

## 11.9 Chapter 3's heavy-tailed counterexample finally has complete readings

In [Chapter 3, Section 3.8](03-normal.md#section-3-8), the failure of Cauchy averages to concentrate already warned us to examine tails. That argument used a known characteristic function and uniqueness. Uniqueness is now established; it remains to calculate the reading we borrowed there.

For \(a>0\), consider the candidate \(h(t)=e^{-a|t|}\). It is bounded, continuous and integrable. Evenness and an elementary exponential integral give

\[
\frac1{2\pi}\int e^{-itx}e^{-a|t|}\,dt
=\frac1\pi\int_0^\infty e^{-at}\cos(tx)\,dt
=\frac{a}{\pi(a^2+x^2)}.
\]

For the last step, take the real part of a complex exponential integral, or integrate by parts twice. The result is nonnegative and has integral 1 by the antiderivative arctangent. Reciprocity now proves rigorously that the centered Cauchy law of scale \(a\) has characteristic function \(e^{-a|t|}\).

Let \(X_1,\ldots,X_n\) be independent variables with this law. Then

\[
\phi_{(X_1+\cdots+X_n)/n}(t)
=\left(e^{-a|t|/n}\right)^n=e^{-a|t|}.
\]

Uniqueness shows that the average has exactly the same law as every \(X_i\). Averaging has produced no concentration.

The calculation sharpens the connection between tails and scale: the Cauchy reading has a corner of order \(|t|\) at zero, while a centered finite-variance law leaves a quadratic term. The order that survives accumulation determines why different sums need different scalings.

We have not yet developed general stable-distribution theory. But we already know that the central limit theorem cannot mean “addition always produces normality.”

## 11.10 Oscillation can even recover atoms and interval boundaries

Density inversion required additional integrability; uniqueness did not. For any probability, mist still lets us recover interval masses, provided we treat the boundaries carefully.

For \(a<b\), integrate the density formula of Section 11.6 over \((a,b)\):

\[
\int_a^b g_\varepsilon(x)\,dx
=\frac1{2\pi}\int
\frac{e^{-ita}-e^{-itb}}{it}\,
\phi_\mu(t)e^{-\varepsilon^2t^2/2}\,dt.
\]

At \(t=0\), define the quotient to be \(b-a\). Its modulus is at most \(b-a\), and the Gaussian factor ensures the absolute integrability needed for interchange.

The left side is also \(P(a<X+\varepsilon Z<b)\). Conditional on \(X=x\), this probability tends to 1 when \(x\) lies inside the interval and 0 outside; at either endpoint, Gaussian symmetry makes it tend to \(1/2\). Hence

\[
\mu((a,b))+\tfrac12\mu\{a\}+\tfrac12\mu\{b\}
=\lim_{\varepsilon\downarrow0}\frac1{2\pi}\int
\frac{e^{-ita}-e^{-itb}}{it}\phi_\mu(t)
e^{-\varepsilon^2t^2/2}\,dt.
\]

Those half-atoms are not a notational nuisance. They are what symmetric noise sees from the two sides of a boundary.

Even a single atom can be read directly:

\[
\frac1{2T}\int_{-T}^T e^{-ita}\phi_\mu(t)\,dt
=\int\frac{\sin(T(x-a))}{T(x-a)}\,\mu(dx)
\longrightarrow\mu\{a\}.
\]

At \(x=a\), the quotient is defined as 1; its modulus never exceeds 1, and it tends to zero at every other point. Dominated convergence finishes the proof. Repeated oscillation cancels contributions away from the target, while mass exactly at the target keeps pointing in the same direction.

We know readings recover distributions. The harder question now is whether stabilizing every reading makes the distribution itself stabilize.

## 11.11 Every frequency converges—why can the world still disappear?

If \(\mu_n\Rightarrow\mu\), [Chapter 7](07-convergence.md)'s bounded-continuous-function criterion immediately gives \(\phi_{\mu_n}(t)\to\phi_\mu(t)\): apply it separately to cosine and sine.

The converse has a trap. Let \(\mu_n\) be uniform on \([-n,n]\). Then

\[
\phi_n(t)=\frac{\sin(nt)}{nt}\longrightarrow
\begin{cases}1,&t=0,\\0,&t\ne0.\end{cases}
\]

Every frequency has a limit, but the limit is no probability's characteristic function: it is discontinuous at 0. On the position side, every fixed bounded interval has mass tending to zero. Probability has not vanished at any \(n\), but it has escaped our stationary observation window.

Pointwise limits must therefore do more than stabilize readings: they must stop mass escaping to infinity. Chapter 7 distinguished tightness of one probability from uniform tightness of a family. We need the latter: for every \(\eta>0\), one common bounded closed interval must contain at least \(1-\eta\) of every \(\mu_n\).

The behavior of characteristic functions near zero can detect this escape. To see it, we must combine a small band of low frequencies rather than stare at one frequency.

## 11.12 How can a short band near zero restrain distant mass?

For \(\delta>0\), define

\[
A_\delta(\mu)=\frac1{2\delta}\int_{-\delta}^{\delta}
(1-\operatorname{Re}\phi_\mu(t))\,dt
=\int\left(1-\frac{\sin(\delta x)}{\delta x}\right)\mu(dx).
\]

Interchange is legitimate because the integrand is bounded on a finite frequency interval. At \(x=0\), use the continuous extension. The bracket is nonnegative; if \(|x|>2/\delta\), the sinc term has modulus less than \(1/2\). Therefore

\[
\mu\{|x|>2/\delta\}\le2A_\delta(\mu).
\]

This is our bridge. When the low-frequency average deviates little from 1, distant positions cannot conceal much mass.

Suppose \(\phi_n(t)\to\phi(t)\) at every real number and \(\phi\) is continuous at 0. Automatically \(\phi(0)=1\). First choose \(\delta\) small enough that \(1-\operatorname{Re}\phi(t)\) is small throughout the band. Bounded dominated convergence on that finite interval gives

\[
A_\delta(\mu_n)\longrightarrow
\frac1{2\delta}\int_{-\delta}^{\delta}
(1-\operatorname{Re}\phi(t))\,dt.
\]

All sufficiently large \(n\) consequently have a common tail bound. For the finitely many remaining \(\mu_n\), use \([-R,R]\uparrow\mathbb R\) separately and take the largest radius. The whole family is uniformly tight.

Notice the order: control the limiting readings near zero, control all sufficiently late probabilities, then accommodate the finitely many initial ones. Saying only “each probability is tight” cannot produce a common window.

## 11.13 With a common window, how do we extract an actual limiting law?

Preventing escape is not yet constructing a limit. We need a selection argument on the real line. Rather than borrow the later Prokhorov theorem for general spaces, we use rational marks directly.

Let \(\{\mu_n\}\) be uniformly tight, with distribution functions \(F_n\). Enumerate the rationals, select a convergent subsequence at the first, then a further one at the second, and continue. A diagonal subsequence \(n_k\) satisfies

\[
F_{n_k}(q)\longrightarrow L(q)\qquad(q\in\mathbb Q).
\]

Every reading lies in \([0,1]\), so the extraction can continue, and \(L\) is monotone on the rationals. Define

\[
F(x)=\inf_{q>x,\ q\in\mathbb Q}L(q).
\]

This is monotone and right-continuous. For right-continuity, choose any number slightly above \(F(x)\), then a rational \(q>x\) with \(L(q)\) below that number. All sufficiently nearby points to the right of \(x\) still have \(y<q\), hence \(F(y)\le L(q)\). Combine this with monotonicity.

Uniform tightness gives \(F(-\infty)=0,F(+\infty)=1\). Indeed, for any \(\eta\), choose a common interval \([-R,R]\). All \(F_n(q)\le\eta\) when \(q<-R\), and all \(F_n(q)\ge1-\eta\) when \(q>R\). Pass to limits and then let \(\eta\downarrow0\) to obtain both endpoint properties.

Chapter 10's quantile construction now produces a probability \(\mu\) with distribution function \(F\): send a uniform variable to the appropriate quantile. We need not assume anew that a limiting measure exists.

Finally check \(F_{n_k}(x)\to F(x)\) at continuity points \(x\) of \(F\). For rationals \(p<x<q\), monotonicity gives

\[
L(p)\le\liminf_k F_{n_k}(x)
\le\limsup_k F_{n_k}(x)\le L(q).
\]

The infimum on the right is \(F(x)\). The supremum on the left is \(F(x-)\): on one hand \(L(p)\le F(p)\); on the other, for every \(y<x\), a rational \(q\in(y,x)\) gives \(F(y)\le L(q)\). At continuity points the bounds agree.

Chapter 7's distribution-function criterion now gives a weakly convergent subsequence. This is a real-line Helly selection principle: a common tail window prevents escape, countably many marks permit diagonal selection, and monotonicity with right-continuity assembles scattered readings into a probability.

## 11.14 Lévy's continuity theorem: local compatibility recovers an entire limiting world

Our tools can finally be joined.

**If the characteristic functions of probabilities \(\mu_n\) converge at every real number to \(\phi\), and \(\phi\) is continuous at 0, there is a unique probability \(\mu\) with \(\phi=\phi_\mu\), and \(\mu_n\Rightarrow\mu\). Conversely, weak convergence makes characteristic functions converge pointwise to the limiting characteristic function.**

This is Lévy's continuity theorem on the real line. The converse is already proved. For the forward direction, the low-frequency bound gives uniform tightness; the previous section extracts a weakly convergent subsequence with limit \(\mu\). Along it, the bounded-continuous-function criterion gives \(\phi_\mu(t)=\phi(t)\). The candidate readings really belong to a probability.

Every other subsequence likewise has a further weakly convergent subsequence, whose limit has the same characteristic function and therefore equals \(\mu\) by uniqueness. If the full sequence failed to converge to \(F_\mu\) at a continuity point of \(F_\mu\), we could select a subsequence staying a fixed distance away, then extract a weakly convergent subsequence, a contradiction. Thus the full sequence converges weakly.

We did not assume continuity of \(\phi\) everywhere. Continuity at zero prevents escape; once a probability is found, continuity elsewhere follows automatically.

Nor must the random variables all live on the same probability space. We compare their laws. Chapter 7's coupling can provide a new joint realization when needed, but pointwise conclusions in that new realization are not almost-sure relationships already possessed by the original variables.

The theorem fulfills the promise of frequency language: pointwise calculations that preserve continuity at zero imply a limit of entire distributions. Chapter 3's bell curve can at last return along this road.

## 11.15 What exactly does finite variance leave near zero?

It is tempting to expand the exponential and take expectations immediately. But a remainder involving \(|X|^3\) silently demands a third moment, which is not a hypothesis of the finite-variance central limit theorem.

Our quadratic expansion must spend only a second moment. The exponential's integral remainder gives

\[
e^{iu}=1+iu-\frac{u^2}{2}+u^2r(u),\qquad
r(u)=\int_0^1(1-s)(1-e^{isu})\,ds.
\]

For every real \(u\), \(|r(u)|\le1\), and \(r(u)\to0\) as \(u\to0\). This remainder does not bring a third power into the integral.

Suppose \(\mathbb EZ=0,\mathbb EZ^2=1\). Substituting \(u=hZ\) yields

\[
\phi_Z(h)=1-\frac{h^2}{2}
+h^2\mathbb E[Z^2r(hZ)]
=1-\frac{h^2}{2}+o(h^2).
\]

Since \(|Z^2r(hZ)|\le Z^2\) is integrable, dominated convergence supplies the final step. No third-moment assumption has been added.

More generally, if \(\mathbb E|X|^k<\infty\), repeated difference quotients dominated by \(|X|^j\) give \(\phi_X^{(j)}(t)=\mathbb E[(iX)^je^{itX}]\) for \(j\le k\). Our limit requires only the quadratic local information above.

Finite variance does not make every distant outcome harmless. It makes their combined contribution at sufficiently low frequencies a controlled quadratic term. Compared with the Cauchy function's linear corner at zero, this is genuinely different local geometry.

## 11.16 Why do multiplied readings of small errors leave only a quadratic term?

[Chapter 3, Section 3.6](03-normal.md#section-3-6) explained the bell curve's mechanism through products and quadratic terms. The remainder control of Section 11.15 and the continuity theorem just proved now justify every step of that route. Let \(X_1,X_2,\ldots\) be independent and identically distributed, with

\[
\mathbb EX_1=m,\qquad
0<\sigma^2=\mathbb E(X_1-m)^2<\infty.
\]

Put \(Z_j=(X_j-m)/\sigma\), and consider

\[
S_n=\frac{X_1+\cdots+X_n-nm}{\sigma\sqrt n}
=\frac{Z_1+\cdots+Z_n}{\sqrt n}.
\]

Fix a frequency \(t\). Independence and the quadratic expansion give

\[
\phi_{S_n}(t)=\left[\phi_{Z_1}(t/\sqrt n)\right]^n,
\qquad
u_n:=\phi_{Z_1}(t/\sqrt n)
=1-\frac{t^2}{2n}+o(n^{-1}).
\]

Many texts now take a complex logarithm. That is legitimate, but requires choosing a branch near 1. A direct comparison avoids hiding this detail. Let \(v_n=1-t^2/(2n)\). For sufficiently large \(n\), \(0\le v_n\le1\), while \(|u_n|\le1\). An algebraic identity gives

\[
|u_n^n-v_n^n|
\le |u_n-v_n|\sum_{j=0}^{n-1}|u_n|^j|v_n|^{n-1-j}
\le n|u_n-v_n|\longrightarrow0.
\]

The elementary real limit gives \(v_n^n\to e^{-t^2/2}\). Hence

\[
\phi_{S_n}(t)\longrightarrow e^{-t^2/2}.
\]

The right side is the standard Gaussian characteristic function already computed directly, continuous at 0. Lévy's theorem finally yields

\[
\frac{X_1+\cdots+X_n-nm}{\sigma\sqrt n}
\Rightarrow N(0,1).
\]

This completes the modern proof of the independent, identically distributed, finite-variance central limit theorem. If \(\sigma^2=0\), then \(X_1=m\) almost surely. We cannot divide by \(\sigma\); instead the unstandardized centered sum divided by \(\sqrt n\) is identically zero and converges to \(\delta_0\).

Square-root scaling keeps the accumulated quadratic contribution finite, while the integrable control from Section 11.15 removes the remainder. The argument spends only a second moment, admitting even errors with no third moment into the same limit.

That formal calculation alone would not suffice. Uniqueness identifies whom the readings describe; continuity ensures the distributions truly approach that law without losing mass outside the frequency calculation. Our longer route makes the final few lines more than an attractive guess.

## 11.17 What does a Gaussian limit give—and what does it leave open?

Weak convergence does not imply every local shape converges. If the original variables are integer-valued, \(S_n\) at every finite \(n\) still has only countably many possible values and no Lebesgue density at all. We cannot say its density converges pointwise to a bell curve; local limit theorems need additional conditions and scale analysis.

The finite-variance proof supplies no uniform approximation rate either. Quantifying the error often requires stronger moment or tail control. A limit without a quantified error should not be presented as an equally accurate numerical formula at every sample size.

Independence is equally substantive. If all \(X_j\) equal one standard Gaussian \(Z\), the centered sum divided by \(\sqrt n\) is \(\sqrt nZ\); its mass spreads outward rather than approaching a standard Gaussian. Limit theorems under dependence need their own conditions.

One useful connection deserves clarification now. Suppose \(A_n\Rightarrow A\) and \(B_n\to b\) in probability, each pair \((A_n,B_n)\) defined on the same probability space, though spaces may differ with \(n\). Then

\[
A_n+B_n\Rightarrow A+b,\qquad
A_nB_n\Rightarrow bA.
\]

No independence is needed. Weak convergence makes the laws of \(A_n\) uniformly tight: choose continuity points in the limiting law's two tails, use convergence of distribution functions for large \(n\), then accommodate the finite beginning. For bounded continuous \(f\), first restrict \(|A_n|\) to a common finite interval, then restrict \(|B_n-b|\) to be small. Addition or multiplication in this compact region makes the change in \(f\) uniformly small. Tightness and convergence in probability control the bad events, where the difference is at most \(2\|f\|_\infty\). Let \(n\) grow, enlarge the interval and shrink the tolerance. This gives \(\mathbb E f(A_n+B_n)-\mathbb E f(A_n+b)\to0\), and likewise for products. Weak convergence applied to \(x\mapsto f(x+b)\) or \(f(bx)\) supplies the remaining limit.

This is the basic mechanism of Slutsky-type conclusions: one quantity still fluctuates while another concentrates at a constant, permitting replacement in a distributional limit. If the second limit is not constant, marginal convergence alone cannot determine the joint limit; Chapter 4's warning about relationships between times still applies.

Does a Gaussian limit mean that the \(S_n\) along one experiment's record converge almost surely to some Gaussian variable? Our theorem says no such thing. Chapter 7 distinguished these questions. Stabilization of distributional shape and the behavior along an infinite record remain different mathematical demands.

## 11.18 Which functions can really be readings of a probability?

We began with probabilities and obtained characteristic functions, then recovered probabilities from limits of characteristic functions. We can now return to Section 11.3: how can a function prove that it is more than an invented account of frequencies?

Bochner's theorem on the real line answers: **\(h(0)=1\), continuity at 0, and positive definiteness characterize characteristic functions of probability measures.** Necessity is proved. We now construct the probability for sufficiency, turning compatible finite readings into an actual law once again.

First obtain control from positive definite matrices. Give finite formal combinations the inner products \(\langle v_t,v_s\rangle=h(t-s)\). Positive definiteness gives Cauchy–Schwarz; zero-length vectors may first be quotiented out. Every \(v_t\) has length 1, so

\[
|h(t+s)-h(t)|^2
\le\|v_{t+s}-v_t\|^2\|v_0\|^2
=2(1-\operatorname{Re}h(s)).
\]

Two-by-two matrices also give \(|h(t)|\le1\). Continuity at zero thus implies global uniform continuity. The formal inner products involve only finite combinations and do not assume any random variable exists.

Next let \(h_\varepsilon(t)=h(t)e^{-\varepsilon^2t^2/2}\). This remains positive definite: in any finite quadratic form replace the coefficients by \(c_je^{i\varepsilon t_jZ}\), then integrate over a standard Gaussian \(Z\). It is also continuous and integrable.

Throughout, our forward transform is \(\int e^{itx}g(x)\,dx\), with factor \(1/(2\pi)\) in the inverse integral. We do not yet know whether \(h\) comes from a probability, so nonnegativity of a density cannot be assumed in advance. First define the candidate function

\[
g_\varepsilon(x)=\frac1{2\pi}\int e^{-itx}h_\varepsilon(t)\,dt.
\]

Nonnegativity must be extracted from the finite quadratic forms we already have. Fix \(x\) and \(T>0\), partition \([-T,T]\) into \(N\) equal intervals of length \(\Delta_N=2T/N\), and choose a point \(u_j\) in each. In the positive definite quadratic form, take \(c_j=\Delta_N e^{-ixu_j}/\sqrt{2T}\). Then

\[
0\le\sum_{j,k=1}^N c_j\overline{c_k}\,h_\varepsilon(u_j-u_k)
=\frac{\Delta_N^2}{2T}\sum_{j,k=1}^N
e^{-ix(u_j-u_k)}h_\varepsilon(u_j-u_k).
\]

Every finite sum is real and nonnegative. The integrand is continuous on the compact square, and the right side is precisely a Riemann sum for the double integral. Letting \(N\to\infty\) therefore gives another real nonnegative number, denoted \(Q_T(x)\):

\[
0\le\frac1{2T}\int_{-T}^T\int_{-T}^T
e^{-ix(u-v)}h_\varepsilon(u-v)\,du\,dv
=\int_{-2T}^{2T}\left(1-\frac{|t|}{2T}\right)
e^{-ixt}h_\varepsilon(t)\,dt.
\]

The right side of the identity comes from the difference \(t=u-v\): when \(|t|\le2T\), the overlap of the two intervals has length \(2T-|t|\), leaving a triangular weight after division by \(2T\). This factor normalizes the position window; its role differs from the Fourier inverse factor \(1/(2\pi)\).

Now let \(T\to\infty\). The triangular weight tends pointwise to 1 and has modulus at most 1, while \(|h_\varepsilon|\) is integrable. Dominated convergence gives

\[
\lim_{T\to\infty}Q_T(x)
=\int_{\mathbb R}e^{-ixt}h_\varepsilon(t)\,dt
=2\pi g_\varepsilon(x)\ge0.
\]

The final nonnegativity follows because each \(Q_T(x)\) is nonnegative. Only after dividing by the positive number \(2\pi\) do we obtain \(g_\varepsilon(x)\ge0\). Positive definiteness has actually become nonnegativity of the candidate density; the name “inversion” did not grant it.

Total mass cannot be assigned by decree either. Another Gaussian window gives

\[
\int e^{-\delta^2x^2/2}g_\varepsilon(x)\,dx
=\int h_\varepsilon(t)\gamma_\delta(t)\,dt
\longrightarrow h_\varepsilon(0)=1.
\]

For every \(\delta>0\), integrability of \(h_\varepsilon\) and the position Gaussian justify interchange; continuity at zero gives the final limit. The left side increases as \(\delta\downarrow0\), so monotone convergence gives \(\int g_\varepsilon=1\). Reciprocity from Section 11.8 now shows that \(h_\varepsilon\) is genuinely a probability's characteristic function.

Finally take \(\varepsilon=1/n\). These genuine characteristic functions converge pointwise to \(h\), and \(h\) is continuous at zero. Lévy's theorem constructs a probability with characteristic function \(h\), and uniqueness says there is only one. Sufficiency is proved.

We did not use Bochner's theorem to prove Lévy's theorem and then cite it in reverse. Real-line tightness and distribution functions established continuity first; we then used it to construct probabilities from positive definite functions. Positive definiteness is no abstract ornament: it preserves “every mean squared modulus is nonnegative” in finite readings, ultimately forcing the inverse integral to be a nonnegative probability.

Gaussian smoothing runs through this entire route. In uniqueness, it turns two probabilities into smooth densities we can compare; in inversion, integrability permits removal of the smoothing factor. Here it first makes candidate readings integrable while preserving positive definiteness; only then does positive definiteness prove nonnegativity, and a Gaussian window prove total mass 1. The common mechanism damps high frequencies to obtain controlled integrals, then lifts the mist using established limit tools. Starting from an existing probability and starting from readings not yet realized still carry different proof obligations.

Bochner's 1933 paper *Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse* is one original source for this subject. The Gaussian smoothing proof above is our modern organization, not a claim to reproduce the paper's argument. [Original publication record](https://link.springer.com/article/10.1007/BF01452844)

## 11.19 After observation, frequencies can be conditional readings too

A conditional distribution kernel \(K(z,dx)\) from Chapter 10 can now be recorded as

\[
\Phi(z,t)=\int e^{itx}K(z,dx).
\]

For fixed \(t\), it is measurable in \(z\); for fixed \(z\), it is continuous in \(t\) and is a probability's characteristic function. Kernel integration also ensures

\[
\Phi(Z,t)=\mathbb E[e^{itX}\mid\sigma(Z)]
\quad\text{a.s.}
\]

Complex conditional expectations again treat real and imaginary parts separately. Observation does not change the definition of a frequency, but it may change every mean direction.

What if each rational-frequency conditional reading equals the unconditional \(\phi_X(t)\), almost everywhere? First merge exceptional sets over the countably many rationals. At every remaining observation value, continuity extends equality to all real frequencies. Uniqueness gives

\[
K(z,\cdot)=\mathcal L(X)
\quad\text{for }\mathcal L(Z)\text{-almost every }z.
\]

Substituting into the kernel integral for joint probabilities gives \(P(X\in A,Z\in C)=P(X\in A)P(Z\in C)\). Thus \(X\) and \(Z\) are independent. Conversely, independence makes the constant law a conditional kernel, so conditional readings remain unchanged.

This is much stronger than an unchanged conditional mean. An observation may leave one fair price unchanged while altering risk, tails and the prices of other payoffs. Only an unchanged sufficiently rich family of readings warrants saying that information has not changed this variable's world.

Again we need a common null set. We did not intersect separate almost-everywhere claims over uncountably many frequencies. We first merged the rational exceptions, then used each probability's continuity. Chapter 10's careful handling of versions now protects this new distribution-identification argument.

## Chapter 11 Epilogue: Hearing a bell curve is not yet watching a lifetime's record

The coins on the table once made us ask why an unrealized outcome could have a price today. Information later changed the price, and conditional distributions unfolded the world behind it. Now we have found another complete record of that world: rotate outcomes at different frequencies and observe their average directions.

Distant outcomes were not forbidden, nor atoms erased. Every probability leaves these bounded readings. Gaussian mist makes them invertible, lifting the mist restores the original world, and continuity near zero prevents mass escaping to infinity in a limit.

Chapter 3's curve finally has a new explanation. Independent addition becomes multiplication of frequency readings; finite variance leaves the same quadratic structure near zero. At square-root scale, many details recede and the Gaussian reading survives.

But readings identify a distribution. An infinite experiment's record still has questions of its own.

As one experimenter keeps tossing, how do earlier deviations accumulate? Can rare large jumps repeatedly disrupt an average? Does a random series really converge along almost every record? What can information left after every finite beginning decide?

We can now describe the shape of fluctuations after many experiments. Next we must ask what actually stabilizes as a lifetime's record keeps lengthening.

This time we must control more than an endpoint's distribution: we must control all deviations that can accumulate along the way.

## History and further reading

Fourier, *Théorie analytique de la Chaleur* (1822): [ETH digitized original](https://www.e-rara.ch/zut/doi/10.3931/e-rara-19706). This supports the historical connection between heat conduction and oscillatory analysis, not an attribution of modern probability's characteristic-function construction to the original book.

Bochner, *Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse*, *Mathematische Annalen* 108 (1933), 378–410: [original journal record](https://link.springer.com/article/10.1007/BF01452844). Our smoothing, positive-definiteness and continuity-theorem route is developed according to this book's own dependencies.

For a modern course entry into characteristic functions, Lévy's continuity theorem and the CLT, see the [MIT probability course](https://math.mit.edu/~sheffield/spring2014math175.html). The book's breadth continues to be compared with the [official contents of Kallenberg's third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1). This chapter proves the real-line uniqueness, inversion, tightness selection, continuity theorem and finite-variance i.i.d. CLT it uses. Weak convergence in general metric spaces, path-space tightness, triangular arrays and multivariate limits still require their own theories and cannot be replaced by the real-line results here.
