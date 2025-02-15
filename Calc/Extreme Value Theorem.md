# [[Calc home]]

The [[Extreme Value Theorem]] is a fundamental concept in calculus that guarantees the existence of maximum and minimum values for a continuous function over a closed interval.
## Theorem Statement

#### Let $f$ be a continuous function on a closed interval $[a, b]]$. Then $f$ attains both an absolute maximum value $f(c)$ and an absolute minimum value $f(d)$ at some numbers $c$ and $d$ in $[a, b]]$.


## Key Concepts

* **Continuous Function:**  A function is continuous on an interval if its graph can be drawn without lifting your pen.  Formally, a function $f(x)$ is continuous at a point $x=c$ if $\lim_{x \to c} f(x) = f(c)$.  [[Continuity]]
* **Closed Interval:** A closed interval $[a, b]]$ includes its endpoints, $a$ and $b$.  Open intervals $(a, b)$ do not include the endpoints.
* **Absolute Maximum/Minimum:** The absolute maximum (or minimum) is the largest (or smallest) value of the function over the entire interval.  It's also sometimes called the global maximum/minimum.
* **Local Maximum/Minimum:** A local maximum (or minimum) is the largest (or smallest) value of the function within a small neighborhood around a point. [[Local vs. Absolute Extrema]]


## Finding Extrema

To find the absolute maximum and minimum values of a continuous function $f(x)$ on a closed interval $[a, b]]$:

1. **Find critical points:** Find all values of $x$ in the interval $(a, b)$ where $f'(x) = 0$ or $f'(x)$ is undefined.
2. **Evaluate the function:** Evaluate $f(x)$ at each [[Critical Point]] found in step [[1, and also at the endpoints $x = a$ and $x = b$.
3. **Compare values:** The largest value among those found in step 2 is the absolute maximum, and the smallest value is the absolute minimum.


## Example

Let's find the absolute maximum and minimum values of $f(x) = x^3 - 3x + 2$ on the interval $[-2, 2$.

1. **Find critical points:** $f'(x) = 3x^2 - 3 = 0$, which gives $x^2 = [[1$, so $x = [[1$ and $x = -[[1$. Both are in the interval $(-2, 2)$.

2. **Evaluate the function:**
   $f(-2) = (-2)^3 - 3(-2) + 2 = -2$
   $f(-[[1) = (-[[1)^3 - 3(-[[1) + 2 = 4$
   $f([[1) = ([[1)^3 - 3([[1) + 2 = 0$
   $f(2) = (2)^3 - 3(2) + 2 = 4$

3. **Compare values:** The absolute maximum is 4, which occurs at $x = -[[1$ and $x = 2$. The absolute minimum is -2, which occurs at $x = -2$.


```desmos-graph
y = x^3 - 3x + 2
```

##  Important Note

The EVT only guarantees the existence of absolute extrema; it doesn't provide a method for finding them if the function is not differentiable or the interval is not closed.  For example, the function $f(x) = x$ on the open interval $(0, [[1)$ has no absolute maximum or minimum.


## Summary

The [[Extreme Value Theorem]] is a powerful tool for analyzing the behavior of continuous functions on closed intervals.  By understanding its conditions and applying the steps outlined above, you can confidently locate the absolute maximum and minimum values of many functions.
