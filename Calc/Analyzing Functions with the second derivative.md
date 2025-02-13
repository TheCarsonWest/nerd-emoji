# [[Calc home]]

The second [[derivative]], denoted as $f''(x)$ or $\frac{d^2y}{dx^2}$, provides crucial information about the shape and behavior of a function.  It helps us understand concavity and inflection points.

## Concavity

The second [[derivative]] reveals the concavity of a function.

* **$f''(x) > 0$ on an interval:** The function is **concave up** (or "holds water") on that interval.  The graph curves upwards like a smile.

* **$f''(x) < 0$ on an interval:** The function is **concave down** (or "spills water") on that interval. The graph curves downwards like a frown.

* **$f''(x) = 0$ on an interval:** This doesn't automatically mean the function is neither concave up nor concave down.  Further investigation is needed. [[Test for Concavity]]

```desmos-graph
y = x^3 - 3x
y = x^2
y = -x^2
```

## [[Inflection Points]] 
An **inflection point** is a point on the graph where the concavity changes.  This means the function transitions from concave up to concave down, or vice versa.  To find inflection points:

[[1. **Find the second [[derivative]]:** $f''(x)$.
2. **Solve for $f''(x) = 0$ or where $f''(x)$ is undefined.**  These are potential inflection points.
3. **Test the concavity on intervals around the potential inflection points.** If the concavity changes across a potential inflection point, it is an inflection point. If it doesn't change, it's not an inflection point. Second [[Derivative]] Test for [[Inflection Points]] 
**Example:**

Let's consider the function $f(x) = x^3 - 3x$.

[[1. $f'(x) = 3x^2 - 3$
2. $f''(x) = 6x$
3. $f''(x) = 0$ when $x = 0$.
4. Testing intervals:
    * $x < 0$: $f''(x) < 0$ (concave down)
    * $x > 0$: $f''(x) > 0$ (concave up)

Since the concavity changes at $x = 0$, there is an inflection point at $(0, f(0)) = (0, 0)$.


## Relationship to the First [[Derivative]] and Optimization [[Extrema and Concavity]]

The second [[derivative]] can be used in conjunction with the first [[derivative]] to determine the nature of critical points (where $f'(x) = 0$ or $f'(x)$ is undefined):

* **Second [[Derivative]] Test:** If $f'(c) = 0$ and:
    * $f''(c) > 0$, then $f(c)$ is a **local minimum**.
    * $f''(c) < 0$, then $f(c)$ is a **local maximum**.
    * $f''(c) = 0$, the test is inconclusive; further investigation is needed (e.g., the First [[Derivative]] Test).


## Applications

Understanding concavity and inflection points is crucial for:

* **Sketching graphs:** Accurately depicting the shape of a function.
* **Optimization problems:** Identifying maximum and minimum values.
* **Modeling real-world phenomena:** Analyzing rates of change and trends.


This rundown provides a foundation for analyzing functions using the second [[derivative]] in Calculus AB.  Remember to always consider the context of the problem and use appropriate tests to draw accurate conclusions.
