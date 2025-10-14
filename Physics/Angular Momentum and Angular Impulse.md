# [[AP Physics Home]]
# AP Physics Notes: Topic 6.3 - Angular Momentum and Angular Impulse

## 1. Introduction to Angular Momentum

Just as [[Linear Momentum]] describes the "quantity of motion" for translational motion, **Angular Momentum** ($L$) describes the "quantity of rotational motion" for rotational motion. It is a crucial concept for understanding how rotating systems behave, especially when torques act upon them or when their mass distribution changes.

## 2. Angular Momentum ($L$)

Angular momentum is a vector quantity. Its direction is determined by the right-hand rule.

### 2.1 For a Point Particle

For a point particle of mass $m$ with position vector $\vec{r}$ relative to an origin and linear momentum $\vec{p} = m\vec{v}$, its angular momentum $\vec{L}$ about that origin is defined as the cross product:

$
\vec{L} = \vec{r} \times \vec{p} = \vec{r} \times (m\vec{v})
$

The magnitude of this angular momentum is:

$
L = r p \sin\theta = r (mv) \sin\theta
$

where $\theta$ is the angle between $\vec{r}$ and $\vec{p}$. If $\vec{r}$ and $\vec{p}$ are perpendicular, $L = r p = r m v$.

### 2.2 For a Rigid Body

For a rigid body rotating about a fixed axis with a moment of inertia $I$ and angular velocity $\vec{\omega}$, its angular momentum $\vec{L}$ is given by:

$
\vec{L} = I\vec{\omega}
$

In this case, the direction of $\vec{L}$ is along the axis of rotation, in the same direction as $\vec{\omega}$.

### 2.3 Units of Angular Momentum

The SI unit for angular momentum is Joule-second (J·s) or kilogram-meter squared per second (kg·m²/s).

## 3. Angular Impulse ($J_{\text{angular}}$)

Analogous to how [[Change in Momentum and Impulse]] relates linear impulse to a change in linear momentum, **Angular Impulse** relates to a change in angular momentum.

### 3.1 Definition

Angular impulse ($J_{\text{angular}}$) is the integral of the net external torque ($\vec{\tau}_{\text{net}}$) over a time interval $t$:

$
\vec{J}_{\text{angular}} = \int_{t_1}^{t_2} \vec{\tau}_{\text{net}} \, dt
$

If the net torque is constant, this simplifies to:

$
\vec{J}_{\text{angular}} = \vec{\tau}_{\text{net}} \Delta t
$

### 3.2 Angular Impulse-Momentum Theorem

The **Angular Impulse-Momentum Theorem** states that the angular impulse applied to an object is equal to the change in its angular momentum:

$
\vec{J}_{\text{angular}} = \Delta \vec{L} = \vec{L}_f - \vec{L}_i
$

Combining this with the definition of angular impulse:

$
\int_{t_1}^{t_2} \vec{\tau}_{\text{net}} \, dt = \Delta \vec{L}
$

This theorem is derived directly from [[Newton’s Second Law in Rotational Form]], $\vec{\tau}_{\text{net}} = \frac{d\vec{L}}{dt}$.

### 3.3 Units of Angular Impulse

The SI unit for angular impulse is Newton-meter-second (N·m·s), which is equivalent to kg·m²/s, the unit for angular momentum.

## 4. Key Relationships and Summary

| Concept         | Translational Analog | Rotational Analog     | Definition / Equation                                       |
| :-------------- | :------------------- | :-------------------- | :---------------------------------------------------------- |
| Momentum        | Linear Momentum ($p$) | Angular Momentum ($L$) | $L = I\omega$ (rigid body) or $L = r p \sin\theta$ (point) |
| Impulse         | Linear Impulse ($J$)   | Angular Impulse ($J_{\text{angular}}$) | $J_{\text{angular}} = \tau_{\text{net}} \Delta t$            |
| Impulse-Momentum Theorem | $\Delta p = J$       | $\Delta L = J_{\text{angular}}$ | $\Delta L = \tau_{\text{net}} \Delta t$                    |
| Cause of Change | Net Force ($\vec{F}_{\text{net}}$) | Net Torque ($\vec{\tau}_{\text{net}}$) | $\tau_{\text{net}} = \frac{dL}{dt}$                       |

## 5. [[Conservation of Angular Momentum]]

An extremely important consequence of the Angular Impulse-Momentum Theorem is the **Conservation of Angular Momentum**. If the net external torque acting on a system is zero ($\vec{\tau}_{\text{net}} = 0$), then the angular impulse is zero, and thus the total angular momentum of the system remains constant ($\Delta \vec{L} = 0$, so $\vec{L}_i = \vec{L}_f$). This principle is fundamental to understanding the behavior of isolated rotating systems, such as planets orbiting stars, figure skaters spinning, or collapsing stars forming pulsars.