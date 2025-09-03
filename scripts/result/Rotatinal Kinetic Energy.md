# [[AP Physics Home]]
# Rotational Kinetic Energy

Rotational Kinetic Energy is the energy an object possesses due to its rotation. Just as objects moving linearly have [[Translational Kinetic Energy]], objects that spin or rotate around an axis have rotational kinetic energy. It is a scalar quantity, measured in joules (J).

## Definition and Formula

Imagine a rigid body rotating about a fixed axis. Each tiny particle within the body has some linear velocity $v$ and thus some translational kinetic energy $\frac{1}{2}mv^2$. The total rotational kinetic energy of the body is the sum of the kinetic energies of all its individual particles.

For a single particle of mass $m$ at a distance $r$ from the axis of rotation, its linear speed $v$ is related to the angular speed $\omega$ by $v = r\omega$.
Its kinetic energy is $KE_{particle} = \frac{1}{2}mv^2 = \frac{1}{2}m(r\omega)^2 = \frac{1}{2}mr^2\omega^2$.

For the entire rigid body, the total rotational kinetic energy ($KE_{rot}$) is the sum over all particles:

$
KE_{rot} = \sum \frac{1}{2}m_ir_i^2\omega^2
$

Since all particles in a rigid body rotate with the same angular speed $\omega$, we can factor it out:

$
KE_{rot} = \frac{1}{2}\left(\sum m_ir_i^2\right)\omega^2
$

The term $\sum m_ir_i^2$ is defined as the [[Moment of Inertia]], $I$.

Therefore, the formula for rotational kinetic energy is:

$
KE_{rot} = \frac{1}{2}I\omega^2
$

Where:
*   $KE_{rot}$ is the rotational kinetic energy (Joules, J)
*   $I$ is the [[Moment of Inertia]] (kg·m²)
*   $\omega$ is the angular speed (radians/second, rad/s)

## Moment of Inertia ([[Moment of Inertia]])

The [[Moment of Inertia]] (I) is a measure of an object's resistance to changes in its rotational motion. It plays a role in rotational dynamics analogous to mass in translational dynamics. Its value depends on the object's mass distribution relative to the axis of rotation. For continuous objects, the summation becomes an integral: $I = \int r^2 dm$. Different shapes have different formulas for their moment of inertia.

## Comparison with Translational Kinetic Energy

Rotational kinetic energy shares a striking resemblance in its mathematical form to [[Translational Kinetic Energy]].

| Feature                 | Translational Kinetic Energy ($KE_{trans}$) | Rotational Kinetic Energy ($KE_{rot}$) |
| :---------------------- | :------------------------------------------- | :--------------------------------------- |
| **Formula**             | $\frac{1}{2}mv^2$                             | $\frac{1}{2}I\omega^2$                   |
| **"Inertia" Term**      | Mass ($m$)                                   | [[Moment of Inertia]] ($I$)              |
| **"Motion" Term (Sq)**  | Linear Speed ($v^2$)                         | Angular Speed ($\omega^2$)              |
| **Type of Motion**      | Linear movement                              | Rotation about an axis                   |

## Total Kinetic Energy

When an object is both translating (moving linearly) and rotating, its total kinetic energy is the sum of its translational and rotational kinetic energies:

$
KE_{total} = KE_{trans} + KE_{rot} = \frac{1}{2}mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2
$

Where $v_{cm}$ is the speed of the center of mass and $I_{cm}$ is the moment of inertia about an axis passing through the center of mass. This is particularly relevant for objects that are [[Rolling]] without slipping.

## Applications

Rotational kinetic energy is a critical component when analyzing systems involving rotating objects, especially in the context of the [[Conservation of Energy]]. For example:
*   A rolling ball down a ramp transforms gravitational [[Potential Energy]] into both translational and rotational kinetic energy.
*   A spinning flywheel stores energy as rotational kinetic energy.
*   Understanding the dynamics of gears, pulleys, and other rotating machinery.

The principles of rotational kinetic energy are fundamental to understanding the dynamics of a vast range of physical systems, from atoms to galaxies.