# Chapter 29: When Small Probabilities Become Exponentially Small — Large Deviations

A fair coin tossed n times lands heads every time with probability 2⁻ⁿ. This outcome is n/2 away from the expected number of heads. The central limit theorem identifies a width of order √n around the mean. It does not say whether its bell curve can be extended all the way to “every toss is heads.”

Extrapolating the local Gaussian quadratic exponent to that location gives a cost n/2, whereas the exact coin calculation gives n log 2. Both probabilities are small and exponentially decaying, but their ratio still grows or shrinks exponentially. For exceptionally rare events, “roughly small” is not nearly enough.

## 29.1 The Bell Curve Never Promised to Reach That Far

<a id="ldp-scales"></a>

Let Bᵢ be iid Bernoulli variables with 0<p<1, and write the head frequency as \(\overline B_n=n^{-1}\sum_{i=1}^n B_i\). For an upward deviation within the possible frequency range, take 0<a<1−p. At a=1−p the event is exactly all heads, with probability pⁿ; for a>1−p it is empty. The CLT controls fixed finite intervals for the standardized variable, whereas a fixed deviation in the interior range sends the threshold to infinity. Weak convergence does not control these escaping sets.

\[
\frac{\sqrt n(\overline B_n-p)}{\sqrt{p(1-p)}}\Rightarrow N(0,1),\qquad \{\overline B_n\ge p+a\}=\left\{\frac{\sqrt n(\overline B_n-p)}{\sqrt{p(1-p)}}\ge\frac{a\sqrt n}{\sqrt{p(1-p)}}\right\}.
\]

This is not a small defect in CLT accuracy: the scale of the question has changed. We fix a macroscopic deviation and increase the number of trials, asking the probability cost of sustaining it. Begin with the case where counting gives the cost directly.

## 29.2 The Cost of an Atypical Collection of Coins

Take 0<p<1, k heads and q=k/n. Multiply the number of placements of the heads by the probability of each record. Integral comparison gives log(n!)=n log n−n+O(log(n+1)). Applying this to k! and (n−k)!, with 0 log 0=0 at the endpoints, gives a uniform logarithmic error.

\[
\begin{aligned}\log P\{\overline B_n=q\}&=-nD(q\Vert p)+O(\log(n+1)),\\D(q\Vert p)&=q\log\frac qp+(1-q)\log\frac{1-q}{1-p},\qquad0\le q\le1.\end{aligned}
\]

The combinatorial factor rewards frequencies realizable in many orders; the original probability penalizes records departing from p. Their difference is the net cost. One cannot apply the probability of a single all-heads record to every frequency. A frequency interval contains at most n+1 terms, so its logarithm divided by n is governed by the least costly one; approximating an interior frequency by k/n gives the matching lower bound.

D vanishes at q=p. Its second-order Taylor expansion recovers the nearby Gaussian cost, while farther away it retains its nonquadratic shape. For a fair coin the cost at q=1 is exactly log 2. Gaussian theory meets this cost locally; neither replaces the other.

\[
D(p+a\Vert p)=\frac{a^2}{2p(1-p)}+o(a^2)\quad(a\to0),\qquad D(1\Vert1/2)=\log2.
\]

## 29.3 Why Logarithms Retain the Least Expensive Route

<a id="ldp-definition"></a>

Independent costs multiply and logarithms add them. Repeating an experiment at n-fold scale often multiplies its logarithmic cost by n. We therefore divide the logarithm of probability by a speed aₙ tending to infinity. At this scale a finite collection of alternative routes is governed by the largest probability.

\[
\max_{i\le r}b_{n,i}\le\sum_{i=1}^r b_{n,i}\le r\max_{i\le r}b_{n,i},\qquad a_n^{-1}\log r\longrightarrow0.
\]

We cannot demand the same limit for every event. A continuous law assigns zero probability to a point, yet its neighborhoods may have finite exponential cost; a boundary can also cut through attainable records. The large deviation principle preserves this distinction through open lower bounds and closed upper bounds.

Let Zₙ take values in a metric space S. A lower-semicontinuous I:S→[0,∞] is a rate function. The variables satisfy an LDP at speed aₙ with rate I if every open G and closed F satisfy the following bounds, with log 0=−∞ and the infimum over the empty set equal to infinity.

