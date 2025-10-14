# [[AP Physics Home]]
# AP Physics Note Page: Rotational Equilibrium and Newton’s First Law in Rotational Form

## 5.5 Rotational Equilibrium and Newton’s First Law in Rotational Form

This topic explores the conditions under which an object remains in a state of constant rotational motion (or no rotational motion at all). It's the rotational analog to [[Newton’s First Law]] for translational motion.

### I. Rotational Equilibrium Defined

An object is said to be in **rotational equilibrium** if its angular acceleration ($\alpha$) is zero. This means the object is either:
1.  At rest (not rotating), i.e., its angular velocity ($\omega$) is zero and remains zero.
2.  Rotating at a constant angular velocity ($\omega \neq 0$ but constant).

This concept is crucial for analyzing static structures like bridges, cranes, and even simple seesaws, where no angular motion is desired.

### II. Condition for Rotational Equilibrium

Just as a net force causes translational acceleration (Newton's Second Law: $\Sigma F = ma$), a net torque causes angular acceleration ([[Newton’s Second Law in Rotational Form]]: $\Sigma \tau = I \alpha$).

Therefore, for an object to be in rotational equilibrium ($\alpha = 0$), the net torque acting on it must be zero.

$ \Sigma \tau = 0 $

Where $\Sigma \tau$ is the sum of all torques acting on the object. This sum must be taken with respect to a chosen pivot point. The choice of pivot point is arbitrary for an object in equilibrium, as long as it's consistent.

### III. Torques and Lever Arms

[[Torque]] ($\tau$) is the rotational equivalent of force. It measures the effectiveness of a force in causing an object to rotate about a pivot point.

The magnitude of torque is given by:
$ \tau = r F \sin(\theta) $
Where:
*   $r$ is the distance from the pivot point to the point where the force is applied (the lever arm).
*   $F$ is the magnitude of the force.
*   $\theta$ is the angle between the position vector $r$ and the force vector $F$.
*   Often, we use the perpendicular component of the force ($F_\perp = F \sin(\theta)$) or the perpendicular lever arm ($r_\perp = r \sin(\theta)$), so $\tau = r F_\perp$ or $\tau = r_\perp F$.

Torque also has a direction:
*   **Positive torque** (counter-clockwise rotation)
*   **Negative torque** (clockwise rotation)

### IV. Rotational Equilibrium and Newton’s First Law

Newton's First Law states that an object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.

In rotational form:
*   An object that is not rotating (at rest rotationally) will remain not rotating unless acted upon by a net torque.
*   An object that is rotating at a constant angular velocity will continue to rotate at that constant angular velocity unless acted upon by a net torque.

This implies that if $\Sigma \tau = 0$, then $\alpha = 0$.

### V. Static Equilibrium

When an object is completely at rest and remains at rest, it is said to be in **static equilibrium**. For static equilibrium, two conditions must be met:

1.  **Translational Equilibrium:** The net force acting on the object must be zero.
    $ \Sigma F_x = 0 $
    $ \Sigma F_y = 0 $
    This ensures no linear acceleration.
2.  **Rotational Equilibrium:** The net torque acting on the object must be zero.
    $ \Sigma \tau = 0 $
    This ensures no angular acceleration.

Both conditions are essential for an object to remain perfectly still. For example, a ladder leaning against a wall must satisfy both to stay put.

### VI. Problem-Solving Strategy for Rotational Equilibrium

1.  **Draw a Free-Body Diagram (FBD):** Identify all forces acting on the object.
2.  **Choose a Pivot Point:** Select a convenient pivot point. Often, choosing the pivot at a point where an unknown force acts can simplify calculations by making that force's torque zero.
3.  **Identify Lever Arms:** Determine the distance from the pivot to the line of action of each force.
4.  **Calculate Torques:** For each force, calculate its torque magnitude and assign its direction (positive for counter-clockwise, negative for clockwise).
5.  **Apply Equilibrium Conditions:**
    *   $\Sigma \tau = 0$ (for rotational equilibrium)
    *   $\Sigma F_x = 0$
    *   $\Sigma F_y = 0$ (for static equilibrium)
6.  **Solve the System of Equations:** Use the equations to find unknown forces or distances.

| Concept             | Translational Equivalent | Rotational Equivalent |
| :------------------ | :----------------------- | :-------------------- |
| State of motion     | Constant velocity / Rest | Constant angular velocity / Rest |
| Condition           | $\Sigma \vec{F} = 0$     | $\Sigma \vec{\tau} = 0$ |
| Result              | No linear acceleration   | No angular acceleration |