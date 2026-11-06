# T-GRAPHONS: Random Graphs, Finite Patterns and Nonunique Representations

We prove finite-cylinder equality criteria for standard Borel representations and the graphon connection, nonuniqueness and identifiable information for binary symmetric loopless graphs. A graphon is not silently used as a definition encompassing all directed, weighted and sparse models, and no general coordinate-isomorphism classification is claimed. Return to [Chapter46](../chapters/46-arrays.md#arrays-graphon).

## 1. Finite cylinders give a complete equality-in-law criterion

<a id="graphon-proof-cylinders"></a>

Choose a countable generating algebra 𝓐 of E containing E. For a separate representation F and a finite rectangle with Aᵢⱼ∈𝓐 in each cell, compute the following integral. For joint exchangeability use one vertex pool, a common W for reverse edges and tests of D on the actual diagonal.

\[ I_F((A_{ij}))=\int\prod_{i=1}^m\prod_{j=1}^n\mathbf1_{A_{ij}}\big(F(z,u_i,v_j,w_{ij})\big)\,dz\,d\mathbf u\,d\mathbf v\,d\mathbf w. \]

Two representations give the same array law exactly when all these countably many integrals agree. Necessity is the cylinder probability identity. Sufficiency uses finite-dimensional rectangle π–λ, then cylinder uniqueness for the countable array. Single-cell marginals, row laws, a few low-order moments or any finite list of tests are insufficient. This criterion allows standard Borel values and includes diagonals and directions without requiring pointwise equality of functions.

## 2. From pair randomization to a graphon

<a id="graphon-proof-representation"></a>

Let X be a jointly exchangeable {0,1}-valued graph with Xᵢⱼ=Xⱼᵢ and Xᵢᵢ=0. T-ARRAYS supplies symmetric F. Define W(z,u,v)=∫1{F(z,u,v,w)=1}dw. It is jointly Borel, symmetric in u,v and takes values in [0,1]. Conditional on global and vertex inputs, distinct unordered edges are independent with success probabilities W, so threshold construction gives the same law.

\[ X_{ij}=\mathbf1\{W(U_0,U_i,U_j)>W_{\{i,j\}}\},\quad i\ne j;\qquad X_{ii}=0. \]

Strict versus nonstrict threshold does not change probabilities because pair uniforms are continuous and independent. For fixed z, W(z,·,·) is a graphon; global mixing permits a random graphon. This means a jointly Borel parameter family evaluated at a random parameter, not an assumed measurable choice on a quotient of function spaces. If the graph law is dissociated, T-ARRAY-ERGODIC permits fixing a good z, so one deterministic graphon suffices. This is a probability kernel, not a claim that one sampled finite adjacency matrix is its unique graphon.

## 3. How ordinary subgraph probabilities recover every induced law

<a id="graphon-proof-patterns"></a>

\[ t(H,W)=\int_{[0,1]^{V(H)}}\prod_{ab\in E(H)}W(x_a,x_b)\,d\mathbf x. \]

Let H be a finite simple loopless graph. The integral is the probability that every specified H-edge occurs, imposing no restriction on other edges. To require exactly edges E and absence of remaining potential edges B, conditional independence gives ∫∏E W·∏B(1−W). Expanding gives

\[ \mathbb P_W\{\text{induced edges exactly }E\}=\sum_{J\subseteq B}(-1)^{|J|}t((V,E\cup J),W). \]

Thus two deterministic graphons generate the same infinite graph law exactly when t(H,W) agrees for every finite simple H. This is an exact sampling-equivalence criterion; it neither proves nor needs a claim that the functions are connected by one invertible coordinate change. For random global W, replace t by E t to obtain the complete graph-law criterion.

The distribution of the random vector (t(H,W)) is identifiable too. Products of finitely many densities are densities of disjoint graph unions, with repetitions giving powers. Hence the graph law determines every finite polynomial moment. Densities lie in [0,1]; product Bernstein polynomials approximate continuous functions uniformly on finite cubes, by applying the binomial variance estimate to each coordinate and combining finitely many errors as in Chapter13. Thus moments determine each finite-vector law and cylinder uniqueness determines the countable density-vector law, without recovering graphon coordinates.

## 4. Identical row laws but different triangles

<a id="graphon-proof-row-counterexample"></a>

Let W₁ be constantly one half. Split [0,1] into equal halves and let W₂ be one exactly across the halves and zero within either half. Both degree functions are identically one half. Given a vertex latent variable, its edges to other vertices are iid Bernoulli(1/2), so every row has the same deterministic de Finetti director.

\[ t(K_3,W_1)=1/8,\qquad t(K_3,W_2)=0. \]

In the second graph a triple crosses between halves zero or two times, never on all three edges. Thus individually correct row representations do not determine alignment of shared indices across rows. Both graph laws are dissociated, so eliminating global randomness does not remove this failure.

## 5. Even noninvertible coordinates can preserve the graph law

<a id="graphon-proof-nonunique"></a>

Let T(x)=2x modulo one. Interval preimages split into two halves of half length, so T preserves Lebesgue probability, first on intervals then by π–λ. Set W(x,y)=xy and V(x,y)=T(x)T(y). The variables T(Uᵢ) remain iid uniform, so both functions generate the same graph law and all finite pattern densities agree.

There is no invertible modulo null sets, measure-preserving S with V(x,y)=W(Sx,Sy) almost everywhere. Integrating y and using measure preservation gives T(x)/2=S(x)/2, hence S=T almost everywhere. Every full-measure subset contains almost every pair x,x+1/2, which T identifies, so T is not injective on a full-measure set. This disproves the stronger claim that nonuniqueness is only invertible renaming.

For general representations, fixed measure-preserving input reparameterizations are a sufficient equality condition: use one transformation for the common vertex pool, separate ones for separate pools and retain shared unordered-pair noise in both directions. This is not a proved necessary classification. Equality of every finite-cylinder integral is the general necessary-and-sufficient criterion established here; all graph densities give its binary symmetric specialization. Stronger Hoover coordinate-equivalence and cut-distance classifications are not counted as proved.

## 6. A finite exchangeable graph need not extend infinitely

<a id="graphon-proof-finite"></a>

Choose one edge uniformly on three vertices. This is an S₃-exchangeable graph. If it had an infinite exchangeable extension, every triple would almost surely have exactly one edge, simultaneously over countably many triples. The event X₁₂=1 has probability one third. On it, triples {1,2,k} force X₁k=X₂k=0 for k≥3, and triples {1,k,l} force every edge between k,l≥3 to equal one. The triple {3,4,5} then has three edges, a contradiction.

Infinitude is a genuine premise of the representation theorem. Finite sampling has approximation theories, but an exact infinite latent-sampling representation cannot be assigned to every finite exchangeable adjacency matrix without qualification.
