# [[Calc home]]
# Area Between Two Curves - AP Calculus AB Rundown

## Introduction

Finding the area between two curves is a common application of definite integrals in AP Calculus AB. The core idea is to integrate the difference between the two functions over a specified interval. This rundown will cover the essential concepts, formulas, and techniques you need to master this topic.

## The Fundamental Idea

The area between two curves, $f(x)$ and $g(x)$, over an interval $[a, b]$ is found by integrating the absolute difference between the functions.  It is important to find which function is on top to ensure that the result is positive.

## Formula

The area, $A$, between the curves $f(x)$ and $g(x)$ from $x = a$ to $x = b$ is given by:

$$
A = \int_{a}^{b} |f(x) - g(x)| \, dx
$$

Where $f(x)$ and $g(x)$ are continuous functions on the interval $[a, b]$.  If $f(x) \geq g(x)$ on $[a, b]$, then the formula simplifies to:

$$
A = \int_{a}^{b} [f(x) - g(x)] \, dx
$$

**Key Point:** $f(x)$ is the "top" function and $g(x)$ is the "bottom" function within the interval $[a, b]$.

## Steps to Calculate Area Between Curves

1.  **Identify the Functions:** Determine the equations of the two curves, $f(x)$ and $g(x)$.
2.  **Find the Intersection Points:** Determine the interval of integration $[a, b]$ by finding the $x$-coordinates of the points where the two curves intersect. This is done by setting $f(x) = g(x)$ and solving for $x$. These solutions are your limits of integration, $a$ and $b$.  [[Finding Intersection Points]]
3.  **Determine Which Function is on Top:** Determine which function has a greater value within the interval $[a, b]$.  Choose a test value $c$ such that $a < c < b$.  Evaluate $f(c)$ and $g(c)$.  The larger value is the "top" function.  [[Determining the Top Function]]
4.  **Set up the Integral:** Set up the definite integral with the appropriate limits of integration and the difference between the top and bottom functions.
5.  **Evaluate the Integral:** Evaluate the definite integral to find the area.  This might require u-substitution or other integration techniques.

## Examples

### Example 1

Find the area between the curves $f(x) = x^2$ and $g(x) = x$ from $x = 0$ to $x = 1$.

1.  **Functions:**  $f(x) = x^2$ and $g(x) = x$
2.  **Interval:** $[0, 1]$ (Given)
3.  **Top Function:** On the interval $[0, 1]$, $g(x) = x$ is greater than $f(x) = x^2$. For example, at $x = 0.5$, $f(0.5) = 0.25$ and $g(0.5) = 0.5$.
4.  **Integral:**
    $$
    A = \int_{0}^{1} (x - x^2) \, dx
    $$
5.  **Evaluation:**
    $$
    A = \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_{0}^{1} = \left( \frac{1}{2} - \frac{1}{3} \right) - \left( 0 - 0 \right) = \frac{1}{6}
    $$

Therefore, the area between the curves is $\frac{1}{6}$.

### Example 2

Find the area between the curves $f(x) = x^2 - 4$ and $g(x) = x - 2$.

1.  **Functions:** $f(x) = x^2 - 4$ and $g(x) = x - 2$
2.  **Intersection Points:**
    $$
    x^2 - 4 = x - 2 \\
    x^2 - x - 2 = 0 \\
    (x - 2)(x + 1) = 0 \\
    x = 2, x = -1
    $$
    Interval: $[-1, 2]$
3.  **Top Function:** On the interval $[-1, 2]$, $g(x) = x - 2$ is greater than $f(x) = x^2 - 4$. For example, at $x = 0$, $f(0) = -4$ and $g(0) = -2$.
4.  **Integral:**
    $$
    A = \int_{-1}^{2} [(x - 2) - (x^2 - 4)] \, dx = \int_{-1}^{2} (-x^2 + x + 2) \, dx
    $$
5.  **Evaluation:**
    $$
    A = \left[ -\frac{x^3}{3} + \frac{x^2}{2} + 2x \right]_{-1}^{2} = \left( -\frac{8}{3} + \frac{4}{2} + 4 \right) - \left( \frac{1}{3} + \frac{1}{2} - 2 \right) = -\frac{8}{3} + 2 + 4 - \frac{1}{3} - \frac{1}{2} + 2 = 8 - 3 - \frac{1}{2} = 5 - \frac{1}{2} = \frac{9}{2}
    $$

Therefore, the area between the curves is $\frac{9}{2}$.

## Integrating with Respect to $y$

Sometimes, it's easier to integrate with respect to $y$ if the functions are easily expressible in terms of $y$, i.e., $x = f(y)$ and $x = g(y)$. In this case, the area is:

$$
A = \int_{c}^{d} |f(y) - g(y)| \, dy
$$

Where $c$ and $d$ are the $y$-coordinates of the intersection points, and $f(y)$ and $g(y)$ are the functions of $y$.  $f(y)$ is the "right" function and $g(y)$ is the "left" function.



To find the intersection points of two curves



# [[Calc home]]

# [[area between two curves]]

# [[Calc home]]