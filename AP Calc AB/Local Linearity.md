[[Calc home]]

Local linearity is a fundamental concept in calculus that describes how a function can be approximated by a line in a small neighborhood around a point. This concept is crucial for understanding derivatives and their applications.
# [[Local Linear Approximation]]


## [[Tangent Lines]]

A tangent line to a curve at a point is a line that "touches" the curve at that point and has the same slope as the curve at that point. 

**Definition:**

The tangent line to the graph of $y=f(x)$ at the point $(a,f(a))$ is the line that passes through $(a,f(a))$ and has slope $f'(a)$, the [[Derivative]] of $f$ at $x=a$.

**Equation of the Tangent Line:**

Using the point-slope form of a line, the equation of the tangent line is given by:
# $$y - f(a) = f'(a)(x-a)$$
**Example:**
Consider the function $f(x) = x^2$. The [[Derivative]] of $f(x)$ is $f'(x) = 2x$. At the point $(1,1)$, the slope of the tangent line is $f'(1) = 2$. 
Therefore, the equation of the tangent line is:
$$y - 1 = 2(x-1)$$

```desmos-graph
y = x^2
y - 1 = 2(x-1)
```


### [[Implications for Derivatives]]

The concept of local linearity is closely tied to the definition of the [[Derivative]]. The [[Derivative]] of a function at a point represents the slope of the tangent line at that point. This slope is also the rate of change of the function at that point.

**Geometric Interpretation:**

The [[Derivative]] $f'(a)$ represents the instantaneous rate of change of $f(x)$ at $x=a$. Geometrically, it is the slope of the tangent line to the graph of $f(x)$ at the point $(a,f(a))$.

**Physical Interpretation:**

In physical applications, the [[Derivative]] can represent quantities like velocity (the rate of change of position), acceleration (the rate of change of velocity), or the rate of change of a population.
