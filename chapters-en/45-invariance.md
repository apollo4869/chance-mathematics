# Chapter 45: What Does Symmetry Actually Preserve?

Draw a random point on the unit circle. Rotating the paper may leave its probability law unchanged. But if we first look at the point and then rotate it to the top, the result is a single deterministic point. Every individual operation is a legitimate rotation; the resulting laws differ.

Now unfold the circle into an infinite line. The circle can have no preferred direction, yet the line cannot assign the same positive probability to every unit interval. Seemingly similar absence of a preferred location demands different mathematical answers. We need to specify not just how symmetric an object looks, but which transformations are allowed, how they are selected and what information those choices retain.

## 45.1 Rotating the paper versus moving the point to the top

<a id="symmetry-choice"></a>

Describe a point on the circle by its angle θ, added modulo 2π. If θ is uniform by length on [0,2π), then θ+a is uniform for every a specified in advance. Check lengths of arcs under translation and use measure uniqueness for all Borel sets.

\[ \mathbb P\{\theta+a\in A\}=\mathbb P\{\theta\in A\}\quad\text{for each fixed }a. \]

Choosing a=−θ makes the transformed point identically zero. No individual rotation failed to preserve length; the rotation acquired a particular dependence on the point being rotated. A probability identity for fixed a does not permit arbitrary substitution of a data-dependent value. This small example will persist throughout the chapter: symmetry constrains laws without licensing every observation rule.

## 45.2 Transformations must compose and must be measurable

<a id="measurable-action"></a>

Two successive rotations should equal one rotation; there must be doing nothing and undoing an operation. These requirements give a group G: associative multiplication, identity e and inverses. We need it to record composition accurately, not to attach a vocabulary to probability in advance. A left action on an object space E satisfies

\[ ex=x,\qquad (gh)x=g(hx). \]

Equip E and G with σ-fields. Measurable multiplication, inversion and the jointly measurable map (g,x)↦gx allow random transformations of random objects and their laws. Measurability for each fixed g alone is insufficient for random substitution. Our general measurable arguments use standard Borel groups and nonempty standard Borel E. Haar construction uses compact metrizable or locally compact Polish topological groups; orbit disintegration separately assumes a continuous action on a Polish space.

## 45.3 The law is invariant, not every sample point

<a id="invariant-law"></a>

\[ g_*\mu(A)=\mu(g^{-1}A),\qquad g_*\mu=\mu\quad(g\in G). \]

This defines a G-invariant probability. It does not require gx=x: almost every point on the circle moves. Nor does it require independent coordinates: a sequence constantly equal to one random Z is invariant under every finite permutation and retains complete dependence. Chapter43 identified directing probabilities for infinite permutation-invariant records; we now vary the permitted transformations and determine what each forces.

Translations, permutations and orthogonal rotations preserve different structures. Translations preserve position differences, orthogonal maps preserve inner products and lengths, and permutations preserve repetitions of values in finite samples. There is no universal ladder on which more randomness means more symmetry; a conclusion acquires meaning only after its action is specified.

## 45.4 How finite averages suggest a continuous average

<a id="haar-question"></a>

For a finite group, equal averaging over every transformation gives a choice favoring no element. For an infinite group we cannot divide one by the number of elements. The circle has length, but an arbitrary compact group need not come with coordinate volume; O(n) consists of orthogonal matrices and has zero ordinary volume in matrix space. We need to construct a probability from the transformations themselves.

\[ m(gA)=m(A),\qquad m(G)=1. \]

The first requirement says left multiplication does not alter the choice; the second makes it a probability. Such an m is Haar probability. We now prove existence and uniqueness on compact metrizable groups, rather than treating uniform choice of a group element as a pre-existing random experiment.

## 45.5 Constructing an average favoring no direction

<a id="compact-construction"></a>

Start with a possibly very uneven ρ, requiring only positive masses on every point of a dense sequence. Multiply independent such transformations and average the distributions at the first N possible numbers of steps, including zero steps at the identity.

\[ \nu_N=\frac1N\sum_{j=0}^{N-1}\rho^{*j},\qquad \rho*\nu_N-\nu_N=\frac{\rho^{*N}-\delta_e}{N}. \]

Compactness supplies a weakly convergent subsequence with limit m; the right side tends to zero on bounded tests, giving ρ*m=m. This is only stationarity under a single averaged transformation. To obtain every individual invariance, set u(x)=∫f(xy)m(dy) for continuous f. Then u(x)=∫u(xh)ρ(dh). The function attains its maximum on compact G; equality of the average to that maximum forces every point seen by ρ to have the maximum. Full support and continuity force u to be constant on G.

