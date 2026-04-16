
# [[AP Physics C Home]]
# Kirchhoff’s Loop Rule

Kirchhoff’s Loop Rule, often referred to as Kirchhoff's Voltage Law (KVL), is a fundamental principle in circuit analysis derived from the [[Law of Conservation of Energy]]. It is essential for solving complex [[Compound DC Circuits]].

## Definition
The loop rule states that the algebraic sum of all potential differences (voltage changes) around any closed loop in a circuit must equal zero. In simpler terms, if you start at any point in a circuit and trace a complete path back to the starting point, the total energy gained from sources (like batteries) must equal the total energy dissipated by components (like resistors).

Mathematically, this is expressed as:
$$\sum_{i=1}^{n} \Delta V_i = 0$$

## Sign Conventions for Loop Analysis
When applying the loop rule, it is critical to maintain consistent signs. We define a direction for the loop (either clockwise or counter-clockwise). As you traverse each component, follow these rules:

| Component | Direction of Traverse | Change in Potential ($\Delta V$) |
| :--- | :--- | :--- |
| **Resistor** | With current direction | $-IR$ |
| **Resistor** | Against current direction | $+IR$ |
| **Battery** | From negative to positive terminal | $+\mathcal{E}$ |
| **Battery** | From positive to negative terminal | $-\mathcal{E}$ |

## The Physics Behind the Rule
The loop rule is a direct consequence of the conservative nature of the electrostatic field. Since the electrostatic force is conservative, the work done in moving a charge around a closed path is zero. Because electric potential is defined as potential energy per unit charge, moving a charge around a closed loop results in a net change in potential of zero. If the sum were not zero, the circuit would violate the [[The First Law of Thermodynamics]], implying that energy could be created or destroyed within a closed system.

## Application Strategy
To solve problems involving the loop rule, follow this systematic approach:

1.  **Identify Loops:** Clearly identify all independent closed loops in the circuit.
2.  **Assign Currents:** Label the magnitude and direction of the current in each branch of the circuit. If you guess the wrong direction, the mathematical solution will simply yield a negative value for the current.
3.  **Traverse Loops:** Choose a direction (e.g., clockwise) to traverse each loop.
4.  **Write Equations:** Apply the sum of potential differences equal to zero for each loop. Use the sign conventions listed above.
5.  **Solve System of Equations:** Combine these equations with those derived from [[Kirchhoff’s Junction Rule]] to solve for unknown currents or resistances.

For circuits involving capacitors, remember that you may also need to reference [[Capacitors]] to determine the voltage across those specific components. When circuits are analyzed over time, you may transition into [[Resistor-Capacitor (RC) Circuits]], where the loop rule remains valid but involves time-dependent differential equations.