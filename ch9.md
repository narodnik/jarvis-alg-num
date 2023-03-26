---
header-includes: |
    - \newcommand{\leg}[2]{\left( \frac{#1}{#2} \right)}
---
# Polynomial $λ_n(x)$ is irreducible

## Discriminant $Δ = ±nⁿ$

Let $f_n(x) = xⁿ - 1$ and the discriminant
$$ Δ = \prod_{i < j} (ζⁱ - ζʲ)² $$
$$ f_n'(x) = (x - ζ₂)⋯(x - ζ_n) + (x - ζ₁)(x - ζ₃)⋯(x - ζ_n) + ⋯ + (x - ζ₁)⋯(x - ζ_{n - 1}) $$
$$ ⇒ f_n'(ζ₁) = (ζ₁ - ζ₂)⋯(ζ₁ - ζ_n) $$

\begin{alignat*}{2}
n &= 1 \qquad Δ &&= 1 \\
n &= 2 \qquad Δ &&= (ζ¹ - ζ²)² \\
n &= 3 \qquad Δ &&= (ζ¹ - ζ²)² (ζ¹ - ζ³)² (ζ² - ζ³)² \\
n &= 4 \qquad Δ &&= (ζ¹ - ζ²)² (ζ¹ - ζ³)² (ζ² - ζ³)² (ζ¹ - ζ⁴)² (ζ² - ζ⁴)² (ζ³ - ζ⁴)²
\end{alignat*}

$$ Δ = \prod_{i ≠ j} (ζⁱ - ζʲ)² $$

$$ \prod_{i < j} (ζⁱ - ζʲ)² = \prod_{j=1}^n f_n'(ζⁱ) $$

But $f_n'(x) = nx^{n - 1}$
$$ Δ = nⁿ \left( \prod_{j = 1}^n ζⁱ \right)^{n - 1} $$
If $n ≡ 0 \mod{2}$ then $\frac{n²}{2} + \frac{n}{2} ≡ b \mod{n}$ for some $b ∈ ℤ$
where $b = \frac{n}{2}$ so in this case $\sum_{i = 1}^n i ≡ n/2 \mod{n}$.
Otherwise it is 0.

```python
>>> for i in range(1, 10):
...     print(i, (sum(x for x in range(i+1)) % i) / i)
... 
1 0.0
2 0.5
3 0.0
4 0.5
5 0.0
6 0.5
7 0.0
8 0.5
9 0.0
```
So we see
$$ \prod_{j = 1}^n ζⁱ = ±1 $$
$$ Δ = ±nⁿ $$

## $g(x)$ divides $f_n(x)$ and contains one primitive root means it has all roots

*Let there be a $g(x) ∈ ℤ[x]$ such that $g(x)|f_n(x)$ with $g(ζ) = 0$.
We claim $g(ζᵖ) = 0$ for all prime $p ∤ n$.*

Suppose $g(ζᵖ) ≠ 0$. Since $f_n(x) = (x - ζ₁)⋯(x - ζ_n)$ and $g|f_n$, so
for some $d$
$$ g(x) = (x - ζ₁)⋯(x - ζ_d) $$
Then $g(ζᵖ)$ is the product of differences for nth roots of unity, hence
it divides the discriminant $±nⁿ$.

Let $Φ_p$ be the Frobenius automorphism in mod $p$ and note
$$ Φ_p(g(x)) ≡ g(Φ_p(x)) \mod{p} $$
$$ ⇒ p | g(ζᵖ) - g(ζ)ᵖ $$
but $g(ζ) = 0$ so $p | g(ζᵖ)$.

$$ p | g(ζᵖ), \quad g(ζᵖ) | nⁿ ⇒ p | nⁿ ⇒ p | n $$
which is a contradiction. So we get the result.

## $g(x)$ is $λ_n(x)$

Let $g(x)$ be a nontrivial factor of $λ_n(x)$ and therefore of $f_n(x)$.

As before let $ζ$ be a primitive nth root of unity with $g(ζ) = 0$.

Then for all primes $p ∤ n$ the previous result states $g(ζᵖ) = 0$.

$$ μ = \{ ζᵏ : \gcd(k, n) = 1 \} $$
are all the primitive roots for $n$. So it follows $ζᵏ$ for any $k$ coprime to $n$
is also a primitive $n$th root of unity.

Let $k$ be comprime to $n$. Write $k = p₁ ⋯ p_m$.

Then $g(ζ^{p₁}) = 0$ and $ζ^{p₁}$ is a primitive root.

Now let $q_{i + 1} = q_i p_{i + 1}$ with $q_i = p₁$. By the same argument,
$g(ζ^{q_{i + 1}}) = 0$.

Since $k = q_{i + 1}$, we see $g(ζᵏ) = 0$ so every primitive $n$th root of unity
is a root of $g(x) ⇒ g(x) = λ_n(x)$.

$g(x)$ is a generic polynomial dividing $f_n(x)$, so this argument means $λ_n(x)$
is irreducible, since $g(x)$ must $λ_n(x)$ and there are no smaller divisors.

# Exercises

## 9.2

\begin{align*}
ζ²ⁿ &= 1 \\
    &= (ζⁿ)²
\end{align*}
so $ζⁿ = ±1$, but $ζ$ is a primitive $2n$ root of unity so $ζⁿ = -1$.

$n$ is odd, so $(-1)ⁿ = -1$
$$ ⇒ -ζⁿ = 1 \textrm{ or } (-ζ)ⁿ = 1 $$
so $-ζ$ is a primitive $n$th root of unity.

## 9.3.1

$$ m | n ⇒ m = p₁^{k₁} ⋯ p_r^{k_r}, \; n = m p₁^{l₁} ⋯ p_r^{l_r} q₁^{m₁} ⋯ q_t^{m_t} $$
$$ mn = m² p₁^{l₁} ⋯ p_r^{l_r} n $$
$$ \gcd(m² p₁^{l₁} ⋯ p_r^{l_r}, n₁) = 1 $$
$$ ⇒ 𝜙(mn) = 𝜙(m² p₁^{l₁} ⋯ p_r^{l_r}) 𝜙(n₁) $$
\begin{align*}
𝜙(p^{2k + l}) &= p^{2k + l} - p^{2k + l - 1} \\
    &= p^k (p^{k + l} - p^{k + l - 1})
\end{align*}
$$ 𝜙(m² p₁^{l₁} ⋯ p_r^{l_r}) = m 𝜙(m p₁^{l₁} ⋯ p_r^{l_r}) $$
and so we see
$$ \deg λ_{mn}(x) = \deg λ_n(x^m) $$

## 9.3.2

Let $y : λ_n(y) = 0$, then $y ≠ 1$.
For any $a : λ_n(aᵐ) = 0 ⇒ aᵐ ≠ 0$, so $a$ is a primitive root of $λ_{mn}(x)$.

We can divide each poly by $(x - a)$ and since they have the same degree,
we see $λ_{mn}(x) = λ_n(xᵐ)$.

## 9.3.3

Let $g(x) = x^{p^{1 - r}}$, then we can compose the functions
$$ (λ_p ∘ g)(x^{p^{r - 1}}) = λ_p(x) $$
$$ (λ_{pʳ} ∘ g)(x) = λ_{pʳ}(x^{p^{1 - r}}) $$
So observe $pʳ = p^{1 - r} p^{2r - 1} ⇒ p^{1 - r} | pʳ$.

Let $mn = p$ so that $m = p^{1 - r}, n = pʳ$ then
$$ λ_p(x) = λ_{p^r}(x^{p^{1 - r}}) $$
now compose with $g⁻¹$ to get
$$ λ_{pʳ}(x) = λ_p(x^{p^{r - 1}}) $$

### 9.4

$$ λ_p(x) = \frac{xᵖ - 1}{x - 1} $$
$$ λ₁(x) = x - 1 $$
$$ xⁿ - 1 = λ₁(x) λ_p(x) λ_q(x) λ_{pq}(x) $$
Rearrange this last identity and we get
\begin{align*}
λ_q(x) λ_{pq}(x) &= \frac{ xⁿ - 1 }{ λ₁(x) λ_p(x) } \\
    &= \frac{ (xᵖ)^q - 1 }{ (x - 1) · \frac{ xᵖ - 1 }{ x - 1} } \\
    &= λ_q(xᵖ)
\end{align*}


# Discriminants and Integral Bases

## $pℤ_K = ⟨1 - ζ⟩^{𝜙(pʳ)}$

We can see
$$ λ_{pʳ}(X) = X^{p^{r - 1} (p - 1)} + X^{p^{r - 1} (p - 2)} + ⋯ + X^{p^{r - 1}} + 1 \tag{1}$$
Just multiply the denominator out and you can see this holds.

Then the primitive roots are $ζᵍ$ with $g ∈ G = \{ 1 ≤ g ≤ n | \gcd(p, g) = 1 \}$. You can
see that that any $g^{pⁱ}$ is not primitive hence we exclude those.

$$ λ_{pʳ}(X) = \prod_{g ∈ G} (X - ζᵍ) \tag{2}$$

Put $X = 1$ into (1), and we get $λ_{pʳ}(1) = p$ since there are $p - 1$ terms $+ 1$.
Then also substituting into (2) shows

$$ p = \prod_{g ∈ G} (1 - ζᵍ) $$
$$ ⇒ ⟨p⟩ = \prod_{g ∈ G} ⟨1 - ζᵍ⟩ $$

$$ 1 - ζᵍ = (1 - ζ)(1 + ζ + ⋯ + ζ^{g - 1}) $$
which shows $⟨1 - ζᵍ⟩ ⊆ ⟨1 - ζ⟩$.
And we can calculate the converse by finding $h : gh ≡ 1 \mod{pʳ}$ since $ζ^{gh} = ζ¹$.
So both ideals are the same.

Lastly $[ℚ(ζ) : ℚ] = 𝜙(pʳ)$. To see this write $ℚ(ζ)$ in terms of its basis over $ℚ$.
Then you see the generators are all the primitive elements which is $𝜙(pʳ)$.

## Ring of Integers $ℤ_K = ℤ[ζ]$

$$ Δ\{ω₁, …, ω_n \} ℤ_K ⊆ ℤω₁ + ⋯ + ℤω_n $$
$$ Δ\{1, ζ, …, ζ^{k - 1}\} = ±pˢ $$
$$ pˢ ℤ_K ⊆ ℤ[ζ] = ℤ + ℤζ + ⋯ + ℤζ^{k - 1} ⊆ ℤ_K $$

From section 5, we know $pℤ_K = ⟨π⟩ᵏ ⇒ k = [ℚ(ζ) : ℚ]$.

### $ℤ_K = ℤ + πℤ_K$

We know $N_{ℚ(ζ)/ℚ}(π) = p$. By definition $N_{ℚ(ζ)/ℚ}(π) = |ℤ_K / ⟨π⟩|$ which we see is $p$,
so $|ℤ_K/⟨π⟩| = p$. Now lets consider the cosets
$$ a + ⟨π⟩, \quad a ∈ ℤ $$
Now we show correspondence of cosets mod $p$.

Take $a, a' ∈ ℤ$ with $a ≡ a' \mod{p}$, then since $⟨p⟩ ⊂ ⟨π⟩$ we have $a ≡ a' \mod{⟨π⟩}$.

Likewise let $a ≡ a' \mod{⟨π⟩}$, then $a - a' ∈ ⟨π⟩ ⇒ ⟨a - a'⟩ ⊆ ⟨π⟩$, and so
$⟨a - a'⟩ = ⟨π⟩Q$ for some ideal of $ℤ_K$.

Note that $N(a - a') = (a - a')²$ and $N(a - a') = N_{ℚ(ζ)/ℚ}(⟨a - a'⟩)$ so
\begin{align*}
(a - a') &= N_{ℚ(ζ)/ℚ}(⟨a - a'⟩) \\
    &= N_{ℚ(ζ)/ℚ}(⟨π⟩Q) \\
    &= N_{ℚ(ζ)/ℚ}(⟨π⟩) N_{ℚ(ζ)/ℚ}(Q) \\
    &= p N_{ℚ(ζ)/ℚ}(Q) \\
\end{align*}
so we see $p | (a - a')²$ and since $p$ is prime $p | (a - a')$ and $a ≡ a' \mod{p}$ so
$$ a ≡ a' \mod{⟨π⟩} ⇔ a ≡ a' \mod{p} $$
so we see the cosets $a + ⟨π⟩ : a ∈ \{ 0, …, p - 1 \}$ are distinct and
$$ ℤ_K / ⟨π⟩ ≅ ℤ / ⟨p⟩ $$

Since the cosets of $ℤ_K$ are $a + ⟨π⟩, a ∈ ℤ$, we see $ℤ_K = ℤ + πℤ_K$.

# Gauss Sums and Quadratic Reciprocity


$$ τ = \leg{1}{23}ζ + ⋯ + \leg{22}{23}ζ²² $$
$$ τ² = \leg{1}{23}ζ \left[\leg{1}{23}ζ + ⋯ + \leg{22}{23}ζ²²\right] ⋯ + \leg{22}{23}ζ²² \left[\leg{1}{23}ζ + ⋯ + \leg{22}{23}ζ²²\right] $$
Let $c = a⁻¹ b \mod{23} ⇒ b = ac \mod{23}$ and then follow the steps.

$$ 1 + ζ + ⋯ + ζ²² = 0 ⇒ \sum_{a = 0}^{22} ζᵏᵃ = 0 $$
so we see $\sum_{a = 1}^{23} ζᵏᵃ = -1$.

Lastly also note $22 ≡ -1 \mod{23} ⇒ \leg{22}{23} = \leg{-1}{23} = -1$.

## Exercise 9.6: Generalize Above to $p$ Prime

$$ τ = \leg{1}{p} ζ + ⋯ + \leg{p - 1}{p} ζᵖ⁻¹ $$
$$ τ² = \leg{1}{p} ζ \left[ \leg{1}{p} ζ + ⋯ + \leg{p - 1}{p} ζᵖ⁻¹ \right] + ⋯ + \left[ \leg{1}{p} ζ + ⋯ + \leg{p - 1}{p} ζᵖ⁻¹ \right] $$
$$ b = ac \mod{p} $$
\begin{align*}
τ² &= \sum_{a = 1}^{p - 1} \sum_{c = 1}^{p - 1} \leg{a²c}{p} ζᵃ⁺ᵃᶜ \\
    &= \sum_{a = 1}^{p - 1} \sum_{c = 1}^{p - 2} \leg{a²c}{p} ζᵃ⁽¹⁺ᶜ⁾ + \sum_{a = 1}^{p - 1} \leg{a²(p - 1)}{p} ζᵃ⁽¹⁺⁽ᵖ⁻¹⁾⁾ \\
    &= \sum_{a = 1}^{p - 1} \sum_{c = 1}^{p - 2} \leg{c}{p}   ζᵃ⁽¹⁺ᶜ⁾ + \sum_{a = 1}^{p - 1} \leg{-1}{p} \\
\end{align*}
From Pinter chapter 23, H7 we know
$$ \leg{-1}{p} = \begin{cases}
1  \; \textrm{ if } p ≡ 1 \mod{4} \\
-1 \; \textrm{ if } p ≡ 3 \mod{4} \\
\end{cases} $$
$$ τ² = \sum_{c = 1}^{p - 2} \left[ \leg{c}{p} \sum_{a = 1}^{p - 1} ζᵃ⁽¹⁺ᶜ⁾ \right] + (p - 1) \leg{-1}{p} $$
Since $ζ$ is primitive and $ζⁿ - 1 = 0$, then since $\frac{Xⁿ - 1}{X - 1} = 1 + ⋯ + Xⁿ⁻¹$, we can see $\sum_{a = 0}^{p - 1} ζᵃ = 0$
or $1 + \sum_{a = 1}^{p - 1} ζᵃ = 0 ⇒ \sum_{a = 1}^{p - 1} ζᵃᵏ = -1$ for $k ≢ 0 \mod{p - 1}$.

Set $k = 1 + c$ and we see
\begin{align*}
τ² &= \left[ \sum_{c = 1}^{p - 2} \leg{c}{p} · (-1) \right] + (p - 1) \leg{-1}{p} \\
   &= - \sum_{c = 1}^{p - 2} \leg{c}{p} + (p - 1) \leg{-1}{p} \\
\end{align*}
With $ℤ_p^* = \{ 1, …, p - 1 \}$, we can create the group endomorphism $h : ℤ_p^* → ℤ_p^*$ by $h(a) = a²$.
The range of $h$ has $(p - 1)/2$ elements, which means we can split $ℤ_p^*$ into two cosets: quadratic residues and nonresidues.
We therefore see
\begin{align*}
\sum_{c = 1}^{p - 1} \leg{c}{p} &= \leg{1}{p} + ⋯ + \leg{p - 1}{p} = 0\\
    &= \leg{1}{p} + ⋯ + \leg{p - 2}{p} + \leg{-1}{p} \\
    &= \sum_{c = 1}^{p - 2} \leg{c}{p} + \leg{-1}{p}
\end{align*}
$$ \sum_{c = 1}^{p - 2} \leg{c}{p} = - \leg{-1}{p} $$

\begin{align*}
τ² &= \leg{-1}{p} + (p - 1) \leg{-1}{p} \\
   &= \leg{-1}{p} p \\
\end{align*}
