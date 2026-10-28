# Why Do All Subsets of Null Sets Change the Measurable World?

Chapter 5 extends length to measure but leaves two questions requiring complete answers: why Lebesgue measurable sets really outnumber Borel sets, and how an arbitrary measure incorporates previously nonmeasurable subsets of null sets. This companion provides the constructions and the set-theoretic proof.

<a id="t-measure-completion"></a>

## T-MEASURE.1 Completion of an arbitrary measure

Let \((S,\mathcal F,\mu)\) be any measure space. Put \(\mathcal N=\{N:N\subseteq Z\in\mathcal F,\ \mu(Z)=0\}\), and define \(\overline{\mathcal F}=\{A\triangle N:A\in\mathcal F,N\in\mathcal N\}\). Here \(\triangle\) is symmetric difference; \(N\) need not yet belong to \(\mathcal F\). Equivalently, \(E\in\overline{\mathcal F}\) precisely when old measurable sets sandwich it as \(A\subseteq E\subseteq B\), with \(\mu(B\setminus A)=0\).

The forms are equivalent. If \(E=A_0\triangle N\), with \(N\subseteq Z\) and \(\mu Z=0\), use the lower set \(A_0\setminus Z\) and upper set \(A_0\cup Z\). Conversely, a set sandwiched between \(A,B\) differs from \(A\) by a subset of \(B\setminus A\). Complements satisfy \(E^c=A_0^c\triangle N\). The symmetric difference between a countable union and the corresponding old measurable union is contained in \(\bigcup_nN_n\subseteq\bigcup_nZ_n\). Thus \(\overline{\mathcal F}\) is a \(\sigma\)-algebra containing \(\mathcal F\).

Define \(\overline\mu(A_0\triangle N)=\mu(A_0)\). If \(B_0\triangle M\) is another representation, then \(A_0\triangle B_0\) lies in an old measurable null set. Deleting that null set makes \(A_0,B_0\) equal; additivity shows that adding or removing a measurable null set does not change a measure. The definition is therefore independent of representation, including when \(\mu(A_0)=\infty\); no infinite subtraction is used.

Countable additivity still needs proof. If the sets \(E_i=A_i\triangle N_i\) are disjoint, choose old null sets \(Z_i\supseteq N_i\). Their old measurable cores \(C_i=A_i\setminus Z_i\) lie inside \(E_i\), hence are disjoint, and \(\mu C_i=\mu A_i\). The difference between \(\bigcup_iE_i\) and \(\bigcup_iC_i\) lies in the old null set \(\bigcup_iZ_i\). Consequently,

\[
\overline\mu\Bigl(\bigcup_iE_i\Bigr)=\mu\Bigl(\bigcup_iC_i\Bigr)=\sum_i\mu(C_i)=\sum_i\overline\mu(E_i).
\]

If \(\overline\mu(E)=0\), its representation places \(E\) inside the old measurable null set \(A_0\cup Z\). Every subset of \(E\) therefore belongs to \(\overline{\mathcal F}\) and has measure zero. This proves completeness. Any complete extension of the old measure must contain all these null subsets, hence must contain \(\overline{\mathcal F}\). The sandwich bounds force its values there to equal \(\overline\mu\). Completion is thus the smallest complete extension, with unique values on that smallest domain. No σ-finiteness is used.

<a id="t-measure-cantor"></a>

## T-MEASURE.2 A null set large enough to contain a continuum

Start with \([0,1]\) and repeatedly remove the open middle third of every remaining interval. At stage \(n\), the union \(C_n\) consists of \(2^n\) closed intervals of length \(3^{-n}\). Put \(C=\bigcap_nC_n\). It is closed and \(m(C)\le(2/3)^n\) for every \(n\), hence \(m(C)=0\).

Every binary sequence \(b=(b_1,b_2,\ldots)\in\{0,1\}^{\mathbb N}\) gives \(x(b)=\sum_{n\ge1}2b_n3^{-n}\in C\). If two sequences first differ at \(k\), their initial difference has magnitude \(2\cdot3^{-k}\), while the entire remaining tail can cancel at most \(3^{-k}\). Their points are distinct. This injection avoids the usual endpoint ambiguity of general ternary expansions.

The set of binary sequences is \(\mathcal P(\mathbb N)\), whose cardinality is denoted \(\mathfrak c\). A real number is encoded by its lower cut in the rationals, so \(|\mathbb R|\le\mathfrak c\); the injection just constructed gives the reverse inequality. Thus \(|C|=|\mathbb R|=\mathfrak c\). The continuum hypothesis is not being assumed.

The cardinal comparison used here has a direct proof. Given injections \(f:A\to B\), \(g:B\to A\), put \(A_0=A\setminus g(B)\), \(A_{n+1}=g(f(A_n))\), and \(U=\bigcup_{n\ge0}A_n\). On \(U\), set \(h=f\); elsewhere set \(h=g^{-1}\), which is defined because those points are outside \(A_0\). Each part is injective and their images are disjoint: if \(b=f(x)\), \(x\in U\), then \(g(b)\in U\), so the other part cannot also produce it. If \(b\notin f(U)\), then \(g(b)\notin U\), and the second part maps that point to \(b\). Thus \(h:A\to B\) is bijective. This proves the Cantor–Bernstein principle.

