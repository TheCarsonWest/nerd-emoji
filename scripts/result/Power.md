
# [[AP Physics C Home]]
# Topic 3.5: Power

## Definition of Power
In physics, **Power** is defined as the rate at which work is done or the rate at which energy is transferred or transformed. Since work is related to energy change, power essentially measures how quickly a force can change the energy of a system.

Because power is a rate, it is a scalar quantity, not a vector. Its SI unit is the **Watt (W)**, which is defined as one Joule per second ($1 \text{ W} = 1 \text{ J/s}$).

## Mathematical Definitions
There are several ways to express power mathematically depending on the variables provided.

### 1. Instantaneous Power
Instantaneous power represents the rate of doing work at a specific moment in time. It is defined as the derivative of work with respect to time:
$$P = \frac{dW}{dt}$$

Since work is defined as $dW = \vec{F} \cdot d\vec{r}$, we can substitute this to derive a relationship involving velocity:
$$P = \vec{F} \cdot \frac{d\vec{r}}{dt} = \vec{F} \cdot \vec{v}$$

Thus, if a force is applied to an object moving with velocity $\vec{v}$, the power delivered by that force is:
$$P = Fv \cos(\theta)$$
where $\theta$ is the angle between the force vector and the velocity vector.

### 2. Average Power
Average power is the total work done over a specific time interval $\Delta t$:
$$P_{avg} = \frac{W}{\Delta t} = \frac{\Delta E}{\Delta t}$$

## Power Relationships Summary

| Scenario | Equation | Variable Definitions |
| :--- | :--- | :--- |
| General (Work) | $P = \frac{W}{t}$ | $W$ = Work, $t$ = time |
| Constant Force & Velocity | $P = \vec{F} \cdot \vec{v}$ | $\vec{F}$ = Force, $\vec{v}$ = velocity |
| Energy Rate | $P = \frac{\Delta E}{t}$ | $\Delta E$ = Energy change |

## Key Concepts
*   **Sign of Power:** Because power involves a dot product ($\vec{F} \cdot \vec{v}$), the result can be positive, negative, or zero.
    *   **Positive Power:** The force is adding energy to the system (doing work on the object).
    *   **Negative Power:** The force is removing energy from the system (often a dissipative force like friction).
    *   **Zero Power:** The force is perpendicular to the motion (doing no work).

*   **Relationship to Calculus:** When you are given a graph of Work versus time, the slope of the line at any point represents the instantaneous power. Conversely, if you are given a graph of Power versus time, the area under the curve represents the total work done:
$$W = \int P \, dt$$

## Connecting Concepts
Understanding power is essential for analyzing systems involving [[Work]] and [[Conservation of Energy]]. In advanced mechanics problems, calculating power is often the bridge required to move between force-based dynamics and energy-based conservation principles. For instance, determining the "horsepower" of a motor requires understanding the [[Torque]] and rotational speed, which relates to rotational power:
$$P = \tau \omega$$
where $\tau$ is torque and $\omega$ is angular velocity.