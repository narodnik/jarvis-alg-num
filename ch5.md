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

## There are prime ideals $𝔭_1, …, 𝔭_r$ such that $𝔭_1 ⋯ 𝔭_r ⊆ 𝖆$ (lemma 5.24)

$𝖆$ is a non-zero ideal of $ℤ_K$.

$ℤ_K$ is Noetherian.
Since $𝖆$ forms an ascending chain
$𝖆 ⊆ 𝖆_1 ⊆ 𝖆_2 ⊆ ⋯$,
it eventually terminates.

There are no prime ideals $𝔭_1 ⋯ 𝔭_r ⊆ 𝖆$.
The same is true for all ideals in the chain $𝖆_i$.

Lets take $𝖆$ to be the largest ideal in the chain.

$𝖆$ is not prime otherwise $𝔭_1 = 𝖆 ⊆ 𝖆$
and the proof is finished.

So there are ideals $𝖆_1, 𝖆_2$ in $ℤ_K$ such that
$𝖆_1 𝖆_2 ⊆ 𝖆,
𝖆_1 ∉ 𝖆,
𝖆_2 ∉ 𝖆$
Write
$$𝔟_1 = 𝖆 + 𝖆_1,
𝔟_2 = 𝖆 + 𝖆_2$$
Then we can see that
$$𝔟_1 𝔟_2 = (𝖆 + 𝖆_1)(𝖆 + 𝖆_2)
= 𝖆 + 𝖆_1 𝖆 + 𝖆_2 𝖆 + 𝖆_1 𝖆_2$$
Since $𝖆_1 𝖆_2 ⊆ 𝖆$, so
$𝔟_1 𝔟_2 ⊆ 𝖆$.
But also observe that
$$𝖆 ⊊ 𝔟_1, 𝖆 ⊊ 𝔟_2$$

Since $𝔟_1, 𝔟_2$ are bigger than $𝖆$, then by $𝖆$'s maximality,
there exist prime ideals $𝔭_i$ such that
$$𝔭_1 ⋯ 𝔭_s ⊆ 𝔟_1$$
$$𝔭_{s+1} ⋯ 𝔭_t ⊆ 𝔟_2$$
$$⇒ 𝔭_1 ⋯ 𝔭_t ⊆ 𝔟_1 𝔟_2
⊆ 𝖆$$
Which is a contradiction.

## $\mathfrak{a ⊆ b ⇒ b^{-1} ⊆ a^{-1}}$

Let $β ∈ 𝔟^{-1}$
$$β 𝔟 ⊆ ℤ_K$$
but $𝖆 ⊆ 𝔟 ⇒ β 𝖆 ⊆ ℤ_K$ and so
$$β ∈ 𝖆^{-1}$$

## $𝖆^{-1} = \{ α ∈ K : α 𝖆 ⊆ ℤ_K \}$ is a fractional ideal (lemma 5.25)

$$𝖆^{-1} = \{ α ∈ K : α 𝖆 ⊆ ℤ_K \}$$
Let $γ ∈ 𝖆$ and $𝔠 = γ 𝖆^{-1}$.
Take $i, i' ∈ 𝔠$, then $i = γ β, i' = γ β'$ with
$β, β' ∈ 𝖆^{-1}$.
$$(β + β') 𝖆 = β 𝖆 + β' 𝖆 ⊆ (ℤ_K + ℤ_K) = ℤ_K$$

Let $i = γ β ∈ 𝔠$ with $γ ∈ 𝖆, β ∈ 𝖆^{-1}$ and $r ∈ ℤ_K$.
We want to show that $ri ∈ 𝔠$.

But note that $r ∈ 𝖆^{-1}$, so $r β ∈ 𝖆^{-1} ⇒ ri = γ (r β) ∈ 𝔠$.

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

## $𝖆$ is a proper ideal of $ℤ_K ⇒ ℤ_K ⊊ 𝖆^{-1}$ (lemma 5.26)

### $𝖆 ⊆ 𝔟 ⇒ 𝔟^{-1} ⊆ 𝖆^{-1}$

Let $β ∈ 𝔟^{-1}$, then $β 𝔟 ⊆ ℤ_K$.

But $𝖆 ⊆ 𝔟 ⇒ β 𝖆 ⊆ ℤ_K$

So $β ∈ 𝖆^{-1}$.

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

## $𝖆$ is any ideal $⇒ 𝖆𝖆^{-1} = ℤ_K$ (lemma 5.29)

By the prev lemma, max ideals $𝔭𝔭^{-1} = ℤ_K$. So $𝖆$ is not maximal.

### Derive identity

$𝖆𝔭^{-1}$ is an ideal.
$$𝖆 ⊆ 𝖆𝔭^{-1}$$
but $∃θ ∈ 𝔭^{-1} : θ ∉ ℤ_K$ so $𝖆 ⊊ 𝖆𝔭^{-1}$.

Since $𝖆𝔭^{-1}$ is an ideal, and $𝖆$ is the biggest such that
$𝖆𝖆^{-1} = ℤ_K$ then
$$𝖆𝔭^{-1}(𝖆𝔭^{-1}) = ℤ_K$$

### Prove final statement

$$𝖆𝔭^{-1}(𝖆𝔭^{-1}) = ℤ_K$$
$$[𝔭^{-1}(𝖆𝔭^{-1})] · 𝖆 = ℤ_K$$
$$ ⇒ 𝔭^{-1}(𝖆𝔭^{-1}) ⊆ 𝖆^{-1}$$
by the definition of a fractional ideal.
$$ ⇒ 𝖆𝔭^{-1}(𝖆𝔭^{-1}) ⊆ 𝖆𝖆^{-1}$$

## Every ideal $𝖆 ≠ 0$ is a product of prime ideals (lemma 5.31)

Every maximal ideal is prime.

Let $𝖆$ be the biggest ideal not a product of primes.
Then it is contained in $𝔭$ prime and so we can write.
$$   𝖆 𝔭^{-1} =   𝔭_1 ⋯ 𝔭_r $$
$$ ⇒ 𝖆        = 𝔭 𝔭_1 ⋯ 𝔭_r $$

# Norms of Ideals

## $N_{K/ℚ}(⟨α⟩) = |N_{K/ℚ}(α)|$

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

