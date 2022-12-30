---
header-includes: |
    - \newcommand{\mf}{\mathfrak}
    - \newcommand{\sseq}{\subseteq}
    - \newcommand{\bb}{\mathbb}
---

# Lemma 5.24

$\mathfrak{a}$ is a non-zero ideal of $\mathbb{Z}_K$.

$\mathbb{Z}_K$ is Noetherian.
Since $\mathfrak{a}$ forms an ascending chain
$\mathfrak{a} \subseteq \mathfrak{a}_1 \subseteq \mathfrak{a}_2 \subseteq \cdots$,
it eventually terminates.

There are no prime ideals $\mathfrak{p}_1 \cdots \mathfrak{p}_r \subseteq \mathfrak{a}$.
The same is true for all ideals in the chain $\mathfrak{a}_i$.

Lets take $\mathfrak{a}$ to be the largest ideal in the chain.

$\mathfrak{a}$ is not prime otherwise $\mathfrak{p}_1 = \mathfrak{a} \subseteq \mathfrak{a}$
and the proof is finished.

So there are ideals $\mathfrak{a}_1, \mathfrak{a}_2$ in $\mathbb{Z}_K$ such that
$\mathfrak{a}_1 \mathfrak{a}_2 \subseteq \mathfrak{a},
\mathfrak{a}_1 \not\subseteq \mathfrak{a},
\mathfrak{a}_2 \not\subseteq \mathfrak{a}$
Write
$$\mathfrak{b}_1 = \mathfrak{a} + \mathfrak{a}_1,
\mathfrak{b}_2 = \mathfrak{a} + \mathfrak{a}_2$$
Then we can see that
$$\mathfrak{b}_1 \mathfrak{b}_2 = (\mathfrak{a} + \mathfrak{a}_1)(\mathfrak{a} + \mathfrak{a}_2)
= \mathfrak{a} + \mathfrak{a}_1 \mathfrak{a} + \mathfrak{a}_2 \mathfrak{a} + \mathfrak{a}_1 \mathfrak{a}_2$$
Since $\mathfrak{a}_1 \mathfrak{a}_2 \subseteq \mathfrak{a}$, so
$\mathfrak{b}_1 \mathfrak{b}_2 \subseteq \mathfrak{a}$.
But also observe that
$$\mathfrak{a} \subsetneq \mathfrak{b}_1, \mathfrak{a} \subsetneq \mathfrak{b}_2$$

Since $\mathfrak{b}_1, \mathfrak{b}_2$ are bigger than $\mathfrak{a}$, then by $\mathfrak{a}$'s maximality,
there exist prime ideals $\mathfrak{p}_i$ such that
$$\mathfrak{p}_1 \cdots \mathfrak{p}_s \subseteq \mathfrak{b}_1$$
$$\mathfrak{p}_{s+1} \cdots \mathfrak{p}_t \subseteq \mathfrak{b}_2$$
$$\implies \mathfrak{p}_1 \cdots \mathfrak{p}_t \subseteq \mathfrak{b}_1 \mathfrak{b}_2
\subseteq \mathfrak{a}$$
Which is a contradiction.

# $\mathfrak{a \subseteq b \implies b^{-1} \subseteq a^{-1}}$

Let $\beta \in \mathfrak{b}^{-1}$
$$\beta \mathfrak{b} \subseteq \mathbb{Z}_K$$
but $\mathfrak{a \subseteq b} \implies \beta \mathfrak a \subseteq \mathbb Z_K$ and so
$$\beta \in \mathfrak a^{-1}$$

# Lemma 5.25

$$\mathfrak a^{-1} = \{ \alpha \in K : \alpha \mathfrak a \subseteq \mathbb Z_K \}$$
Let $\gamma \in \mathfrak a$ and $\mathfrak c = \gamma \mathfrak a^{-1}$.
Take $i, i' \in \mathfrak c$, then $i = \gamma \beta, i' = \gamma \beta'$ with
$\beta, \beta' \in \mathfrak a^{-1}$.
$$(\beta + \beta') \mathfrak a = \beta \mathfrak a + \beta' \mathfrak a \subseteq (\mathbb Z_K + \mathbb Z_K) = \mathbb Z_K$$

Let $i = \gamma \beta \in \mathfrak c$ with $\gamma \in \mathfrak a, \beta \in \mathfrak a^{-1}$ and $r \in \mathbb Z_K$.
We want to show that $ri \in \mathfrak c$.

But note that $r \in \mathfrak a^{-1}$, so $r \beta \in \mathfrak a^{-1} \implies ri = \gamma (r \beta) \in \mathfrak c$.

# Lemma 5.26

## $\mf a \sseq \mf b \implies \mf b^{-1} \sseq \mf a^{-1}$

Let $\beta \in \mf b^{-1}$, then $\beta \mf b \sseq \bb Z_K$.

But $\mf a \sseq \mf b \implies \beta \mf a \sseq \bb Z_K$

So $\beta \in \mf a^{-1}$.

