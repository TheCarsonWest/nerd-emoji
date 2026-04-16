
# [[AP Physics C Home]]
# AP Physics C: Topic 1.5 - Motion in Two or Three Dimensions

## Introduction

Motion in two or three dimensions extends the concepts of one-dimensional kinematics by incorporating the vector nature of position, velocity, and acceleration across multiple axes. This topic is fundamental to understanding complex movements like projectile motion, orbital mechanics, and more generally, any motion not confined to a single straight line. It builds directly upon the principles introduced in [[Displacement, Velocity, and Acceleration]] and relies heavily on the use of [[Scalars and Vectors]].

## Vector Nature of Motion

In two or three dimensions, physical quantities like position, displacement, velocity, and acceleration are represented by vectors. This means they have both magnitude and direction. We typically use a Cartesian coordinate system (x, y, z) to describe these vectors.

### Position Vector

The position vector $\vec{r}$ describes an object's location in space relative to a chosen origin.
In 2D: $$\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j}$$
In 3D: $$\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$
Where $x(t)$, $y(t)$, and $z(t)$ are the coordinates as functions of time, and $\hat{i}$, $\hat{j}$, $\hat{k}$ are unit vectors along the x, y, and z axes, respectively.

### Displacement Vector

The displacement vector $\Delta\vec{r}$ represents the change in an object's position from an initial position $\vec{r}_i$ to a final position $\vec{r}_f$.
$$\Delta\vec{r} = \vec{r}_f - \vec{r}_i = (x_f - x_i)\hat{i} + (y_f - y_i)\hat{j} + (z_f - z_i)\hat{k}$$

### Velocity Vector

#### Average Velocity
The average velocity $\vec{v}_{avg}$ is the ratio of the displacement vector to the time interval $\Delta t$.
$$\vec{v}_{avg} = \frac{\Delta\vec{r}}{\Delta t}$$

#### Instantaneous Velocity
The instantaneous velocity $\vec{v}(t)$ is the derivative of the position vector with respect to time. It is a vector tangent to the path of motion at any given point.
$$\vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k} = v_x(t)\hat{i} + v_y(t)\hat{j} + v_z(t)\hat{k}$$
The magnitude of the instantaneous velocity is called the speed: $v = |\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$.

### Acceleration Vector

#### Average Acceleration
The average acceleration $\vec{a}_{avg}$ is the ratio of the change in velocity vector to the time interval $\Delta t$.
$$\vec{a}_{avg} = \frac{\Delta\vec{v}}{\Delta t}$$

#### Instantaneous Acceleration
The instantaneous acceleration $\vec{a}(t)$ is the derivative of the velocity vector with respect to time, or the second derivative of the position vector.
$$\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{dv_x}{dt}\hat{i} + \frac{dv_y}{dt}\hat{j} + \frac{dv_z}{dt}\hat{k} = a_x(t)\hat{i} + a_y(t)\hat{j} + a_z(t)\hat{k}$$
$$\vec{a}(t) = \frac{d^2\vec{r}}{dt^2}$$

## Kinematic Equations for Constant Acceleration

When acceleration is constant, the motion can be analyzed independently in each dimension. The one-dimensional kinematic equations apply to each component of motion.

| Component Equations for Constant Acceleration |
| :-------------------------------------------- |
| $v_x = v_{x0} + a_xt$                         |
| $x = x_0 + v_{x0}t + \frac{1}{2}a_xt^2$       |
| $v_x^2 = v_{x0}^2 + 2a_x(x - x_0)$            |
| $v_y = v_{y0} + a_yt$                         |
| $y = y_0 + v_{y0}t + \frac{1}{2}a_yt^2$       |
| $v_y^2 = v_{y0}^2 + 2a_y(y - y_0)$            |
| $v_z = v_{z0} + a_zt$                         |
| $z = z_0 + v_{z0}t + \frac{1}{2}a_zt^2$       |
| $v_z^2 = v_{z0}^2 + 2a_z(z - z_0)$            |

These component equations can be combined vectorially:
$$\vec{v} = \vec{v}_0 + \vec{a}t$$
$$\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$$

### Projectile Motion

[[Projectile Motion]] is a classic example of motion in two dimensions under constant acceleration, where the acceleration is due to gravity (neglecting air resistance). Typically, $a_x = 0$ and $a_y = -g$ (if y is upward).

## Relative Motion

Understanding motion often requires specifying a [[Reference Frames and Relative Motion]]. In 2D/3D, the velocity of an object A relative to a reference frame B is given by:
$$\vec{v}_{AB} = \vec{v}_{AC} + \vec{v}_{CB}$$
where C is an intermediate reference frame.

## Summary of Key Concepts and Equations

| Concept           | Description                                                                                                                                                                                                            | Equation (2D)                                                                                                              |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| Position          | Vector from origin to object's location.                                                                                                                                                                               | $\vec{r} = x\hat{i} + y\hat{j}$                                                                                          |
| Displacement      | Change in position vector.                                                                                                                                                                                             | $\Delta\vec{r} = \vec{r}_f - \vec{r}_i$                                                                                   |
| Instantaneous Velocity | Time derivative of position vector. Direction is tangent to path.                                                                                                                                                      | $\vec{v} = \frac{d\vec{r}}{dt} = v_x\hat{i} + v_y\hat{j}$                                                                 |
| Instantaneous Acceleration | Time derivative of velocity vector (second derivative of position vector).                                                                                                                                             | $\vec{a} = \frac{d\vec{v}}{dt} = a_x\hat{i} + a_y\hat{j}$                                                                 |
| Constant Acceleration (Vector Form) | If $\vec{a}$ is constant, treat components independently. | $\vec{v} = \vec{v}_0 + \vec{a}t$ <br> $\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$ |