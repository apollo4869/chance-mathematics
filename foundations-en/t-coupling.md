# Coupling, Common Mass and Time Alignment

## 1. Marginals and paths

<a id="coupling-measure"></a>

Let E be standard Borel. A coupling of probabilities μ and η is a probability Γ on E×E with these two marginals. We use the following total variation convention; the third supremum is over measurable real functions.

\[ d_{\rm TV}(\mu,\eta)=\sup_A|\mu(A)-\eta(A)|=\frac12\int|p-q|\,d\lambda=\frac12\sup_{|f|\le1}|\mu f-\eta f|,\quad \lambda=\mu+\eta,\ p=\frac{d\mu}{d\lambda},\ q=\frac{d\eta}{d\lambda}. \]

Put a=min(p,q)λ, whose mass is 1−dTV. Put this common part on the diagonal; for the remaining mass use the product of the normalized residual measures. Their supports {p>q} and {q>p} are disjoint. Omit branches of mass zero. This constructs a maximal coupling. Every coupling satisfies the next inequality, since the two indicators can differ only where the coordinates differ.

\[ d_{\rm TV}(\mu,\eta)\le \Gamma\{(x,y):x\ne y\}. \]

Applying a Markov kernel K to both measures contracts total variation, because |Kf|≤1. If a kernel Q on E×E has marginals P(x,·),P(y,·) and uses identical randomization on the diagonal thereafter, sequential kernel construction gives two valid P-chains. They stay equal after their meeting time τ.

\[ d_{\rm TV}(\mathcal L(X_n),\mathcal L(Y_n))\le\mathbb P(\tau>n). \]

Measurable common randomization uses Chapter 10; the diagonal is Borel. This construction says nothing about the meeting of two originally independent realizations.

## 2. Common mass and uniform forgetting

<a id="coupling-global"></a>

If P(x,·)≥εν for every x and 0<ε<1, the residual \(R_x\)=(P(x,·)−εν)/(1−ε) is a probability kernel. A shared Bernoulli(ε) coin sends both coordinates to the same ν-state on success, and otherwise uses their residuals. Lock them together after meeting. Thus P(τ>n)≤(1−ε)ⁿ. If ε=1, forgetting takes one step.

Existence is not assumed. Probabilities are complete in total variation: relative to λ=Σ2⁻ʲ\(\mu _j\), a Cauchy sequence has an L¹ density limit, nonnegative with integral one. The map μ↦μP is a strict contraction. Its iterates have summable successive distances and converge to a fixed point π. Contraction also gives uniqueness.

## 3. Two ways to align time

<a id="coupling-shift"></a>

Successful same-time coupling requires \(X_n\)=\(Y_n\) after a finite τ. Shift coupling only asks for finite integer R,S such that \(X_{R+k}\)=\(Y_{S+k}\) for every k≥0. The latter does not imply convergence at equal times: opposite phases of the alternating chain coincide after a one-step shift but stay at total variation distance one at equal times.

The regenerative construction below gives an actual shift coupling. Finite mean cycles and aperiodicity then synchronize two regeneration clocks. The resulting coupling need not be adapted to both original filtrations simultaneously; what matters is that each complete path has its correct law.

## 4. Dependencies and return

<a id="coupling-back"></a>

Only Radon–Nikodym, kernel randomization, sequential construction and L¹ completeness were used. A local small set cannot replace global common mass. Return to [Chapter 42](../chapters/42-harris-coupling.md#harris-common), then use [T-HARRIS-REGENERATION](t-harris-regeneration.md).
