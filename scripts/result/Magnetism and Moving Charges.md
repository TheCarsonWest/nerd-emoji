
# [[AP Physics C Home]]
# Magnetism and Moving Charges

The interaction between magnetic fields and moving charges is a fundamental concept in electromagnetism. Unlike electric fields, which exert forces on charges whether they are moving or stationary, magnetic fields only exert forces on charges that are in motion.

## The Magnetic Force on a Moving Charge

When a particle with charge $q$ moves with velocity $\mathbf{v}$ through a uniform magnetic field $\mathbf{B}$, it experiences a magnetic force $\mathbf{F}_B$. This force is described by the Lorentz force law (specifically the magnetic component):

$$\mathbf{F}_B = q(\mathbf{v} \times \mathbf{B})$$

The magnitude of this force is given by:

$$F_B = |q|vB\sin(\theta)$$

Where:
*   $q$ is the charge of the particle (Coulombs).
*   $v$ is the speed of the particle (m/s).
*   $B$ is the magnetic field strength (Tesla, T).
*   $\theta$ is the angle between the velocity vector $\mathbf{v}$ and the magnetic field vector $\mathbf{B}$.

### Directionality and the Right-Hand Rule
The cross product $\mathbf{v} \times \mathbf{B}$ dictates that the force is always perpendicular to both the velocity of the particle and the magnetic field. To determine the direction of the force, use the **Right-Hand Rule (RHR)**:
1. Point your fingers in the direction of the velocity vector $\mathbf{v}$.
2. Curl your fingers toward the magnetic field vector $\mathbf{B}$.
3. Your extended thumb points in the direction of the force $\mathbf{F}_B$ for a *positive* charge. 
*Note: If the charge is negative, the force is in the exact opposite direction of your thumb.*

## Motion of Charges in a Magnetic Field

Because the magnetic force is always perpendicular to velocity, it cannot change the speed or kinetic energy of the particle; it acts as a centripetal force, changing only the direction of motion. This leads to [[Uniform Circular Motion]] for charged particles in a uniform magnetic field.

When the velocity is perpendicular to the field ($\theta = 90^\circ$), the particle moves in a circle. Setting the magnetic force equal to the centripetal force ($F_c = \frac{mv^2}{r}$):

$$|q|vB = \frac{mv^2}{r}$$

Solving for the radius ($r$) of the particle's path:

$$r = \frac{mv}{|q|B}$$

This relationship is crucial in [[Mass Spectrometry]] and cyclotron design, where the radius depends directly on the particle's momentum ($p=mv$).

## Summary Table of Forces

| Force Type | Formula | Dependence on Motion |
| :--- | :--- | :--- |
| **Electric Force** | $\mathbf{F}_E = q\mathbf{E}$ | Independent of velocity |
| **Magnetic Force** | $\mathbf{F}_B = q(\mathbf{v} \times \mathbf{B})$ | Dependent on velocity |

## Applications
The principles of magnetism and moving charges are applied across various technologies:
*   **Cathode Ray Tubes (CRT):** Using magnetic fields to steer electron beams.
*   **Particle Accelerators:** Utilizing magnetic fields to confine and guide high-energy particles.
*   **Velocity Selectors:** Combining [[Electric Fields]] and magnetic fields to allow only particles of a specific velocity to pass through undeflected.