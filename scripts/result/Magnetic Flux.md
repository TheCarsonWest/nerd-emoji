
# [[AP Physics C Home]]
# Topic 13.1: Magnetic Flux

Magnetic flux ($\Phi_B$) is a fundamental concept in electromagnetism that measures the total magnetic field passing through a given surface area. Conceptually, it represents the "number" of magnetic field lines passing through a loop or coil.

## Definition and Equation

Magnetic flux is defined as the dot product of the magnetic field vector and the area vector. The area vector, $\vec{A}$, is perpendicular to the surface of the loop, with a magnitude equal to the surface area.

The general equation for magnetic flux through a surface is:

$$\Phi_B = \int \vec{B} \cdot d\vec{A}$$

For a uniform magnetic field passing through a flat surface with area $A$, this simplifies to:

$$\Phi_B = B A \cos(\theta)$$

Where:
*   $\Phi_B$ is the magnetic flux (measured in Webers, $Wb$).
*   $B$ is the magnitude of the magnetic field (measured in Tesla, $T$).
*   $A$ is the area of the surface (measured in $m^2$).
*   $\theta$ is the angle between the magnetic field vector ($\vec{B}$) and the normal (perpendicular) vector to the surface area ($\vec{A}$).

### Important Considerations for $\theta$

It is a common error to measure $\theta$ relative to the plane of the loop rather than the normal vector. The table below summarizes the relationship between orientation and flux:

| Angle ($\theta$) | Orientation of $\vec{B}$ relative to $\vec{A}$ | Value of $\cos(\theta)$ | Resulting Flux ($\Phi_B$) |
| :--- | :--- | :--- | :--- |
| $0^\circ$ | Parallel to normal (perpendicular to loop) | $1$ | Maximum ($BA$) |
| $90^\circ$ | Perpendicular to normal (parallel to loop) | $0$ | Zero |
| $180^\circ$ | Anti-parallel to normal | $-1$ | Minimum ($-BA$) |

## Physical Significance

Magnetic flux is the scalar quantity that links the presence of magnetic fields to changes in electric potential. While the magnetic field itself cannot do work on a particle, changes in magnetic flux are the driving force behind electromagnetic induction.

### Understanding the Area Vector
The direction of the area vector $\vec{A}$ is determined by the "right-hand rule." If you curl the fingers of your right hand in the direction of the current flow around a loop, your thumb points in the direction of the vector $\vec{A}$. This convention is crucial when applying [[Electromagnetic Induction]] and [[Faradays Law]], where the direction of the induced EMF depends on the rate of change of flux ($\frac{d\Phi_B}{dt}$).

## Units and Relationships

*   **Weber ($Wb$):** The SI unit of magnetic flux, defined as $1\ T \cdot m^2$.
*   **Dimensional Analysis:** Since $[B] = \frac{F}{qv} = \frac{kg}{C \cdot s}$, flux has dimensions of $\frac{kg \cdot m^2}{A \cdot s^2}$.

This concept is the direct analog to [[Electric Flux]] studied in electrostatics. While Gauss's Law for electricity relates electric flux to enclosed charge, the magnetic version, Gauss's Law for Magnetism, states that the net magnetic flux through any closed surface is always zero:

$$\oint \vec{B} \cdot d\vec{A} = 0$$

This result implies that there are no "magnetic charges" or monopoles; magnetic field lines must always form continuous closed loops. Understanding this property is essential before moving on to [[Induced Currents and Magnetic Forces]].