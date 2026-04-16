
# [[AP Physics C Home]]
# Topic 11.8: Resistor-Capacitor (RC) Circuits

An RC circuit is a circuit containing a resistor ($R$) and a capacitor ($C$) connected in series or parallel. These circuits are dynamic, meaning current and voltage change over time as the capacitor charges or discharges.

## Charging an RC Circuit
When a capacitor is connected in series with a resistor and a DC voltage source ($\mathcal{E}$), the capacitor does not charge instantly. Instead, it charges exponentially.

Initially (at $t=0$), the capacitor acts as a wire (short circuit) because it is uncharged. As charge accumulates on the plates, the capacitor creates a back-EMF that opposes the flow of current. The charge $q(t)$ on the capacitor at any time $t$ is given by:

$$q(t) = C\mathcal{E}(1 - e^{-t/RC})$$

The current $I(t)$ in the circuit decreases over time:

$$I(t) = \frac{\mathcal{E}}{R}e^{-t/RC}$$

## Discharging an RC Circuit
When a charged capacitor is removed from the voltage source and connected across a resistor, it discharges. The potential energy stored in the capacitor dissipates as heat through the resistor. The equations for charge and current during discharge are:

$$q(t) = Q_0e^{-t/RC}$$
$$I(t) = -\frac{Q_0}{RC}e^{-t/RC}$$

*(Note: The negative sign in current indicates the direction of flow is opposite to the charging current.)*

## The Time Constant ($\tau$)
The behavior of an RC circuit is determined by the time constant, denoted by $\tau$. It represents the time required for the capacitor to charge to approximately 63.2% of its maximum value or discharge to approximately 36.8% of its initial value.

$$\tau = RC$$

| Time ($t$) | Charging ($q$) | Discharging ($q$) |
| :--- | :--- | :--- |
| $t = 0$ | $0$ | $Q_0$ |
| $t = \tau$ | $0.632Q_{max}$ | $0.368Q_0$ |
| $t = 5\tau$ | $\approx 1.00Q_{max}$ | $\approx 0.00Q_0$ |

## Important Considerations
*   **Steady State:** After a "long time" (typically considered $t > 5\tau$), the capacitor is fully charged. In a DC circuit, a fully charged capacitor acts as an open switch; the current in that branch becomes zero.
*   **Energy:** The energy stored in a capacitor can be reviewed in [[Capacitors]].
*   **Kirchhoff's Rules:** Analyzing these circuits requires applying [[Kirchhoffs Loop Rule]]. Because current is time-dependent, the loop rule results in a first-order differential equation. Solving these equations often involves techniques discussed in [[Simple Circuits]].

Understanding RC circuits is fundamental to advanced electrical engineering, including signal filtering and timing circuits. For circuits involving other components, consider reviewing [[Circuits with Resistors and Inductors (LR Circuits)]] or [[Circuits with Capacitors and Inductors (LC Circuits)]].