# T-MECKE: Poisson Identification, Cox Bias, and Cluster Palm Laws

Return to [Chapter 50](../chapters/50-palm-gibbs.md#palm-mecke). We use the single-occurrence deletion and joint measurability of T-PALM. The Poisson part permits atomic intensity and multiplicities. The series and σ-finite assembly identity also hold on standard Borel parent spaces; the locally finite Radon formulation uses LCSC metric spaces and locally finite intensity. Palm probabilities for Cox and cluster laws additionally require σ-finite mean intensity.

## 1. An Occurrence-by-Occurrence Finite-Intensity Calculation

<a id="mecke-finite"></a>

First let μ(E)=a<∞; for a=0 both sides vanish. Chapter 48 constructs N=Σᵢ≤KδZi, with K Poisson(a) and Zi iid μ/a. For nonnegative measurable g, label symmetry, Tonelli, and \(k/k!=1/(k-1)!\) give

\[ \mathbb E\sum_{i=1}^Kg(Z_i,N-\delta_{Z_i})=e^{-a}\sum_{k\ge1}\frac{a^k}{k!}k\int g(x,\eta)\frac{\mu(dx)}a\,\mathcal L\!\left(\sum_{j=1}^{k-1}\delta_{Z_j}\right)(d\eta)=\int\mathbb E g(x,N)\mu(dx). \]

Two labels at the same position remain two occurrences, and removing i removes only its occurrence. The argument therefore includes atomic μ. It does not condition on an event of having a point at x; it compares adjacent terms in the complete Poisson series.

## 2. σ-Finite Assembly and the Full Mecke Identity

<a id="mecke-sigma"></a>

Partition E into disjoint Dⱼ of finite μ-mass. The restrictions of N to Dⱼ and its complement are independent. Fix the exterior configuration and apply the finite-intensity formula to the sum inside Dⱼ, allowing g to depend on the entire configuration. Integrate over the independent exterior to obtain \(\mathbb E\int_{D_j}g(x,N-\delta_x)N(dx)=\int_{D_j}\mathbb E g(x,N)\mu(dx)\). Sum over j using Tonelli. The nonreduced form follows by substituting g(x,η)=f(x,η+δₓ).

\[ \mathbb E\int g(x,N-\delta_x)N(dx)=\int\mathbb E g(x,N)\mu(dx),\qquad \mathbb E\int f(x,N)N(dx)=\int\mathbb E f(x,N+\delta_x)\mu(dx). \]

Iterating the one-point identity r times gives the factorial Mecke formula for r different occurrences and a test of the remaining configuration. Each deletion makes the next sum range over remaining occurrences, exactly producing ordered distinct labels, even when spatial coordinates coincide. All integrals are nonnegative, so Tonelli permits their interchange. The induction does not remove spatial diagonals; doing so would be wrong for atomic intensity.

## 3. Why the Identity Characterizes Poisson Law

<a id="mecke-characterization"></a>

Let Ξ be a locally finite point process satisfying the reduced identity with deterministic Radon μ. Taking g(x,η)=h(x) first gives mean μ. Thus EΞf=μf<∞ for \(f\in C_c^+\). Put \(L(t)=\mathbb E e^{-t\Xi f}\). Difference quotients are dominated by Ξf, giving a right derivative at zero and a derivative for t>0. Substitute \(g(x,\eta)=f(x)e^{-tf(x)}e^{-t\eta f}\) to obtain

\[ -L^{\prime}(t)=L(t)\mu(fe^{-tf}),\qquad L(0)=1,\qquad L(t)=\exp\{-\mu(1-e^{-tf})\}. \]

The linear ordinary differential equation is solved by an integrating factor, without presuming L is nonzero. Taking t=1 gives the Poisson functional, and Chapter 49 uniqueness gives Ξ with law PRM(μ). The converse was proved above. This characterizes the entire law, rather than just a Poisson moment identity. T-PALM gives the full Palm law N+δₓ and reduced Palm law N. In the stationary finite-intensity case, P⁰=Law(N+δ₀) also characterizes homogeneous Poisson law, since stationary Campbell converts it back into Mecke’s identity.

## 4. How a Cox Environment Is Reweighted

<a id="mecke-cox"></a>

Let N conditional on random Radon Λ be PRM(Λ), with σ-finite ν=EΛ. Apply T-PALM to mass Λ marked by Λ itself, writing the directing-measure Palm kernel as Rₓ(dλ). Conditional Mecke, the tower property, and disintegration give

\[ \mathbb E\int g(x,N-\delta_x)N(dx)=\int\nu(dx)\int R_x(d\lambda)\int g(x,\eta)\operatorname{PRM}(\lambda)(d\eta). \]

The reduced Palm law is a Cox mixture over the reweighted intensity kernel, and the full Palm law adds one δₓ. The original directing law is not simply reused. All identities first hold for nonnegative joint tests, and one common ν-null set is obtained from countable generating classes, rather than arbitrary unrelated versions at every x.

In particular, if Λ=Zμ with 0<EZ<∞, the directing Z has law \(P^*(dz)=zP_Z(dz)/\mathbb EZ\) under Rₓ, for μ-almost every x. Equal prior probabilities for Z=1 and Z=3 give P*(Z=3)=3/4. If EZ² is finite then E*Z=EZ²/EZ; otherwise this expectation is infinite. For bounded increasing a, \(\operatorname{Cov}(Z,a(Z))=\frac12\mathbb E[(Z-Z^{\prime})(a(Z)-a(Z^{\prime}))]\ge0\). Bias toward high intensity is therefore a calculation, not a metaphor. When EZ=∞, Zdx has infinite stationary intensity, so finite-λ Palm probability normalization is unavailable.

## 5. How a Typical Daughter Selects a Cluster

<a id="mecke-clusters"></a>

Let Poisson parent marks (x,ζ) have intensity a(dx)Q(x,dζ), with locally finite daughter point measures ζ, and let Ψ=Σζᵢ be locally finite almost surely. Additionally assume σ-finiteness of \(\nu(A)=\int a(dx)\int\zeta(A)Q(x,d\zeta)\). Chapter 49’s local mass criterion constructs Ψ; σ-finiteness of its mean is an extra hypothesis here. Group the daughter sum by parent occurrence and apply Mecke to the parent PRM to obtain

\[ \mathbb E\int g(u,\Psi-\delta_u)\Psi(du)=\int a(dx)\int Q(x,d\zeta)\int\zeta(du)\,\mathbb E g(u,\Psi+\zeta-\delta_u). \]

On the right, Ψ is an independent background with the original cluster law; Poisson insertion restores the whole selected parent’s daughter cluster. Disintegrating a(dx)Q(x,dζ)ζ(du) along u by the same finite-weight method gives a kernel for the selected cluster and parent. Adding an independent background and deleting one δᵤ gives reduced Palm law. Parent locations need not be locally finite; σ-finite parent intensity and the stated output conditions suffice.

For stationary translated clusters, take parent intensity κdy and an independent finite shape ζ, with K=ζ(E), 0<EK<∞, translated by each parent location. Tonelli gives ν=κEK du and hence local finiteness. Changing variables u=y+v shows that full P⁰ is an independent background Ψ plus \(\theta_V\zeta^*\), where \(Q^*(d\zeta)=KQ(d\zeta)/EK\), and V is uniform among the K occurrences conditional on ζ*. Reduced Palm deletes δ₀ afterward. If each shape is Kδ₀ with equal probabilities for K=1 and K=2, Palm root multiplicities have probabilities 1/3 and 2/3. The background has no point at zero, since its finite mean intensity is diffuse.
