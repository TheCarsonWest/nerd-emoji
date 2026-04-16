
# [[AP Physics C Home]]
# 6.4: Conservation of Angular Momentum

The principle of conservation of angular momentum is a fundamental concept in rotational mechanics, serving as the rotational analog to the [[Conservation of Linear Momentum]]. It allows us to analyze complex systems—ranging from spinning figure skaters to planetary orbits—without needing to know the specific forces applied at every instant.

## The Conservation Law

Angular momentum ($L$) is conserved for a system if the net external torque acting on that system is zero. Mathematically, this is expressed as:

$$ \sum \vec{\tau}_{ext} = \frac{d\vec{L}}{dt} $$

If the net external torque is zero ($\sum \vec{\tau}_{ext} = 0$), then the rate of change of angular momentum is zero, meaning:

$$ \vec{L}_{initial} = \vec{L}_{final} $$

Or, in terms of rotational inertia ($I$) and angular velocity ($\omega$):

$$ I_i \omega_i = I_f \omega_f $$

### Conditions for Conservation

It is vital to distinguish between internal and external torques. Internal torques (torques exerted by parts of the system on each other) do not change the total angular momentum of the system. Only external torques can alter the system's angular momentum.

| Scenario | Net External Torque | Angular Momentum Conserved? |
| :--- | :--- | :--- |
| A figure skater pulls in arms | Zero | Yes |
| A planet orbiting the sun | Zero (Radial force) | Yes |
| A door being pushed open | Non-zero | No |
| A falling cat twisting in air | Zero (Internal forces only) | Yes |

## [[Rotational Collisions and Angular Momentum]]

When two objects collide or interact rotationally, we treat the interaction as a closed system. Because the collision forces are internal (acting within the system), the total angular momentum remains constant throughout the process. This is particularly useful for problems involving "sticky" collisions where objects become attached or change their distribution of mass.

### Important Considerations
1. **Axis of Rotation:** Conservation of angular momentum must be calculated about the same fixed point or axis for both the initial and final states.
2. **Vector Nature:** Angular momentum is a vector. If a system has multiple rotating components, you must account for the direction of their rotation (e.g., using the right-hand rule) and sum them as vectors.
3. **Change in Rotational Inertia:** Frequently, these problems involve a change in $I$. For example, when a mass moves closer to the axis of rotation, $I$ decreases, which—by conservation—forces $\omega$ to increase to keep $L$ constant.

## Applications
This principle explains why ice skaters spin faster when they pull their arms in. By pulling their mass closer to the axis of rotation, they decrease their moment of inertia ($I$). To conserve angular momentum ($L = I\omega$), their angular velocity ($\omega$) must increase.

Another classic application is the [[Motion of Orbiting Satellites]]. As a planet moves in an elliptical orbit, its distance from the sun changes. As the distance (radius) changes, the planet's speed must change to ensure that angular momentum is conserved at every point in the orbit. This is effectively Kepler's Second Law.