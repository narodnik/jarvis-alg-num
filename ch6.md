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

# Quadratic Forms

Positive definite forms $f(x, y) ≥ 0$ and
$f(x, y) = 0 ⇒ (x, y) = (0, 0)$.

Therefore $a, c > 0$ since $f(x, 0), f(0, y) > 0$.
Complete the square to see $b² - 4ac < 0$.
$$ ax² + bxy + cy² = a\left(x + \frac{b}{2a} y\right)² + \left(c - \frac{b²}{4a}\right) y² $$

A form is normal if $-a < b ≤ a$.

A form is reduced if it is normal and $a < c$ or $a = c$ and $b ≥ 0$.

Generators for $\textrm{SL}₂(ℤ)$
$$
T =
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
\qquad \textrm{and} \qquad
S = \begin{pmatrix}
0 & 1 \\
-1 & 0
\end{pmatrix}
$$
Which correspond to
$$ (a, b + 2a, c + b + a) \qquad \textrm{and} \qquad (c, -b, a) $$

# Minimum Values

$(x, y)$ are coprime.

$$ |x| ≥ 2 ⇒ f(x, y) > c $$
$$ |y| ≥ 2 ⇒ f(x, y) > c $$

| $x$ | $y$ | $f(x, y)$ |
|-----|-----|-----------|
| -1  | -1  | $> c$     |
| -1  | 0   | $a$       |
| -1  | 1   | $≥ c$     |
| 0   | -1  | $c$       |
| 0   | 1   | $c$       |
| 1   | -1  | $≥ c$     |
| 1   | 0   | $a$       |
| 1   | 1   | $> c$     |

When $a = c$, there are 4 pairs $f(x, y) = a$,
which becomes 6 when $a = b = c$.

## $|y| = 1, |x| ≥ 2$

Complete the square
\begin{align*}
4a f(x, y) &= 4a(ax² + bxy + cy²) \\
           &= (2ax + by)² - (b² - 4ac) y² \\
           &= (2ax + by)² - (b² - 4ac)
\end{align*}
But note that
$$ |2ax + by| ≥ |2ax| - |by| ≥ 4a - |b| ≥ 3a $$
since $|y| = 1$ and $b ≤ a$.
$$ ⇒ 4a f(x, y) ≥ 9a² - (b² - 4ac) = 4ac + 8a² + (a² - b²) $$
but $|b| ≤ a$ so $4a f(x, y) ≥ 4ac$ or
$$ f(x, y) ≥ c $$

## $|y| ≥ 2$

$$ 4a f(x, y) = (2ax + by)² - (b² - 4ac) y² ≥ -(b² - 4ac) y² $$
$$ y² ≥ 4 $$
$$ ⇒ 4a f(x, y) ≥ -4(b² - 4ac) = 16ac - 4b² $$
Note $b² - 4ac < 0$ and we can factor that out.
$$ 4a f(x, y) ≥ 12ac + 4(ac - b²) ≥ 12ac ≥ 4ac $$
$$ f(x, y) > c $$

## Remaining Cases

$(x, y) = 1$ and if $y = 0$, then $x = ±1$ so
$$ f(±1, 0) = a $$

$$ f(0, ±1) = c $$
$$ f(±1, ±1) = a + b + c > c $$
$$ f(±1, ∓1) = a - b + c ≥ c $$

# Decompose $M \in \textrm{SL}₂(ℤ)$

$$
M =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

Use $S$ to make $a, c$ positive.

Then use $T⁻¹$ to reduce $a$ so $a < 0$ and $-a < c$.
Then flip them with $S$. This reduces $c$.
Repeat this process.

The final matrix is $\begin{pmatrix}
    1 & s \\
    0 & 1
\end{pmatrix}$ which is some power of $T$.
We now have a decomposition for $M$ by inverting the chain of operations.
