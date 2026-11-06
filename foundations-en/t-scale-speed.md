# T-SCALE-SPEED: Stopping, Green Kernels and Speed Normalization

A companion to [Chapter 36](../chapters/36-scale-speed.md). On I=(ℓ,r), b,σ are locally Lipschitz and σ>0, with a=σ²/2. Use Chapter 35’s maximal solution, usual filtration and stopped Itô. No local time, general time change or Chapter 38 Feynman–Kac is assumed. Fix an interior reference c and the chapter’s normalization of p,S,m.

## 1. Finite Compact-Interval Exit without Assuming the Hitting Formula

<a id="scale-compact-exit"></a>

Fix ℓ<α<x<β<r. The function p is positive C¹, S is strictly increasing C² and m′=1/(ap) is positive continuous. They are bounded and bounded away from zero on [α,β]. Define G by the deterministic formula below and u(x)=∫_α^βG(x,y)m′(y)dy. Then G≥0 and vanishes at endpoints, so u≥0 is continuous and bounded. Direct differentiation gives u∈C² and Lu=−1 without using a stochastic occupation formula.

Let τ be the first hit of α or β. Itô up to t∧τ has bounded integrand u′σ, hence a square-integrable mean-zero martingale. Thus E(t∧τ)=u(x)−E u(Xₜ∧τ)≤u(x). Monotone convergence yields Eτ≤u(x)<∞, so τ is finite almost surely. Continuity and local extendibility make exit occur at α or β. Letting t increase, endpoint values and DCT give Eτ=u(x).

The bounded local martingale S(Xₜ∧τ) is a true martingale, by localization and constant domination. Since τ is finite, DCT gives S(x)=S(α)P(\(\tau_\alpha<\tau_\beta\))+S(β)P(\(\tau_\beta<\tau_\alpha\)). The probabilities sum to one, proving the hitting formula. Any interior point has positive probability of reaching another within a suitable compact interval. This interior regularity differs from the regular boundary type.

## 2. Differentiation, Stopping and Borel Extension of the Green Kernel

<a id="scale-green"></a>

\[ D=S(\beta)-S(\alpha),\quad G(x,y)=\frac{(S(x\wedge y)-S(\alpha))(S(\beta)-S(x\vee y))}{D},\quad u_f(x)=\int_\alpha^\beta G(x,y)f(y)m^\prime(y)dy. \]

For continuous f write A(x)=∫_αˣ(S(y)−S(α))f(y)m′dy and B(x)=∫ₓᵝ(S(β)−S(y))f(y)m′dy. Then u_f=((Sβ−Sx)A+(Sx−Sα)B)/D. The endpoint terms cancel when differentiating, giving \(u_f^\prime\)/p=(B−A)/D and derivative −f m′. Hence \(Lu_f\)=(1/m′)(\(u_f^\prime\)/p)′=−f with zero endpoint values. This also verifies the scale-slope jump −1 and normalization.

Stopped Itô gives \(u_f\)(x)=E \(u_f\)(Xₜ∧τ)+E∫₀ᵗ∧τ f(Xₛ)ds. Bounded f and finite Eτ allow DCT as t→∞. For fixed x, both sides define finite Borel measures on [α,β], agreeing on all continuous functions. Continuous distance cutoffs increase to open-set indicators; measure uniqueness gives equality, and MCT extends to every nonnegative Borel f. Signed f requires absolute integrability.

With f=\(\mathbf1_{\{y_0\}}\), atomless m gives E∫₀ᵗ∧τ\(\mathbf1_{\{X_s=y_0\}}\)ds=0, hence zero occupation almost surely. Countable interval exhaustion and integer horizons extend this to lifetime for each fixed y₀. We have not intersected exceptional sets over uncountably many points or inferred that the path never hits y₀.

## 3. Exhaustion and One-Sided Return Formulas

<a id="scale-exhaustion"></a>

