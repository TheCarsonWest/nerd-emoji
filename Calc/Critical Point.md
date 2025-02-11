# [[Calc home]]

# TLDR: Find where $f'(x) = 0$  or is undefined 

Critical points are pivotal in understanding the behavior of a function.  They help us find local maxima, local minima, and saddle points, which are key to sketching accurate graphs and solving optimization problems.

## What are Critical Points?

A critical point of a function $f(x)$ occurs at any $x$-value where either:

[[1]].  $f'(x) = 0$ (the [[derivative]] is zero)
[[2]].  $f'(x)$ is undefined (the [[derivative]] doesn't exist)

In simpler terms, critical points are locations where the function's slope is either zero or undefined.

## Finding Critical Points

The process involves two steps:

[[1]]. **Find the [[derivative]]:** Calculate $f'(x)$.
[[2]]. **Solve for critical points:**  Set $f'(x) = 0$ and solve for $x$.  Also, identify any $x$-values where $f'(x)$ is undefined (e.g., points of discontinuity or sharp corners).

**Example:**

Let's find the critical points of the function $f(x) = x^[[3]] - 3x$.

[[1]].  The [[derivative]] is $f'(x) = 3x^[[2]] - [[3]]$.
[[2]].  Setting $f'(x) = 0$, we get $3x^[[2]] - [[3]] = 0$, which simplifies to $x^[[2]] = [[1]]$.  Thus, $x = [[1]]$ and $x = -[[1]]$ are critical points.
[[3]]. $f'(x)$ is defined for all real numbers.

Therefore, the critical points are $x = [[1]]$ and $x = -[[1]]$.


## Classifying Critical Points: The First [[Derivative]] Test

The first [[derivative]] test helps determine whether a critical point is a local maximum, local minimum, or neither.

[[1]]. **Test points:** Choose test points in the intervals created by the critical points.
[[2]]. **Evaluate the [[derivative]]:**  Evaluate $f'(x)$ at each test point.
[[3]]. **Interpret the sign:**
    * If $f'(x)$ changes from positive to negative, the critical point is a **local maximum**.
    * If $f'(x)$ changes from negative to positive, the critical point is a **local minimum**.
    * If $f'(x)$ does not change sign, the critical point is neither a local maximum nor a local minimum (it's a saddle point or an inflection point).

**Example (continued):**

For $f(x) = x^[[3]] - 3x$, the critical points are $x = [[1]]$ and $x = -[[1]]$.

*   For $x < -[[1]]$, $f'(x) > 0$.
*   For $-[[1]] < x < [[1]]$, $f'(x) < 0$.
*   For $x > [[1]]$, $f'(x) > 0$.

Thus, $x = -[[1]]$ is a local maximum, and $x = [[1]]$ is a local minimum.

```desmos-graph
y = x^[[3]] - 3x
```

[[First Derivative Test]]

[[Second Derivative Test]]


## Classifying Critical Points: The Second [[Derivative]] Test

The second [[derivative]] test provides an alternative method for classifying critical points.  It's often easier to use than the first [[derivative]] test, but it only works when the second [[derivative]] exists.

[[1]]. **Find the second [[derivative]]:** Calculate $f''(x)$.
[[2]]. **Evaluate at critical points:** Evaluate $f''(x)$ at each critical point.
[[3]]. **Interpret the sign:**
    * If $f''(x) < 0$, the critical point is a **local maximum**.
    * If $f''(x) > 0$, the critical point is a **local minimum**.
    * If $f''(x) = 0$, the test is inconclusive (you need to use the first [[derivative]] test).


**Example (continued):**

For $f(x) = x^[[3]] - 3x$, $f''(x) = 6x$.

*   At $x = -[[1]]$, $f''(-[[1]]) = -[[6]] < 0$, so $x = -[[1]]$ is a local maximum.
*   At $x = [[1]]$, $f''([[1]]) = [[6]] > 0$, so $x = [[1]]$ is a local minimum.

##  Important Note: Local vs. Global Extrema

Critical points help find *local* extrema (maxima or minima within a specific interval). To find *global* extrema (the absolute highest or lowest values over