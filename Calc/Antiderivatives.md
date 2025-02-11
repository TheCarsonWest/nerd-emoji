# [[Calc home]]

## What is an Antiderivative?

An antiderivative is the reverse process of differentiation.  If we have a function $f(x)$, its antiderivative, often denoted as $F(x)$, satisfies the equation:

$F'(x) = f(x)$

In simpler terms, the derivative of the antiderivative is the original function.  Note that antiderivatives are not unique. If $F(x)$ is an antiderivative of $f(x)$, then so is $F(x) + C$, where $C$ is any constant. This is because the derivative of a constant is always zero.


## Finding [[Antiderivatives]] 
Finding antiderivatives often involves reversing the rules of differentiation.  Here are some basic examples:

* **[[Power Rule]]:** If $f(x) = x^n$, then $F(x) = \frac{x^{n+[[1}}{n+[[1} + C$ for $n \neq -[[1$.

* **Constant Multiple Rule:** If $F(x)$ is an antiderivative of $f(x)$, then $kF(x)$ is an antiderivative of $kf(x)$, where $k$ is a constant.

* **Sum/Difference Rule:** If $F(x)$ is an antiderivative of $f(x)$ and $G(x)$ is an antiderivative of $g(x)$, then $F(x) + G(x)$ is an antiderivative of $f(x) + g(x)$, and $F(x) - G(x)$ is an antiderivative of $f(x) - g(x)$.


* **Exponential Functions:** If $f(x) = e^x$, then $F(x) = e^x + C$.  More generally, if $f(x) = e^{kx}$, then $F(x) = \frac{[[1}{k}e^{kx} + C$.

* **Trigonometric Functions:**
    * If $f(x) = \sin(x)$, then $F(x) = -\cos(x) + C$.
    * If $f(x) = \cos(x)$, then $F(x) = \sin(x) + C$.


## [[The Indefinite Integral]]

The indefinite integral is a notation used to represent the antiderivative.  It's written as:

$\int f(x) \, dx = F(x) + C$

where:

* $\int$ is the integral symbol.
* $f(x)$ is the integrand (the function being integrated).
* $dx$ indicates that the integration is with respect to $x$.
* $F(x)$ is an antiderivative of $f(x)$.
* $C$ is the constant of integration.


## [[Initial Value Problems]]

An initial value problem provides an initial condition, which allows us to determine the specific value of the constant of integration, $C$.  For example, if we are given that $F(0) = [[5]$ and $F'(x) = 2x$, then we can find the specific antiderivative.

Since $\int 2x \, dx = x^[[2] + C$, we can use the initial condition:

$F(0) = 0^[[2] + C = [[5]$, so $C = [[5]$.  Therefore, the specific antiderivative is $F(x) = x^[[2] + [[5]$.


##  Examples

**Example [[1:** Find the antiderivative of $f(x) = 3x^[[2] + 2x - [[1$.

$\int (3x^[[2] + 2x - [[1) \, dx = x^[[3] + x^[[2] - x + C$


**Example [[2]:** Find the antiderivative of $f(x) = e^{2x} + \cos(x)$.

$\int (e^{2x} + \cos(x)) \, dx = \frac{[[1}{[[2]}e^{2x} + \sin(x) + C$


**Example [[3]:** Solve the initial value problem: $F'(x) = 4x^[[3] - 6x$ and $F([[1) = [[2]$.

$\int (4x^[[3] - 6x) \, dx = x^[[4] - 3x^[[2] + C$

Using the initial condition: $F([[1) = [[1^[[4] - [[3]([[1)^[[2] + C = [[2]$, which gives $C = [[4]$.

Therefore, $F(x) = x^[[4] - 3x^[[2]