\[
-\inf_G I\le\liminf_n\frac1{a_n}\log P(Z_n\in G),\qquad \limsup_n\frac1{a_n}\log P(Z_n\in F)\le-\inf_F I.
\]

For a Borel event A, sandwich between its interior and closure. If their infimal costs agree, a logarithmic limit follows. I is not a density: it records neighborhood costs at a specified scale. Changing the scale or topology can change the answer.

## 29.4 Why a Rate Function Should Be Good

When minimizing the cost of a deviation, candidate records might escape to infinity without realizing their limiting cost. Compact finite-cost sublevel sets prevent that escape. Such a rate function is called good.

\[
\{x:I(x)\le L\}\text{ is compact for every finite }L.
\]

Goodness concerns the geometry of cost, not ordinary tightness of random variables. It gives convergent subsequences of bounded-cost approximate minimizers; lower semicontinuity retains their limiting cost. Contraction, closed-set neighborhood limits and path energy will all use this mechanism.

## 29.5 Ordinary Tightness Misses Exponential Escape

<a id="ldp-exponential-tightness"></a>

Let Zₙ equal zero with probability 1−1/n and n with probability 1/n. It converges in probability to zero and its laws are tight. Yet outside any fixed compact set the probability is still eventually 1/n. Its logarithm divided by n tends to zero, not an arbitrarily large negative number.

Exponential tightness requires, for each L>0, a compact Kᴸ whose escape probability has upper logarithmic rate at most −L. Ordinary tightness asks for small probability. Here it must be small fast enough at the scale under study.

\[
\limsup_n a_n^{-1}\log P(Z_n\notin K^L)\le-L.
\]

This is the missing control from local to global. Given open lower and compact upper bounds, split closed F into F∩Kᴸ and escape from Kᴸ. The finite-sum logarithmic rule bounds the result by max{−inf_F I,−L}; let L increase to get the closed upper bound. Ordinary tightness cannot supply this step.

## 29.6 How Costs Change When the Observation Changes

<a id="ldp-contraction"></a>

Given costs for full records, read only a continuous statistic Φ. Many records can yield the same value. The cost of a reading y should be the least cost among records producing it. This is the contraction principle.

\[
J(y)=\inf\{I(x):\Phi(x)=y\}.
\]

Assume I is good. On a nonempty fiber of finite infimal cost, a minimizing sequence has a convergent subsequence in an I-sublevel set. Continuity retains the fiber and lower semicontinuity retains the cost, so the minimum is attained. A J-sublevel is exactly the continuous image of an I-sublevel and is compact. Open and closed preimages and the original LDP prove both bounds for Φ(Zₙ).

Continuity matters. If Zₙ is normal with variance 1/n, let Φ(x)=1 exactly at zero and zero elsewhere. Then Φ(Zₙ) is always zero. The formal fiber formula would give cost I(0)=0 at y=1, contradicting the open lower bound. A discontinuity at one point can invalidate a formal contraction.

## 29.7 Making Rare Samples Typical Under Another Law

<a id="ldp-tilting"></a>

When coin frequencies depart from p toward q, they are typical if observed under a coin whose head probability is q. We can use a law of large numbers under that law and then restore the original record weights. For random vectors, multiply by an exponential linear weight and divide by its normalizer.

\[
\Lambda(\theta)=\log\int e^{\langle\theta,x\rangle}\mu(dx),\qquad \mu_\theta(dx)=e^{\langle\theta,x\rangle-\Lambda(\theta)}\mu(dx)\quad(\Lambda(\theta)<\infty).
\]

For a finite sample the old and new weights differ by an exponential determined by the sample mean. If the tilted mean is the target x, its neighborhood has probability tending to one under the tilted law, at cost θ·x−Λ(θ). Chernoff gives the same expression from above. Tilting is where upper and lower bounds meet, not merely a computational trick.

Cramér published his work on deviations of sums in 1938. Our finite-dimensional and entropy method is a modern reconstruction, not a claim to reproduce his original proof order. The important difficulty is that not every x is a tilted mean. Proving only parameter-matched points does not prove the general theorem.

