
# [[AP Physics C Home]]
# Topic 12.3: Magnetism and Current-Carrying Wires

When electric current flows through a wire, it generates its own magnetic field. This is the fundamental principle behind electromagnets, motors, and many other electrical devices. Understanding how current-carrying wires interact with external magnetic fields is crucial for AP Physics C.

## The Magnetic Force on a Current-Carrying Wire

If a wire carrying a current $I$ is placed within an external magnetic field $\vec{B}$, the field exerts a force on the moving charges within the wire. This force, known as the Lorentz force, acts on the entire segment of the wire.

The magnitude of the magnetic force $F_B$ on a straight segment of wire of length $L$ is given by:

$$F_B = ILB \sin(\theta)$$

In vector form, this is expressed as:

$$\vec{F_B} = I(\vec{L} \times \vec{B})$$

Where:
*   $I$ is the current (Amperes).
*   $\vec{L}$ is a vector representing the length of the wire segment, with a direction aligned with the conventional current.
*   $\vec{B}$ is the external magnetic field vector (Tesla).
*   $\theta$ is the angle between the wire's length vector $\vec{L}$ and the magnetic field $\vec{B}$.

### Determining Direction
To find the direction of the force, we use the [[Right-Hand Rule]]. Point your fingers in the direction of the current $I$ (the direction of $\vec{L}$), then curl them in the direction of the magnetic field $\vec{B}$. Your thumb will point in the direction of the magnetic force $\vec{F_B}$.

## Magnetic Fields Created by Wires

Not only are wires affected by magnetic fields, but they also create their own. The shape of the wire determines the shape of the magnetic field generated.

| Wire Geometry | Magnetic Field Formula | Key Notes |
| :--- | :--- | :--- |
| **Long Straight Wire** | $$B = \frac{\mu_0 I}{2 \pi r}$$ | Field circles the wire; use Right-Hand Rule to find direction. |
| **Center of Current Loop** | $$B = \frac{\mu_0 I}{2R}$$ | Field is perpendicular to the plane of the loop. |
| **Solenoid (Interior)** | $$B = \mu_0 n I$$ | $n = N/L$ (turns per unit length). Relatively uniform field. |

*   $\mu_0$ is the permeability of free space: $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$.
*   $r$ is the radial distance from the wire.
*   $R$ is the radius of the current loop.

## Force Between Two Parallel Wires

When two parallel wires carry current, each creates a magnetic field that exerts a force on the other. This interaction creates an attractive or repulsive force per unit length:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2 \pi d}$$

*   **Rule of Thumb:** Parallel currents in the *same* direction attract each other; parallel currents in *opposite* directions repel each other.

For a deeper understanding of how these fields are derived mathematically, see [[Ampere's Law]].