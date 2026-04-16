
# [[AP Physics C Home]]
# Resistor-Capacitor (RC) Circuits

In DC circuits, we often assume currents are constant. However, when a capacitor is included in a circuit with resistors, the current and voltage become time-dependent. These are known as RC circuits.

## Charging a Capacitor
When a switch is closed to connect an uncharged capacitor ($C$) in series with a resistor ($R$) and an EMF source ($\mathcal{E}$), the capacitor begins to accumulate charge. By applying [[Kirchhoff’s Loop Rule]], the potential differences sum to zero:

$$\mathcal{E} - IR - \frac{q}{C} = 0$$

Using $I = \frac{dq}{dt}$, this becomes a first-order differential equation. Solving for charge $q(t)$ gives:

$$q(t) = C\mathcal{E}(1 - e^{-t/RC})$$

From this, we can derive the time-dependent current $I(t)$ by taking the derivative $\frac{dq}{dt}$:

$$I(t) = \frac{\mathcal{E}}{R}e^{-t/RC}$$

## Discharging a Capacitor
If a charged capacitor is disconnected from the battery and allowed to discharge through a resistor, the EMF source is removed ($\mathcal{E} = 0$). The loop rule becomes:

$$-IR - \frac{q}{C} = 0$$

The solutions for charge and current during discharge are:

$$q(t) = Q_0e^{-t/RC}$$
$$I(t) = -\frac{Q_0}{RC}e^{-t/RC}$$

Note that the current is negative during discharge because charge flows in the opposite direction compared to the charging phase.

## The Time Constant ($\tau$)
The behavior of RC circuits is governed by the product of resistance and capacitance, known as the **time constant** ($\tau$):

$$\tau = RC$$

The time constant dictates how quickly a capacitor charges or discharges. After one time constant ($t = \tau$), the capacitor is charged to approximately 63.2% of its maximum value.

| Process | Charge $q(t)$ | Current $I(t)$ |
| :--- | :--- | :--- |
| **Charging** | $Q_{max}(1 - e^{-t/\tau})$ | $I_0 e^{-t/\tau}$ |
| **Discharging** | $Q_0 e^{-t/\tau}$ | $-I_0 e^{-t/\tau}$ |

## Conceptual Summary
*   **At $t=0$ (Charging):** The capacitor acts like a **wire** (a short circuit). There is no charge on the plates, so the potential difference across the capacitor is 0V. The entire EMF drops across the resistor, and current is at its maximum ($I = \mathcal{E}/R$).
*   **At $t \rightarrow \infty$ (Steady State):** The capacitor acts like an **open circuit**. It is fully charged ($q = C\mathcal{E}$), so current ceases to flow through the branch containing the capacitor.

Understanding how to analyze these circuits involves applying [[Kirchhoff’s Junction Rule]] and [[Kirchhoff’s Loop Rule]] to determine initial and steady-state conditions before solving the differential equations for time-dependent behavior.