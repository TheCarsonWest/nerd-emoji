
# [[AP Physics C Home]]
# Topic 2.8: Spring Forces

Spring forces are a fundamental example of a "restoring force"—a force that acts to bring a system back to its equilibrium position. In AP Physics C, understanding these forces is crucial for both mechanics and later units on oscillations.

## Hooke's Law

The primary relationship governing ideal springs is **Hooke's Law**. It states that the force exerted by a spring is directly proportional to the displacement of the spring from its equilibrium position.

The equation for Hooke's Law is:
$$F_s = -kx$$

### Variables Breakdown
| Variable | Definition | SI Unit |
| :--- | :--- | :--- |
| $F_s$ | The force exerted by the spring | Newtons (N) |
| $k$ | The spring constant (stiffness) | N/m |
| $x$ | Displacement from equilibrium | Meters (m) |

**Important Note on the Negative Sign:**
The negative sign indicates that the force is a **restoring force**. If you stretch the spring (positive $x$), the spring pulls back in the negative direction. If you compress the spring (negative $x$), the spring pushes back in the positive direction.

[[Calculating the Spring Constant from Experimental Data]]

## Springs and Work
Because the force of a spring is non-constant (it changes as $x$ changes), we cannot simply use $W = Fd$. Instead, we must use calculus to integrate the force over the distance.

The work done *by* the spring as it moves from an initial position $x_i$ to a final position $x_f$ is:
$$W_s = \int_{x_i}^{x_f} (-kx) \, dx = -\frac{1}{2}kx_f^2 + \frac{1}{2}kx_i^2$$

This leads directly to the concept of Elastic Potential Energy, which you can explore further in [[Potential Energy]].

## The Spring-Mass System
When a spring is attached to a mass, it forms a dynamic system often analyzed using [[Newtons Second Law]]. If the mass is displaced and released on a frictionless surface, it will exhibit simple harmonic motion.

The net force acting on the mass at any point $x$ is:
$$\sum F = ma = -kx$$

Rearranging this gives a differential equation:
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = 0$$

Solving this equation is fundamental to understanding [[Defining Simple Harmonic Motion (SHM)]].

## Important Considerations for AP Physics C
1.  **Ideal Springs:** Unless otherwise stated, assume springs are "massless" and "ideal" (they obey Hooke's Law perfectly and do not dissipate energy via heat).
2.  **Vertical Springs:** When a spring is suspended vertically, gravity adds a constant force ($mg$). The equilibrium position shifts downward by an amount $\Delta x = \frac{mg}{k}$. When analyzing motion, it is often easiest to define the new equilibrium position as the new "zero" point for your coordinate system.
3.  **Forces:** Always remember to draw your [[Forces and Free-Body Diagrams]] carefully. The spring force vector always points toward the equilibrium position, regardless of the direction of motion.