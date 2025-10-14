# [[AP Physics Home]]
# Topic 4.4: Elastic and Inelastic Collisions

Collisions are fundamental interactions between two or more objects that exert forces on each other over a relatively short time. During a collision, the internal forces between the objects are typically much larger than any external forces, allowing us to often approximate the system as isolated during the impact.

## [[Conservation of Linear Momentum]]

A crucial principle in analyzing collisions is the [[Conservation of Linear Momentum]]. For any system of objects undergoing a collision, if the net external force on the system is zero, the total linear momentum of the system before the collision is equal to the total linear momentum of the system after the collision.

$
\vec{p}_{\text{total, initial}} = \vec{p}_{\text{total, final}}
$

For two objects (1 and 2):
$
m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f}
$
Where $m$ is mass, $\vec{v}$ is velocity, and subscripts $i$ and $f$ denote initial and final states, respectively.

## Types of Collisions

Collisions are primarily categorized by whether [[Translational Kinetic Energy]] is conserved.

### 1. Elastic Collisions

An **elastic collision** is a collision in which the total translational kinetic energy of the system is conserved, in addition to linear momentum. In such collisions, there is no net loss of kinetic energy, meaning no energy is converted into other forms like heat, sound, or deformation.

**Key Characteristics:**
*   **Momentum is conserved:** $m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f}$
*   **Kinetic Energy is conserved:** $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2$

**Example:** Collisions between billiard balls are often approximated as elastic. Collisions between atoms or subatomic particles are often perfectly elastic.

### 2. Inelastic Collisions

An **inelastic collision** is a collision in which linear momentum is conserved, but the total translational kinetic energy of the system is *not* conserved. Some of the initial kinetic energy is transformed into other forms of energy (e.g., heat, sound, potential energy of deformation) during the collision.

**Key Characteristics:**
*   **Momentum is conserved:** $m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = m_1\vec{v}_{1f} + m_2\vec{v}_{2f}$
*   **Kinetic Energy is NOT conserved:** $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 \neq \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2$
    *   Generally, $KE_{final} < KE_{initial}$

**Example:** A car crash, a bullet embedding itself in a block of wood. Most macroscopic collisions are inelastic to some degree.

### 3. Perfectly Inelastic Collisions

A **perfectly inelastic collision** is a specific type of inelastic collision where the colliding objects stick together after impact and move as a single combined mass. This results in the maximum possible loss of kinetic energy while still conserving momentum.

**Key Characteristics:**
*   **Momentum is conserved:** $m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = (m_1 + m_2)\vec{v}_{f}$
    *   Since they stick together, $v_{1f} = v_{2f} = v_f$.
*   **Kinetic Energy is NOT conserved:** $KE_{final} < KE_{initial}$ (maximum loss)

**Example:** A railway car coupling with another and moving together, a ball of clay hitting a wall and sticking to it.

## Summary Table

| Feature                 | Elastic Collision                               | Inelastic Collision                          | Perfectly Inelastic Collision                      |
| :---------------------- | :---------------------------------------------- | :------------------------------------------- | :------------------------------------------------- |
| **Momentum Conservation** | Yes                                             | Yes                                          | Yes                                                |
| **Kinetic Energy Conservation** | Yes                                             | No                                           | No (Max loss)                                      |
| **Objects Stick Together** | No                                              | No (usually, but can happen)                 | Yes                                                |
| **Energy Loss**         | None (ideal)                                    | Some transformed (heat, sound, deformation)  | Maximum transformed (heat, sound, deformation)     |
| **Equation (1D)**       | $m_1v_{1i} + m_2v_{2i} = m_1v_{1f} + m_2v_{2f}$ | $m_1v_{1i} + m_2v_{2i} = m_1v_{1f} + m_2v_{2f}$ | $m_1v_{1i} + m_2v_{2i} = (m_1 + m_2)v_{f}$         |
|                         | $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 = \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2$ | $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 \neq \frac{1}{2}m_1v_{1f}^2 + \frac{1}{2}m_2v_{2f}^2$ | $\frac{1}{2}m_1v_{1i}^2 + \frac{1}{2}m_2v_{2i}^2 > \frac{1}{2}(m_1 + m_2)v_{f}^2$ |

Understanding the distinction between these collision types is crucial for applying the correct conservation laws and solving problems involving interactions between objects.
