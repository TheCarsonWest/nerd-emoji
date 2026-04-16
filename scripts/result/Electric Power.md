
# [[AP Physics C Home]]
# Electric Power

In the context of electric circuits, **Electric Power** ($P$) represents the rate at which electrical energy is transferred or converted into other forms of energy (such as heat, light, or mechanical motion) by an electric circuit component. Understanding power is crucial for designing safe and efficient electrical systems.

## Defining Electric Power

When charge moves through a potential difference, the potential energy changes. Power is defined as the rate of change of this energy with respect to time ($t$). Since $P = \frac{dU}{dt}$ and $U = qV$, we arrive at the fundamental definition:

$$P = IV$$

Where:
*   $P$ is power measured in Watts ($W$ or $J/s$).
*   $I$ is the current through the component measured in Amperes ($A$).
*   $V$ is the potential difference (voltage) across the component measured in Volts ($V$).

## Power Dissipation in Resistors

For components that obey [[Resistance, Resistivity, and Ohm's Law]], we can substitute Ohm's Law ($V = IR$) into the power equation to derive alternative forms. These are particularly useful when you only know two of the three variables ($I, V, R$).

### Power Equations Table

| Equation | Best Used When... |
| :--- | :--- |
| $$P = IV$$ | Both current and voltage are known. |
| $$P = I^2R$$ | Current and resistance are known (e.g., series circuits). |
| $$P = \frac{V^2}{R}$$ | Voltage and resistance are known (e.g., parallel circuits). |

### Joule Heating
When current flows through a resistor, the collisions between moving electrons and the atoms of the resistor material transfer energy to the atoms, increasing their kinetic energy. This manifests as thermal energy, commonly known as **Joule heating**. This process is irreversible in standard resistors and represents energy "lost" from the circuit as heat.

## Power Ratings and Efficiency

Electrical appliances are often labeled with a "power rating." This rating indicates the power the device consumes when connected to a specific operating voltage. 

*   **Warning:** Operating a device at a voltage higher than its rating can cause excessive power dissipation ($P = \frac{V^2}{R}$), leading to overheating or component failure.
*   **Energy Consumption:** Power is the *rate* of consumption. Total energy ($E$) used over a time interval $\Delta t$ is calculated by:

$$E = P \cdot \Delta t$$

While the SI unit for energy is the Joule ($J$), utility companies often measure energy in **kilowatt-hours** ($kWh$), where $1 \text{ kWh} = 3.6 \times 10^6 \text{ J}$.

## Relation to Circuit Laws

Power is fundamentally linked to the energy conservation principles found in [[Kirchhoff’s Loop Rule]]. In any closed loop, the total power supplied by the battery (or EMF source) must equal the total power dissipated by all components (resistors, etc.) in that circuit:

$$\sum P_{supplied} = \sum P_{dissipated}$$

This conservation ensures that energy is neither created nor destroyed within the electrical system, merely transformed.