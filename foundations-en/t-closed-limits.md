# T-CLOSED-LIMITS: Capacities and Weak Convergence of Random Closed Sets

Return to [Chapter 51](../chapters/51-random-closed-sets.md#sets-convergence). Use the LCSC metric setting and proper metric ρ of T-FELL; empty sets are allowed. Weak convergence is on its proved compact Polish Fell space, not a synonym for convergence of every compact-hit reading.

## 1. What Portmanteau Actually Says

<a id="closed-portmanteau"></a>

For open U write \(T^\circ(U)=P(F\cap U\ne\varnothing)\). Countable inner compact approximation gives \(T^\circ(U)=\sup_{K\subset U,\ K\text{ compact}}T(K)\), using an increasing compact sequence obtained from an exhaustion and distance from E∖U. Since \(H_U\) is open and \(H_K\) closed, Chapter 24 gives

\[ F_n\Rightarrow F\quad\Longrightarrow\quad\liminf_nT_n^\circ(U)\ge T^\circ(U),\qquad\limsup_nT_n(K)\le T(K). \]

If compact K satisfies \(T(K)=T^\circ(\operatorname{int}K)\), the open-hit lower bound and compact-hit upper bound squeeze Tₙ(K) to T(K). The exceptional event is that F hits K but not its interior, not membership of some chosen position. General compacts need not satisfy this: Fₙ={1/n} tends to {0}, while Tₙ({0})=0 and T({0})=1.

## 2. Capacity Continuity Tests Determine Weak Limits

<a id="closed-capacity-convergence"></a>

Theorem: for a given random closed set F, Fₙ⇒F exactly when Tₙ(K)→T(K) for every compact satisfying the preceding capacity-continuity condition. Necessity was proved. Sufficiency requires more than saying capacity is unique. Compactness and Chapter 24 Prokhorov give a weakly convergent further subsequence from every subsequence; call its law Q. We must identify Q.

For nonempty compact K put \(K^r=\{x:\rho(x,K)\le r\}\), r>0, which is compact. Let D be the infimum distance between F and K, with D=∞ for empty F. Properness makes a finite infimum attained within a bounded region, so {D≤r}=H(Kʳ), also proving measurability. Hitting Kʳ without hitting its interior forces D=r, since {ρ(x,K)<r} lies in that interior. D has at most countably many finite atoms. Thus all but countably many r give valid continuity tests; choose such rⱼ decreasing to zero.

For the subsequential limit Q, Portmanteau and test convergence give \(Q(H_{K^r})\ge T(K^r)\) and \(Q(H_{\operatorname{int}K^r})\le\liminf_nP(F_n\cap\operatorname{int}K^r\ne\varnothing)\le T(K^r)\). Hence Q(\(H_K\))≤T(Kʳ); letting rⱼ decrease to zero gives Q(\(H_K\))≤T(K). Conversely the compact-hit bound and decreasing compact continuity of both laws give Q(\(H_K\))≥T(K). Both sides vanish for empty K. T-CHOQUET identifies Q with Law(F). Every subsequence has the same further limit, proving convergence of the whole sequence.

## 3. A Candidate Capacity Still Needs Existence

<a id="closed-candidate"></a>

If only a candidate T is given, first verify the normalization, complete alternation, and decreasing continuity of T-CHOQUET; only then apply the preceding theorem. Convergence Tₙ→T on all compacts is sufficient when T satisfies those conditions, but is not necessary. For example Fₙ={n} tends to ∅ in Fell topology although every realization is nonempty. Compactness of the hyperspace permits the entire shape to escape to infinity; it does not imply convergence of nonemptiness probabilities. On noncompact E, nonemptiness is not automatically a continuity event.

## 4. Check the Actual Operation Before Mapping

<a id="closed-mappings"></a>

Chapter 24 continuous mapping applies to finite unions, proper continuous spatial maps, and translations proved in T-FELL. Combining two random sets first requires joint weak convergence, not merely two marginal convergences. Intersection, complement, support, and infinite-time range do not qualify by name: T-FELL gives the intersection counterexample, and T-RANDOM-SHAPES treats support and ranges. Complements are generally open, so are not even objects of the same state space.
