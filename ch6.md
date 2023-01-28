# Units

## $d ≡ 2, 3 \mod 4$

$$N(α) = a² - db² = 1$$

Note $d < 0$ so either $a² = 1$ or $-db² = 1$.

$$a = ±1$$

When $d = -1$, then $b = ±1$ so we also have $±i$.

## $d ≡ 1 \mod 4$

$$N(α) = 1 ⇔ (2a + b)² - db² = 4$$
$$d = -3, -7, -11, …$$
We cannot have $-db² ≤ 4$ for $d < -3$, so $b = 0$.
$$(2a + 0) = 4 ⇒ a = ±1$$

Now consider $d = -3$. $|b| ≥ 2 ⇒ -db² ≥ 12$.
So $b = -1, 0, 1$.
Then by solving we find all units for $d = -3$ are
the 6th roots of unity.

## Summary

Note $\bar{ω} = ω^{n - 1}$ so $N(ω) = ω \bar{ω} = ω^n$.

# Euclidean Imaginary Quadratic Fields

See `ch6-euclid.py`. With $d = -19$, the top vertex becomes
$1.14i$.
$$ N\left(\frac{α}{β} - κ\right) > 1 ⇒ N(ρ) = N(α - κβ) > N(β) $$
Let $α = 28 \sqrt{d}, β = 108$, then $α/β = 1.13i$. Then we
can confirm the above is true.

## $x = qu + r$ for $u$ a non unit, and $r = 0$ or $r$ a unit

$I$ is the maximal ideal containing all non units of $R$.
Let $u ∈ I$ such that $𝜙(u)$ is minimal in $I$. Then
$$ x = qu + r \textrm{ with } 𝜙(r) < 𝜙(u) \textrm{ or } r = 0 $$
If $r = 0$, then $x = qu$. So assume $r ≠ 0$.

$r ∉ I$ because $𝜙(u)$ is minimal, so $r$ is a unit.

## $ℤ_K$ is not Euclidean

By previous result, $u | α$ or $u | 2 ± 1$.

$u$ cannot divide $1$ since it is not a unit, so $u | 2$ or $3$.

$$ N\left(a + b\left(\frac{1 + \sqrt{d}}{2}\right)\right) = a² + ab + b² \left(\frac{1 - d}{4}\right) $$

$d < -11 ⇒ k = \frac{1 - d}{4} ≥ 4$.

$$ a² + ab + kb² = 2, 3 $$
Complete the square and see there's no solution. So both $2, 3$ are irreducible.
$u = 2, -2, 3, -3$.

Now let $α = \frac{1 + \sqrt{d}}{2}$, but $u \nmid α$ and $u \nmid α ± 1$.
So $u$ does not exist.
