
# [[Calc Home]]
# AP Calculus BC - Topic 10.1: Infinite Sequences and Series

Infinite Sequences and Series form a fundamental part of advanced calculus, providing tools to represent functions and solve problems that cannot be addressed with finite sums. This topic introduces the concepts of ordered lists of numbers (sequences) and the summation of these numbers (series), exploring their convergence and divergence properties.

## I. Infinite Sequences

An **infinite sequence** is an ordered list of numbers, typically denoted as $\{a_n\}_{n=1}^{\infty}$ or simply $a_1, a_2, a_3, \dots, a_n, \dots$. Each term $a_n$ is a function of the index $n$, which is a positive integer.

### A. Convergence and Divergence of Sequences
A sequence $\{a_n\}$ **converges** to a limit $L$ if, as $n$ approaches infinity, the terms of the sequence approach $L$. If no such limit exists, the sequence **diverges**.

Mathematically, a sequence converges to $L$ if:
$$ \lim_{n \to \infty} a_n = L $$
where $L$ is a finite number.

**Key Limit Properties:**
The properties of limits for functions apply directly to sequences. For example, if $\lim_{n \to \infty} a_n = A$ and $\lim_{n \to \infty} b_n = B$:
*   $\lim_{n \to \infty} (a_n \pm b_n) = A \pm B$
*   $\lim_{n \to \infty} (c \cdot a_n) = c \cdot A$
*   $\lim_{n \to \infty} (a_n \cdot b_n) = A \cdot B$
*   $\lim_{n \to \infty} \left( \frac{a_n}{b_n} \right) = \frac{A}{B}$ (provided $B \neq 0$)

**Squeeze Theorem for Sequences:**
If $b_n \le a_n \le c_n$ for all $n$ greater than some integer $N$, and if $\lim_{n \to \infty} b_n = L$ and $\lim_{n \to \infty} c_n = L$, then $\lim_{n \to \infty} a_n = L$.

**Monotonic and Bounded Sequences:**
A sequence is **monotonic** if it is either non-decreasing ($a_n \le a_{n+1}$) or non-increasing ($a_n \ge a_{n+1}$) for all $n$.
A sequence is **bounded** if there exist numbers $M$ and $N$ such that $N \le a_n \le M$ for all $n$.
[[Monotonic Sequence Theorem]]: If a sequence is both monotonic and bounded, then it converges.

## II. Infinite Series

An **infinite series** is the sum of the terms of an infinite sequence. It is denoted as $\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \dots$.

### A. Partial Sums and Convergence
To determine if an infinite series converges, we examine its **partial sums**. The $k$-th partial sum, $S_k$, is the sum of the first $k$ terms:
$$ S_k = \sum_{n=1}^{k} a_n = a_1 + a_2 + \dots + a_k $$
If the sequence of partial sums $\{S_k\}$ converges to a finite limit $S$, then the series $\sum_{n=1}^{\infty} a_n$ converges, and its sum is $S$.
$$ \sum_{n=1}^{\infty} a_n = \lim_{k \to \infty} S_k = S $$
If $\lim_{k \to \infty} S_k$ does not exist or is infinite, the series **diverges**.

### B. Common Types of Series
| Series Type          | Form                                     | Convergence Condition      | Sum (if convergent)       |
| :------------------- | :--------------------------------------- | :------------------------- | :------------------------ |
| [[Geometric Series]] | $\sum_{n=0}^{\infty} ar^n$ or $\sum_{n=1}^{\infty} ar^{n-1}$ | $|r| < 1$                  | $\frac{a}{1-r}$           |
| Telescoping Series   | Terms cancel out                         | $\lim_{k \to \infty} (S_k)$ exists |                           |
| $p$-series           | $\sum_{n=1}^{\infty} \frac{1}{n^p}$    | $p > 1$                    | No general formula       |

### C. The nth-Term Test for Divergence
The [[Geometric Series & the nth-Term Test]] is a crucial preliminary test. If $\lim_{n \to \infty} a_n \neq 0$ or if the limit does not exist, then the series $\sum_{n=1}^{\infty} a_n$ **diverges**.

**Important Note:** If $\lim_{n \to \infty} a_n = 0$, the $n$-th term test is inconclusive. The series *may* converge or diverge (e.g., the harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, even though $\lim_{n \to \infty} \frac{1}{n} = 0$).

### D. Properties of Convergent Series
If $\sum a_n$ and $\sum b_n$ are convergent series, then:
*   $\sum (a_n \pm b_n) = \sum a_n \pm \sum b_n$
*   $\sum c \cdot a_n = c \cdot \sum a_n$ for any constant $c$.
Adding or removing a finite number of terms from a series does not affect its convergence or divergence, though it will change the sum if it converges.