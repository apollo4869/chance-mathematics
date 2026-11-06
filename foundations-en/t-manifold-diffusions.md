# T-MANIFOLD-DIFFUSIONS: From Chart Equations to Actual Diffusions

Companion to [Chapter 40](../chapters/40-stochastic-geometry.md#geometry-patching), using the actual tools of [T-GEOMETRY](t-geometry.md). Filtrations satisfy the usual conditions. Semimartingales here are continuous; identities hold before maximal lifetime. No ambient embedding is assumed except in the section explicitly given one.

## 1. Local Existence for Continuous Drivers Is Not a Black Box

<a id="manifold-proof-clock"></a>

Let Z=M+A be an Rᵐ continuous semimartingale, with M₀=0 a continuous local martingale and A locally of finite variation. A constant initial value may be included in A, and a deterministic dt term is included by adjoining Z⁰=t. For smooth Vᵢ interpret the Stratonovich equation first as the Itô equation below, rather than assuming an integral along an unknown solution. Chapter 32 then identifies the two forms. Smooth coordinate cutoffs make V and its first two derivatives bounded, so both V and DVᵢVⱼ are globally Lipschitz.

\[ dY^a=V_i^a(Y)\,dZ^i+\frac12\partial_bV_i^a(Y)V_j^b(Y)\,d[M^j,M^i],\qquad C_t=t+\sum_i\operatorname{Var}(A^i)_t+\sum_i[M^i]_t. \]

The bracket matrix measure is positive semidefinite: use increasing quadratic variations for rational vectors on a common countable full-measure set, then take densities with respect to the trace measure. Each cross-variation total variation is bounded by half the sum of its two diagonal measures. Thus C controls all finite-variation terms. Stop at C≤N on a fixed finite horizon T. The stopped martingale increments are square integrable by Chapter 31 isometry, localization and Fatou.

Divide time into intervals on which C increases by at most δ. Chapter 31 vector isometry, Doob’s inequality and Cauchy–Schwarz for finite-variation integration give the contraction estimate below, with K depending only on cutoff coefficients and dimension. Choose δ so that the factor is less than one. Completeness of the maximal-L² space of continuous adapted processes gives a solution on each interval; stopping at C≤N requires at most ⌈N/δ⌉+1 intervals. Localize a finite initial value by its magnitude and patch on equal-initial-value events as in Chapter 35, then remove N, T and state cutoffs.

\[ E\sup|\Gamma(Y)-\Gamma(\widetilde Y)|^2\le K(\delta+\delta^2)E\sup|Y-\widetilde Y|^2. \]

The same estimate gives pathwise uniqueness. Two cutoff solutions agree before their common exit. Integral limits hold in stopped maximal L², and in ucp after localization; continuous versions give indistinguishable equation identities. Applying Chapter 32 to Vᵢ(Y) identifies its covariation with Z as precisely the correction above, proving the original Stratonovich equation. No manifold construction later on this page is used.

## 2. Test Functions and Coordinates Give the Same Definition

<a id="manifold-proof-coordinates"></a>

A continuous adapted M-valued X is a manifold semimartingale if every globally smooth real f makes f(X) locally a continuous real semimartingale before lifetime. Compactly supported smooth tests suffice: on a compact region multiply f by a cutoff equal to one, and exhaust the space. A chart coordinate is not global, but cutoff extension gives a global test agreeing on a smaller chart. Conversely, Chapter 32 Itô in coordinates gives the local decomposition of every f(X). Countable charts permit patching on a common full-measure set.

\[ dy^a(X)=\partial_i y^a(X)\,dx^i(X)+\frac12\partial_{ij}y^a(X)\,d[x^i(X),x^j(X)]. \]

This proves correct coordinate compatibility for Itô descriptions. Stratonovich rewrites the same identity as an ordinary-looking chain rule; it does not repair an inconsistent Itô theory. For continuous semimartingales A, B and Z, the product rule and Chapter 31 bracket identities prove the associativity below. Finite-variation terms add no bracket. Compute first with bounded stopped energy and then localize; this establishes compatibility of coordinate one-form integrals.

\[ Y=\int B\circ dZ\quad\Longrightarrow\quad \int A\circ dY=\int AB\circ dZ,\qquad [AB,Z]=\int A\,d[B,Z]+\int B\,d[A,Z]. \]

Indeed, expanding the left side gives ∫AB dZ plus one half each of ∫A d[B,Z] and ∫B d[A,Z], exactly the right side. Summing components gives the vector version. Hence the integral of αᵢ(X)∘dxⁱ agrees between charts; add along successive stopped chart intervals without requiring global coordinates.

## 3. Patching, Measurability and Actual Lifetime

<a id="manifold-proof-patching"></a>

For global smooth fields Vᵢ and a given continuous semimartingale Z, use the locally finite Pⱼ⊂⊂Qⱼ of T-GEOMETRY. At the current point select the lowest-index Pⱼ containing it, and solve in Qⱼ until exit. The next initial value is measurable at that stopping time; the same Picard construction remains adapted on a stochastic interval, without independent increments of Z. The chain rule and pathwise uniqueness identify overlapping chart solutions. Lowest-index selection is Borel, and countable stopping and Picard limits establish measurability. In joint initial-value and noise variables, use the convergence event of the full Picard sequence and a fixed default on failure to get a Borel solution map; no invented common null set for every initial value is needed.

Repeated chart switching alone is not a proof. If switching times accumulate at finite S while the path stays in compact K, use the finite separating map F of T-GEOMETRY. Each component satisfies its tested equation with coefficients bounded on K. After stopping C≤N, martingale and finite-variation integrals extend continuously to S, so F(X) has a limit. Compactness and the continuous inverse give a limit for X. Only finitely many relevant charts meet K, and each closure of Pⱼ is positively separated from M\Qⱼ. Each switch crosses a uniformly positive gap, contradicting uniform continuity of the extended F(X).

A finite maximal lifetime ζ must mean eventual departure from every compact set, not merely the absence of one bounded coordinate. If a compact K is visited arbitrarily near ζ, choose a compactly supported f equal to one on K. Both Vᵢf and VⱼVᵢf are globally bounded, so the integral representation of f(X) extends continuously to ζ. A visit subsequence forces limit one; eventually X stays in the compact set {f≥1/2}, where the preceding extension argument applies, a contradiction. A countable compact exhaustion unifies the assertion. For the maximal solution without artificial interior killing, lifetime is the limit of compact-exit times.

Local uniqueness also gives global pathwise uniqueness by successive common chart intervals; a finite separation time would violate uniqueness in a preceding compact neighborhood. For Brownian input and deterministic smooth fields, Picard and chart patching give a measurable solution map in initial state and driving noise. Brownian strong Markov at stopping times then gives strong Markov for the maximal solution. General semimartingale input carries no such automatic conclusion.

## 4. Second-Order Operators, Connection Drift and Local Laws

<a id="manifold-proof-generator"></a>

\[ A f=b^i\partial_i f+\frac12a^{ij}\partial_{ij}f,\quad a'^{ab}=\partial_i y^a\,a^{ij}\partial_jy^b,\quad b'^a=\partial_i y^a b^i+\frac12a^{ij}\partial_{ij}y^a. \]

For Stratonovich drift V₀ and Brownian fields Vα, Chapter 32 gives A=V₀+½ΣVα². Applying Itô to new coordinates and tests gives the transformations above. The expression A(fh)−fAh−hAf identifies a as a nonnegative symmetric second-order tensor, but b alone is not a vector. The connection transformation law and the second derivative of the inverse coordinate identity cancel to produce the genuine vector β below.

\[ \beta^k=b^k+\frac12\Gamma^k_{ij}a^{ij},\qquad Af=\beta(f)+\frac12a^{ij}(\operatorname{Hess}f)_{ij},\qquad \beta=V_0+\frac12\sum_\alpha\nabla_{V_\alpha}V_\alpha. \]

To show that the generator identifies the law here, let a be smooth positive definite and b smooth in a chart. Suppose the maximal continuous process without extra killing makes f(X)−∫Af a local martingale. Test cutoff coordinates and products; Chapter 32 gives Mⁱ=xⁱ(X)−∫bⁱ and [Mⁱ,Mʲ]=∫aⁱʲ. Smooth Gram–Schmidt or Cholesky gives invertible σ with σσᵀ=a. Then W=∫σ⁻¹dM has unit-time bracket. Extend past chart exit using independent Brownian noise; Chapter 33 Lévy characterization makes this an actual Brownian motion.

Thus X satisfies the stopped Euclidean SDE. Chapter 35 Picard construction and pathwise uniqueness identify it on any such weak realization with the same noise solution map, giving uniqueness of the stopped law. Countable patching as in Section 3 gives uniqueness of the maximal law. The argument is local, smooth and strictly elliptic; it does not establish uniqueness for every formal degenerate operator or boundary extension.

## 5. Explicit Checks on the Circle and Sphere

<a id="manifold-proof-sphere"></a>

\[ Y=\tan(B/2):\quad dY=\frac{1+Y^2}{2}\,dB+\frac{Y(1+Y^2)}4\,dt,\qquad Z=-1/Y:\quad dZ=\frac{1+Z^2}{2}\,dB+\frac{Z(1+Z^2)}4\,dt. \]

These equations hold on their respective stopped angular charts. Itô for −1/y converts the drift, including its second-order term, exactly to z(1+z²)/4. Brownian exit from (−π,π) is finite, but e^{iB} exists globally: a chart pole is not path explosion. The chart metric is 4(1+y²)⁻²dy², and the Laplacian formula of T-GEOMETRY gives precisely the generator Δ/2.

\[ P(x)=I-xx^{\mathsf T},\qquad dX=P(X)\,dW-\frac n2X\,dt,\quad X_0\in S^n\subset\mathbb R^{n+1}. \]

Fix a deterministic initial sphere point x and construct this ambient equation by Chapter 35 local smooth-coefficient theory. For R=|X|², Chapter 32 gives dR=2(1−R)X·dW+(R−1)(R−n−1)dt. Stop at |X|≤K; Gronwall makes the second moment of R−1 zero, so R≡1. Removing localization, the path stays on the compact sphere and cannot explode. Sphere invariance was not assumed in advance.

On the sphere Vα=Peα satisfies ΣDVαVα=−nx by direct differentiation, so the equation equals dX=P(X)∘dW. Omitting normal drift leaves drift n in |X|² at the sphere and breaks the constraint. Bounded martingale expectations give E Xₜ=\(e^{-nt/2}\)X₀, including \(e^{-t/2}\) on the circle. This is an actual consequence of the path equation, not a proof of full long-time mixing.

## 6. A Given Isometric Embedding and a Rotating-Frame Counterexample

<a id="manifold-proof-embedding"></a>

Let i:(M,g)→Rᴺ be a given smooth isometric embedding and Pₓ the ambient orthogonal projection onto TₓM. The fields Vα=Pₓeα are smooth global tangent fields; Section 3 constructs their Stratonovich SDE up to intrinsic maximal lifetime. Extend f smoothly to an ambient neighborhood by T-GEOMETRY Section 5. Differentiating P²=P and multiplying on both sides by P gives P(DP)P=0.

At a point rotate the ambient basis into tangent and normal directions. Normal fields vanish there; tangent contributions to ∇ᵥV vanish by P(DP)P=0. Thus Σ∇Vα Vα=0 and ΣVα⊗Vα=g⁻¹. The Hessian decomposition gives ΣVα²f=Δg f. Section 4 law uniqueness identifies this with the horizontal-frame Brownian construction. For nonclosed or nonproper embeddings, retain compact-exit lifetime in M; bounded ambient coordinates do not replace it.

\[ E_1=(\cos x,\sin x),\quad E_2=(-\sin x,\cos x)\quad\hbox{on }\mathbb R^2,\qquad \sum_i\nabla_{E_i}E_i=(0,1). \]

Direct differentiation gives ∇E₁E₁=cos x E₂ and ∇E₂E₂=sin x E₁, whose sum is (0,1). The naive Stratonovich equation ΣEᵢ∘dWⁱ therefore has generator ½Δ+½∂ᵧ, not standard planar Brownian; subtract ½(0,1)dt to correct it. Stratonovich gives coordinate compatibility for vector-field equations, not automatic metric Brownian motion from every orthonormal frame. [Return to the chapter](../chapters/40-stochastic-geometry.md#geometry-frame-choice).
