# Chapter 40: When Random Paths Enter Curved Space — Stochastic Differential Geometry

A particle is confined to a circle. Its motion can be irregular, but changing a coordinate chart should not send it off the circle. The simplest description lets its angle be Brownian. Yet rewriting the very same path in horizontal and vertical coordinates introduces drift into an equation that had none. Is that drift part of the motion, or part of its description?

## 40.1 Why a Circle Particle Needs an Inward Term

<a id="geometry-circle"></a>

Let θₜ=Bₜ and start at (1,0), with Xₜ=cos Bₜ and Yₜ=sin Bₜ. The angle is not being declared a global single-valued coordinate on the circle; a real Brownian path first maps onto it. Chapter 32 gives the two equations below.

\[ dX_t=-Y_t\,dB_t-\frac12X_t\,dt,\qquad dY_t=X_t\,dB_t-\frac12Y_t\,dt. \]

The first-order noise is tangent, while drift points inward. Dropping drift because the angle had none would give dX=−Y dB and dY=X dB. The product rule immediately contradicts the constraint: d(X²+Y²)=(X²+Y²)dt. The inward terms in the actual equation exactly cancel accumulated squared increments.

Itô’s formula has not failed. It tells us that first-order rates in nonlinear coordinates remember second-order fluctuation. The error was to transform the drift coefficient as an ordinary vector field using only a Jacobian. The small calculation turns “the same motion” into a checkable mathematical requirement.

## 40.2 The Coordinate Goes to Infinity, but the Particle Remains

<a id="geometry-chart-pole"></a>

Use one real coordinate for circle position. On the chart omitting (−1,0), take y=tan(θ/2); recover position as ((1−y²)/(1+y²),2y/(1+y²)). Another Itô calculation gives the equation below.

\[ dy_t=\frac{1+y_t^2}{2}\,dB_t+\frac{y_t(1+y_t^2)}4\,dt. \]

Brownian exits (−π,π) in finite time, so this coordinate tends to infinity in finite time. Yet cos B and sin B remain continuously defined. In the second chart z=−1/y, Itô’s second-order term again contributes and gives dz=(1+z²)dB/2+z(1+z²)dt/4. The apparent coordinate catastrophe has a regular continuation.

Thus coordinate explosion in a Euclidean SDE must be separated from geometric lifetime. We need a language that joins local records into one path and detects departures that really cannot be repaired by changing charts. That is the role of an atlas here, rather than a more elaborate name for the state space.

## 40.3 Which Coefficients Should Transform as Vectors

<a id="geometry-jets"></a>

Before defining a manifold, consider a local equation dxⁱ=bⁱdt+σⁱαdWα, with a=σσᵀ. Chapter 32 computes exactly the equation of another record y=ψ(x):

\[ a_y^{ab}=\partial_i\psi^a\,a_x^{ij}\partial_j\psi^b,\qquad
b_y^a=\partial_i\psi^a b_x^i+\frac12a_x^{ij}\partial_{ij}\psi^a. \]

Covariance transforms with first derivatives, whereas drift also needs the coordinate’s second derivatives. These are two coefficient types of one second-order operator, not conflicting descriptions. Keeping b while forgetting a loses the information needed to transform drift.

Geometric compatibility will not mean that every symbol stays unchanged. It means the parts transform together by the correct rules. Itô descriptions already do so; Stratonovich will offer another expression that incorporates the correction into the integration convention.

## 40.4 Organizing Local Records into a Space

<a id="geometry-atlas"></a>

Take a finite-dimensional Hausdorff, second-countable smooth manifold M without boundary. Charts identify open regions with open subsets of Rⁿ and have smooth invertible transitions. Hausdorffness prevents a limit from being two positions; second countability lets probability use countable charts, stopping times and common null sets. These assumptions have a role beyond topological etiquette.

A tangent vector is an instantaneous first-order response of smooth readings at a point. Defining it as a derivation satisfying Leibniz, local Taylor proves the form vⁱ∂ᵢ and the Jacobian transition rule. A vector field smoothly assigns these responses across positions; a one-form assigns a linear scalar reading to a tangent vector.

