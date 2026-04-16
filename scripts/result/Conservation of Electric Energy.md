
# [[AP Physics C Home]]
# Conservation of Electric Energy

Conservation of energy is a fundamental principle in physics. When applied to electric systems, it states that the total energy in an isolated electric system remains constant. This is a specific application of the broader concept of [[Conservation of Energy]] to the electric field and electric potential.

## Electric Potential Energy vs. Electric Potential

It is crucial to distinguish between energy and potential.

*   **Electric Potential Energy ($U_E$):** The energy stored in a system of charges due to their positions. The unit is Joules ($J$).
*   **Electric Potential ($V$):** The electric potential energy per unit charge at a specific location in space. The unit is Volts ($V = J/C$).

The relationship is defined as:
$$U_E = qV$$

For a point charge $q$ in the presence of another charge $Q$ at a distance $r$:
$$U_E = k\frac{qQ}{r}$$

For a more comprehensive look at these definitions, refer to [[Electric Potential Energy]] and [[Electric Potential]].

## The Conservation Principle

In an electric field, the total mechanical energy of a charge $q$ is conserved if only conservative electric forces are doing work. The total energy $E_{total}$ is the sum of kinetic energy ($K$) and electric potential energy ($U_E$):

$$E_{total} = K + U_E = \text{constant}$$

When a charge moves from an initial point ($i$) to a final point ($f$), the change in kinetic energy is equal to the negative change in potential energy:

$$\Delta K + \Delta U_E = 0$$
$$K_f - K_i = -(U_{E,f} - U_{E,i})$$

Since $U_E = qV$, we can rewrite this in terms of electric potential:

$$\frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 = -q(V_f - V_i)$$

This equation allows us to solve for the velocity of a particle moving through an electric potential difference without needing to know the path taken.

### Energy Conversion Summary Table

| Energy Component | Definition | Mathematical Form |
| :--- | :--- | :--- |
| **Kinetic Energy** | Energy of motion | $K = \frac{1}{2}mv^2$ |
| **Electric Potential Energy** | Energy due to position in a field | $U_E = qV$ |
| **Total Energy** | Constant in a conservative field | $E = K + U_E$ |

## Applications

### Accelerated Charged Particles
When a charged particle (like an electron or proton) is released from rest in an electric field, its potential energy is converted entirely into kinetic energy. 

$$K_f = q(V_i - V_f)$$
$$\frac{1}{2}mv^2 = q\Delta V$$

This principle is the basis for particle accelerators and the operation of cathode ray tubes.

### Work Done by Electric Forces
The work done by an electric field on a charge is related to the change in potential energy:
$$W_{field} = -\Delta U_E = -q\Delta V$$

If an external force moves a charge against the field without changing its kinetic energy, the external work is:
$$W_{ext} = \Delta U_E = q\Delta V$$

This connects directly to the concept of [[Work]], where we analyze the displacement of objects under the influence of force. If you are examining more complex circuits or field interactions, it is often helpful to reference [[Electric Fields]] to determine the path and magnitude of the potential difference.