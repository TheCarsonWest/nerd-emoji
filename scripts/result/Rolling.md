# [[AP Physics Home]]
# AP Physics: Topic 6.5 - Rolling

## 1. Introduction to Rolling Motion

Rolling is a common type of motion that combines both **translation** (movement of the center of mass) and **rotation** (spinning about an axis). When an object rolls, its center of mass moves linearly, while every point on the object simultaneously rotates around the center of mass. This means the object's total kinetic energy is a sum of its translational kinetic energy and rotational kinetic energy.

## 2. Condition for Pure Rolling

Pure rolling, or rolling without slipping, is a critical concept. It occurs when the point of contact between the rolling object and the surface is instantaneously at rest relative to the surface. This implies a direct relationship between the translational velocity of the center of mass and the angular velocity of the object.

For pure rolling:
$ v_{CM} = R\omega $
where:
*   $v_{CM}$ is the linear velocity of the center of mass.
*   $R$ is the radius of the rolling object.
*   $\omega$ is the angular velocity.

Similarly, for pure rolling, the translational acceleration of the center of mass ($a_{CM}$) is related to the angular acceleration ($\alpha$) by:
$ a_{CM} = R\alpha $

If $v_{CM} > R\omega$, the object is slipping forward. If $v_{CM} < R\omega$, the object is skidding or slipping backward.

## 3. Kinematics of Pure Rolling

Consider a point on the circumference of a wheel rolling without slipping:

*   **Velocity at the Top:** The velocity of the top point is twice the velocity of the center of mass ($v_{top} = 2v_{CM}$).
*   **Velocity at the Bottom:** The velocity of the bottom point (point of contact) is instantaneously zero relative to the surface ($v_{bottom} = 0$). This is the definition of pure rolling.
*   **Velocity at the Center of Mass:** The velocity of the center of mass is $v_{CM}$.

This can be visualized as a superposition of a purely translational motion (all points move with $v_{CM}$) and a purely rotational motion (points rotate with $R\omega$).

## 4. Dynamics of Rolling

To analyze the dynamics of rolling, we use Newton's Second Law for both translational and rotational motion.

1.  **Translational Motion (along the direction of motion):**
    $ \sum F_{x} = M a_{CM} $
    where $M$ is the total mass of the object.

2.  **Rotational Motion (about the center of mass):**
    $ \sum \tau = I \alpha $
    where $I$ is the [[Rotational Inertia]] of the object about its center of mass.

**Friction's Role in Rolling:**
For an object to roll, there must be a force that provides the torque needed for rotation. This is often **static friction**.
*   If an object rolls down an incline, static friction acts **up the incline** to prevent slipping and cause rotation.
*   If an object is pulled horizontally by a force $F$ at its center of mass and rolls without slipping, static friction acts **backward** to provide the necessary torque.

It's crucial to remember that if pure rolling occurs, the static friction force does **no work** because the point of application of the force (the point of contact) is instantaneously at rest.

## 5. Kinetic Energy of Rolling Objects

The total kinetic energy ($K_{total}$) of a rolling object is the sum of its translational kinetic energy ($K_{trans}$) and its rotational kinetic energy ($K_{rot}$).

$ K_{total} = K_{trans} + K_{rot} $
$ K_{total} = \frac{1}{2} M v_{CM}^2 + \frac{1}{2} I_{CM} \omega^2 $

For pure rolling, we can substitute $\omega = v_{CM}/R$:

$ K_{total} = \frac{1}{2} M v_{CM}^2 + \frac{1}{2} I_{CM} \left(\frac{v_{CM}}{R}\right)^2 $
$ K_{total} = \frac{1}{2} v_{CM}^2 \left(M + \frac{I_{CM}}{R^2}\right) $

This equation shows that the total kinetic energy depends on both the object's mass and its moment of inertia. Objects with larger moments of inertia (relative to their mass and radius) will have a larger fraction of their kinetic energy stored as rotational energy.

## 6. Rolling Down an Incline

When different objects (e.g., solid cylinder, hollow cylinder, sphere) roll down an incline without slipping, they all have the same gravitational potential energy at the top. However, they will reach the bottom with different speeds due to their different [[Rotational Inertia]].

By [[Conservation of Energy]]:
$ PE_{initial} + K_{initial} = PE_{final} + K_{final} $
If starting from rest ($K_{initial}=0$) at height $h$ ($PE_{final}=0$ at bottom):
$ Mgh = \frac{1}{2} M v_{CM}^2 + \frac{1}{2} I_{CM} \omega^2 $
Using $I_{CM} = kMR^2$ (where $k$ is a constant based on the object's shape) and $\omega = v_{CM}/R$:
$ Mgh = \frac{1}{2} M v_{CM}^2 + \frac{1}{2} (kMR^2) \left(\frac{v_{CM}}{R}\right)^2 $
$ Mgh = \frac{1}{2} M v_{CM}^2 + \frac{1}{2} kM v_{CM}^2 $
$ Mgh = \frac{1}{2} M v_{CM}^2 (1+k) $
Solving for $v_{CM}$:
$ v_{CM} = \sqrt{\frac{2gh}{1+k}} $

| Object           | Rotational Inertia ($I_{CM}$) | $k$ value | $v_{CM}$ at bottom |
| :--------------- | :----------------------------- | :-------- | :----------------- |
| Hoop/Thin Ring   | $MR^2$                         | 1         | $\sqrt{gh}$        |
| Solid Cylinder   | $\frac{1}{2}MR^2$              | $\frac{1}{2}$ | $\sqrt{\frac{4}{3}gh}$ |
| Solid Sphere     | $\frac{2}{5}MR^2$              | $\frac{2}{5}$ | $\sqrt{\frac{10}{7}gh}$ |

From the table, the solid sphere (smallest $k$) will have the largest $v_{CM}$ and thus reach the bottom first, followed by the solid cylinder, and then the hoop. This demonstrates how the distribution of mass affects the rolling motion.