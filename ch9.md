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

