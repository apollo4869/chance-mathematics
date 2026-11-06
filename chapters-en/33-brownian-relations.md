# Chapter 33: The Deeper Relations Between Brownian Motion and Martingales — Continuous Martingales, Representation, Time Change and Girsanov

A particle moves left or right over equal intervals. We can already record it by Brownian paths and construct motions with drift. Now leave every recorded path untouched, but give rightward records greater probability weight. Can weighting alone produce exactly a law with constant drift?

For one Gaussian increment this is a completing-the-square calculation. The difficulty is that increments belong to one path: weights at different observation times must agree, and a positive limiting weight may fail to retain total mass. We must distinguish changes of path weights, changes of the clock, and changes of the observer’s information.

## 33.1 Reweighting One Gaussian Increment

<a id="br-gaussian-weight"></a>

Let B be standard d-dimensional Brownian motion relative to a filtration F satisfying the usual conditions. Start in one dimension with a constant a. Multiplying the centered Gaussian increment density on an interval of length Δt by the weight below and completing the square gives mean aΔt and variance Δt. Its normalization is not a guess: the Gaussian integral equals one.

\[ e^{ax-a^2\Delta t/2}\frac{e^{-x^2/(2\Delta t)}}{\sqrt{2\pi\Delta t}}=\frac{e^{-(x-a\Delta t)^2/(2\Delta t)}}{\sqrt{2\pi\Delta t}}. \]

On a fixed [0,T], multiplying interval weights leaves \(\exp(aB_T-a^2T/2)\). Every deterministic partition therefore acquires independent Gaussian increments with drift, and refinement changes nothing. We already have a candidate weight for an entire path, rather than a refitted terminal distribution.

If a is chosen from information available at each left endpoint, conditional Gaussian integration still normalizes each finite product. Passing to zero mesh does not permit exchanging limit and expectation merely because each approximant has mean one. The stochastic exponential of Chapter 32 puts us precisely at this boundary.

## 33.2 Weights at Different Times Must Agree

<a id="br-density"></a>

Fix finite T. For nonnegative \(\mathcal F_T\)-measurable L with \(E_P\) L=1 define Q(A)=\(E_P\)[L1\_A] on \(\mathcal F_T\). At time t only \(Z_t\)=\(E_P\)[L|\(\mathcal F_t\)] is visible. An event already decided in \(\mathcal F_s\) cannot receive a different probability merely because its weight is recomputed later; this is exactly the martingale requirement. Conversely, a nonnegative martingale Z starting at one gives density \(Z_t\) on \(\mathcal F_t\) when its terminal horizon is T.

\[ Q(A)=E_P[Z_t\mathbf1_A]\quad(A\in\mathcal F_t),\qquad E_Q[X\mid\mathcal F_s]=\frac{E_P[Z_tX\mid\mathcal F_s]}{Z_s}\quad(s\le t\le T). \]

The second formula initially concerns bounded \(\mathcal F_t\)-measurable X and assumes \(Z_T\)>0 almost surely. Integrating either side under Q over A∈\(\mathcal F_s\) cancels \(Z_s\) against the density of Q on \(\mathcal F_s\) and gives \(E_P\)[\(Z_tX1\)\_A]. This proves the conditional-expectation identity; truncation extends it to Q-integrable X. Strict positivity gives equivalence on \(\mathcal F_T\). A density allowed to vanish initially gives only Q absolutely continuous with respect to P.

The main change-of-measure theorems below are proved on finite horizons. Without an additional argument, a family of finite-time densities is not automatically a probability on the original \(\mathcal F_\infty \). The static density theory of Chapter 10 and the extension problem of Chapter 8 have distinct roles here.

## 33.3 Why a Positive Stochastic Exponential May Fail to Be a Probability

<a id="br-exponential"></a>