## 29.8 The Information Cost of Replacing a Distribution

<a id="ldp-entropy"></a>

To avoid being confined to one exponential family, allow any replacement law ν whose mean is near the target. If ν is absolutely continuous with respect to μ, its density ρ records each sample’s reweighting. For typical ν-samples, the mean log weight tends to the following quantity; n independent observations pay n times that cost.

\[
H(\nu\mid\mu)=\int\rho\log\rho\,d\mu=\int\log\rho\,d\nu\quad(\nu\ll\mu),\qquad H(\nu\mid\mu)=\infty\quad(\nu\not\ll\mu).
\]

Use 0 log 0=0. There is no infinity-minus-infinity ambiguity: r|log r|≤1/e for 0<r<1. Integrating r log r−r+1≥0 gives H≥0, with equality only when ν=μ. The logarithm arises from multiplying independent likelihoods, not from arbitrarily choosing a distance. Relative entropy is asymmetric and is not a metric.

For coins this returns exactly D(q∥p). For general means we seek the cheapest replacement law realizing that mean. It need not exist, and an unbounded mean constraint need not be closed under weak convergence. The proof therefore retains the closure of nearby means instead of assuming an optimal tilt always exists.

## 29.9 Cramér’s Theorem: From Local Exponential Bounds to the Whole Space

<a id="ldp-cramer"></a>

Let Xᵢ be iid vectors in Rᵈ with law μ, and assume Λ is finite on an open neighborhood of zero. Their sample means satisfy an LDP at speed n with the following good rate function. Laws supported on a proper affine subspace are included; no nonsingular covariance is required.

\[
I(x)=\Lambda^*(x)=\sup_{\theta\in\mathbb R^d}\{\langle\theta,x\rangle-\Lambda(\theta)\}.
\]

First prove the upper bound. For fixed x and finite Λ(θ), a sample mean in its δ-ball has scalar product at least θ·x−|θ|δ. Exponential Markov and independence give the following estimate. Choose θ approaching I(x) and use finite covers for compact upper bounds. If I(x) is infinite, choose arbitrarily large finite targets.

\[
P\{\overline X_n\in B(x,\delta)\}\le\exp\{-n[\langle\theta,x\rangle-|\theta|\delta-\Lambda(\theta)]\}.
\]

Exponential moments near zero extend the result to noncompact closed sets. Choose positive η with finite Λ at ±ηeⱼ; coordinate Chernoff bounds control escape from a large cube. The same tests bound the sublevel sets of I. As a supremum of continuous affine functions I is lower-semicontinuous. Thus goodness and exponential tightness are established separately.

\[
P(\|\overline X_n\|_\infty>R)\le2d\,e^{-n(\eta R-C)},\qquad I(x)\ge\eta\|x\|_\infty-C,\quad C=\max_{j,\pm}\Lambda(\pm\eta e_j).
\]

## 29.10 The Lower Bound Must Survive Missing Tilt Parameters

Take ν with finite first moment and finite entropy, whose mean x belongs to open G. A law of large numbers places its sample mean in G. Its log density is integrable, so another law places the mean log weight near H. Restore μ-weights only on this typical event to obtain the open lower bound.

\[
\mu^{\otimes n}(\overline X_n\in G)\ge e^{-n(H(\nu\mid\mu)+\delta)}\nu^{\otimes n}\!\left(\overline X_n\in G,\ \frac1n\sum_{i=1}^n\log\rho(X_i)\le H(\nu\mid\mu)+\delta\right).
\]

The probability in parentheses tends to one. The relation is an inequality, not always equality: ν may vanish on sets with positive μ-mass. This is a finite-product change of measure, not a density between infinite sample laws, where such a density often does not exist.

\[
J(x)=\inf\{H(\nu\mid\mu):\int|y|\nu(dy)<\infty,\ \int y\nu(dy)=x\}.
\]

The open lower bound is therefore −inf_G J. We still must identify it with I. Mixtures and convexity of r log r make J convex, but not necessarily closed. The entropy inequality bounds its convex conjugate by Λ. Conversely truncate an exponential tilt to a large ball: samples are bounded, entropy is finite, and the normalizer increases to the moment generating function. This proves that the conjugate of J is exactly Λ.

