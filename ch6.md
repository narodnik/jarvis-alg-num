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

# Every positive definite form is properly equivalent to a reduced form (theorem 6.14)

We already saw above that the smallest possible value for a reduced form is
$f(x, y) = a$.

## Algorithm

```python
if a > c or (a = c and b < 0):
    (a, b, c) → (c, -b, a)                  #1
# Remaining two cases
elif a < c:
    if b <= -a:
        (a, b, c) → (a, b + 2a, c + b + a)  #2
    else:
        assert b > a
        (a, b, c) → (a, b - 2a, c - b + a)  #3
elif a = c and b >= 0:
    assert b > a
    (a, b, c) → (a, b - 2a, c - b + a)      #4
```

First observe that in all the steps, $a$ does not increase.
Eventually it must become constant.

In the remaining two cases, the absolute value of $|b|$ gets smaller.
We will show that for each case.

### Branch 2: $b ≤ -a$

First assume $b = -a ⇒ |b| = a$, then we see that
$(a', b', c') = (a, a, c)$ and $b' = |b|$.
Now $a = b < c$ so the form is reduced.

Now assume $b < -a ⇒ a + b < 0 ⇒ 2a + b < a$.
But since $a > 0 ⇒ -a < 0$, we see
$b < -a < 0$.

If $2a + b > 0$ then
$|2a + b| = |b'| < a$. But $b < -a ⇒ a < |b| ⇒ |b'| < |b|$.

Else $b' = 2a + b < 0$, then
$a > 0, b < 0 ⇒ 2a + b > b$ so $|b'|$ also is smaller.

### Branch 3: $b > a$

$b > a$ and $a > 0 ⇒ 0 < a < b$.
$$ b - 2a < b $$

If $b - 2a ≥ 0$ then $|b - 2a| < |b|$ and we are done.

So now $b - 2a < 0$. Also $b > a ⇒ b - a > 0$.
We want to disprove $|b - 2a| ≥ |b|$.

First assume $|b - 2a| = |b|$, then $b > 0 ⇒ b - 2a = -b ⇒ a = 0$
which is impossible so $|b - 2a| > |b| = b$.
$$ ⇒ b - 2a < -b $$
$$ 2b - 2a < 0 $$
$$ b < a $$
which is a contradiction.

### Branch 4

The proof is essentially the same as branch 3, since $b > a$ and the transform
is the same.

## Determinant is Fixed

We can easily show algebraically the determinant is unchanged when applying any transform.
So $b'^2 - 4a'c' = b² - 4ac$.

When $a = b$, then $c$ is also fixed.

