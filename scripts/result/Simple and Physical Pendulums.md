
# [[AP Physics C Home]]
# Topic 7.5: Simple and Physical Pendulums

In AP Physics C, understanding pendulums requires applying the concepts of [[Defining Simple Harmonic Motion (SHM)]] to rotational systems. Pendulums are systems that oscillate about an equilibrium position due to a restoring force or torque.

## The Simple Pendulum

A simple pendulum consists of a point mass ($m$) attached to a massless string of length ($L$) oscillating in a uniform gravitational field. 

For small angles, the restoring force is proportional to the displacement, allowing us to model the motion as Simple Harmonic Motion (SHM). Using Newton’s Second Law in rotational form ([[Newtons Second Law in Rotational Form]]), where $\tau = I\alpha$:

The torque provided by gravity is $\tau = -mgL\sin(\theta)$. For small angles, $\sin(\theta) \approx \theta$ (in radians), leading to the differential equation:

$$\frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0$$

This yields the following period for a simple pendulum:

$$T = 2\pi\sqrt{\frac{L}{g}}$$

## The Physical Pendulum

A physical pendulum is any rigid body oscillating about a fixed pivot point that does not pass through its center of mass. Unlike the simple pendulum, the distribution of mass matters, requiring the use of [[Rotational Inertia]].

Using the rotational version of Newton’s Second Law, $\tau_{net} = I\alpha$, where $I$ is the moment of inertia about the pivot point and $d$ is the distance from the pivot to the center of mass:

$$\tau = -mgd\sin(\theta) = I\frac{d^2\theta}{dt^2}$$

Again, applying the small-angle approximation ($\sin(\theta) \approx \theta$):

$$\frac{d^2\theta}{dt^2} + \left(\frac{mgd}{I}\right)\theta = 0$$

Comparing this to the standard SHM equation $\frac{d^2\theta}{dt^2} + \omega^2\theta = 0$, we find the angular frequency $\omega = \sqrt{\frac{mgd}{I}}$. The period is:

$$T = 2\pi\sqrt{\frac{I}{mgd}}$$

## Comparison Table

| Feature | Simple Pendulum | Physical Pendulum |
| :--- | :--- | :--- |
| **Assumption** | Mass at end of string | Extended rigid body |
| **Angular Frequency ($\omega$)** | $\sqrt{\frac{g}{L}}$ | $\sqrt{\frac{mgd}{I}}$ |
| **Period ($T$)** | $2\pi\sqrt{\frac{L}{g}}$ | $2\pi\sqrt{\frac{I}{mgd}}$ |
| **Requires $I$?** | No ($I = mL^2$) | Yes |

## Key Takeaways
1. **Small Angle Approximation:** Both formulas strictly apply only when $\theta$ is small (typically $\theta < 15^\circ$). If the amplitude is large, the motion is no longer strictly simple harmonic.
2. **Dependence on $g$:** Both pendulums are sensitive to the local gravitational field. A pendulum clock that keeps perfect time on Earth will run slow on the Moon.
3. **The Pivot Point:** In a physical pendulum, the moment of inertia ($I$) must be calculated relative to the axis of rotation (the pivot point). If you have the inertia about the center of mass ($I_{cm}$), use the [[Parallel Axis Theorem]] to find the inertia about the pivot point.