Global work also needs smooth cutoffs. Smooth bumps on precompact chart balls, locally finitely normalized, construct partitions of unity and let functions, metrics and tests patch legitimately. [T-GEOMETRY 1–2](../foundations/t-geometry.md#geometry-proof-atlas) supplies compact exhaustions, cutoffs, derivations and the local inverse argument rather than assuming an unspecified geometry package.

## 40.5 When a Path Is a Manifold Semimartingale

<a id="geometry-semimartingale"></a>

An M-valued process cannot generally be added or averaged, but every smooth real reading f(X) can be observed. Here “manifold semimartingale” explicitly means the continuous version: X is continuous and adapted, and every smooth f(X) is locally a continuous real semimartingale before lifetime. Compactly supported smooth tests suffice. Geometric jumps require additional jump rules; the continuous chain rule is not silently extended to them.

Why is this compatible with chart descriptions? A cutoff extends each coordinate on a smaller chart to a global smooth test, giving a coordinate semimartingale. Conversely, coordinate Itô applied to any f gives the required decomposition. Countable charts and compact exhaustion handle stopping and null sets. The [full argument](../foundations/t-manifold-diffusions.md#manifold-proof-coordinates) also checks coordinate one-form integrals.

The definition does not make the path differentiable. It ensures existing stochastic calculus can act on every smooth reading and say the same thing across different records.

## 40.6 What Stratonovich Actually Simplifies

<a id="geometry-stratonovich"></a>

\[ dX=V_0(X)\,dt+\sum_\alpha V_\alpha(X)\circ dW^\alpha
\quad\Longrightarrow\quad
df(X)=V_0f(X)\,dt+\sum_\alpha V_\alpha f(X)\circ dW^\alpha. \]

The V’s are actual tangent vector fields, not unexplained chart coefficients. Chapter 32 Stratonovich chain rule pushes both noise and drift fields forward under ψ, making chart equations compatible. Conversion back to Itô restores drift V₀ⁱ+½ΣVαʲ∂ⱼVαⁱ and exactly the second-order transformation of Section 3.

The conventions are not competing accounts of what is more real. One process admits an Itô form with explicit correction or a vector-field form with symmetric integration. Stratonovich simplifies geometric patching; Itô retains its martingale, isometry and generator advantages. Neither convenience replaces an existence proof.

## 40.7 Compatible Formulas Still Need an Existing Process

<a id="geometry-patching"></a>

For smooth global fields and Brownian input, first use Chapter 35 cutoff Picard inside a precompact chart. Before exiting a larger chart, the chain rule and pathwise uniqueness identify overlapping solutions, allowing continuation. Initial values and chart selection must be measurable at the stopping time; lowest-index selection in a countable cover ensures this.

The difficulty is not the first switch but infinitely many switches in finite time. On a compact region, finitely many cutoff coordinates form a position-separating map F. Each component of F(X) has continuous stochastic-integral and finite-variation limits; a continuous inverse on the compact set gives a limit for X. Each switch crosses a positive gap, ruling out infinitely many accumulating switches along that compact path.

This gives a pathwise unique maximal solution whose finite lifetime can only mean eventual exit from every compact set. Continuous semimartingale input also works, but needs contraction on a clock built from total variation and brackets. [T-MANIFOLD-DIFFUSIONS 1–3](../foundations/t-manifold-diffusions.md#manifold-proof-clock) actually proves it. Renaming a Euclidean theorem is not a global geometric construction.

## 40.8 Orthonormal Noise Directions Can Still Add Drift

<a id="geometry-frame-choice"></a>

Even after coordinate compatibility, another plausible guess can fail: choose orthonormal directions at every point and send independent Brownian increments along them. Is the result automatically Brownian motion determined by the metric? The plane already tests this.

\[ E_1=(\cos x,\sin x),\qquad E_2=(-\sin x,\cos x),\qquad
\frac12(E_1^2+E_2^2)=\frac12\Delta+\frac12\partial_y. \]

The directions are orthonormal everywhere but rotate with position. Acting twice differentiates the fields’ own coefficients and leaves vertical drift. Ignoring it would identify distinct processes on the same Euclidean plane as one Brownian motion. Explaining the extra term requires differentiating vectors between nearby points, not merely measuring lengths at a single point.

## 40.9 A Connection Records How Vectors Are Compared

<a id="geometry-connection"></a>

A metric gives length and angle at a point; a connection describes how another tangent vector changes when moving in a direction. Written ∇ᵥW, it is function-linear in V and obeys Leibniz in W. Coordinates therefore differentiate W’s components and add ΓᵏᵢⱼVⁱWʲ. The non-tensor transformation of Γ is precisely what makes the whole ∇ᵥW a tangent vector.

A connection is not required for coordinate compatibility of a Stratonovich vector-field equation; that was already established. Here it is needed for parallel transport, distinguishing coordinate from geometric drift, and defining metric isotropy without an arbitrary local noise frame.

## 40.10 How the Metric Fixes the Choice

<a id="geometry-metric"></a>

Require parallel transport to preserve the metric and impose zero torsion, so the difference of two vector-field derivatives is their bracket. These determine the Levi–Civita connection uniquely. Writing the metric and its inverse as gᵢⱼ and gⁱʲ, solve three permutations of the metric-derivative identity to obtain:

\[ \Gamma^k_{ij}=\frac12g^{k\ell}(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}),\qquad
\operatorname{Hess}f(V,W)=V(Wf)-(\nabla_VW)f. \]

The subtraction in the Hessian separates change of the vector field itself from second-order change of the function. It is linear in both V and W and therefore admits a metric trace. The term left by the rotating planar frame now has a precise meaning rather than looking accidental. [T-GEOMETRY 3–4](../foundations/t-geometry.md#geometry-proof-connection) proves existence, uniqueness, transitions and the deterministic details.

## 40.11 Geometric Drift in a Second-Order Motion

<a id="geometry-generator"></a>

\[ \beta^k=b^k+\frac12\Gamma^k_{ij}a^{ij},\qquad
Af=\beta(f)+\frac12a^{ij}(\operatorname{Hess}f)_{ij},\qquad
\beta=V_0+\frac12\sum_\alpha\nabla_{V_\alpha}V_\alpha. \]

The b of Section 3 does not transform as a vector, but β does after the connection–covariance contraction. This is proved rather than named: substitute the transformation of Γ and cancel inverse-coordinate second derivatives against the Itô correction. The generator splits into a genuine vector drift and a second-order Hessian part.

Thus “no drift” needs a specified meaning. Coordinate b=0, Stratonovich field V₀=0 and connection drift β=0 are different conditions. The circle’s inward term and the rotating frame’s extra term show why the mere presence of dt does not decide geometric fairness.

## 40.12 From the Metric to Laplace–Beltrami

<a id="geometry-laplacian"></a>

For metric-isotropic second-order fluctuation, covariance should be g⁻¹ and geometric drift zero. The preceding decomposition then forces generator ½Δg, the metric trace of the Hessian. Coordinates give two equal expressions:

\[ \Delta_g f=g^{ij}(\partial_{ij}f-\Gamma^k_{ij}\partial_k f)
=\frac1{\sqrt{|g|}}\partial_i\!\left(\sqrt{|g|}\,g^{ij}\partial_j f\right). \]

For a local orthonormal frame, Δg=Σ(Eᵢ²−∇Eᵢ Eᵢ). Add Stratonovich drift −½Σ∇Eᵢ Eᵢ to remove the bias of arbitrary frame rotation. Substituting the circle stereographic metric g=4/(1+y²)² recovers exactly the drift and variance from Section 2.

Brownian motion is therefore not “independent standard Brownian coordinates in a chosen chart,” a requirement destroyed by chart changes. It is identified by this coordinate-independent second-order operator. A correct operator still leaves a path construction to do.

## 40.13 Actually Constructing the Local Law

<a id="geometry-local-brownian"></a>

\[ dx_t^k=\sigma^k_\alpha(x_t)\,dW_t^\alpha-\frac12g^{ij}(x_t)\Gamma^k_{ij}(x_t)\,dt,\qquad
\sigma\sigma^{\mathsf T}=g^{-1}. \]

Smooth positive definite g permits a smooth local σ by Gram–Schmidt or Cholesky. Chapter 35 constructs this SDE until chart exit. Another σ can change the coupling under the same noise but not this local law. Coordinate and product tests identify drift and brackets of any process making f(X)−½∫Δg f a local martingale. Multiplying its martingale by σ⁻¹ produces a unit-bracket Brownian driver; Euclidean local uniqueness identifies the stopped laws.

No arbitrary formal generator is being declared a process, and no future heat-kernel theorem fills a gap. [T-MANIFOLD-DIFFUSIONS 4](../foundations/t-manifold-diffusions.md#manifold-proof-generator) gives the full strictly elliptic identification. The frame construction below will join the local rules globally on one probability space.

## 40.14 A Sphere Model Makes the Correction Computable

<a id="geometry-sphere"></a>

On Sⁿ⊂Rⁿ⁺¹, tangent projection is P(x)=I−xxᵀ. Projecting ambient Brownian increments suggests the Itô equation dX=P(X)dW. Yet at the sphere its squared norm has positive drift n. First-order tangency does not ensure second-order accumulation stays on a curved surface.

\[ dX_t=(I-X_tX_t^{\mathsf T})\,dW_t-\frac n2X_t\,dt
\quad\Longleftrightarrow\quad
dX_t=(I-X_tX_t^{\mathsf T})\circ dW_t,\quad |X_0|=1. \]

For every deterministic initial point, the corrected equation has an actual global strong solution. Start with Euclidean local existence and compute dR=2(1−R)X·dW+(R−1)(R−n−1)dt for R=|X|². Stopped in bounded regions, Gronwall keeps the second moment of R−1 zero. The solution stays on the compact sphere and extends for all time. The constraint was proved, not substituted as an assumption.

Differentiating projection fields gives ΣDVαVα=−nx, proving the equivalence of conventions. Expectations give E Xₜ=\(e^{-nt/2}\)X₀: each path has radius one, while its mean position moves inward. Particles do not follow that radial mean path; their directions spread. The [construction and calculation](../foundations/t-manifold-diffusions.md#manifold-proof-sphere) retain the stopping and integrability conditions.

## 40.15 Checking That an Ambient Model Has Not Changed the Motion

<a id="geometry-embedding"></a>

Can projection on the sphere be generalized? Given a smooth isometric embedding i:(M,g)→Rᴺ, let Vα=Pₓeα, where Pₓ is ambient orthogonal projection onto TₓM. The manifold SDE theorem constructs ΣVα∘dWα. Identifying metric Brownian motion still requires its generator.

Differentiating P²=P gives P(DP)P=0. At a point split the ambient basis into tangent and normal vectors: normal projections vanish, and the sum of tangent connection corrections vanishes too. Thus ΣVα⊗Vα=g⁻¹ and Σ∇Vα Vα=0, giving generator ½Δg. The sphere is its explicit example; strictly elliptic law uniqueness identifies the projected model with local coordinate Brownian motion.

The embedding is a hypothesis, not an asserted proof that every metric has a global isometric embedding. For nonproper embeddings, bounded ambient coordinates do not replace compact-exit lifetime in M. The [equivalence proof](../foundations/t-manifold-diffusions.md#manifold-proof-embedding) keeps both restrictions. A general construction needs a route independent of an ambient space.

## 40.16 Making a Carried Set of Directions Part of the State

<a id="geometry-frame-bundle"></a>

Noise increments belong to Rⁿ and position belongs to M. Sending noise into the current tangent space requires an isometry u:Rⁿ→TₓM, an orthonormal frame. Instead of assuming one global smooth frame chosen at every point, record both the particle and the frame it currently carries.

The collection is O(M). Local metric Gram–Schmidt writes each u as E(x)q with q∈O(n), giving explicit local product charts. The enlarged state space is not abstraction for its own sake. It retains how directions are transported, precisely the information needed to interpret local noise commands at changing positions.

Over a compact base region, all orthonormal frames still form a compact set because the fiber O(n) is compact. Frames therefore cannot explode first while the particle stays compact. [T-GEOMETRY 6](../foundations/t-geometry.md#geometry-proof-frames) constructs the charts and horizontal fields explicitly.

## 40.17 Parallel Transport Connects the Directions of Successive Steps

<a id="geometry-horizontal"></a>

\[ H_i=u_i^k\partial_{x^k}-\Gamma^k_{\ell m}u_i^\ell u_j^m\partial_{u_j^k}. \]

Moving along the ith frame direction gives base velocity uᵢ while all frame vectors are parallel-transported by the connection. This produces the horizontal field above. Differentiating gₖₗuⱼᵏuᵣˡ along Hᵢ, metric compatibility cancels every term and preserves orthonormality. The transformation of Γ proves the field is not chart-specific.

Unlike an arbitrarily rotating local frame, directions are not reassigned from the appearance of current coordinates. They are carried along the actual path by one geometric transport rule. No noise is being predicted; existing directions are being interpreted.

## 40.18 Riemannian Brownian Motion Now Actually Exists

<a id="geometry-development"></a>

\[ dU_t=\sum_{i=1}^nH_i(U_t)\circ dW_t^i,\qquad X_t=\pi(U_t),\qquad U_0=u_0. \]

On a smooth Hausdorff second-countable boundaryless Riemannian manifold, the proved manifold SDE theorem constructs a pathwise unique maximal solution on O(M). Its projection X is continuous and adapted. Every compactly supported smooth f makes f(Xₜ)−f(X₀)−½∫₀ᵗΔg f(Xₛ)ds a local martingale before lifetime. This is the Riemannian Brownian motion constructed here, without extra interior killing.

The key calculation belongs in the main narrative. First Hᵢ(f∘π)=uᵢᵏ∂ₖf. A second application differentiates u to produce the negative connection term and f to produce second partials: together, the Hessian. Summing uses Σuᵢ⊗uᵢ=g⁻¹ and yields Δg. Calculation, not terminology, connects the construction to its intended generator.

Changing u₀ to u₀q rotates Brownian input to q⁻¹W and leaves projected law unchanged. Local elliptic uniqueness identifies all maximal Δg/2 laws, and strong Markov descends from the frame SDE using independence of projected law from frame choice. The [full proof](../foundations/t-development.md#development-proof-brownian) includes lifetime, measurable kernels and stopped conditional laws.

## 40.19 Development Can Also Recover Its Input

<a id="geometry-antidevelopment"></a>

\[ dU=\sum_iH_i(U)\circ dZ^i,\qquad
Z_t^i=\int_0^t(U_s^{-1})^i_k\circ dx^k(X_s),\qquad Z_0=0. \]

The horizontal equation also develops any continuous Rⁿ semimartingale Z. Conversely, parallel-lift a given manifold semimartingale X from an initial frame and use U⁻¹ to return tangent changes to Rⁿ. Time derivatives of rough paths are still not being taken; the construction uses proved Stratonovich one-form integration.

Why are the operations inverse? Horizontal fields satisfy U⁻¹dπ(Hᵢ)=eᵢ, and Stratonovich associativity reduces antidevelopment(development Z) to Z; parallel-lift uniqueness proves the other direction. For local-martingale input, each f’s second-order finite-variation term is its Hessian contraction. This defines a connection martingale, not the demand for zero drift in every arbitrary coordinate.

Whether antidevelopment is a martingale also depends on the chosen connection. Coordinates are expression; connection is structure. [T-DEVELOPMENT 1–3](../foundations/t-development.md#development-proof-construction) proves the inverse identities and the two directions of the martingale characterization.

## 40.20 In What Sense Is the Motion Geometrically Invariant

<a id="geometry-isometry"></a>

If Φ:(M,g)→(N,h) is a global smooth Riemannian isometry, the pushed connection preserves h and has zero torsion. Levi–Civita uniqueness identifies it with N’s connection. Horizontal fields and their SDE therefore push forward together. Under the same noise, Φ(X) is the target development’s projection, proving invariance of Brownian law rather than only formal agreement of generators.

This does not mean every nonlinear map preserves Brownian law for a fixed metric. Changing circle angle to y also changes metric components to 4/(1+y²)²dy². Keeping dy² instead changes the model. Nor must the same Brownian input yield identical coupled paths under every frame choice. The transformed geometric object and law are invariant; a pathwise identity requires transforming the driver too.

## 40.21 Lifetime Means Leaving the Space, Not One Chart

<a id="geometry-lifetime"></a>

The infinite coordinate of Section 2 now has a precise interpretation. Maximal lifetime ζ is the limit of compact-exit times; finite ζ means eventual departure from every compact subset of M. The circle is compact, so coordinate divergence cannot cause geometric explosion.

Conversely, a process can explode without any chart singularity. The ODE dX=X²dt on the complete Euclidean line already has finite lifetime, showing that a complete carrier space does not control arbitrary coefficients. Metric Brownian has geometrically fixed coefficients, making the sharper question meaningful: does the geometry itself limit escape speed?

## 40.22 Nonexplosion Needs Actual Control

<a id="geometry-lyapunov"></a>

\[ V\ge1,\quad V\in C^2(M),\quad \{V\le r\}\ \hbox{compact},\quad AV\le cV,\quad c\ge0
\quad\Longrightarrow\quad P_x(\zeta=\infty)=1. \]

V is a position reading growing at infinity. If its generator growth is controlled by itself, stopped Itô and Gronwall give E V(Xₜ∧τᵣ)≤\(e^{ct}\)V(x). The probability of hitting V=r is at most this bound divided by r; letting r increase excludes finite-time escape. Expectations are first justified on compact sets, not formally continued past lifetime.

Compact manifolds need no reading at infinity: maximal compact-exit lifetime already guarantees nonexplosion. Noncompact spaces require actual conditions. Smoothness of the manifold or continuity of paths does not answer how quickly the process travels outward. The [proof](../foundations/t-development.md#development-proof-lyapunov) also explains why length controls finite-variation development but not Brownian input.

## 40.23 Geodesic Completeness Is Still Not Stochastic Completeness

<a id="geometry-completeness"></a>

Geodesic completeness means every geodesic extends for all parameter time. Stochastic completeness here means that from every initial point the maximal metric Brownian lifetime is almost surely infinite. The quantifiers concern different objects. Development preserves length for finite-variation input, so metric completeness supplies endpoints for finite-time Cauchy tails; Brownian infinite total variation removes that premise.

\[ P_t f(x)=E_x[f(X_t)\mathbf1_{\{t<\zeta\}}],\qquad P_{s+t}=P_sP_t,\qquad P_t1(x)=P_x(t<\zeta). \]

Strong Markov conditioning gives this possibly mass-losing semigroup identity. Stochastic completeness is equivalent to Pₜ1(x)=1 for all x and t, connecting path lifetime to an operator reading without assuming a smooth heat kernel. The example below makes the reading strictly less than one.

\[ g=dr^2+f(r)^2d\theta^2,\quad f(r)=r\ (r\le1),\quad f(r)=e^{r^3}\ (r\ge2),\qquad
dR_t=d\beta_t+\frac32R_t^2\,dt\quad(R_t>2). \]

Interpolate smoothly and positively between the two regions; the origin is Euclidean. This is a smooth surface on all of R². Distance from the origin is r, closed metric balls are compact, and fixed-speed geodesics stay in compact tangent-bundle subsets for finite time, proving completeness directly. Outside, Brownian radius satisfies the displayed equation: rapidly growing area creates a large outward term in the radial reading.

This is not a guess based on “large drift.” For lower radius a≥2, scale S(r)=∫ₐʳ1/f has finite limit, giving positive probability of crossing every L before returning to a. The bounded function v(r)=2∫ₐʳf(y)⁻¹∫ₐʸf satisfies Lv=1 and bounds expected exit times uniformly. Thus radius reaches infinity in finite time on an event of positive probability. [Stopping, tail estimates and limits](../foundations/t-development.md#development-proof-incomplete) are all proved.

## 40.24 Geometric Holes and Boundary Rules Need Another Distinction

<a id="geometry-boundary"></a>

Incompleteness does not force Brownian explosion either. Removing the origin from the Euclidean plane terminates some finite-length geodesics, but Chapter 38’s annulus calculation shows Brownian does not hit that point. On each finite time interval its radius has a positive minimum and finite maximum, so the process is still stochastically complete in the punctured plane.

If a boundary is included, arrival rules still need specification. On a half-line, absorption at zero and reflection have the same interior generator ½∂² but different laws. Chapter 37 Tanaka constructs |x+B| and removes its local-time term for Neumann tests; absorption has a zero atom at positive times. Interior formulas, the state space and boundary rules each contribute to the process.

The main construction treats maximal interior processes on boundaryless manifolds; it does not silently complete general reflecting, sticky or elastic boundary classification. The [examples and proofs](../foundations/t-development.md#development-proof-boundary) separate chart poles, inaccessible holes, actual explosion and different boundary rules.

## 40.25 When the Space Has Multiplication, Increments Change Form

<a id="geometry-lie"></a>

On a Lie group G, the present state transports a random change near the identity to its own neighborhood. The increment is Yₛ⁻¹Yₛ₊ₜ rather than subtraction of two points. Left-invariant fields transport local instructions, and independence of future noise with constant rules gives independent stationary left increments.

Order can matter. In the Heisenberg product, (x,y,z)(x′,y′,z′) adds xy′ to the last coordinate. Multiplying (1,0,0) then (0,1,0) gives last coordinate one; reversing them gives zero. Exponentiating a single Euclidean sum loses that order. Moving Chapter 27 jumps to a group requires constructing small products, not merely rewriting a characteristic function.

## 40.26 Actually Compensating Small Jumps on a Matrix Group

<a id="geometry-lie-jumps"></a>

Consider a setting in which ambient matrices control small jumps: take a given compact smooth matrix Lie group G⊂O(N). A Lie-algebra basis Aᵢ gives left-invariant fields Xᵢ(g)=gAᵢ, and an exponential-chart cutoff χ reads first-order jumps near identity. Given b, nonnegative covariance q and a Lévy measure with ∫‖h−I‖²ν(dh)<∞, one can actually construct:

\[ Af(g)=b^iX_if(g)+\frac12q^{ij}X_iX_jf(g)+
\int_G\big(f(gh)-f(g)-\chi^i(h)X_if(g)\big)\nu(dh). \]

First truncate small jumps, right-multiply the finitely many marks in arrival order and run left-invariant diffusion between them. In compensated matrix form the drift retains only the integrable second-order remainder h−I−χⁱ(h)Aᵢ. Doob and Gronwall give maximal-L² convergence; closed compact G contains the limit. Driver independence and pathwise uniqueness then identify independent stationary future increments, producing a genuine group Lévy process.

[T-LIE-LEVY](../foundations/t-lie-levy.md) gives the construction, generator and fixed-truncation triplet uniqueness. Its stated compact-matrix scope does not claim Hunt necessity classification for every Lie group. With a bi-invariant metric, the pure Gaussian case returns to Riemannian Brownian, connecting continuous geometry and jumps through local rules.

## 40.27 What Is Preserved When We Describe the Same Process

<a id="geometry-recognition"></a>

Circle angle, stereographic and ambient coordinates have different drift expressions while recording one motion. What persists is the second-order relation between smooth readings and their common geometric generator. Conversely, distributing equally sized noise directions by different rotation rules can change drift; pairing the same interior operator with different boundaries can change the law.

Coordinate invariance is neither sameness of every term nor irrelevance of every choice. It distinguishes a change of expression from a choice of structure. Connection, metric, state space and boundary conditions do not disappear behind elegant notation; construction and counterexamples reveal each role.

## 40.28 What Remains after Local Isotropy

<a id="geometry-insight"></a>

The inward drift that opened the chapter is no longer mysterious. Second-order fluctuation leaves corrections in nonlinear records; Stratonovich transports tangent rules conveniently; a connection compares directions, a metric specifies isotropy, and a frame equation constructs an actual path. Malliavin differentiation is not a prerequisite for this construction, and Brownian time nondifferentiability has never been removed.

We can now identify which features of one motion belong to its record and which to geometry. A further question concerns more than notation: as the process keeps running, can local symmetry support stable long-time observation? Is an average determined by invariant structure, or does it retain the initial point and global space? New arguments about time and symmetry are needed; a local generator alone does not answer.

### Sources and Proof Scope

This chapter is a modern reconstruction, not an invented unified discovery narrative. Geometric-analysis scope is checked against [Hsu’s author bibliography](https://sites.math.northwestern.edu/~ehsu/Research.html) and the [publisher record](https://doi.org/10.1090/gsm/038), stochastic-completeness boundaries against [Grigor’yan’s author notes](https://www.math.uni-bielefeld.de/~grigor/scmp.pdf), and group Lévy background against [Applebaum’s institutional archive](https://eprints.whiterose.ac.uk/id/eprint/9794/1/Applebaum_Levy_Processes.pdf). Proofs are independently organized rather than copied.

Full companions: [T-GEOMETRY](../foundations/t-geometry.md), [T-MANIFOLD-DIFFUSIONS](../foundations/t-manifold-diffusions.md), [T-DEVELOPMENT](../foundations/t-development.md) and [T-LIE-LEVY](../foundations/t-lie-levy.md). The main scope is continuous semimartingales and maximal diffusions on smooth boundaryless manifolds. Equivalence for a given isometric embedding does not include Nash existence. General geometric jump conventions, boundary extensions and Hunt necessity on arbitrary Lie groups are not claimed proved.
