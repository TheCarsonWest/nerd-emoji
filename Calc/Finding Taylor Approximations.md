
# [[Calc Home]]
## AP Calculus BC: Topic 10.11 - Finding Taylor Approximations

### Introduction to Taylor Polynomials

Taylor polynomials provide a way to approximate a function $f(x)$ with a polynomial, especially useful when the function itself is difficult to work with directly. These approximations are built around a specific point, called the "center" or "point of tangency," and they become more accurate as more terms are included in the polynomial. Essentially, a Taylor polynomial matches the function's value and its derivatives up to a certain order at the center point.

### Definition of a Taylor Polynomial

A Taylor polynomial of order $n$ for a function $f(x)$ centered at $x=c$ is given by:

$$P_n(x) = f(c) + f'(c)(x-c) + \frac{f''(c)}{2!}(x-c)^2 + \frac{f'''(c)}{3!}(x-c)^3 + \dots + \frac{f^{(n)}(c)}{n!}(x-c)^n$$

This can be written in summation notation as:

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k$$

Where:
*   $f^{(k)}(c)$ is the $k$-th derivative of $f(x)$ evaluated at $x=c$.
*   $k!$ is the factorial of $k$.
*   $(x-c)^k$ is the power term.

The higher the order $n$, the better the approximation of $f(x)$ around $x=c$.

### Maclaurin Polynomials

A special case of a Taylor polynomial is a [[Maclaurin Polynomial]], which is simply a Taylor polynomial centered at $x=0$.
Setting $c=0$ in the general formula yields:

$$P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots + \frac{f^{(n)}(0)}{n!}x^n$$

Or in summation notation:

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!}x^k$$

### Steps to Find a Taylor Approximation

To find a Taylor polynomial of order $n$ for a function $f(x)$ centered at $x=c$:

1.  **Calculate Derivatives**: Find the first $n$ derivatives of $f(x)$.
2.  **Evaluate at the Center**: Evaluate $f(c), f'(c), f''(c), \dots, f^{(n)}(c)$.
3.  **Construct the Polynomial**: Substitute these values into the Taylor polynomial formula.

**Example**: Find the 3rd-order Taylor polynomial for $f(x) = \ln(x)$ centered at $x=1$.

| $k$ | $f^{(k)}(x)$           | $f^{(k)}(1)$ | $f^{(k)}(1)/k!$ | Term Formula ($P_3(x)$)                                        |
| :-- | :--------------------- | :----------- | :-------------- | :-------------------------------------------------------------- |
| 0   | $f(x) = \ln(x)$        | $\ln(1) = 0$ | $0/0! = 0$      | $0$                                                             |
| 1   | $f'(x) = 1/x = x^{-1}$ | $1/1 = 1$    | $1/1! = 1$      | $1(x-1)^1 = x-1$                                                |
| 2   | $f''(x) = -x^{-2}$     | $-1/1^2 = -1$ | $-1/2! = -1/2$  | $\frac{-1}{2}(x-1)^2$                                           |
| 3   | $f'''(x) = 2x^{-3}$    | $2/1^3 = 2$  | $2/3! = 2/6 = 1/3$ | $\frac{1}{3}(x-1)^3$                                            |

So, the 3rd-order Taylor polynomial for $\ln(x)$ centered at $x=1$ is:
$$P_3(x) = 0 + (x-1) - \frac{1}{2}(x-1)^2 + \frac{1}{3}(x-1)^3$$
$$P_3(x) = (x-1) - \frac{1}{2}(x-1)^2 + \frac{1}{3}(x-1)^3$$

### Approximating Function Values

Once a Taylor polynomial $P_n(x)$ is found, it can be used to approximate values of $f(x)$ near the center $c$. The closer $x$ is to $c$, generally the more accurate the approximation. For instance, to approximate $\ln(1.1)$ using $P_3(x)$ from the example above, we would plug in $x=1.1$:

$$P_3(1.1) = (1.1-1) - \frac{1}{2}(1.1-1)^2 + \frac{1}{3}(1.1-1)^3$$
$$P_3(1.1) = (0.1) - \frac{1}{2}(0.1)^2 + \frac{1}{3}(0.1)^3$$
$$P_3(1.1) = 0.1 - \frac{0.01}{2} + \frac{0.001}{3}$$
$$P_3(1.1) = 0.1 - 0.005 + 0.000333\dots \approx 0.095333$$
(The actual value of $\ln(1.1) \approx 0.095310$)

### Taylor Series vs. Taylor Polynomials

A [[Taylor Series]] is an infinite-order Taylor polynomial. It represents a function exactly within its [[Radius and Interval of Convergence]]. A Taylor polynomial is a finite truncation of the Taylor series.

### Error in Taylor Approximations

Since Taylor polynomials are approximations, there will always be an error. The error, $R_n(x) = f(x) - P_n(x)$, can be estimated using the [[Lagrange Error Bound]], which gives an upper bound on the absolute value of the error. This is crucial for determining the accuracy of the approximation.