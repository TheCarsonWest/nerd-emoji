
# [[AP Physics C Home]]
# AP Physics C: Compound DC Circuits

Compound DC circuits are circuits that contain multiple resistors arranged in complex combinations of series and parallel networks, often powered by one or more voltage sources. Analyzing these circuits requires a systematic approach to simplify the network or apply conservation laws to determine currents, voltages, and equivalent resistance.

## Equivalent Resistance
To simplify a compound circuit, we often reduce the network to a single equivalent resistor, $R_{eq}$. This allows us to determine the total current flowing from the power source using Ohm's Law.

| Connection Type | Equivalent Resistance Formula |
| :--- | :--- |
| **Series** | $$R_{eq} = R_1 + R_2 + R_3 + \dots$$ |
| **Parallel** | $$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$ |

When simplifying, you must first identify the "innermost" parts of the circuit (sections that are purely series or purely parallel) and replace them with a single equivalent resistor, then repeat the process until the entire circuit is reduced to a single loop.

## Systematic Analysis Strategy
When a circuit is too complex for simple series/parallel reduction—such as when multiple batteries are present in different branches—you must apply formal circuit analysis techniques.

### 1. Identify Nodes and Branches
*   **Node:** A junction point where three or more wires meet.
*   **Branch:** A path connecting two nodes that contains components (resistors, batteries).

### 2. Apply Kirchhoff’s Laws
Kirchhoff's laws are the fundamental tools for solving any DC circuit, regardless of complexity.

*   **[[Kirchhoff’s Junction Rule]]:** Based on the conservation of charge, the sum of currents entering a junction must equal the sum of currents leaving it.
    $$\sum I_{in} = \sum I_{out}$$

*   **[[Kirchhoff’s Loop Rule]]:** Based on the conservation of energy, the algebraic sum of potential differences (voltage drops and gains) around any closed loop must be zero.
    $$\sum V = 0$$

## Steps for Solving Complex Circuits
If a circuit cannot be reduced, follow these steps to find the unknowns (typically currents):

1.  **Label currents:** Assign a direction (e.g., $I_1$, $I_2$, $I_3$) to each branch. If your guess is wrong, the result will simply be negative.
2.  **Define loops:** Select distinct loops within the circuit. Ensure you cover every component at least once.
3.  **Write equations:** 
    *   Write Junction Rule equations for the nodes.
    *   Write Loop Rule equations for each loop.
4.  **Solve the system:** Use substitution or matrix algebra to solve the system of linear equations for the unknown currents.

## Summary of Component Behavior
Remember that while $R_{eq}$ simplifies the math, the individual components still obey their specific physical properties, often discussed in [[Resistance, Resistivity, and Ohm's Law]] and [[Electric Power]].

*   **In Series:** Current ($I$) is constant through all components; voltage ($V$) divides.
*   **In Parallel:** Voltage ($V$) is constant across all components; current ($I$) divides based on the path of least resistance.