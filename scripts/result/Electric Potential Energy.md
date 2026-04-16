
# [[AP Physics C Home]]
# AP Physics C: Electric Potential Energy

Electric potential energy is the energy a charged object possesses because of its position within an electric field. It is a scalar quantity and a fundamental concept in understanding electrostatic interactions.

## The Concept of Potential Energy

Just as a mass in a gravitational field has gravitational potential energy due to its position, a charged particle in an electric field has electric potential energy ($U_E$). This energy arises from the work done by the electric field (or against it) to move a charge from one point to another.

The change in electric potential energy, $\Delta U_E$, is defined by the negative of the work done by the conservative electric force as the charge moves from point A to point B:

$$\Delta U_E = U_B - U_A = -W_{electric} = -\int_A^B \vec{F}_E \cdot d\vec{r}$$

Since $\vec{F}_E = q\vec{E}$, this simplifies to:

$$\Delta U_E = -q \int_A^B \vec{E} \cdot d\vec{r}$$

## Potential Energy of a System of Point Charges

When we have two point charges, $q_1$ and $q_2$, separated by a distance $r$, the potential energy of the system is the work required to assemble them by bringing them from infinity to their current separation. The formula for this interaction energy is:

$$U_E = \frac{k q_1 q_2}{r}$$

Where:
*   $k$ is Coulomb's constant ($8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$)
*   $q_1, q_2$ are the charges (including signs)
*   $r$ is the separation distance

### Key Observations

| Interaction Type | Sign of $U_E$ | Meaning |
| :--- | :--- | :--- |
| Like Charges | Positive (+) | Work is required to push them together; they naturally repel. |
| Opposite Charges | Negative (-) | Energy is released as they move together; they are bound. |

## Relationship to Electric Potential

It is crucial to distinguish between Electric Potential Energy and [[Electric Potential]]. While potential energy ($U_E$) depends on the charge ($q$) being placed in a field, electric potential ($V$) is a property of the field itself at a specific point in space.

They are related by the following equation:

$$U_E = qV$$

This relationship allows us to calculate the potential energy of a charge $q$ if we know the electric potential $V$ at its location.

## Conservation of Energy in Electrostatics

In systems where only conservative electric forces are at play, the total mechanical energy of a charged particle is conserved. If we consider a particle moving from position A to B in an electric field:

$$K_A + U_A = K_B + U_B$$

Substituting the kinetic energy formula ($K = \frac{1}{2}mv^2$):

$$\frac{1}{2}mv_A^2 + qV_A = \frac{1}{2}mv_B^2 + qV_B$$

This principle is essential for solving problems involving [[Simple Circuits]] and the motion of charged particles, such as those found in cathode ray tubes or particle accelerators. Understanding this energy conservation is also a prerequisite for understanding [[Capacitors]] and how they store energy in their fields.