[[Calc home]]

The [[Squeeze Theorem]], also known as the Sandwich Theorem, is a powerful tool in calculus for determining the limit of a function. It states that if two functions "squeeze" a third function between them, and the two outer functions have the same limit at a point, then the middle function must also have the same limit at that point.

### Formal Statement

Let $f(x)$, $g(x)$, and $h(x)$ be functions defined on an open interval containing $a$, except possibly at $a$ itself. If:

1.  $g(x) \leq f(x) \leq h(x)$ for all $x$ in the interval (except possibly at $x=a$)
2.  $\lim_{x \to a} g(x) = L$ and $\lim_{x \to a} h(x) = L$

Then:

$\lim_{x \to a} f(x) = L$

### [Desmos example](https://www.desmos.com/calculator/s7ztp99uvn)


### Example

Let's find the limit of the function $f(x) = x^2 \sin(\frac{1}{x})$ as $x$ approaches 0.

**1. Find bounding functions:**

We know that $-1 \leq \sin(\frac{1}{x}) \leq 1$ for all $x$ (except $x=0$).  Multiplying this inequality by $x^2$, we get:

$-x^2 \leq x^2 \sin(\frac{1}{x}) \leq x^2$

**2. Find the limits of the bounding functions:**

$\lim_{x \to 0} -x^2 = 0$ and $\lim_{x \to 0} x^2 = 0$

**3. Apply the [[Squeeze Theorem]]:**

Since $-x^2 \leq x^2 \sin(\frac{1}{x}) \leq x^2$ and both $-x^2$ and $x^2$ approach 0 as $x$ approaches 0, we can conclude that:

$\lim_{x \to 0} x^2 \sin(\frac{1}{x}) = 0$

### Applications

The [[Squeeze Theorem]] is particularly useful when dealing with functions that are difficult to evaluate directly. It is often used to:

*  Find limits involving trigonometric functions.
*  Prove the limit of a sequence.
*  Determine the convergence of a series.

### Key Points

*  The [[Squeeze Theorem]] only works if the bounding functions have the same limit.
*  The inequality $g(x) \leq f(x) \leq h(x)$ must hold for all values of $x$ in the interval, except possibly at $x=a$.
*  The [[Squeeze Theorem]] can be used to find limits of functions that are otherwise difficult to evaluate.

By understanding the [[Squeeze Theorem]], you gain a valuable tool for solving a variety of calculus problems.
