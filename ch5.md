---
header-includes: |
    - \usepackage{mathtools}
    - \usepackage{amsmath}
---

# Ring Theory

* Let $R$ be an integral domain and $p ∈ R$.
  If $⟨p⟩$ is maximal then $p$ is irreducible.
* $I$ is a maximal ideal $⇔ R/I$ is a field.
    * Let $a ∈ R - I$. Then $aR + I = R ⇒ 1 ∈ ab + I$ for some $b$.
      So $(a + I)(b + I) = 1 + I$, and every $a ∉ I$ has an inverse.
* Let $R$ be an integral domain and $p ∈ R$.
  Then $⟨p⟩$ is prime $⇔$ $p$ is prime.
* Let $R$ be a ring. Then $I$ is prime $⇔$ $R/I$ is an integral domain.
    * $(a + I)(b + I) = I ⇒ a \text{ or } b ∈ I$
* Maximal ideals are prime.
* Finite integral domains are fields.

# Prime Ideals

## $ℤ_K/𝔭$ is finite (lemma 5.20)

Let $𝔭$ be a non-zero prime ideal in $ℤ_K$. Let $α ∈ 𝔭, α ≠ 0$.
Then $N(α) ∈ ℤ$ and $α | N(α) ⇒ N(α) ∈ 𝔭$.

$ℤ_K$ has integral basis
$$ℤ_K = ℤω_1 + ⋯ + ℤω_n$$
Since $Nω_i ∈ 𝔭$ by the nature of ideals, then $a_i ω_i ≡ b_i ω_i \mod 𝔭$
where $0 ≤ b_i < N$. It could be smaller but we have established an upper
bound for $b_i$, so $ℤ_K/𝔭$ is finite.

## $K$ is a number field. Every non-zero prime ideal $𝔭 ⊆ ℤ_K$ is maximal (proposition 5.21)

Proof:
* Prime ideal $𝔭 ⇒ ℤ_K/𝔭$ is an integral domain.
* $ℤ_K/𝔭$ is finite (lemma 5.20).
* Finite integral domain is a field.
* $ℤ_K/𝔭$ is a field $⇒ 𝔭$ is a maximal ideal.

# Fractional Ideals

## There are prime ideals $𝔭_1, …, 𝔭_r$ such that $𝔭_1 ⋯ 𝔭_r ⊆ 𝔞$ (lemma 5.24)

$𝔞$ is a non-zero ideal of $ℤ_K$.

$ℤ_K$ is Noetherian.
Since $𝔞$ forms an ascending chain
$𝔞 ⊆ 𝔞_1 ⊆ 𝔞_2 ⊆ ⋯$,
it eventually terminates.

There are no prime ideals $𝔭_1 ⋯ 𝔭_r ⊆ 𝔞$.
The same is true for all ideals in the chain $𝔞_i$.

Lets take $𝔞$ to be the largest ideal in the chain.

$𝔞$ is not prime otherwise $𝔭_1 = 𝔞 ⊆ 𝔞$
and the proof is finished.

So there are ideals $𝔞_1, 𝔞_2$ in $ℤ_K$ such that
$𝔞_1 𝔞_2 ⊆ 𝔞,
𝔞_1 ∉ 𝔞,
𝔞_2 ∉ 𝔞$
Write
$$𝔟_1 = 𝔞 + 𝔞_1,
𝔟_2 = 𝔞 + 𝔞_2$$
Then we can see that
$$𝔟_1 𝔟_2 = (𝔞 + 𝔞_1)(𝔞 + 𝔞_2)
= 𝔞 + 𝔞_1 𝔞 + 𝔞_2 𝔞 + 𝔞_1 𝔞_2$$
Since $𝔞_1 𝔞_2 ⊆ 𝔞$, so
$𝔟_1 𝔟_2 ⊆ 𝔞$.
But also observe that
$$𝔞 ⊊ 𝔟_1, 𝔞 ⊊ 𝔟_2$$

