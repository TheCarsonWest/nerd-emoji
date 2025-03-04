# [[Calc home]]
# Separable Equations (AP Calculus AB Rundown)

## Introduction

Separable equations are a specific type of differential equation that can be solved using a relatively straightforward method.  They are frequently encountered in AP Calculus AB and represent a powerful tool for modeling various phenomena.  A differential equation is separable if it can be written in a form where the variables can be "separated" to opposite sides of the equation.

## General Form

A first-order differential equation is considered separable if it can be written in the form:

$$
\frac{dy}{dx} = f(x)g(y)
$$

where $f(x)$ is a function of $x$ only, and $g(y)$ is a function of $y$ only.

## Solution Method

1. **Separate the variables:**  Rewrite the equation so that all terms involving $y$ (including $dy$) are on one side and all terms involving $x$ (including $dx$) are on the other side.  This typically involves algebraic manipulation.

$$
\frac{1}{g(y)} dy = f(x) dx
$$

[[Division by Zero]]

2. **Integrate both sides:** Apply the integral to both sides of the equation with respect to their respective variables.

$$
\int \frac{1}{g(y)} dy = \int f(x) dx
$$

[[Integration Techniques]]

3. **Solve for $y$ (if possible):** After integrating, you will have an equation involving $x$ and $y$.  Attempt to isolate $y$ to express the solution explicitly as $y = F(x)$. If this isn't feasible, leave the solution in implicit form.

[[Implicit Differentiation]]

4. **Apply initial conditions (if given):** If an initial condition is provided (e.g., $y(x_0) = y_0$), substitute the values of $x_0$ and $y_0$ into the solution to determine the constant of integration ($C$) from the integration step.

[[Initial Value Problems]]

## Example

Solve the differential equation:

$$
\frac{dy}{dx} = xy^2
$$

1. **Separate Variables:**
   $$
   \frac{1}{y^2} dy = x dx
   $$

2. **Integrate Both Sides:**
   $$
   \int \frac{1}{y^2} dy = \int x dx
   $$
   $$
   -\frac{1}{y} = \frac{x^2}{2} + C
   $$

3. **Solve for $y$:**
   $$
   y = -\frac{1}{\frac{x^2}{2} + C} = -\frac{2}{x^2 + 2C}
   $$
   We can replace $2C$ with a new constant, say $K$.
   $$
   y = -\frac{2}{x^2 + K}
   $$

## Common Applications

Separable equations are used in a wide variety of applications, including:

* **Exponential Growth and Decay:** Modeling population growth, radioactive decay, and other processes where the rate of change is proportional to the current quantity. [[Exponential Growth and Decay]]
* **Newton's Law of Cooling:** Describing the cooling or heating of an object in a surrounding medium. [[Newton's Law of Cooling]]
* **Mixing Problems:** Analyzing the concentration of substances in tanks or containers with inflow and outflow.  [[Mixing Problems]]


This rundown provides a fundamental understanding of separable equations.  Practice solving various examples to solidify your understanding and prepare for the AP Calculus AB exam.
