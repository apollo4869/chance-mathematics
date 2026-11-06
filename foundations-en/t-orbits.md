# T-ORBITS: Orbits, Conditional Probabilities and Common Versions

Let G be a compact metrizable group acting continuously on a nonempty Polish space E, and let m be its constructed two-sided Haar probability. We prove orbit disintegration for this continuous compact-group setting; the quotient of an arbitrary measurable action is not silently assumed standard Borel. Return to [Chapter45](../chapters/45-invariance.md#orbit-question).

## 1. Making an orbit a legitimate measurable parameter

<a id="orbit-quotient"></a>

Start with a bounded complete compatible metric d on E and put d*(x,y)=sup over g of d(gx,gy). This is an invariant metric and dominates d. If xₙ tends to x, compactness of G and continuity give sup d(gxₙ,gx) tending to zero: otherwise a convergent subsequence of offending gₙ gives a contradiction. Thus d* is compatible. A d*-Cauchy sequence has a d-limit, then converges in d* by compatibility, so d* is complete. Separability is retained.

\[ Q=E/G,\qquad q(x)=Gx,\qquad \bar d(qx,qy)=\min_{g\in G}d^*(x,gy). \]

Compactness attains the minimum; zero distance means the same orbit, and invariance combines two group elements to prove the triangle inequality. The map q is continuous and open, and the image of a countable dense set is dense. For a Cauchy sequence in Q take a subsequence with consecutive distances below 2 to the negative nth power. Recursively choose representatives with these summable d* distances. Completeness gives a limit of representatives, hence convergence of the original Cauchy sequence. Thus Q is Polish.

We also need q to map closed sets to closed sets. If q(xₙ) tends to q(x) with xₙ in closed F, choose gₙ with d*(xₙ,gₙx) tending to zero. A subsequence in compact G tends to g, and then xₙ tends to gx∈F. Hence q(x)∈q(F). This will be used for a measurable section.

## 2. A measurable section and the precise invariant information

<a id="orbit-section"></a>

Choose countably many d*-dense points aⱼ. For an orbit o recursively take the least jₙ for which the orbit meets all previously selected closed balls and the closed ball B(aⱼ,2 to the negative nth power) simultaneously. Density ensures existence. Each test asks whether o belongs to q(F), with F a finite intersection of closed balls, so it is a closed-set test. Splitting over the countably many finite histories proves jₙ is Borel.

The selected centers are Cauchy: every later stage has a point of the orbit in both its selected ball and each previous selected ball, so the centers are at distance at most the sum of radii. Their limit s(o) lies in that compact orbit because the distances to it tend to zero. Measurability of pointwise limits gives a Borel section s with q(s(o))=o.

\[ \mathcal I_G=\{A\in\mathcal B(E):gA=A\ \forall g\in G\}=q^{-1}\mathcal B(Q). \]

The inclusion from right to left is immediate. If A is invariant, then A=q⁻¹(s⁻¹(A)), which proves the converse. We have not confused each orbit being Borel with solving the measurable structure of the entire quotient: the constructed section supplies that step. Completing under a probability P later does not change the almost sure meaning of the corresponding conditional expectations.

## 3. Orbit probabilities and group averages

<a id="orbit-kernel"></a>

\[ \eta_x(A)=\int_G\mathbf1_A(gx)\,m(dg),\qquad Pf(x)=\int f(gx)\,m(dg)=\eta_x f. \]

For every x, ηₓ is a probability; for every Borel A, joint measurability of the action and Chapter10 kernel integration make x↦ηₓ(A) measurable. Right Haar invariance gives ηₕₓ=ηₓ, while left Haar invariance gives ηₓ(hA)=ηₓ(A); the two directions are distinct. Its support is in the compact orbit Gx. The measurable section makes o↦\(\eta_{s(o)}\) a probability kernel from Q to E, without trying to unify arbitrary RCD versions over uncountably many x.

The operator P preserves constants and positivity and satisfies P²=P, since the first average is already constant along each orbit. If μ is G-invariant, bounded f and invariant A satisfy ∫A Pf dμ=∫A f dμ by Fubini and deterministic invariance. Thus Pf is conditional expectation given the invariant σ-field. Truncate positive and negative parts and use integral contraction to extend this to L¹.

\[ \mu(A)=\int_Q\eta_{s(o)}(A)\,(\mu\circ q^{-1})(do),\qquad \mathbb P\{X\in A\mid q(X)\}=\eta_X(A)\quad\text{a.s.} \]

Conversely any mixture of these orbit probabilities with a probability on Q is G-invariant. An invariant probability concentrated on one orbit must be η: averaging at every point gives that same η and integrating proves uniqueness. Thus orbit conditioning is not merely an available version; under these hypotheses invariance forces its conditional law.

## 4. How conditional kernels of a jointly invariant law transform

<a id="orbit-equivariant"></a>

Suppose G also acts continuously on a nonempty Polish space F, and the joint law of (X,Y) is invariant under simultaneous action. Chapter10 first gives any Borel conditional kernel K for X given Y=y. Define the following averaged kernel at every y. Joint measurability follows from (g,y,z)↦\(\mathbf1_A\)(g⁻¹z) and the kernel K(gy,dz), not from pretending that a set varying with g is a fixed test.

\[ \bar K(y,A)=\int_G\int_E\mathbf1_A(g^{-1}z)K(gy,dz)\,m(dg). \]

It is a probability at every y and is a Borel kernel. Test it against bounded φ(y), transform the law of Y by g, use invariance of that law and then of the joint law; the tested integral of K(gy,gA) becomes E[φ(Y)\(\mathbf1_A\)(X)]. Averaging over g proves the conditional-kernel identity. No intersection of the exceptional null sets for all g is required.

\[ \bar K(hy,hA)=\bar K(y,A)\quad(h\in G,\ y\in F,\ A\in\mathcal B(E)). \]

Substitute k=gh and use right Haar invariance to verify this pointwise. This is equivariance, not invariance at fixed y under every h; the latter follows only when hy=y. If G acts trivially on F, each conditional kernel is invariant. For the original K one normally gets an almost sure identity for each fixed h only; that cannot be upgraded without proof to one common pointwise version.

## 5. Choosing a transformation using the information retained

<a id="orbit-adaptive"></a>

If X has G-invariant law and a:Q→G is Borel, then a(qX)X has the same law as X. Conditional on qX=o the element a(o) is fixed, and η is invariant under it; integrating the kernel identity proves the claim. Dependence on the observed orbit is allowed, but arbitrary dependence on the position within that orbit is not. Reflecting a standard normal X according to its sign to produce |X| is a counterexample: a two-point orbit retains only absolute value, and choosing the positive sign uses exactly the information removed by orbit averaging.

Compactness and continuity are genuine hypotheses. For a general measurable action on a standard Borel space, even if each transformation preserves probability, the orbit quotient need not have this Polish structure, so one cannot simply write a regular conditional law given the orbit. A noncompact group also lacks a normalizable Haar probability, so the averaging formulas do not carry over. Chapter10 disintegration given a specified standard Borel statistic is a different claim from arbitrary orbit parameters being legitimate.

There is a concrete noncompact counterexample. Give the countable group Q/Z the discrete topology and let it act on the circle by rational rotations. Circle Haar probability λ is invariant, but every orbit is countable and λ-null. For a Borel A invariant under all rational rotations, the finite measure λ(A∩·) has the same invariance. Its integrals of continuous tests depend continuously on rotation, so density gives invariance under all circle rotations. Compact-group uniqueness gives λ(A∩·)=λ(A)λ, hence λ(A)=λ(A)². The invariant σ-field is λ-trivial although many orbits remain.

If a measurable standard Borel-valued q exactly distinguished these orbits, triviality of σ(q) would force q to be almost surely constant: its law takes only zero or one on a countable determining class, and intersecting the corresponding full-probability sets leaves at most one point. One countable orbit would then have λ-mass one, a contradiction. Thus an arbitrary orbit quotient cannot simply be inserted in a regular conditional-probability formula; the quotient construction for compact continuous actions is substantive.
