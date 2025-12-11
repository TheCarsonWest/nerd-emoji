
# [[Calc Home]]
# AP Calculus BC: Topic 10.12 - Lagrange Error Bound

## 1. Introduction to Lagrange Error Bound

The Lagrange Error Bound, also known as Taylor's Inequality or the Remainder Estimation Theorem, provides a way to quantify the maximum possible error when approximating a function $f(x)$ with its $n$-th degree Taylor polynomial, $P_n(x)$, centered at $x=c$. This is crucial for determining the accuracy of a Taylor approximation. It builds upon the concepts covered in [[Finding Taylor Approximations]] and [[Finding Taylor or Maclaurin Series for a Function]].

## 2. The Remainder Term ($R_n(x)$)

When we approximate a function $f(x)$ with its $n$-th degree Taylor polynomial $P_n(x)$, the difference between the actual function value and the approximation is called the remainder or error term, $R_n(x)$.
$$ R_n(x) = f(x) - P_n(x) $$
Therefore, $f(x) = P_n(x) + R_n(x)$. The Lagrange Error Bound helps us to find an upper bound for the absolute value of this remainder, $|R_n(x)|$.

## 3. The Lagrange Error Bound Formula

The Lagrange Error Bound states that if $P_n(x)$ is the $n$-th degree Taylor polynomial for $f(x)$ centered at $x=c$, then the remainder $R_n(x)$ satisfies:

$$ |R_n(x)| \le \frac{M}{(n+1)!} |x-c|^{n+1} $$

where:
*   $P_n(x)$ is the Taylor polynomial of degree $n$.
*   $x$ is the point at which the approximation is made.
*   $c$ is the center of the Taylor polynomial.
*   $n$ is the degree of the Taylor polynomial.
*   $M$ is an upper bound for the absolute value of the $(n+1)$-th derivative of $f(x)$ on the interval between $c$ and $x$. That is, $M \ge |f^{(n+1)}(z)|$ for all $z$ between $c$ and $x$. Finding this value of $M$ is often the most challenging part of applying the theorem.

## 4. How to Find $M$ (The Upper Bound for the $(n+1)$-th Derivative)

To find $M$, you need to:
1.  Calculate the $(n+1)$-th derivative of $f(x)$, denoted as $f^{(n+1)}(x)$.
2.  Identify the interval between the center $c$ and the point $x$ where you are approximating. Let this interval be $I$.
3.  Find the maximum absolute value of $f^{(n+1)}(z)$ for all $z$ in the interval $I$. This maximum value will be your $M$.
    *   **Strategies for finding $M$**:
        *   If $|f^{(n+1)}(x)|$ is a decreasing function on $I$, then $M = |f^{(n+1)}(c)|$.
        *   If $|f^{(n+1)}(x)|$ is an increasing function on $I$, then $M = |f^{(n+1)}(x)|$.
        *   If $|f^{(n+1)}(x)|$ has a critical point within $I$ or is not monotonic, you may need to evaluate it at the endpoints of the interval and at any critical points within the interval to find its maximum absolute value.
        *   For functions like $\sin(x)$ or $\cos(x)$, their derivatives are always bounded by 1, so $M=1$ is often used regardless of the interval. Similarly, for $e^x$, $M$ depends on the interval.

## 5. Applications of Lagrange Error Bound

The Lagrange Error Bound is used for:
*   **Bounding the error**: Providing a guarantee that the error in an approximation will not exceed a certain value.
*   **Determining the degree of the polynomial**: Finding the minimum degree $n$ required for a Taylor polynomial to approximate a function within a specified tolerance at a given point.
*   [[Convergence of Taylor Series]]: It helps demonstrate that if $\lim_{n \to \infty} R_n(x) = 0$, then the Taylor series converges to the function $f(x)$. This is fundamental for understanding the [[Radius and Interval of Convergence]].

## 6. Example Table: Common Taylor Series and their Derivatives

| Function $f(x)$ | $f^{(n)}(x)$ | $f^{(n+1)}(x)$ | Max Value $|f^{(n+1)}(z)|$ (for specific interval) |
| :---------------- | :------------- | :--------------- | :---------------------------------------------------- |
| $e^x$             | $e^x$          | $e^x$            | $e^b$ (if interval is $[c, b]$ and $c < b$)           |
| $\sin(x)$         | $\sin(x \pm n\pi/2)$ | $\sin(x \pm (n+1)\pi/2)$ | $1$ (since $|\sin(z)| \le 1$ for all $z$)          |
| $\cos(x)$         | $\cos(x \pm n\pi/2)$ | $\cos(x \pm (n+1)\pi/2)$ | $1$ (since $|\cos(z)| \le 1$ for all $z$)          |

This table highlights how the $(n+1)$-th derivative behaves, which is crucial for determining $M$.