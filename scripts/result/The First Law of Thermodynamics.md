
# [[AP Physics C Home]]
# Topic 9.4: The First Law of Thermodynamics

The First Law of Thermodynamics is a statement of the principle of conservation of energy applied to thermal systems. It relates the changes in internal energy of a system to the energy transferred into or out of the system as heat and work.

## The Conservation of Energy

The First Law states that the change in the internal energy ($\Delta U$) of a closed system is equal to the heat added to the system ($Q$) minus the work done by the system ($W$). Mathematically, this is expressed as:

$$\Delta U = Q - W$$

Alternatively, some textbooks express this as $\Delta U = Q + W_{on}$, where $W_{on}$ is the work done *on* the system. In AP Physics C, the convention $\Delta U = Q - W$ (where $W$ is work done *by* the system) is standard.

### Sign Conventions

Understanding the sign conventions is critical for solving thermodynamics problems.

| Quantity | Symbol | Positive (+) | Negative (-) |
| :--- | :--- | :--- | :--- |
| **Internal Energy** | $\Delta U$ | Temperature increases | Temperature decreases |
| **Heat** | $Q$ | Heat added to the system | Heat removed from the system |
| **Work** | $W$ | Work done *by* the system (expansion) | Work done *on* the system (compression) |

## Internal Energy and Ideal Gases

For an ideal gas, the internal energy depends solely on the temperature. This is a fundamental concept derived from the [[Kinetic Theory of Temperature and Pressure]]. The change in internal energy for a monatomic ideal gas is given by:

$$\Delta U = \frac{3}{2}nR\Delta T$$

where $n$ is the number of moles, $R$ is the ideal gas constant, and $\Delta T$ is the change in temperature.

## Work in Thermodynamic Processes

Work in thermodynamics is often calculated using pressure-volume ($PV$) diagrams. The work done by a gas during expansion or compression is the area under the curve on a $PV$ plot:

$$W = \int P \, dV$$

If the pressure is constant (an isobaric process), this simplifies to:

$$W = P\Delta V$$

## Specialized Thermodynamic Processes

The First Law is often applied to specific idealized processes. Each process changes the behavior of the variables in the equation $\Delta U = Q - W$.

*   **Adiabatic Process:** No heat is transferred ($Q = 0$). Therefore, $\Delta U = -W$. Any work done by the system comes at the expense of its internal energy.
*   **Isochoric Process:** The volume is constant ($\Delta V = 0$), so $W = 0$. Therefore, $\Delta U = Q$. All energy added as heat goes directly into increasing internal energy.
*   **Isothermal Process:** The temperature remains constant ($\Delta T = 0$), implying $\Delta U = 0$ for an ideal gas. Thus, $Q = W$. All heat added is converted directly into work done by the system.
*   **Isobaric Process:** Pressure remains constant. $W = P\Delta V$. This process often involves the use of specific heat capacities, which are related to [[Specific Heat and Thermal Conductivity]].

Understanding these processes is essential for analyzing heat engines and refrigerators, which are applications of [[Entropy and the Second Law of Thermodynamics]].