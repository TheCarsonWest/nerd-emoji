
# [[Calc Home]]
# AP Calculus BC Topic 10.13: Radius and Interval of Convergence

## 1. Introduction to Power Series and Convergence

A **power series** is a series of the form
$$
\sum_{n=0}^{\infty} c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \dots
$$
where $x$ is a variable, $c_n$ are constants (the coefficients of the series), and $a$ is a constant (the center of the series). For a specific value of $x$, a power series is a series of constants, which may or may not converge.

The primary goal when working with power series is to determine for which values of $x$ the series converges. The set of all $x$ values for which a power series converges is called its [[Interval of Convergence]].

## 2. Radius of Convergence ($R$)

The **Radius of Convergence**, denoted by $R$, is a non-negative number that describes the "half-width" of the interval where the power series converges. It tells us how far away from the center $a$ the series is guaranteed to converge.

There are three possibilities for $R$:
1.  **$R=0$**: The series converges only at its center, $x=a$.
2.  **$R=\infty$**: The series converges for all real numbers, $x \in (-\infty, \infty)$.
3.  **$0 < R < \infty$**: The series converges for $x$ values within a finite distance $R$ from the center $a$. That is, for $|x-a| < R$.

### Finding the Radius of Convergence

The most common and effective method for finding $R$ is the [[Ratio Test (infinite series)]].

For a power series $\sum_{n=0}^{\infty} c_n (x-a)^n$, apply the Ratio Test:
$$
L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{c_{n+1}(x-a)^{n+1}}{c_n(x-a)^n} \right|
$$
$$
L = \lim_{n \to \infty} \left| \frac{c_{n+1}}{c_n} (x-a) \right| = |x-a| \lim_{n \to \infty} \left| \frac{c_{n+1}}{c_n} \right|
$$
For convergence, we require $L < 1$.
$$
|x-a| \lim_{n \to \infty} \left| \frac{c_{n+1}}{c_n} \right| < 1
$$
Let $K = \lim_{n \to \infty} \left| \frac{c_{n+1}}{c_n} \right|$.
Then, $|x-a| K < 1$.

*   If $K=0$, then $0 < 1$, which is always true. This means the series converges for all $x$, so $R=\infty$.
*   If $K=\infty$, then $|x-a| \infty < 1$ is never true (unless $x=a$), so $R=0$.
*   If $0 < K < \infty$, then $|x-a| < \frac{1}{K}$. In this case, the Radius of Convergence is $R = \frac{1}{K}$.

## 3. Interval of Convergence ($I$)

The **Interval of Convergence**, $I$, is the set of all $x$-values for which a power series converges. It is centered at $a$ and its "length" is $2R$.

### Finding the Interval of Convergence

1.  **Find the Radius of Convergence ($R$)** using the Ratio Test.
2.  **Determine the open interval**:
    *   If $R=0$, the interval is $[a, a]$ (just the point $a$).
    *   If $R=\infty$, the interval is $(-\infty, \infty)$.
    *   If $0 < R < \infty$, the initial open interval of convergence is $(a-R, a+R)$. This is derived from $|x-a| < R$, which means $-R < x-a < R$, so $a-R < x < a+R$.
3.  **Test the endpoints**: For $0 < R < \infty$, the Ratio Test is inconclusive at the endpoints $x = a-R$ and $x = a+R$ (because $L=1$). You **must** substitute these values back into the original power series and determine whether the resulting constant series converges or diverges using other series tests ([[Geometric Series & the nth-Term Test]], [[The Integral Test]], Comparison Tests, Alternating Series Test, etc.).

### Possible Forms of the Interval of Convergence

Depending on whether the series converges at one, both, or neither of the endpoints, the interval of convergence can take one of four forms (when $0 < R < \infty$):

| Form             | Description                                     |
| :--------------- | :---------------------------------------------- |
| $(a-R, a+R)$     | Diverges at both endpoints                      |
| $[a-R, a+R)$     | Converges at $a-R$, diverges at $a+R$           |
| $(a-R, a+R]$     | Diverges at $a-R$, converges at $a+R$           |
| $[a-R, a+R]$     | Converges at both endpoints                     |

### Example

Consider the series $\sum_{n=1}^{\infty} \frac{(x-3)^n}{n}$.
1.  **Radius of Convergence**: Use the Ratio Test.
    $$
    L = \lim_{n \to \infty} \left| \frac{\frac{(x-3)^{n+1}}{n+1}}{\frac{(x-3)^n}{n}} \right| = \lim_{n \to \infty} \left| \frac{(x-3)^{n+1}}{n+1} \cdot \frac{n}{(x-3)^n} \right|
    $$
    $$
    L = \lim_{n \to \infty} \left| (x-3) \frac{n}{n+1} \right| = |x-3| \lim_{n \to \infty} \frac{n}{n+1} = |x-3| \cdot 1 = |x-3|
    $$
    For convergence, $|x-3| < 1$. So, $R=1$.
2.  **Open Interval**: $a=3$, $R=1$. The open interval is $(3-1, 3+1) = (2, 4)$.
3.  **Test Endpoints**:
    *   **At $x=2$**: $\sum_{n=1}^{\infty} \frac{(2-3)^n}{n} = \sum_{n=1}^{\infty} \frac{(-1)^n}{n}$. This is the [[Alternating Series Test|alternating harmonic series]], which converges by the Alternating Series Test.
    *   **At $x=4$**: $\sum_{n=1}^{\infty} \frac{(4-3)^n}{n} = \sum_{n=1}^{\infty} \frac{1^n}{n} = \sum_{n=1}^{\infty} \frac{1}{n}$. This is the [[p-Series|harmonic series]] ($p=1$), which diverges.

Therefore, the Interval of Convergence is $[2, 4)$.