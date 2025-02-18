# [[Calc home]]
# [[Calc Rules and theorems]]
The [[Fundamental Theorem of Calculus]] connects the seemingly disparate concepts of derivatives and [[integrals]]. It essentially states that differentiation and integration are inverse operations.  It's broken down into two parts:

## Part 1: The FTC and Accumulation Functions

Part 1 of the FTC deals with the derivative of an integral.  It states that if we have a function $F(x)$ defined as the integral of another function $f(t)$ from a constant $a$ to $x$:

$F(x) = \int_a^x f(t) \, dt$

then the derivative of $F(x)$ is simply $f(x)$:

$\frac{d}{dx} \left[ \int_a^x f(t) \, dt \right]] = f(x)$

**In simpler terms:** The rate of change of the accumulated area under a curve is the height of the curve at that point.

[[Accumulation Functions]]

This means that if we have a function representing the accumulation of something (like the total distance traveled given a velocity function), its derivative gives the instantaneous rate of that accumulation (like the instantaneous velocity).

**Example:**

Let $f(t) = t^2$.  Then

$F(x) = \int_1^x t^2 \, dt = \left[ \frac{t^3}{3} \right]]_1^x = \frac{x^3}{3} - \frac{1}{3}$

And $\frac{dF}{dx} = x^2 = f(x)$, as the FTC Part 1 states.


## Part 2: The FTC and Definite Integrals

Part 2 of the FTC provides a method for evaluating definite [[integrals]]. If $F(x)$ is an antiderivative of $f(x)$, then:

$\int_a^b f(x) \, dx = F(b) - F(a)$

**In simpler terms:** To find the definite integral of a function, find its antiderivative, evaluate it at the upper limit of integration, subtract the evaluation at the lower limit of integration.

[[Antiderivatives]]

**Example:**

To evaluate $\int_1^3 x^2 \, dx$, we find the antiderivative of $x^2$, which is $\frac{x^3}{3}$. Then:

$\int_1^3 x^2 \, dx = \left[ \frac{x^3}{3} \right]]_1^3 = \frac{3^3}{3} - \frac{1^3}{3} = 9 - \frac{1}{3} = \frac{26}{3}$


## Connecting the Two Parts

The two parts of the FTC are intimately related. Part 1 shows that differentiation "undoes" integration, while Part 2 uses this fact to provide a practical method for calculating definite [[integrals]].  Part 2 relies on the existence of an antiderivative, which is guaranteed (under certain conditions) by Part 1.

## Visual Representation

```desmos-graph
y = x^2
y = \int_0^x t^2 dt
```

The graph shows $y=x^2$ (blue) and its accumulation function from 0 to x (red). Notice how the slope of the red curve at any point x is equal to the value of the blue curve at that point, illustrating FTC Part 1.


## Important Note:

The FTC applies to continuous functions on a closed interval $[a, b]]$.  While many functions encountered in AP Calculus AB satisfy this condition, it's crucial to be aware of this limitation.


This rundown provides a concise overview of the [[Fundamental Theorem of Calculus]] for AP Calculus AB. Remember to practice applying both parts to various functions to solidify your understanding.
