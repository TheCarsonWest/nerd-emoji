
# [[AP Physics C Home]]
# Newton's Second Law in Rotational Form

In translational mechanics, Newton's Second Law states that the net force acting on an object is proportional to its acceleration: $F_{net} = ma$. In rotational mechanics, this principle has a direct analog. Newton's Second Law for rotation relates the net torque acting on a rigid body to its angular acceleration.

## The Rotational Analog

Just as force causes linear acceleration, torque causes angular acceleration. While mass represents the resistance to linear acceleration (inertia), [[Rotational Inertia]] represents the resistance to angular acceleration.

The relationship is expressed as:

$$\tau_{net} = I\alpha$$

Where:
*   $\tau_{net}$ is the net [[Torque]] applied to the object (measured in $N \cdot m$).
*   $I$ is the [[Rotational Inertia]] of the object about the axis of rotation (measured in $kg \cdot m^2$).
*   $\alpha$ is the angular acceleration (measured in $rad/s^2$).

## Comparison Table: Linear vs. Rotational

It is helpful to visualize the direct mapping between linear and rotational concepts to better understand how this law functions.

| Concept | Linear Analog | Rotational Analog |
| :--- | :--- | :--- |
| **Cause of Change** | Force ($F$) | [[Torque]] ($\tau$) |
| **Resistance to Motion** | Mass ($m$) | [[Rotational Inertia]] ($I$) |
| **Motion** | Acceleration ($a$) | Angular Acceleration ($\alpha$) |
| **Newton's 2nd Law** | $F_{net} = ma$ | $\tau_{net} = I\alpha$ |

## Important Considerations

### 1. The Axis of Rotation
This equation is strictly valid when both $\tau$ and $I$ are calculated with respect to the same fixed axis of rotation. If an object is rotating about its center of mass, $I$ corresponds to the moment of inertia about that center. If the axis of rotation is at the edge of the object, you must use the [[Parallel Axis Theorem]] (if applicable) or define $I$ specifically for that axis.

### 2. Directionality
Since torque and angular acceleration are vector quantities, this equation holds true for the direction of rotation. By convention, counter-clockwise rotation is often treated as positive, while clockwise rotation is treated as negative. When solving problems, consistently applying a sign convention is crucial to ensuring that your net torque and angular acceleration have the correct signs.

### 3. Constraints in Systems
Often, this law is used in conjunction with [[Connecting Linear and Rotational Motion]]. For example, in a system where a hanging mass is attached to a string wrapped around a pulley:
*   For the mass: $\Sigma F = T - mg = ma$
*   For the pulley: $\Sigma \tau = TR = I\alpha$
*   Constraint: $a = \alpha R$

By substituting the constraint into the equations, you can solve for the unknown tension $T$ or the angular acceleration $\alpha$.

## Applications
This law is the fundamental tool for solving dynamic rotational problems, such as:
*   Atwood machines involving a massive pulley.
*   Calculating the acceleration of objects rolling down inclines (see [[Rolling]]).
*   Determining the forces required to stop or start a rotating flywheel or wheel.