Let M be a continuous local martingale starting at zero, with A=[M]. Chapter 32 proved that the following solves dZ=Z dM; we do not reconstruct that integral. Z is strictly positive, but limits of localized martingales only guarantee that expectation does not increase. We have a supermartingale, not yet a probability density.

\[ Z_t=\mathcal E(M)_t:=\exp(M_t-A_t/2),\qquad Z_0=1,\qquad E_PZ_t\le1. \]

On a fixed T the exact test is E \(Z_T\)=1. Supermartingale expectations decrease, so this equality forces every conditional supermartingale inequality for s≤t≤T to be an equality. Thus Z is a true martingale and equals E[\(Z_T\)|\(\mathcal F_t\)]. Conditional averages of one integrable terminal variable are uniformly integrable, making it a closed martingale on this finite interval. Reweighting has become a precise integrability problem.

## 33.4 How Novikov’s Condition Prevents Loss of Mass

<a id="br-novikov"></a>

A directly checkable clock condition is E exp(\(A_T\)/2)<∞, known as Novikov’s condition. Its relevance cannot be guessed merely from the other factor 1/2 in the exponential. First assume the stronger E exp(\(cA_T\)/2)<∞ for some c>1. Choose p>1,r>1 with C=r(rp²−p)/(r−1)<c: first take 1<r<c, then p sufficiently close to one. Exponential algebra and Hölder give, for any localized endpoint ρ≤T,

\[ Z_\rho^p=\mathcal E(rpM)_\rho^{1/r}e^{(rp^2-p)A_\rho/2},\qquad E Z_\rho^p\le\left(Ee^{CA_T/2}\right)^{(r-1)/r}. \]

Only the supermartingale bound E\(\mathcal E(rpM)\)≤1 was used, not an unproved true-martingale property. Stop when |M| or A first reaches n. Stopped Z is bounded and is a true martingale with mean one. The displayed estimate makes these terminal weights uniformly bounded in \(L^p\) and therefore uniformly integrable. Removing the stops gives E \(Z_T\)=1.

The critical c=1 needs another step; it cannot silently replace c>1. For 0<a<1 apply the proved result to aM, whose clock is a²A, and choose c=1/a²>1. Its required exponential moment is exactly E exp(\(A_T\)/2). Hence \(\mathbb E\mathcal E(aM)_T=1\). Another application of Hölder gives

\[ 1=E\{Z_T^a e^{a(1-a)A_T/2}\}\le(EZ_T)^a\left(Ee^{aA_T/2}\right)^{1-a}. \]

The last exponential moment is bounded by the finite constant E exp(\(A_T\)/2). Letting a↑1 gives E \(Z_T\)≥1, while the supermartingale inequality gives the reverse. This proves the finite-horizon Novikov criterion at its critical coefficient, not just a version with extra integrability.

## 33.5 Recognizing Brownian Motion After Removing Drift

<a id="br-levy"></a>

Even if reweighting restores fairness, a one-time distribution does not identify Brownian motion. We need a test of the entire conditional structure. Let N be a d-dimensional continuous local martingale starting at zero with [N^i,N^j]\_t=\(\delta _ij\) t. Then N is standard Brownian motion relative to the current filtration: Lévy’s martingale characterization.

The proof turns Chapter 11’s characteristic functions into conditional characteristic functions. Fix u and apply Chapter 32’s Itô formula to the real and imaginary parts of the complex exponential below. It is a local martingale with deterministic modulus bound exp(|u|²T/2) on [0,T], hence a true martingale.

\[ \exp\{iu\cdot N_t+|u|^2t/2\},\qquad E[e^{iu\cdot(N_t-N_s)}\mid\mathcal F_s]=e^{-|u|^2(t-s)/2}. \]

Multiply by 1\_A for A∈\(\mathcal F_s\) and take expectations. The right side factors into P(A) and a Gaussian characteristic function. Chapter 14’s uniqueness for finite measures identifies the increment as that Gaussian, independent of \(\mathcal F_s\). Iteration yields independent increments at finitely many times; continuity is already given. The converse follows from Brownian isometry and covariation. Fairness together with the full common quadratic clock identifies the motion.

