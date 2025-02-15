[[Calc home]]

Local linearity is a fundamental concept in calculus that describes how a function can be approximated by a line in a small neighborhood around a point. This concept is crucial for understanding derivatives and their applications.
# [[Local Linear Approximation]]


## [[Tangent Lines]]

A tangent line to a curve at point is a line that "touches" the curve at that point and has the same slope as the curve at that point. 

**Definition:**

The tangent line to the graph of $y=f(x)$ at the point $(a,f(a))$ is the line that passes through $(a,f(a))$ and has slope $f'(a)$, the [[Derivative]] of $f$ at $x=a$.

**Equation of the Tangent Line:**

Using the point-slope form of a line, the equation of the tangent line is given by:
# $$y - f(a) = f'(a)(x-a)$$
**Example:**
Consider the function $f(x) = x^2$. The [[Derivative]] of $f(x)$ is $f'(x) = 2x$. At the point $([[1,[[1)$, the slope of the tangent line is $f'([[1) = 2$. 
Therefore, the equation of the tangent line is:
$$y - [[1 = 2(x-[[1)$$

```desmos-graph
y = x^2
y - [[1 = 2(x-[[1)
```

# [[Test for the Accuracy of Local Linearity]]