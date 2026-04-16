
# [[AP Physics C Home]]
# 3.3 Potential Energy

Potential energy ($U$) is defined as the energy possessed by an object due to its position or configuration. It is a stored form of energy that can be converted into kinetic energy or work. In physics, potential energy is fundamentally linked to conservative forces.

## Conservative vs. Non-Conservative Forces

The concept of potential energy only applies to conservative forces. A force is considered **conservative** if the work done by that force on an object moving between two points is independent of the path taken.

| Property | Conservative Forces | Non-Conservative Forces |
| :--- | :--- | :--- |
| Work Done | Path independent | Path dependent |
| Round Trip | Zero work done | Non-zero work done |
| Potential Energy | Defined | Not defined |
| Examples | Gravity, Spring Force, Electrostatic Force | Friction, Air Resistance, Tension |

## Definition via Work
The change in potential energy ($\Delta U$) of a system is defined as the negative of the work done by the conservative force ($W_c$) on the object as it moves from an initial position $x_i$ to a final position $x_f$:

$$\Delta U = U_f - U_i = -W_c = -\int_{x_i}^{x_f} \vec{F}_c \cdot d\vec{r}$$

This relationship implies that if a conservative force does positive work (e.g., gravity pulling an object down), the system loses potential energy.

## Common Forms of Potential Energy

### Gravitational Potential Energy
Near the Earth's surface, where the gravitational force is assumed to be constant, the gravitational potential energy is given by:

$$U_g = mgh$$

Where $m$ is mass, $g$ is the acceleration due to gravity, and $h$ is the vertical height relative to a chosen reference point (where $U=0$).

### Elastic Potential Energy
For an ideal spring following Hooke's Law ($F_s = -kx$), the potential energy stored in the spring when compressed or stretched by a displacement $x$ is:

$$U_s = \frac{1}{2}kx^2$$

Where $k$ is the spring constant. This is derived by integrating the spring force: $W_s = \int_{0}^{x} -(-kx) dx = \frac{1}{2}kx^2$.

## Force and Potential Energy Relationship

There is a direct calculus-based relationship between the potential energy function $U(x)$ and the conservative force $F(x)$. Since work is the integral of force, force is the negative gradient (or derivative) of potential energy:

$$F(x) = -\frac{dU}{dx}$$

This is a critical concept in [[Energy of Simple Harmonic Oscillators]], where the slope of the potential energy curve indicates the direction and magnitude of the force acting on the object.

## Conclusion and Applications

Understanding potential energy is essential for analyzing systems where energy is conserved. For a deeper understanding of how these energies are applied in systems, refer to [[Conservation of Energy]]. Additionally, this concept is foundational when moving from mechanical systems to electrical systems, which is covered in [[Electric Potential Energy]].