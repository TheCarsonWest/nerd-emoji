# [[Calc home]]
# Average Value of a Function (Calculus AB)

This rundown covers the average value of a function over an interval, a key concept in integral calculus.

## Definition

The average value of a function $f(x)$ on the interval $[a, b]$ is given by:

$$
f_{avg} = \frac{1}{b-a} \int_a^b f(x) \, dx
$$

**Explanation:**

*   $f_{avg}$ represents the average y-value of the function $f(x)$ over the interval $[a, b]$.
*   $\int_a^b f(x) \, dx$ represents the definite integral of $f(x)$ from $a$ to $b$, which geometrically represents the area under the curve of $f(x)$ between $x = a$ and $x = b$.
*   $b - a$ represents the length of the interval.

Essentially, we are dividing the area under the curve by the length of the interval to find the average height (y-value) of the function.

## Intuition

Imagine a rectangle with width $(b - a)$ whose area is equal to the area under the curve of $f(x)$ from $a$ to $b$.  The height of this rectangle is the average value of the function, $f_{avg}$.

## Formula Derivation

The average value formula comes from the Mean Value Theorem for Integrals. [[Mean Value Theorem]]

The Mean Value Theorem for Integrals states that if $f(x)$ is continuous on $[a, b]$, then there exists a value $c$ in $[a, b]$ such that:

$$
\int_a^b f(x) \, dx = f(c)(b - a)
$$

Where $f(c)$ is the value of the function at some point $c$ in the interval.

To find the average value, we are essentially finding the constant value of the function, lets call it $f_{avg}$, that would give the same area under the curve as the original function over the interval $[a, b]$.

So,

$$
\int_a^b f(x) \, dx = f_{avg}(b - a)
$$

Solving for $f_{avg}$, we get:

$$
f_{avg} = \frac{1}{b-a} \int_a^b f(x) \, dx
$$

## Steps to Calculate the Average Value

1.  **Identify the function:** Determine the function $f(x)$ whose average value you need to find.
2.  **Identify the interval:** Determine the interval $[a, b]$ over which you want to find the average value.
3.  **Compute the definite integral:** Evaluate the definite integral $\int_a^b f(x) \, dx$.  This might involve using integration techniques like u-substitution.
4.  **Apply the formula:** Plug the result of the integral and the interval endpoints into the average value formula: $f_{avg} = \frac{1}{b-a} \int_a^b f(x) \, dx$.
5.  **Simplify:** Simplify the expression to find the average value $f_{avg}$.

## Examples

**Example 1:**

Find the average value of $f(x) = x^2$ on the interval $[0, 2]$.

1.  **Function:** $f(x) = x^2$
2.  **Interval:** $[0, 2]$
3.  **Definite Integral:**
    $$
    \int_0^2 x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{2^3}{3} - \frac{0^3}{3} = \frac{8}{3}
    $$
4.  **Average Value:**
    $$
    f_{avg} = \frac{1}{2-0} \int_0^2 x^2 \, dx = \frac{1}{2} \cdot \frac{8}{3} = \frac{4}{3}
    $$

Therefore, the average value of $f(x) = x^2$ on the interval $[0, 2]$ is $\frac{4}{3}$.

**Example 2:**

Find the average value of $f(x) = \sin(x)$ on the interval $[0, \pi]$.

1.  **Function:** $f(x) = \sin(x)$
2.  **Interval:** $[0, \pi]$
3.  **Definite Integral:**
    $$
    \int_0^\pi \sin(x) \, dx = \left[ -\cos(x) \right]_0^\pi = -\cos(\pi) - (-\cos(0)) = -(-1) - (-1) = 1 + 1 = 2
    $$
4.  **Average Value:**
    $$
    f_{avg} = \frac{1}{\pi - 0} \int_0^\pi \sin(x) \, dx = \frac{1}{\pi} \cdot 2 = \frac{2}{\pi}
    $$

Therefore, the average value of $f(x) = \sin(x)$ on the interval $[0, \pi]$ is $\frac{2}{\pi}$.

## Common Mistakes

*   **Forgetting the $\frac{1}{b-a}$ factor:** This is a very common mistake.  Make sure to divide the definite integral by the length of the interval.
*   **Incorrectly evaluating the definite integral:** Pay close attention to the limits of integration and the antiderivative.
*   **Mixing up the average value with the average rate of change:** The average value is about the y-values of the function, while the average rate of change is about the slope of the function. [[Average Rate of Change vs Average Value]]

## Applications

The average value of a function has applications in various fields:

*   **Physics:** Finding the average velocity, average acceleration, etc.
*   **Engineering:** Calculating the average power consumption, average temperature, etc.
*   **Economics:** Determining the average cost, average revenue, etc.

## [[Important Integration Techniques]]

Remember to review your integration techniques, especially u-substitution, as they will be necessary to evaluate the definite integrals required for calculating the average value of a function.
