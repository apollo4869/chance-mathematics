# T-ROTATABLE: Finite Rotations and Infinite Gaussian Mixtures

We establish the rotational representation of real infinite sequences, not Chapter46 array representations. Tools are compact-group orbit conditioning, Chapter12 strong laws, Chapter24 tightness, Chapter43 directing laws and Chapter14 multivariate characteristic-function uniqueness. Return to [Chapter45](../chapters/45-invariance.md#rotation-sequences).

## 1. Where spherical probability comes from

<a id="rotatable-sphere"></a>

The group O(n) is closed and bounded in matrix space, defined by QᵀQ=I, hence compact metrizable. Its Haar pushforward to the unit sphere is the unique O(n)-invariant probability there. Independent standard normals Z₁,…,Zₙ have joint density depending only on squared norm; an orthogonal transformation has absolute Jacobian one, so their vector law is invariant. Its norm is almost surely nonzero, so Z/||Z|| is invariant and has exactly this spherical law. For n=1 it puts half mass on each endpoint.

\[ \sqrt n\,(U^{(n)}_1,\ldots,U^{(n)}_k)\ \stackrel d=\ \frac{(Z_1,\ldots,Z_k)}{\sqrt{n^{-1}\sum_{i=1}^nZ_i^2}}\ \longrightarrow\ (Z_1,\ldots,Z_k). \]

Construct the right side using one infinite normal sequence. The denominator tends almost surely to one by the strong law, proving convergence for each fixed k directly, rather than inferring it from a picture of a high-dimensional sphere.

## 2. Finite rotations retain a radius, not automatically a Gaussian law

<a id="rotatable-finite"></a>

Let a real vector X∈Rⁿ have O(n)-invariant law. Orbits are spheres of fixed norm and the origin; T-ORBITS gives the uniform spherical law conditional on radius. Thus an equal-in-law construction is X=RU, with arbitrary R=||X|| and independent uniform unit direction U, interpreting zero radius as zero. Finite-dimensional invariance does not force the Gaussian radial law.

A uniform unit-sphere vector is not a nonzero centered Gaussian scale mixture: at every positive scale a Gaussian norm is unbounded, whereas the spherical norm equals one. Requiring independent coordinates changes the conclusion. For n≥2 rotation makes the coordinates identically distributed and symmetric, with characteristic function φ. Independence and a two-dimensional rotation give φ(s)φ(t)=φ(√(s²+t²)). It is positive near zero, and repeated use of φ(t)=φ(t/√2)² makes it positive everywhere. The continuous function u↦log φ(√u) is additive on nonnegative reals, hence equals cu with c≤0. Thus φ(t)=exp(ct²), a centered Gaussian or point mass at zero. Independence supplies a genuine additional restriction.

## 3. Infinite compatibility first forces tightness of radial scales

<a id="rotatable-tightness"></a>

Call an infinite real sequence rotatable if every initial n-vector has O(n)-invariant law. Let Sₙ be the average of its first n squares, with no moment assumption. Finite-dimensional orbit conditioning gives the following first-coordinate law, with Sₙ and U independent on the right.

\[ S_n=\frac1n\sum_{i=1}^nX_i^2,\qquad X_1^2\stackrel d=S_n\,n(U^{(n)}_1)^2. \]

The spherical limit supplies c,δ>0 and n₀ such that P{nU₁²>c}≥δ for n≥n₀. Hence δP{Sₙ>K}≤P{X₁²>cK}. Since X₁ is a finite real random variable, the right side tends to zero as K tends to infinity. The finitely many smaller n are individually tight, so all laws of Sₙ are tight. This prevents escape of the radius without assuming a second moment.

## 4. Identifying every finite-dimensional limit

<a id="rotatable-mixture"></a>

Take a weakly convergent subsequence of Sₙ with limit V, a finite nonnegative real variable. For fixed k the law of the first k coordinates never changes and also equals √Sₙ times the first k scaled spherical coordinates. To pass through the random scale rigorously let ψₙ(v,t) be the characteristic function of that spherical vector at scale √v. The common-normal construction has denominator tending to one; uniformly for 0≤v≤K the exponential difference is bounded by min(2,√K||t||·||the first k normals||·|inverse denominator−1|). This tends almost surely to zero and is bounded by two, so ψₙ converges uniformly on compact v-intervals to

\[ \exp(-v\|t\|^2/2),\qquad \mathbb E\exp\!\left(i\sum_{j=1}^kt_jX_j\right)=\mathbb E\exp(-V\|t\|^2/2). \]

First truncate at Sₙ≤K, where the uniform error tends to zero; tightness controls the rest, and then K tends to infinity. The limit function is continuous and bounded in v, so weak convergence applies to its integral. Chapter14 multivariate uniqueness identifies every finite-dimensional law, and Chapter8 cylinder uniqueness identifies the infinite record law: sample V, then conditionally independent N(0,V) coordinates. The converse follows because each fixed-V Gaussian vector is orthogonally invariant and so is its mixture.

In the mixture construction the conditional strong law gives Sₙ tending to V almost surely for each finite V. Integrating over V proves the unconditional statement without requiring finite EV. Convergence is an event on record space, so the original sequence has an almost sure limit V*, whose law uniquely determines the mixing law. Its empirical measures also converge conditionally weakly to N(0,V*), identifying Chapter43 directing measure with this random Gaussian law; unify conditional identities on a countable determining class and extend.

The conclusion is not that rotational symmetry means independent Gaussians. An infinite rotatable sequence is a random-variance mixture of centered Gaussian sequences; nondegenerate V* retains common dependence. For example V* may independently take values one or four: coordinate squares share information about that scale and are dependent. Conversely iid Rademacher variables are exchangeable but not rotatable; a 45-degree rotation of two coordinates produces zero and absolute value √2, while original coordinates take only ±1.

For that two-point variance example, E[X₁²X₂²]=17/2 while E[X₁²]E[X₂²]=25/4, a difference of 9/4. This verifies dependence directly rather than merely appealing to the phrase shared hidden parameter.