Nearest-point separation of finite-dimensional closed convex epigraphs then proves that the lower-semicontinuous closure of J equals the conjugate of Λ; no unproved variational principle is invoked. Closing J does not change its infimum on an open set, since nearby means eventually remain in that set. [T-LDP](../foundations/t-ldp.md#t-ldp-cramer-lower) gives the separation, truncation and limit order in full. The general lower bound follows, including missing-tilt boundary and degenerate cases.

## 29.11 A Gaussian Limit Is Not the Required Tail Condition

For a normal law Λ is linear plus quadratic, giving a quadratic cost about the mean. For a Poisson law with parameter λ>0 the cost is x log(x/λ)−x+λ for x≥0, infinity for negative x, and λ at zero by continuity. These are deviations of means with different global costs. The full exponential reading of the law, not merely its variance, determines the answer.

Finite variance cannot replace exponential moments. Take a nonnegative Pareto variable with tail x⁻ᵝ for x≥1 and β>2. It satisfies a finite-variance CLT, yet one variable exceeding na suffices to push the sample mean above a. For a above the true mean, the following probability has no strictly positive cost at speed n.

\[
P(\overline X_n>a)\ge P(X_1>na)=(na)^{-\beta},\qquad \lim_{n\to\infty}\frac1n\log P(\overline X_n>a)=0.
\]

The displayed lower bound and probability at most one give the equality. A single large jump realizes the deviation, making this exponential scale lose discrimination. If all Xᵢ equal one nondegenerate Y, their mean stays Y; identical marginal laws cannot replace independence either.

Even with exponential moments, ordinary tilting need not reach every target. For density proportional to e⁻ˣ(1+x)⁻³ on x≥0, the parameter reaches only θ=1. The endpoint tilt has density 2(1+x)⁻³ and mean one; larger targets lie outside the tilted-mean range. The preceding closure argument preserves the lower bound at these points rather than excluding them from the theorem.

## 29.12 When the Entire Empirical Distribution Deviates

<a id="ldp-sanov"></a>

A mean compresses many records into one number. Samples with the same mean may concentrate near the center or at two extremes. To ask whether data resemble another distribution, retain their empirical measure, assigning mass 1/n to each observation, instead of inventing a separate theorem for every statistic.

\[
L_n=\frac1n\sum_{i=1}^n\delta_{X_i}\in\mathcal P(E).
\]

Let E be Polish and μ any common law. Use Chapter 24’s weak topology, reading integrals of bounded continuous functions; a basic neighborhood constrains finitely many readings. Sanov’s theorem says Lₙ satisfies an LDP at speed n with good rate H(·|μ). No moment generating function or finite state space is required.

Finite alphabets suggest the answer through multinomial counting: each type has log probability equal to minus n times its discrete relative entropy, up to logarithmic error. Infinite spaces do not provide finitely many types to count. We must organize all continuously readable local evidence into entropy.

## 29.13 Why Entropy Is the Strongest Exponential Test

<a id="ldp-entropy-variational"></a>

\[
H(\nu\mid\mu)=\sup_{f\in C_b(E)}\left\{\int f\,d\nu-\log\int e^f\,d\mu\right\}.
\]

Each f supplies testable evidence: samples resembling ν should have f-average near νf. Exponential Markov measures the rarity of that evidence by its exponential mean under μ. Taking every test says that entropy is not an added penalty, but the strongest exponential cost supplied jointly by bounded continuous evidence.

The identity needs proof. First allow bounded Borel tests. Re-normalizing μ by eᶠ and using nonnegative entropy bounds each test by H. Truncating logρ to [−M,M] and letting M increase gives the reverse inequality. If ν charges a μ-null set, M times its indicator makes the supremum infinite. Finally approximate bounded Borel functions in L¹(μ+ν) by equally bounded continuous functions. The exponential is Lipschitz on a fixed bounded interval, allowing replacement by C_b. [T-SANOV](../foundations/t-sanov.md#t-sanov-entropy) proves the approximations and their limit order.

Each test is weakly continuous, so H is lower-semicontinuous. Finite entropy also limits mass placed in regions rare under μ. For 0<p=μ(A)<1, use the test log(1/p) times its indicator to obtain the tail control.

\[
\nu(A)\le\frac{H(\nu\mid\mu)+\log2}{\log(1/\mu(A))}.
\]

Tightness of μ makes μ(Kᶜ) arbitrarily small, so the bound gives uniform tightness of entropy-bounded ν. Chapter 24’s Prokhorov theorem and lower semicontinuity make entropy sublevels compact. This proves goodness rather than merely suggesting a cost.

## 29.14 How Sanov’s Two Bounds Meet at the Same Cost

Fix ν and b<H(ν|μ). Choose a continuous test with νf−log μeᶠ>b. This persists in a weak neighborhood, while independence gives the exact exponential moment below. Exponential Markov bounds its probability by e⁻ⁿᵇ; finite compact covers give the compact upper bound.

\[
E_\mu e^{nL_nf}=\left(\int e^f\,d\mu\right)^n.
\]

For finite-entropy ν in open G, observe ν-samples. Laws of large numbers for finitely many continuous readings place Lₙ in G; a law for logρ controls the cost of returning to μ. The same finite-product inequality as for means gives −H. Minimize over ν for the open lower bound. Full support is not required; this does not make the two infinite sample measures equivalent.

The closed upper bound remains. Ordinary tightness of empirical measures is not enough. Given L>0, choose δⱼ=2⁻ʲ and compact Kⱼ with extremely small μ-tails: set θⱼ=(L+j+1)/δⱼ and μ(Kⱼᶜ)≤e⁻ᶿʲ. Requiring every tail mass to be at most δⱼ defines a weakly closed uniformly tight, hence compact, set of measures. Chernoff for the Bernoulli tail counts bounds failure of constraint j by e⁻ⁿ⁽ᴸ⁺ʲ⁾; the infinite union is still at most e⁻ⁿᴸ. The calculation covers even nδⱼ<1.

Intersect the closed set with this compact set and discard the exponentially negligible remainder to complete Sanov. [T-SANOV](../foundations/t-sanov.md#t-sanov-proof) gives parameter choices, weak closedness and infinite sums. The 1957 original paper must be distinguished from this modern Polish-space organization.

## 29.15 An Empirical Law Does Not Make Every Statistic Continuous

Sanov retains more information than a mean, but weak contraction cannot directly give deviations of arbitrary unbounded means. The laws νₘ=(1−1/m)δ₀+(1/m)δₘ converge weakly to δ₀ while their means remain one. A little mass escapes to infinity, vanishing from bounded continuous readings while carrying the entire mean.

Cramér’s exponential moments control such tail contributions. We proved the mean and empirical-measure theorems separately instead of hiding a discontinuous statistic inside contraction. For a bounded continuous payoff f, contraction is legitimate: the cost of its mean reading y is the least entropy among laws with νf=y.

## 29.16 Every Finite Record Can Behave Normally While Paths Escape

<a id="ldp-path-obstruction"></a>

Now replace an empirical record by a whole motion. Finite-dimensional exponential estimates are still insufficient. On [0,T] let hₙ be a deterministic triangular spike of height one centered at T/(n+1), supported within distance T/[3(n+1)] of its center and zero outside. At each fixed t its value is eventually zero. Every finite-dimensional record therefore has a trivial LDP charging zero cost only to the zero vector.

Yet the paths have no uniformly convergent subsequence, and their point masses are not exponentially tight. The set {hₙ:n≥1} is closed and separated from the zero path, with probability always one. A full path upper bound based on the zero-path rate would incorrectly be minus infinity. No finite-dimensional calculation is wrong; together they miss increasingly narrow oscillations.

Chapter 24 required shared oscillation control for weak path limits. At a large-deviation scale its failure probability must also be exponentially small enough. Simply carrying over a “small probability” from ordinary tightness is insufficient.

## 29.17 Shrinking Noise and Reading an Atypical Brownian Path

<a id="ldp-schilder"></a>

Fix T>0 and a standard d-dimensional Brownian motion B. Study √ε B as ε decreases to zero. Typical paths approach zero uniformly, but reaching a neighborhood of a nonzero continuous curve is not impossible. We use the uniform norm on continuous paths starting at zero, writing this space as \(\mathcal C_T\), distinct from Chapter 28’s C₀ of functions vanishing at infinity.

\[
\mathcal C_T=\{h\in C([0,T];\mathbb R^d):h(0)=0\},\qquad X^\varepsilon=\sqrt\varepsilon B,\qquad a_\varepsilon=\varepsilon^{-1}.
\]

Schilder’s theorem gives total squared velocity as the good rate. A continuous path without a square-integrable velocity representation has infinite cost. Absolute continuity is essential: a continuous path can concentrate variation on a Lebesgue-null set, a hidden motion that finite energy cannot permit.

\[
I_T(h)=\begin{cases}\displaystyle\frac12\int_0^T|g(s)|^2\,ds,&h(t)=\displaystyle\int_0^tg(s)\,ds,\ g\in L^2([0,T];\mathbb R^d),\\\infty,&\text{otherwise}.\end{cases}
\]

This is not a path theorem obtained merely by guessing from a Gaussian squared exponent. We must calculate energy on grids, prove that the grids retain every finite-cost path, and control motion missed between observations.

## 29.18 From Gaussian Increments to Polygonal Path Costs

Take m equal intervals of length Δ=T/m and let Πₘ interpolate grid values linearly. The independent increment density has the following exponent. Its prefactor, a power of ε, disappears after taking logarithms and multiplying by ε. Each squared displacement is divided by its elapsed time, not simply summed without time weights.

\[
E_m(h)=\frac12\sum_{j=1}^m\frac{|h(j\Delta)-h((j-1)\Delta)|^2}{\Delta}.
\]

A density lower bound on an open ball gives the open lower bound; volume times the maximal density gives compact upper bounds. An exponential moment of a Gaussian square controls distant points and completes noncompact closed bounds. The continuous finite-dimensional polygonal embedding gives the full LDP of ΠₘXε: energy Eₘ on that polygonal subspace and infinity off it. [T-SCHILDER](../foundations/t-schilder.md#t-schilder-grid) supplies this density proof rather than substituting a CLT or ordinary weak convergence.

## 29.19 Why Grid Energies Force a Square-Integrable Velocity

<a id="ldp-energy"></a>

Use nested dyadic grids m=2ᵏ. Cauchy–Schwarz shows that refinement cannot decrease energy. Let vₖ be the piecewise constant velocity of Π₂ᵏh. Its finer counterpart averages to the coarse velocity in each coarse cell, giving the orthogonal difference identity.

\[
\|v_\ell-v_k\|_2^2=\|v_\ell\|_2^2-\|v_k\|_2^2\quad(\ell\ge k),\qquad\|v_k\|_2^2=2E_{2^k}(h).
\]

Bounded grid energies make the right side tend to zero as k and ℓ increase, so the velocities are Cauchy in L². Completeness established before Chapter 15 gives a limit g. The uniform integration error is at most √T times the L² error. Since the polygons also converge uniformly to h, we obtain h(t)=∫g. This genuinely excludes continuous but non-absolutely-continuous paths.

Conversely, if h=∫g with g in L², Jensen for cell averages bounds the energies by its squared integral. The same Cauchy argument gives a velocity limit whose integral to every t is h. Measure uniqueness identifies it with g almost everywhere. This gives an exact identification, not merely a one-sided estimate.

\[
I_T(h)=\sup_{k\ge0}E_{2^k}(h).
\]

Each grid energy is continuous, so I is lower-semicontinuous. I≤L also gives the common oscillation bound below; Arzelà–Ascoli makes its sublevel compact. Finite cost permits neither unbounded motion nor fixed-height spikes of arbitrarily small width.

\[
|h(t)-h(s)|\le\sqrt{2L}\,|t-s|^{1/2},\qquad\|h\|_\infty\le\sqrt{2LT}\quad(I_T(h)\le L).
\]

## 29.20 The Missed Motion Must Be Rarer Than the Target Event

<a id="ldp-exponential-approximation"></a>

On each interval the Brownian path’s difference from its chord is at most twice its maximal increment from the left endpoint. If a Euclidean d-dimensional error exceeds δ, some coordinate exceeds δ/√d. Chapter 26’s reflection tail and union bounds over coordinates and intervals give the following estimate, without assuming independent bridges.

\[
P\{\|X^\varepsilon-\Pi_mX^\varepsilon\|_\infty>\delta\}\le4dm\exp\!\left\{-\frac{\delta^2m}{8dT\varepsilon}\right\}.
\]

Let ε decrease first and then m increase. The error event can be assigned arbitrarily large exponential cost: this is an exponentially good approximation. For one fixed m the error is not automatically superexponentially small. The order of limits matters, and a fixed-grid approximation is not automatically exponentially equivalent to the path.

Ordinary approximation only makes the error probability tend to zero; it may remain much larger than the target e⁻ᶜ⁄ᵋ. We need a rarer error before subtracting it from the probability that a polygon approaches the target. This is real additional work beyond weak path convergence.

## 29.21 Turning All Grid Costs into a Path Theorem

First establish path exponential tightness, not as a synonym for ordinary tightness. Given L>0 choose δⱼ→0 and increasingly fine dyadic mⱼ so that δⱼ²mⱼ/(8dT), with the prefactor 4dmⱼ accounted for, is sufficiently large. Require a uniform path bound and distance at most δⱼ from its polygon for every j. Bounded polygons on each fixed grid form a compact set. Errors δⱼ→0 give total boundedness; the constraints are closed and the space complete, hence compact.

The preceding estimate and the Brownian maximal tail make the infinite union of constraint failures decay at any prescribed exponential rate. Its prefactors grow with j and must be absorbed when choosing mⱼ, not ignored term by term in an infinite sum. The companion supplies explicit parameters.

For compact K, membership of Xε in K implies its projection lies in ΠₘK. The finite-dimensional upper bound gives −inf_K Eₘ. Dyadic energies increase, and compactness allows refinement to commute with taking the infimum: otherwise a cluster point of low-energy candidates would contradict the limiting energy bound. This gives −inf_K I. Exponential tightness extends it to every closed set.

For finite-energy h in open G choose a ball contained in G. Select a sufficiently fine but fixed grid so Πₘh is close to h and the failure cost strictly exceeds I(h). The polygonal neighborhood costs at most Eₘ(h)≤I(h). Subtracting the exponentially smaller error retains that lower bound. Optimize over h to complete Schilder, not only its finite-dimensional part.

[T-SCHILDER](../foundations/t-schilder.md#t-schilder-full) writes out the exponential compact sets, limit order and subtraction lemma in full. No Girsanov theorem, stochastic integral or unproved path variational principle is used.

## 29.22 Which Errors Are Negligible at the Exponential Scale?

<a id="ldp-exponential-equivalence"></a>

Variables Zₙ and Yₙ on the same space are exponentially equivalent at speed aₙ if, for every positive δ, their distance exceeds δ with probability decaying faster than every e⁻ᴸᵃⁿ. This is a precise condition for changing an approximation without changing its LDP.

\[
\limsup_n a_n^{-1}\log P\{d(Z_n,Y_n)>\delta\}=-\infty\qquad(\delta>0).
\]

If Zₙ has an LDP with good rate I, Yₙ has the same LDP. Bound a closed F by the probability that Zₙ lies in its closed δ-neighborhood plus the error, then let δ decrease. Goodness makes the neighborhood infima converge to the infimum on F: bounded-cost candidates have a convergent subsequence whose vanishing distance forces its limit into F. The neighborhoods themselves need not be compact.

For the open lower bound use a ball inside G and subtract the superexponentially small error via the preceding subtraction lemma. See [T-LDP](../foundations/t-ldp.md#t-ldp-equivalence) for the proof. In Schilder’s construction a grid m(ε) tending to infinity gives exponential equivalence by the explicit tail bound. Our fixed-grid proof first established the path LDP independently, without circular reasoning.

## 29.23 When Probabilities Become Exponential Integrals

<a id="ldp-laplace-principle"></a>

If records cost I but an observer rewards them by exp(aₙΦ), reward and cost subtract on the logarithmic scale. An LDP yields the following Laplace formula, initially restricted precisely to bounded continuous Φ.

\[
\lim_n a_n^{-1}\log E e^{a_n\Phi(Z_n)}=\sup_x\{\Phi(x)-I(x)\}.
\]

For the lower bound use a small open neighborhood where Φ≥Φ(x)−δ and the LDP lower bound. For the upper bound split its bounded range into finitely many bins of width δ. Bound each contribution by the exponential at the upper endpoint times P(Φ≥the lower endpoint), a closed event. The finite-sum rule gives at most sup(Φ−I)+δ. Let δ decrease. This proves the variational formula rather than assuming it.

An unbounded Φ needs additional exponential tail control. Just as an unbounded mean cannot be contracted weakly without further work, exponential rewards can let tiny masses far away dominate the answer.

## 29.24 How Squared Energy Answers a Concrete Crossing Question

For one-dimensional Brownian small noise, require reaching a positive height b before T. If a finite-energy path reaches b at s≤T, Cauchy–Schwarz gives energy at least b²/(2s), hence b²/(2T). The straight line h(t)=bt/T attains the infimum. The maximum is a continuous uniform-topology reading; the open event maximum>b and closed event maximum≥b have the same infimal cost: take \(h_\eta(t)=(b+\eta)t/T\) and let η decrease to zero to approach that cost from the open side.

\[
\lim_{\varepsilon\downarrow0}\varepsilon\log P\left\{\sup_{t\le T}\sqrt\varepsilon B_t\ge b\right\}=-\frac{b^2}{2T}.
\]

Chapter 26’s reflection formula gives the same exponent, but energy now reveals a transferable mechanism: uniform velocity minimizes squared cost for a prescribed displacement in finite time. This does not assert pathwise convergence of conditioned trajectories to a line, or identify probability cost with physical dissipation. Such claims require additional models and results.

It also explains why differentiating every sample path would be wrong. Brownian paths remain rough and almost surely outside the finite-energy class at every ε. Finite-energy paths describe the costs of rare neighborhoods; Brownian samples have not suddenly acquired differentiability.

## 29.25 The Scales of the Typical and the Rare

All-heads records do not violate the law of large numbers, and distant deviations do not refute the CLT. They demand a different scale. Logarithms turn products of independent weights into additive costs; minimization asks which alternative records can realize the same deviation.

Exponential tilting and convex closure identify the cost of means. Relative entropy prices changing an entire empirical law. Squared energy survives refinement of continuous Gaussian records. These are not three unrelated formulas: each seeks an observation under which rare records become analyzable, while accounting faithfully for the reweighting cost.

The common structure does not erase the distinctions. Finite-dimensional laws do not replace paths, weak tightness does not replace exponential tightness, small errors need not be exponentially negligible, and finite variance does not replace the needed tail conditions. Only after constructing a path can its geometry support such extreme questions.

If we move beyond observing completed paths and act while motion unfolds, using only information already seen, function spaces and distributions no longer suffice. Which information is currently available and which quantities can be chosen before the next noise arrives become mathematical data. A different necessity remains: not only to describe a motion, but to specify precisely what can be known when within it.

### Sources and Scope

Cramér’s 1938 paper can be checked through its [attributed translation and original publication information](https://arxiv.org/abs/1802.05988). See [Sanov’s 1957 journal archive](https://www.mathnet.ru/eng/sm/v84/i1/p11) and [the institutional archive for Schilder’s 1966 paper](https://research.ibm.com/publications/some-asymptotic-formulas-for-wiener-integrals), which retains the title and original-paper link. Modern proofs were compared with [Varadhan’s author notes](https://math.nyu.edu/faculty/varadhan/LDP/Spring2010.3.pdf). Our narrative and proof organization are independent modern reconstructions, not claims that all three originals used today’s Polish-space, convex-closure and grid arguments in this form.

The proved scope is finite-dimensional iid Cramér under exponential moments near zero, Sanov in the Polish weak topology, Schilder for standard d-dimensional Brownian motion on a finite time interval with the uniform topology, and contraction, exponential equivalence and the bounded continuous Laplace formula under the stated assumptions. Deviations of general dynamics, Freidlin–Wentzell for small-noise SDEs and unbounded exponential rewards do not follow automatically and require their own prerequisites.
