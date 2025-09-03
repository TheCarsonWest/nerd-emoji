# [[AP Physics Home]]
# AP Physics Note Page: Topic 8.2 Pressure

## Introduction to Pressure

Pressure is a fundamental concept in fluid mechanics and is crucial for understanding how forces are distributed within fluids (liquids and gases) and on surfaces in contact with them. Unlike solid objects where forces are often concentrated at specific points, forces exerted by fluids are distributed over an area.

## Definition of Pressure

Pressure ($P$) is defined as the magnitude of the normal (perpendicular) force ($F_\perp$) exerted by a fluid or on a surface, divided by the area ($A$) over which the force is distributed.

$
P = \frac{F_\perp}{A}
$

-   $F_\perp$: The component of force perpendicular to the surface (in Newtons, N).
-   $A$: The area over which the force is applied (in square meters, m$^2$).
-   $P$: Pressure (in Pascals, Pa).

Pressure is a [[Scalars and Vectors in One Dimension|scalar]] quantity, meaning it has magnitude but no direction. However, the force creating the pressure always acts perpendicular to the surface.

### Units of Pressure

The SI unit for pressure is the Pascal (Pa), defined as one Newton per square meter:
$
1 \text{ Pa} = 1 \frac{\text{N}}{\text{m}^2}
$

Other common units include:
-   **Atmosphere (atm)**: Average atmospheric pressure at sea level.
-   **Torr**: Often used in vacuum measurements.
-   **Pounds per square inch (psi)**: Common in engineering contexts, especially in the U.S.
-   **Bar**: Approximately equal to atmospheric pressure.

| Unit Name | Equivalence to Pascal (approx.) |
| :-------- | :------------------------------ |
| Pascal (Pa) | $1 \text{ N/m}^2$               |
| Atmosphere (atm) | $1.013 \times 10^5 \text{ Pa}$ |
| Torr | $133.32 \text{ Pa}$             |
| psi | $6894.76 \text{ Pa}$            |
| Bar | $1 \times 10^5 \text{ Pa}$      |

## Pressure in Fluids

For a fluid at rest, pressure acts equally in all directions at a given depth. This is a consequence of [[Newton’s Second Law]] and the molecular nature of fluids. Imagine a tiny cube within a fluid; if the pressure wasn't equal on all sides, the cube would accelerate.

### Absolute vs. Gauge Pressure

-   **Absolute Pressure ($P_{abs}$)**: The total pressure at a certain point, measured relative to a perfect vacuum. This is the pressure value used in most physics equations.
-   **Gauge Pressure ($P_{gauge}$)**: The pressure measured relative to the surrounding atmospheric pressure ($P_{atm}$). This is what most tire gauges or blood pressure cuffs measure.

The relationship between them is:
$
P_{abs} = P_{gauge} + P_{atm}
$
Where $P_{atm}$ is typically $1.013 \times 10^5 \text{ Pa}$ at sea level.

### Pressure Variation with Depth in a Fluid

For an incompressible fluid (density $\rho$ is constant) at rest under gravity, the pressure increases with depth. Consider a fluid column of height $h$. The pressure at a depth $h$ below the surface is given by:

$
P = P_0 + \rho g h
$

-   $P$: Pressure at depth $h$.
-   $P_0$: Pressure at the surface of the fluid (often atmospheric pressure if exposed to air).
-   $\rho$: Density of the fluid (in kg/m$^3$).
-   $g$: Acceleration due to gravity (approximately $9.8 \text{ m/s}^2$).
-   $h$: Depth below the surface (in meters).

This equation shows that:
1.  Pressure increases linearly with depth.
2.  Pressure is the same at all points at the same horizontal level within a continuous fluid.
3.  Pressure does not depend on the shape or volume of the container, only on the depth, fluid density, and surface pressure.

## [[Pascal's Principle]]

Pascal's Principle states that a pressure change applied to an enclosed incompressible fluid is transmitted undiminished to every portion of the fluid and to the walls of the containing vessel. This principle is fundamental to hydraulic systems.

If a force $F_1$ is applied to a small area $A_1$ in an enclosed fluid, it creates a pressure $P = F_1/A_1$. This pressure is transmitted throughout the fluid, meaning it exerts a force $F_2 = P A_2$ on a larger area $A_2$.
$
\frac{F_1}{A_1} = \frac{F_2}{A_2}
$
This allows a small force to generate a large force, enabling hydraulic lifts and brakes.

## Applications of Pressure

Pressure is a crucial concept in many areas, including:
-   **Weather forecasting**: Understanding atmospheric pressure systems.
-   **Medical devices**: Blood pressure monitors, intravenous drips.
-   **Engineering**: Design of dams, submarines, hydraulic systems.
-   **Aeronautics**: Lift generation in aircraft wings.
-   **Everyday life**: Drinking with straws, plunging a toilet.