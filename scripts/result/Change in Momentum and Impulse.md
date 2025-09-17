# [[AP Physics Home]]
# AP Physics 1: Topic 4.2 - Change in Momentum and Impulse

## Introduction to Momentum

Momentum is a fundamental concept in physics, representing an object's "quantity of motion." It is a vector quantity, possessing both magnitude and direction. For a more detailed understanding, refer to [[Linear Momentum]].

## Change in Momentum ($\Delta p$)

The change in momentum ($\Delta p$) of an object is defined as the difference between its final momentum ($p_f$) and its initial momentum ($p_i$). Since momentum is a vector, the change in momentum is also a vector, and its direction is crucial.

Mathematically, the change in momentum is given by:

$
\Delta p = p_f - p_i
$

Where:
*   $p_f = mv_f$ (final momentum)
*   $p_i = mv_i$ (initial momentum)

Thus, the change in momentum can also be expressed as:

$
\Delta p = m(v_f - v_i) = m \Delta v
$

*   $m$ is the mass of the object (scalar, kg)
*   $v_f$ is the final velocity of the object (vector, m/s)
*   $v_i$ is the initial velocity of the object (vector, m/s)
*   $\Delta p$ is the change in momentum (vector, kg·m/s)

**Key Point:** A change in momentum occurs whenever an object's mass changes (rarely in AP Physics 1) or, more commonly, when its velocity changes (either in magnitude, direction, or both).

## Impulse ($J$)

Impulse ($J$) is a measure of the effect of a force acting over a period of time. It quantifies how much a force changes an object's momentum. Impulse is also a vector quantity, and its direction is the same as the net force causing it.

The impulse exerted on an object by a constant net force is defined as the product of the net force and the time interval over which it acts:

$
J = F_{net} \Delta t
$

Where:
*   $F_{net}$ is the net average force applied (vector, N)
*   $\Delta t$ is the time interval over which the force acts (scalar, s)
*   $J$ is the impulse (vector, N·s)

**Note:** If the force is not constant, impulse is calculated as the area under the force-time graph. For AP Physics 1, problems often involve constant forces or average forces.

### Units of Impulse

The units of impulse can be expressed as Newton-seconds (N·s). From Newton's Second Law ($F = ma$), we know that $1 N = 1 kg \cdot m/s^2$. Therefore, the units of impulse are equivalent to:

$
1 \text{ N} \cdot \text{s} = (1 \text{ kg} \cdot \text{m/s}^2) \cdot \text{s} = 1 \text{ kg} \cdot \text{m/s}
$

This equivalence highlights the direct relationship between impulse and momentum, as the units of momentum are also kg·m/s.

## The Impulse-Momentum Theorem

The Impulse-Momentum Theorem is a direct consequence of Newton's Second Law. It states that the impulse applied to an object is equal to the change in its momentum. This theorem is a powerful tool for analyzing situations where forces act over time to change an object's motion.

Starting from Newton's Second Law ([[Newton’s Second Law]]):
$
F_{net} = ma
$
Since $a = \frac{\Delta v}{\Delta t}$:
$
F_{net} = m \frac{\Delta v}{\Delta t}
$
Rearranging the terms:
$
F_{net} \Delta t = m \Delta v
$
Substituting the definitions of impulse and change in momentum:
$
J = \Delta p
$

This fundamental theorem connects force, time, mass, and velocity.

| Quantity                 | Symbol       | Type     | SI Unit   |
| :----------------------- | :----------- | :------- | :-------- |
| Change in Momentum       | $\Delta p$   | Vector   | kg·m/s    |
| Impulse                  | $J$          | Vector   | N·s       |
| Net Average Force        | $F_{net}$    | Vector   | N         |
| Time Interval            | $\Delta t$   | Scalar   | s         |
| Mass                     | $m$          | Scalar   | kg        |
| Change in Velocity       | $\Delta v$   | Vector   | m/s       |

## Applications of Impulse and Change in Momentum

The Impulse-Momentum Theorem helps explain various real-world phenomena and engineering designs:

*   **Impact Protection**: Objects designed to absorb impact (e.g., airbags, crumple zones in cars, padding in sports equipment) work by increasing the time interval ($\Delta t$) over which the force acts. By extending $\Delta t$ for a given change in momentum ($\Delta p$), the average force ($F_{net} = \Delta p / \Delta t$) experienced by an object is reduced, minimizing injury or damage.
*   **Follow-Through in Sports**: Athletes (e.g., in golf, tennis, baseball) are taught to "follow through" with their swings. This increases the contact time ($\Delta t$) between the implement (club, racket, bat) and the ball, thus increasing the impulse ($J = F_{net} \Delta t$) imparted to the ball, leading to a greater change in momentum ($\Delta p$) and higher final velocity.
*   **Rocket Propulsion**: Rockets expel exhaust gases at high velocity. The force exerted by the engine on the gases (action) results in an equal and opposite force on the rocket (reaction), according to [[Newton’s Third Law]]. This sustained force over time provides an impulse, changing the rocket's momentum.

Understanding these concepts is crucial for analyzing collisions and interactions between objects, which are further explored in [[Conservation of Linear Momentum]] and [[Elastic and Inelastic Collisions]].