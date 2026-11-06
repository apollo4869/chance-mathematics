# Chapter 42: When Does a Random System Forget Its Initial State?

A stationary probability can describe a population exactly without erasing the difference an individual starting point leaves in its future. To understand that difference, we compare two complete experiments and seek a legitimate construction through which they can share a future.

## 42.1 Equal averages, permanently different futures

<a id="harris-phase"></a>

Let two pointers alternate between zero and one, starting in opposite states. Their time fractions at zero both approach one half, and the uniform law is invariant. Yet at every fixed time, their positions distinguish their initial states without error.

Chapter41 used this model to separate ergodicity from mixing. We now compare two future laws rather than average a single record. Given a much later position, can an observer still distinguish where the system began? This is a new question about distances between laws, not a restatement of time averaging.

Now let each step either exchange or stay, with equal probabilities. After one step both laws are uniform. Neither the long-run fraction nor the invariant law changed; overlapping mass appeared in the transitions. Chapter17 used common mass on finite spaces. We must discover when it can keep reappearing on an infinite space.

## 42.2 Measuring the trace of an initial state

<a id="harris-tv"></a>

Fix a late time. An observer may test any measurable event A: membership in a region, a coordinate threshold, or another specified state class. If the probabilities of every A are close, no such test distinguishes the laws well. This suggests taking the worst event discrepancy rather than choosing a coordinate distance in advance.

\[ d_{\rm TV}(\mu,\eta)=\sup_{A\in\mathcal E}|\mu(A)-\eta(A)|=\frac12\int\left|\frac{d\mu}{d\lambda}-\frac{d\eta}{d\lambda}\right|d\lambda,\qquad \lambda=\mu+\eta. \]

Our distance is at most one. The positive and negative parts of the density difference have equal integrals; the region where the first density is larger realizes the supremum and explains the factor one half. A bounded observation f has discrepancy at most 2‖f‖∞dTV. Applying the same probability kernel cannot increase distance, since it replaces a bounded observation by another with the same bound.

## 42.3 Joining experiments without changing either law

<a id="harris-couple"></a>

Directly comparing complicated densities may be hard. Instead generate X and Y in one auxiliary experiment, keeping their separate laws μ and η. If they are usually equal, their indicators for any event are usually equal. Such a joint realization is a coupling.

\[ |\mathbb P(X\in A)-\mathbb P(Y\in A)|\le \mathbb P(X\ne Y),\qquad d_{\rm TV}(\mu,\eta)\le\mathbb P(X\ne Y). \]

