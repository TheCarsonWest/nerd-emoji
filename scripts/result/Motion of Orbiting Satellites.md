# [[AP Physics Home]]
# AP Physics 1: Topic 6.6 - Motion of Orbiting Satellites

## Introduction to Orbiting Satellites

An orbiting satellite is an object (natural or artificial) that revolves around a larger celestial body due to the force of [[Gravitational Force]]. Examples include the Moon orbiting Earth (natural satellite) or the International Space Station (artificial satellite). For simplicity in AP Physics 1, we often consider orbits to be perfectly circular, although in reality, most orbits are elliptical.

## Forces and Motion in Orbit

The primary force acting on a satellite in orbit is the [[Gravitational Force]] exerted by the central body. This force acts as the centripetal force, continuously pulling the satellite towards the center of its orbit and causing it to move in a curved path.

*   **Central Body Mass**: $M$
*   **Satellite Mass**: $m$
*   **Orbital Radius**: $r$ (distance from the center of the central body to the satellite)

The gravitational force is given by Newton's Law of Universal Gravitation:
$F_g = \frac{GMm}{r^2}$
where $G$ is the universal gravitational constant ($6.67 \times 10^{-11} \text{ N} \cdot \text{m}^2/\text{kg}^2$).

For a satellite in a stable circular orbit, this gravitational force provides the necessary [[Circular Motion]]'s centripetal force:
$F_c = \frac{mv^2}{r}$
Equating these two forces allows us to derive key orbital characteristics.

## Orbital Speed and Period

By setting the gravitational force equal to the centripetal force, we can determine the orbital speed ($v$) of the satellite.

$ \frac{GMm}{r^2} = \frac{mv^2}{r} $
Notice that the mass of the satellite ($m$) cancels out, meaning the orbital speed for a given radius only depends on the mass of the central body ($M$).

$ v^2 = \frac{GM}{r} $
$ v = \sqrt{\frac{GM}{r}} $

This equation shows that satellites in higher orbits (larger $r$) move slower.

The orbital period ($T$) is the time it takes for a satellite to complete one full revolution. For a circular orbit, the distance traveled in one period is the circumference $2\pi r$.
Since $v = \frac{\text{distance}}{\text{time}} = \frac{2\pi r}{T}$, we can express the period as:
$ T = \frac{2\pi r}{v} $
Substituting the expression for $v$:
$ T = \frac{2\pi r}{\sqrt{\frac{GM}{r}}} = 2\pi r \sqrt{\frac{r}{GM}} $
$ T = 2\pi \sqrt{\frac{r^3}{GM}} $
Squaring both sides gives us **Kepler's Third Law** for circular orbits:
$ T^2 = \frac{4\pi^2}{GM} r^3 $
This relationship indicates that $T^2 \propto r^3$, meaning the square of the orbital period is proportional to the cube of the orbital radius. The constant of proportionality depends only on the mass of the central body.

### Geosynchronous Orbit
[[Geosynchronous Orbit]] is a special type of orbit where a satellite remains above the same point on Earth's equator. This requires the satellite's orbital period to be exactly one sidereal day (approximately 23 hours, 56 minutes, 4 seconds), matching Earth's rotation period.

## Energy of an Orbiting Satellite

An orbiting satellite possesses both kinetic energy ($K$) due to its motion and gravitational [[Potential Energy]] ($U_g$) due to its position in the gravitational field.

*   **Kinetic Energy**:
    $ K = \frac{1}{2}mv^2 $
    Substituting $v^2 = \frac{GM}{r}$:
    $ K = \frac{1}{2}m\left(\frac{GM}{r}\right) = \frac{GMm}{2r} $

*   **Gravitational Potential Energy**:
    The gravitational potential energy for a system of two masses is defined as:
    $ U_g = -\frac{GMm}{r} $
    The negative sign indicates that the system is bound; energy must be added to separate the masses. The potential energy is zero at infinite separation.

*   **Total Mechanical Energy ($E_{total}$)**:
    The total mechanical energy is the sum of kinetic and potential energy:
    $ E_{total} = K + U_g $
    $ E_{total} = \frac{GMm}{2r} + \left(-\frac{GMm}{r}\right) $
    $ E_{total} = -\frac{GMm}{2r} $
    The total mechanical energy of an orbiting satellite is negative, which is characteristic of a bound system. The total energy is constant for an isolated satellite system.

## Summary of Orbital Parameters

| Parameter        | Symbol | Formula                               | Dependencies                                      | Notes                                             |
| :--------------- | :----- | :------------------------------------ | :------------------------------------------------ | :------------------------------------------------ |
| Gravitational Force | $F_g$  | $\frac{GMm}{r^2}$                     | $G, M, m, r$                                      | Acts as centripetal force                       |
| Orbital Speed    | $v$    | $\sqrt{\frac{GM}{r}}$                 | $G, M, r$ (independent of satellite mass $m$)     | Decreases with increasing radius                |
| Orbital Period   | $T$    | $2\pi \sqrt{\frac{r^3}{GM}}$          | $G, M, r$ (independent of satellite mass $m$)     | Increases with increasing radius (Kepler's 3rd Law) |
| Kinetic Energy   | $K$    | $\frac{GMm}{2r}$                      | $G, M, m, r$                                      | Always positive, decreases with increasing radius |
| Potential Energy | $U_g$  | $-\frac{GMm}{r}$                      | $G, M, m, r$                                      | Always negative, increases (less negative) with increasing radius |
| Total Energy     | $E_{total}$ | $-\frac{GMm}{2r}$                     | $G, M, m, r$                                      | Always negative, increases (less negative) with increasing radius |

This framework allows us to analyze the motion and energy of satellites in circular orbits, providing a fundamental understanding of celestial mechanics relevant to AP Physics.