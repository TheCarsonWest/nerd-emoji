
# [[AP Physics C Home]]
# Topic 6.1: Rotational Kinetic Energy

## Introduction
In classical mechanics, kinetic energy is the energy an object possesses due to its motion. While we previously studied the kinetic energy of objects moving linearly ($K = \frac{1}{2}mv^2$), objects that rotate about an axis also possess kinetic energy. This energy is derived from the individual motion of every particle that makes up the rotating rigid body.

## Deriving Rotational Kinetic Energy
Consider a rigid object rotating about a fixed axis with an angular velocity $\omega$. We can imagine this object as a collection of many small point masses $m_i$, each at a distance $r_i$ from the axis of rotation.

The linear speed of any specific particle $i$ is given by $v_i = r_i\omega$. The kinetic energy of this individual particle is:
$$K_i = \frac{1}{2}m_i v_i^2 = \frac{1}{2}m_i(r_i\omega)^2 = \frac{1}{2}m_i r_i^2 \omega^2$$

To find the total kinetic energy of the rotating body, we sum the kinetic energies of all particles:
$$K_{rot} = \sum \frac{1}{2} m_i r_i^2 \omega^2 = \frac{1}{2} \left( \sum m_i r_i^2 \right) \omega^2$$

Since the term $\sum m_i r_i^2$ is defined as the [[Rotational Inertia]] ($I$), we arrive at the fundamental equation for rotational kinetic energy:
$$K_{rot} = \frac{1}{2}I\omega^2$$

## Comparing Linear and Rotational Energy
There is a direct analogy between linear and rotational kinetic energy. Both rely on a measure of "resistance to change in motion" (mass vs. moment of inertia) and the "rate of motion" squared (velocity vs. angular velocity).

| Quantity | Linear Motion | Rotational Motion |
| :--- | :--- | :--- |
| Inertial Property | Mass ($m$) | [[Rotational Inertia]] ($I$) |
| Velocity | Velocity ($v$) | Angular Velocity ($\omega$) |
| Kinetic Energy | $K = \frac{1}{2}mv^2$ | $K = \frac{1}{2}I\omega^2$ |

## Total Kinetic Energy
For objects that are undergoing both translational motion (moving through space) and rotational motion (spinning), the total kinetic energy of the system is the sum of both types:
$$K_{total} = K_{trans} + K_{rot}$$
$$K_{total} = \frac{1}{2}mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2$$

Note that for the rotation term, the [[Rotational Inertia]] must be calculated about the center of mass ($I_{cm}$) if the object is rotating about its center while moving linearly. This concept is central to understanding [[Rolling]] motion without slipping.

## Important Considerations
*   **Units:** Rotational kinetic energy is measured in Joules (J), consistent with all energy forms.
*   **Vector Nature:** While angular velocity $\omega$ is a vector, kinetic energy is a scalar quantity. It does not have a direction.
*   **Work-Energy Theorem:** Just as net work changes linear kinetic energy, a net torque acting on a rotating object changes its rotational kinetic energy, a relationship explored in [[Torque and Work]].

By understanding how energy is stored in rotation, we can solve complex dynamics problems involving flywheels, rolling spheres, and rotating machinery.