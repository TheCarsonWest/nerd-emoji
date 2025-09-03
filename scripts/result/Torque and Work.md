# [[AP Physics Home]]
# AP Physics Note Page: Topic 6.2 - Torque and Work

This page explores the concepts of torque and work in rotational motion, building upon their linear counterparts. Just as force causes linear acceleration, torque causes angular acceleration. Similarly, work done by a force can be extended to work done by a torque in rotational systems.

## 1. Defining Torque ($\tau$)

Torque is the rotational equivalent of force. It measures the effectiveness of a force in causing an object to rotate about an axis. Torque is a vector quantity, but for AP Physics 1, we often consider its magnitude and direction (clockwise/counter-clockwise or into/out of the page).

### 1.1. Calculation of Torque

Torque is calculated as the product of the force applied and the perpendicular distance from the axis of rotation to the line of action of the force. This perpendicular distance is known as the **lever arm** ($r_{\perp}$).

$
\tau = r F \sin \theta
$
Where:
- $\tau$ is the torque (N·m)
- $r$ is the distance from the axis of rotation to the point where the force is applied (m)
- $F$ is the magnitude of the force applied (N)
- $\theta$ is the angle between the position vector $\vec{r}$ and the force vector $\vec{F}$

Alternatively, if $r_{\perp}$ is the lever arm, then:
$
\tau = F r_{\perp}
$

**Direction of Torque:**
- Counter-clockwise rotation is conventionally positive ($+$).
- Clockwise rotation is conventionally negative ($-$).

## 2. Work Done by a Torque

Just as [[Work]] is done by a force when an object undergoes displacement, work is done by a torque when an object undergoes angular displacement.

### 2.1. Rotational Work Formula

The work ($W$) done by a constant torque ($\tau$) acting through an angular displacement ($\Delta\theta$) is given by:

$
W = \tau \Delta\theta
$

Where:
- $W$ is the work done (Joules, J)
- $\tau$ is the constant net torque (N·m)
- $\Delta\theta$ is the angular displacement (radians, rad)

**Important Notes:**
- Angular displacement $\Delta\theta$ **must** be in radians for this formula to yield units of Joules.
- If the torque is not constant, calculus is required to integrate $\tau$ with respect to $\theta$.

### 2.2. Work-Energy Theorem for Rotational Motion

The work-energy theorem states that the net work done on an object equals the change in its kinetic energy. For rotational motion, this extends to:

$
W_{net} = \Delta K_{rot} = \frac{1}{2} I \omega_f^2 - \frac{1}{2} I \omega_i^2
$

Where:
- $W_{net}$ is the net work done by all torques (J)
- $\Delta K_{rot}$ is the change in [[Rotatinal Kinetic Energy]] (J)
- $I$ is the moment of inertia (kg·m$^2$)
- $\omega_f$ is the final angular speed (rad/s)
- $\omega_i$ is the initial angular speed (rad/s)

This theorem is fundamental for relating the work done by torques to changes in an object's rotational motion.

## 3. Power in Rotational Motion

[[Power]] is the rate at which work is done. For rotational motion, power ($P$) can be expressed as:

$
P = \frac{dW}{dt} = \tau \frac{d\theta}{dt} = \tau \omega
$

Where:
- $P$ is the power (Watts, W)
- $\tau$ is the torque (N·m)
- $\omega$ is the angular speed (rad/s)

This is analogous to the linear power formula $P = Fv$.

## 4. Relationship between Linear and Rotational Work

The concepts of linear and rotational work are inherently linked. As discussed in [[Conneting Linear and Rotational Motion]], linear quantities can be related to their rotational counterparts.

For a tangential force $F_t$ acting at a distance $r$ from the axis of rotation, undergoing a linear displacement $s = r\Delta\theta$:

$
W_{linear} = F_t s = F_t (r\Delta\theta) = (F_t r) \Delta\theta = \tau \Delta\theta = W_{rotational}
$

This demonstrates that the work done by a tangential force causing rotation is equivalent to the work done by the torque produced by that force over the angular displacement.

## 5. Applications and Problem-Solving

Understanding torque and work is crucial for analyzing systems involving rotation, such as:
- Gears and pulleys
- Spinning tops and flywheels
- Doors opening and closing
- Any object rotating about an axis where forces are applied

**Key considerations:**
- Identify the axis of rotation.
- Draw a free-body diagram to identify all forces and their points of application.
- Determine the lever arm for each force to calculate individual torques.
- Calculate net torque to determine angular acceleration or net work to determine change in rotational kinetic energy.