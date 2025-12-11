
# [[Calc Home]]
# AP Calculus BC: The Integral Test (Infinite Series)

## Introduction to the Integral Test

The Integral Test is a powerful tool used to determine the convergence or divergence of an [[Infinite Sequences and Series]] where the terms are positive and decreasing. It establishes a connection between the behavior of an infinite series and the behavior of an improper integral. It's particularly useful when the terms of a series can be easily related to a continuous, decreasing, and positive function.

## Conditions for the Integral Test

Before applying the Integral Test to a series $\sum_{n=N}^{\infty} a_n$, we must verify that its corresponding function $f(x)$ satisfies three specific conditions for $x \ge N$ (where $N$ is some positive integer). Let $f(x)$ be a function such that $f(n) = a_n$ for all integers $n \ge N$.

| Condition     | Description                                                          |
| :------------ | :------------------------------------------------------------------- |
| **Continuous** | $f(x)$ must be continuous on the interval $[N, \infty)$.             |
| **Positive**  | $f(x)$ must be positive ($f(x) > 0$) for all $x$ in $[N, \infty)$. |
| **Decreasing** | $f(x)$ must be decreasing on the interval $[N, \infty)$.            |

To show that $f(x)$ is decreasing, you can show that $f'(x) < 0$ for $x \ge N$.

## Statement of the Integral Test

If $f$ is continuous, positive, and decreasing for $x \ge N$, and $a_n = f(n)$, then:

1.  If the improper integral $\int_{N}^{\infty} f(x) dx$ converges, then the series $\sum_{n=N}^{\infty} a_n$ also converges.
2.  If the improper integral $\int_{N}^{\infty} f(x) dx$ diverges, then the series $\sum_{n=N}^{\infty} a_n$ also diverges.

It's crucial to understand that the Integral Test *only* tells us whether a series converges or diverges. It does *not* tell us the actual sum of the convergent series. The value of the integral is generally not equal to the sum of the series, although their convergence behaviors are linked.

### Example Application

Consider the p-series $\sum_{n=1}^{\infty} \frac{1}{n^p}$.
Let $f(x) = \frac{1}{x^p} = x^{-p}$. For $p > 0$ and $x \ge 1$:
*   $f(x)$ is continuous on $[1, \infty)$.
*   $f(x)$ is positive on $[1, \infty)$.
*   $f'(x) = -px^{-p-1} = -\frac{p}{x^{p+1}}$. If $p > 0$, then $f'(x) < 0$ for $x \ge 1$, so $f(x)$ is decreasing.

Now, we evaluate the improper integral:
$$ \int_{1}^{\infty} \frac{1}{x^p} dx $$
This integral converges if $p > 1$ and diverges if $0 < p \le 1$.
Therefore, by the Integral Test:
*   The p-series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges if $p > 1$.
*   The p-series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ diverges if $0 < p \le 1$.

This is a very important result often referred to as the [[p-Series Test]].

## Remainder Estimate for the Integral Test

For a convergent series $\sum a_n$ with sum $S$, the remainder $R_n = S - S_n = a_{n+1} + a_{n+2} + \dots$ can be estimated using integrals. This is particularly useful for approximating the sum of a series and bounding the error.

If $f(x)$ is continuous, positive, and decreasing for $x \ge N$, and $\sum_{n=N}^{\infty} a_n$ converges, then:

$$ \int_{n+1}^{\infty} f(x) dx \le R_n \le \int_{n}^{\infty} f(x) dx $$

This inequality means that the remainder $R_n$ is bounded by two improper integrals. This can be used to determine the number of terms needed to ensure that the sum approximation $S_n$ is within a desired error tolerance.

Furthermore, we can improve our approximation of the sum $S$ itself:

$$ S_n + \int_{n+1}^{\infty} f(x) dx \le S \le S_n + \int_{n}^{\infty} f(x) dx $$

This gives a more precise interval within which the true sum $S$ must lie.