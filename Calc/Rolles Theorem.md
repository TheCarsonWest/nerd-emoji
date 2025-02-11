
Rolle's Theorem is a foundational result in calculus that provides a condition under which a function is guaranteed to have a horizontal tangent line.  It serves as a stepping stone to understanding the more general [[Mean Value Theorem]].

## Statement of Rolle's Theorem

Let $f$ be a function that satisfies the following three hypotheses:

[[1. **$f$ is continuous on the closed interval $[a, b]$**:  This means the function has no breaks or jumps within the interval.  [[Continuity]]

[[2]. **$f$ is differentiable on the open interval $(a, b)$**: This means the function is smooth and has a [[derivative]] at every point within the interval.  [[Differentiability]]

[[3]. **$f(a) = f(b)$**: The function values at the endpoints of the interval are equal.

Then there exists at least one number $c$ in the open interval $(a, b)$ such that $f'(c) = 0$.  In other words, there's at least one point in the interval where the tangent line is horizontal.


## Geometric Interpretation

Imagine the graph of a function. Rolle's Theorem states that if the function is continuous and differentiable on an interval, and the function values at the endpoints of the interval are the same, then there must be at least one point within the interval where the tangent line is horizontal (i.e., the slope is zero).

```desmos-graph
y = x^[[3] - 4x
y = 0
```

In the graph above, the function $y = x^[[3] - 4x$ satisfies Rolle's Theorem on the interval $[-[[2], [[2]]$ because $f(-[[2]) = f([[2]) = 0$.  Notice there are horizontal tangents at approximately $x \approx -[[1.15$ and $x \approx [[1.15$.


## Proof (Sketch)

The proof relies on the [[Extreme Value Theorem]]. Since $f$ is continuous on the closed interval $[a, b]$, it must attain both a maximum and a minimum value on that interval.

* **Case [[1:  The maximum and minimum values are both equal to $f(a) = f(b)$.**  Then $f(x)$ is constant on $[a, b]$, and $f'(x) = 0$ for all $x$ in $(a, b)$.

* **Case [[2]: Either the maximum or minimum value is different from $f(a) = f(b)$.** This means the maximum or minimum must occur at some point $c$ in the *open* interval $(a, b)$.  At this point, the [[derivative]] must be zero ($f'(c) = 0$) because it's either a local maximum or minimum.  [[Extreme Value Theorem]]


## Example

Let $f(x) = x^[[2] - 4x + [[3]$ on the interval $[[1, [[3]]$.

[[1. $f(x)$ is a polynomial, so it's continuous and differentiable everywhere.
[[2]. $f([[1) = 0$ and $f([[3]) = 0$.

Therefore, Rolle's Theorem guarantees the existence of at least one $c$ in $([[1, [[3])$ such that $f'(c) = 0$.  We can find this by calculating the [[derivative]]: $f'(x) = 2x - [[4]$. Setting $f'(c) = 0$, we get $2c - [[4] = 0$, which gives $c = [[2]$.  Note that $[[2]$ is in the interval $([[1, [[3])$.


##  Important Note

Rolle's Theorem only guarantees the *existence* of at least one $c$ such that $f'(c) = 0$.  There may be more than one such point.  The theorem doesn't provide a method for finding all such points, only that at least one exists under the given conditions.
