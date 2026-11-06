# Chapter 50: What Do We See from a Typical Random Point?

Pool the records of many spatial experiments. Half the experiments contain one point and half contain three. Select one occurrence uniformly from all occurrences in the pooled records. Its probability of coming from a three-point experiment is three-quarters, not one-half.

If instead we first choose a record uniformly and then choose one of its points, the answer remains one-half. The system has not changed; the sampling schemes give different weights to the same record. The phrase “choose a typical point” already conceals an unspecified probability experiment.

## 50.1 Does a Record Count Once or Three Times?

<a id="palm-sampling"></a>

Make the experiment precise. Let N equal one or three with equal probabilities, and conditional on N take independent uniform positions on [0,1]. Mark the record by Z=N and write \(\Xi=\sum_{i=1}^N\delta_{U_i}\). Sampling records gives P(Z=3)=1/2. Sampling pooled occurrences changes the law of Z to

\[ \mathbb P^{\rm occ}(Z=3)=\frac{\mathbb E[N\mathbf1_{\{Z=3\}}]}{\mathbb EN}=\frac{3/2}{2}=\frac34. \]

Uniformity of positions is not the issue. Even with identical location marginals, a record containing more occurrences offers more chances to be selected. We must record both the selected location and its full environment. Mean point density is insufficient, and the original configuration law is not automatically the law after selection.

## 50.2 Put Location and Environment in One Measure

<a id="palm-campbell"></a>

Let \(\Xi\) be a random Radon measure on E, with the locally compact second-countable metric assumptions of Chapter 49. The environment Z takes values in a standard Borel space S. It may be Ξ itself or include intensity, marks, and other information. For a location window A and environment event D define

\[ C(A\times D)=\mathbb E[\Xi(A)\mathbf1_{\{Z\in D\}}],\qquad \nu(A)=\mathbb E\Xi(A). \]

C is the Campbell measure. It is generally not normalized to be a probability. It counts each environment according to the mass it offers for selection. Nonnegative kernel integration and Tonelli make it countably additive, rather than merely a formula on rectangles. Its location marginal is ν. If ν is σ-finite, C is σ-finite too. Local finiteness of realizations does not ensure this mean condition; the finite random intensity of infinite mean from Chapter 49 remains a boundary example.

## 50.3 A Palm Kernel Comes from Disintegration

<a id="palm-disintegration"></a>

Once position and environment form a joint measure, ask for the environment law after separating the position. Assume σ-finite ν. Weight ν by a positive measurable w to make it finite, normalize wC, and apply the standard Borel disintegration of Chapter 10. Removing the weight, which depends only on location, gives

\[ C(dx,dz)=\nu(dx)Q_x(dz),\qquad \mathbb E\int g(x,Z)\Xi(dx)=\int\nu(dx)\int g(x,z)Q_x(dz). \]

