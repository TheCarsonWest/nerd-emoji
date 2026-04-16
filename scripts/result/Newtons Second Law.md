
# [[AP Physics C Home]]
# Newton's Second Law

Newton's Second Law is the cornerstone of classical mechanics. It provides the mathematical link between the forces acting on an object and the resulting motion of that object. While [[Newtons First Law]] describes motion when the net force is zero, Newton's Second Law describes how motion changes when the net force is non-zero.

## The Mathematical Definition

Newton's Second Law states that the acceleration of an object is directly proportional to the net force acting upon it and inversely proportional to the object's mass. The direction of the acceleration is the same as the direction of the net force.

The standard form of the equation is:

$$\sum \vec{F} = m\vec{a}$$

Where:
*   $\sum \vec{F}$ represents the vector sum of all forces (Net Force) in Newtons ($N$).
*   $m$ represents the inertial mass in kilograms ($kg$).
*   $\vec{a}$ represents the acceleration vector in meters per second squared ($m/s^2$).

### Components of Motion
Because force and acceleration are vectors, we often analyze them using component vectors in a Cartesian coordinate system. This is particularly useful when analyzing [[Forces and Free-Body Diagrams]].

| Component | Equation |
| :--- | :--- |
| **x-axis** | $\sum F_x = ma_x$ |
| **y-axis** | $\sum F_y = ma_y$ |
| **z-axis** | $\sum F_z = ma_z$ |

## Momentum and Force
In AP Physics C, it is important to recognize that Newton's original formulation of his second law was actually in terms of momentum ($p$). This definition is more general because it accounts for systems where mass might be changing (like a rocket burning fuel).

The relationship is defined as:

$$\vec{F}_{net} = \frac{d\vec{p}}{dt}$$

Since $\vec{p} = m\vec{v}$, if mass is constant, this derivative simplifies back to the familiar $F=ma$. You can find further details on this relationship in [[Change in Momentum and Impulse]].

## Applying the Law: A Systematic Approach
When solving problems involving Newton's Second Law, follow these steps to ensure accuracy:

1.  **Identify the System:** Clearly define which object or collection of objects you are analyzing.
2.  **Draw a Free-Body Diagram (FBD):** Sketch the object and draw all forces acting *on* it. Refer to [[Forces and Free-Body Diagrams]] for best practices.
3.  **Choose a Coordinate System:** Align your axes with the direction of acceleration if possible to simplify the math.
4.  **Write the Equations of Motion:** Apply Newton's Second Law to each axis independently.
5.  **Solve for Unknowns:** Use the resulting system of equations to solve for the target variable (often acceleration or tension).

## Special Considerations
*   **Massless Objects:** In many textbook problems, strings or pulleys are considered "massless." This implies that the net force on these items is zero, allowing for easier calculation of tension.
*   **External vs. Internal Forces:** Newton's Second Law only considers *external* forces. Internal forces (forces between objects within your chosen system) cancel out due to [[Newtons Third Law]].
*   **Non-Constant Forces:** If the force is not constant, you must use calculus to integrate the acceleration over time or position, linking back to [[Work]] and energy principles.