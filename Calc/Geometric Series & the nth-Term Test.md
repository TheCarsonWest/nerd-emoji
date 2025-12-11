
# [[Calc Home]]
# AP Calculus BC Notes: 10.2 Geometric Series & the nth-Term Test

This page focuses on two fundamental concepts in the study of infinite series: geometric series, which have a predictable convergence pattern, and the nth-Term Test, a basic test for divergence. These tools are essential for determining the behavior of [[Infinite Sequences and Series]].

---

## 1. Geometric Series

A **geometric series** is a series where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the **common ratio** ($r$).

### 1.1 Definition & General Form
A geometric series can be written in two common forms:
*   Starting at $n=0$: $\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ar^3 + \dots$
*   Starting at $n=1$: $\sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + ar^3 + \dots$

Where:
*   $a$ is the first term (when $n=0$ or $n=1$ in the respective forms).
*   $r$ is the common ratio.

### 1.2 Convergence and Divergence of Geometric Series

The convergence of a geometric series depends entirely on the value of its common ratio $r$.

| Condition for $r$ | Series Behavior | Sum (if it converges) |
| :---------------- | :-------------- | :-------------------- |
| $|r| < 1$         | Converges       | $S = \frac{a}{1-r}$   |
| $|r| \ge 1$        | Diverges        | N/A                   |

**Explanation:**
*   **If $|r| < 1$**: As $n$ increases, $r^n$ approaches $0$. The partial sums approach a finite value, $\frac{a}{1-r}$.
*   **If $|r| = 1$**: The terms do not approach $0$ (they are $\pm a$). The series will either oscillate (e.g., $1-1+1-1+\dots$) or grow indefinitely (e.g., $1+1+1+1+\dots$).
*   **If $|r| > 1$**: The terms $ar^n$ grow in magnitude, so the series cannot converge.

---

## 2. The nth-Term Test for Divergence

The nth-Term Test (also known as the Test for Divergence) is a quick way to *identify* series that diverge. It cannot be used to prove convergence.

### 2.1 Statement of the Test
If $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ **diverges**.

### 2.2 Important Considerations

*   **The Converse is FALSE:** If $\lim_{n \to \infty} a_n = 0$, the test is inconclusive. The series **may converge or may diverge**. You must use other tests (e.g., [[The Integral Test]], Comparison Tests, etc.) to determine its behavior.
    *   **Example of Inconclusive Case:** For the harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$, $\lim_{n \to \infty} \frac{1}{n} = 0$. However, the harmonic series is known to diverge.
    *   **Example of Convergent Case:** For the series $\sum_{n=1}^{\infty} \frac{1}{n^2}$, $\lim_{n \to \infty} \frac{1}{n^2} = 0$. This series converges (it's a p-series with $p=2 > 1$).

*   **What it proves:** The nth-Term Test only proves **divergence**. It never proves convergence.

### 2.3 When to Use It
This test is often the first one to try because it's simple to apply. If the limit of the terms is not zero, you're done – the series diverges. If the limit is zero, you need to use a different test.

---

## 3. Summary of Tests

| Test                    | When to Use                                    | What it Determines                                      |
| :---------------------- | :--------------------------------------------- | :------------------------------------------------------ |
| **Geometric Series**    | When series is in $ar^n$ or $ar^{n-1}$ form   | Converges if $|r|<1$, Diverges if $|r| \ge 1$. If convergent, finds the sum. |
| **nth-Term Test**       | As a preliminary test for any series $\sum a_n$ | If $\lim_{n \to \infty} a_n \neq 0$, then $\sum a_n$ diverges. (Inconclusive if $\lim_{n \to \infty} a_n = 0$) |

These fundamental tests provide the groundwork for analyzing the convergence and divergence of more complex series in AP Calculus BC.