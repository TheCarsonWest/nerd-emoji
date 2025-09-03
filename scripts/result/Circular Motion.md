# [[AP Physics Home]]
# AP Physics 1: Topic 2.9 - Circular Motion

## Introduction to Circular Motion

Circular motion describes the movement of an object along the circumference of a circle or a circular path. This topic is fundamental to understanding many phenomena, from planets orbiting stars to cars turning corners. A key characteristic is that even if the speed of the object is constant, its direction is continuously changing, implying an acceleration.

## Key Concepts

### Uniform Circular Motion (UCM)

[[Uniform Circular Motion]] is a special case where an object moves in a circular path at a constant **speed**. Despite the constant speed, the object is always accelerating because its [[Vectors and Motion in Two Dimensions|velocity vector]] is continuously changing direction.

### Centripetal Acceleration

For an object to move in a circle, there must be an acceleration directed towards the center of the circle. This is called **centripetal acceleration** ($a_c$). Without it, the object would move in a straight line tangent to the circle according to [[Newton’s First Law]].

The magnitude of centripetal acceleration is given by:

$a_c = \frac{v^2}{r}$

Where:
* $a_c$ is the centripetal acceleration (in m/s²)
* $v$ is the tangential speed of the object (in m/s)
* $r$ is the radius of the circular path (in m)

Alternatively, using angular velocity $\omega$:

$a_c = \omega^2 r$

Where $\omega$ is the angular velocity (in rad/s). Recall that $v = \omega r$.

### Centripetal Force

According to [[Newton’s Second Law]], if there is an acceleration, there must be a net force causing it. The force responsible for centripetal acceleration is called the **centripetal force** ($F_c$). It is always directed towards the center of the circular path, parallel to the centripetal acceleration.

The magnitude of centripetal force is:

$F_c = m a_c = \frac{mv^2}{r}$

Where:
* $F_c$ is the centripetal force (in N)
* $m$ is the mass of the object (in kg)
* $v$ is the tangential speed (in m/s)
* $r$ is the radius of the circular path (in m)

It's crucial to understand that "centripetal force" is not a new fundamental force, but rather a *role* played by existing forces (e.g., tension, friction, gravity, normal force). For instance, for a car turning a corner, friction provides the centripetal force. For a satellite orbiting Earth, [[Gravitational Force]] provides the centripetal force.

### Tangential Velocity

The velocity of an object in circular motion is always tangent to the circular path at any given point. Its direction is constantly changing, even if its magnitude (speed) remains constant in UCM. The magnitude of tangential velocity $v$ is related to the period $T$ and frequency $f$:

$v = \frac{2\pi r}{T} = 2\pi r f$

Where:
* $T$ is the period (time for one full revolution, in s)
* $f$ is the frequency (number of revolutions per second, in Hz or s⁻¹)
* $r$ is the radius (in m)

## Applications of Circular Motion

| Scenario                      | Force Providing Centripetal Force ($F_c$)       | Relevant Equations                             |
| :---------------------------- | :---------------------------------------------- | :--------------------------------------------- |
| Car turning on a flat road    | Static friction ($F_f$)                         | $F_f = \frac{mv^2}{r}$                         |
| Object swung on a string      | Tension ($T_{string}$)                          | $T_{string} = \frac{mv^2}{r}$                  |
| Satellite orbiting Earth      | Gravitational force ($F_g$)                     | $F_g = G \frac{M m}{r^2} = \frac{mv^2}{r}$     |
| Loop-the-loop (at top)        | Normal force ($F_N$) + Gravitational force ($F_g$) | $F_N + F_g = \frac{mv^2}{r}$                   |
| Loop-the-loop (at bottom)     | Normal force ($F_N$) - Gravitational force ($F_g$) | $F_N - F_g = \frac{mv^2}{r}$                   |

### Solving Problems with Circular Motion

1.  **Draw a [[Forces and Free-Body Diagrams|Free-Body Diagram]]:** Identify all forces acting on the object.
2.  **Choose a Coordinate System:** Orient one axis (usually the y-axis) towards the center of the circular path. The other axis is tangential.
3.  **Apply [[Newton’s Second Law]]:** Sum the forces in the radial direction and set them equal to $ma_c$.
    $\Sigma F_{radial} = ma_c = \frac{mv^2}{r}$
4.  **Solve:** Use the resulting equation to find the unknown quantity. Remember that forces *causing* the circular motion are centripetal, not an extra force.