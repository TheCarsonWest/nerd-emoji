
# [[AP Physics C Home]]
# AP Physics C: Representing Motion

Understanding how to represent motion is fundamental to kinematics, the study of motion without considering its causes. This topic focuses on using mathematical functions and graphical representations to describe an object's position, velocity, and acceleration over time.

## Key Concepts in Motion Representation

The primary quantities used to describe motion are position, velocity, and acceleration. These are all [[Scalars and Vectors|vector quantities]], meaning they have both magnitude and direction, although often in one-dimensional motion, we represent direction with a positive or negative sign.

For a deeper dive into these core concepts, refer to the [[Displacement, Velocity, and Acceleration]] notes page.

## Graphical Representations of Motion

Motion can be effectively visualized using graphs, which provide immediate insights into an object's behavior. The three primary types of graphs are:

### 1. Position-Time Graphs ($x(t)$)

A position-time graph plots an object's position ($x$) as a function of time ($t$).

*   **Slope**: The slope of a position-time graph at any point gives the object's **instantaneous velocity** ($v$).
    $$v = \frac{dx}{dt}$$
*   **Curvature**: The curvature of the graph indicates acceleration. A straight line means constant velocity (zero acceleration), while a curved line indicates changing velocity (non-zero acceleration).
*   **Interpretation Examples**:

| Graph Feature                 | Implication                     |
| :---------------------------- | :------------------------------ |
| Horizontal line               | Object is at rest ($v=0$)       |
| Straight, upward sloping line | Constant positive velocity      |
| Straight, downward sloping line | Constant negative velocity      |
| Curved, upward opening        | Positive acceleration           |
| Curved, downward opening      | Negative acceleration           |

### 2. Velocity-Time Graphs ($v(t)$)

A velocity-time graph plots an object's velocity ($v$) as a function of time ($t$).

*   **Slope**: The slope of a velocity-time graph at any point gives the object's **instantaneous acceleration** ($a$).
    $$a = \frac{dv}{dt}$$
*   **Area Under the Curve**: The area between the velocity-time graph and the time axis represents the **displacement** ($\Delta x$) of the object during that time interval.
    $$\Delta x = \int_{t_1}^{t_2} v(t) dt$$
*   **Interpretation Examples**:

| Graph Feature                 | Implication                       |
| :---------------------------- | :-------------------------------- |
| Horizontal line               | Constant velocity (zero acceleration) |
| Straight, upward sloping line | Constant positive acceleration    |
| Straight, downward sloping line | Constant negative acceleration    |
| Curved line                   | Changing acceleration             |

### 3. Acceleration-Time Graphs ($a(t)$)

An acceleration-time graph plots an object's acceleration ($a$) as a function of time ($t$).

*   **Area Under the Curve**: The area between the acceleration-time graph and the time axis represents the **change in velocity** ($\Delta v$) of the object during that time interval.
    $$\Delta v = \int_{t_1}^{t_2} a(t) dt$$
*   **Slope**: The slope of an acceleration-time graph (often called "jerk") is typically not directly analyzed in AP Physics C kinematics.

## Mathematical Relationships (Calculus Connections)

The relationships between position, velocity, and acceleration are fundamentally defined by calculus.

*   **Velocity from Position**: Velocity is the time derivative of position.
    $$v(t) = \frac{dx(t)}{dt}$$
*   **Acceleration from Velocity**: Acceleration is the time derivative of velocity.
    $$a(t) = \frac{dv(t)}{dt}$$
*   **Acceleration from Position**: Acceleration is the second time derivative of position.
    $$a(t) = \frac{d^2x(t)}{dt^2}$$
*   **Velocity from Acceleration**: The change in velocity is the integral of acceleration over time.
    $$\Delta v = v_f - v_i = \int_{t_i}^{t_f} a(t) dt$$
*   **Position from Velocity**: The change in position (displacement) is the integral of velocity over time.
    $$\Delta x = x_f - x_i = \int_{t_i}^{t_f} v(t) dt$$

These integral relationships are crucial for deriving the [[Representing Motion|kinematic equations for constant acceleration]] and for analyzing motion where acceleration is not constant.

## Analyzing Motion with Calculus

When dealing with more complex motion where acceleration (or even velocity) is a function of time, calculus provides the exact tools.

*   To find $v(t)$ from $x(t)$, differentiate $x(t)$.
*   To find $a(t)$ from $v(t)$, differentiate $v(t)$.
*   To find $v(t)$ from $a(t)$, integrate $a(t)$ with respect to $t$ (remembering to include the initial velocity as a constant of integration).
*   To find $x(t)$ from $v(t)$, integrate $v(t)$ with respect to $t$ (remembering to include the initial position as a constant of integration).

This integration and differentiation process allows for a complete description of motion given any one of the $x(t)$, $v(t)$, or $a(t)$ functions and appropriate initial conditions.