
# [[AP Physics C Home]]
# AP Physics C: Resistive Forces

Resistive forces, also known as drag forces or fluid resistance, are forces that oppose the relative motion of an object through a fluid (liquid or gas). Unlike kinetic friction which acts between two solid surfaces, resistive forces depend on the velocity of the object and the properties of the fluid.

## Types of Resistive Forces

There are two primary models for resistive forces depending on the velocity of the object: linear drag and quadratic (or turbulent) drag.

| Drag Type | Typical Context | Relationship to Velocity |
| :--- | :--- | :--- |
| **Linear Drag** | Small objects moving at low speeds (e.g., oil, slow-moving viscous fluid) | Proportional to $v$ |
| **Quadratic Drag** | Larger objects moving at high speeds (e.g., air, water) | Proportional to $v^2$ |

### Linear Drag
For low-speed motion, the resistive force is modeled as:
$$ \vec{F}_r = -b\vec{v} $$
Where $b$ is a constant that depends on the properties of the fluid and the shape of the object, and $\vec{v}$ is the velocity. The negative sign indicates the force acts opposite to the direction of motion.

### Quadratic Drag
For high-speed motion, the resistive force is modeled as:
$$ \vec{F}_r = -\frac{1}{2}D\rho A v^2 $$
Where $D$ is the drag coefficient, $\rho$ is the density of the fluid, $A$ is the cross-sectional area, and $v$ is the speed. Because of the $v^2$ dependence, resistive force increases rapidly as speed increases.

## Terminal Velocity
As an object falls through a fluid, it accelerates until the resistive force equals the gravitational force. At this point, the net force is zero, and the object reaches its maximum constant speed, known as **terminal velocity**.

[[Terminal Velocity Analysis]]

To determine the terminal velocity, one must apply [[Newtons Second Law]]. For an object falling under linear drag:

1. Sum of forces: $\sum F_y = mg - bv_t = ma$
2. At terminal velocity, $a = 0$.
3. Solving for $v_t$:
$$ v_t = \frac{mg}{b} $$

For quadratic drag, the process is similar:
$$ mg - \frac{1}{2}D\rho A v_t^2 = 0 $$
$$ v_t = \sqrt{\frac{2mg}{D\rho A}} $$

## Solving Equations of Motion
Because resistive forces depend on velocity, the acceleration is not constant. This means standard kinematic equations do not apply. To find position or velocity as a function of time, one must set up a differential equation using [[Newtons Second Law]] and integrate. 

Often, you will need to rearrange the equation to the form $a = \frac{dv}{dt}$ and separate variables to solve for $v(t)$. This is a critical skill for AP Physics C, as it bridges the gap between basic mechanics and calculus-based physics.

*See also related topics:*
* [[Forces and Free-Body Diagrams]]
* [[Kinetic and Static Friction]]