# [[AP Physics Home]]
# AP Physics 1.5: Vectors and Motion in Two Dimensions

This page expands on the concept of [[Scalars and Vectors in One Dimension]] to analyze motion in a plane (two dimensions), a fundamental skill for understanding more complex physics problems.

## 1. Introduction to Vectors in 2D

In two dimensions, a vector quantity requires both magnitude and direction, often represented by an arrow on a coordinate plane. The direction is typically specified by an angle relative to a positive axis (e.g., positive x-axis).

### Components of a Vector
Any vector $\vec{A}$ can be broken down into its perpendicular components along the x and y axes. This is crucial for simplifying vector operations.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the positive x-axis:
*   **x-component:** $A_x = A \cos \theta$
*   **y-component:** $A_y = A \sin \theta$

Conversely, if you have the components $A_x$ and $A_y$:
*   **Magnitude:** $A = \sqrt{A_x^2 + A_y^2}$
*   **Direction (angle):** $\theta = \tan^{-1}\left(\frac{A_y}{A_x}\right)$ (Careful with quadrant for $\theta$)

## 2. Vector Operations

Performing operations like addition, subtraction, and scalar multiplication on vectors in two dimensions is most straightforward using their components.

### Vector Addition
To add two vectors $\vec{A}$ and $\vec{B}$, add their corresponding components:
$ \vec{R} = \vec{A} + \vec{B} $
$ R_x = A_x + B_x $
$ R_y = A_y + B_y $
Then find the magnitude and direction of $\vec{R}$ from $R_x$ and $R_y$.

### Vector Subtraction
To subtract vector $\vec{B}$ from $\vec{A}$, subtract their components:
$ \vec{D} = \vec{A} - \vec{B} = \vec{A} + (-\vec{B}) $
$ D_x = A_x - B_x $
$ D_y = A_y - B_y $
Note that subtracting a vector is equivalent to adding its negative (same magnitude, opposite direction).

### Scalar Multiplication
Multiplying a vector $\vec{A}$ by a scalar $c$:
$ c\vec{A} = (cA_x, cA_y) $
The magnitude changes by a factor of $|c|$, and the direction reverses if $c$ is negative.

## 3. Position, Velocity, and Acceleration in 2D

The definitions of position, velocity, and acceleration extend directly from one dimension to two by considering their x and y components independently.

### Position Vector
A particle's position is given by a position vector $\vec{r}$ from the origin:
$ \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} $
where $\hat{i}$ and $\hat{j}$ are unit vectors along the x and y axes, respectively.

### Displacement Vector
The change in position is the displacement vector $\Delta \vec{r}$:
$ \Delta \vec{r} = \vec{r}_f - \vec{r}_i = (x_f - x_i)\hat{i} + (y_f - y_i)\hat{j} = \Delta x \hat{i} + \Delta y \hat{j} $

### Velocity Vector
[[Representing Motion]] in 2D involves the velocity vector, which is always tangent to the path of motion.
*   **Average Velocity:**
    $ \vec{v}_{avg} = \frac{\Delta \vec{r}}{\Delta t} = \frac{\Delta x}{\Delta t}\hat{i} + \frac{\Delta y}{\Delta t}\hat{j} = v_{x,avg}\hat{i} + v_{y,avg}\hat{j} $
*   **Instantaneous Velocity:**
    $ \vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} = v_x(t)\hat{i} + v_y(t)\hat{j} $
    The magnitude of the instantaneous velocity is the speed: $v = \sqrt{v_x^2 + v_y^2}$.

### Acceleration Vector
*   **Average Acceleration:**
    $ \vec{a}_{avg} = \frac{\Delta \vec{v}}{\Delta t} = \frac{\Delta v_x}{\Delta t}\hat{i} + \frac{\Delta v_y}{\Delta t}\hat{j} = a_{x,avg}\hat{i} + a_{y,avg}\hat{j} $
*   **Instantaneous Acceleration:**
    $ \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{dv_x}{dt}\hat{i} + \frac{dv_y}{dt}\hat{j} = a_x(t)\hat{i} + a_y(t)\hat{j} $
    Acceleration can change both the magnitude and direction of the velocity vector.

## 4. Kinematics in Two Dimensions (Constant Acceleration)

When acceleration is constant, the motion in the x and y directions can be analyzed independently using the one-dimensional kinematic equations. This is a powerful concept.

| Kinematic Equation | X-Component | Y-Component |
| :----------------- | :---------- | :---------- |
| Velocity-Time      | $v_x = v_{0x} + a_x t$ | $v_y = v_{0y} + a_y t$ |
| Position-Time      | $x = x_0 + v_{0x} t + \frac{1}{2} a_x t^2$ | $y = y_0 + v_{0y} t + \frac{1}{2} a_y t^2$ |
| Velocity-Position  | $v_x^2 = v_{0x}^2 + 2 a_x (x - x_0)$ | $v_y^2 = v_{0y}^2 + 2 a_y (y - y_0)$ |

Common applications include [[Projectile Motion]] where $a_x = 0$ and $a_y = -g$ (assuming positive y is upward). The time '$t$' is the common link between the x and y motions.

This independent analysis of components also forms the basis for understanding more complex topics like [[Circular Motion]].