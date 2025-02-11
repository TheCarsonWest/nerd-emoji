# [[Calc home]]
# [[Analyzing Functions with the second derivative]]
Concavity describes the curvature of a function's graph.  A function is concave up if its graph curves upward, like a smile, and concave down if its graph curves downward, like a frown.  We determine concavity using the second [[derivative]] of the function.

## The Second [[Derivative]] [[Test for Concavity]] 
The concavity of a function $f(x)$ at a point $x=c$ is determined by the sign of its second [[derivative]], $f''(c)$:

* **Concave Up:** If $f''(c) > 0$, then the graph of $f(x)$ is concave up at $x=c$.
* **Concave Down:** If $f''(c) < 0$, then the graph of $f(x)$ is concave down at $x=c$.
* **Inflection Point:** If $f''(c) = 0$ and the concavity changes at $x=c$ (from concave up to concave down or vice versa), then $x=c$ is an inflection point.  [[Inflection Points]]

**Important Note:** $f''(c) = 0$ does *not* guarantee an inflection point.  The concavity must actually change at $x=c$.  Consider the function $f(x) = x^[[4]]$.  $f''(x) = 12x^[[2]]$, and $f''(0) = 0$, but the function is concave up on both sides of $x=0$, so there's no inflection point at $x=0$.

## Finding Intervals of Concavity

To find the intervals where a function is concave up or concave down, we follow these steps:

[[1]]. **Find the second [[derivative]]:** Calculate $f''(x)$.
[[2]]. **Find critical points of the second [[derivative]]:** Solve the equation $f''(x) = 0$ or find where $f''(x)$ is undefined. These points are potential boundaries for intervals of concavity.
[[3]]. **Test intervals:** Choose test points in the intervals determined by the critical points of $f''(x)$.  Evaluate $f''(x)$ at each test point.
[[4]]. **Determine concavity:**  If $f''(x) > 0$ in an interval, the function is concave up in that interval. If $f''(x) < 0$, the function is concave down.


## Example

Let's consider the function $f(x) = x^[[3]] - 3x^[[2]] + [[2]]$.

[[1]]. **First [[derivative]]:** $f'(x) = 3x^[[2]] - 6x$
[[2]]. **Second [[derivative]]:** $f''(x) = 6x - [[6]]$
[[3]]. **Critical points of $f''(x)$:** $f''(x) = 0$ when $6x - [[6]] = 0$, which means $x = [[1]]$.
[[4]]. **Test intervals:** We test the intervals $(-\infty, [[1]])$ and $([[1]], \infty)$.
    * For $x = 0$ (in $(-\infty, [[1]])$): $f''(0) = -[[6]] < 0$, so $f(x)$ is concave down on $(-\infty, [[1]])$.
    * For $x = [[2]]$ (in $([[1]], \infty)$): $f''([[2]]) = [[6]] > 0$, so $f(x)$ is concave up on $([[1]], \infty)$.
[[5]]. **Inflection Point:** Since the concavity changes at $x=[[1]]$, there is an inflection point at $x=[[1]]$.


```desmos-graph
y = x^[[3]] - 3x^[[2]] + [[2]]
```

[[Second [[Derivative]] Test]]

This example demonstrates how to find intervals of concavity and identify inflection points. Remember to always check for changes in concavity when the second [[derivative]] is zero.  A sign chart can be very helpful in organizing your work.