Thus ∫f(xy)m(dy)=∫f(y)m(dy), which is left invariance. Compactness has two substantive roles: preventing escape of probability subsequences and attaining a maximum. Neither guarantee survives unchanged on the real line. The full limit and measure identification are in [T-HAAR, Section1](../foundations/t-haar.md#haar-compact).

## 45.6 Why left averaging also controls the right

<a id="haar-two-sided"></a>

Left and right multiplication differ in a noncommutative group; calling both translations does not identify them. Push m forward by inversion to get a right invariant probability r. For any left invariant probability ν, evaluate one double integral in the two orders, using a different invariance in each.

\[ \iint f(xy)\,r(dx)\nu(dy)=\nu(f)=r(f). \]

Thus ν=r. Taking ν=m makes m right invariant as well, and every other left invariant probability equals it. Uniqueness and two-sided invariance are proved together. On a finite group each element gets mass 1/|G|, on the circle the measure is dθ/(2π), and on O(n) it is a probability determined by the group structure rather than independent uniform choices of matrix entries.

## 45.7 What information survives averaging

<a id="orbit-question"></a>

After all rotations of a planar vector, length remains but direction is no longer retained. The orbit Gx records this range of transformed versions. An observable event A is invariant information when gA=A. For a general action, naming an orbit does not by itself license conditional probability; its quotient may not satisfy Chapter10 regular conditional distribution hypotheses.

Fix a compact metrizable G acting continuously on Polish E. Take a bounded complete compatible metric d, take its supremum over all group elements to obtain an invariant d*, and minimize distance between orbits. Compactness prevents distinct orbits sticking at zero distance; successive close representatives prove completeness of the quotient. Thus E/G is Polish.

\[ d^*(x,y)=\sup_{g\in G}d(gx,gy),\qquad \bar d(Gx,Gy)=\min_{g\in G}d^*(x,gy). \]

Countably many dense balls also select a Borel representative of every orbit. Hence invariant Borel events are exactly pullbacks by q(x)=Gx. The full metric, measurable section and σ-field arguments are in [the first two sections of T-ORBITS](../foundations/t-orbits.md#orbit-quotient), rather than replacing quotient construction by the statement that each orbit is measurable.

## 45.8 How probability must be distributed given an orbit

<a id="orbit-conditional"></a>

\[ \eta_x(A)=\int_G\mathbf1_A(gx)\,m(dg),\qquad Pf(x)=\int_G f(gx)\,m(dg). \]

The measure ηₓ is a probability on the orbit, measurable in x and the same for every point on one orbit. It is also invariant under G. If μ is invariant, integrating Pf over an invariant event A and exchanging integration orders gives the integral of f over A. Thus group averaging is not merely a smoothing trick: it is exactly conditional expectation given invariant information.

\[ Pf=\mathbb E_\mu[f\mid\mathcal I_G],\qquad \mathbb P_\mu\{X\in A\mid q(X)\}=\eta_X(A)\quad\text{a.s.} \]

The identity P²=P holds because a second average removes no additional within-orbit information. Mixing these η with any probability on the quotient gives an invariant μ, and every invariant μ has this disintegration. For planar rotations the random radius is arbitrary, but conditional on a positive radius the direction must be uniform. The center is a singleton orbit; there is no need to assign an identifiable angle at radius zero.

## 45.9 Invariance versus equivariance of a conditional kernel

<a id="conditional-equivariance"></a>

If the joint law of (X,Y) is invariant under simultaneous transformation, its conditional law given Y=y need not be invariant on its own. Take X=Y uniform on a circle: given Y we know X, so its conditional law is a point mass, which should move when Y is rotated. The required relation is K(hy,hA)=K(y,A), called equivariance.

For compact G acting continuously on nonempty Polish spaces of X and Y, Chapter10 supplies any conditional kernel K. Define the following. It is a probability kernel at every y and satisfies the common equivariance relation for every h,y,A.

\[ \bar K(y,A)=\int_G K(gy,gA)\,m(dg),\qquad \bar K(hy,hA)=\bar K(y,A). \]

The first expression means integrating \(\mathbf1_A\)(g⁻¹z) against K(gy,dz), which ensures joint measurability. Testing against bounded functions of Y and using joint invariance proves it is still a conditional kernel; the second equality follows pointwise by right Haar substitution. The [full kernel proof](../foundations/t-orbits.md#orbit-equivariant) avoids intersecting exceptional null sets over uncountably many group elements. Only when G acts trivially on Y does equivariance reduce to invariance of each conditional probability.

## 45.10 Why the line does not permit the same probability average

<a id="noncompact-line"></a>

If a translation-invariant probability existed on the line, every half-open interval [n,n+1) would have the same mass c. Positive c makes total mass infinite; zero c makes the countable union, the entire line, have mass zero. Both are impossible. The problem is not failure to find a clever density: the requirement contradicts finite total mass and countable additivity.

Length remains a translation-invariant measure, but cannot be normalized into probability on the whole line. In a general noncompact locally compact group, disjoint translates of a positive-mass relatively compact open U give the same contradiction. Compact-group probability and noncompact local measurement must separate here.

This does not forbid probability-preserving actions of a noncompact group on other spaces. Rational rotations by a discrete group preserve circle probability, yet their orbit quotient does not inherit the compact-group construction. See the counterexample in [T-ORBITS](../foundations/t-orbits.md#orbit-adaptive).

## 45.11 How Haar measure exists on a locally compact group

<a id="local-haar"></a>

On a locally compact Polish group we may require finite mass on compact sets, positive mass on nonempty open sets and left invariance, while allowing infinite total mass. Haar measure exists in this setting and is unique up to a positive factor. Since total mass one is not a general normalization, first choose a nonzero nonnegative compactly supported continuous f₀. Once Haar measure has been constructed, divide by its positive integral of f₀ to obtain the normalization with integral one.

The construction starts without any unknown group integral. Cover nonnegative compactly supported f by finitely many left translates of g and minimize the sum of coefficients; divide by the cost of covering f₀. As the support of g shrinks, the ratio of two functions varies little on each small piece. A cover of their sum can then be split proportionally, turning subadditivity of costs into additivity in the limit.

\[ I_g(f)=\frac{\inf\{\sum c_i:f\le\sum c_i g(a_i^{-1}\,\cdot)\}}{\inf\{\sum c_i:f_0\le\sum c_i g(a_i^{-1}\,\cdot)\}}. \]

Countable dense tests and a diagonal subsequence give a positive linear functional. Local boundedness is not global boundedness, so the companion uses a strictly positive decaying weight to obtain the bounded positive-functional representation proved in Chapter28, then divides the weight back out to produce a locally finite Radon measure. [T-HAAR, Sections2–5](../foundations/t-haar.md#haar-covering) supplies all steps of asymptotic additivity, representation and uniqueness up to scale.

## 45.12 Why right translation may change a left invariant measure

<a id="modular-function"></a>

A right translate of left Haar is still left invariant, so uniqueness forces right translation to change only a scalar factor. A modular function requires an explicit convention; ours is

\[ \mu(Ag)=\Delta(g)\mu(A),\qquad \int f(xg)\,\mu(dx)=\Delta(g)^{-1}\int f\,d\mu. \]

Two right translations give Δ(gh)=Δ(g)Δ(h), and an integral ratio for a compactly supported continuous test proves continuity. Two-sided invariance means Δ is identically one. Abelian and compact groups have this property, but a noncommutative noncompact group need not. For a general action relative invariance can be written μ(gA)=χ(g)μ(A); quasi-invariance, which merely preserves null sets, is weaker. These are not interchangeable forms of probability invariance.

## 45.13 A computable example combining dilation and translation

<a id="affine-example"></a>

\[ (a,b)(c,d)=(ac,b+ad),\quad a,c>0,\qquad d\mu_L=\frac{da\,db}{a^2},\quad d\mu_R=\frac{da\,db}{a},\quad \Delta(c,d)=c^{-1}. \]

The element (a,b) represents x↦ax+b. Left multiplication by fixed (a,b) has Jacobian a², canceled by the squared new first coordinate. Right multiplication by fixed (c,d) has Jacobian c, so the left density gains a factor 1/c. The right density has only a first power in its denominator and cancels that right Jacobian. The distinction is an actual change-of-variables effect, not a notation preference.

On the line one may also use e^(κx)dx: translating A to a+A multiplies its mass by e^(κa). This is a relatively invariant measure, not a translation-invariant probability. Allowing a factor enlarges possible measurements while recording exactly which weights the transformation fails to preserve.

## 45.14 Is deleting records without reordering genuinely weaker?

<a id="spreadability"></a>

Finite permutations form a group action. Taking a subsequence at strictly increasing indices generally has no inverse and is no longer a group action, yet its invariance can still be studied. An infinite sequence is spreadable if every deterministic infinite subsequence has the original law. Exchangeability implies spreadability, but the converse is not apparent: no subsequence has directly swapped two positions.

Infinitude connects them. Spreadability first gives stationarity. Average k bounded functions over k successive blocks of length N. Every term in the expanded product uses increasing indices, so its expectation equals that at the first k positions. By Chapter41 each long-block average converges to its invariant conditional average; their product no longer distinguishes the order of the functions.

\[ \mathbb E\prod_{j=1}^k f_j(X_j)=\mathbb E\prod_{j=1}^k\mathbb E[f_j(X_1)\mid\mathcal I]. \]

Rectangle tests give exchangeability and Chapter43 then gives its directing probability. This Ryll-Nardzewski-type result shows that apparently fewer subsequence symmetries can force all finite permutation symmetries for an infinite sequence. The [full block-average proof](../foundations/t-predictable-symmetry.md#sampling-spreadable) also identifies invariant conditional averages with the directing measure; it does not classify arbitrary stationary processes as exchangeable.

## 45.15 When an observer may skip a record

<a id="sampling-question"></a>

Deterministic subsequence invariance has not answered random sampling. In an iid μ sequence, keeping the first occurrence of a desired result plainly favors that result. The right information restriction is to decide whether to keep observation n before seeing it. Suppose the conditional law of Xₙ given 𝓕ₙ₋₁ is μ; take increasing, almost surely finite selection times satisfying

\[ \{\tau_j=n\}\in\mathcal F_{n-1}. \]

Split the final selected fₖ(Xτₖ) over {τₖ=n}. Previous selected outcomes and the current selection decision are already in 𝓕ₙ₋₁, so conditional integration replaces fₖ by μ(fₖ). Sum over n and induct backward in k: the selected sequence remains iid μ. The first head is a stopping time but fails the condition and always selects a head. Allowing selection never to occur and then conditioning on success can also bias the law.

For an exchangeable sequence repeat the argument conditional on its director ν. The selected records remain conditionally iid ν, retaining the original exchangeable law. Fresh observations must still have conditional law ν given the enlarged past; future outcomes cannot be smuggled into the information. See the [complete predictable skipping proof](../foundations/t-predictable-symmetry.md#sampling-skipping).

## 45.16 The boundary between prior and retrospective rotation

<a id="predictable-transform"></a>

Instead of deleting observations, transform each new noise. If μ is G-invariant, fresh Xₙ has law μ conditional on the past and gₙ is decided from that past, conditional integration gives the following. It preserves each conditional law and, by iteration, the entire iid law.

\[ \mathbb E[f(g_nX_n)\mid\mathcal F_{n-1}]=\int f(g_nx)\,\mu(dx)=\mu(f). \]

A fresh normal vector block may be multiplied by an orthogonal matrix chosen from previous records and remains the same normal noise. Choosing the matrix after seeing that block and rotating it to the first coordinate axis changes its law. A function-monotone-class argument for the conditional kernel makes random gₙ substitution legitimate; invariance under each fixed matrix alone is not the proof.

## 45.17 Some transformations depending on current data remain legitimate

<a id="orbit-adaptation"></a>

The preceding result does not mean every data-dependent transformation fails. For compact-group invariant X, selecting a(qX) from its orbit alone preserves its law. Conditional on the orbit, a is fixed and the orbit probability is invariant under it. For a rotationally invariant planar point, choosing an angle based on radius is legitimate, while always rotating its present direction to the top is not.

The issue is not the word adaptive, but the precise relation between information used for selection and conditional invariance. The [last section of T-ORBITS](../foundations/t-orbits.md#orbit-adaptive) proves the orbit-based rule; [T-PREDICTABLE-SYMMETRY](../foundations/t-predictable-symmetry.md#sampling-transform) proves prior noise transformations. They use different information and need not be forced into one slogan.

## 45.18 Finite rotations leave an arbitrary radius

<a id="rotation-finite"></a>

The orbits of O(n) on Rⁿ are spheres and the origin. Orbit disintegration writes every invariant vector in law as RU, with uniform unit direction U independent of an arbitrary nonnegative radius R. An independent standard normal vector Z has radial density, so Z/||Z|| constructs U explicitly.

This is not yet Gaussianity. A uniform unit-sphere point has norm exactly one and is not a nonzero Gaussian scale mixture. With the additional assumption of independent coordinates, however, two-dimensional rotation forces the common characteristic function to satisfy φ(s)φ(t)=φ(√(s²+t²)); logarithms give a continuous additive function and hence a centered Gaussian. Rotation and independence are different assumptions. See [T-ROTATABLE, Section2](../foundations/t-rotatable.md#rotatable-finite) for the calculation.

## 45.19 How infinite compatibility forces a Gaussian mixture

<a id="rotation-sequences"></a>

An infinite real sequence is rotatable when each initial n-vector has O(n)-invariant law. A single n allows an arbitrary radius, but all radii must belong to one infinite record, not be chosen independently for each dimension. Let Sₙ be the mean of the first n squares. Finite-dimensional orbit representation gives

\[ S_n=\frac1n\sum_{i=1}^nX_i^2,\qquad (X_1,\ldots,X_k)\stackrel d=\sqrt{S_n}\,\sqrt n\,(U^{(n)}_1,\ldots,U^{(n)}_k)\quad(n\ge k), \]

The variables Sₙ and U may be taken independent on the right. Normalizing independent normals shows that the first k spherical coordinates multiplied by √n tend to independent standard normals. We must also prevent escape of Sₙ; E Sₙ cannot be used without a second moment. Choose c,δ>0 so that P{nU₁²>c}≥δ for large n. Then δP{Sₙ>K}≤P{X₁²>cK}. The right side tends to zero and gives precisely the needed tightness.

Take a weak limit V of Sₙ. Truncate the scale to a compact interval, use uniform approximation of the spherical characteristic functions there, then control tails. This identifies every finite-dimensional characteristic function.

\[ \mathbb E e^{i\sum_{j=1}^kt_jX_j}=\mathbb E e^{-V\sum_{j=1}^kt_j^2/2},\qquad (X_j)_{j\ge1}\stackrel d=(\sqrt V Z_j)_{j\ge1}, \]

Here V is finite and nonnegative, the Zⱼ are independent standard normals independent of V, and finite EV is not required. The converse is checked at every fixed V. The complete tightness, limit interchange and uniqueness proof is in [T-ROTATABLE](../foundations/t-rotatable.md#rotatable-tightness). This is narrower than an exchangeable mixture of arbitrary probabilities: more permitted transformations restrict the director to a random member of the centered Gaussian family.

## 45.20 Averages identify scale without necessarily removing it

<a id="rotatable-information"></a>

In the mixture construction the conditional strong law gives Sₙ tending almost surely to V. This is a statement on record space, so the original sequence has the same observable limit and the variance mixing law is unique. If V is random, all coordinates carry it jointly and are not thereby unconditionally independent. Chapter41 retained random averages now have a new precise form: the retained information is the variance of the directing Gaussian.

An iid ±1 sequence is exchangeable but does not allow arbitrary orthogonal mixing of two coordinates: a 45-degree rotation produces zero and ±√2. A random-variance Gaussian sequence allows all such mixtures while retaining dependence through its common scale. Together these examples show that symmetry does not mean absence of dependence; it determines the structure into which dependence is compressed.

## 45.21 Symmetry is a choice that must be specified

<a id="symmetry-insight"></a>

Averages on a circle, infinite length on the line, left-right factors in the affine group and random Gaussian scale in infinite records arise from different transformation requirements. They do not prove that the world is intrinsically uniform. They let us test what an exact assumption permits, excludes and retains.

The two ways of rotating our original circle are now distinguished: a fixed prior transformation, one chosen from orbit information and one erasing the observed current position have different information conditions. Group averaging gives conditional expectation, predictable choices preserve conditional laws, and counterexamples mark their limits. If observations instead record a relation for every pair of objects, what common information survives relabeling? One must specify which indices are transformed before copying a sequence director onto a whole network of relations.

## 45.22 Historical sources and complete proof routes

<a id="symmetry-sources"></a>

Haar’s [1933 paper](https://doi.org/10.2307/1968346) concerns measure on continuous groups. Our organization through compact-group random-step averages, local covering costs and kernels is a modern reconstruction, not a reenactment of that paper or the uniquely possible historical discovery. The locally compact proof is completed within the stated Polish scope; the nonmetrizable general theorem is not counted as proved here.

For the classical background of spreadability and exchangeability see Ryll-Nardzewski’s [1957 paper](https://doi.org/10.4064/cm-4-2-149-156). The Gaussian scale-mixture theorem for infinite rotatable sequences is commonly called Freedman’s theorem; the research paper [Rotatable random sequences in local fields](https://arxiv.org/abs/1903.02058) distinguishes that classical real result from its local-field extension. We prove only the real sequence version, not array or local-field representations.

The complete proofs are [T-HAAR](../foundations/t-haar.md), [T-ORBITS](../foundations/t-orbits.md), [T-PREDICTABLE-SYMMETRY](../foundations/t-predictable-symmetry.md) and [T-ROTATABLE](../foundations/t-rotatable.md). The main text retains the maximum principle for averages, orbit conditional expectation, long-block averages, predictable-selection slicing and radial tightness. The companions complete local representation, common kernel versions and limit identification without moment assumptions.
