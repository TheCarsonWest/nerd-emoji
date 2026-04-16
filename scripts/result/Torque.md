
# [[AP Physics C Home]]
# AP Physics C: Torque

Torque is the rotational analogue of force. While force causes linear acceleration, torque causes rotational (angular) acceleration. Understanding torque is essential for analyzing systems in [[Rotational Equilibrium and Newtons First Law in Rotational Form]] and [[Newtons Second Law in Rotational Form]].

## Definition of Torque

Torque ($\tau$) measures the tendency of a force to rotate an object about an axis. It depends on three factors: the magnitude of the applied force, the distance from the pivot point (the lever arm), and the angle at which the force is applied.

The vector equation for torque is defined as the cross product of the position vector ($\vec{r}$) and the force vector ($\vec{F}$):

$$\vec{\tau} = \vec{r} \times \vec{F}$$

The magnitude of torque is given by:

$$\tau = rF\sin(\theta)$$

Where:
*   $r$ is the position vector from the pivot point to the point of application.
*   $F$ is the magnitude of the force applied.
*   $\theta$ is the angle between the position vector and the force vector.

## The Lever Arm Concept

It is often useful to think of torque as the product of the force and the "lever arm" (or moment arm). The lever arm ($r_{\perp}$) is the perpendicular distance from the axis of rotation to the line of action of the force.

$$\tau = F \cdot r_{\perp}$$

| Component | Description |
| :--- | :--- |
| $\vec{r}$ | Displacement vector from axis to force application point |
| $\vec{F}$ | The force vector applied to the object |
| $\theta$ | Angle between $\vec{r}$ and $\vec{F}$ |
| $r_{\perp}$ | The perpendicular component ($r\sin\theta$) |

## Important Considerations

### Direction and Sign Convention
Torque is a vector quantity. In two-dimensional problems, we assign a sign based on the rotation direction:
*   **Counter-clockwise (CCW):** Typically positive ($+$).
*   **Clockwise (CW):** Typically negative ($-$).

### Net Torque
If multiple forces act on an object, the total torque acting on the object is the vector sum of the individual torques:

$$\tau_{net} = \sum \tau_i = \tau_1 + \tau_2 + \dots$$

### The Cross Product
The cross product $\vec{r} \times \vec{F}$ implies that the resulting torque vector is perpendicular to both the position vector and the force vector. This is determined using the Right-Hand Rule. If you curl the fingers of your right hand from $\vec{r}$ toward $\vec{F}$, your thumb points in the direction of the torque vector $\vec{\tau}$.

## Relationship to Other Topics

Torque is not just a standalone concept; it is the fundamental "driver" of rotational motion. It acts as the cause for angular acceleration, much like force acts as the cause for linear acceleration in [[Newtons Second Law in Rotational Form]]. 

When a torque does work on an object, it results in a change in [[Rotational Kinetic Energy]], a concept explored further in [[Torque and Work]]. Additionally, analyzing torque is vital when calculating the angular momentum of a system, which can be reviewed in [[Angular Momentum and Angular Impulse]].