This bound can be sharp. Sample the minimum of the two RN densities jointly and sample their residuals separately; the mismatch probability then equals dTV. [T-COUPLING](../foundations/t-coupling.md#coupling-measure) constructs it fully. Shared sampling is a proof device, not a claim about a hidden common cause in two physical systems.

For processes, meeting once is insufficient. Independently sampling the next step could separate them immediately. A successful coupling of P-chains keeps them equal after a finite random time. Distance at time n is then bounded by the probability that coupling is not yet complete.

\[ d_{\rm TV}(P^n(x,\cdot),P^n(y,\cdot))\le\mathbb P_{x,y}(\tau>n). \]

## 42.4 A common chance available everywhere

<a id="harris-common"></a>

The simplest condition is P(x,·)≥εν for every x. Each step uses a shared coin with success probability ε. On success both coordinates take the same ν-state; on failure each uses its residual kernel after subtracting εν. Averaging over the coin restores P in either coordinate. Shared randomization after success keeps them together.

\[ \sup_{x,y}d_{\rm TV}(P^n(x,\cdot),P^n(y,\cdot))\le(1-\varepsilon)^n. \]

The same decomposition makes μ↦μP a strict contraction on probabilities. Completeness in total variation constructs a unique invariant π and yields a uniform geometric rate. Existence is not hidden inside an assumption. See [T-COUPLING](../foundations/t-coupling.md#coupling-global).

But on the real line, if the next position is concentrated near the current one, a fixed bounded interval cannot capture a uniform positive mass from every remote start. Global common mass is too demanding. We need returns to a region where a common chance is available.

## 42.5 A possible route is not an almost sure arrival

<a id="harris-access"></a>

On an uncountable space, individual points may have zero hitting probability. Communication cannot be described only by arrows between points. Choose a nonzero σ-finite ψ. If every positive-ψ set is hit at some positive time with positive probability from every x, call the chain ψ-irreducible. Harris recurrence requires infinitely many visits almost surely. Each fixed A has its own assertion; this is not one path visiting all sets simultaneously.

The difference is concrete. Let zero be absorbing. From j≥1 jump to zero with probability \(a_j\)=2⁻ʲ⁻¹ and otherwise to j+1. The chain is δ₀-irreducible and δ₀ is its unique invariant probability: state one has no incoming mass, then induction removes all positive integers. Yet escape forever from j has the following positive probability.

\[ \mathbb P_j(\tau_0=\infty)=\prod_{k=j}^{\infty}(1-a_k)>0,\qquad \sum_{k=j}^{\infty}a_k<\infty. \]

Since \(a_k\)≤1/4, positivity follows from −log(1−\(a_k\))≤2\(a_k\). Thus total variation distance to δ₀ does not vanish. Unique stationarity, positive-probability accessibility and forgetting from every start remain distinct.

## 42.6 A common exit on a continuous space

<a id="harris-small"></a>

A measurable C is a one-step small set if its transitions all dominate the same εν. If this holds for Pᵐ it is an m-step small set. Smallness concerns uniformly extractable probability mass, not diameter or volume. C may have positive volume, and ν need not be supported on C.

\[ P^m(x,A)\ge\varepsilon\nu(A)\quad(x\in C,\ A\in\mathcal E). \]

For a continuous everywhere positive transition density p(x,y), compact C and target D give a common lower bound c>0. Normalized reference measure on D then supplies ν with ε≤c|D|. Compactness and positivity prove the inequality; saying that the system has noise does not.

We first work with a specified one-step small set recurrent from every start. These checkable conditions suffice for regeneration and Harris convergence on a general standard Borel space. The companion proves multistep small-set extraction on standard Borel spaces, but the full structural reduction from abstract aperiodic Harris recurrence to an all-start recurrent skeleton is not proved by a definition; our conclusions keep their actual hypotheses explicit.

## 42.7 Splitting a transition into two sources

<a id="harris-split"></a>

At C the next state is not automatically independent of the past; P(x,·) still depends on x. Its εν-part does not. First decide which source supplies the transition:

\[ P(x,\cdot)=\varepsilon\nu(\cdot)+(1-\varepsilon)R_x(\cdot),\qquad R_x=\frac{P(x,\cdot)-\varepsilon\nu}{1-\varepsilon}\quad(x\in C). \]

The successful coin is at time n, but the new independent starting point is at n+1. Conditional on the preceding states, failed coins and this success, \(X_{n+1}\) always has law ν. This identifies a legitimate restart in an enlarged probability space, not a physical mechanism disappearing.

Each visit is a trial, with probability (1−ε)ᵏ of k failures. Infinitely many visits therefore give repeated successes. The half-open segment from one successful endpoint up to but excluding the next forms an iid cycle. The half-open convention prevents an endpoint from being counted in two supposedly independent cycles. [T-HARRIS-REGENERATION](../foundations/t-harris-regeneration.md#regen-cycles) constructs all kernels and marks.

## 42.8 An invariant measure from a complete cycle

<a id="harris-invariant"></a>

Starting from ν, count the expected visits to each region before the next regeneration. This defines a measure m without guessing a stationary density.

\[ m(A)=E_\nu\sum_{j=0}^{L-1}\mathbf1_A(X_j),\qquad m(E)=E_\nu L=\mu. \]

Applying P shifts the cycle occupation one step forward. The removed X₀ and added \(X_L\) both have law ν, so mP=m. Crucially {L>j} does not inspect the new coin at j, allowing the conditional transition P. Misplacing the regeneration epoch by one step would invalidate this argument.

Even if μ is infinite, m is σ-finite. Expected visits to C equal 1/ε, and {x:Pʲ(x,C)≥1/k} cover the space with m-masses at most k/ε. Regeneration thus produces an actual usable measure. Every positive-m set has positive chance of a cycle visit, so repeated independent cycles visit it infinitely often from every start: Harris recurrence.

## 42.9 Finite cycles can have infinite mean length

<a id="harris-positive"></a>

If μ<∞, π=m/μ is invariant. The iid cycle reward strong law gives time averages πf from any start. If η is also invariant, take expectations for bounded f under the η-start to get ηf=πf. This proves uniqueness without aperiodicity.

When μ=∞, no invariant probability exists, not merely no normalization of this particular m. Construct everywhere positive bounded g with mg<∞ from the σ-finite cover. Its cycle reward is integrable, while infinite mean lengths make the number of cycles per unit time vanish, so its time average is zero. Any invariant probability would integrate this strictly positive g to zero. The [companion](../foundations/t-harris-regeneration.md#regen-positive) supplies the remainder and integral details.

This separates Harris recurrence from positive recurrence. The first promises repeated restarts; the second requires their mean duration to be finite so that stationary observation can be normalized.

## 42.10 A countdown clock displaying the distinction

<a id="harris-countdown"></a>

Consider an integer countdown: j≥1 moves deterministically to j−1, while zero draws a positive integer L and moves to L−1. Zero is an atom and its return time is L. Cycle occupation and the stationary candidate can be computed coordinate by coordinate.

\[ m(\{j\})=\mathbb P(L>j),\qquad \pi_j=\frac{\mathbb P(L>j)}{EL}\quad(EL<\infty). \]

Take P(L=l)=1/[l(l+1)], l≥1. Its tail is 1/(j+1): every cycle is finite but its mean is infinite. Every state is visited infinitely often, yet no invariant probability exists. Since P(L=1)>0, periodicity is not the obstruction. An unbounded geometric tail instead has finite mean and normalizes.

## 42.11 Ratios remain meaningful when time averages vanish

<a id="harris-ratio"></a>

In null recurrence, the time fraction spent in a finite region may vanish. Ratios between regions can still stabilize. If the absolute cycle rewards of f and g are integrable and g is nonnegative with positive mean reward, normalize first by cycle count rather than elapsed time.

\[ m|f|<\infty,\quad 0<mg<\infty,\quad g\ge0\quad\Longrightarrow\quad \frac{\sum_{j<n}f(X_j)}{\sum_{j<n}g(X_j)}\longrightarrow\frac{mf}{mg}\quad\mathbb P_x\text{-a.s.} \]

Complete cycles obey the strong law. The final incomplete cycle cannot simply be discarded, but its reward is bounded by an integrable full-cycle reward, which is negligible relative to cycle count. The initial delay is finite. Thus the theorem allows μ=∞ and periodicity. For the countdown, visits to j divided by visits to zero tend to P(L>j), although both time fractions vanish.

This is not division of two limiting zeros: the ratio retains a scale that separate time averages lose. [T-HARRIS-RATIO](../foundations/t-harris-ratio.md#ratio-cycles) proves it with precise function versions.

## 42.12 Restarts need not occur at the same time

<a id="harris-shift"></a>

Once each chain regenerates, each has a fresh ν-start. Choose these starts to be the same and share the future. This gives a shift coupling: finite R,S satisfy \(X_{R+k}\)=\(Y_{S+k}\). Half-open prefixes exclude endpoints, and endpoints are independent of their prefixes, preserving the marginal laws.

R and S need not agree. Opposite alternating chains coincide after a one-step shift while retaining opposite phases at equal times. Regeneration explains restarting; aperiodicity and finite mean cycles must additionally synchronize the clocks.

## 42.13 Period as a persistent time phase

<a id="harris-period"></a>

For countable chains, period is the gcd of return lengths. On a general space, measurable disjoint phases D₀,…,\(D_{d-1}\) may satisfy P(x,\(D_{i+1}\))=1 cyclically, modulo the relevant irreducibility measure. Under stationarity their masses are equal; a start in one phase remains in a specified phase at time n, giving distance from π at least 1−1/d.

For the constructed regeneration clock the required check is gcd support(L)=1. A cyclic phase structure constrains regeneration lengths and obstructs this. Rather than assert all abstract definitions equivalent by name, we prove convergence directly under this checkable clock condition.

## 42.14 Why independent clocks eventually reach zero together

<a id="harris-clock"></a>

With μ finite, the residual clock has invariant law \(\rho _j\)=P(L>j)/μ. Two independent clocks preserve ρ⊗ρ. Simultaneous zero still requires product irreducibility. Span one supplies it: nonnegative combinations of finitely many possible cycle lengths contain all sufficiently large integers, permitting both clocks to connect specified states in the same sufficiently long time.

For a countable irreducible chain with invariant probability, Poincaré recurrence on stationary paths makes every state recurrent; strong Markov extends hitting to all starts. Thus the product hits (0,0). This uses established recurrence, not the mixing theorem being proved. [T-HARRIS-CONVERGENCE](../foundations/t-harris-convergence.md#convergence-countable) also derives the mean return identity.

## 42.15 Matching lengths is not yet matching paths

<a id="harris-marks"></a>

Cycle length usually depends on its starting state. Drawing a length and then an independent ν-start would generally change the chain. Sample the whole half-open cycle from its conditional law given its length. Its mark space is a countable disjoint union of standard Borel spaces, so Chapter10 disintegration genuinely applies.

Fill in the conditional marks before the common zero T. No lengths beginning at T have been sampled, so draw one fresh ν-state there and share the original P kernel afterwards. Both marginal full path laws remain correct and the paths agree after T. The coupling need not depend only on the current pair of states; the coupling inequality does not require that property.

## 42.16 A Harris convergence theorem with an actual construction

<a id="harris-convergence"></a>

Combine the actual assumptions: E is standard Borel; P has a specified one-step small set C with ε,ν; C is visited infinitely often from every start; the ν-regeneration length L has finite mean μ and span one. Then π=m/μ is the unique invariant probability and, for every x,

\[ d_{\rm TV}(P^n(x,\cdot),\pi)\longrightarrow0. \]

Existence and uniqueness come from cycle occupation and rewards. Convergence comes from synchronized regeneration with correct conditional path filling. Every initial probability η converges too, by integrating the pointwise bound at most one. The all-start conclusion relies on pointwise recurrence; assumptions on only a full-measure closed class give conclusions only within that class.

For specified data on Q=Pᵐ with the same finite mean and span conditions, first construct its π. Since πP is Q-invariant, πP=π. Kernel contraction handles the remainder of n modulo m. Conditional bridges retain intermediate states. See [T-HARRIS-CONVERGENCE](../foundations/t-harris-convergence.md).

## 42.17 How distant events decouple in stationary records

<a id="harris-mixing"></a>

In a π-stationary chain, the past influences the future through the current state. The whole path after n is itself a probability kernel from \(X_n\). Thus one-time total variation convergence controls entire future events. For past A and distant future B,

\[ \sup_{A\in\sigma(X_j:j\le0),\,B\in\sigma(X_j:j\ge n)}|\mathbb P_\pi(A\cap B)-\mathbb P_\pi(A)\mathbb P_\pi(B)|\le \int\pi(dx)\,d_{\rm TV}(P^n(x,\cdot),\pi)\to0. \]

This is strong mixing, beyond correct average frequencies. Yet the bound is integrated under π, not uniform over remote initial states. Stationarity, ergodicity, mixing, all-start convergence and uniform convergence remain different assertions.

## 42.18 A local rule forcing repeated returns

<a id="harris-drift"></a>

The regenerative theorem assumes returns; it does not yet verify them in a new model. Give remote states a large V and ask whether PV≤γV+K with γ<1. Outside C={V≤R}, a negative drift summed to bounded stopping times bounds the mean hitting time. This is the argument between an inward mean and almost sure return.

\[ R>\max\left(1,\frac{2K}{1-\gamma}\right),\quad d=(1-\gamma)R-K>0,\quad E_x\tau_C\le\frac{V(x)}d. \]

If C also has common εν, the mean excursion length after failed trials is controlled. For two paths, separate returns are insufficient. Put S=V(x)+V(y): large S contracts through drift, while small S puts both points in C and allows common mass. A sufficiently small β in the weight w=1+βV combines the estimates into a strict contraction.

\[ \|\mu P-\eta P\|_{1+\beta V}\le r\|\mu-\eta\|_{1+\beta V},\quad r<1,\qquad d_{\rm TV}(P^n(x,\cdot),\pi)\le \frac{r^n}{2}\bigl(2+\beta V(x)+\beta\pi V\bigr). \]

Completeness of weighted measures constructs π. Any other invariant probability, even without finite V-moment, is excluded by pointwise convergence and bounded convergence. [T-HARRIS-DRIFT](../foundations/t-harris-drift.md) proves the constants, stopping argument, metric and fixed point. This is a sufficient geometric criterion, not a claim that all positive recurrent chains forget geometrically.

## 42.19 Shared noise can shrink distance without meeting

<a id="harris-gaussian"></a>

For \(X_{n+1}\)=a\(X_n\)+σ\(Z_{n+1}\), |a|<1,σ>0, V=1+x² verifies drift. A Gaussian density has a positive lower bound on a compact product, providing a small set. The unique invariant law is N(0,σ²/(1−a²)), with the preceding total variation bound. Gaussian addition identifies the law; a separate proof establishes convergence.

Using the same Z-sequence from x and y gives difference aⁿ(x−y), which tends to zero but never vanishes when a≠0 and x≠y. Failure of one coupling to meet does not disprove total variation forgetting; another coupling can use common mass more effectively. Nor does total variation convergence say that every pair of independently sampled paths approaches in space.

## 42.20 Every fixed start is not a uniform bound over starts

<a id="harris-uniform"></a>

Return to a span-one countdown with finite mean and unbounded support. Every fixed j converges to π. Yet for a given n, starting at j>n leaves the clock deterministically at j−n. Taking j arbitrarily large makes \(\pi _{j-n}\) arbitrarily small. Thus the worst initial-state distance remains one at every n.

\[ \forall j,\ d_{\rm TV}(P^n(j,\cdot),\pi)\to0,\qquad \sup_j d_{\rm TV}(P^n(j,\cdot),\pi)=1\quad\text{for every }n. \]

A weaker kind of forgetting also differs: deterministic x↦x/2 on [0,1] converges weakly to δ₀ from every x, but for x>0 the total variation distance is one at every finite n. Spatial proximity and indistinguishability by all measurable tests are different. This chapter deliberately asks for the latter.

## 42.21 A broader return structure behind ratio limits

<a id="harris-hopf"></a>

Independent regenerative cycles make ratio limits visible, but independence is not their only source. For an invertible conservative ergodic σ-finite measure-preserving system, induce on a finite positive-measure set A. Conservativity provides returns and ergodicity makes its return towers cover the space modulo null sets.

Sum integrable f,g over one tower excursion. Tower partition recovers the original integrals mf,mg. Birkhoff for the induced probability transformation and control of the final integrable excursion give the Hopf ratio mf/mg. An infinite-measure problem is reduced to a finite observation region without assuming a probability measure on the whole space.

Conservativity cannot be dropped: translation k↦k+1 on Z preserves counting measure and is ergodic, but a start at two never visits zero or one. Equal integrals of the two singleton indicators give no usable future denominator. [T-HARRIS-RATIO](../foundations/t-harris-ratio.md#ratio-hopf) proves the stated scope, not arbitrary nonsingular or positive-operator versions.

## 42.22 Forgetting is a proved property, not a synonym for randomness

<a id="harris-insight"></a>

The alternating pointer has stable averages and a unique invariant law but retains phase. An infinite-mean clock repeatedly restarts but cannot normalize stationary time. An escaping chain with an absorbing point has a unique invariant probability without convergence from every start. These calculations separate three judgments: stable averages, existence and uniqueness of stationary probability, and forgetting of initial distributions.

The successful construction does not show that randomness naturally erases history. Common mass permits resampling; recurrence repeats the opportunity; finite mean cycles normalize stationary observation; absence of a time phase permits synchronization. Drift and small sets turn these mechanisms into checkable local conditions. Each carries a different step of the proof.

We asked how much information about an early position remains after time advances. Another symmetry is different: if arbitrary finite rearrangements of observations preserve the law, what information remains? A hidden-parameter coin record can ignore order while its long-run average remembers the parameter. Insensitivity to order must not simply be called independence.

## 42.23 Sources, modern reconstruction and scope

<a id="harris-sources"></a>

Harris’s [The existence of stationary measures for certain Markov processes](https://digicoll.lib.berkeley.edu/record/112840/files/math_s3_v2_article-08.pdf) appeared in the 1956 Third Berkeley Symposium proceedings, volume II, pages113–124. Our pointer, countdown and escape examples are modern teaching constructions, not a reconstruction of the paper’s discovery sequence.

The 1978 [splitting work of Nummelin](https://doi.org/10.1007/BF00534764) and the [regenerative approach of Athreya and Ney](https://repository.ias.ac.in/1112/) connected general-state chains to atoms and renewal through added randomization. Here we construct splitting for specified minorization data and prove half-open cycles, σ-finite invariance, ratios, successful coupling and the specified skeleton extension. A separately developed weighted contraction proves a quantitative Harris criterion. Scope was checked against [Hairer–Mattingly](https://arxiv.org/abs/0810.2777) and [Hairer’s author notes](https://www.hairer.org/notes/Convergence.pdf); exposition and proof organization follow this book’s own questions.

The five complete proofs are [T-COUPLING](../foundations/t-coupling.md), [T-HARRIS-REGENERATION](../foundations/t-harris-regeneration.md), [T-HARRIS-CONVERGENCE](../foundations/t-harris-convergence.md), [T-HARRIS-RATIO](../foundations/t-harris-ratio.md), and [T-HARRIS-DRIFT](../foundations/t-harris-drift.md). The most general skeleton reduction for abstract aperiodic Harris chains, the broadest continuous-time Harris/ratio theory and general nonsingular Hopf versions are outside their proved scope.
