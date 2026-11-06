# T-ERGODIC-DECOMPOSITION: Ergodic Decomposition on a Standard Borel Space

This page completes [§41.13](../chapters/41-ergodic-theory.md#ergodic-decomposition). Let (E,B) be standard Borel, T a Borel map and P an invariant probability. Construct kernels on the Borel sigma algebra and interpret completed conditional expectations afterward. The result is an almost-everywhere kernel decomposition, not an exception-free classification of all starting points.

## 1. Turning invariant information into a conditioning parameter

<a id="decomposition-proof-parameter"></a>

Choose a countable generating algebra A={A_j}, containing E and closed under finite set operations. Choose Borel representatives h_j=E[1_{A_j}|I] with values in [0,1]. Completed variables have Borel representatives since completion only adds null sets. Put H=(h_j), taking values in [0,1]ᴺ, and G=σ(H). Each h_j is invariant modulo P, so G⊂I modulo P.

Conversely, for B∈I approximate 1_B in L²(P) by simple functions g_n from A; indicator monotone classes and finite-measure approximation give this density. Conditional contraction makes E[g_n|I] converge to 1_B in L². Each is a finite linear combination of the h_j and hence G-measurable. The limit has a G-measurable version. Thus I and G agree modulo P, without claiming that every sigma algebra is literally countably generated.

## 2. Three common null sets for the conditional kernel

<a id="decomposition-proof-kernel"></a>

Chapter 10 gives a regular conditional kernel K(z,dx) given H. Set P_ω=K(H(ω),·). The identities P_ω(A_j)=h_j(ω) hold simultaneously on one full-measure set. Integration gives P(A)=∫P_ω(A)P(dω), first on the algebra and then by π–λ.

Also P_ω{H(x)=H(ω)}=1 almost everywhere. Given H, membership of each h_j in an interval with rational endpoints is determined, so its conditional kernel assigns the same zero or one to these countably many tests. Remove their common null set and use the intervals to separate distinct real values. This yields equality of every coordinate, rather than merely equality in distribution.

For A_j and C∈I, preservation gives ∫_C1_{T⁻¹A_j}dP=∫_C1_{A_j}dP. Thus P_ω(T⁻¹A_j)=P_ω(A_j) almost everywhere. After intersecting countably many sets, P_ω∘T⁻¹ and P_ω agree on the algebra, hence everywhere by π–λ. The retained kernels are truly invariant; we have not chosen a different exceptional ω for every Borel set.

## 3. Why the conditional kernels really are ergodic

<a id="decomposition-proof-ergodicity"></a>

Birkhoff for the countably many indicators gives a full P-set outside N where all averages converge to h_j(x). Since P(N)=0, disintegration gives P_ω(N)=0 almost everywhere. Intersect with the common sets above. For P_ω-almost every x, Aₙ1_{A_j}(x) converges to h_j(ω), a constant in x.

Bounded convergence also gives L² convergence under P_ω. The mean ergodic theorem applies to this now-proved invariant probability, identifying E_{P_ω}[1_{A_j}|I(P_ω)] as constant. Algebraic simple functions are dense in each L²(P_ω), so continuity of projection makes every invariant variable constant. Invariant indicators then prove ergodicity. This avoids a common gap: an event invariant modulo P_ω need not be invariant modulo the original P; events cannot simply be transferred between the two completions.

## 4. Integrable readings, uniqueness and a countable factor of an arbitrary space

<a id="decomposition-proof-scope"></a>

For a specified f∈L¹(P), Tonelli makes P_ω|f| finite almost everywhere, and its kernel integral represents E[f|G]=E[f|I]. Countably many specified readings admit a common null set. Another conditional kernel for the same G agrees on the countable algebra by uniqueness of conditional expectation, then on all Borel sets by π–λ. Relabelling the parameter or changing kernels on null starting points does not affect this measure-theoretic uniqueness.

On an arbitrary probability space, a problem involving only countably many f_j and their forward translates factors through Φ(ω)=(f_j(Tᵏω))_{j,k}, a countable product of real lines satisfying Φ∘T=S∘Φ. The pushforward law is standard Borel and preserving, and all readings under study are recovered on this factor. A subadditive theorem can therefore be proved there and pulled back without asserting regular disintegration of the original space itself. This is the legitimate use of decomposition on the next page. [Return to the text](../chapters/41-ergodic-theory.md#ergodic-subadditive).
