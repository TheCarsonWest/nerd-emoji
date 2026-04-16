
# [[AP Physics C Home]]
# AP Physics C: Torque and Work

## Introduction
In translational mechanics, work is defined as the product of force and displacement. Similarly, in rotational mechanics, work is performed when a torque causes an angular displacement. Understanding the relationship between torque and work is essential for analyzing rotating systems, such as engines, turbines, and flywheels.

## Rotational Work
When a constant torque $\tau$ acts on an object, causing it to rotate through an angular displacement $\Delta\theta$ (in radians), the work done $W$ is given by:

$$W = \int_{\theta_i}^{\theta_f} \tau \, d\theta$$

If the torque is constant, the formula simplifies to:

$$W = \tau\Delta\theta$$

This equation is the rotational analog to the translational work equation $W = F\Delta x$. It is important to note that the work done by a torque is positive if the torque acts in the same direction as the angular displacement (increasing rotational kinetic energy) and negative if it acts against it (decreasing rotational kinetic energy).

### Comparison of Linear and Rotational Work
The following table highlights the parallels between linear and rotational dynamics regarding work and energy.

| Concept | Linear Analog | Rotational Analog |
| :--- | :--- | :--- |
| **Force/Torque** | $F$ | $\tau$ |
| **Displacement** | $\Delta x$ | $\Delta\theta$ |
| **Work Formula** | $W = F\Delta x$ | $W = \tau\Delta\theta$ |
| **Kinetic Energy** | $K = \frac{1}{2}mv^2$ | $K_{rot} = \frac{1}{2}I\omega^2$ |
| **Work-Energy Theorem** | $W_{net} = \Delta K$ | $W_{net} = \Delta K_{rot}$ |

## The Work-Energy Theorem for Rotation
Just as the net work done on an object equals its change in translational kinetic energy, the net work done by a torque on a rigid body about a fixed axis equals the change in its rotational kinetic energy. This is defined by:

$$W_{net} = \Delta K_{rot} = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2$$

Where $I$ is the [[Rotational Inertia]] and $\omega$ is the angular velocity. This principle is a powerful tool for solving problems involving rotating objects without needing to analyze the specific time-dependent dynamics of the motion.

## Power in Rotational Systems
[[Power]] is defined as the rate at which work is done. In a rotational system, the instantaneous power $P$ delivered by a torque is given by the product of the torque and the angular velocity:

$$P = \frac{dW}{dt} = \tau \frac{d\theta}{dt} = \tau\omega$$

This relationship shows that for a given power output, a higher torque requires a lower angular velocity, and a higher angular velocity requires a lower torque—a fundamental concept in mechanical transmission design.

## Key Takeaways
*   Rotational work is the integral of torque over angular displacement.
*   The rotational work-energy theorem connects torque-induced energy changes directly to the change in rotational kinetic energy.
*   Power transmission in rotating shafts is directly related to the applied torque and the speed of rotation.
*   Always ensure angular displacement is in **radians** when calculating work.