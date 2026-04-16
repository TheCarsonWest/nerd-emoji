
# [[AP Physics C Home]]
# AP Physics C: Systems and Center of Mass

## Introduction to Systems

In physics, a **system** is a collection of objects chosen for analysis. Defining a system is crucial for applying fundamental principles like [[Conservation of Linear Momentum]] or [[Conservation of Energy]]. The objects within the system are subject to **internal forces** (forces between objects in the system) and **external forces** (forces exerted by objects outside the system). Only external forces can change the total momentum or energy of a closed system.

## Center of Mass (CM)

The **center of mass (CM)** is a unique point in a system or object that represents the average position of all the mass in the system. For many purposes, a system can be treated as if all its mass is concentrated at its center of mass, and all external forces act at this point. This greatly simplifies the analysis of complex systems, especially when considering [[Translational Kinetic Energy]] and the overall motion of the system.

**Key Properties of the CM:**
*   It simplifies the application of [[Newtons Second Law]] to extended objects or systems.
*   The CM of a system follows a path determined by the net external force acting on the system, regardless of internal forces or the motion of individual parts.
*   For symmetrical objects with uniform density, the CM is at the geometric center.

## Calculating the Center of Mass

### Discrete Particle Systems

For a system consisting of $N$ discrete particles with masses $m_1, m_2, \dots, m_N$ located at positions $\vec{r}_1, \vec{r}_2, \dots, \vec{r}_N$, the position vector of the center of mass, $\vec{r}_{CM}$, is given by:

$$ \vec{r}_{CM} = \frac{\sum_{i=1}^{N} m_i \vec{r}_i}{M} $$

Where $M = \sum_{i=1}^{N} m_i$ is the total mass of the system. In component form, this can be written as:

$$ x_{CM} = \frac{\sum_{i=1}^{N} m_i x_i}{M} $$
$$ y_{CM} = \frac{\sum_{i=1}^{N} m_i y_i}{M} $$
$$ z_{CM} = \frac{\sum_{i=1}^{N} m_i z_i}{M} $$

### Continuous Mass Distributions

For objects with a continuous mass distribution, we replace the summation with an integral. Consider an infinitesimally small mass element $dm$ at position $\vec{r}$:

$$ \vec{r}_{CM} = \frac{1}{M} \int \vec{r} \, dm $$

Again, in component form:

$$ x_{CM} = \frac{1}{M} \int x \, dm $$
$$ y_{CM} = \frac{1}{M} \int y \, dm $$
$$ z_{CM} = \frac{1}{M} \int z \, dm $$

To evaluate these integrals, $dm$ must be expressed in terms of the position coordinates. This often involves using mass densities:
*   **Linear mass density ($\lambda$)**: $dm = \lambda \, dl$ (for 1D objects like rods)
*   **Surface mass density ($\sigma$)**: $dm = \sigma \, dA$ (for 2D objects like plates)
*   **Volume mass density ($\rho$)**: $dm = \rho \, dV$ (for 3D objects)

[[Integration]] techniques are essential for solving these types of problems.

## Velocity and Acceleration of the Center of Mass

The velocity of the center of mass, $\vec{v}_{CM}$, is the time derivative of its position vector:

$$ \vec{v}_{CM} = \frac{d\vec{r}_{CM}}{dt} = \frac{\sum_{i=1}^{N} m_i \vec{v}_i}{M} = \frac{\vec{P}_{total}}{M} $$

Where $\vec{v}_i$ is the velocity of particle $i$, and $\vec{P}_{total} = \sum m_i \vec{v}_i$ is the total linear momentum of the system.

Similarly, the acceleration of the center of mass, $\vec{a}_{CM}$, is the time derivative of its velocity vector:

$$ \vec{a}_{CM} = \frac{d\vec{v}_{CM}}{dt} = \frac{\sum_{i=1}^{N} m_i \vec{a}_i}{M} $$

Where $\vec{a}_i$ is the acceleration of particle $i$.

## Newton's Second Law for a System

Applying [[Newtons Second Law]] to the system as a whole, considering only external forces:

$$ \vec{F}_{net, ext} = M \vec{a}_{CM} $$

Here, $\vec{F}_{net, ext}$ is the net external force acting on the system, and $M$ is the total mass of the system. This powerful equation states that the center of mass of a system moves as if all the system's mass were concentrated at that point and all external forces were applied there. Internal forces cancel out in pairs due to [[Newtons Third Law]] and therefore do not affect the motion of the center of mass. This is a fundamental concept in analyzing collisions and explosions.