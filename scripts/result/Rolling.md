
# [[AP Physics C Home]]
# Topic 6.5: Rolling

Rolling motion is a form of complex motion that combines both translational and rotational dynamics. An object is said to be "rolling without slipping" when its point of contact with the surface is instantaneously at rest relative to the surface.

## Kinematics of Rolling
For an object of radius $R$ rolling without slipping, there is a strict relationship between the linear velocity of the center of mass ($v_{cm}$) and the angular velocity ($\omega$). If the wheel rotates through an angle $\theta$, the center of mass moves a distance $s = R\theta$. Differentiating this with respect to time gives the velocity relationship:

$$v_{cm} = R\omega$$

Similarly, the linear acceleration ($a_{cm}$) of the center of mass relates to the angular acceleration ($\alpha$):

$$a_{cm} = R\alpha$$

[[Connecting Linear and Rotational Motion]] provides the foundation for these relationships.

## Dynamics of Rolling
When an object rolls without slipping, static friction acts at the point of contact. This friction force is what causes the object to rotate (providing the torque) rather than slide. 

The dynamics of a rolling object can be analyzed by combining Newton's Second Law for translation and rotation:

1. **Translation:** $\sum F = Ma_{cm}$
2. **Rotation:** $\sum \tau = I_{cm}\alpha$

Because the object is rolling without slipping, the friction force $f$ is an unknown variable that must be solved for using the system of equations above. It is important to note that the static friction force is *not* simply $\mu_s N$; it is determined by the constraints of the motion.

## Energy in Rolling
The total kinetic energy of a rolling object is the sum of its translational kinetic energy and its rotational kinetic energy.

$$K_{total} = K_{trans} + K_{rot} = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2$$

Since $v_{cm} = R\omega$, we can rewrite the rotational term:

$$K_{total} = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I_{cm}\left(\frac{v_{cm}}{R}\right)^2 = \frac{1}{2}Mv_{cm}^2 \left(1 + \frac{I_{cm}}{MR^2}\right)$$

### Rolling Objects Comparison
The term $\frac{I_{cm}}{MR^2}$ is a dimensionless constant specific to the shape of the object. Objects with a larger moment of inertia require more energy to rotate, meaning they will have a lower translational velocity when rolling down an incline compared to objects with a smaller moment of inertia.

| Object | Moment of Inertia ($I_{cm}$) | Shape Factor ($I_{cm}/MR^2$) |
| :--- | :--- | :--- |
| Hoop (thin cylinder) | $MR^2$ | $1$ |
| Disk (solid cylinder) | $\frac{1}{2}MR^2$ | $1/2$ |
| Solid Sphere | $\frac{2}{5}MR^2$ | $2/5$ |
| Hollow Sphere | $\frac{2}{3}MR^2$ | $2/3$ |

For more on these values, see [[Rotational Inertia]].

## Energy Conservation
When an object rolls down an incline without slipping, mechanical energy is conserved if there is no air resistance or deformation. The static friction force does **no work** on the object because the point of contact is instantaneously at rest. Therefore, the loss in gravitational potential energy equals the gain in both translational and rotational kinetic energy.

$$Mgh = \frac{1}{2}Mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2$$

This application of energy conservation is often more efficient than using Newton's laws for solving problems involving motion down a ramp. See [[Conservation of Energy]] for more context.