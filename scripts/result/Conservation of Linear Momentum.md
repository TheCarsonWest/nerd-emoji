# [[AP Physics Home]]
# 4.3: Conservation of Linear Momentum

This note page expands on the fundamental principle of [[Conservation of Linear Momentum]], a crucial concept in AP Physics. It builds upon our understanding of [[Linear Momentum]] and [[Change in Momentum and Impulse]], detailing the conditions under which the total momentum of a system remains constant.

## I. The Principle of Conservation of Linear Momentum

The Law of Conservation of Linear Momentum states that if the net external force acting on a system of particles is zero, then the total linear momentum of the system remains constant. In simpler terms, the momentum lost by one part of the system is gained by another part, such that the total momentum before and after an interaction is the same.

### A. Mathematical Statement
For an [[Isolated System]] (where net external force is zero), the total momentum ($P_{total}$) before an interaction is equal to the total momentum after the interaction.

$
\vec{P}_{initial} = \vec{P}_{final}
$

For a system with multiple objects, this can be expressed as the sum of individual momenta:

$
\sum_{i} m_i \vec{v}_{i, initial} = \sum_{i} m_i \vec{v}_{i, final}
$

Where:
*   $m_i$ is the mass of the $i$-th object.
*   $\vec{v}_{i, initial}$ is the initial velocity of the $i$-th object.
*   $\vec{v}_{i, final}$ is the final velocity of the $i$-th object.

This equation holds true for each component (x, y, z) independently, meaning $\vec{P}_{x, initial} = \vec{P}_{x, final}$ and $\vec{P}_{y, initial} = \vec{P}_{y, final}$.

## II. Conditions for Momentum Conservation

The conservation of linear momentum is a direct consequence of [[Newton’s Third Law]] when considering an [[Isolated System]].

### A. Isolated System
A system is considered **isolated** if the net external force acting on it is zero. This means:
1.  **No external forces**: No forces from outside the system act on its components.
2.  **External forces balance**: If external forces are present, they sum to zero (e.g., gravity balanced by a normal force, but usually, we consider interactions where external forces are negligible during the short duration of the interaction).

**Internal forces**, which are forces exchanged between objects within the system (e.g., collision forces), do not change the total momentum of the system. According to [[Newton’s Third Law]], these forces are equal in magnitude and opposite in direction, so their impulse on the system cancels out.

## III. Applications and Types of Interactions

The conservation of linear momentum is particularly useful in analyzing collisions and explosions.

### A. Collisions
In a collision, objects exert forces on each other over a short period. As these forces are internal to the system, the total momentum of the system (all colliding objects) is conserved, provided external forces are negligible during the collision. Collisions are broadly categorized into:

| Type of Collision | Conservation of Momentum | Conservation of Kinetic Energy | Description |
| :---------------- | :----------------------- | :----------------------------- | :---------- |
| **[[Elastic and Inelastic Collisions]]** | Yes                      | Yes                            | Objects bounce off each other; kinetic energy and momentum are conserved. |
| **[[Elastic and Inelastic Collisions]]** | Yes                      | No (Kinetic energy is lost, usually as heat, sound, or deformation) | Objects may stick together or deform; momentum is conserved, but kinetic energy is not. |

### B. Explosions (Reverse Collisions)
An explosion is essentially the reverse of an inelastic collision where objects initially at rest or moving together separate. Internal forces (e.g., expanding gases) propel parts of the system apart. The total momentum of the system *before* the explosion is equal to the total momentum *after* the explosion. If the system was initially at rest, its total momentum remains zero after the explosion.

**Example**: A cannon firing a projectile. The cannon and projectile form a system. Before firing, total momentum is zero. After firing, the forward momentum of the projectile is equal in magnitude and opposite in direction to the backward momentum (recoil) of the cannon, ensuring the total momentum of the system remains zero.

$
(m_{cannon} + m_{projectile}) \vec{v}_{initial} = m_{cannon} \vec{v}_{cannon, final} + m_{projectile} \vec{v}_{projectile, final}
$
If $\vec{v}_{initial} = 0$, then $0 = m_{cannon} \vec{v}_{cannon, final} + m_{projectile} \vec{v}_{projectile, final}$.

### C. Recoil
Recoil is a direct application of momentum conservation, particularly evident when objects push off each other, like a gun firing a bullet or a rocket expelling exhaust. The momentum of the expelled mass (bullet, exhaust) in one direction is balanced by the momentum of the remaining object (gun, rocket) in the opposite direction.

## IV. Connection to Impulse
Recall that [[Change in Momentum and Impulse]] is defined as $\vec{J} = \Delta \vec{P} = \vec{F}_{net} \Delta t$.
If the net external force $\vec{F}_{net}$ acting on a system is zero, then the impulse $\vec{J}$ is zero. This implies that the change in momentum $\Delta \vec{P}$ is also zero, meaning the total momentum $\vec{P}$ remains constant. This reinforces the principle of momentum conservation.