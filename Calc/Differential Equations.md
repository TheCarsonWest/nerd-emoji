# [[Calc home]]
# Differential Equations

## I. Introduction to Differential Equations

*   **Definition:** A differential equation is an equation that relates a function to its derivatives.  In AP Calculus AB, we primarily focus on first-order differential equations, meaning they involve the first derivative.

*   **General Form:** A first-order differential equation can often be written in the form:

    $\qquad \frac{dy}{dx} = f(x, y)$

*   **Goal:** The goal is to find a function $y = f(x)$ that satisfies the differential equation. This function is called a *solution* to the differential equation.

*   **Types of Solutions:**
    *   **General Solution:**  Contains an arbitrary constant (usually 'C'). Represents a family of solutions.
    *   **Particular Solution:** Obtained by finding the value of the arbitrary constant 'C' using an initial condition.

## II. Solving Differential Equations: Separation of Variables ***

*   **Method:** Separation of Variables is a technique used to solve certain types of first-order differential equations. It works when the equation can be written in the form:

    $\qquad \frac{dy}{dx} = g(x)h(y)$

*   **Steps:**

    1.  **Separate the Variables:**  Rewrite the equation so that all terms involving 'y' and 'dy' are on one side, and all terms involving 'x' and 'dx' are on the other side.

        $\qquad \frac{dy}{h(y)} = g(x) dx$

    2.  **Integrate Both Sides:** Integrate both sides of the equation with respect to their respective variables. Remember to include the constant of integration (+C) on *one* side (usually the side with 'x').

        $\qquad \int \frac{dy}{h(y)} = \int g(x) dx + C$

    3.  **Solve for y:**  Solve the resulting equation for 'y' in terms of 'x'. This gives you the general solution.

    4.  **Apply Initial Condition (if given):** If an initial condition is provided (e.g., y(0) = 2), substitute the values of 'x' and 'y' into the general solution to solve for the constant 'C'.  This gives you the particular solution.

*Example:*

Solve the differential equation $\frac{dy}{dx} = xy$ with the initial condition $y(0) = 2$.

1.  **Separate:** $\frac{dy}{y} = x dx$

2.  **Integrate:** $\int \frac{dy}{y} = \int x dx + C$  which gives  $\ln|y| = \frac{1}{2}x^2 + C$

3.  **Solve for y:** $e^{\ln|y|} = e^{\frac{1}{2}x^2 + C}$ , so $|y| = e^{\frac{1}{2}x^2}e^C$. We can write $y = Ae^{\frac{1}{2}x^2}$, where $A = \pm e^C$.

4.  **Apply Initial Condition:** $y(0) = 2$, so $2 = Ae^{\frac{1}{2}(0)^2} = A(1)$.  Therefore, $A = 2$.

    The particular solution is $y = 2e^{\frac{1}{2}x^2}$.

[[Integration Techniques]]
[[Absolute Values in Integration]]
[[Solving for C]]

## III. Slope Fields ***

*   **Definition:** A slope field (also called a direction field) is a graphical representation of the solutions to a first-order differential equation. At each point (x, y) in the plane, a small line segment (or arrow) is drawn with a slope equal to the value of  $\frac{dy}{dx}$  at that point.

*   **Interpretation:** The slope field visually shows the direction that solutions to the differential equation would take at different points in the plane.  You can sketch solution curves by following the "flow" of the slope field.

*   **Construction:**
    1.  Choose a grid of points (x, y) in the plane.
    2.  For each point (x, y), evaluate  $\frac{dy}{dx}$  using the given differential equation.
    3.  Draw a short line segment at (x, y) with the slope you calculated.

*   **Using Slope Fields:**
    *   **Sketching Solutions:** Given an initial condition, start at the corresponding point on the slope field and follow the direction of the line segments to sketch a solution curve.
    *   **Qualitative Analysis:**  Slope fields can help you understand the general behavior of solutions, such as where solutions are increasing, decreasing, or constant. They can also help identify equilibrium solutions (where $\frac{dy}{dx} = 0$).

[[Equilibrium Solutions]]
[[Sketching on Slope Fields]]

## IV. Exponential Growth and Decay ***

*   **Differential Equation:** The classic differential equation for exponential growth and decay is:

    $\qquad \frac{dy}{dt} = ky$

    where:
    *   'y' represents the quantity that is growing or decaying.
    *   't' represents time.
    *   'k' is the constant of proportionality.  If k > 0, it represents growth; if k < 0, it represents decay.

*   **Solution:** The general solution to this differential equation is:

    $\qquad y(t) = y_0e^{kt}$

    where:
    *   $y(t)$ is the amount at time 't'.
    *   $y_0$ is the initial amount (at t = 0).

*   **Applications:**
    *   **Population Growth:** Modeling the growth of populations (e.g., bacteria, animals).
    *   **Radioactive Decay:** Modeling the decay of radioactive substances.
    *   **Compound Interest:**  Modeling the growth of investments with continuous compounding.
    *   **Newton's Law of Cooling:**  Modeling the temperature change of an object as it cools or warms.

*   **Half-Life:** For exponential decay, the half-life is the time it takes for the quantity to reduce to half its initial value. If $T$ is the half-life, then:

    $\qquad e^{kT} = \frac{1}{2}$

    Taking the natural logarithm of both sides gives:

    $\qquad kT = \ln\left(\frac{1}{2}\right) = -\ln(2)$

    So,  $T = \frac{-\ln