Qₓ is the Palm probability kernel of the environment. [T-PALM](../foundations/t-palm.md#palm-kernel-construction) gives the full construction, measurability, and common-null-set argument. The conditioning belongs to the joint measure weighted by mass. It is not direct conditioning under the original probability on having a point at x, which usually has probability zero for a diffuse point process.

## 50.4 Versions May Vary; the Sampling Identity Does Not

<a id="palm-versions"></a>

The kernel is unique only ν-almost everywhere. Compare two kernels on finite-ν windows and a countable generating collection of environment events, combine their exceptional sets, and use probability uniqueness for every event. This makes the whole conditional law consistent at a location, without assigning a unique answer at every null location.

Mixing Qₓ with ν(dx)/ν(A) in a window of finite positive ν(A) recovers the environment law weighted by occurrences in that window. Counting each nonempty configuration once before selecting a point instead introduces a configuration-dependent normalization and a different law. Palm theory makes “typical” into a verifiable sampling identity, rather than just a name.

## 50.5 At a Multiple Root, Delete One Occurrence

<a id="palm-reduced"></a>

When the environment is the integer point process Ξ, Qₓ is supported on configurations with at least one occurrence at x. Define reduced Palm by \(Q_x^!=\mathcal L(\eta-\delta_x),\ \eta\sim Q_x\). Its central identity is

\[ \mathbb E\int g(x,\Xi-\delta_x)\Xi(dx)=\int Q_x^!g(x,\cdot)\nu(dx). \]

With k units at the root, reduction leaves k−1. Restriction to E∖{x} removes all k units and is another operation. The fixed-site double-daughter example of Chapter 49 now does more than distinguish clusters from Cox laws: deletion must refer to occurrences rather than distinct locations. General noninteger mass still has a Palm kernel, but no automatic operation of deleting one unit.

## 50.6 What Stationarity Leaves After Moving the Origin

<a id="palm-stationary-law"></a>

On \(\mathbb R^d\) put \(\theta_x\eta(A)=\eta(A+x)\), moving an occurrence at x to the new origin. This action is jointly continuous in the vague topology: shifted continuous tests share a compact support, and local mass bounds control uniform approximation. Let Ξ be stationary with mean λdx, 0<λ<∞. For a fixed environment event D, \(A\mapsto\mathbb E\int_A\mathbf1_{\{\theta_x\Xi\in D\}}\Xi(dx)\) is translation invariant and locally finite. Haar uniqueness from Chapter 45 makes it a constant multiple of volume. This yields a window-independent probability P⁰:

\[ \mathbb E\int g(x,\theta_x\Xi)\Xi(dx)=\lambda\int\mathbb E^0g(x,\eta)dx. \]

This is the stationary Palm distribution, with E⁰ denoting its expectation. A point process has at least one root occurrence, but general random mass need not have a root atom: the Palm version of deterministic length is still length. Stationarity need not be ergodicity and does not remove mixed environments. Finite positive intensity supplies the normalization; stationarity alone does not.

## 50.7 Adjacent Terms in the Poisson Series Fit Together

<a id="palm-mecke"></a>

Now compute a Palm law. Under finite intensity μ, draw K∼Poisson(μE) and then K independent locations. Summing over occurrences contributes k in the kth term, changing k/k! into 1/(k−1)!. The selected occurrence is integrated against μ(dx), while the remaining k−1 locations reassemble the original Poisson series. Consequently,

\[ \mathbb E\int g(x,N-\delta_x)N(dx)=\int\mathbb Eg(x,N)\mu(dx). \]

This is Mecke’s formula. Points need not occupy different locations: each occurrence contributes once and its own label is deleted, so atomic intensities are included. For σ-finite intensity, compute within finite-intensity pieces with the independent exterior as a parameter, then assemble using Tonelli. [T-MECKE](../foundations/t-mecke.md#mecke-finite) supplies the series calculation and assembly for all nonnegative joint tests.

## 50.8 How an Integral Identity Identifies a Whole Law

<a id="palm-mecke-character"></a>

Conversely, suppose a locally finite Ξ satisfies the identity with deterministic Radon μ. Tests independent of the remainder first give EΞf=μf. For \(f\in C_c^+\), set \(L(t)=Ee^{-t\Xi f}\), then substitute \(g(x,\eta)=f(x)e^{-tf(x)}e^{-t\eta f}\). The exponent introduced by deletion cancels:

\[ -L^{\prime}(t)=\mu(fe^{-tf})L(t),\qquad L(t)=\exp\{-\mu(1-e^{-tf})\}. \]

An integrating factor solves the equation, and Chapter 49 Laplace uniqueness identifies Ξ as Poisson. Finite EΞf dominates differentiation; no unbounded-test shortcut is hidden. This is a necessary and sufficient characterization, not merely a mean formula. Testing the remainder makes the identity much more informative than the first-order Campbell mean formula.

## 50.9 The Poisson Root: Add Once, Remove Once

<a id="palm-poisson"></a>

Comparing Mecke with reduced Campbell disintegration gives \(Q_x^!=\mathcal L(N)\) and \(Q_x=\mathcal L(N+\delta_x)\) for μ-almost every x. Any preexisting Poisson multiplicity at x remains. The homogeneous stationary version is \(P^0=\mathcal L(N+\delta_0)\). Conversely, this Palm identity for a stationary finite-intensity process yields Mecke through stationary Campbell and again characterizes Poisson law.

Adding a point is a proved law from the Poisson series, not a rule for all processes. For exactly n independent uniform points, reduced Palm has n−1 points while the original law has n. Other environments change the remaining world more substantially.

## 50.10 Why a Typical Event Favors High Intensity

<a id="palm-cox"></a>

Suppose N conditional on Λ is Poisson and ν=EΛ is σ-finite. Apply Mecke conditional on Λ, then disintegrate the Campbell measure of Λ. Reduced Palm is again a Cox mixture, but the directing intensity law is reweighted by the mass it supplies at the selected location. Adding a point to an original Cox sample alone is not the Palm computation.

\[ \Lambda=Z\mu,\quad0<\mathbb EZ<\infty\quad\Longrightarrow\quad P^*(dz)=\frac z{\mathbb EZ}P_Z(dz). \]

If Z originally equals one or three with equal probabilities, a typical event sees Z=3 with probability three-quarters. Generate the Poisson background conditional on this biased Z and finally add the selected occurrence to obtain full Palm law. Sampling changes the weight with which environments enter the sample, not the original system. The probability normalization is unavailable when EZ is infinite.

## 50.11 A Typical Daughter Brings Cluster Companions

<a id="palm-cluster"></a>

For point clusters generated by Poisson parents, first group daughter sums by parent occurrence. Mecke at parent level restores the whole selected cluster; other parents and daughters form an independent original-law background. Select an occurrence in the chosen cluster and delete it once to obtain reduced Palm. Poisson parents regenerate the background, but do not remove the selected daughter’s companions.

For parent intensity κdx and an independent finite cluster shape ζ with K occurrences, 0<EK<∞, total stationary intensity is κEK. Bias the shape law by \(K/EK\), choose V uniformly among its K occurrences, and add \(\theta_V\zeta^*\) to an independent background for full Palm law. If clusters are one or two repeated points at the parent, each with probability one-half, Palm root multiplicity two has probability two-thirds. [T-MECKE](../foundations/t-mecke.md#mecke-clusters) proves the general marked-cluster disintegration and calculation.

## 50.12 Returning from Occurrence Sampling to Location Sampling

<a id="palm-inversion"></a>

Palm calculations change the sampling direction. Can we recover the original law? For stationary random mass of finite positive intensity, choose positive continuous integrable h with ∫h=1. Then EΞh=λ, so Ξh is finite almost surely. On a nonzero configuration, \(\int h(x)\Xi(dx)/(\Xi h)=1\). Multiply F(Ξ) by this one and apply Campbell disintegration:

\[ \mathbb E[F(\Xi)\mathbf1_{\{\Xi\ne0\}}]=\lambda\int\mathbb E^0\frac{h(x)F(\theta_{-x}\eta)}{(\theta_{-x}\eta)h}\,dx. \]

Assign zero at exceptional denominators; Campbell ensures those pairs form a null set under the product being integrated. The inversion recovers the nonempty part. Empty configurations never offer selectable mass, so their probability must be retained separately. One can invert occurrence sampling, but cannot silently recover an unrecorded empty-sample weight.

## 50.13 Adjacent Points Partition the Line into Cycles

<a id="palm-cycle"></a>

For a stationary simple point process on the line, nonempty almost surely and of finite positive intensity, points are unbounded in both directions. Otherwise a maximum or minimum would have an impossible translation-invariant conditional probability law. Under Palm, the root is zero and the successor distance is T₁>0. Every location belongs to one half-open interpoint interval. Partitioning a spatial integral into these cycles gives

\[ \mathbb EF(\Xi)=\lambda\mathbb E^0\int_0^{T_1}F(\theta_t\eta)dt,\qquad \lambda\mathbb E^0T_1=1. \]

This length weight is not guessed from independent renewal cycles. It follows from Campbell for every stationary simple point process in this class. With empty configurations, the left side requires the nonempty indicator; one cannot automatically write 1=λE⁰T₁. Inversion hypotheses specify which realizations participate in normalization.

## 50.14 Cycle Laws and Time Laws Can Be Constructed Both Ways

<a id="palm-cycle-dual"></a>

Moving the root to its successor preserves Palm law. This is not taken on intuition. Assign nonnegative transport from each point to other points and apply Campbell to the same double sum from senders and receivers. The resulting mass-transport identity, with transport only to successors, proves invariance under rerooting.

Conversely, give a law Q on two-sided simple rooted configurations invariant under successor rerooting. If \(m=E_QT_1\in(0,\infty)\), define \(PF=m^{-1}E_Q\int_0^{T_1}F(\theta_t\eta)dt\). Length bias followed by a uniform origin inside the cycle constructs stationary P with intensity 1/m and Palm law exactly Q. [T-PALM-INVERSION](../foundations/t-palm-inversion.md#palm-cycle-suspension) proves both stationarity and Palm identification; checking only the first would not establish duality.

## 50.15 Renewal Epochs and Observation Times Share a Language

<a id="palm-renewal-main"></a>

In Chapter 19’s two-sided iid gap record, moving to the next arrival merely shifts indices, so it is a rerooting-invariant law Q. For strictly positive gaps of finite mean m, the preceding construction identifies the stationary renewal process and its Palm law. Length bias is now recognized as the independent-gap case of general time–cycle duality, rather than an isolated trick.

\[ \mathbb E\varphi(A,R)=\frac1m\mathbb E_Q\int_0^{L_1}\varphi(t,L_1-t)dt. \]

Age A and residual life R come from one internal cycle position, and the containing interval is length-biased. No nonarithmetic assumption is needed: real-time stationarity randomizes lattice phase. At infinite mean there is no finite m for probability normalization. What fails is this stationary probability construction, not every possible infinite-mean theory.

## 50.16 Palm Sampling Is Already Exact in a Finite Window

<a id="palm-window"></a>

Before relating Palm to small-window observation, avoid taking a limit too early. Write N=Ξ(B), m=EN=λ|B|, and p=P(N>0), with B bounded and of positive volume. Weight configurations by N/m, then select one occurrence X uniformly in B and observe θXΞ. This law is exactly P⁰ for every B. Stationary Campbell has already removed the location integral; no shrinking window is required.

A common different experiment merely conditions on B being nonempty, then selects X uniformly. Let its centered law be \(Q_B\). The decomposition \(N=\mathbf1_{\{N>0\}}+(N-1)^+\) gives an exact probability mixture, hence

\[ d_{\rm TV}(Q_B,P^0)\le\delta_B=\frac{m-p}{m}. \]

The error comes from counting a nonempty configuration once versus counting all its occurrences. The bound controls the entire recentered environment, not merely its window count.

## 50.17 Why One Local Approximation Has Two Topologies

<a id="palm-local"></a>

For a simple process with B inside a radius-r ball at zero, Campbell bounds δB by the Palm probability of at least two points within radius 2r. The root has exactly one point, and local finiteness keeps other points a positive distance away. The probability vanishes. Thus recentered \(Q_B\) converges in total variation, without even a second-moment assumption. For homogeneous Poisson, explicitly δB≤λ|B|/2.

Without recentering, conditioning on nonemptiness generally gives only weak convergence in the vague space. A diffuse Poisson conditional sample still has no point exactly at zero, whereas a Palm sample does. Their total variation distance stays one. The weak topology permits a root approaching zero, while the event of an exact root keeps distinguishing the laws. [T-PALM-APPROXIMATION](../foundations/t-palm-approximation.md#palm-local-simple) proves the error bounds and translation-continuity argument.

Multiplicities introduce a further failure: conditioning on nonemptiness misses cluster-size bias. In the one-or-two daughter-cluster example, conditional root multiplicity two tends to one-half, whereas Palm gives two-thirds. Recentring cannot repair the wrong weight. Local approximation must specify sampling, simplicity, and topology; it cannot be reduced to saying Palm is conditioning on a nearby point.

## 50.18 Nonstationary Locations Need Legitimate Versions

<a id="palm-local-kernel"></a>

For a Campbell kernel Qₓ with σ-finite ν, first fix a Polish topology on the environment space S and its Borel σ-algebra. If only a standard Borel structure is given, choose a Polish topology generating it; the weak convergence below refers to that choice. Partition locations into finite-ν pieces and use a countable Borel generating family to specify increasing partitions. For a cell A containing x define \(Q_A\)=C(A×·)/ν(A). This is a normalized window Palm average, without division at a zero-probability location. For countably many base opens of the environment, its readings are conditional expectations of Qₓ’s readings on increasing partitions. Closed-martingale convergence from Chapter 15 gives limits for one common kernel version outside one ν-null set, combined over finite unions of countable base opens; zero-mass cells receive a fixed probability.

Finite unions of base opens and Portmanteau upgrade the readings to \(Q_A\)⇒Qₓ. If Qₓ has a jointly measurable density relative to one fixed environment probability, product-space martingale convergence and Scheffé’s calculation upgrade this to total variation. Without common domination the upgrade fails: for one uniform random point, Palm at x is the deterministic singleton δₓ, while a window average gives that exact configuration probability zero. The [complete companion](../foundations/t-palm-approximation.md#palm-kernel-averages) retains the common-null-set and domination conditions, without claiming validity for arbitrary shrinking sets or every prescribed x.

## 50.19 The Original Law May Forbid the Remainder

<a id="palm-density-obstruction"></a>

Poisson remainders keep the original law, Cox remainders bias the environment, and cluster remainders retain companions. A natural next step is to try expressing reduced Palm as a density relative to the original configuration law P. This need not be possible.

Place exactly one uniform point on [0,1]. Its mean intensity is smooth length measure. Deleting the selected point leaves the empty configuration with certainty, while P never allows it. The environment probabilities are singular. A density for mean intensity does not imply a density for the remainder relative to the original environment. We must examine both location and remainder, rather than only first-order spatial intensity.

## 50.20 What a Papangelou Density Is Relative To

<a id="palm-papangelou"></a>

Choose a σ-finite reference m and let P be the law of Ξ. Only when \(C^!\ll m\otimes P\) does Radon–Nikodym provide a nonnegative jointly measurable c satisfying

\[ \mathbb E\int F(x,\Xi-\delta_x)\Xi(dx)=\mathbb E\int F(x,\Xi)c(x,\Xi)m(dx). \]

The function c is the Papangelou conditional intensity and the identity is GNZ. If \(\nu(dx)=\rho(x)m(dx)\), comparing the two Campbell decompositions gives \(Q_x^!(d\eta)=c(x,\eta)P(d\eta)/\rho(x)\) where 0<ρ<∞. Normalization is not guessed: testing with a constant environment gives ρ(x)=Ec(x,Ξ). At ρ=0 the formula does not determine a Palm version.

It describes the relative weight of inserting a spatial occurrence given a remainder. It is not the predictable compensator rate relative to a time filtration in Chapter 30. Sharing the words conditional intensity does not make the two objects identical. [T-GIBBS](../foundations/t-gibbs.md#gibbs-papangelou) proves existence from absolute continuity and the Palm-density duality, retaining the singleton counterexample.

## 50.21 From a Poisson Reference to Interaction Weights

<a id="palm-gibbs-finite"></a>

In a finite volume B with m(B)<∞, let πₘ be the reference Poisson law. For a measurable density p with ∫p dπₘ=1, assume heredity: once a configuration is forbidden, adding points keeps it forbidden. Mecke gives reduced Campbell density p(η+δₓ), so Papangelou on p>0 is the insertion density ratio. Heredity prevents a new remainder mass from appearing where the original law has zero density.

\[ P(d\eta)=p(\eta)\pi_m(d\eta),\qquad c(x,\eta)=\frac{p(\eta+\delta_x)}{p(\eta)}\quad(p(\eta)>0). \]

For example, take bounded activity z(x) and a symmetric nonnegative pair potential φ, weighting configurations by the product of activities times the exponential of negative energy. The empty configuration makes the partition function positive; the Poisson exponential moment makes it finite. Nonnegative potentials allow hard exclusion, with a conflicting insertion assigned weight zero. This is an existing finite Gibbs probability, not merely a formal exponential of energy.

## 50.22 How Insertion Rules Determine the Finite-Volume Law

<a id="palm-janossy"></a>

The converse requires proof too. Given the same bounded insertion intensity, GNZ relates the ordered n-point law on total count n to the n−1-point law after deletion. Janossy measure Jₙ records these complete finite-configuration readings, with recursion

\[ J_n(dx_1\cdots dx_n)=J_{n-1}(dx_1\cdots dx_{n-1})c\!\left(x_n,\sum_{i<n}\delta_{x_i}\right)m(dx_n). \]

Starting from the empty probability, iteration reconstructs every n-point density, and total probability one fixes the initial weight. If the empty probability were zero, the recursion would make every finite-n probability zero, a contradiction. Thus these rules uniquely determine the finite-volume Gibbs law. A symmetric pair potential also makes inserting x then y compatible with the reverse order. An arbitrary nonnegative c is not automatically a legal insertion rule for a probability.

## 50.23 Interior Laws Must Agree When the Exterior Is Fixed

<a id="palm-gibbs-kernels"></a>

Fix the exterior configuration ξ. Interior energy includes interactions within B and between B and its exterior. Normalizing relative to finite Poisson gives a probability kernel \(\Gamma_B\) that resamples the interior and retains the exterior. Parameter integration and evaluation measurability make it a genuine measurable kernel. For nonnegative potentials, the empty interior makes normalization legitimate even when exterior interactions are large.

For A⊂B, the Poisson reference is independent across the two pieces, and energy separates exactly into interior, exterior, and crossing terms. Normalization gives \(\Gamma_B\Gamma_A=\Gamma_B\). A full-space probability must additionally satisfy \(P\Gamma_B=P\), the DLR condition. This is not automatic existence from a consistent family of kernels. With finite-volume uniqueness, DLR and global GNZ are equivalent for the stated potentials. The proof conditions on exterior events and unifies null sets for countable tests, rather than relying on the appearance of the equations.

## 50.24 Infinite Volume Needs Tightness and Valid Limit Exchanges

<a id="palm-gibbs-existence"></a>

We establish a specific infinite-volume theorem: \(E=\mathbb R^d\), constant z>0, and \(\phi(x,y)=\psi(x-y)\), with ψ nonnegative, continuous, symmetric, and compactly supported. Use growing boxes with empty exteriors. Insertion intensities are at most z, and repeated GNZ gives factorial bounds on every compact K:

\[ \mathbb E(\Xi_n(K))_r\le(z|K|)^r,\qquad r\ge1. \]

First moments and Chapter 49 give tight measure laws; the closed integer subspace retains point configurations. To pass GNZ, continuity and finite range of the potential give local continuity of insertion functions, while second moments give uniform integrability for unbounded counts on the left. Expectations therefore pass legitimately to the limit. GNZ, conditioning, and finite-volume uniqueness give DLR. Translation averaging also yields a stationary Gibbs law. [T-GIBBS](../foundations/t-gibbs.md#gibbs-infinite-existence) contains the details.

This proves existence, not infinite-volume uniqueness. Hard exclusion and general measurable potentials handled in finite volume cannot be inserted into this continuous-limit proof without more work. Specifying rules, constructing finite kernels, proving consistency, obtaining an infinite probability, and proving uniqueness are different mathematical claims with different hypotheses.

## 50.25 Spatial Density, Sampling Weight, and Conditional Rules Differ

<a id="palm-three-densities"></a>

Three easily confused quantities can now be separated: mean spatial intensity ν, the Palm kernel of occurrence-sampled environments, and a Papangelou insertion density when absolute continuity holds. Campbell and GNZ relate them rigorously, but they carry different information. Poisson laws make some relations unusually simple. Fixed counts, mixed intensities, and clusters show why that simplicity is not a default rule for all random worlds.

Changing sampling does not physically alter the original system. It changes which environments have more opportunities to enter the observation record. Calculating that change requires weights, normalization, and conditional kernels. The mathematics makes what we observe into a precise, testable claim, rather than a universal philosophical statement about observers.

## 50.26 Typicality Is a Choice That Needs Proof

<a id="palm-insight"></a>

The opening three-point record still occurs with probability one-half. Three-quarters belongs to occurrence sampling. Campbell turns that finite calculation into a joint measure, disintegration gives Palm kernels, Mecke identifies the special regeneration structure of Poisson laws, inversion returns from event weights to spatial weights, and Gibbs theory establishes the compatibility and absolute continuity needed for insertion.

These results make a typical location and a typical occurrence objects that can be compared, calculated, and inverted. Long-term averages, intensities, and local conditioning cannot replace a sampling rule. Their differences become especially visible at multiplicities, empty configurations, mixed environments, and the boundary between weak and stronger convergence.

## 50.27 When Locations Are No Longer Recorded by Isolated Points

<a id="palm-next-question"></a>

Selecting an occurrence requires countable points or specified mass. Some experiments instead leave a random shape: the range of a curve, a reachable region, or a boundary. It may have neither a natural point count nor an assigned mass. If we only observe whether it meets a region, can we still build its probability and limit theory?

This is not achieved by merely dropping the measure symbol. New observations must determine which events are measurable and which spatial changes can be ignored. Studying typicality has shown why specifying the information to retain precedes choosing the mathematical object.

## 50.28 Complete Proofs and Scholarly Sources

<a id="palm-sources"></a>

The companions are [T-PALM](../foundations/t-palm.md), [T-MECKE](../foundations/t-mecke.md), [T-PALM-INVERSION](../foundations/t-palm-inversion.md), [T-PALM-APPROXIMATION](../foundations/t-palm-approximation.md), and [T-GIBBS](../foundations/t-gibbs.md). Campbell disintegration assumes σ-finite mean; stationary probabilities require finite positive intensity; cycle duality concerns simple nonempty processes on the line; infinite-volume Gibbs existence uses the stated continuous nonnegative finite-range potentials. General-group inversion, non-σ-finite Palm probabilities, and the broadest Gibbs existence and uniqueness do not follow automatically.

Mecke’s [1967 original paper](https://doi.org/10.1007/BF00535466) studies stationary random measures on locally compact Abelian groups. Technical scope is also compared with the [Last–Penrose author manuscript](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf) and the [publisher’s chapter in Kallenberg’s third edition](https://doi.org/10.1007/978-3-030-61871-1_32). Organizing the chapter around sampling differences is a modern mathematical reconstruction, not a claimed personal discovery sequence, and references do not replace the proofs above.
