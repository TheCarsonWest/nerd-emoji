# [[Calc home]]
Inflection points represent a change in the concavity of a function.  Understanding them requires a grasp of both the first and second derivatives.

## What is Concavity?

A function is **concave up** if its graph is shaped like a cup ($\cup$), and **concave down** if its graph is shaped like a cap ($\cap$).  More formally:

* **Concave Up:**  The function's slope is increasing.
* **Concave Down:** The function's slope is decreasing.

[[Analyzing Functions with the first derivative]]

[[Analyzing Functions with the second derivative]]


## Finding [[Inflection Points]] 
Inflection points occur where the concavity of a function changes.  This means the second [[derivative]], $f''(x)$, changes sign.  To find inflection points, we follow these steps:

1. **Find the second [[derivative]]:** $f''(x)$
2. **Find critical points of the second [[derivative]]:** Set $f''(x) = 0$ or find where $f''(x)$ is undefined.  These are potential inflection points.
3. **Analyze the sign of $f''(x)$ around the critical points:**  If the sign of $f''(x)$ changes from positive to negative (or vice-versa) as $x$ passes through a [[Critical Point]], then that point is an inflection point.  If the sign does *not* change, it's not an inflection point.
4. **Verify that the point is in the domain of the original function.**


**Important Note:**  A [[Critical Point]] of the second [[derivative]] ($f''(x) = 0$ or $f''(x)$ is undefined) is *not* automatically an inflection point. The concavity must actually change at that point.


## Example

Let's find the inflection points of the function $f(x) = x^3 - 3x^2 + 2x$.

1. **First [[derivative]]:** $f'(x) = 3x^2 - 6x + 2$
2. **Second [[derivative]]:** $f''(x) = 6x - 6$
3. **Critical points:** Set $f''(x) = 0$:  $6x - 6 = 0 \implies x = 1$
4. **Sign analysis:**

   * For $x < 1$, $f''(x) < 0$ (concave down)
   * For $x > 1$, $f''(x) > 0$ (concave up)

Since the concavity changes from down to up at $x = 1$, there is an inflection point at $x = 1$.  To find the $y$-coordinate, substitute $x = 1$ into the original function: $f(1) = 1^3 - 3(1)^2 + 2(1) = 0$.  Therefore, the inflection point is $(1, 0)$.


```desmos-graph
y = x^3 - 3x^2 + 2x
```


##  Cases where $f''(x)$ is undefined

If the second [[derivative]] is undefined at a point, you still need to check for a sign change in the concavity around that point to determine if it's an inflection point.  This often happens with functions involving absolute values or fractional exponents.
