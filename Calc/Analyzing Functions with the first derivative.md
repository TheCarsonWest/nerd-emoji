# [[Calc home]]

This rundown covers using the first [[derivative]] to analyze the behavior of a function.  We'll focus on finding [[Critical Point]], increasing/decreasing intervals, and local extrema.

## [[1. Finding Critical Points

Critical points are points in the domain of a function where the [[derivative]] is either zero or undefined.  These points are potential locations for local maxima, local minima, or neither.

To find critical points:

[[1. **Find the first [[derivative]]:** $f'(x)$
2. **Set the [[derivative]] equal to zero:** $f'(x) = 0$ and solve for $x$.  These are the critical points where the [[derivative]] is zero.
3. **Find where the [[derivative]] is undefined:** Determine if there are any points in the domain of $f(x)$ where $f'(x)$ is undefined (e.g., division by zero, square root of a negative number). These are also critical points.

**Example:**

Let $f(x) = x^3 - 3x$. Then $f'(x) = 3x^2 - 3$.

Setting $f'(x) = 0$, we get $3x^2 - 3 = 0$, which gives $x = \pm [[1$.

$f'(x)$ is defined for all real numbers, so there are no additional critical points where the [[derivative]] is undefined.

Therefore, the critical points are $x = [[1$ and $x = -[[1$.


## 2. Increasing and Decreasing Intervals

The first [[derivative]] tells us about the function's increasing and decreasing behavior:

* **$f'(x) > 0$:**  $f(x)$ is increasing on this interval.
* **$f'(x) < 0$:** $f(x)$ is decreasing on this interval.

To find increasing/decreasing intervals:

[[1. **Find the critical points.**
2. **Test intervals:** Choose test points in the intervals created by the critical points.  Plug these test points into $f'(x)$. If $f'(x) > 0$, the function is increasing in that interval; if $f'(x) < 0$, it's decreasing.


**Example (continuing from above):**

For $f(x) = x^3 - 3x$, the critical points are $x = -[[1$ and $x = [[1$.

* **Interval $(-\infty, -[[1)$:** Test point $x = -2$. $f'(-2) = 3(-2)^2 - 3 = 9 > 0$, so $f(x)$ is increasing on $(-\infty, -[[1)$.
* **Interval $(-[[1, [[1)$:** Test point $x = 0$. $f'(0) = -3 < 0$, so $f(x)$ is decreasing on $(-[[1, [[1)$.
* **Interval $([[1, \infty)$:** Test point $x = 2$. $f'(2) = 9 > 0$, so $f(x)$ is increasing on $([[1, \infty)$.


## 3. Local Extrema (Local Maxima and Minima)

### First [[Derivative]] test
Local extrema occur at critical points.  The first [[derivative]] test helps determine whether a [[Critical Point]] is a local maximum, local minimum, or neither:

[[1. **If $f'(x)$ changes from positive to negative at a [[Critical Point]] $c$, then $f(c)$ is a local maximum.**
2. **If $f'(x)$ changes from negative to positive at a [[Critical Point]] $c$, then $f(c)$ is a local minimum.**
3. **If $f'(x)$ does not change sign at a [[Critical Point]] $c$, then $f(c)$ is neither a local maximum nor a local minimum (it could be a saddle point).**


**Example (continuing from above):**

* At $x = -[[1$, $f'(x)$ changes from positive to negative, so $f(-[[1) = (-[[1)^3 - 3(-[[1) = 2$ is a local maximum.
* At $x = [[1$, $f'(x)$ changes from negative to positive, so $f([[1) = ([[1)^3 - 3([[1) = -2$ is a local minimum.


```desmos-graph
y = x^3 - 3x
```

[[Second Derivative Test]]  The second [[derivative]] test provides an alternative method to classify critical points.  It's often easier than the first [[derivative]] test but has limitations.

## 4. Concavity and [[Inflection Points]]

