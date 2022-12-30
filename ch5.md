# Lemma 5.24

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
𝖆_1 \not\in 𝖆,
𝖆_2 \not\in 𝖆$
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

# $\mathfrak{a ⊆ b ⇒ b^{-1} ⊆ a^{-1}}$

Let $β ∈ 𝔟^{-1}$
$$β 𝔟 ⊆ ℤ_K$$
but $𝖆 ⊆ 𝔟 ⇒ β 𝖆 ⊆ ℤ_K$ and so
$$β ∈ 𝖆^{-1}$$

# Lemma 5.25

$$𝖆^{-1} = \{ α ∈ K : α 𝖆 ⊆ ℤ_K \}$$
Let $γ ∈ 𝖆$ and $𝔠 = γ 𝖆^{-1}$.
Take $i, i' ∈ 𝔠$, then $i = γ β, i' = γ β'$ with
$β, β' ∈ 𝖆^{-1}$.
$$(β + β') 𝖆 = β 𝖆 + β' 𝖆 ⊆ (ℤ_K + ℤ_K) = ℤ_K$$

Let $i = γ β ∈ 𝔠$ with $γ ∈ 𝖆, β ∈ 𝖆^{-1}$ and $r ∈ ℤ_K$.
We want to show that $ri ∈ 𝔠$.

But note that $r ∈ 𝖆^{-1}$, so $r β ∈ 𝖆^{-1} ⇒ ri = γ (r β) ∈ 𝔠$.

# Lemma 5.26

## $𝖆 ⊆ 𝔟 ⇒ 𝔟^{-1} ⊆ 𝖆^{-1}$

Let $β ∈ 𝔟^{-1}$, then $β 𝔟 ⊆ ℤ_K$.

But $𝖆 ⊆ 𝔟 ⇒ β 𝖆 ⊆ ℤ_K$

So $β ∈ 𝖆^{-1}$.

