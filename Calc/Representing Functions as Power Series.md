
# [[Calc Home]]
# AP Calculus BC Notes: Representing Functions as Power Series

## Introduction

Representing a function as a power series allows us to express complex functions as an infinite sum of simpler polynomial terms. This is incredibly useful for approximating functions, solving differential equations, and evaluating integrals that might otherwise be intractable. A power series centered at $x=c$ is an expression of the form:

$$
\sum_{n=0}^{\infty} a_n (x-c)^n = a_0 + a_1(x-c) + a_2(x-c)^2 + \dots
$$

When a function $f(x)$ can be represented by a power series, we say that the series **converges** to $f(x)$ on its [[Radius and Interval of Convergence]].

## Key Techniques for Representation

The primary goal is to manipulate known series or use calculus operations to derive a power series for a given function.

### 1. Using the Geometric Series Formula

The most fundamental power series representation comes from the sum of a [[Geometric Series & the nth-Term Test]].
For $|r| < 1$, the sum of a geometric series is:
$$
\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}
$$
By setting $r = u$, we have the basic power series for $\frac{1}{1-x}$ centered at $x=0$:
$$
\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \dots, \quad \text{for } |x|<1
$$

This series can be manipulated to represent a variety of rational functions.

**Examples:**
*   **For $\frac{1}{1+x}$**: Substitute $x$ with $-x$ into the base series.
    $$
    \frac{1}{1+x} = \frac{1}{1-(-x)} = \sum_{n=0}^{\infty} (-x)^n = \sum_{n=0}^{\infty} (-1)^n x^n = 1 - x + x^2 - x^3 + \dots, \quad \text{for } |-x|<1 \implies |x|<1
    $$
*   **For $\frac{1}{1-3x^2}$**: Substitute $x$ with $3x^2$.
    $$
    \frac{1}{1-3x^2} = \sum_{n=0}^{\infty} (3x^2)^n = \sum_{n=0}^{\infty} 3^n x^{2n} = 1 + 3x^2 + 9x^4 + 27x^6 + \dots, \quad \text{for } |3x^2|<1 \implies |x| < \frac{1}{\sqrt{3}}
    $$

### 2. Differentiation of Power Series

If $f(x) = \sum_{n=0}^{\infty} a_n (x-c)^n$ for $|x-c| < R$, then $f'(x)$ can be found by differentiating the series term-by-term. The radius of convergence $R$ remains the same.

$$
f'(x) = \frac{d}{dx} \left( \sum_{n=0}^{\infty} a_n (x-c)^n \right) = \sum_{n=1}^{\infty} n a_n (x-c)^{n-1}
$$

**Example:** To find a power series for $\frac{1}{(1-x)^2}$:
We know $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$. Differentiating both sides with respect to $x$:
$$
\frac{d}{dx} \left( \frac{1}{1-x} \right) = \frac{d}{dx} \left( \sum_{n=0}^{\infty} x^n \right)
$$
$$
\frac{1}{(1-x)^2} = \sum_{n=1}^{\infty} n x^{n-1} = 1 + 2x + 3x^2 + 4x^3 + \dots, \quad \text{for } |x|<1
$$

### 3. Integration of Power Series

If $f(x) = \sum_{n=0}^{\infty} a_n (x-c)^n$ for $|x-c| < R$, then $\int f(x) dx$ can be found by integrating the series term-by-term. The radius of convergence $R$ remains the same.

$$
\int f(x) dx = \int \left( \sum_{n=0}^{\infty} a_n (x-c)^n \right) dx = C + \sum_{n=0}^{\infty} \frac{a_n}{n+1} (x-c)^{n+1}
$$
The constant of integration $C$ can be found by evaluating $f(c)$ or a known value of the integrated function.

**Example:** To find a power series for $\ln(1-x)$:
We know $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$.
Since $\int \frac{1}{1-x} dx = -\ln(1-x)$, we integrate the series:
$$
-\ln(1-x) = C + \sum_{n=0}^{\infty} \frac{x^{n+1}}{n+1} = C + x + \frac{x^2}{2} + \frac{x^3}{3} + \dots
$$
To find $C$, let $x=0$: $-\ln(1-0) = C + 0 \implies 0 = C$.
So, $\ln(1-x) = -\sum_{n=0}^{\infty} \frac{x^{n+1}}{n+1} = -x - \frac{x^2}{2} - \frac{x^3}{3} - \dots, \quad \text{for } |x|<1$.

## Common Power Series Representations

Knowing these common series is crucial for manipulating and deriving new representations. These are essentially [[Finding Taylor or Maclaurin Series for a Function]] centered at $c=0$.

| Function $f(x)$ | Power Series Representation (Maclaurin Series) | Interval of Convergence |
| :---------------- | :--------------------------------------------- | :---------------------- |
| $\frac{1}{1-x}$   | $\sum_{n=0}^{\infty} x^n$                      | $(-1, 1)$               |
| $e^x$             | $\sum_{n=0}^{\infty} \frac{x^n}{n!}$           | $(-\infty, \infty)$     |
| $\sin x$          | $\sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}$ | $(-\infty, \infty)$     |
| $\cos x$          | $\sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}$     | $(-\infty, \infty)$     |
| $\arctan x$       | $\sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{2n+1}$ | $[-1, 1]$               |
| $\ln(1+x)$        | $\sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n}$ | $(-1, 1]$               |

## Strategies for Deriving Series

1.  **Algebraic Manipulation**: Transform the given function into a form resembling $\frac{a}{1-r}$ or any of the common series. This often involves factoring, polynomial long division, or partial fraction decomposition.
2.  **Substitution**: Replace $x$ with $kx$, $x^m$, or $ax+b$ in a known series.
3.  **Differentiation/Integration**: If the function is the derivative or integral of a known series, apply term-by-term calculus.
4.  **Multiplication/Division**: Multiply or divide known power series (though division is generally more complex).

## Further Considerations

*   **[[Radius and Interval of Convergence]]**: Always determine the interval for which the power series representation is valid. This is crucial for understanding where the series accurately represents the function.
*   **[[Finding Taylor or Maclaurin Series for a Function]]**: While the techniques above are for manipulating known series, the most general method for finding a power series (Taylor series) directly from a function's derivatives is given by Taylor's Formula.
*   **Applications**: Power series are fundamental in approximating definite integrals, solving differential equations, and in [[Finding Taylor Approximations]].