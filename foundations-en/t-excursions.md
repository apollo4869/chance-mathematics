# T-EXCURSIONS: Proving Poisson Excursions by Threshold Regeneration

Companion to [Chapter 37](../chapters/37-local-time.md#local-excursion-clock). Start B at zero, use its symmetric local time L from T-LOCAL-TIME, and put R=|B|. The right local time of R at zero is not L. Throughout, n is the intensity of positive R-excursions indexed by L; signed B-excursions have intensity n/2 for each sign. Inputs are Chapter 26 strong Markov/reflection, Chapter 21 exponential renewal, Chapter 27 minimal PRM and the already constructed L.

## 1. Path Pieces, Labels and Measurability

<a id="excursion-proof-space"></a>

E consists of finite-lifetime continuous nonnegative paths, zero at 0 and after ζ>0, and strictly positive on (0,ζ). Encode (e,ζ) in C_loc×(0,∞). Zero endpoint and post-lifetime conditions and strictly positive minima on every interior rational compact interval are countable measurable conditions, making E standard Borel. The lifetime is uniquely determined by the path and height H=sup e is measurable.

The complement of the zero set is a countable disjoint union (g,d). Enumerate components by their first rational point in a fixed enumeration. The nearest zero on each side is a Borel path functional. Set e(t)=R(g+t) until d−g and zero afterward, with label ℓ=\(L_g\)=\(L_d\). Strong Markov cannot be applied directly at g: last departure from zero is generally not a stopping time.

Distinct excursions have distinct labels. Indeed dL has the entire zero set as support. For rational p<q containing a zero, the first zero after p is a stopping time; strong Markov and the Skorokhod representation make L increase before q almost surely. Countably many rational intervals suffice. Thus nonzero inverse-local-time jumps correspond exactly to excursions. Zero ordinary time on the zero set makes τℓ the sum of the preceding excursion lifetimes.

## 2. First Prove a Finite-Intensity Marked Poisson Process

<a id="excursion-proof-poisson"></a>

Fix ε>0. Wait for Hε, the first |B|-hit of ε, then Dε, the next zero, and restart at Dε. Both are finite stopping times. Retain the entire excursion containing Hε, whose height is at least ε, and discard the others. The distinction between ≥ and > is null for these heights, as also follows from the tail formula below.

Put U=L_Hε. On [−ε,ε] take h(x)=A+C|x| with boundary value one and C=qA. Tanaka and finite-variation multiplication make \(e^{-qL}\)h(B), stopped at Hε, a bounded martingale: its dL-coefficient is C−qh(0)=0 and there is no other drift. Since Hε is finite, DCT gives the transform below: U is exponential with mean ε.

\[ Ee^{-qU}=\frac1{1+q\varepsilon},\qquad q\ge0. \]

The full excursion mark must also be independent of U. On {U>l} for deterministic l, \(\tau_l\)<Hε and B\(\tau_l\)=0; the first ε-reaching excursion after \(\tau_l\) is precisely the same retained mark. Strong Markov at \(\tau_l\) gives P(U>l,e∈F)=P(U>l)Qε(F), where Qε is the first retained mark law. Atomlessness of U handles U=l. Half-lines generate σ(U), proving independence. Strong Markov at Dε makes successive pairs (U,e) iid.

Thus ε-reaching excursions, indexed by local time, form a rate-1/ε Poisson clock with iid Qε marks. Chapter 21’s ordered-density and marking calculation gives its Laplace functional on finite local-time windows as exp[−∫dl∫(1−e^{−f})ε⁻¹Qε(de)] for every nonnegative Borel f. This proves Poisson behavior of the actual path pieces, not of a separately constructed point process with the same mean.

Different thresholds delete small marks from the same path decomposition. Their intensities agree on overlaps, as follows by taking expected counts. Define n on {H≥ε} as ε⁻¹Qε; thresholds 1/k exhaust E and produce a unique σ-finite measure. MCT in the finite-threshold Laplace functionals gives the full PRM with intensity dl n(de).

\[ n(H\ge a)=a^{-1},\qquad E\exp\!\left[-\sum_\ell f(\ell,e_\ell)\right]=\exp\!\left[-\int_0^\infty\!\int_E(1-e^{-f(\ell,e)})n(de)d\ell\right]. \]

Sign symmetry makes each mark’s sign fair and independent of its absolute shape, retaining independence from the exponential interval. Marking therefore gives independent positive and negative B-excursion PRMs, each of intensity dl n(de)/2. Chapter 27’s finite-band Laplace uniqueness identifies the disjoint Borel counts; general point-process theory from Chapter 48 is unnecessary.

## 3. Lifetime Intensity and Clock Normalization

<a id="excursion-proof-lifetime"></a>

Summing excursion lifetimes and applying the PRM functional identifies the inverse-clock exponent as n(1−e^{−λζ}). T-LOCAL-TIME computed that transform independently, so it equals √(2λ). Direct integration yields the density below. For uniqueness differentiate in λ to identify the finite weighted measure ζe^{−ζ}n(dζ), then use Chapter 13 Laplace uniqueness. Difference quotients and exponential-integrability bounds justify differentiation.

\[ n(1-e^{-\lambda\zeta})=\sqrt{2\lambda},\qquad n(\zeta\in ds)=\frac{ds}{\sqrt{2\pi}s^{3/2}},\qquad n(\zeta>t)=\sqrt{\frac2{\pi t}}. \]

Constants depend on the local-time scale. Right local time of R at zero equals 2L: the positive-part Tanaka formula for nonnegative R reads R=∫1_{R>0}dR+½\(L_R^{0,+}\), which compared with R=β+L gives the identity. Indexing by \(L_R^{0,+}\) would halve the excursion intensity. These conventions cannot be mixed.

## 4. An Entrance Law without Markov at Last Zero

<a id="excursion-proof-entrance"></a>

\[ q_t(x,y)=\frac{e^{-(y-x)^2/(2t)}-e^{-(y+x)^2/(2t)}}{\sqrt{2\pi t}},\qquad k_t(y)=\lim_{x\downarrow0}\frac{q_t(x,y)}x=\frac{2y}{\sqrt{2\pi}t^{3/2}}e^{-y^2/(2t)}. \]

Reflection gives the killed positive-half-line kernel q. We prove that kₜ(y)dy is the n-entrance law and subsequent transitions use q. For an ε-reaching retained excursion let ρ be its internal first-ε time. Pathwise ρ≤Hε, so \(E_{Q_\varepsilon}\rho\)≤E Hε=ε². The actual Hε is a stopping time; its following path until zero is killed Brownian motion from ε, independent of the initial excursion segment.

Take 0<t₁<⋯<tⱼ and bounded continuous tests compactly supported in each coordinate. On ρ≤t₁/2, replacing tᵢ by tᵢ−ρ changes only the time in the first q-kernel. The displayed Gaussian difference shows qᵤ(ε,y)/ε and its u-derivative have uniform integrable bounds for u≥t₁/2 on the required y-compacts; intermediate time differences are unchanged. The error after division by ε is at most C Eρ, tending to zero. The n-mass of ρ>t₁/2 is at most 2Eρ/(εt₁)≤2ε/t₁.

Let ε decrease to zero. Discarded low-height excursions have vanishing n-mass within {ζ>t₁}, a finite-measure set. The finite-dimensional law is therefore the product below. A monotone-class argument extends continuous tests to Borel tests, and the post-slice residual path is killed Brownian motion. No strong Markov step was taken at the last zero g.

\[ n(e(t_1)\in dy_1,\ldots,e(t_j)\in dy_j,\ t_j<\zeta)=k_{t_1}(y_1)\prod_{i=2}^jq_{t_i-t_{i-1}}(y_{i-1},y_i)\,dy_1\cdots dy_j. \]

## 5. Lifetime Disintegration and a Constructed Normalized Excursion

<a id="excursion-proof-normalized"></a>

\[ h_u(y)=\frac{y}{\sqrt{2\pi}u^{3/2}}e^{-y^2/(2u)},\qquad c_s=\frac1{\sqrt{2\pi}s^{3/2}},\qquad Q_s(dy_1\cdots dy_j)=\frac{k_{t_1}(y_1)\prod_{i=2}^jq_{t_i-t_{i-1}}(y_{i-1},y_i)h_{s-t_j}(y_j)}{c_s}\,dy_1\cdots dy_j. \]

The function h is the first-zero density. Applying it after tⱼ gives the joint n-law with ζ. Chapter 10 standard-Borel disintegration supplies conditional laws, unique only for almost every s. To select every s and construct actual continuous paths, take the Euclidean norm Eˢ of three independent zero-to-zero Brownian bridges of length s. It is continuous, zero at the endpoints and strictly positive inside: on each [δ,s−δ], the three-dimensional bridge is locally absolutely continuous with respect to three-dimensional Brownian motion, which does not hit a specified point; countably many δ suffice.

Check finite-dimensional laws directly. Integrating the three-dimensional Gaussian over spheres gives radial transition density qₜ(x,y)y/x for x>0 and entrance density √(2/π)y²\(t^{-3/2}\)\(e^{-y^2/(2t)}\) at zero. The bridge’s terminal correction is \((s/(s-t_j))^{3/2}\)\(e^{-y_j^2/(2(s-t_j))}\). Multiplying telescopes the successive y/x factors and gives exactly Q_s above. Thus Eˢ has the conditional excursion law; scaling time by s and space by √s from E¹ supplies all s.

The process e=E¹ is the normalized Brownian excursion. It is not an undefined conditioning of an ordinary bridge on the null event of remaining positive. Three bridges construct it, and lifetime disintegration identifies it. Conditioned random-tree functional limits remain Chapter 53’s responsibility. Return to [normalized excursions](../chapters/37-local-time.md#local-normalized).
