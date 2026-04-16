
# [[AP Physics C Home]]
# AP Physics C: Work (Topic 3.2)

Work is a fundamental concept in physics that connects the application of a force to the change in an object's energy. In AP Physics C, we treat work not just as "force times distance," but as the integral of force over a displacement path.

## Definition of Work
Work ($W$) is defined as the scalar product of the force vector ($\vec{F}$) and the displacement vector ($d\vec{r}$). When a constant force is applied, this simplifies to the familiar dot product formula.

### The Work Formula
For a constant force:
$$W=\vec{F} \cdot \Delta\vec{r} = F \Delta r \cos(\theta)$$

Where:
*   $F$ is the magnitude of the force.
*   $\Delta r$ is the displacement.
*   $\theta$ is the angle between the force vector and the displacement vector.

For a variable force (which is critical in AP Physics C), we must use integration:
$$W=\int_{r_1}^{r_2} \vec{F}(r) \cdot d\vec{r}$$

## The Dot Product and Angle
Because work is the dot product of two vectors, the resulting value is a scalar. The angle $\theta$ determines the sign of the work:

| Angle ($\theta$) | $\cos(\theta)$ | Work Sign | Meaning |
| :--- | :--- | :--- | :--- |
| $0^\circ \leq \theta < 90^\circ$ | Positive | Positive | Force aids motion (adding energy). |
| $\theta = 90^\circ$ | 0 | Zero | Force is perpendicular to motion (no work). |
| $90^\circ < \theta \leq 180^\circ$ | Negative | Negative | Force opposes motion (removing energy). |

## Work-Energy Theorem
The [[Work]] done on an object by the *net* force is equivalent to the change in the object's kinetic energy. This is a powerful problem-solving tool that allows us to bypass kinematic equations when forces vary or when the path is complex.

$$W_{net} = \Delta K = K_f - K_i$$

Where $K = \frac{1}{2}mv^2$.

## Work Done by Specific Forces
It is important to categorize work based on the type of force:

1.  **Work by Gravity:** Near Earth's surface, gravity is constant.
    $$W_g = -mg \Delta y$$
    This is path-independent, leading into the concept of [[Potential Energy]].
2.  **Work by Springs:** Springs exert a variable force governed by Hooke's Law ($F_s = -kx$). The work done *by the spring* is:
    $$W_s = -\frac{1}{2}k(x_f^2 - x_i^2)$$
3.  **Work by Friction:** Friction always acts opposite to the direction of motion. Therefore, work done by kinetic friction is always negative and results in energy being "lost" as thermal energy.

## Important Considerations
*   **Units:** The SI unit for work is the Joule ($J$), where $1 J = 1 N \cdot m$.
*   **Directionality:** Always remember that work is a scalar, but it can be negative. Negative work indicates that the force is removing kinetic energy from the system, often by transferring it into other forms like heat or [[Potential Energy]].
*   **Calculus Application:** When given a position-dependent force function, such as $F(x) = 3x^2$, you must perform the integral $\int F(x)dx$ over the interval to calculate work.