# [[AP Physics Home]]
# AP Physics Note Page: Topic 2.2 Forces and Free-Body Diagrams

## Introduction to Forces

A **force** is a push or a pull exerted on an object. It is a vector quantity, meaning it has both magnitude and direction. Forces are responsible for changing an object's state of motion (acceleration), or deforming it. The standard unit for force in the International System of Units (SI) is the Newton (N).

Forces can be categorized into two main types:
*   **Contact Forces:** These occur when objects physically touch each other (e.g., friction, normal force, tension, applied force).
*   **Non-Contact (Field) Forces:** These forces act over a distance without physical contact (e.g., gravitational force, electrostatic force, magnetic force).

For a deeper understanding of vector properties, refer to [[Scalars and Vectors in One Dimension]] and [[Vectors and Motion in Two Dimensions]].

## Types of Forces

Here are some common types of forces encountered in AP Physics:

| Force Type          | Symbol   | Description                                                                                              |
| :------------------ | :------- | :------------------------------------------------------------------------------------------------------- |
| **Applied Force**   | $F_A$    | A force directly applied to an object by a person or another object.                                     |
| **Normal Force**    | $F_N$    | A contact force perpendicular to the surface of contact, preventing objects from passing through surfaces. |
| **Friction Force**  | $F_f$    | A contact force parallel to the surface, opposing relative motion or its tendency.                       |
| **Tension Force**   | $F_T$    | The force transmitted through a string, rope, cable, or wire when pulled tight.                          |
| **Gravitational Force** | $F_g$ (or $W$) | The attractive force between any two objects with mass. On Earth, it's an object's weight.               |
| **Spring Force**    | $F_s$    | The restorative force exerted by a spring, proportional to its displacement from equilibrium.            |

For more details on specific forces, see [[Gravitational Force]] and [[Spring Forces]].

## Net Force

The **net force** ($\Sigma \vec{F}$ or $\vec{F}_{net}$) on an object is the vector sum of all individual forces acting on it. It determines the object's acceleration according to [[Newton’s Second Law]].

Mathematically, if multiple forces $\vec{F_1}, \vec{F_2}, ..., \vec{F_n}$ act on an object:
$
\vec{F}_{net} = \sum \vec{F} = \vec{F_1} + \vec{F_2} + ... + \vec{F_n}
$
In component form, for 2D motion:
$
\sum F_x = F_{1x} + F_{2x} + ... + F_{nx}
$
$
\sum F_y = F_{1y} + F_{2y} + ... + F_{ny}
$
The magnitude of the net force is $|\vec{F}_{net}| = \sqrt{(\sum F_x)^2 + (\sum F_y)^2}$.

## Free-Body Diagrams (FBDs)

[[Free-Body Diagrams]] are essential tools in mechanics for visualizing all forces acting *on a single object*. They help simplify complex scenarios and apply Newton's Laws correctly.

### Steps to Draw a Free-Body Diagram:

1.  **Isolate the Object:** Choose the specific object of interest.
2.  **Represent the Object:** Draw the object as a single point or a simplified box. This is crucial as FBDs show forces *acting on* the object, not forces *exerted by* it.
3.  **Identify All Forces:** Determine every force acting on the object. Ask yourself:
    *   Is there gravity? (Always present unless specified otherwise)
    *   Is the object touching any surfaces? (Normal force, friction)
    *   Is it being pulled by a rope/string? (Tension)
    *   Is something pushing or pulling it directly? (Applied force)
    *   Is it attached to a spring? (Spring force)
4.  **Draw Force Vectors:** For each identified force, draw an arrow originating from the center of the object (or point mass) pointing in the direction of the force.
    *   Label each vector clearly with its force symbol (e.g., $F_g$, $F_N$, $F_T$).
    *   The relative lengths of the arrows should roughly indicate the magnitudes of the forces.
5.  **Establish a Coordinate System:** Draw an x-y coordinate system. Align one axis with the direction of acceleration if possible (e.g., parallel to an incline).

### Example FBD: Block on an Incline

Consider a block resting on a rough inclined plane.
*   **Object:** The block.
*   **Forces:**
    *   **Gravitational Force ($F_g$):** Acts straight down.
    *   **Normal Force ($F_N$):** Perpendicular to the inclined surface, pushing up and away from it.
    *   **Static Friction Force ($F_f$):** Parallel to the inclined surface, opposing the tendency of motion (up the incline if the block tends to slide down).

The FBD would show these three arrows originating from the block, with $F_g$ pointing vertically down, $F_N$ perpendicular to the incline, and $F_f$ parallel to the incline. When analyzing, $F_g$ would typically be resolved into components parallel and perpendicular to the incline.