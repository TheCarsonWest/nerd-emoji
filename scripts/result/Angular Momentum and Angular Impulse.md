
# [[AP Physics C Home]]
# Topic 6.3: Angular Momentum and Angular Impulse

Angular momentum is the rotational analogue of linear momentum. While linear momentum describes an object's tendency to continue moving in a straight line, angular momentum describes an object's tendency to continue rotating.

## Angular Momentum of a Point Particle

For a point particle moving with linear momentum $\vec{p}$ at a position $\vec{r}$ relative to a pivot point, angular momentum ($\vec{L}$) is defined as the cross product of the position vector and the momentum vector.

$$\vec{L} = \vec{r} \times \vec{p} = \vec{r} \times (m\vec{v})$$

The magnitude of angular momentum for a point particle can be calculated as:

$$L = r p \sin(\theta) = mvr \sin(\theta)$$

Where $\theta$ is the angle between the position vector $\vec{r}$ and the velocity vector $\vec{v}$. Alternatively, you can use the perpendicular distance (lever arm) $r_{\perp} = r \sin(\theta)$, leading to $L = m v r_{\perp}$.

## Angular Momentum of a Rigid Body

For a rigid body rotating about a fixed axis with angular velocity $\omega$, the angular momentum is determined by the object's [[Rotational Inertia]] and its rate of rotation:

$$L = I\omega$$

Where $I$ is the rotational inertia and $\omega$ is the angular velocity. This relationship is the rotational equivalent of $p = mv$.

## Angular Impulse

Similar to how a force applied over time changes linear momentum, a torque applied over time changes angular momentum. This is known as angular impulse.

| Concept | Linear Analogue | Rotational Analogue |
| :--- | :--- | :--- |
| **Momentum** | $p = mv$ | $L = I\omega$ |
| **Impulse** | $J = \int F dt = \Delta p$ | $\int \tau dt = \Delta L$ |
| **Equation of Motion** | $F = \frac{dp}{dt}$ | $\tau = \frac{dL}{dt}$ |

The angular impulse-momentum theorem states:

$$\Delta L = \int_{t_i}^{t_f} \tau \, dt$$

If the torque is constant, this simplifies to $\Delta L = \tau \Delta t$. This demonstrates that a net torque is required to change the angular momentum of a system. If the net external torque is zero, the angular momentum remains constant, leading to the [[Conservation of Angular Momentum]].

## Key Takeaways

*   **Direction:** The direction of $\vec{L}$ is determined by the right-hand rule. If you curl the fingers of your right hand in the direction of rotation, your thumb points in the direction of the angular momentum vector.
*   **Vector Nature:** Because angular momentum is a vector quantity, changes in direction (such as in uniform circular motion) imply a change in angular momentum, which requires a net torque.
*   **Relationship to Torque:** [[Newtons Second Law in Rotational Form]] can be expressed as $\tau_{net} = \frac{dL}{dt}$, which is the most fundamental definition of torque.