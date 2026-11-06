# T-GEOMETRY: Coordinates, Metrics, Connections and Frames

Companion to [Chapter 40](../chapters/40-stochastic-geometry.md#geometry-atlas). Fix a finite-dimensional Hausdorff, second-countable smooth manifold M without boundary. Boundary extensions are separate problems, not part of a coordinate convention. We establish the deterministic tools actually used here without invoking Nash embedding or general curvature comparison.

## 1. How Charts Support Global Patching

<a id="geometry-proof-atlas"></a>

A chart x is a homeomorphism from an open U to an open subset of Rⁿ, with smooth invertible transitions. Second countability gives a countable cover by precompact coordinate balls. Construct Kₘ⊂int Kₘ₊₁ exhausting M by successively enlarging finite unions of those balls to contain the previous compact set. Each compact annulus Kₘ₊₁∖int Kₘ₋₁ has a finite cover by smaller chart balls whose closures lie in larger chart domains. Restrict them to neighboring annuli to obtain a locally finite smaller cover Pⱼ and larger domains Qⱼ.

In each Euclidean ball, scaled translates and finite sums of exp(−1/(1−|z|²)) give nonnegative smooth ρⱼ supported compactly in Qⱼ and positive on the closure of Pⱼ. Local finiteness makes ρ=Σρⱼ smooth and positive; φⱼ=ρⱼ/ρ is a smooth partition of unity. For a prescribed open cover, first shrink Qⱼ into a member of that cover. In particular, a compact K inside an open U has a smooth cutoff equal to one near K and compactly supported in U.

The Euclidean local inverse theorem needed here follows directly from contraction. If DF(a)=A is invertible, shrink a ball until ‖I−A⁻¹DF‖<1/2. The map x↦x+A⁻¹(y−F(x)) is a contraction preserving a suitable closed smaller ball. Iteration gives the inverse, difference integrals bound its Lipschitz constant, and difference quotients in F(F⁻¹(y))=y followed by differentiation give a smooth inverse. This suffices for the local embeddings and exponential charts below.

## 2. Tangent Vectors Are Not Fixed Lists of Components

<a id="geometry-proof-tangent"></a>

Define a tangent vector at p as a linear derivation on smooth germs, satisfying v(fh)=f(p)v(h)+h(p)v(f). The local integral Taylor identity expresses f(x)−f(p) as the sum of (xⁱ−pⁱ) times a smooth function with value ∂ᵢf(p). Leibniz therefore gives v=Σv(xⁱ)∂ᵢ. Constants have derivative zero and quadratic remainders disappear. The tangent space has dimension n, and transition components follow from the Jacobian rather than an extra convention.

\[ v_y^a=\frac{\partial y^a}{\partial x^i}v_x^i,\qquad \alpha_x=\alpha_i\,dx^i,\qquad \alpha(v)=\alpha_i v^i. \]

Cotangent space is the dual tangent space, so a one-form transforms to preserve pairing. A smooth vector field has smooth coordinate components and acts as a first-order differential operator. The commutator [V,W]f=V(Wf)−W(Vf) again satisfies Leibniz and is a vector field. Local ODE uniqueness is the deterministic Picard case proved in Chapter 35. The ordinary chain rule identifies solutions on overlaps, giving maximal flow curves.

## 3. How a Metric Selects a Connection

<a id="geometry-proof-connection"></a>

A Riemannian metric is a smoothly varying positive inner product on tangent spaces. Partitions of unity combine local Euclidean metrics into one. It measures curve length but does not by itself express the comparison of vectors at different points. A connection differentiates W along V, is function-linear in V and satisfies ∇ᵥ(fW)=V(f)W+f∇ᵥW. Local coefficients ∇ᵢ∂ⱼ=Γᵏᵢⱼ∂ₖ determine it through these rules.

\[ \Gamma^k_{ij}=\frac12g^{k\ell}(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}),\qquad \nabla_VW=V^i(\partial_iW^k+\Gamma^k_{ij}W^j)\partial_k. \]

Torsion freedom requires ∇ᵥW−∇𝑤V=[V,W]; metric compatibility requires Vg(W,Z)=g(∇ᵥW,Z)+g(W,∇ᵥZ). In a coordinate basis these give symmetric lower connection indices and the metric-derivative identity below. Permuting its three indices, adding twice and subtracting once, then multiplying by the inverse metric gives the Christoffel formula. Substitution verifies both requirements, proving existence and uniqueness.

