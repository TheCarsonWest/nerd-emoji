
# [[AP Physics C Home]]
# AP Physics C: Elastic and Inelastic Collisions

In physics, collisions are interactions between two or more objects where the momentum and kinetic energy of the system are analyzed. Understanding the nature of a collision depends on whether the total kinetic energy of the system is conserved.

## Conservation Principles

Regardless of the type of collision, the total linear momentum of a system is always conserved, provided there are no external forces acting on the system. This concept is explored further in [[Conservation of Linear Momentum]].

$$ \sum \vec{p}_{initial} = \sum \vec{p}_{final} $$

## Types of Collisions

Collisions are categorized based on the behavior of kinetic energy ($K$) during the interaction.

| Collision Type | Kinetic Energy Conserved? | Momentum Conserved? | Note |
| :--- | :--- | :--- | :--- |
| **Elastic** | Yes | Yes | Objects bounce off without deformation or heat loss. |
| **Inelastic** | No | Yes | Kinetic energy is lost to heat, sound, or deformation. |
| **Perfectly Inelastic** | No | Yes | Objects stick together and move with a common velocity. |

### Elastic Collisions
In a perfectly elastic collision, the total kinetic energy of the system before the collision is equal to the total kinetic energy after the collision. While theoretical, many interactions at the atomic scale (like gas molecules) are modeled as elastic.

For a one-dimensional elastic collision involving two masses ($m_1$ and $m_2$) with initial velocities ($v_{1i}$ and $v_{2i}$) and final velocities ($v_{1f}$ and $v_{2f}$), both momentum and energy are conserved:

1. Momentum: $m_1v_{1i} + m_2v_{2i} = m_1v_{1f} + m_2v_{2f}$
2. Kinetic Energy: $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2$

A useful result for 1D elastic collisions is that the relative velocity of recession equals the negative of the relative velocity of approach:

$$ v_{1i} - v_{2i} = -(v_{1f} - v_{2f}) $$

### Inelastic Collisions
Most real-world collisions are inelastic. In these events, some of the initial kinetic energy is transformed into other forms of energy, such as thermal energy, acoustic energy, or the energy required to permanently deform the objects involved.

### Perfectly Inelastic Collisions
This is the limiting case of an inelastic collision where the objects stick together after impact. Because they move with a single common final velocity ($v_f$), the momentum equation simplifies significantly:

$$ m_1v_{1i} + m_2v_{2i} = (m_1 + m_2)v_f $$

The kinetic energy lost ($\Delta K$) in this type of collision is often a key calculation in AP Physics C problems:

$$ \Delta K = K_{final} - K_{initial} $$

Because the objects stick together, this interaction maximizes the loss of kinetic energy allowed by the conservation of momentum.

## Solving Collision Problems

When tackling collision problems, always follow these steps:
1. Define the system to ensure no external forces are acting on it.
2. Determine if the collision is elastic (conserve $K$) or inelastic (conserve $p$ only).
3. Set up the conservation of momentum equations using vector components.
4. If the collision is [[Two-Dimensional Collisions]], analyze the $x$ and $y$ components of momentum independently.