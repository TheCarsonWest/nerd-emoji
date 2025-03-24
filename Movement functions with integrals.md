# [[Calc home]]
# Movement Functions with Integrals: AP Calculus AB Rundown

This document provides a concise overview of movement functions and their relationship to integrals, as relevant to AP Calculus AB.

## Position, Velocity, and Acceleration

These three concepts are fundamental when dealing with movement.  They are related through differentiation and integration.

*   **Position:** Denoted by $s(t)$ or $x(t)$.  It represents the location of an object at a given time $t$.

*   **Velocity:** Denoted by $v(t)$.  It represents the rate of change of position with respect to time.  Velocity is the derivative of position:

$$v(t) = \frac{ds}{dt} = s'(t)$$

*   **Acceleration:** Denoted by $a(t)$.  It represents the rate of change of velocity with respect to time.  Acceleration is the derivative of velocity (and the second derivative of position):

$$a(t) = \frac{dv}{dt} = v'(t) = s''(t)$$

## Integration and Movement

Integration allows us to move "backwards" in the position-velocity-acceleration hierarchy.  Specifically:

*   **Finding Velocity from Acceleration:**  Given the acceleration function $a(t)$ and the initial velocity $v(0)$, we can find the velocity function $v(t)$ by integrating $a(t)$:

$$v(t) = v(0) + \int_{0}^{t} a(\tau) \, d\tau$$

Note that we are using $\tau$ as the variable of integration here to avoid confusion with the upper limit, $t$. [[Understanding Dummy Variables]]

*   **Finding Position from Velocity:** Given the velocity function $v(t)$ and the initial position $s(0)$, we can find the position function $s(t)$ by integrating $v(t)$:

$$s(t) = s(0) + \int_{0}^{t} v(\tau) \, d\tau$$

## Displacement vs. Total Distance

This is a critical distinction.

*   **Displacement:** The change in position of an object over a given time interval.  It's calculated by integrating the velocity function over that interval:

$$\text{Displacement} = \int_{a}^{b} v(t) \, dt = s(b) - s(a)$$

Displacement can be positive, negative, or zero.  A positive displacement means the object moved to the right (or up, depending on the context), a negative displacement means it moved to the left (or down), and a zero displacement means it ended up at the same position where it started.

*   **Total Distance:** The total length of the path traveled by an object over a given time interval.  It's calculated by integrating the *absolute value* of the velocity function over that interval:

$$\text{Total Distance} = \int_{a}^{b} |v(t)| \, dt$$

The absolute value ensures that we're always adding up positive distances, regardless of the direction of movement. To evaluate this integral, you'll need to determine where $v(t)$ is positive and negative on the interval $[a, b]$.  Then, split the integral into intervals where $v(t)$ has a constant sign, and negate $v(t)$ where it's negative:

$$\int_{a}^{b} |v(t)| \, dt = \int_{a}^{c} v(t) \, dt - \int_{c}^{d} v(t) \, dt + \int_{d}^{b} v(t) \, dt$$

Where $v(t) \ge 0$ on $[a, c]$, $v(t) \le 0$ on $[c, d]$, and $v(t) \ge 0$ on $[d, b]$.  This means $v(c) = v(d) = 0$.

## Average Velocity and Average Speed

*   **Average Velocity:** The displacement divided by the time interval:

$$\text{Average Velocity} = \frac{s(b) - s(a)}{b - a} = \frac{1}{b - a} \int_{a}^{b} v(t) \, dt$$

This is also the average value of the velocity function over the interval $[a, b]$. [[Average of a function]]

*   **Average Speed:** The total distance traveled divided by the time interval:

$$\text{Average Speed} = \frac{\text{Total Distance}}{b - a} = \frac{1}{b - a} \int_{a}^{b} |v(t)| \, dt$$

## Key Concepts and Cautions

*   **Initial Conditions:** Don't forget to use initial conditions ($s(0)$ and $v(0)$) when finding position and velocity functions. These are crucial for determining the constant of integration.

*   **Units:** Pay attention to the units of measurement (e.g., meters, seconds, meters/second, meters/second²).

*   **Direction:** Velocity is a vector quantity (it has both magnitude and direction). Speed is a scalar quantity (it only has magnitude).  The sign of the velocity indicates direction.

*   **When $v(t) = 0$:**  When the velocity is zero, the object is momentarily at rest.  This is often a turning point, where the object changes direction.  Finding these points is essential for calculating total distance.
[[Finding Roots]]

## [[Understanding Dummy Variables]]
In the equations:
$$v(t) = v(0) + \int_{0}^{t} a(\tau) \, d\tau$$
$$s(t) = s(0) + \int_{0}^{t} v(\tau) \, d\tau$$

The variable $\tau$ is a "dummy variable".  It's just a placeholder variable used within the integral.  The important thing is that the *limits* of integration are in terms of time ($0$ to $t$).  The variable of integration inside the integral ($a(\tau)$ or $v(\tau)$) doesn't affect the final result, as long as it's consistent with the differential ($d\tau$). We use a different variable than $t$ to avoid confusion between the upper limit of integration and the variable in the function we are defining.

## [[Average of a function]]
The Average Value Theorem states that if a function $f(x)$ is continuous on the closed interval $[a, b]$, then there exists a number $c$ in the interval $(a, b)$ such that:

$$f(c) = \frac{1}{b-a} \int_a^b f(x) \, dx$$

In the context of velocity, the average velocity over the interval $[a,b]$ is the average value of the velocity function $v(t)$ over that interval.


To find the roots (or zeros) of a function, such