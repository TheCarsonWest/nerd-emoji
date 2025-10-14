# [[AP Physics Home]]
# AP Physics Note Page: Topic 8.3 - Fluids and Newton’s Laws

This topic explores how the fundamental principles of [[Newton’s Second Law]] and [[Newton’s Third Law]] apply to systems involving fluids, building upon our understanding of forces and motion. We'll examine concepts like density, pressure, and buoyancy, understanding how fluids exert forces and respond to external forces.

## 1. Density ($\rho$)

Density is a fundamental property of a substance, defining how much mass is contained within a given volume. It's crucial for understanding fluid behavior.

*   **Definition**: Mass per unit volume.
*   **Formula**:
    $ \rho = \frac{m}{V} $
    Where:
    *   $\rho$ (rho) is the density (kg/m$^3$)
    *   $m$ is the mass (kg)
    *   $V$ is the volume (m$^3$)
*   **Significance**: Denser objects or fluids have more mass packed into the same space. For example, steel is denser than water.

## 2. Pressure ($P$)

Pressure is the force exerted perpendicularly on a surface per unit area. In fluids, pressure acts in all directions.

*   **Definition**: Force per unit area perpendicular to the surface.
*   **Formula**:
    $ P = \frac{F}{A} $
    Where:
    *   $P$ is the pressure (Pascals, Pa = N/m$^2$)
    *   $F$ is the perpendicular force (N)
    *   $A$ is the area over which the force is distributed (m$^2$)
*   **Units**: The SI unit for pressure is the Pascal (Pa). Other common units include atmospheres (atm) and pounds per square inch (psi).
*   **Pressure in a Fluid at Rest (Hydrostatic Pressure)**:
    For a fluid at rest, the pressure increases with depth due to the weight of the fluid above it.
    $ P = P_0 + \rho g h $
    Where:
    *   $P$ is the pressure at depth $h$
    *   $P_0$ is the pressure at the surface (often atmospheric pressure)
    *   $\rho$ is the fluid density
    *   $g$ is the acceleration due to gravity
    *   $h$ is the depth
*   [[Atmospheric Pressure]]: The pressure exerted by the weight of the air in the atmosphere. At sea level, it's approximately $1.01 \times 10^5$ Pa.

## 3. Buoyancy and Archimedes’ Principle

Buoyancy is an upward force exerted by a fluid that opposes the weight of an immersed object. This force is a direct consequence of the pressure difference within the fluid.

*   **Buoyant Force ($F_B$)**: The net upward force exerted by a fluid on an object.
*   **Archimedes' Principle**: States that the buoyant force on an object submerged (partially or fully) in a fluid is equal to the weight of the fluid displaced by the object.
    $ F_B = \rho_{fluid} V_{displaced} g $
    Where:
    *   $F_B$ is the buoyant force (N)
    *   $\rho_{fluid}$ is the density of the fluid (kg/m$^3$)
    *   $V_{displaced}$ is the volume of the fluid displaced by the object (equal to the volume of the submerged part of the object) (m$^3$)
    *   $g$ is the acceleration due to gravity (m/s$^2$)

### Applying Newton's Laws to Buoyancy

When an object is in a fluid, its motion (or lack thereof) is governed by the forces acting on it, which include its weight and the buoyant force. We use [[Forces and Free-Body Diagrams]] to analyze these situations.

*   **Floating**: An object floats if $F_B \ge mg$. This occurs when the object's average density is less than or equal to the fluid's density. In equilibrium, $F_B = mg$.
    *   If $\rho_{object} < \rho_{fluid}$, the object floats with part of its volume submerged.
    *   If $\rho_{object} = \rho_{fluid}$, the object is neutrally buoyant (can remain at any depth).
*   **Sinking**: An object sinks if $F_B < mg$. This occurs when the object's average density is greater than the fluid's density. The net force is downward, causing acceleration.
    *   The net force is $F_{net} = mg - F_B$ (downward).

| State     | Condition (Forces) | Condition (Densities)         |
| :-------- | :----------------- | :---------------------------- |
| Floats    | $F_B \ge mg$       | $\rho_{object} \le \rho_{fluid}$ |
| Sinks     | $F_B < mg$         | $\rho_{object} > \rho_{fluid}$   |

## 4. Continuity Equation (Revisited in Fluids and Conservation Laws)

While primarily discussed in [[Fluids and Conservation Laws]], the concept of fluid flow, where mass is conserved, is related to how fluids behave under forces. The continuity equation describes the conservation of mass in fluid flow:
$ A_1 v_1 = A_2 v_2 $
Where $A$ is the cross-sectional area and $v$ is the fluid speed. This implies that for an incompressible fluid, where the area decreases, the speed must increase, affecting the forces experienced by the fluid.