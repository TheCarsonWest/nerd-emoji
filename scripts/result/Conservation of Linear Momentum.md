
# [[AP Physics C Home]]
# AP Physics C: Conservation of Linear Momentum

## The Principle of Conservation of Momentum
The principle of conservation of linear momentum states that if the net external force acting on a system is zero, the total momentum of that system remains constant. In other words, the momentum before an interaction is equal to the momentum after the interaction, provided no outside forces intervene.

Mathematically, this is expressed as:
$$\vec{P}_{initial} = \vec{P}_{final}$$

Or, by summation:
$$\sum \vec{p}_i = \sum \vec{p}_f$$

## Conditions for Conservation
It is crucial to distinguish between *internal* and *external* forces. 
*   **Internal Forces:** Forces between objects within the defined system. These do not change the total momentum of the system because, according to Newton’s Third Law, they exist in equal and opposite action-reaction pairs (e.g., collision forces).
*   **External Forces:** Forces acting on the system from outside (e.g., friction, gravity, or an applied push). If the vector sum of these forces is zero, momentum is conserved.

### Momentum Conservation Table

| System State | Condition | Consequence |
| :--- | :--- | :--- |
| **Isolated System** | $\sum \vec{F}_{ext} = 0$ | Total Momentum is conserved |
| **Non-isolated System** | $\sum \vec{F}_{ext} \neq 0$ | Total Momentum changes (Impulse occurs) |

## Applying Conservation of Linear Momentum
When analyzing collisions or explosions, we treat the system as a closed entity. For a two-body collision, the conservation equation is:
$$m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f}$$

Because momentum is a vector quantity, you must apply the conservation law independently to each component ($x$ and $y$ dimensions) in two-dimensional problems:
$$m_1v_{1ix} + m_2v_{2ix} = m_1v_{1fx} + m_2v_{2fx}$$
$$m_1v_{1iy} + m_2v_{2iy} = m_1v_{1fy} + m_2v_{2fy}$$

## Collisions and Systems
Understanding how objects behave during collisions is essential for AP Physics C. While momentum is *always* conserved in isolated systems, kinetic energy is only conserved in specific types of interactions.

*   [[Elastic and Inelastic Collisions]] cover the specific energy behavior during these interactions.
*   To understand how forces cause these changes in momentum over time, review [[Change in Momentum and Impulse]].

## Problem-Solving Strategy
1.  **Define the System:** Draw a boundary around all objects involved in the interaction.
2.  **Check Forces:** Verify that no external forces (or negligible ones, like friction during an instantaneous collision) act on the system.
3.  **Coordinate System:** Establish a clear coordinate system.
4.  **Vector Components:** Break velocities into components if the collision is not one-dimensional.
5.  **Equation Setup:** Write the momentum conservation equation for each dimension.
6.  **Solve:** Substitute known values and solve for the unknowns.

This concept is foundational for mechanics, and it often appears alongside work and energy principles. For a deeper understanding of energy interactions during these events, refer to [[Conservation of Energy]].