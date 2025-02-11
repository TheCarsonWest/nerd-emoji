
[[Differentiability]], a cornerstone concept in Calculus AB, essentially describes whether a function has a well-defined [[derivative]] at a specific point.  It's closely tied to the idea of a smooth, continuous curve.  A function is differentiable at a point if its graph has a tangent line at that point.  This means the function must be both continuous and smooth at that point. Let's break down the key aspects:


## [[1. The Definition of the [[Derivative]]

The [[derivative]] of a function $f(x)$ at a point $x=a$, denoted as $f'(a)$, is defined as:

$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$

This limit represents the slope of the tangent line to the graph of $f(x)$ at $x=a$.  If this limit exists, the function is differentiable at $x=a$.


## [[2].  Relationship to [[Continuity]]

[[Continuity]]

A function must be continuous at a point to be differentiable at that point. However, [[continuity]] alone is not sufficient for differentiability.  A function can be continuous at a point but not differentiable there.


## [[3]. Conditions for Non-[[Differentiability]]

A function is *not* differentiable at a point if any of the following occur:

* **Sharp Corner/Cusp:** The function has a sharp turn or cusp at the point.  The slope of the tangent line approaches different values from the left and right.

```desmos-graph
y = abs(x)
```

* **Vertical Tangent:** The function has a vertical tangent line at the point. The slope of the tangent line approaches infinity.

* **Discontinuity:** The function is discontinuous (has a jump, hole, or asymptote) at the point.

```desmos-graph
y = [[1/(x-[[1)
{x>[[1}
y = [[2]
{x=[[1}
y = x
{x<[[1}
```

* **Oscillating Function:** The function oscillates infinitely rapidly near the point.


## [[4].  [[Differentiability]] and Smoothness
 [[Differentiability]] implies smoothness.  A differentiable function will have a smooth, continuous curve without any sharp corners, cusps, or vertical tangents. However, the converse is not always true (a function can be smooth but not differentiable everywhere).

[[Higher Order Derivatives]]


## [[5].  Practical Applications
 [[Differentiability]] is crucial for many applications in Calculus AB, including:

* **Finding instantaneous rates of change:** The [[derivative]] gives the instantaneous rate of change of a function at a specific point.
* **Optimization problems:** Finding maximum and minimum values of a function often involves analyzing its [[derivative]].
* **Related rates problems:**  Using derivatives to relate the rates of change of different variables.
* **Curve sketching:**  The [[derivative]] helps determine the increasing/decreasing intervals and concavity of a function.


## [[6].  Checking for [[Differentiability]] 
To determine if a function is differentiable at a point, you typically:

[[1. Check for [[continuity]] at the point.
[[2]. Calculate the left-hand and right-hand derivatives using the limit definition.
[[3]. If the left-hand and right-hand derivatives are equal and finite, the function is differentiable at the point.


In summary, differentiability is a crucial concept in Calculus AB that connects the idea of a function's slope to its smoothness and [[continuity]]. Understanding the conditions for differentiability and non-differentiability is essential for mastering many important calculus concepts and applications.
