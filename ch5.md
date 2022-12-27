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

