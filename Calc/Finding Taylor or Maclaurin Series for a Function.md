
# [[Calc Home]]
# Topic 10.14: Finding Taylor or Maclaurin Series for a Function

Taylor and Maclaurin series are powerful tools for representing functions as infinite polynomials. This allows us to approximate complex functions, especially for evaluation or integration, using polynomial properties.

## Introduction to Taylor and Maclaurin Series

A **Taylor series** is an infinite polynomial representation of a function $f(x)$ centered at $x=c$. This series uses the function's derivatives evaluated at the center $c$ to construct its terms.

A **Maclaurin series** is a special case of a Taylor series where the series is centered at $x=0$.

These series are a type of [[Power Series]] where the coefficients are determined by the function's derivatives.

## Formulas

### Taylor Series Formula

For a function $f(x)$ that has derivatives of all orders at $x=c$, its Taylor series centered at $x=c$ is given by:

$$
T(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(c)}{n!}(x-c)^n = f(c) + f'(c)(x-c) + \frac{f''(c)}{2!}(x-c)^2 + \frac{f'''(c)}{3!}(x-c)^3 + \dots
$$

### Maclaurin Series Formula

For a function $f(x)$ that has derivatives of all orders at $x=0$, its Maclaurin series is given by setting $c=0$:

$$
M(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots
$$

## Steps to Find a Taylor or Maclaurin Series

1.  **Find Derivatives**: Calculate the first few derivatives of the function $f(x)$. Look for a pattern in the derivatives.
2.  **Evaluate at the Center**: Evaluate each derivative at the center $c$ (or $0$ for a Maclaurin series). This gives you $f(c), f'(c), f''(c), \dots, f^{(n)}(c)$.
3.  **Substitute into Formula**: Substitute these values into the general Taylor or Maclaurin series formula.
4.  **Write General Term (Optional but Recommended)**: Express the series using summation notation if a clear pattern emerges for $f^{(n)}(c)$. This is crucial for determining the [[Radius and Interval of Convergence]].

### Example Walkthrough: Finding the Maclaurin Series for $f(x) = e^x$

Let's find the Maclaurin series for $f(x) = e^x$. Here, $c=0$.

1.  **Find Derivatives**:
    *   $f(x) = e^x$
    *   $f'(x) = e^x$
    *   $f''(x) = e^x$
    *   $f'''(x) = e^x$
    *   In general, $f^{(n)}(x) = e^x$.

2.  **Evaluate at Center ($c=0$)**:
    *   $f(0) = e^0 = 1$
    *   $f'(0) = e^0 = 1$
    *   $f''(0) = e^0 = 1$
    *   $f'''(0) = e^0 = 1$
    *   In general, $f^{(n)}(0) = e^0 = 1$.

3.  **Substitute into Maclaurin Formula**:
    Using $M(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$
    We get:
    $$
    e^x = 1 + 1 \cdot x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + \dots
    $$

4.  **Write General Term**:
    The general term for $f^{(n)}(0)$ is $1$.
    $$
    e^x = \sum_{n=0}^{\infty} \frac{1}{n!}x^n
    $$

## Common Maclaurin Series

It's helpful to memorize or be able to quickly derive some common Maclaurin series:

| Function $f(x)$ | Maclaurin Series $\sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$ |
| :---------------- | :---------------------------------------------------------------- |
| $e^x$             | $\sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ |
| $\sin(x)$         | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots$ |
| $\cos(x)$         | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots$ |
| $\frac{1}{1-x}$   | $\sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \dots$ (Geometric Series) |
| $\ln(1+x)$        | $\sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$ |
| $\arctan(x)$      | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \dots$ |

These series are fundamental for [[Representing Functions as Power Series]] and form the basis for many applications. When approximating functions, understanding the [[Lagrange Error Bound]] is crucial to determine the accuracy of the approximation.