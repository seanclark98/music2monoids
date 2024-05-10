
$\rm Definition\ 1.\>$
Define $H_l$ to be the set of all tertian $l$-note chords.

$\rm Definition\ 2.\>$
We define transformations $T_{i,j}^m : H_l \rightarrow H_l$ by
$$
(n_k)T_{i,j}^m = \begin{cases}
      (n + m)_j & k = i \\
      (n - m)_i & k = j\\
      n_k & k \neq i,j
   \end{cases}
$$
where $n_k$ is the $l$-note chord of type $k$ with root $n$.

$\rm Definition\ 3.\>$
Given $T_{i,j}^m : H_l \rightarrow H_l$.
Define $\mathcal{G}_l = \{T_{i,j}^m : (n_k, (n_k)T_{i,j}^m) \in \mathcal{P}_{1,0}$ or $(n_k)T_{i,j}^m = n_k\text{ for all }k\}$.

$\rm Definition\ 4.\>$
Define $\phi_t : S_t \rightarrow Aut(\mathbb{Z}_{12}^{t-1})$ by

$$(\bm{v})((\sigma)\phi_t) = \bm{w}$$

where $\sigma \in S_t, \bm{v} = (v_1,...,v_{t-1}), \bm{w} = (w_1,...,w_{t-1})$ and
$$
w_i = \begin{cases}
      v_{(i)\sigma^{-1}} & 1 \leq (i)\sigma^{-1} \leq t-1 \\
      - \sum\limits_{i=1}^{t-1} v_i & (i)\sigma^{-1} = t
   \end{cases}
$$

$\rm Theorem\ 1.\>$
Let $G_l$ be the group generated by $\mathcal{G}_l$ and $t(l)$ be the number of types of $l$-note chords.
Then $G_l \cong \mathbb{Z}_{12}^{t(l)-1} \rtimes_{\phi_{t(l)}}  S_{t(l)}$ for $l \in \{2,3,4,5,6,8,9,10\}$ and $G_l \cong \mathbb{Z}_{12} \wr S_{t(l)}$ for $l = 7$ and $l = 11$.