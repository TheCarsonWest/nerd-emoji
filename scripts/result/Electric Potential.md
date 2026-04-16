
# [[AP Physics C Home]]
# Electric Potential

Electric potential is a fundamental concept in electrostatics that describes the energy per unit charge at any point in an electric field. It allows us to analyze electric circuits and fields using scalar quantities rather than vector fields, simplifying many calculations.

## Definition and Relation to Electric Potential Energy

Electric potential, denoted by $V$, is defined as the [[Electric Potential Energy]] ($U_E$) per unit charge ($q$). It essentially measures the "voltage" at a specific point in space.

$$V = \frac{U_E}{q}$$

The SI unit for electric potential is the **Volt (V)**, where $1 \text{ V} = 1 \text{ J/C}$. Note that while electric potential energy depends on the test charge present, electric potential is a property of the field itself and depends only on the source charges creating that field.

## Potential Difference ($\Delta V$)

The work required to move a charge between two points is related to the change in electric potential. The potential difference between two points, often called "voltage," is given by:

$$\Delta V = V_f - V_i = -\int_{i}^{f} \vec{E} \cdot d\vec{r}$$

This equation shows that the potential difference is the line integral of the electric field $\vec{E}$ along the path from point $i$ to point $f$.

| Quantity | Symbol | Unit | Definition |
| :--- | :--- | :--- | :--- |
| Electric Potential | $V$ | Volts (V) | Energy per unit charge |
| Potential Difference | $\Delta V$ | Volts (V) | Change in potential between points |
| Electric Field | $\vec{E}$ | N/C or V/m | Force per unit charge |

## Relationship Between Electric Field and Potential

The electric field is the negative gradient of the electric potential. This relationship allows us to derive the electric field if the potential function is known:

$$\vec{E} = -\nabla V$$

In a one-dimensional system, this simplifies to:

$$E_x = -\frac{dV}{dx}$$

This signifies that the electric field points in the direction of the steepest decrease in potential.

## Electric Potential due to Point Charges

For a single point charge $q$, the electric potential at a distance $r$ from the charge is determined by setting the potential at infinity to zero:

$$V = k_e \frac{q}{r}$$

Where $k_e$ is Coulomb's constant. By the **Principle of Superposition**, if multiple point charges are present, the total electric potential at a point is the algebraic sum of the potentials due to each individual charge:

$$V_{total} = \sum_{i} k_e \frac{q_i}{r_i}$$

Because potential is a scalar (not a vector), we simply add the values without needing to worry about directional components. This makes solving for potential generally easier than solving for the [[Electric Fields]].

## Equipotential Surfaces

An equipotential surface is a region where the electric potential is the same at every point. Moving a charge along an equipotential surface requires zero work. Crucially, the electric field lines are always perpendicular to equipotential surfaces.