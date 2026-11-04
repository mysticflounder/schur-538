---
title: "The sixth Schur number is at least 538"
title-meta: "The sixth Schur number is at least 538"
author: Adam McKenna
date: "November 2026"
monofont: "Menlo"
monofontoptions: "Scale=0.85"
abstract: |
  We give an explicit partition of $\{1,\dots,538\}$ into six sum-free sets.
  This shows $S(6)\ge 538$ and improves the bound $S(6)\ge 537$ of Chen, Zhu
  and Long. It also gives $R_6(3)\ge 540$ for the Ramsey number of the triangle
  in six colours. The partition is checked directly and in Lean 4.
---

# 1. The result

A set $A$ of positive integers is *sum-free* when there are no $x,y\in A$ with
$x+y\in A$; the elements $x$ and $y$ may be equal. The Schur number $S(k)$ is
the largest $n$ such that $\{1,\dots,n\}$ is the union of $k$ sum-free sets.

Fredricksen and Sweet gave $S(6)\ge 536$ [FS00], and Chen, Zhu and Long gave
$S(6)\ge 537$ [CZL26]. The latter is the largest lower bound in the sources that
we read on 3 November 2026.

**Theorem 1.** $S(6)\ge 538$.

*Proof.* Let $W$ be the word of 538 letters in Figure 1, and for
$i=1,\dots,6$ let $C_i$ be the set of positions $n$ such that letter $n$ of $W$
is $i$. These six sets partition $\{1,\dots,538\}$, and their sizes are
$131, 85, 58, 67, 63, 134$. There are $269^2=72361$ pairs $(x,y)$ with
$1\le x\le y$ and $x+y\le 538$. For each pair, the letters at positions $x$, $y$
and $x+y$ are not all the same. So each $C_i$ is sum-free. $\square$

Figure 1. The word $W$. Each row gives the position of its first letter.

```
  1  1214532151 4154552214 1213122344 2151413435 2315124412
 51  2541313532 2515141312 2334213142 5552231312 3452214421
101  5133531314 1552443221 3122432215 1514353321 4121614245
151  3215141545 5121412163 6214121614 5641516161 6266661413
201  1656465161 4166626616 1616266661 6661666666 6666666636
251  6161666666 6666666666 6666666666 6666666663 6666666166
301  6666161666 6662616666 6626661666 6564656131 4166662616
351  1615646541 6121412636 1214121564 5141512354 2416121412
401  3351415151 2234221312 2344255141 3135231512 4412254321
451  3132255524 1312433221 3141515223 5313145221 4421513253
501  4314151244 3221312141 2255451415 12354121
```

Let $R_k(3)$ be the least $N$ such that every colouring of the edges of the
complete graph $K_N$ with $k$ colours has a monochromatic triangle.

**Corollary 2.** $R_6(3)\ge 540$.

*Proof.* We use the classical construction behind $S(k)\le R_k(3)-2$
[FS00, (2)]. Take the vertices $0,1,\dots,538$ of $K_{539}$, and give the edge
$\{a,b\}$ the colour $i$ with $|a-b|\in C_i$. A monochromatic triangle
$a<b<d$ would put $x=b-a$, $y=d-b$ and $x+y=d-a$ in one set $C_i$. This is not
possible, because $C_i$ is sum-free. So this colouring with six colours has no
monochromatic triangle, and neither has its restriction to fewer vertices. So
$R_6(3)>539$. $\square$

# 2. Checks

The following Python program holds the only computation that Theorem 1 needs.
With `W` the word of Figure 1, as one string, it prints
`538 ['1', '2', '3', '4', '5', '6'] []`. The last item is the list of pairs
$(x,y)$ with letters at $x$, $y$ and $x+y$ all the same.

```python
w = " " + W
bad = [(x, y) for x in range(1, 270) for y in range(x, 539 - x)
       if w[x] == w[y] == w[x + y]]
print(len(W), sorted(set(W)), bad)
```

The existence of the partition is also checked in Lean 4, version v4.35.0-rc3.
The Lean file imports Lean core only and states, in the namespace
`SchurWitness538`:

```lean
theorem schur_six_538 :
    ∃ c : Nat → Fin 6, ∀ x y : Nat, 1 ≤ x → 1 ≤ y → x + y ≤ 538 →
      ¬ (c x = c y ∧ c y = c (x + y))
```

For the witness in the file, $c(n)+1$ is letter $n$ of $W$ for
$1\le n\le 538$ (theorem `colouring538_val`). So the sets
$\{n\in\{1,\dots,538\}: c(n)=i\}$, for $i$ in `Fin 6`, are the sets $C_{i+1}$ of
Theorem 1. Lean does not define $S(k)$ or $R_k(3)$: the step from the partition
to $S(6)\ge 538$ is the definition of $S(6)$, and Corollary 2 is not formalized.
The theorem uses the axioms `propext` and `Quot.sound`. The file has no `sorry`
and does not use `native_decide`.

# 3. Data availability

The word and the Lean package are at
<https://github.com/mysticflounder/schur-538>, under the license CC BY 4.0. The
file `schur6-538.word` has the letters of $W$ and one final newline. Its SHA-256 is

`9e149c007b778655afd199685ebcc76260604a44f4c322d8aa9a1d96afb71d20`,

and the SHA-256 of `lean/SchurSix538.lean` is

`ef4fa1757ff30ed191f7eb1af24af288ab0a67726ee52b108355402789a63b81`.

The repository also holds a second such word, `schur6-538-b.word`, which differs
from $W$ in 37 letters. The Lean theorem does not use it.

# Use of AI tools

The word was found by a computer program whose development the author directed.
AI models (Anthropic Claude and OpenAI GPT models) wrote the program. The computer
checks, the Lean formalization and this note were produced with the AI system
Claude (Anthropic; model Claude Opus 5.5) under the direction of the author. A
separate agent of the same model audited the word and the Lean theorem with its
own code. The author has checked the content and takes responsibility for it.

# References

- [CZL26] Z. Chen, L. Zhu, F. Long, A new lower bound for the sixth Schur
  number: $S(6)\ge 537$, preprint, arXiv:2610.31362v1 (2026).
- [FS00] H. Fredricksen, M. M. Sweet, Symmetric sum-free partitions and
  lower bounds for Schur numbers, Electron. J. Combin. 7 (2000), #R32.
  doi:10.37236/1510.
