# T-ARRAYS: A Complete Proof of Shared-Index Conditional Independence and Finite-Order Representation

We prove shared-subset uniform representations for jointly exchangeable relation arrays of any fixed finite order with nonempty standard Borel values, including repeated indices and diagonals. First we prove an unordered-subset version carrying all lower-order marks, then encode ordered relations. T-ARRAY-VARIANTS separately proves the separately exchangeable case. Tools are Chapter8 countable experiments, Chapter9 L² projections, Chapter10 standard Borel kernels and randomization, and T-DIRECTING-MEASURE probability parameter spaces; Chapters47 and49 are not used. Return to [Chapter46](../chapters/46-arrays.md#arrays-proof-mechanism).

## 1. Exact statement and the measurable tools actually required

<a id="arrays-proof-statement"></a>

Fix an integer r≥0 and nonempty standard Borel spaces S₀,…,Sᵣ. Let Zₐ take values in \(S_{|a|}\) for every finite a⊂N with |a|≤r, including Z∅. Joint exchangeability means every finite permutation π preserves the law of the whole family (Zπa). There are Borel functions fₗ, invariant under local vertex relabeling, giving the following joint law. All \(U_b\) are independent Uniform(0,1); a subset b uses one \(U_b\), not a fresh one whenever it appears inside another a.

\[ (Z_a)_{|a|\le r}\ \stackrel d=\ \left(f_{|a|}\big((U_b)_{b\subseteq a}\big)\right)_{|a|\le r}. \]

Identify local inputs with subsets of [|a|] using any enumeration of a; invariance makes the result independent of that enumeration. At r=0, randomization of the single Z∅ by one uniform proves the result. The following induction step establishes rather than assumes conditional independence.

Chapter10 kernel randomization can be chosen as \(\Gamma_S\):P(S)×(0,1)→S. Encode S by a Borel isomorphism into a Borel subset of [0,1], form quantiles from rational CDF evaluations and repair outputs outside the code using a fixed point. For every probability the repair concerns a uniform-null section; the function is Borel on all parameters. The standard Borel evaluation structure on P(S) was proved in [T-DIRECTING-MEASURE](t-directing-measure.md#directing-proof-space). Assigning a fixed value at uniform endpoints extends randomization to the closed interval without changing any law. Thus Γ depends on the probability itself, not on a description of its kernel.

## 2. How projection norms detect additional information

<a id="arrays-proof-projection"></a>

For 𝓖⊂𝓗 and V∈L², projection gives the following Pythagoras identity. Equality of the two projection norms therefore proves equality of the conditional expectations themselves.

\[ \|\mathbb E[V\mid\mathcal H]-\mathbb E[V\mid\mathcal G]\|_2^2=\|\mathbb E[V\mid\mathcal H]\|_2^2-\|\mathbb E[V\mid\mathcal G]\|_2^2. \]

We will also compare projections onto different data fields with equal joint distributions. Their norms depend only on the joint law of (V,Y), since optimal square prediction has the following form. The data Y may be countably infinite; its value space remains standard Borel and Doob–Dynkin factorization applies.

\[ \|\mathbb E[V\mid\sigma(Y)]\|_2^2=\sup_{h\text{ bounded Borel}}\{2\mathbb E[Vh(Y)]-\mathbb E[h(Y)^2]\}. \]

Completing the square gives the upper bound; truncations of a measurable version of the actual conditional expectation attain the supremum. Equality of norms under relabeling below is therefore a precise projection identity, not an informal assertion of equal information.

## 3. Reserving an infinite background without encoding an ordering bias

<a id="arrays-proof-reservoir"></a>

Assume the result for r−1. Relabel the index set as two countably infinite sets N and R. A bijection to the original index set constructs all data; each finite target marginal has its original law because a finite injection extends to a finite permutation. This also proves invariance under any index injection: verify finite cylinders, then use countable product uniqueness.

Independently add iid continuous marks Rᵢ∼Uniform(0,1) to the level-one labels; within this induction step continue to call the enlarged level-one space S₁, then project back to the original labels at the end. All marks are distinct on one probability-one event, by a countable union over pairs. Field inclusions in this proof are understood modulo P, adjoining ambient null sets when needed; sorting on this common full-measure event suffices for the L² projections. For a⊂N with |a|<r form a background record Yₐ containing every \(Z_c\) with |c|≤r and c∩N⊂a, together with all auxiliary marks in R and a. Order the vertices of a by their auxiliary marks; enumerate R once and for all.

Precisely, for |a|=l index the record by b⊂[l] and finite d⊂R with |b|+|d|≤r, with values in \(S_{|b|+|d|}\), and include the l sorted marks and the background mark sequence. Its space \(T_l\) restricts only finite sorting conditions and is a Borel subspace of a countable standard Borel product; the image of all realizable records is not assumed Borel without proof. Fix arbitrary labels on the null tie inputs. Auxiliary marks make Yₐ an object without an external ordering bias: when N is relabeled the marks move with vertices and internal ordering is unchanged. Thus (Yₐ) is an ordinary subset-exchangeable family, rather than a family with an unspecified additional coordinate action.

For r≥2 singleton records give the mark of each named vertex. Hence from (\(Y_b\)) for b⊊e one can recover every \(Z_c\) whose positive part c∩N is a proper subset of e, by locating its sorted coordinates; the converse is immediate from the records. For r=1 the local data consist solely of Y∅, exactly the background. There is also a fixed Borel projection from Yₐ to original Zₐ: its coordinate using all l positive positions and no background position. These details make the next σ-field inclusions genuine.

## 4. A projection sandwich by moving other vertices into the background

<a id="arrays-proof-independence"></a>

Fix an r-set e⊂N and V=f(\(Z_e\)), with bounded real Borel f. Let 𝓖 be generated by (Yₐ:a⊊e), and 𝓗 by all lower-order Yₐ and any finitely many top-level \(Z_b\) whose index differs from e. Then 𝓖⊂𝓗. Split R into infinite T and R∖T, and choose an injection γ fixing e pointwise, mapping R bijectively onto T and N∖e bijectively onto R∖T. Injection invariance gives the same joint distribution of V and the data generating 𝓗 before and after this transformation.

Call the transformed data field 𝓙. A record Yₐ uses at most r−1 positive vertices, so its image still misses at least one vertex of e; the image of another r-set b≠e cannot equal e either. Every transformed datum therefore uses a proper subset of e and some R indices. The auxiliary marks needed for sorting are already in 𝓖 as well. Thus 𝓙⊂𝓖; we do not need or assert equality.

\[ \|\mathbb E[V\mid\mathcal G]\|_2\le\|\mathbb E[V\mid\mathcal H]\|_2=\|\mathbb E[V\mid\mathcal J]\|_2\le\|\mathbb E[V\mid\mathcal G]\|_2. \]

The equality follows from equal joint laws and the projection formula. Pythagoras proves E[V|𝓗]=E[V|𝓖]. For finitely many distinct r-sets, peel off the last factor and use the tower property repeatedly. Given all lower-order records, top-level variables are conditionally independent, and the conditional law of \(Z_e\) depends only on (Yₐ:a⊊e). During the iteration the other conditional-kernel factors are already measurable in all records, so the same conditional-expectation identity remains applicable.

\[ \mathbb E\left[\prod_{e\in A}h_e(Z_e)\,\middle|\,(Y_a)_{|a|<r}\right]=\prod_{e\in A}K_{h_e}\big((Y_a)_{a\subsetneq e}\big),\qquad A\text{ finite}. \]

## 5. From conditional expectations to one common measurable kernel

<a id="arrays-proof-kernel"></a>

For e=[r], Chapter10 gives a regular conditional kernel K(v,·) from local data v=(\(Y_b\):b⊊[r]) to Sᵣ. The local data space is a finite standard Borel product; its law and its joint law with \(Z_{[r]}\) are invariant under the permutation group on r vertices. Average K over this finite group to get a Borel probability kernel K* everywhere, with K*(σv,A)=K*(v,A) for all parameters, permutations and Borel A.

The average remains a conditional-law version: test bounded local functions, change variables in each term and use joint invariance. Exchangeability makes the same K* work for every e after an enumeration of its vertices. Each Sᵣ has a countable generating algebra. Remove one null set for these tests, all r-sets and all finite families of r-sets, then use two monotone-class extensions for general Borel tests. This gives a genuine common conditional product law rather than unrelated versions for uncountably many tests.

## 6. Completing the induction while sharing each subset noise

<a id="arrays-proof-induction"></a>

The family (Yₐ:|a|<r) satisfies the induction hypothesis and thus has a simultaneous representation using independent \(U_b\) with |b|<r. For every r-set e form its local record \(v_e\) through those functions, and use a fresh independent \(U_e\) to define \(Z'_e=\Gamma(K^*(v_e),U_e)\). Conditional on all lower-level uniforms these variables have precisely the preceding product law. Integrating over lower-level uniforms restores the full joint law of the records and top-level data. Recover original lower-level Zₐ by their fixed record projections.

Local invariance of K*, invariance of the inductive functions and Γ depending only on the probability make the new top function locally invariant on all inputs too. Auxiliary-mark ties were null in the original law, whose distribution is preserved, so decoding is valid off one countable common null set. Forget the added marks to finish the induction. Every function is a composition of Borel projections, finite sorting, kernel integration and measurable randomization.

For the converse, any finite permutation π leaves (\(U_{\pi b}\)) an independent uniform family. Local invariance of the functions identifies the transformed outputs exactly with \(Z_{\pi a}\). Thus the construction is jointly exchangeable. Both directions are proved: every such exchangeable law has a representation, and every displayed construction is exchangeable, not merely the latter.

## 7. Complete decoding of ordered relations and repeated indices

<a id="arrays-proof-ordered"></a>

Now take a jointly exchangeable array \(X_{i_1,\ldots,i_d}\) of finite order d, allowing repeated indices. Add independent continuous marks Rᵢ. For each a with 1≤|a|=l≤d, order its vertices a₁,…,\(a_l\) by their marks, and store \(X_{a_{v(1)},\ldots,a_{v(d)}}\) for every surjection v:[d]→[l] as one \(S_l\)-valued label Zₐ. There are finitely many such maps. At l=1 also store the vertex mark. Use a singleton empty label. This multilevel subset family is jointly exchangeable with finite standard Borel product value spaces.

Apply the theorem just proved. For a target ordered tuple take its support a. The represented singleton labels give the Rᵢ of each named vertex; sort them, locate the tuple’s surjection coordinate and read it from represented Zₐ. Use a fixed value on ties. Since original marks are distinct, decoding is almost surely correct in the represented law as well; there are countably many tuples, so one common null set suffices. This proves that each equality pattern uses the noises of all subsets of its support, without dismissing directions or diagonals as similar cases.

\[ X_{ij}=F(U_\varnothing,U_{\{i\}},U_{\{j\}},U_{\{i,j\}})\ (i\ne j),\qquad X_{ii}=D(U_\varnothing,U_{\{i\}}). \]

In two dimensions this is the full directed Aldous–Hoover representation with diagonals: the reverse edge uses the same unordered-pair noise and reverses the vertex inputs. For an originally symmetric array, store a single pair value; the resulting F is symmetric in its two vertex inputs. Edges independent only conditional on vertices still share those vertex inputs rather than resampling them for every edge.

## 8. Scope and conclusions that cannot be added

<a id="arrays-proof-scope"></a>

We have proved jointly exchangeable standard Borel relation families of any fixed finite order and every repetition pattern. Finitely many relation types can be stored together in finite product labels. We do not claim coverage of uncountably many relation types, nonstandard Borel targets or arbitrary infinitary relations. The representation is equality of array laws, not a claim that the original space already contains the independent U, or that a representing function and its latent variables are uniquely observable. The following three companions prove multitype separate exchangeability, extremality and function identification.
