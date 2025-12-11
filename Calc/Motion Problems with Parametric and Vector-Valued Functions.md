
# [[Calc Home]]
# AP Calculus BC Notes: Motion Problems with Parametric and Vector-Valued Functions

This topic extends motion analysis from single-variable calculus to objects moving along paths defined parametrically or by vector-valued functions, typically in a 2D plane. It integrates concepts from [[Differentiating Parametric Equations]] and [[Calculus and Vector-Valued Functions]].

## 1. Position, Velocity, and Acceleration

For a particle moving in the $xy$-plane, its position at time $t$ can be described by:
*   **Parametric Equations:** $x = f(t)$ and $y = g(t)$
*   **Vector-Valued Function:** $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ or $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$

### 1.1. Velocity Vector
The velocity vector describes the instantaneous rate of change of position. It is the derivative of the position vector with respect to time.

If $\mathbf{r}(t) = \langle x(t), y(t) \rangle$, then the velocity vector is:
$$ \mathbf{v}(t) = \mathbf{r}'(t) = \langle x'(t), y'(t) \rangle = \left\langle \frac{dx}{dt}, \frac{dy}{dt} \right\rangle $$
Here, $x'(t)$ is the horizontal component of velocity, and $y'(t)$ is the vertical component of velocity.

### 1.2. Acceleration Vector
The acceleration vector describes the instantaneous rate of change of the velocity vector. It is the derivative of the velocity vector (or the second derivative of the position vector) with respect to time.

If $\mathbf{v}(t) = \langle x'(t), y'(t) \rangle$, then the acceleration vector is:
$$ \mathbf{a}(t) = \mathbf{v}'(t) = \mathbf{r}''(t) = \langle x''(t), y''(t) \rangle = \left\langle \frac{d^2x}{dt^2}, \frac{d^2y}{dt^2} \right\rangle $$

## 2. Speed

Speed is the magnitude of the velocity vector. It is a scalar quantity and is always non-negative.

For $\mathbf{v}(t) = \langle x'(t), y'(t) \rangle$, the speed is given by:
$$ \text{Speed} = ||\mathbf{v}(t)|| = \sqrt{(x'(t))^2 + (y'(t))^2} $$

**Key Point:** If the particle is at rest, its speed is 0, which implies $x'(t) = 0$ and $y'(t) = 0$.

## 3. Direction of Motion

The direction of motion at any point is given by the direction of the velocity vector. The slope of the tangent line to the path at time $t$ is given by:
$$ \frac{dy}{dx} = \frac{dy/dt}{dx/dt} $$
provided $dx/dt \neq 0$. This is a direct application of [[Differentiating Parametric Equations]].

## 4. Total Distance Traveled (Arc Length)

The total distance a particle travels along its path from time $t=a$ to $t=b$ is the arc length of the path over that interval. This is calculated by integrating the speed function.

$$ \text{Total Distance} = \int_a^b ||\mathbf{v}(t)|| \, dt = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt $$
This formula is consistent with the general formula for [[Arc Lengths of Parametric Equations]].

## 5. Displacement

Displacement refers to the net change in position from an initial time $t=a$ to a final time $t=b$. It is a vector quantity.

If the initial position is $\mathbf{r}(a) = \langle x(a), y(a) \rangle$ and the final position is $\mathbf{r}(b) = \langle x(b), y(b) \rangle$, then the displacement vector is:
$$ \Delta \mathbf{r} = \mathbf{r}(b) - \mathbf{r}(a) = \left\langle \int_a^b x'(t) \, dt, \int_a^b y'(t) \, dt \right\rangle $$
The net change in $x$-position is $\int_a^b x'(t) \, dt = x(b) - x(a)$.
The net change in $y$-position is $\int_a^b y'(t) \, dt = y(b) - y(a)$.

## 6. Integrals to Find Position

If you are given the initial position $\mathbf{r}(t_0) = \langle x(t_0), y(t_0) \rangle$ and the velocity vector $\mathbf{v}(t) = \langle x'(t), y'(t) \rangle$, you can find the position at any time $t$ using integration:

$$ x(t) = x(t_0) + \int_{t_0}^t x'(u) \, du $$
$$ y(t) = y(t_0) + \int_{t_0}^t y'(u) \, du $$
Thus,
$$ \mathbf{r}(t) = \left\langle x(t_0) + \int_{t_0}^t x'(u) \, du, y(t_0) + \int_{t_0}^t y'(u) \, du \right\rangle $$

Similarly, if given initial velocity and acceleration, you can integrate acceleration to find velocity.

## 7. Describing Motion

| Quantity            | Description                                             | Vector/Scalar | Formula                                                                  |
| :------------------ | :------------------------------------------------------ | :------------ | :----------------------------------------------------------------------- |
| **Position**        | Location of the particle at time $t$.                 | Vector        | $\mathbf{r}(t) = \langle x(t), y(t) \rangle$                             |
| **Velocity**        | Rate of change of position; tangent to the path.      | Vector        | $\mathbf{v}(t) = \langle x'(t), y'(t) \rangle$                           |
| **Acceleration**    | Rate of change of velocity.                             | Vector        | $\mathbf{a}(t) = \langle x''(t), y''(t) \rangle$                         |
| **Speed**           | Magnitude of the velocity vector.                       | Scalar        | $||\mathbf{v}(t)|| = \sqrt{(x'(t))^2 + (y'(t))^2}$                        |
| **Slope of Path**   | Direction of motion (tangent line to path).           | Scalar        | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$                                    |
| **Total Distance**  | Length of path traveled.                                | Scalar        | $\int_a^b ||\mathbf{v}(t)|| \, dt$                                        |
| **Displacement**    | Net change in position (vector from start to end).      | Vector        | $\mathbf{r}(b) - \mathbf{r}(a)$                                          |

## [[When is a Particle Moving Up/Down, Left/Right?]]
A particle moves **right** when $x'(t) > 0$.
A particle moves **left** when $x'(t) < 0$.
A particle moves **up** when $y'(t) > 0$.
A particle moves **down** when $y'(t) < 0$.

A particle stops moving horizontally when $x'(t) = 0$.
A particle stops moving vertically when $y'(t) = 0$.

## [[Particle Direction Change]]
For a particle to change horizontal direction, $x'(t)$ must change sign.
For a particle to change vertical direction, $y'(t)$ must change sign.
For a particle to change direction along its path, its velocity vector must point in a new general direction. This typically involves at least one of $x'(t)$ or $y'(t)$ changing sign, or both reversing direction.

## [[Projectile Motion]]
Projectile motion often involves parametric equations with constant acceleration due to gravity.
If an object is launched from height $h$ with initial velocity $\mathbf{v}_0 = \langle v_{0x}, v_{0y} \rangle = \langle ||\mathbf{v}_0||\cos\theta, ||\mathbf{v}_0||\sin\theta \rangle$, where $\theta$ is the launch angle, and acceleration due to gravity is $a_y = -g$:

*   $\mathbf{a}(t) = \langle 0, -g \rangle$
*   $\mathbf{v}(t) = \langle v_{0x}, v_{0y} - gt \rangle$
*   $\mathbf{r}(t) = \langle x_0 + v_{0x}t, y_0 + v_{0y}t - \frac{1}{2}gt^2 \rangle$

Here, $x_0$ and $y_0$ are initial horizontal and vertical positions (often $x_0=0, y_0=h$).