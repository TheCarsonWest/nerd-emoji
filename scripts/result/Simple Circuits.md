
# [[AP Physics C Home]]
# AP Physics C: Simple Circuits

Simple circuits form the backbone of electrical analysis. They typically consist of an electromotive force (EMF) source—like a battery—connected to components such as resistors, capacitors, and wires. Understanding these circuits requires applying fundamental conservation laws.

## Electromotive Force (EMF) and Terminal Voltage
While we often treat batteries as "ideal" sources of voltage, real batteries have internal resistance, denoted as $r$. The terminal voltage $V$ is the actual potential difference measured across the terminals of the source when current flows.

The relationship is governed by:
$$V = \mathcal{E} - Ir$$

Where:
*   $\mathcal{E}$ is the EMF (ideal voltage).
*   $I$ is the current.
*   $r$ is the internal resistance.

## Resistor Combinations
Resistors in a circuit can be combined to simplify calculations. The two primary configurations are series and parallel.

| Connection Type | Equivalent Resistance Equation | Current Properties | Voltage Properties |
| :--- | :--- | :--- | :--- |
| **Series** | $R_{eq} = R_1 + R_2 + R_3 + ...$ | Same current through all | Voltage divides across resistors |
| **Parallel** | $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ...$ | Current divides across branches | Same voltage across all |

## Analyzing Simple Circuits
To solve for unknown currents, voltages, or resistances in simple circuits, we utilize Ohm's Law in conjunction with [[Kirchhoff’s Loop Rule]] and [[Kirchhoff’s Junction Rule]]. 

1.  **Identify Loops:** Apply the Loop Rule (conservation of energy) to define equations for potential changes around a closed path. The sum of potential differences must equal zero: $\sum \Delta V = 0$.
2.  **Identify Junctions:** Apply the Junction Rule (conservation of charge) to state that the sum of currents entering a junction must equal the sum of currents leaving: $\sum I_{in} = \sum I_{out}$.

## Power in Simple Circuits
The rate at which energy is delivered to a circuit element or dissipated as heat is defined as power. Using [[Electric Power]] principles, we can calculate this for any resistor:

$$P = IV = I^2R = \frac{V^2}{R}$$

For the entire circuit, the power delivered by the battery is $P = I\mathcal{E}$.

## Measuring Tools
In laboratory settings, we use specific instruments to analyze these circuits:
*   **Ammeter:** Measures current. It is placed in **series** with the component being measured and ideally has zero resistance ($R \approx 0$) to avoid altering the circuit.
*   **Voltmeter:** Measures potential difference. It is placed in **parallel** across the component and ideally has infinite resistance ($R \to \infty$) to ensure no current flows through the meter itself.

For more complex systems where simple series/parallel combinations fail, refer to [[Compound DC Circuits]]. Additionally, when circuits involve time-dependent behavior with capacitors, refer to [[Resistor-Capacitor (RC) Circuits]].