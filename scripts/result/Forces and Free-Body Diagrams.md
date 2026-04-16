
# [[AP Physics C Home]]
# Topic 2.2: Forces and Free-Body Diagrams

Forces are the fundamental interactions that cause objects to accelerate, deform, or change their state of motion. Understanding how to identify, categorize, and represent these forces is the cornerstone of classical mechanics.

## Understanding Force
A force is a vector quantity defined as a push or a pull upon an object resulting from the object's interaction with another object. Because it is a vector, it possesses both magnitude and direction. In the SI system, forces are measured in Newtons ($N$), where $1 N = 1 kg \cdot m/s^2$.

Forces are generally categorized into two types:
1. **Contact Forces:** Arise from physical contact between objects (e.g., friction, tension).
2. **Field Forces:** Act over a distance without physical contact (e.g., [[Gravitational Force]], electric forces, magnetic forces).

## Free-Body Diagrams (FBDs)
A Free-Body Diagram is a vital conceptual tool used to visualize all forces acting on a single object. When constructing an FBD, follow these steps:
1. **Isolate the Object:** Draw the object of interest alone, removing all surrounding surfaces or constraints.
2. **Represent as a Point:** Treat the object as a point mass (particle model) located at the origin of a coordinate system.
3. **Draw Vectors:** Draw arrows originating from the center of the mass pointing in the direction of each force. The length of the arrow should be proportional to the magnitude of the force.
4. **Label Clearly:** Every vector must be clearly labeled (e.g., $F_g$ for weight, $F_T$ for tension).

### Common Force Notation
| Force Name | Symbol | Description |
| :--- | :--- | :--- |
| Gravitational Force | $F_g$ or $mg$ | The weight of an object due to gravity. |
| Normal Force | $F_N$ | Perpendicular support force from a surface. |
| Tension | $F_T$ or $T$ | Pulling force transmitted through a string/rope. |
| Friction | $f_s$ or $f_k$ | Resistive force parallel to surfaces. |
| Applied Force | $F_{app}$ | An external push or pull. |

## Applying Newton's Laws
Once the FBD is complete, we apply [[Newtons Second Law]] to solve for unknown variables. The net force is the vector sum of all individual forces:
$$\sum \vec{F} = m\vec{a}$$

To solve these problems mathematically, decompose the force vectors into their respective x and y components using trigonometry:
$$F_x = F \cos(\theta)$$
$$F_y = F \sin(\theta)$$

After decomposition, set up the equations of motion for each axis separately:
$$\sum F_x = m a_x$$
$$\sum F_y = m a_y$$

If the object is in equilibrium (not accelerating), then $\sum F = 0$. If the object is accelerating, the sum equals $ma$. Always ensure your coordinate system is aligned with the direction of acceleration whenever possible to simplify the algebraic process.

For a deeper dive into the specific dynamics governing these interactions, see [[Newtons First Law]] and [[Newtons Third Law]].