\[ \partial_i g_{jk}=\Gamma^\ell_{ij}g_{\ell k}+\Gamma^\ell_{ik}g_{j\ell},\qquad \Gamma'^a_{bc}=\frac{\partial y^a}{\partial x^k}\Gamma^k_{ij}\frac{\partial x^i}{\partial y^b}\frac{\partial x^j}{\partial y^c}+\frac{\partial y^a}{\partial x^k}\frac{\partial^2x^k}{\partial y^b\partial y^c}. \]

The second transformation law follows by differentiating the coordinate components of W. Its second-derivative term makes ∇ᵥW a genuine tangent vector. Torsion freedom and metric compatibility are coordinate-independent, so uniqueness also proves that the chart formulas define one Levi–Civita connection. The coefficients Γ themselves are not a tensor.

## 4. Hessians and Laplace–Beltrami

<a id="geometry-proof-laplacian"></a>

\[ \operatorname{Hess}f(V,W)=V(Wf)-(\nabla_VW)f,\qquad \Delta_g f=g^{ij}(\partial_{ij}f-\Gamma^k_{ij}\partial_kf)=\frac1{\sqrt{|g|}}\partial_i(\sqrt{|g|}\,g^{ij}\partial_jf). \]

Leibniz makes the Hessian function-linear in both arguments; zero torsion makes it symmetric. Its metric trace is therefore coordinate-independent. The divergence expression is not an unchecked alternative definition: differentiation of the determinant expansion gives ∂log|g|=tr(g⁻¹∂g), while differentiating g⁻¹g=I gives ∂g⁻¹=−g⁻¹(∂g)g⁻¹. Substitution in the Christoffel formula identifies the first-order coefficients of the two expressions.

For a local orthonormal frame Eᵢ, tracing the Hessian gives Δf=Σ(Eᵢ²f−(∇Eᵢ Eᵢ)f). Calling ΣEᵢ² the Laplacian would omit a vector field. Integration by parts for compactly supported smooth tests follows from the divergence expression in each chart and a partition of unity. This establishes the formal energy identity, not by itself a global heat kernel or long-time invariant law.

## 5. A Checkable Embedding on Compact Regions

<a id="geometry-proof-local-embedding"></a>

For a compact K choose finitely many chart cutoffs ρⱼ so that one is positive at every point. Extend ρⱼ and ρⱼxⱼⁱ by zero and collect them as a global smooth map F. If F(p)=F(q) and ρⱼ(p)>0, the same positive cutoff and chart coordinates agree, so p=q. If dF(v)=0, first dρⱼ(v)=0 and then ρⱼdxⱼ(v)=0, hence v=0. Thus F is an immersion near K and an injection on K; compactness makes its inverse on F(K) continuous.

For a given smooth embedding i:M→Rᴺ, a full-rank minor and the local inverse argument of Section 1 give ambient coordinates in which i(M) is {z″=0}. Extend smooth functions or vector-field components constantly in z″ and multiply by ambient cutoffs; finite partitions combine these on compact regions. This supplies the local extensions needed for projection SDEs. It does not prove global isometric embedding for every metric; our general Brownian construction does not require that theorem.

## 6. The Orthonormal Frames Form a Manifold

<a id="geometry-proof-frames"></a>

A point u of O(M) is a linear isometry Rⁿ→TₓM. Metric Gram–Schmidt turns coordinate vectors into a smooth local orthonormal basis E(x), so u=E(x)q with q∈O(n). Near the identity, the Cayley map (I−A)⁻¹(I+A) from skew matrices supplies charts on O(n), with inverse (q−I)(q+I)⁻¹; translations cover the group. Hence O(M) has explicit smooth local product charts. Its inverse image over a compact base set is compact by finite trivializations and the compactness of O(n).

\[ H_i=u_i^k\frac{\partial}{\partial x^k}-\Gamma^k_{\ell m}u_i^\ell u_j^m\frac{\partial}{\partial u_j^k},\qquad H_i\big(g_{k\ell}u_j^ku_r^\ell\big)=0. \]

The formula moves in direction uᵢ while parallel-transporting every frame vector. Metric compatibility cancels the derivatives in the second identity, proving tangency to O(M); the connection transformation law gives agreement between charts. For a constant orthogonal q, right multiplication R_q(u)=uq transforms horizontal fields by the differential relation below. This will make changes of initial frame equivalent to rotations of Brownian input.

\[ H_i(uq)=(R_q)_*\sum_jq_{ji}H_j(u). \]

## 7. Parallel Transport, Geodesics and Isometries

<a id="geometry-proof-transport"></a>

\[ \dot u_j^k=-\Gamma^k_{\ell m}(x)\dot x^\ell u_j^m,\qquad \ddot x^k+\Gamma^k_{ij}(x)\dot x^i\dot x^j=0. \]

The first equation is a linear ODE along a given C¹ curve. Metric compatibility preserves inner products, and the compact image of any finite curve segment bounds frames and permits patching. The second defines geodesics; metric compatibility preserves speed. On a compact manifold, the base point and a fixed-length velocity stay in a compact tangent-bundle subset, so the ODE extends. A local equation alone does not imply this on a noncompact manifold.

A global smooth Riemannian isometry pushes the connection to a torsion-free metric-compatible one; uniqueness identifies the target Levi–Civita connection. It therefore preserves Hessian traces, parallel transport and horizontal fields. Under a coordinate change the metric components change too; changing an equation while keeping an unrelated Euclidean metric may change the actual motion. [Return to the chapter](../chapters/40-stochastic-geometry.md#geometry-isometry).
