
# [[AP Physics C Home]]
# Topic 2.7: Kinetic and Static Friction

Friction is a resistive force that acts parallel to the surfaces in contact, opposing the relative motion (or attempted motion) between them. In AP Physics C, understanding the distinction between static and kinetic friction is critical for solving problems involving [[Forces and Free-Body Diagrams]] and [[Newtons Second Law]].

## The Nature of Friction
Friction arises from the microscopic interactions between the surfaces of two objects. Even surfaces that appear smooth have irregularities that collide or bond when in contact. The magnitude of the frictional force is generally proportional to the **normal force** ($F_N$), which represents the pressing together of the two surfaces.

## Static Friction ($f_s$)
Static friction acts on an object that is at rest or not sliding relative to the surface. It is a "self-adjusting" force; it increases to match the applied force until it reaches a maximum threshold.

*   **Behavior:** As long as the object does not move, the static frictional force $f_s$ exactly balances the component of the applied force parallel to the surface.
*   **The Threshold:** Once the applied force exceeds the maximum possible static friction ($f_{s,max}$), the object begins to move.

The relationship is expressed as:
$$f_s \leq \mu_s F_N$$

Where:
*   $f_{s,max} = \mu_s F_N$ is the maximum static friction before slipping occurs.
*   $\mu_s$ is the **coefficient of static friction**, a dimensionless constant determined by the two materials in contact.

## Kinetic Friction ($f_k$)
Kinetic friction (or sliding friction) acts when the two surfaces are in relative motion. Unlike static friction, kinetic friction is generally constant regardless of how fast the object is moving (up to a point).

The relationship is defined as:
$$f_k = \mu_k F_N$$

Where:
*   $\mu_k$ is the **coefficient of kinetic friction**.
*   Typically, $\mu_k < \mu_s$ for any given pair of surfaces, which explains why it is harder to *start* moving a heavy object than it is to *keep* it moving.

## Comparison Table

| Feature | Static Friction ($f_s$) | Kinetic Friction ($f_k$) |
| :--- | :--- | :--- |
| **Motion** | Zero relative motion | Relative motion present |
| **Magnitude** | Variable ($0$ to $\mu_s F_N$) | Constant ($\mu_k F_N$) |
| **Coefficient** | $\mu_s$ (Static) | $\mu_k$ (Kinetic) |
| **Direction** | Opposes *intended* motion | Opposes *actual* motion |

## Key Concepts for Problem Solving
When analyzing systems with friction, consider the following:

1.  **Direction:** Always draw the friction vector opposite to the direction of the relative velocity or the tendency to move.
2.  **Normal Force:** Do not assume $F_N = mg$. If an object is on an incline, $F_N = mg \cos(\theta)$. If there are vertical applied forces, $F_N$ must be calculated using [[Newtons Second Law]] in the y-direction.
3.  **Transitions:** In problems involving potential movement, always check the condition of the system. Calculate the applied force and compare it to $f_{s,max}$. If $F_{applied} > \mu_s F_N$, then the object accelerates, and you must use $f_k$ for your equations of motion.

For a broader discussion on forces that oppose motion, see [[Resistive Forces]].