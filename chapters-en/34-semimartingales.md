# Chapter 34: When Continuous Motion and Jumps Meet — Semimartingales and Jump Integration

Refining a record of prices, population or an instrument reading does not divide a genuine shock into many small changes. Immediately before the jump the value is x; the next value is x+z. A square changes by a term involving z², and a cube also leaves z³. The time mesh tends to zero, but this z does not.

For continuous paths, second-order variation survives while higher remainders disappear. That was a theorem, not a convention obeyed by every random motion. We must retain shocks that do not shrink, while still controlling the accumulation of infinitely many small jumps.

## 34.1 One Jump Already Changes the Chain Rule

<a id="jump-cubic"></a>

Before introducing any new process, compare the values immediately before and after one jump. The cubic identity is

\[ (x+z)^3-x^3=3x^2z+3xz^2+z^3. \]

Chapter 32 discarded the final term for continuous paths because the largest increment vanished while the sum of squared increments stayed controlled. A jump of fixed size invalidates that argument. Its entire nonlinear change must be retained instead of being called a small remainder.

\[ R_f(x,z)=f(x+z)-f(x)-f^\prime(x)z,\qquad |R_f(x,z)|\le C_Kz^2\quad(|x|,|x+z|\le K). \]

The quadratic bound is Taylor’s integral remainder for a C² function on a compact set. It does not approximate a large jump by a quadratic polynomial. It explains why sufficiently small jumps can have a summable total correction. Finitely many large jumps and summable squared small jumps will serve different purposes.

## 34.2 The Rule Is Chosen Before the Vertical Line

<a id="jump-predictable"></a>

Let N be a Poisson count of rate λ. If each arrival carries a payment H selected beforehand, accumulation must use the value available before arrival. Using N₋ rather than the just-updated N changes the total by one full unit at each arrival. Refining time does not remove that difference.

\[ \sum_{s\le t}N_{s-}\Delta N_s=\frac{N_t^2-N_t}{2},\qquad \sum_{s\le t}N_s\Delta N_s=\frac{N_t^2+N_t}{2}. \]

Chapter 30 encoded this order in the predictable sigma-algebra. We use it without retelling the arrival story. The new task is to prove that rules chosen beforehand define one integral across continuous noise and infinitely active small jumps. Filtrations satisfy the usual conditions, paths are càdlàg, and the initial value at time zero is kept separate from the jump measure.

## 34.3 Not Every Fair Shock Starts in L²

<a id="jump-heavy-shock"></a>

An amount Y is revealed at time one. Its mean is zero and its absolute value is integrable, but its square is not. Information is trivial before one and reveals Y afterwards. The process M, zero before one and equal to Y afterwards, is conditionally fair. Its path has only one jump.

\[ M_t=Y\mathbf1_{[1,\infty)}(t),\qquad E|Y|<\infty,\quad EY=0,\quad EY^2=\infty. \]

It is not locally square-integrable. For a localizing sequence eventually passing one, the event of not stopping before one belongs to the trivial pre-revelation information and cannot select according to Y. Some stopped process must retain the whole Y with probability one, leaving an infinite second moment. The continuous-martingale argument of stopping at amplitude n fails because the jump can overshoot every bound.

Integration against this process is easy: it has finite variation and the integral is a jump sum. The problem is not that the process is unusable. Square energy alone is too narrow a description of integrators. We need both martingale cancellation and pathwise finite variation.

## 34.4 Putting Two Kinds of Control in One Object

<a id="jump-semimartingale"></a>

An adapted càdlàg process X is a semimartingale if it is the sum of its initial value, a local martingale and an adapted finite-variation process. The finite-variation term is not initially required to be predictable. This matters for including the heavy-tailed shock just encountered.

\[ X=X_0+M+A,\qquad M_0=A_0=0,\qquad \operatorname{Var}(A)_t<\infty\quad(t<\infty). \]

The decomposition need not be unique. N is the compensated martingale N−λt plus λt, but N itself may instead be placed in the finite-variation term. Their difference is both a local martingale and finite variation. Chapter 31’s assertion about continuous finite-variation local martingales remains correct; continuity was essential.

A crucial decomposition makes the definition usable: every càdlàg local martingale is the sum of a local martingale with deterministically bounded jumps and a finite-variation local martingale of locally integrable variation. Thus a semimartingale can be represented by a locally square-integrable martingale plus finite variation, although its original martingale component need not be locally square-integrable.