## 33.6 Which Part Ceases to Be Fair When Probability Changes

<a id="br-girsanov"></a>

Let Z now be a strictly positive continuous true martingale, Z₀=1, defining Q on a fixed T by \(Z_T\). If a continuous P-local martingale M starting at zero fluctuates jointly with Z, reweighting creates a predictable accumulation. Subtract the process below to remove it. The continuous bracket need not possess a dt density.

\[ N_t=M_t-\int_0^t Z_s^{-1}\,d[M,Z]_s.\qquad\text{Then }N\text{ is a continuous }Q\text{-local martingale.} \]

Take M₀=0. The product formula gives d(ZN)=N dZ+Z dM: the finite-variation correction cancels the cross term. This explains the common fluctuation divided by current weight. Localization must still be converted into actual conditional expectations. Stop N at absolute value n. Its product with Z is a P-local martingale dominated in absolute value by nZ at bounded stopping times. Uniform integrability of the stopped family of closed Z makes the product a true martingale. Section 2’s Bayes identity then makes stopped N a Q-martingale. Remove n. The full stopped-product calculation is in [companion proof 1](../foundations/t-brownian-relations.md#t-br-change).

## 33.7 Girsanov: The Same Coordinates, a Different Drift

<a id="br-brownian-drift"></a>

Let θ be predictable and d-dimensional, with ∫₀ᵀ|θ|²ds finite almost surely, and assume \(Z=\mathcal E(\int_0^\cdot\theta_s\cdot dB_s)\) is a true martingale on [0,T]. Novikov is one proved sufficient condition. Chapter 31 gives \([B^i,Z]_t=\int_0^t Z_s\theta_s^i\,ds\). The preceding section makes the following a continuous Q-local martingale.

\[ \widetilde B_t=B_t-\int_0^t\theta_s\,ds,\qquad\frac{dQ}{dP}\bigg|_{\mathcal F_T}=\exp\left\{\int_0^T\theta_s\cdot dB_s-\frac12\int_0^T|\theta_s|^2ds\right\}. \]

Subtracting finite variation leaves quadratic variation unchanged, and equivalent finite probabilities preserve ucp limits. Indeed, P(\(E_n\))→0 implies Q(\(E_n\))≤K P(\(E_n\))+\(E_P\)[\(Z_T1\)\_{\(Z_T\)>K}]; send n then K to infinity. The common bracket under Q is therefore still \(\delta _ij\) t. Lévy’s characterization makes B̃ Q-Brownian. This proves the drift transformation rather than guessing independence from Gaussian marginals.

For example X=B+bt has drift b under P. Choose θ=−b; then B̃=B+bt=X is Brownian under the new probability. Conversely θ=b makes the original coordinate B have drift b under Q. The sign is fixed by the density convention; it cannot be changed while retaining the same exponential.

## 33.8 A Sufficient Condition Is Not Necessary

<a id="br-novikov-boundary"></a>

Take 0<t₀<T, C=\(B_{t₀}\)², and let θ be zero before t₀ and C afterwards. This is simple predictable, with finite pathwise squared energy. Conditional on \(\mathcal F_{t₀}\), the remaining increment is independent Gaussian, so the conditional mean below is one, as is its total mean. Section 3 shows Z is a true martingale.

\[ Z_T=e^{C(B_T-B_{t_0})-C^2(T-t_0)/2},\qquad E[Z_T\mid\mathcal F_{t_0}]=1,\qquad E e^{C^2(T-t_0)/2}=\infty. \]

The divergence follows because the Gaussian density’s negative quadratic exponent cannot control the positive quartic exponent. Novikov fails, yet the changed probability exists. An easy clock bound is not the definition of a valid probability; total mass and temporal consistency are the underlying requirements.

## 33.9 How a Strictly Positive Local Weight Loses Mass

<a id="br-strict-local"></a>

A genuine counterexample is needed for the opposite direction. Take three independent Brownian coordinates W, start at deterministic x≠0, and put R=|x+W|, r=|x|. The three-dimensional path does not hit this origin: stopping the harmonic function 1/|y| between ε and a large radius makes the inner-ball probability tend to zero with ε; then increase the outer radius. The stopping and common null set are proved in [companion proof 2](../foundations/t-brownian-relations.md#t-br-strict), without a Bessel SDE.

\[ Z_t=\frac r{R_t}=\mathcal E\left(-\int_0^\cdot\frac{x+W_s}{R_s^2}\cdot dW_s\right)_t,\qquad EZ_t=2\Phi(r/\sqrt t)-1<1\quad(t>0). \]

Itô formula reads the zero Laplacian of 1/|y|, giving a strictly positive continuous local martingale. R has a positive minimum on compact time intervals, making the integral energy legitimate. The expectation follows by direct spherical integration of the three-dimensional Gaussian density, carried out in the supplement. The everywhere-positive weight has less than unit total mass.

Normalizing each \(Z_t\) separately by its mean produces individual probabilities but generally destroys temporal consistency. Here E[\(Z_t\)|\(\mathcal F_s\)]/\(Z_s\)=2Φ(\(R_s\)/√(t−s))−1 depends on random \(R_s\), not just on s,t. What is missing is a closed-martingale structure, not a scalar normalization constant.

## 33.10 Equivalence on Every Finite Window Is Not Equivalence Forever

<a id="br-infinite-horizon"></a>

Return to the weight exp(\(aB_t\)−a²t/2), a≠0. It is a true martingale on every finite interval yet tends almost surely to zero as t→∞. The required \(B_t\)/t→0 needs no delicate path theorem: Doob’s squared maximal bound on [0,2^{k+1}] puts the probability of exceeding ε2^k below 2^{1−k}/ε². Borel–Cantelli covers successive dyadic time ranges.

On canonical continuous path space with its raw coordinate filtration, the law of B+at is directly defined and has precisely these densities on finite-time coordinate sigma-algebras. Here null sets of the entire infinite-horizon Wiener law are not inserted into the initial information. But the event lim x(t)/t=0 has probability one under Wiener measure and zero under the drifted law. The infinite-horizon probabilities are singular. Treating \(Z_\infty \)=0 as a density on \(\mathcal F_\infty \) gives the zero measure, not the drifted path law.

This filtration qualification matters. If all infinite-horizon P-null sets are inserted into the initial information, the complement of the limit event above already belongs to the initial sigma-algebra. Every finite-terminal density gives it probability zero, whereas the full drifted law gives it probability one. These cannot be consistent simultaneously. Infinite-time extension and finite-time change of measure require separate proofs.

## 33.11 Which Deterministic Translations Only Reweight Paths

<a id="br-cameron-martin"></a>

Constant drift suggests a finer test. On [0,T] take deterministic continuous h with h(0)=0 and compare the path laws μ of B and \(\mu _h\) of B+h. If h is absolutely continuous with L² derivative, take θ=h′. The deterministic Gaussian exponential has mean one, and Girsanov gives the density below; the laws are equivalent.

\[ \mathcal H_T=\left\{h:h(t)=\int_0^t g(s)ds,\ g\in L^2[0,T]\right\},\qquad\frac{d\mu_h}{d\mu}(x)=\exp\{I(g)(x)-\|g\|_2^2/2\}. \]

I(g) is a measurable version of Chapter 31’s deterministic Wiener integral, not an ordinary Riemann integral available on every rough path. Strict positivity and equivalence make its version-null sets negligible for both measures. Squared energy is the precise cost of reweighting, not an informal demand that a curve look smooth.

## 33.12 How Infinite Energy Separates the Laws

<a id="br-cm-singularity"></a>

The condition is necessary, and failure gives singularity rather than merely a missing density formula. Use a Haar step-function orthonormal basis \(e_k\) of L²[0,T]. Path readings \(\xi _k\)=∫\(e_k\) dx are finite linear combinations of increments. Under the original law they are independent standard Gaussians; translation adds means \(m_k\)=∫\(e_k\) dh. If Σ\(m_k\)² is finite, the basis expansion gives g∈L². Comparing increments at dyadic endpoints and using continuity gives h(t)=∫₀ᵗg, so h is in the energy space. The statistic below is defined for a positive denominator and set to zero when the denominator is zero.

\[ s_n=\sum_{k\le n}m_k^2,\qquad D_n=\frac{\sum_{k\le n}m_k\xi_k}{s_n},\qquad \operatorname{Var}_\mu(D_n)=\operatorname{Var}_{\mu_h}(D_n)=s_n^{-1}\quad(s_n>0). \]

If h is outside the energy space, \(s_n\)→∞. Choose \(s_{n_j}\)≥2^j. Chebyshev and the first Borel–Cantelli lemma make \(D_{n_j}\) tend almost surely to zero under μ and to one under \(\mu _h\). This measurable path event separates the laws. Infinitely many independent Gaussian readings detect a displacement with infinite total energy. Haar completeness and endpoint details are in [companion proof 5](../foundations/t-brownian-relations.md#t-br-cm).

## 33.13 Energy on a Finite Window and on the Entire Time Axis

<a id="br-cm-global"></a>

On \(C_{\mathrm{loc}}\)[0,∞), the same result uses locally absolutely continuous curves with finite total squared energy. Finite energy makes the deterministic stochastic integral converge in L² and almost surely. Exponential second moments are bounded by exp(total energy), yielding uniform integrability and a strictly positive limiting density. Infinite energy is separated by the same statistic on Haar bases over successive unit intervals. If a finite window already fails \(\mathcal H_T\), that projection alone gives singularity.

The coordinate proof also establishes the translation criterion for a countable product of independent standard Gaussians: an ℓ² mean sequence gives equivalence, otherwise singularity. It supplies a genuine energy tool for Chapter 23’s separable isonormal coordinates and later Gaussian differentiation. Multiple Wiener integrals and the complete chaos expansion of Chapter 39 have not been proved here.

## 33.14 A Clock That Reweighting Cannot Arbitrarily Change

<a id="br-clock-question"></a>

Equivalent reweighting changes drift but preserves the same paths’ quadratic variation. If a continuous local martingale M has clock A different from t, Lévy’s criterion does not apply directly. Chapter 31’s Cantor clock shows why an instantaneous variance factor may not remove the difference. What should now change is the parameter used to read the path.

\[ A_t=[M]_t,\qquad\tau_s=\inf\{t\ge0:A_t>s\},\qquad W_s=M_{\tau_s}. \]

The inverse clock can skip a whole interval of calendar time. We must prove that when A is constant, M is constant too; otherwise W might not be continuous. Drawing an inverse function does not settle this measurable path issue.

## 33.15 DDS: Reading Continuous Fair Fluctuations as Brownian Motion

<a id="br-dds"></a>

First assume \(A_\infty \)=∞ almost surely and M₀=0. Then \(\tau _s\) is a finite stopping time and \(A_{\tau _s}\)=s. Relative to \(G_s\)=\(\mathcal F_{\tau _s}\), W is Brownian and \(M_t\)=\(W_{A_t}\). This is the scalar DDS time change. It does not automatically turn an arbitrary multidimensional covariance matrix into one common scalar clock.

The flat-interval step has a concrete estimate. Fix rational u<v and stop before \(A_t\)−\(A_u\) first exceeds 1/n. The increment martingale has total bracket at most 1/n, so Doob bounds the probability of amplitude exceeding ε by 1/(nε²). On {\(A_v\)=\(A_u\)} the stop cannot occur early. Let n→∞ to obtain constancy of M. A common null set over rational intervals and continuity handle every flat interval.

Inverse-clock jumps therefore leave no jump in M, and W is continuous. Stop the original martingale at integer bracket levels: both the stopped martingale and its square compensation are closed, allowing unbounded optional sampling. Thus W and W²−s are martingales on finite clock intervals. Chapter 31’s bracket uniqueness and Lévy’s criterion finish the proof. The inverse’s stopping property, right-continuity of its filtration and the closed-martingale estimates are proved in [companion proofs 3–4](../foundations/t-brownian-relations.md#t-br-dds).

## 33.16 A Clock Can Stop and Can Depend on the Path

<a id="br-dds-finite"></a>

If ζ=\(A_\infty \) is finite, M has a limit on that event. Read W up to clock time ζ and then hold it fixed; its bracket is s∧ζ. On an enlarged space add independent Brownian motion β and then ∫₀ˢ1\_{u>ζ}dβ\_u to fill the remaining quadratic clock. ζ is a stopping time in the clock filtration and the martingales have zero cross bracket. Lévy again gives Brownian W, retaining \(M_t\)=\(W_{A_t}\). A one-point original space cannot generate Brownian motion by itself, so enlargement cannot simply be omitted.

The representation does not imply that \(M_t\) is Gaussian conditional on \(A_t\). Stop Brownian motion at its first hit of 1. Then \(A_t\)=t∧τ, but \(M_t\)=1 on {τ<t}, while \(A_t\)>0. The clock and the new Brownian path may be dependent; a random time is not automatically an independent sampling time.

## 33.17 What Distribution Can Brownian Motion Leave When It Stops

<a id="br-embedding"></a>

A random time destroys the intuition of a Gaussian terminal value, but creates a construction tool. Given a centered real law μ with finite second moment, can we choose a stopping time τ on an already given Brownian path so B\_τ has law μ and Eτ is its variance? Selection must be legal in the natural filtration, not retrospective inspection of a complete path.

Write μ as the law of its monotone quantile g(U). U only specifies a deterministic table; it is not extra Brownian information. Let \(m_w\) be the mean of g on a dyadic cell. Each parent is the midpoint of its two child means. Starting at \(m_w\), wait until Brownian first hits one child mean. The distances agree, so each child has probability 1/2. Refining embeds a discrete conditional-mean martingale in a continuous path.

\[ X_n=E[g(U)\mid\mathcal D_n],\qquad B_{\tau_n}\stackrel d=X_n,\qquad E\tau_n=E X_n^2\uparrow E g(U)^2. \]

If child means coincide, monotonicity of the quantile forces g to be constant almost everywhere on the parent cell, so refinement stops there. Otherwise \(\tau _n\) increases with uniformly bounded mean, making its limit τ finite almost surely. Continuity gives \(B_{\tau _n}\)→B\_τ, while dyadic conditional means converge in L² to g(U). Thus B\_τ has law μ and Eτ=∫x²μ(dx). This is a natural-filtration Skorokhod embedding, without future SDE theory, distinct from Chapter 24’s same-named new-space representation. Stopping and branch details are in [companion proof 8](../foundations/t-brownian-relations.md#t-br-embedding).

## 33.18 Moments of the Stopping Clock Need More Than a Variance Guess

<a id="br-embedding-moments"></a>

The construction also gives Eτ^p≤\(C_p\)∫|x|^{2p}μ(dx) for p≥1 when that moment is finite, and a uniformly integrable stopped Brownian family. The second-moment identity does not itself imply higher bounds. The mechanism is that if much time has elapsed while amplitude remains small, the next independent Gaussian increment must again fit an unusually narrow interval.

\[ P(\tau_n>2u)\le P(B^*_{\tau_n}>\delta\sqrt u)+q_\delta P(\tau_n>u),\qquad q_\delta=P(|N(0,1)|\le2\delta). \]

Choose q\_δ<\(2^{-p}\), integrate tails, and use Chapter 15’s Doob maximal inequality of order 2p. [Companion proof 9](../foundations/t-brownian-relations.md#t-br-embedding-moments) justifies finite-stage moments and passage to the limit, without borrowing Chapter 34’s BDG. This supplies an actual tool for Chapter 25’s optional embedding route without reproving its completed Donsker argument.

## 33.19 Does Having Brownian Noise Mean Having All Information

<a id="br-information"></a>

DDS changes the clock and may enlarge the space; embedding asks for one terminal law. A stronger requirement is to retain the current Brownian motion and calendar time and write every fair fluctuation as an integral against this very B. The answer depends on whether B generates all the available information.

Let F be the completed right-continuous natural filtration of B. For every X∈L²(\(\mathcal F_T\)) there is a unique predictable H with E∫₀ᵀ|H|²dt<∞ satisfying the following. Uniqueness is as a Pdt equivalence class, and the associated conditional-expectation martingale has a continuous version.

\[ X=E X+\int_0^T H_s\cdot dB_s,\qquad E[X\mid\mathcal F_t]=E X+\int_0^tH_s\cdot dB_s. \]

## 33.20 Isometry Turns Representation into a Closed-Space Problem

<a id="br-representation"></a>

Chapter 31’s isometry makes constants plus Brownian-integral terminal values a closed subspace S of L². To prove X=0 whenever X is orthogonal to S, find a sufficiently rich family already in S. Gaussian exponentials for deterministic step h do exactly this. Itô formula provides their integral representation; their second moments equal exp(∫|h|²), and their integral energies are finite.

\[ E_T(h)=\exp\left(\int_0^T h\cdot dB-\frac12\|h\|_2^2\right)=1+\int_0^T E_s(h)h_s\cdot dB_s. \]

Choose arbitrary constant values of h on a finite partition. If X is orthogonal to every \(E_T\)(h), then F(Y)=E[X|Y], where Y is the vector of partition increments, satisfies E[F(Y)exp(a·Y)]=0 for every real vector a. It remains to prove that these readings identify F; saying there are many exponentials is not a completeness proof.

## 33.21 Why Gaussian Exponentials Read Every Terminal Value

<a id="br-exponential-totality"></a>

Differentiate E[F(Y)exp(a·Y)] repeatedly in real a at zero. Gaussian exponential moments and Cauchy–Schwarz dominate polynomial-exponential products on compact parameter sets, so dominated convergence gives E[F(Y)Y^k]=0 for all mixed powers. Expand exp(iu·Y) in its absolutely convergent power series; its absolute sum is bounded by exp(Σ|\(u_jY\)\_j|), still integrable against |F|. Every Fourier reading of the finite signed measure F(y)\(P_Y\)(dy) vanishes. Uniqueness from Chapters 11/14 gives F=0.

Thus X is orthogonal to every square-integrable function of every finite Gaussian record. Finite cylinders at rational times generate the continuous Brownian path information. The L² closure of their indicators covers \(\mathcal F_T\) by π–λ and finite-measure tail approximation; completion-null sets do not change L². Therefore X=0. The closed-space projection gives the representation. Conditional expectation and the martingale property of the integral give the process identity; isometry gives uniqueness. The proof uses the structure generating all the information, not just Brownian marginals.

## 33.22 From Square-Integrable Terminal Values to Local Martingales

<a id="br-local-representation"></a>

For an integrable terminal value, first truncate it to obtain continuous L²-represented martingales. Doob’s weak L¹ maximal estimate controls their whole-path differences. A summable-probability subsequence gives a continuous version. Only then stop at amplitude n, use bounded-martingale L² representation and glue by uniqueness. One must not assume all stopped local-martingale paths are continuous in order to prove their continuity.

In the usual natural Brownian filtration, every càdlàg local martingale thereby has an indistinguishable continuous version and a local predictable integral representation. Energy is only required locally pathwise finite, not to have finite expectation. [Companion proof 6](../foundations/t-brownian-relations.md#t-br-local-representation) supplies truncation, localization and common-null-set details.

## 33.23 Changing Measure Is Different from Enlarging Information

<a id="br-representation-boundary"></a>

If an independent Brownian motion C is also observed, B remains Brownian in the enlarged filtration, but C cannot be ∫H dB: [C,B]=0 would force ∫H ds=0 and hence H=0 almost everywhere, contradicting [C]=t. If instead \(B_T\) is disclosed at time zero, B is not even a martingale, since E[\(B_T\)|F₀]=\(B_T\) rather than zero. The two information changes break different properties.

Finite-horizon equivalent reweighting can preserve representation, but with driver B̃. If N is a Q-martingale, Y=ZN is a P-martingale. Represent Y, then apply Chapter 32’s quotient formula to Y/Z to obtain the identity below. This does not require an unproved assertion that B̃’s natural filtration equals the original one. Local details are in [companion proof 7](../foundations/t-brownian-relations.md#t-br-transfer).

\[ dY=h\cdot dB,\quad dZ=Z\theta\cdot dB\quad\Longrightarrow\quad dN=(h/Z-N\theta)\cdot d\widetilde B. \]

Conversely, in natural Brownian information every strictly positive terminal probability density gives a continuous density martingale. Represent it and divide by Z to write it as a stochastic exponential. Its density origin already makes it a true martingale; Novikov need not hold. Representation explains the full shape of such dynamic changes of measure rather than supplying just another sufficient condition.

## 33.24 The Same Paths and Three Changes That Must Not Be Confused

<a id="br-insight"></a>

The initial reweighting of one Gaussian increment has become a probability transformation on the same event space. Coordinates have not been redrawn path by path, yet fairness depends on weights and drift changes with them; quadratic variation survives finite-time equivalence. Reading by quadratic time instead turns a continuous local martingale into Brownian motion, but clock and noise need not be independent.

Representation draws another boundary: whether one Brownian noise represents every fair fluctuation depends on the information admitted to observation. Equivalent reweighting is different from adding new random information. These distinctions follow from the density martingale, quadratic clock and closed-space proofs, not a universal analogy about random worlds.

We can now change drift, reread quadratic time and understand martingales in continuous-noise information. Chapter 27’s paths also jump: a single jump’s product remainder does not shrink to a continuous bracket contribution, and an exponential may reach zero in one jump. What integral and decomposition can retain both continuous accumulation and discrete changes?

### Sources and Proof Scope

Conditions for characterization, time change, measure change and representation can be compared with Chapter 4 of [Tehranchi’s author notes](https://www.statslab.cam.ac.uk/~mike/StoCal/notes.pdf). Dubins and Schwarz’s On Continuous Martingales appeared in PNAS 53(5), 913–916 (1965); see the [original journal record](https://www.pnas.org/doi/10.1073/pnas.53.5.913). Girsanov’s original paper has its [journal record here](https://epubs.siam.org/doi/10.1137/1105027). This discovery sequence, dyadic embedding and technical organization are modern teaching reconstructions, not claims to reproduce historical thoughts or rewrite those papers paragraph by paragraph.

The main text contains the central calculations and proofs; [T-BROWNIAN-RELATIONS](../foundations/t-brownian-relations.md) completes stopping, terminating clocks, Gaussian coordinates, local representation and embedding moment estimates. The scope is continuous local martingales, finite-horizon equivalent changes of measure, representation in the usual natural Brownian filtration, and the specified Wiener/countable-Gaussian translations. This does not establish general jump Girsanov, every Gaussian Banach-space formulation or Chapter 39’s chaos theory.
