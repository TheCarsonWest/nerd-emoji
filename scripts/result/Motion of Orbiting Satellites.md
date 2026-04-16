
# [[AP Physics C Home]]
# 6.6: Motion of Orbiting Satellites

For an object to orbit a planet or star, it must be in a state of continuous freefall. The gravitational force acts as the centripetal force required to keep the object in a circular path.

## The Physics of Orbital Motion

When a satellite of mass $m$ orbits a central body of mass $M$ at a distance $r$ from the center of the mass, the gravitational force provides the centripetal force. 

Setting the law of universal gravitation equal to the centripetal force equation:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

By simplifying, we can derive the orbital velocity ($v$):

$$v = \sqrt{\frac{GM}{r}}$$

From this, we see that the velocity of an orbit is independent of the mass of the satellite ($m$). It depends solely on the mass of the central body ($M$) and the radius of the orbit ($r$).

## Orbital Period and Energy

We can derive the relationship between the period ($T$) and the orbital radius using the relationship $v = \frac{2\pi r}{T}$. Substituting this into our velocity equation yields Kepler's Third Law:

$$T^2 = \frac{4\pi^2}{GM}r^3$$

Furthermore, the total mechanical energy of an orbiting satellite is the sum of its kinetic energy ($K$) and gravitational potential energy ($U_g$). Using the relationship $K = \frac{1}{2}mv^2$ and the velocity derived above:

$$E_{total} = K + U_g = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

This negative total energy indicates that the satellite is in a "bound state," meaning it requires additional energy to escape the gravitational field entirely.

## Summary Table of Orbital Parameters

| Parameter | Formula |
| :--- | :--- |
| Orbital Velocity | $v = \sqrt{\frac{GM}{r}}$ |
| Orbital Period | $T = 2\pi\sqrt{\frac{r^3}{GM}}$ |
| Kinetic Energy | $K = \frac{GMm}{2r}$ |
| Gravitational Potential Energy | $U_g = -\frac{GMm}{r}$ |
| Total Mechanical Energy | $E = -\frac{GMm}{2r}$ |

## Key Concepts to Explore

Understanding satellites requires a solid grasp of fundamental gravitational and energy principles. For a deeper look at the components that make up these orbits, refer to the following:

*   [[Gravitational Fields]] (The force field governing the orbit)
*   [[Potential Energy]] (Specifically, the derivation of gravitational potential energy)
*   [[Conservation of Energy]] (How energy is conserved as a satellite changes orbital height)
*   [[Angular Momentum and Angular Impulse]] (Essential for understanding non-circular, elliptical orbits)

### Important Considerations
*   **Geosynchronous Orbits:** An orbit where the satellite's period matches the rotation of the Earth. These are calculated by setting $T = 86,400$ seconds.
*   **Escape Velocity:** The minimum speed needed for an object to break free from the gravitational attraction of a massive body, derived by setting total mechanical energy equal to zero ($K + U_g = 0$).