Since $𝔟_1, 𝔟_2$ are bigger than $𝔞$, then by $𝔞$'s maximality,
there exist prime ideals $𝔭_i$ such that
$$𝔭_1 ⋯ 𝔭_s ⊆ 𝔟_1$$
$$𝔭_{s+1} ⋯ 𝔭_t ⊆ 𝔟_2$$
$$⇒ 𝔭_1 ⋯ 𝔭_t ⊆ 𝔟_1 𝔟_2
⊆ 𝔞$$
Which is a contradiction.

## $\mathfrak{a ⊆ b ⇒ b^{-1} ⊆ a^{-1}}$

Let $β ∈ 𝔟^{-1}$
$$β 𝔟 ⊆ ℤ_K$$
but $𝔞 ⊆ 𝔟 ⇒ β 𝔞 ⊆ ℤ_K$ and so
$$β ∈ 𝔞^{-1}$$

## $𝔞^{-1} = \{ α ∈ K : α 𝔞 ⊆ ℤ_K \}$ is a fractional ideal (lemma 5.25)

$$𝔞^{-1} = \{ α ∈ K : α 𝔞 ⊆ ℤ_K \}$$
Let $γ ∈ 𝔞$ and $𝔠 = γ 𝔞^{-1}$.
Take $i, i' ∈ 𝔠$, then $i = γ β, i' = γ β'$ with
$β, β' ∈ 𝔞^{-1}$.
$$(β + β') 𝔞 = β 𝔞 + β' 𝔞 ⊆ (ℤ_K + ℤ_K) = ℤ_K$$

Let $i = γ β ∈ 𝔠$ with $γ ∈ 𝔞, β ∈ 𝔞^{-1}$ and $r ∈ ℤ_K$.
We want to show that $ri ∈ 𝔠$.

But note that $r ∈ 𝔞^{-1}$, so $r β ∈ 𝔞^{-1} ⇒ ri = γ (r β) ∈ 𝔠$.

```python
sage: K.<a> = NumberField(x^2 + 5)
sage: O = K.ring_of_integers()
sage: I = O.ideal(1 + a)
sage: (1 - a) * I
Fractional ideal (6)
sage: (1 - a)/6 * I
Fractional ideal (1)
sage: 1 - a in I^-1
True
sage: a in I^-1
True
sage: I.basis()
[6, a + 1]
sage: factor(I)
(Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1))
```

## $𝔞$ is a proper ideal of $ℤ_K ⇒ ℤ_K ⊊ 𝔞^{-1}$ (lemma 5.26)

### $𝔞 ⊆ 𝔟 ⇒ 𝔟^{-1} ⊆ 𝔞^{-1}$

Let $β ∈ 𝔟^{-1}$, then $β 𝔟 ⊆ ℤ_K$.

But $𝔞 ⊆ 𝔟 ⇒ β 𝔞 ⊆ ℤ_K$

So $β ∈ 𝔞^{-1}$.

Section 4.6 shows $⟨1 - \sqrt{-5}⟩$ is not prime.

```python
sage: K.<a> = NumberField(x^2 + 5)
sage: O = K.ring_of_integers()
sage: I = O.ideal(1 + a)
sage: (1 - a) * I
Fractional ideal (6)
sage: (1 - a)/6 * I
Fractional ideal (1)
sage: 1 - a in I^-1
True
sage: a in I^-1
True
sage: I.basis()
[6, a + 1]
sage: I.is_prime()
False
sage: I.is_maximal()
False
sage: I
Fractional ideal (a + 1)
sage: factor(I)
(Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1))
sage: J = O.ideal(2, a + 1)
sage: J.is_prime()
True
sage: 7 + a in J
True
sage: α = O.ideal(7 + a)
sage: factor(α)
(Fractional ideal (2, a + 1)) * (Fractional ideal (3, a + 1))^3
sage: J.is_prime(), J.is_maximal()  # of course
(True, True)
sage: O.ideal(3 + a+ 1)^3
Fractional ideal (43*a + 4)
sage: β = (43*a + 4)*(10 + a) # choose any random value from the ideal
sage: β in O.ideal(3 + a+ 1)^3
True
sage: β in α
False
sage: β*J
Fractional ideal (277830, 7*a + 150115)
sage: α
Fractional ideal (a + 7)
sage: 277830 in α
True
sage: 7*a + 150115 in α
True
sage: β*α^-1*J
Fractional ideal (5145, 7*a + 910)
sage: # which is a subset of Z_K
sage: β*α^-1
Fractional ideal (119/2*a + 35/2)
sage: J
Fractional ideal (2, a + 1)
sage: (119/2*a + 35/2)*J
Fractional ideal (5145, 7*a + 910)
sage: # so therefore β*α^-1 is a subset of J^-1
sage: J^-1
Fractional ideal (1, 1/2*a + 1/2)
sage: # we can see it consists of all odd halfs of a
sage: # and any integer multiple of 1/2
sage: # which β*α^-1 = <119/2*a + 35/2> is a member of
sage: (a + 7)*O
Fractional ideal (a + 7)
sage: β
434*a - 175
sage: N.<a> = Integers(5)[]
sage: N(a + 7)
a + 2
sage: N(434*a - 175)
4*a
sage: # so they are different
```

$$α ∈ 𝔭 ⇒ ⟨α⟩⊆ 𝔭$$
And there exists 
$$𝔭_1 ⋯ 𝔭_r ⊆ ⟨α⟩$$
but since $r$ is minimal
$$𝔭_2 ⋯ 𝔭_r ⊈ ⟨α⟩$$
Let $β ∈ 𝔭_2 ⋯ 𝔭_r$, then $β ∉ ⟨α⟩$.
$$β𝔭 ⊆ 𝔭_1 ⋯ 𝔭_r \implies β𝔭 ⊆ ⟨α⟩$$
$$α^{-1} β𝔭 ⊆ ℤ_K$$
$$α^{-1} β ∈ 𝔭^{-1}$$
But also $β ∉ ⟨α⟩$
$$⇒ α^{-1} β ∉ ℤ_K$$

## $𝔭$ is maximal $⇒ 𝔭𝔭^{-1} = ℤ_K$ (lemma 5.28)

$𝔭^{-1}$ strictly contains $ℤ_K$, so there is a non-integer element $θ ∈ 𝔭^{-1}$,
and $𝔭θ ⊈ 𝔭$. But $𝔭$ is maximal, so $𝔭𝔭^{-1} = ℤ_K$.

## $𝔞$ is any ideal $⇒ 𝔞𝔞^{-1} = ℤ_K$ (lemma 5.29)

By the prev lemma, max ideals $𝔭𝔭^{-1} = ℤ_K$. So $𝔞$ is not maximal.

### Derive identity

$𝔞𝔭^{-1}$ is an ideal.
$$𝔞 ⊆ 𝔞𝔭^{-1}$$
but $∃θ ∈ 𝔭^{-1} : θ ∉ ℤ_K$ so $𝔞 ⊊ 𝔞𝔭^{-1}$.

Since $𝔞𝔭^{-1}$ is an ideal, and $𝔞$ is the biggest such that
$𝔞𝔞^{-1} = ℤ_K$ then
$$𝔞𝔭^{-1}(𝔞𝔭^{-1}) = ℤ_K$$

### Prove final statement

$$𝔞𝔭^{-1}(𝔞𝔭^{-1}) = ℤ_K$$
$$[𝔭^{-1}(𝔞𝔭^{-1})] · 𝔞 = ℤ_K$$
$$ ⇒ 𝔭^{-1}(𝔞𝔭^{-1}) ⊆ 𝔞^{-1}$$
by the definition of a fractional ideal.
$$ ⇒ 𝔞𝔭^{-1}(𝔞𝔭^{-1}) ⊆ 𝔞𝔞^{-1}$$

## Every ideal $𝔞 ≠ 0$ is a product of prime ideals (lemma 5.31)

Every maximal ideal is prime.

Let $𝔞$ be the biggest ideal not a product of primes.
Then it is contained in $𝔭$ prime and so we can write.
$$   𝔞 𝔭^{-1} =   𝔭_1 ⋯ 𝔭_r $$
$$ ⇒ 𝔞        = 𝔭 𝔭_1 ⋯ 𝔭_r $$

# Norms of Ideals

## $N_{K/ℚ}(⟨α⟩) = |N_{K/ℚ}(α)|$ (lemma 5.35)

### Index calculated from determinant

See Alaca ANT theorem 9.1.2.

Let $G$ be a free Abelian group with $n$ generators $ω_1, …, ω_n$.
$$ G = \{ x_1 ω_1 + ⋯ + x_n ω_n : x_i ∈ ℤ \} $$
Let $H$ be a subgroup of $G$ generated by $n$ elements $η_1, …, η_n$
$$ H = \{ y_1 η_1 + ⋯ + y_n η_n : y_i ∈ ℤ \} $$
Because each $η_i ∈ H ⊆ G$ we have
$$ η_i = c_{i, 1} ω_1 + ⋯ + c_{i, n} ω_n $$
Let $C = (c_{i,j})$ be an $n × n$ matrix. Then
$$ [G : H] = \begin{cases}
    |\det(C)| & \text{ if } \det(C) ≠ 0 \\
    ∞         & \text{ if } \det(C) = 0
\end{cases} $$
where $|\det(C)|$ means absolute value of C's determinant.

### Elements of ideal for $⟨α⟩$

$$ ⟨α⟩ = ℤαω_1 + ⋯ + ℤαω_n $$

\begin{align*}
α ω_1 &= a_{1,1} + ⋯ + a_{n, 1} ω_n \\
α ω_2 &= a_{1,2} + ⋯ + a_{n, 2} ω_n \\
      & ⋯ \\
α ω_n &= a_{1,n} + ⋯ + a_{n, n} ω_n \\
\end{align*}

$$ α
\begin{pmatrix}
ω_1 \\
\vdots \\
ω_n
\end{pmatrix}
=
\begin{pmatrix}
a_{1,1} & \hdots & a_{n,1} \\
        & \hdots &         \\
a_{1,n} & \hdots & a_{n,n} \\
\end{pmatrix}
\begin{pmatrix}
ω_1 \\
\vdots \\
ω_n
\end{pmatrix}
$$
The definition of norm from 3.2, is given as the determinant of
that transform matrix.

# $N(𝔞𝔟) = N(𝔞) N(𝔟)$ (theorem 5.37)

Let $𝔭$ be a non-zero prime ideal of $ℤ_K$.

## $ℤ_K / 𝔭 ≅ 𝔞 / 𝔞𝔭$ (lemma 5.36)

There is no ideal $𝔟$ between $𝔞𝔭 ⊊ 𝔟 ⊊ 𝔞$.
To see this simply multiply through by $𝔞^{-1}$, and note $𝔭$ is maximal.
So either $𝔟 = 𝔞$ or $𝔞𝔭$.

Choose $α ∈ 𝔞$ with $α ∉ 𝔞𝔭$. Then because of above $⟨α, 𝔞𝔭⟩ = 𝔞$.
$$ ϕ : ℤ_K → 𝔞/𝔞𝔭 $$
$$ ϕ(x) = αx + 𝔞𝔭 $$
is surjective. The kernel is $⟨𝔭⟩$ since $α⟨𝔭⟩ = 𝔞𝔭$.

The book has a typo on the last line of the proof.
It should be $ℤ_K / 𝔭 ≅ 𝔞 / 𝔞𝔭$.

## Result

Factorise $𝔟$ into prime ideals and so we just deal with $𝔟 = 𝔭$.

$$ ϕ : ℤ_K/𝔞𝔭  →  ℤ_K/𝔞  $$
$$ ϕ(α + 𝔞𝔭)   = α + 𝔞   $$
is a homomorphism. So
$$ \left| \frac{ ℤ_K/𝔞𝔭 }{ 𝔞/𝔞𝔭 } \right| = \left| \frac{ ℤ_K/𝔞𝔭 }{ ℤ_K/𝔭 } \right| = | ℤ_K/𝔞 | $$
$$ ⇒ N(𝔞𝔟) = |ℤ_K/𝔞𝔭| = |ℤ_K/𝔞|·|ℤ_K/𝔭| = N(𝔞) N(𝔟) $$

# Dimension, Ramification Index and Inertia Degree

$ℤ_K$ is $n = [K:ℚ]$ dimension vector space. See section 3.4.
$$ |ℤ_K / ⟨p⟩| = p^n $$
By CRT $ℤ_K / ⟨p⟩ ≅ ℤ_K / 𝔭_1^{e_1} × ℤ_K / 𝔭_r^{e_r}$.
$$ |ℤ_K/𝔭_i^{e_i}| = N(p_i)^{e_i} = [ℤ_K/𝔭_i : 𝔽_p]^{e_i} = (p^{f_i})^{e_i} $$

$$ n = e_1 f_1 + ⋯ + e_r f_r $$

```python
sage: # See chapter 3.6.1
sage: y = ( (sqrt(2) + sqrt(6))/2 )
sage: minpoly(y)
x^4 - 4*x^2 + 1
sage: K.<a> = NumberField(x^4 - 4*x^2 + 1)
sage: O = K.ring_of_integers()
sage: I = O.ideal(5)
sage: I
Fractional ideal (5)
sage: factor(I)
(Fractional ideal (a^3 - 5*a + 1)) * (Fractional ideal (a^3 - 5*a - 1))
sage: A, B = O.ideal(a^3 - 5*a + 1), O.ideal(a^3 - 5*a - 1)
sage: A*B
Fractional ideal (5)
sage: A.ramification_index(), B.ramification_index()
(1, 1)
sage: I.norm()
625
sage: A.norm(), B.norm()
(25, 25)
sage: A.norm() * B.norm()
625
sage: ( ( y^3 - 5*y + 1 )*( y^3 - 5*y - 1) ).expand()
5
```

# Deconstructing Primes into Ideals (prop 5.42)

## Double Quotienting Ideals Isomorphic to Sum of Ideals

Observe the lattice when we collapse normal subgroups down to 0.

$$ \frac{ ⟨p⟩ }{ ⟨g(X)⟩ } ⊆ \frac{ ℤ[X] }{ ⟨g(X)⟩ } ⇔ ⟨p⟩ ⊆ ℤ[X] $$

$$ ϕ : ℤ[X] / ⟨g(X)⟩ → ℤ[X] / ⟨p, g(X)⟩ $$
$$ ϕ(r + ⟨g(X)⟩) = r + ⟨p, g(X)⟩ $$
$$ \ker ϕ = ⟨p, g(X)⟩ $$

Then observe
$$ ϕ(r + ⟨g(X)⟩) = 0 ⇔ r ∈ ⟨p, g(X)⟩ ⇔ r + ⟨g(X)⟩ ∈ ⟨p, g(X)⟩ $$

By first iso theorem with the homomorphism $ϕ$, we see that
$$ (ℤ[X] / ⟨g(X)⟩) / ⟨p, g(X)⟩ ≌ ℤ[X] / ⟨p, g(X)⟩ $$

Alternatively we can observe that $⟨g(X)⟩ ⊆ ⟨p, g(X)⟩ ⊆ ℤ[X]$, and then
by the third theorem
$$ \frac{ ℤ[X] / ⟨g(X)⟩ }{ ⟨p, g(X)⟩ / ⟨g(X)⟩ } ≌ \frac{ ℤ[X] }{ ⟨p, g(X)⟩ } $$
since $⟨p, g(X)⟩ / ⟨g(X)⟩ = ⟨p, g(X)⟩$.

## Setup

$$ K = ℚ(\sqrt{2}, \sqrt{3}) $$
$$ γ = \frac{ \sqrt{2} + \sqrt{6} }{ 2 } $$
$$ g(X) = X^4 - 4X^2 + 1 $$
$$ p = 5 $$
\begin{align*}
\bar{g}(X) &= X^4 + X^2 + 1 \\
           &= (X^2 + X + 1)(X^2 + 4X + 1)
\end{align*}
$$ g_1(X) = (X^2 + X + 1), g_2(X) = X^2 + 4X + 1 $$
$$ 𝔭_1 = ⟨5, γ^2 + γ + 1⟩, 𝔭_2 = ⟨5, γ^2 + 4γ + 1⟩ $$

## $ℤ_K / 𝔭_1 ≅ 𝔽_p[X] / ⟨\bar{g}_1(X)⟩$ and is a Field

$$ ℤ_K / 𝔭_1 = ℤ[γ] / ⟨5, γ^2 + γ + 1⟩ $$

$$ ϕ : ℤ[γ] → ℤ[X] / ⟨g(X)⟩ $$
$$ ϕ(a_0 + a_1 γ + a_2 γ^2 + a_3 γ^3) = a_0 + a_1 X + a_2 X^2 + a_3 X^3 + ⟨g(X)⟩ $$

$$ \frac{ ℤ[γ] }{ ⟨p, g_1(γ)⟩ } ≅ \frac{ ℤ[X] / ⟨g(X)⟩ }{ ⟨p, g_1(X), g(X)⟩ / ⟨g(X)⟩ } ≅ \frac{ ℤ[X] }{ ⟨p, g_1(X), g(X)⟩ }$$

But also going in reverse with $ψ : ℤ[X] / ⟨p⟩ → 𝔽_p$
$$ \frac{ ℤ[X] }{ ⟨p, g_1(X), g(X)⟩ } ≅ \frac{ ℤ[X] / ⟨p⟩ }{ ⟨p, g_1(X), g(X)⟩ / ⟨p⟩ } ≅ \frac{ 𝔽_p[X] }{ ⟨\bar{g}_1(X), \bar{g}(X)⟩ } $$
Note that $\bar{g}_1(X) | \bar{g}(X)$
$$ ℤ_K / 𝔭_1 ≅ 𝔽_p[X] / ⟨\bar{g}_1(X)⟩ $$

$\bar{g}_1(X)$ is irreducible $⇒ ⟨\bar{g}_1(X)⟩$ is a prime ideal $⇒$ the right hand side is a field,
and so $𝔭_1$ is a prime ideal.

## $ℤ_K / ⟨p⟩ ≅ 𝔽_p[X] / ⟨\bar{g}(X)⟩$

\begin{align*}
ℤ_K / ⟨p⟩   &= ℤ[γ] / ⟨p⟩ \\
            &≅ \frac{ ℤ[X] / ⟨g(X)⟩ }{ ⟨p, g(X)⟩ / ⟨g(X)⟩ } \\
            &= \frac{ ℤ[X] }{ ⟨p, g(X)⟩ } \\
            &≅ \frac{ ℤ[X] / ⟨p⟩ }{ ⟨p, g(X)⟩ / ⟨p⟩ } \\
\end{align*}
But let $r ∈ ⟨p, g(X)⟩ / ⟨p⟩ ⊆ ℤ[X] / ⟨p⟩$, then $r = ap + bg(X) ∈ ⟨p, g(X)⟩ + ⟨p⟩ = ⟨p, g(X)⟩$

\begin{align*}
\frac{ ℤ[X] / ⟨p⟩ }{ ⟨p, g(X)⟩ / ⟨p⟩ }
    &= \frac{ ℤ[X] / ⟨p⟩ }{ ⟨p, g(X)⟩ } \\
    &≅ \frac{ 𝔽_p[X] }{ ⟨\bar{g}(X)⟩ } \\
    &≅ ℤ_K / ⟨p⟩
\end{align*}

## Deconstructing $pℤ_K$

There is a map $ℤ_K → ℤ_K / ⟨p⟩$ with kernel $⟨p⟩$.

Then for each component of the decomposed $ℤ_K / ⟨p⟩$, there is another map
$ℤ_K / ⟨p⟩ → ℤ_K / 𝔭_1 ≅ 𝔽_p[X] / ⟨\bar{g}_1(X)⟩$ by $γ → X \mod ⟨p, g_1(X)⟩$.
So the kernel is $⟨p, g_1(γ)⟩$.
$$ pℤ_K = 𝔭_1^{e_1} ⋯ 𝔭_r^{e_r} $$

