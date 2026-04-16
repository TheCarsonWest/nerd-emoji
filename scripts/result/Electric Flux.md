
# [[AP Physics C Home]]
# Topic 8.5: Electric Flux

Electric flux is a fundamental concept in electromagnetism that quantifies the amount of electric field passing through a specific surface. It serves as the gateway to understanding [[Gausss Law]], which is a powerful tool for calculating electric fields in highly symmetric charge distributions.

## Defining Electric Flux

Conceptually, electric flux ($\Phi_E$) can be visualized as the number of electric field lines piercing a given surface. If the surface is perpendicular to the field, the flux is maximized. If the surface is parallel to the field, no lines pierce it, and the flux is zero.

### The Scalar Product Definition

For a flat surface of area $A$ in a uniform electric field $\vec{E}$, the electric flux is the scalar (dot) product of the electric field vector and the area vector $\vec{A}$:

$$\Phi_E = \vec{E} \cdot \vec{A} = EA \cos(\theta)$$

In this equation:
*   $\vec{A}$ is a vector whose magnitude is the area of the surface and whose direction is perpendicular (normal) to the surface.
*   $\theta$ is the angle between the electric field vector $\vec{E}$ and the normal vector $\vec{A}$.

| Scenario | Angle ($\theta$) | Flux ($\Phi_E$) |
| :--- | :--- | :--- |
| $\vec{E}$ is perpendicular to the surface | $0^\circ$ | $EA$ (Maximum) |
| $\vec{E}$ is parallel to the surface | $90^\circ$ | $0$ (Minimum) |
| $\vec{E}$ is at an angle | $\theta$ | $EA \cos(\theta)$ |

## Generalizing for Non-Uniform Fields and Curved Surfaces

When the electric field is not uniform or the surface is curved, we cannot use the simple dot product formula. Instead, we must use calculus. We divide the surface into an infinite number of infinitesimal area elements $d\vec{A}$. The total flux is the sum of these infinitesimal contributions:

$$\Phi_E = \int \vec{E} \cdot d\vec{A}$$

### Closed Surfaces

A special case of great importance in physics involves a *closed surface* (a surface that encloses a volume, such as a sphere or a cube). For a closed surface, we use a specific notation for the integral to indicate the surface is closed:

$$\Phi_E = \oint \vec{E} \cdot d\vec{A}$$

By convention, the area vector $d\vec{A}$ for a closed surface always points **outward** from the volume.

*   If the net flux is positive, there is a net outward flow of field lines, implying a net positive charge enclosed.
*   If the net flux is negative, there is a net inward flow, implying a net negative charge enclosed.
*   If the net flux is zero, the amount of field entering the surface equals the amount leaving, implying no net enclosed charge.

This relationship between the flux through a closed surface and the enclosed charge is the precise foundation of [[Gausss Law]].