<a id="t-measure-borel-code"></a>

## T-MEASURE.3 Why there are at most continuum many Borel sets

The phrase “countably many operations on countably many intervals” is not itself a cardinality proof, because iteration may continue beyond countably many prescribed levels. Use well-founded operation trees. Enumerate the rational-endpoint open intervals. A code is a countable tree whose nodes are finite integer strings: leaves carry basic intervals, and internal nodes carry complement or countable-union operations. Infinite descending branches are forbidden.

Interpret each well-founded tree upward from its leaves. Formally, leaves have rank 0 and a parent has rank the supremum of its children’s ranks plus 1; evaluate sets recursively by rank. All these ranks are countable ordinals, since each node has countably many children and the tree is countable. If repeatedly removing ranked nodes left a remainder, each remaining node would have a remaining child; successive choices would produce an infinite branch, a contradiction. Thus the recursion covers the whole tree. This uses countable choice and well-founded recursion in the usual ZFC set theory.

The class of coded sets contains the basic intervals and is closed under complements and countable unions: add a root above one tree or countably many existing trees. Any infinite branch would continue infinitely in one of those subtrees, so the new tree remains well founded. Hence every Borel set has a code. Conversely, recursion on rank shows that every code evaluates to a Borel set.

The set of finite integer strings is countable. A tree and its node labels can be encoded by a subset of a countable set. Thus there are at most \(2^{\aleph_0}=\mathfrak c\) codes and at most \(\mathfrak c\) Borel sets. Every singleton is closed, giving at least \(\mathfrak c\) Borel sets. This counts all Borel sets, rather than only finitely many construction levels.

<a id="t-measure-strict"></a>

## T-MEASURE.4 The final step to strict inclusion

Cantor’s diagonal argument shows that no set \(E\) maps onto \(\mathcal P(E)\): if \(F\) were such a map from \(E\), put \(D=\{x\in E:x\notin F(x)\}\). The equality \(D=F(d)\) would imply \(d\in D\) exactly when \(d\notin D\). Hence \(|\mathcal P(C)|>\mathfrak c\).

Every subset \(A\) of an outer-null set \(N\) is outer-null. For any \(E\), monotonicity and subadditivity give \(m^*(E)=m^*(E\setminus A)\) and \(m^*(E\cap A)=0\). Thus the Carathéodory splitting identity holds and \(A\) is Lebesgue measurable. All subsets of \(C\) are therefore measurable, whereas at most \(\mathfrak c\) of them are Borel. Consequently,

\[
\mathcal B(\mathbb R)\subsetneq\mathcal L(\mathbb R).
\]

This is an existence proof, not an asserted explicit formula for a non-Borel subset. Its mechanism is the strict cardinality gap between all subsets of a null set and all Borel operation codes. Both classes already contain uncountably many sets.

<a id="t-measure-lebesgue-completion"></a>

## T-MEASURE.5 Lebesgue measure is the completion of Borel length measure

It remains to show that completion misses no Lebesgue measurable sets. Let \(E\) be Lebesgue measurable with finite measure. From the interval-cover definition, choose a countable cover with total length less than \(m(E)+\varepsilon/2\). Enlarge the \(k\)-th interval slightly to an open interval, with the total added length less than \(\varepsilon/2\). Their union is open, satisfies \(O\supseteq E\), and has \(m(O)\le m(E)+\varepsilon\). This follows directly from outer measure, without invoking a regularity theorem.

Choose open \(O_n\) with \(\varepsilon=2^{-n}\), and let \(B=\bigcap_nO_n\). Then \(B\) is Borel, satisfies \(E\subseteq B\), and \(m(B)=m(E)<\infty\), so \(m(B\setminus E)=0\). Apply the same open-cover construction to the null set \(B\setminus E\), obtaining a Borel null superset \(Z\). Thus \(E=B\setminus N\), where \(N\subseteq Z\), precisely a member of the completed Borel measure space.

For a general Lebesgue measurable \(E\), use its finite-measure intersections with \([-n,n]\). Each belongs to the completion, hence so does their countable union. Conversely, Borel sets are Lebesgue measurable and Lebesgue measure is complete. Both measures agree on old Borel sets, so the general completion construction also fixes their values.

An incomplete probability space is therefore not contradictory; it simply has not adjoined every null subset. Chapter 8 constructs probabilities first on the cylinder-generated structure, and Chapter 10 uses standard Borel state spaces for conditional kernels, for specific reasons. A later completion requires care about domains and measurable versions; differing on a null set is not blanket permission to declare an arbitrary function measurable. See the exact [null-modification principle](t-integral.md#t-integral-null).