Take αₙ↓ℓ,βₙ↑r and exit times τₙ↑ζ. For f≥0 the occupation integrals increase to the lifetime integral, so MCT passes expectations. The kernels Gₙ(x,y) also increase pointwise. On the old interval their difference is L-harmonic in x, with nonnegative boundary values, hence nonnegative by linearity in scale. Extension by zero preserves this order. Define \(G_I\) as the increasing limit, possibly infinite. The limit is independent of exhaustion: each fixed compact interval of either exhaustion is eventually contained in the other. Kernel monotonicity gives both limit inequalities, even for infinite limits.

For fixed α with S(r)=∞, α is hit almost surely: \(P_x\)(\(\tau_\beta<\tau_\alpha\))→0 and compact exits are finite. A path not hitting α must first hit every β, an event of vanishing probability. The limiting kernel is S(x∧y)−S(α), giving

\[ E_x\int_0^{\tau_\alpha}f(X_t)dt=\int_\alpha^x(S(y)-S(\alpha))f(y)m(dy)+(S(x)-S(\alpha))\int_x^r f(y)m(dy). \]

Infinite values are permitted. Symmetrically, if S(ℓ)=−∞ the kernel for hitting β from x<β is S(β)−S(x∨y) on (ℓ,β). These formulas will compute entrance return bounds and cycle rewards, without confusing infinite expectation with infinite realized time.

## 4. Discounted Green Kernels and Speed Symmetry

<a id="scale-resolvent"></a>

Fix λ>0 and compact (α,β). The linear ODE Lh=λh has a unique solution by Picard for its two-dimensional first-order integral system with continuous bounded coefficients. Choose u(α)=0,u′(α)/p(α)=1 and v(β)=0,v′(β)/p(β)=−1. The relation (u′/p)′=λum′ makes u positive and increasing on (α,β]; reversing from the right makes v positive and decreasing. A first loss of positivity would contradict the maintained derivative sign.

\[ w_\lambda=\frac{u^\prime v-uv^\prime}{p}>0\text{ is constant},\qquad G^\lambda_{\alpha,\beta}(x,y)=\frac{u(x\wedge y)v(x\vee y)}{w_\lambda}. \]

Differentiate the Wronskian using h″=(λh−bh′)/a and p′/p=−b/a; its derivative is zero. The scale derivative of the kernel jumps by −1 at y, and elsewhere (L−λ)G=0. For continuous f, \(u_f^\lambda\)=∫Gλf dm solves (λ−L)u=f with zero boundary values. Stopped Itô for e⁻λᵗu(Xₜ), followed by t→∞, gives \(R_\lambda^{\alpha\beta}\)f=\(E_x\)∫₀^τe⁻λᵗf(Xₜ)dt. Extend to Borel functions as in section 2; |Rλf|≤||f||∞/λ.

Symmetry Gλ(x,y)=Gλ(y,x) gives ∫gRλf dm=∫fRλg dm for nonnegative f,g, with Tonelli allowing infinity. Exhausting the interval makes nonnegative path integrals increase to the minimal resolvent, preserving symmetry. This is the symmetry actually used to prove invariance, rather than a merely formal integration by parts.

## 5. Scale Changes and Factor Checks

<a id="scale-normalization"></a>

If S is replaced by AS+B with A>0, p becomes Ap, m becomes m/A and G becomes AG. Hitting probabilities and Gm remain unchanged. Since a=σ²/2, standard Brownian has S=x,m=2dx. Integrating the section 2 kernel against 2dy yields (x−α)(β−x), directly checked by ½u″=−1.

In natural scale Y=S(X), dY=α(Y)dW with α(y)=p(S⁻¹y)σ(S⁻¹y)>0 locally Lipschitz. Its speed density is 2/α(y)²; changing back using dy=p(x)dx gives m′(x)dx. This uses a deterministic C² change of coordinate, not an already constructed general random time change for singular speeds. Return to the [chapter’s Green kernel](../chapters/36-scale-speed.md#diffusion-green).
