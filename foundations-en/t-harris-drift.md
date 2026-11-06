# Local Common Mass, Drift and a Quantitative Harris Theorem

## 1. Making local common mass recur

<a id="drift-assumptions"></a>

Let E be standard Borel, V:E→[1,∞) everywhere finite, and PV≤γV+K with 0<γ<1,K≥0. Choose R>max(1,2K/(1−γ)), put C={V≤R}, and verify P(x,·)≥εν on C for specified 0<ε<1 and ν. These data do not follow merely from the presence of noise.

Put d=(1−γ)R−K>0. Outside C the conditional drift is at most −d. Finite stopped telescoping gives \(E_x\)(\(\tau _C\)∧n)≤V(x)/d, then monotone convergence gives \(E_x\)\(\tau _C\)≤V(x)/d. Applying this after a departure from C bounds mean return. After a failed split, mean V of the next state is at most (γR+K)/(1−ε); after success, νV≤(γR+K)/ε. Geometrically many trials with these uniform excursion bounds give a finite mean ν-regeneration cycle.

Thus C is revisited indefinitely, the cycle measure normalizes, and the chain is positive Harris recurrent. The direct contraction proof next also yields aperiodic geometric convergence without presupposing a cycle-span calculation.

## 2. Why a weighted distance is needed

<a id="drift-metric"></a>

\[ w(x)=1+\beta V(x),\quad d_\beta(x,y)=\mathbf1_{\{x\ne y\}}\bigl(2+\beta V(x)+\beta V(y)\bigr),\quad \|\mu-\eta\|_w=\int w\,d|\mu-\eta|. \]

This is a metric: when an intermediate point differs from both endpoints, the right side of the triangle inequality exceeds the left by 2+2βV(y); coincidence cases are immediate. Put the common part of μ,η on the diagonal and couple the mutually singular remainders. Its expected dβ is exactly ∫w d|μ−η|. No coupling costs less, since its diagonal mass cannot exceed the common part. Weighted variation is therefore both the worst error over |f|≤w and the optimal weighted coupling cost.

## 3. Two estimates, far away and nearby

<a id="drift-contraction"></a>

For x≠y write S=V(x)+V(y). If S≥R, independent next steps have expected cost at most 2+βγS+2βK. Relative to 2+βS this is uniformly smaller than one because R>2K/(1−γ). If S<R both points lie in C. The common εν-part makes the next states equal with probability at least ε; the remaining cost is at most 2(1−ε)+βγS+2βK. Choose β>0 with β(γR+2K)≤ε; this is at most 2−ε.

\[ r=\max\left\{\gamma,\frac{2+\beta\gamma R+2\beta K}{2+\beta R},1-\frac{\varepsilon}{2}\right\}<1,\qquad E\,d_\beta(X_1,Y_1)\le r\,d_\beta(x,y). \]

Use a diagonal kernel when x=y. All branches are measurable. First optimally couple μ,η by their common part, then use the preceding conditional transition coupling. This gives \(\|\mu P-\eta P\|_w\)≤r\(\|\mu -\eta \|_w\). Separate returns of the two paths to C would not suffice; the partition by their combined S supplies simultaneous control.

## 4. Completeness, existence and all initial states

<a id="drift-existence"></a>

Probabilities of finite w-moment are complete: multiplication by w identifies weighted signed measures isometrically with finite-variation measures, whose completeness follows from L¹ densities or summable series. The limit remains nonnegative of mass one with finite w-integral. Drift makes P preserve this space. Contraction makes \(\delta _x\)Pⁿ Cauchy, giving an invariant π. Integrating drift, now with finite moment, yields πV≤K/(1−γ).

\[ d_{\rm TV}(P^n(x,\cdot),\pi)\le\frac{r^n}{2}\bigl(2+\beta V(x)+\beta\pi V\bigr). \]

If another invariant η has infinite V-moment, integrate the minimum of the pointwise bound and one. Bounded convergence gives ηPⁿ→π, hence η=π. Every initial probability converges, but this does not produce a geometric constant uniform over all starting states.

## 5. A computable Gaussian example and return

<a id="drift-ar"></a>

For \(X_{n+1}\)=a\(X_n\)+σ\(Z_{n+1}\), |a|<1,σ>0 and iid standard Gaussian Z, take V=1+x². Then PV=1+a²x²+σ²≤γV+K with a²<γ<1 and suitable K. C is compact; the Gaussian transition density has a positive common lower bound c on C×D for a fixed D=[−b,b]. The uniform ν on D and ε<min(1,2bc) verify minorization. The theorem gives a unique invariant law and the quantitative bound.

Gaussian sums or characteristic functions verify invariance of N(0,σ²/(1−a²)), so uniqueness identifies π. Under shared Z the difference is aⁿ(x−y), never exactly zero when a≠0 and x≠y. Thus total variation forgetting holds although this particular synchronous coupling fails to meet. Another coupling can succeed without changing either marginal path law.

Return to [Chapter42](../chapters/42-harris-coupling.md#harris-drift). This is a complete sufficient geometric Harris theorem for specified drift and minorization data, not a claim that every positive recurrent system has a geometric rate.
