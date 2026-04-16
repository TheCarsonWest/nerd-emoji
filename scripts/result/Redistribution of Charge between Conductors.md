
# [[AP Physics C Home]]
# Redistribution of Charge between Conductors

When two or more charged conductors are connected by a conducting wire, charge will flow between them until they reach a state of **electrostatic equilibrium**. This process is governed by the principle that all points on a connected conductor must be at the same electric potential.

## The Principle of Potential Equivalence

In electrostatic equilibrium, the interior of a conductor has no electric field, and the entire volume of a conductor is an equipotential surface. When two conductors (say, sphere A and sphere B) are connected by a conducting path, charge flows until the potential of sphere A ($V_A$) equals the potential of sphere B ($V_B$).

$$V_A = V_B$$

For two spherical conductors of radii $r_1$ and $r_2$, the potential at the surface of each is given by:

$$V = \frac{kQ}{r}$$

Therefore, the condition for equilibrium is:

$$\frac{kQ_1}{r_1} = \frac{kQ_2}{r_2} \implies \frac{Q_1}{r_1} = \frac{Q_2}{r_2}$$

This demonstrates that the final charge on each conductor is directly proportional to its radius.

## Key Relationships in Charge Redistribution

| Property | Relationship |
| :--- | :--- |
| **Total Charge** | Conserved: $Q_{total} = Q_1 + Q_2 = Q_{1,final} + Q_{2,final}$ |
| **Potential** | Equal: $V_{1,final} = V_{2,final}$ |
| **Charge Ratio** | $\frac{Q_1}{Q_2} = \frac{r_1}{r_2}$ |

## Important Implications

### Charge Density and Curvature
The redistribution of charge is highly dependent on the geometry of the conductors. While spherical conductors distribute charge based on their radius, irregularly shaped conductors redistribute charge such that the charge density ($\sigma$) is highest at regions with the smallest radius of curvature (sharp points).

This phenomenon explains the "lightning rod effect," where charge density becomes so high at sharp points that it can ionize the surrounding air, creating a path for discharge. This relates to the concept of [[Electrostatics with Conductors]].

### Connecting to Capacitance
The redistribution of charge is effectively the physical process of charging capacitors in parallel. When two conductors are connected, they effectively act as a single system with a combined capacitance. We can define the capacitance of a spherical conductor as:

$$C = \frac{Q}{V} = \frac{Q}{kQ/r} = \frac{r}{k} = 4\pi\epsilon_0 r$$

When connected, the conductors share charge to maintain a common potential, similar to how capacitors in parallel share the same voltage. For more on this, refer to [[Capacitors]].

### Energy Considerations
It is critical to note that while charge is conserved during redistribution, **electrostatic potential energy is generally not conserved**. When charge moves between conductors, energy is typically dissipated as heat or electromagnetic radiation due to the resistance of the connecting wire or the creation of sparks. The change in energy can be analyzed using concepts from [[Electric Potential Energy]].