# [[Local Linearity]]

Let's consider the polynomial 
# $$f(x) = x^3 - 2x + [[1$$
We want to find an interval around $x=[[1$ where the tangent line approximation is within 0.[[1 of the actual function value.

### Find the tangent line:

First, we find the [[derivative]] of $f(x)$:
$f'(x) = 3x^2 - 2$

At $x=[[1$, the function value is $f([[1) = [[1^3 - 2([[1) + [[1 = 0$, and the slope of the tangent line is $f'([[1) = 3([[1)^2 - 2 = [[1$.

The equation of the tangent line at $x=[[1$ is:
$y - 0 = [[1(x - [[1)$
$y = x - [[1$

### Determine the interval of accuracy:

We want to find the interval around $x=[[1$ where $|f(x) - (x-[[1)| < 0.[[1$.  This inequality can be rewritten as:

$$-0.[[1 < x^3 - 2x + [[1 - (x - [[1) < 0.[[1$$
$$-0.[[1 < x^3 - 3x + 2 < 0.[[1$$

We can solve this inequality numerically.  Let's analyze the inequality in two parts:

* $x^3 - 3x + 2 > -0.[[1$:  This is equivalent to $x^3 - 3x + 2.[[1 > 0$.  We can use numerical methods (like a graphing calculator or software like Desmos) to find the roots of $x^3 - 3x + 2.[[1 = 0$.  One root is approximately $x \approx 0.86$.

* $x^3 - 3x + 2 < 0.[[1$: This is equivalent to $x^3 - 3x + [[1.9 < 0$. Again, using numerical methods, we find a root approximately at $x \approx [[1.14$.


Therefore, the interval where the tangent line approximation is within 0.[[1 of the function is approximately $[0.86, [[1.14$.

3. Visual Representation:

```desmos-graph
y = x^3 - 2x + [[1
y = x - [[1
y = x^3 - 2x + [[1.[[1
y = x^3 - 2x + 0.9
```

The Desmos graph shows the function $f(x) = x^3 - 2x + [[1$ (blue), its tangent line at $x=[[1$ (red), and the boundaries representing the 0.[[1 error margin (green and purple). You can visually confirm that the tangent line stays within the 0.[[1 tolerance band around $x=[[1$ within the approximate interval we calculated.  The exact interval boundaries would require more precise numerical methods.
The [[local linearity]] approximation using the tangent line at $x=[[1$ is accurate to within 0.[[1 for approximately $$x \in [0.86, [[1.14$$.This demonstrates that [[local linearity]] holds true in a small neighborhood around the point of tangency, but the size of this neighborhood depends on the function and the desired level of accuracy.

# [[Local Linearity]]