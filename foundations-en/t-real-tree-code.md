# T-REAL-TREE-CODE: The Complete Real-Tree Proof for an Excursion Quotient

This companion completes the deterministic construction in [Chapter 54](../chapters/54-brownian-crt.md#crt-pseudo). It uses neither GH closedness from Chapter 55 nor any random-tree limit or special Brownian property.

## 1. Assumptions, minima and the pseudometric

<a id="real-code-pseudo"></a>

Let h be continuous and nonnegative on [0,1], with h(0)=h(1)=0. Interior zeros and the zero function are allowed. Intervals below are the closed intervals between their endpoints. Let m(s,t) be the minimum of h over that interval, and define d.

\[ m(s,t)=\min_{[s\wedge t,s\vee t]}h,\qquad d(s,t)=h(s)+h(t)-2m(s,t). \]

Nonnegativity, symmetry and d(s,s)=0 follow directly, but the triangle inequality must allow the third time to lie anywhere. The interval between s and t is contained in the union of those between s,u and u,t. Thus m(s,t) is at least the smaller of m(s,u),m(u,t). Also h(u) is at least their maximum. Consequently

\[ m(s,u)+m(u,t)-h(u)\le\min\{m(s,u),m(u,t)\}\le m(s,t),\qquad d(s,t)\le d(s,u)+d(u,t). \]

Continuity also gives d(s,t)≤2ωₕ(|s−t|), where ωₕ is the uniform modulus of continuity. These are ordinary real minima; no choice of probabilistic versions is involved.

## 2. Zero distance and the compact quotient

<a id="real-code-quotient"></a>

Define s∼t exactly when d(s,t)=0. The triangle inequality proves transitivity. If s∼s′ and t∼t′, two triangle inequalities give d(s,t)≤d(s′,t′) and the reverse. The quotient Tₕ therefore has a well-defined metric, strictly positive between distinct classes. Write p for projection and ρ=p(0)=p(1).

\[ T_h=[0,1]/\!\sim,\qquad d_h(p(s),p(t))=d(s,t),\qquad d_h(\rho,p(t))=h(t). \]

The modulus bound makes p continuous and onto. Thus Tₕ is compact, connected, separable and complete. Neither connectedness nor compactness proves the absence of loops; arcs must actually be constructed.

## 3. The ancestral line is not an arbitrary return path

<a id="real-code-ancestors"></a>

For x=p(t) and 0≤a≤h(t), let rₜ(a) be the last time at or before t with height a. The intermediate value theorem makes this set nonempty; closedness gives its maximum. Between rₜ(a) and t, h≥a, since a lower value would require another crossing of a before reaching h(t). If a<b≤h(t), then rₜ(a)≤rₜ(b) and the minimum between them is a. Consequently a↦x(a)=p(rₜ(a)) is an isometry from [0,h(t)] to a root-to-x path.

\[ r_t(a)=\max\{u\le t:h(u)=a\},\qquad d_h(x(a),x(b))=|a-b|. \]

Independence of representatives needs proof too. If s≤t and p(s)=p(t), then h(s)=h(t)=m(s,t)=H. For a<H the intervening path stays above a, so the last hit of a before t is the same as before s. At a=H the endpoints are already equivalent. Hence x(a) depends only on the quotient point.

## 4. Common ancestors and the segment between two points

<a id="real-code-lca"></a>

Take s≤t, x=p(s), y=p(t), and put m=m(s,t). Below m the intervening path stays above a, so the ancestral points agree. At m, a minimum time u between s and t is equivalent to the height-m point of both lines. Conversely, if ancestral points at height a agree, the intervals from those representatives to s and t, and between the representatives, all stay at least a. Their union covers [s,t], so m≥a. The common initial segment is exactly [0,m]; its endpoint b is the most recent common ancestor.

\[ x\wedge y=b=x(m)=y(m),\qquad |x\wedge y|=m,\qquad d_h(x,y)=|x|+|y|-2|x\wedge y|,\quad |x|=d_h(\rho,x). \]

Descend from x to b along its ancestral line, then ascend to y. Points of heights a,c on different branches still have common ancestor b and distance a+c−2m; points on one branch have distance equal to their height difference. The concatenation is therefore an isometric segment of length dₕ(x,y), not merely a curve with the right total length. Denote its image by [x,y].

## 5. Unique geodesics alone do not exclude other arcs

<a id="real-code-arcs"></a>

Our definition of a real tree has two requirements: every pair has an isometric segment, and the image of every injective continuous arc between that pair is this segment. The second cannot be replaced by uniqueness of geodesics: the Euclidean plane has unique geodesics too. We prove that every interior point of the constructed segment separates its endpoints.

The common-ancestor height q(x,w)=(|x|+|w|−dₕ(x,w))/2 is continuous. Three ancestral lines show that the minimum of q(x,w),q(x,v),q(w,v) occurs at least twice. For example, if q(x,w)<q(x,v), then x and v still share the branch where w has already split, forcing q(w,v)=q(x,w). The other orders follow by interchanging labels. This follows from the exact common-initial-segment description.

Let z=x(a), with a<|x|, and set O={w:q(x,w)>a}. This is open and contains x. If w∉O, w≠z, and v∈O, the three-line fact gives q(w,v)=q(w,x), including the equality q(w,x)=a, since q(v,x)>a. Hence

\[ d_h(w,v)=|w|+|v|-2q(w,x)\ge |w|+a-2q(w,x)=d_h(w,z)>0. \]

Thus O is both open and closed in Tₕ∖{z}. Every interior z of [x,y] lies on at least one endpoint’s ancestral line strictly below that endpoint; the corresponding O separates the endpoints, including when z is their common ancestor. Every continuous path between the endpoints must therefore pass through z.

For an injective continuous arc γ, compactness of its domain and the Hausdorff target make its inverse on its image continuous. The cut-point argument shows its image contains [x,y]. The inverse image of this connected segment is a connected subset of [0,1] containing both endpoints, hence the whole interval. Thus γ has precisely image [x,y]. Both real-tree axioms are proved, and uniqueness of geodesics follows as a consequence.

## 6. Finite subtrees and their recovery

<a id="real-code-reduced"></a>

The finite rooted span R(x₁,…,xₖ)=∪[ρ,xᵢ] is a compact real tree. On adding xᵢ, its ancestral line meets the old tree in a closed initial segment: each old ancestral line contributes one initial segment, and a finite union is the longest of them. The new part is one segment attached at a unique old point. Suppressing unmarked degree-two points gives a finite combinatorial tree with positive edge lengths; a point already in the span adds no edge.

For ordered sample times s₁<⋯<sₖ, put xᵢ=h(sᵢ), yᵢ=m(sᵢ,sᵢ₊₁). A nonadjacent interval minimum is the minimum of its intervening y-values. Hence x,y recover all sample distances. If the y-values are distinct and 0<yᵢ<min(xᵢ,xᵢ₊₁), recursively splitting at the smallest y constructs a binary plane reduced shape, with the initial root edge equal to the global minimum y. For k=1 there is one edge of length x₁. Adding a new ordered sample adds length xᵢ−yᵢ₋₁, so L=Σxᵢ−Σyᵢ.

## 7. Boundaries of the assumptions and return to the chapter

<a id="real-code-boundaries"></a>

Continuity cannot be added only at the end. For h equal to 1 on [1/3,2/3) and 0 elsewhere, the quotient consists of two points at distance 1, with no segment between them, so is not a real tree. Conversely, interior zeros, plateaux and multiple branches at a minimum are allowed for continuous h. Brownian binary branching is not an assumption of the coding theorem.

Replacing the interval minimum by the smaller endpoint height yields |h(s)−h(t)| and collapses equally high points on different branches. The result may still be a legitimate segment, but it no longer recovers branching. Some continuous functions outside our nonnegative based class can also code trees; our root-height identity and closed-tour convention simply do not apply automatically. We have not claimed that every such function fails. [Return to the real-tree conclusion in Chapter 54](../chapters/54-brownian-crt.md#crt-real-tree).
