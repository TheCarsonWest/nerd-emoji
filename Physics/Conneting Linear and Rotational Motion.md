# [[AP Physics Home]]
# AP Physics: Connecting Linear and Rotational Motion

## Introduction

Many physical systems involve both linear and rotational motion. Understanding how these two types of motion are related is crucial for analyzing the behavior of objects that rotate while also translating, or for describing the linear motion of a point on a rotating object. This page explores the fundamental connections between linear and rotational kinematic and dynamic quantities, particularly for rigid bodies and points on rotating objects. A good foundation in [[Circular Motion]] is helpful here.

## Kinematic Relationships

For a point on a rigid body rotating about a fixed axis, or for an object rolling without slipping, there are direct relationships between linear and angular kinematic quantities. The radius $r$ (distance from the axis of rotation) plays a key role in these conversions.

### Displacement, Velocity, and Acceleration

| Linear Quantity | Rotational Quantity | Relationship |
| :-------------- | :------------------ | :----------- |
| Position ($s$ or $x$) | Angular Position ($\theta$) | $s = r\theta$ |
| Tangential Velocity ($v_t$) | Angular Velocity ($\omega$) | $v_t = r\omega$ |
| Tangential Acceleration ($a_t$) | Angular Acceleration ($\alpha$) | $a_t = r\alpha$ |

**Equations:**
*   **Linear Displacement:** $s = r\theta$
    *   Where $s$ is the arc length (linear distance), $r$ is the radius, and $\theta$ is the angular displacement in radians.
*   **Tangential Velocity:** $v_t = r\omega$
    *   Where $v_t$ is the linear velocity tangent to the circular path, and $\omega$ is the angular velocity in rad/s.
*   **Tangential Acceleration:** $a_t = r\alpha$
    *   Where $a_t$ is the linear acceleration tangent to the circular path, and $\alpha$ is the angular acceleration in rad/s$^2$.

It's important to remember that these relationships apply to the *tangential* components of linear motion. For objects undergoing circular motion, there is also a centripetal (or radial) acceleration, $a_c = v_t^2/r = r\omega^2$, which is perpendicular to $a_t$. The total linear acceleration is the vector sum of these components.

## Rolling Without Slipping

A common and important application of connecting linear and rotational motion is the concept of [[Rolling]]. When an object rolls without slipping, there's a specific relationship between its translational speed and its rotational speed.

**Key Condition:** For an object rolling without slipping, the point of contact between the object and the surface is instantaneously at rest relative to the surface.

This implies that the linear speed of the center of mass ($v_{CM}$) is directly related to its angular speed ($\omega$) and radius ($R$):

$
v_{CM} = R\omega
$

Similarly, for acceleration:

$
a_{CM} = R\alpha
$

Where $R$ is the radius of the rolling object. This condition is crucial for analyzing the dynamics of rolling objects, as it links their translational kinematics to their rotational kinematics.

## Rotational and Translational Kinetic Energy

When an object performs both translational and rotational motion, its total kinetic energy is the sum of its translational kinetic energy (associated with the motion of its center of mass) and its rotational kinetic energy (associated with its rotation about its center of mass).

$
K_{total} = K_{translational} + K_{rotational}
$

$
K_{total} = \frac{1}{2}mv_{CM}^2 + \frac{1}{2}I_{CM}\omega^2
$

Where:
*   $m$ is the mass of the object.
*   $v_{CM}$ is the linear speed of the center of mass.
*   $I_{CM}$ is the moment of inertia about the center of mass.
*   $\omega$ is the angular speed of rotation about the center of mass.

This equation is fundamental for applying the [[Conservation of Energy]] principle to objects undergoing both translation and rotation, such as a ball rolling down an incline.

## Dynamic Relationships (Brief Mention)

Just as kinematic quantities are connected, so are dynamic quantities:
*   **Force and Torque:** Torque ($\tau$) is the rotational analog of force. For a force $F$ applied at a distance $r$ from the pivot, $\tau = rF\sin\phi$.
*   **Linear Momentum and Angular Momentum:** [[Linear Momentum]] ($p=mv$) has its rotational counterpart in [[Angular Momentum and Angular Impulse]] ($L=I\omega$).
*   **Newton's Second Law:** $F_{net} = ma$ for linear motion, and $\tau_{net} = I\alpha$ for rotational motion. These can be interconnected in problems involving rolling or hinged systems.

Understanding these connections allows for a comprehensive analysis of systems where both linear and rotational dynamics are at play.