The mechanism is visible: extract the sum J of jumps larger than one and subtract its predictable compensator Jᵖ. The remaining martingale jumps by a small jump plus a compensator jump; conditional fairness at predictable times bounds the latter too. Stopping at an amplitude now overshoots by at most a bounded jump, giving genuine square integrability. [Proof 1](../foundations/t-jump-calculus.md#t-jump-localization) supplies jump-count measurability, locally integrable variation and the compensator-jump bound.

## 34.5 Two Different Readings of Squared Change

<a id="jump-two-brackets"></a>

For a square-integrable martingale, Doob–Meyer still extracts a unique predictable accumulation from M², denoted by the angle bracket. It controls the mean square error of rules chosen beforehand. It need not equal the squared jumps actually observed along a path.

\[ M=N-\lambda t:\qquad [M]_t=N_t,\qquad\langle M\rangle_t=\lambda t. \]

The arrival count records what happened; λt is its predictable compensator relative to the information. Subtracting either from M² gives a local martingale, so this condition alone does not identify the square bracket. That bracket must be constructed from squared-increment sums and must have the actual squared jumps. The difference between the brackets can itself be a nonzero finite-variation martingale.

## 34.6 Complete the Simple Integral Before Taking Limits

<a id="jump-integral"></a>

First let M be an L²-martingale on a finite horizon. A simple predictable H uses a coefficient known in Fₛ on each interval (s,t]. Increments over different intervals are orthogonal in expectation, and the angle bracket reads their conditional second moments. Thus

\[ (H\cdot M)_t=\sum_i H_i(M_{t\wedge t_{i+1}}-M_{t\wedge t_i}),\qquad E|(H\cdot M)_T|^2=E\int_{(0,T]}H_s^2\,d\langle M\rangle_s. \]

The clock may now jump, but predictable rectangles remain dense in the associated L² space. Isometry extends terminal values; Doob lifts terminal convergence to the L² maximal norm. A summable subsequence converges uniformly, giving a càdlàg integral rather than an incorrectly asserted continuous one. [Proof 2](../foundations/t-jump-calculus.md#t-jump-l2) establishes density, random-clock localization and uniqueness of versions.

For X=X₀+M+A add the martingale integral and the pathwise Stieltjes integral. Every locally bounded predictable H is integrable this way. Unbounded H requires specified square-energy and variation integrability; predictability alone is not an integrability condition.

\[ H\cdot X=H\cdot M+\int H_s\,dA_s,\qquad \int H^2d\langle M\rangle<\infty,\quad\int |H|d\operatorname{Var}(A)<\infty\quad\text{locally}. \]

## 34.7 Different Decompositions Must Give the Same Integral

<a id="jump-independent"></a>

For two decompositions of the same X, simple integrals plainly agree. The predictable-integrand limits must agree too. Saying continuity alone is insufficient unless approximations in the two different energy spaces are compatible.

After common localization put both martingale clocks and both path-variation measures into one control measure. A strictly positive path weight makes the averaged variation measure finite when its unweighted expectation is infinite. This is an approximation device, not a change of probability used to prove a martingale. Simple predictable rectangles approximate all controls simultaneously, so both integrals have the same ucp limit. Càdlàg versions are indistinguishable. [Proof 3](../foundations/t-jump-calculus.md#t-jump-independence) also proves stopping and associativity.

\[ \Delta(H\cdot X)_t=H_t\Delta X_t,\qquad K\cdot(H\cdot X)=(KH)\cdot X,\qquad (H\cdot X)^\tau=(H\mathbf1_{(0,\tau]})\cdot X. \]

These identities are first proved for locally bounded predictable processes. Extension to the declared energy/variation class requires checking each integral. In particular X₋ is predictable and pathwise locally bounded, so the integrals needed for products are already well-defined.

## 34.8 Constructing Rather Than Guessing Quadratic Variation

<a id="jump-quadratic"></a>

The square identity remains exact on every deterministic partition. Sending the left-step values to M₋ through integral completeness constructs a càdlàg process Q.

\[ \sum_i(M_{t_{i+1}\wedge t}-M_{t_i\wedge t})^2=M_t^2-M_0^2-2\int_0^t M_s^{\pi}\,dM_s\xrightarrow{ucp}[M]_t. \]

The proof must not depend on nested grids. Left-step processes approach from strictly before each time, and dominated convergence in the localized square clock works for arbitrary deterministic partitions of vanishing mesh. Insert any two rational endpoints; the intervening square sum is nonnegative, so Q is increasing. Right continuity extends monotonicity to all times. Jumps are read from the simple-integral limit.

\[ \begin{aligned}[M]&=M^2-M_0^2-2M_-\cdot M,\\\Delta[M]_t&=(\Delta M_t)^2,\\M^2-\langle M\rangle,\quad M^2-[M]&\quad\text{are local martingales}.\end{aligned} \]

Adding finite variation removes continuous finite-variation cross terms but retains jump products. This establishes brackets, polarization and the product formula for general semimartingales. [Proof 4](../foundations/t-jump-calculus.md#t-jump-quadratic) handles ucp convergence, localization and variation integrals, rather than changing a symbol in the old continuous formula.

\[ XY-X_0Y_0=X_-\cdot Y+Y_-\cdot X+[X,Y],\qquad \Delta[X,Y]=\Delta X\Delta Y. \]

## 34.9 A Purely Discontinuous Martingale Can Move Between Jumps

<a id="jump-decomposition"></a>

If purely discontinuous meant constant between jumps, a compensated Poisson martingale would already be a counterexample. It declines along −λt while waiting, yet has no continuous martingale noise. The relevant distinction is its continuous local-martingale component, not whether the graph contains sloping segments.

In the L² terminal-value space project onto the closed subspace of continuous martingales. Doob’s maximal estimate proves closure: an L²-convergent terminal sequence has a uniformly convergent subsequence of paths, still continuous. The orthogonal remainder is strongly orthogonal to every continuous local martingale: their product is a local martingale. Localization glues the projections into a unique decomposition.

\[ M=M^c+M^d,\qquad [M^c,M^d]=0,\qquad [M]=[M^c]+\sum_{s\le\cdot}(\Delta M_s)^2. \]

The last identity does not follow from projection alone. Extract and compensate actual jumps larger than ε, and use the tail of their squared sizes to prove L² Cauchy convergence. The limit retains every jump of M, leaving a continuous remainder. This also proves that the purely discontinuous part has no hidden continuous quadratic variation. [Proof 5](../foundations/t-jump-calculus.md#t-jump-continuous-part) supplies conditional compensator jumps, common null sets and square-sum limits.

## 34.10 Keeping the Jump Sizes as Well as Their Times

<a id="jump-measure"></a>

Chapter 27’s Lévy measure described frequencies of jump sizes in a fixed model. Rates may now depend on the past, and a jump time may even be announced. The raw record must retain the time and size of each actual jump.

\[ \mu^X(\omega;ds,dx)=\sum_{s>0:\Delta X_s\ne0}\delta_{(s,\Delta X_s)}(ds,dx),\qquad (1\wedge|x|^2)*\mu^X_t<\infty. \]

The star denotes integration over time and marks. There are finitely many jumps in a compact mark band away from zero. Square summability follows from the semimartingale bracket, not from an incorrect assertion about arbitrary càdlàg functions. Measurability uses Chapter 27’s rational-coordinate lemma, which does not depend on Lévy independent increments.

For a predictable average record seek a predictable random measure ν giving the same expected accumulation for every nonnegative predictable rule W. This defines the compensator.

\[ E(W*\mu^X)_T=E(W*\nu)_T,\qquad W\ge0\ \text{predictable on }\Omega\times(0,T]\times(\mathbb R^d\setminus\{0\}). \]

Existence is not accomplished by conditioning separately at every fixed time. [Proof 6](../foundations/t-jump-calculus.md#t-jump-compensator) first applies Chapter 30’s dual projection to square-weighted jumps, then uses Chapter 10’s kernel disintegration with a predictable time-sample base and standard Borel marks. Testing all predictable rules gives local gluing and uniqueness, without invoking Chapter 48’s general point-process theory.

## 34.11 Compensation Need Not Flow Smoothly in Time

<a id="jump-atoms"></a>

Reveal a mark Y at time one, taking ±1 with equal probabilities. At that time μ records the realized mark, while ν puts half a unit on each possible mark. It is not a density with respect to dt.

\[ \nu(ds,dx)=\delta_1(ds)\,\frac{\delta_{-1}+\delta_1}{2}(dx),\qquad \widehat W_s=\int W(s,x)\nu(\{s\},dx). \]

For W=1, revelation produces one event but its count was already known, so compensation leaves zero. For W=x, compensation retains the fair random sign. The same ν gives different remaining square energies for the two rules.

\[ E|(W*(\mu-\nu))_T|^2=E(W^2*\nu)_T-E\sum_{s\le T}\widehat W_s^2. \]

This is the compensated isometry with time atoms. A Poisson dt compensator has no atoms, so the second term vanishes and the familiar formula returns. Omitting it would count an already predictable number as fresh noise.

## 34.12 Taking Limits of Random Jump Rules

<a id="jump-random-integral"></a>

Start with bounded simple predictable W on a finite time interval and a mark band away from zero. The actual sum minus compensation is a finite-variation martingale. Expanding its squared jumps and applying compensation cancels one copy of the squared atomic mean, proving the preceding formula.

Thus E∫W²dν controls approximation error, and Doob lifts it to the L² maximal norm. Density of rectangle rules actually constructs random predictable small-jump integrals. Their jump is not just W(s,∆X); the predictable atomic mean at that time must also be subtracted.

\[ \Delta(W*(\mu-\nu))_s=W(s,\Delta X_s)\mathbf1_{\{\Delta X_s\ne0\}}-\widehat W_s. \]

Locally finite square ν-energy gives local versions. Nonintegrable large marks remain finite actual sums rather than having nonexistent means subtracted. [Proof 7](../foundations/t-jump-calculus.md#t-jump-marked-integral) establishes the sufficient integration domain, stopping and consistency of versions. Not every predictable function is declared integrable.

## 34.13 A Change of Truncation Must Be Balanced in the Drift

<a id="jump-characteristics"></a>

Choose a bounded Borel truncation h agreeing with x near zero. Keep the part of large jumps beyond h explicitly. The remaining bounded-jump process has a unique predictable finite-variation decomposition, giving the canonical form

\[ X=X_0+B^h+X^c+h*(\mu-\nu)+(x-h(x))*\mu,\qquad C=[X^c]. \]

B, C and ν record predictable drift, continuous covariation and compensated jumps. These characteristics are not merely time derivatives of an observed path, nor must they possess dt densities. A predictable jump at a fixed time already rules out that requirement.

\[ B^g=B^h+(g-h)*\nu. \]

Changing h does not change the process. Moving part of a jump from actual summation into compensated integration must simultaneously move its mean into the drift, with the sign shown above. A drift already containing compensation must not have the same small-jump mean subtracted again. [Proof 8](../foundations/t-jump-calculus.md#t-jump-characteristics) treats special semimartingales, uniqueness and balance at atoms.

## 34.14 The Full Jump Remainder Finds Its Place

<a id="jump-ito"></a>

Return to the opening cube. Retain second-order variation of the continuous part, then restore the full function change at every actual jump. For f∈C² this gives

\[ f(X_t)-f(X_0)=\int_0^t f^\prime(X_{s-})\,dX_s+\frac12\int_0^t f^{\prime\prime}(X_{s-})\,d[X]^c_s+\sum_{0<s\le t}R_f(X_{s-},\Delta X_s). \]

This is not a formal substitution. Isolate the finitely many jumps larger than ε and keep their exact function changes. Taylor-expand the remaining increments. Path oscillation controls the continuous remainder; the tail of squared jumps controls the small-jump remainder. First send the mesh to zero, then ε to zero: the limits have different jobs.

Using the full [X] in the second-order integral instead requires subtracting half the quadratic term from each jump correction. The two forms are equivalent and must not be mixed. [Proof 9](../foundations/t-jump-calculus.md#t-jump-ito) proves this and the time-space and multidimensional versions.

## 34.15 A Common Jump Leaves More Than Two Variances

<a id="jump-multidimensional"></a>

When two coordinates change in the same event, the product remainder is the product of their jump sizes. The multidimensional formula therefore needs both the continuous covariation matrix and the full jump vector. Separate coordinate variances lose directional dependence.

\[ \begin{aligned}df(t,X_t)={}&f_t(t,X_{t-})dt+\sum_i f_i(t,X_{t-})dX_t^i\\&+\frac12\sum_{i,j}f_{ij}(t,X_{t-})dC_t^{ij}+dJ_t,\\J_t={}&\sum_{s\le t}\Bigl(f(s,X_s)-f(s,X_{s-})\\&\hspace{3em}-\nabla f(s,X_{s-})\cdot\Delta X_s\Bigr).\end{aligned} \]

The regularity is C¹,², and C is the bracket matrix of the continuous martingale component. Common jumps involving finite-variation coordinates enter the final term, not C. Taking f(x,y)=xy recovers the established product formula and identifies the common variation omitted by the classical rule.

## 34.16 A Continuous Exponential Need Not Survive One Jump

<a id="jump-exponential"></a>

Seek relative evolution dZ=Z₋dL with initial value one. A jump z of L forces multiplication of Z by 1+z, whereas an ordinary exponential multiplies it by eᶻ. The discrepancy persists at every resolution and needs a jump-by-jump correction.

\[ \mathcal E(L)_t=\exp\!\left(L_t-L_0-\tfrac12[L]^c_t\right)\prod_{0<s\le t}(1+\Delta L_s)e^{-\Delta L_s},\qquad L_0=0. \]

The logarithmic correction for small jumps is O(z²), so square summability gives convergence of the product on compact time windows. Finitely many large jumps are multiplied separately. Substitution into the jump Itô formula cancels the continuous second-order term and multiplies each jump by exactly 1+z, proving that this is the required stochastic exponential.

If every jump exceeds −1 the exponential is strictly positive. A jump equal to −1 kills it permanently; a smaller jump can reverse its sign. This differs from Chapter 33’s automatically positive continuous local-martingale exponential. Even strict positivity does not prevent loss of mean, so a probability density still requires a true-martingale condition.

## 34.17 Inverses and Products Need More Than a Minus Sign

<a id="jump-exponential-product"></a>

Without a jump of −1 the inverse is another stochastic exponential, but its driver is not merely −L. Each jump multiplier must change from 1+z to 1/(1+z). Continuous and jump covariation together give

\[ \mathcal E(L)^{-1}=\mathcal E\left(-L+[L]^c+\sum_{s\le\cdot}\frac{(\Delta L_s)^2}{1+\Delta L_s}\right),\qquad \mathcal E(U)\mathcal E(V)=\mathcal E(U+V+[U,V]). \]

The product formula checks every term in the driver. It also proves pathwise uniqueness for this linear integral equation directly: multiply a difference by the inverse on intervals without a jump of −1; the difference is zero. Such a jump kills the difference too, and the argument restarts afterwards. There are finitely many such large jumps on each compact interval, so Chapter 35’s general SDE theory is unnecessary. [Proof 10](../foundations/t-jump-calculus.md#t-jump-exponential) treats convergence, signs, killing and uniqueness.

## 34.18 From Square Energy to the Amplitude of a Whole Path

<a id="jump-bdg"></a>

Isometry gives a terminal second moment, not the largest intermediate fluctuation. Can maximal martingale amplitude and actual quadratic variation control each other? Doob supplies one second-order estimate; the new problem is a two-sided comparison across moment orders in the presence of jumps.

\[ c_pE[M]_T^{p/2}\le E(M_T^*)^p\le C_pE[M]_T^{p/2},\qquad M_T^*=\sup_{s\le T}|M_s|,\quad M_0=0,\quad 1\le p<\infty. \]

This is the càdlàg BDG range established here. Constants depend only on p, either side may be infinite, and stopping is allowed. BDG is not used in constructing the integral. For a finite numerical sequence first seek a bounded coefficient h reading only the past. Increment inequalities for two potentials compare squared sums and maxima pathwise. Substituting a martingale makes the integral terms have mean zero and yields the first-moment Davis inequalities. [Proof 11](../foundations/t-jump-calculus.md#t-jump-davis) verifies both increment cases algebraically.

## 34.19 Why Jumps Change the Boundary of an Inequality

<a id="jump-bdg-boundary"></a>

Lifting first moments to p-th moments must retain the overshoot at a threshold. Continuous growth hits λ exactly; a jump can cross it, with error bounded by the largest jump. Threshold integration and Hölder lift conditional Davis estimates to every p>1, yielding BDG. [Proof 12](../foundations/t-jump-calculus.md#t-jump-bdg) supplies stopping, overshoots and localization rather than replacing them by the word interpolation.

The range cannot simply be written as p>0. For M=N−t on a short window ε, no arrival leaves amplitude ε with probability close to one but zero quadratic variation. When 0<p<1, E(M∗)ᵖ is at least of order εᵖ, whereas E[M]ᵖᐟ² has order ε, so their ratio diverges. The wider range available for continuous martingales does not transfer unconditionally to jump martingales.

## 34.20 Why Semimartingales Really Are Good Integrators

<a id="jump-good-integrator"></a>

We have proved a stability property: simple predictable rules converging uniformly to zero have integrals tending to zero ucp. Isometry and maximal estimates control the locally square-integrable martingale part; the rule’s uniform bound times total variation controls the other part. The definition combines two extendible mechanisms.

The converse—that every small rule giving a small integral forces a semimartingale decomposition—is the deep Bichteler–Dellacherie characterization, not a consequence of the definition. We also prove a directly testable converse: an adapted càdlàg process with finite total conditional variation is a difference of two nonnegative supermartingales, hence a special semimartingale.

\[ \sup_\pi E\sum_i\left|E[X_{t_{i+1}}-X_{t_i}\mid\mathcal F_{t_i}]\right|+E|X_T|<\infty. \]

The condition assembles the predictable changes left in each interval into a dominating process and then uses Chapter 30’s decomposition instead of guessing a drift. [Proof 13](../foundations/t-jump-calculus.md#t-jump-good-integrator) gives the full Rao argument and the forward good-integrator property. The general converse characterization is precisely stated with a literature reference but its long proof remains open; it is not counted as proved here or used as a premise elsewhere.

## 34.21 How Small Jumps Reassemble Continuous Noise

<a id="jump-martingale-fclt"></a>

Chapter 25 excluded destructive spikes in independent random walks. Now each increment’s law may depend on the past, so independence cannot do all the work. Accumulated conditional covariance and a jump Lindeberg condition replace it: large-jump contributions vanish and the remaining square energy accumulates at a deterministic rate.

\[ \langle M^{n,i},M^{n,j}\rangle_t\xrightarrow{ucp}\Sigma_{ij}t,\qquad E\int_{(0,T]\times\mathbb R^d}|x|^2\mathbf1_{\{|x|>\varepsilon\}}\nu^n(ds,dx)\longrightarrow0\quad(\varepsilon>0). \]

For locally square-integrable vector martingales starting at zero, if these conditions hold on every finite T and Σ is symmetric nonnegative, Mⁿ converges weakly in the local J₁ path space to Brownian motion with covariance Σ. A single-time variance limit is insufficient: the first condition controls every time window and the second excludes macroscopic shocks.

First remove compensated large jumps so each remaining jump has a deterministic bound tending to zero; isometry makes the removed part vanish in the L² maximal norm. Stop the accumulated angle bracket, obtain tightness and continuous limits from the Aldous condition, then use the jump Itô remainder to pass conditional characteristic functions to a Gaussian equation. Chapter 33 identifies the noise without using Chapter 35’s general well-posed martingale problems. [Proof 14](../foundations/t-jump-calculus.md#t-jump-fclt) supplies truncation, stopping, passage of expectations and half-axis gluing.

## 34.22 What Is New When Poisson Appears Again

<a id="jump-poisson-limit"></a>

Take a Poisson process of rate n, subtract nt and divide by √n. Its jumps are 1/√n, its angle bracket is exactly t, and every Lindeberg tail eventually vanishes. The preceding theorem gives a Brownian limit for the entire compensated-count path.

\[ M_t^n=\frac{N_t^{(n)}-nt}{\sqrt n}\ \Rightarrow\ B_t\quad\text{in }D_{\mathrm{loc}}(J_1). \]

This is neither Chapter 13’s Poisson approximation nor a Gaussian fit at a terminal time. Predictably varying rates can now be handled when accumulated conditional energy stabilizes and exceptional jumps are controlled. Keeping jumps of fixed size may instead leave Lévy noise. Path limits depend jointly on the distribution of square energy and on whether jumps disappear.

## 34.23 A Unified Calculus Does Not Erase the Differences

<a id="jump-insight"></a>

The opening z³ was not eliminated. It occupies the exact jump function difference, while continuous second-order variation accumulates on a different clock. A unified integral does not identify all forms of roughness. It places them correctly within one product and change-of-variables calculus.

Square brackets record realized common changes; angle brackets and ν read predictable compensation relative to information. Atomic corrections show that an event occurring does not mean its count or mark contains the same amount of new randomness. Predictability fixes canonical drift instead of selecting an arbitrary smooth curve after observing a path.

We can now legitimately write integral equations with continuous noise and jumps. A legitimate expression is not yet an existing solution: state-dependent coefficients feed back into later motion, and local solutions may explode. Proving that these rules construct a process, and determining when it is unique, is the next concrete difficulty.

### Sources and Proof Scope

This chapter is a modern mathematical reconstruction, not a fabricated single discovery narrative for semimartingale theory. The potential-function approach can be compared with Beiglböck and Siorpaes’s [author paper](https://arxiv.org/abs/1305.6188); looser constants are verified explicitly in the companion. Original discussions of good-integrator characterization are due to Bichteler and Dellacherie; Companion 13 gives verifiable references and the outstanding scope. Chapters 27 and 30–33 supply the stated inputs, and the [complete scoped companion](../foundations/t-jump-calculus.md) links back to the main text.
