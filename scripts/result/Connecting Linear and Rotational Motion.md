
# [[AP Physics C Home]]
# AP Physics C: Connecting Linear and Rotational Motion

In AP Physics C: Mechanics, understanding how translational (linear) motion relates to rotational motion is fundamental to analyzing complex systems. This connection is primarily dictated by the radius of rotation $r$.

## The Fundamental Relationships

When an object moves in a circular path or rotates about an axis, the linear variables (position, velocity, and acceleration) are linked to their angular counterparts (angle, angular velocity, and angular acceleration).

The linear arc length $s$, tangential velocity $v$, and tangential acceleration $a_t$ are related to the angular displacement $\theta$, angular velocity $\omega$, and angular acceleration $\alpha$ by the radius $r$:

| Linear Variable | Angular Variable | Relationship |
| :--- | :--- | :--- |
| Arc Length ($s$) | Angular Displacement ($\theta$) | $s=r\theta$ |
| Tangential Velocity ($v$) | Angular Velocity ($\omega$) | $v=r\omega$ |
| Tangential Acceleration ($a_t$) | Angular Acceleration ($\alpha$) | $a_t=r\alpha$ |

*Note: In these equations, $\theta$ must be in radians.*

## Velocity Components

When an object rotates, every point on the rigid body has the same angular velocity $\omega$, but points at different distances from the center have different linear speeds. 

The tangential velocity vector is always perpendicular to the radial vector pointing from the axis of rotation. If an object is not just rotating but also moving linearly (like a wheel rolling on the ground), we use these relations to describe the motion of the center of mass. See [[Rolling]] for a deeper dive into this specific case.

## Acceleration Components

It is crucial to distinguish between tangential and radial (centripetal) acceleration:

1.  **Tangential Acceleration ($a_t$):** This component is responsible for changing the *speed* of the object. It is defined as:
    $$a_t=r\alpha$$
2.  **Radial (Centripetal) Acceleration ($a_r$ or $a_c$):** This component is responsible for changing the *direction* of the velocity vector, keeping the object in a circular path. It is defined as:
    $$a_r=\frac{v^2}{r}=r\omega^2$$

The total linear acceleration vector is the vector sum of these two components:
$$\vec{a}_{total} = \vec{a}_t + \vec{a}_r$$

Since these two components are perpendicular, the magnitude of the total linear acceleration is:
$$a_{total}=\sqrt{a_t^2 + a_r^2}$$

## Why It Matters
These connections allow us to bridge the gap between [[Rotational Kinematics]] and standard linear kinematics. By converting linear forces and velocities into their rotational equivalents (or vice-versa), we can solve problems involving systems like pulleys, gears, and rotating rigid bodies using Newton's laws. For an in-depth look at how these motions interact with forces, review [[Newtons Second Law in Rotational Form]].