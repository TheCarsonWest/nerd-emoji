
# [[AP Physics C Home]]
# AP Physics C: Topic 1.2 - Displacement, Velocity, and Acceleration

In AP Physics C, we begin our study of [[Kinematics]], the description of motion without considering its causes. This topic lays the fundamental groundwork for understanding how objects move in one dimension.

## Position

Position ($\vec{x}$ or $\vec{r}$) describes an object's location relative to a chosen origin. It is a [[Scalars and Vectors|vector quantity]], meaning it has both magnitude and direction. In one dimension, we typically use the x-axis, so position is often denoted as $x$.

## Displacement

Displacement ($\Delta \vec{x}$ or $\Delta x$) is the change in an object's position. It is the straight-line distance and direction from the initial position to the final position.

*   **Definition**: The change in position.
*   **Formula**:
    $$\Delta x = x_f - x_i$$
    where $x_f$ is the final position and $x_i$ is the initial position.
*   **Vector Quantity**: Displacement is a vector. A positive $\Delta x$ indicates movement in the positive direction (e.g., right or up), and a negative $\Delta x$ indicates movement in the negative direction (e.g., left or down).
*   **Units**: Meters (m).
*   **Distinction from Distance**: Distance is the total path length traveled, always positive, and a scalar quantity. Displacement only depends on the start and end points. For example, if you walk 5m right and then 5m left, your total distance traveled is 10m, but your displacement is 0m.

## Velocity

Velocity describes the rate at which an object's position changes. It is a [[Scalars and Vectors|vector quantity]] with both magnitude and direction.

### [[Average Velocity]]

Average velocity ($\vec{v}_{avg}$ or $v_{avg}$) is the total displacement divided by the total time taken for that displacement.

*   **Formula**:
    $$v_{avg} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$
*   **Units**: Meters per second (m/s).

### [[Instantaneous Velocity]]

Instantaneous velocity ($\vec{v}$ or $v$) is the velocity of an object at a specific instant in time. It is defined as the limit of the average velocity as the time interval approaches zero.

*   **Calculus Definition**: Instantaneous velocity is the time derivative of the position function.
    $$v(t) = \frac{dx}{dt}$$
*   **Graphical Interpretation**: On a position-time graph, instantaneous velocity is the slope of the tangent line at any given point.
*   **Distinction from Speed**: Speed is the magnitude of velocity (i.e., how fast an object is moving without regard to direction) and is a scalar quantity. Instantaneous speed is the magnitude of instantaneous velocity.

## Acceleration

Acceleration describes the rate at which an object's velocity changes. It is a [[Scalars and Vectors|vector quantity]].

### [[Average Acceleration]]

Average acceleration ($\vec{a}_{avg}$ or $a_{avg}$) is the change in velocity divided by the time taken for that change.

*   **Formula**:
    $$a_{avg} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$
*   **Units**: Meters per second squared (m/s$^2$).

### [[Instantaneous Acceleration]]

Instantaneous acceleration ($\vec{a}$ or $a$) is the acceleration of an object at a specific instant in time.

*   **Calculus Definition**: Instantaneous acceleration is the time derivative of the velocity function, or the second time derivative of the position function.
    $$a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$
*   **Graphical Interpretation**: On a velocity-time graph, instantaneous acceleration is the slope of the tangent line at any given point.

## Connecting Position, Velocity, and Acceleration via Calculus

The relationships between position, velocity, and acceleration are fundamental in calculus-based physics.

| Quantity       | From Previous (Derivative)           | To Previous (Integral)                 |
| :------------- | :----------------------------------- | :------------------------------------- |
| **Velocity**   | $v(t) = \frac{dx}{dt}$               | $x(t) = \int v(t) dt + C$              |
| **Acceleration** | $a(t) = \frac{dv}{dt}$ or $a(t) = \frac{d^2x}{dt^2}$ | $v(t) = \int a(t) dt + C$              |

*   **Derivatives**:
    *   Taking the [[AP Calculus: Derivatives|derivative]] of the position function with respect to time gives the instantaneous velocity function.
    *   Taking the derivative of the velocity function with respect to time gives the instantaneous acceleration function.
*   **Integrals**:
    *   Taking the [[AP Calculus: Integrals|integral]] of the acceleration function with respect to time gives the instantaneous velocity function (plus an initial velocity constant).
    *   Taking the integral of the velocity function with respect to time gives the instantaneous position function (plus an initial position constant).
    *   These integrals represent the "area under the curve" on a graph.

## Graphical Analysis

Graphical representations are crucial for understanding motion:

*   **Position-Time (x-t) Graph**:
    *   The slope of the x-t graph at any point gives the **instantaneous velocity** ($v = dx/dt$).
    *   A straight line indicates constant velocity.
    *   A curved line indicates changing velocity (acceleration).
*   **Velocity-Time (v-t) Graph**:
    *   The slope of the v-t graph at any point gives the **instantaneous acceleration** ($a = dv/dt$).
    *   The area under the v-t graph between two time points gives the **displacement** ($\Delta x = \int v(t) dt$).
    *   A straight line indicates constant acceleration.
    *   A horizontal line indicates constant velocity (zero acceleration).
*   **Acceleration-Time (a-t) Graph**:
    *   The area under the a-t graph between two time points gives the **change in velocity** ($\Delta v = \int a(t) dt$).

Understanding these relationships is vital for solving kinematics problems in AP Physics C, especially those involving non-constant acceleration.