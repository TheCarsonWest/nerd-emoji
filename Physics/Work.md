# [[AP Physics Home]]
# Topic 3.2: Work

Work is a fundamental concept in physics, representing the transfer of energy to or from an object by means of a force acting on that object. It's crucial for understanding how forces change the motion or configuration of systems.

## Definition of Work

In physics, **work** is done when a force causes a displacement of an object. For work to be done, two conditions must be met:
1.  A force must be applied to the object.
2.  The object must undergo a displacement in the direction of the force, or at least have a component of its displacement along the direction of the force.

If either the force or the displacement is zero, no work is done. Also, if the force is perpendicular to the displacement, no work is done.

## Mathematical Formulation

The work ($W$) done by a constant force ($F$) on an object that undergoes a displacement ($d$) is given by the dot product of the force and displacement vectors. If the force and displacement are in the same direction, the formula simplifies. In general, it includes the angle between them:

$W = F d \cos\theta$

Where:
*   $W$ is the work done (a [[Scalars and Vectors in One Dimension|scalar quantity]]).
*   $F$ is the magnitude of the constant force.
*   $d$ is the magnitude of the displacement.
*   $\theta$ is the angle between the force vector and the displacement vector.

### Units of Work

The SI unit for work is the **Joule (J)**. One Joule is defined as the work done by a force of one Newton causing a displacement of one meter in the direction of the force.
$1 \text{ J} = 1 \text{ N} \cdot 1 \text{ m}$

## Positive, Negative, and Zero Work

The sign of work depends on the angle $\theta$ between the force and displacement vectors:

| Angle ($\theta$) | $\cos\theta$ | Type of Work | Description                                                                        |
| :--------------- | :----------- | :----------- | :--------------------------------------------------------------------------------- |
| $0^\circ \le \theta < 90^\circ$ | Positive       | Positive Work  | Force has a component in the direction of motion, increasing the object's speed/energy. |
| $\theta = 90^\circ$   | Zero         | Zero Work    | Force is perpendicular to the displacement (e.g., centripetal force in [[Circular Motion]]). |
| $90^\circ < \theta \le 180^\circ$ | Negative       | Negative Work  | Force has a component opposite to the direction of motion, decreasing the object's speed/energy. |

**Examples:**
*   **Positive Work:** Pushing a box across the floor in the direction of motion.
*   **Negative Work:** Friction acting on a sliding box, bringing it to a stop; lifting a weight slowly (gravity does negative work).
*   **Zero Work:** Carrying a bag horizontally at a constant velocity (force is vertical, displacement is horizontal); the normal force on a block sliding on a horizontal surface.

## Work Done by Multiple Forces

If multiple forces act on an object, the total (or net) work done is the sum of the work done by each individual force. Alternatively, you can find the net force first and then calculate the work done by the net force:

$W_{net} = \sum W_i = W_1 + W_2 + W_3 + \dots$
Or
$W_{net} = F_{net} d \cos\theta_{net}$

## Work-Energy Theorem

One of the most important applications of work is the [[Work-Energy Theorem]]. This theorem states that the net work done on an object is equal to the change in its [[Translational Kinetic Energy]]:

$W_{net} = \Delta K = K_f - K_i = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$

Where:
*   $W_{net}$ is the net work done on the object.
*   $\Delta K$ is the change in the object's [[Translational Kinetic Energy]].
*   $m$ is the mass of the object.
*   $v_f$ is the final speed of the object.
*   $v_i$ is the initial speed of the object.

This theorem provides a powerful link between forces and changes in motion.

## Work and Energy

Work is directly related to energy transfer. When positive work is done on an object, its energy increases. When negative work is done, its energy decreases. Work is also closely related to [[Potential Energy]] concepts and is a key component in the principle of [[Conservation of Energy]]. The rate at which work is done is known as [[Power]].

## Work Done by a Variable Force

For situations where the applied force is not constant, the work done must be calculated using calculus. If the force varies with position ($F(x)$), the work done is the area under the force-displacement graph:

$W = \int_{x_i}^{x_f} F(x) \, dx$
This is particularly useful for forces like [[Spring Forces]] where $F = -kx$.