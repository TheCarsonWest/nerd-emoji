
# [[AP Physics C Home]]
# 5.5: Rotational Equilibrium and Newton's First Law in Rotational Form

## Introduction
In classical mechanics, equilibrium occurs when an object is not accelerating. While we have previously discussed translational equilibrium ($ \sum \vec{F} = 0 $), rotational equilibrium is a separate condition that must be met for an object to be truly in static or dynamic equilibrium. This topic acts as the rotational analog to Newton’s First Law.

## Newton’s First Law (Rotational Form)
Newton's First Law states that an object at rest remains at rest, and an object in motion continues in motion with a constant velocity unless acted upon by a net external force. In rotational terms, this means that a rigid body will maintain a constant angular velocity ($\omega$) unless acted upon by a net external torque.

For an object to be in rotational equilibrium, the sum of all torques acting on it must be zero:

$$\sum \tau = 0$$

If this condition is met, the angular acceleration ($\alpha$) of the object is zero, as dictated by the rotational version of Newton's Second Law, [[Newtons Second Law in Rotational Form]].

## Conditions for Static Equilibrium
For a rigid body to be in total static equilibrium (meaning it is neither accelerating linearly nor rotating), two primary conditions must be satisfied simultaneously:

| Condition | Mathematical Expression | Physical Meaning |
| :--- | :--- | :--- |
| **Translational Equilibrium** | $$ \sum \vec{F} = 0 $$ | The center of mass is not accelerating. |
| **Rotational Equilibrium** | $$ \sum \vec{\tau} = 0 $$ | The object is not changing its angular velocity. |

### The Importance of the Pivot Point
When analyzing problems involving rotational equilibrium, you can calculate the net torque about *any* pivot point. However, to simplify calculations, it is standard practice to choose a pivot point where an unknown force is applied. Because the torque is calculated as $\vec{\tau} = \vec{r} \times \vec{F}$, if the pivot point lies exactly on the line of action of an unknown force, the lever arm ($r$) is zero, effectively eliminating that unknown from your equation.

## Analyzing Equilibrium Problems
When solving problems such as ladders leaning against walls or beams supported by cables, follow these steps:

1.  **Free Body Diagram:** Identify all forces and their specific points of application.
2.  **Coordinate System:** Choose a standard $x-y$ coordinate system for forces.
3.  **Sum of Forces:** Apply Newton's Second Law for translation:
    *   $$ \sum F_x = 0 $$
    *   $$ \sum F_y = 0 $$
4.  **Sum of Torques:** Choose a convenient pivot point and set the sum of torques to zero. Remember to assign a sign convention (typically counter-clockwise is positive, clockwise is negative).
    *   $$ \sum \tau = \sum (rF \sin\theta) = 0 $$

By combining these equations, you can solve for multiple unknowns, such as tension in cables or reaction forces at hinges. Understanding these concepts is fundamental to mastering statics and provides the groundwork for more complex rotational dynamics, such as [[Torque]] and [[Rotational Inertia]].