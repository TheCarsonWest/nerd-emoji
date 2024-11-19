# [[Calc home]]
# [[Calc Rules and theorems]]
The Trapezoidal Rule is a numerical integration technique used to approximate the definite integral of a function.  It's particularly useful when finding the exact integral is difficult or impossible.  Instead of using rectangles to approximate the area under a curve (like in [[Riemann Sums]]), the Trapezoidal Rule uses trapezoids.

## The Idea Behind the Trapezoidal Rule

Imagine the area under a curve divided into several thin vertical strips. Instead of approximating each strip with a rectangle, we approximate it with a trapezoid.  The top of each trapezoid connects two points on the curve, while the bottom is a segment on the x-axis. The area of each trapezoid is easier to calculate than the area under a curve, and the sum of the areas of all trapezoids provides a better approximation of the integral.

## Formula for the Trapezoidal Rule

Let's say we want to approximate $\int_a^b f(x) \, dx$. We divide the interval $[a, b]$ into $n$ subintervals of equal width, $\Delta x = \frac{b-a}{n}$. Let $x_0 = a$, $x_1 = a + \Delta x$, $x_2 = a + 2\Delta x$, ..., $x_n = b$ be the endpoints of these subintervals.  Then the Trapezoidal Rule states:

# $$\int_a^b f(x) \, dx \approx \frac{\Delta x}{2} [f(x_0) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(x_n)]$$

This can be written more compactly as:
# $$\int_a^b f(x) \, dx \approx \frac{\Delta x}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

## Example

Let's approximate $\int_1^3 x^2 \, dx$ using the Trapezoidal Rule with $n=4$ subintervals.

1. **Find $\Delta x$:** $\Delta x = \frac{3 - 1}{4} = 0.5$

2. **Find the $x_i$ values:** $x_0 = 1$, $x_1 = 1.5$, $x_2 = 2$, $x_3 = 2.5$, $x_4 = 3$

3. **Evaluate the function at each $x_i$:**
   $f(x_0) = f(1) = 1^2 = 1$
   $f(x_1) = f(1.5) = 1.5^2 = 2.25$
   $f(x_2) = f(2) = 2^2 = 4$
   $f(x_3) = f(2.5) = 2.5^2 = 6.25$
   $f(x_4) = f(3) = 3^2 = 9$

4. **Apply the Trapezoidal Rule:**

$\int_1^3 x^2 \, dx \approx \frac{0.5}{2} [1 + 2(2.25) + 2(4) + 2(6.25) + 9] = \frac{0.5}{2} [1 + 4.5 + 8 + 12.5 + 9] = 0.25(35) = 8.75$

The exact value of the integral is $\frac{x^3}{3} \Big|_1^3 = \frac{27}{3} - \frac{1}{3} = \frac{26}{3} \approx 8.667$.  The Trapezoidal Rule gives a reasonably close approximation.


## Error Analysis [[Error Bounds]]

The error in the Trapezoidal Rule depends on the second [[derivative]] of the function and the width of the subintervals. A smaller $\Delta x$ (larger $n$) generally leads to a smaller error.  There are formulas to estimate the error bound, but they are beyond the scope of a basic Calculus AB course.

## Comparison with Riemann Sums [[Riemann Sums]]

Both [[Riemann Sums]] and the Trapezoidal Rule approximate definite [[integrals]]. However, the Trapezoidal Rule generally provides a more accurate approximation for the same