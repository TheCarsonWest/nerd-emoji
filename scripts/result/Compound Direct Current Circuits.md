
# [[AP Physics C Home]]
# AP Physics C: Compound Direct Current Circuits

In many practical applications, electrical circuits are not simple, single-loop systems. A **Compound Direct Current (DC) Circuit** is a circuit containing multiple sources of electromotive force (EMF) and/or a network of resistors arranged in complex combinations of series and parallel branches that cannot be reduced to a single equivalent resistor using standard series/parallel formulas.

To analyze these complex circuits, we must rely on the fundamental conservation laws of charge and energy as applied to electrical networks.

## Analyzing Multi-Loop Circuits

When a circuit cannot be simplified by grouping, we utilize the laws developed by Gustav Kirchhoff. These laws allow us to solve for unknown currents and voltages by creating a system of linear equations.

### Kirchhoff's Laws

The foundational principles for solving any DC circuit are:

| Law | Principle | Physics Concept |
| :--- | :--- | :--- |
| [[Kirchhoffs Junction Rule]] | The sum of currents entering a junction equals the sum of currents leaving. | Conservation of Charge |
| [[Kirchhoffs Loop Rule]] | The sum of potential differences around any closed loop is zero. | Conservation of Energy |

### Procedure for Solving Complex Circuits

1.  **Label Currents:** Assign a variable and an arbitrary direction for the current in every unique branch of the circuit. If your guess is wrong, the final value will simply be negative.
2.  **Apply Junction Rule:** Write down equations for as many independent junctions as possible.
3.  **Apply Loop Rule:** Select closed loops in the circuit. Traverse them (usually in the direction of the assumed current) and sum the potential changes to zero.
    *   If you cross a resistor in the direction of current: $\Delta V = -IR$.
    *   If you cross a resistor against the direction of current: $\Delta V = +IR$.
    *   If you cross an EMF source from negative to positive terminal: $\Delta V = +\varepsilon$.
    *   If you cross an EMF source from positive to negative terminal: $\Delta V = -\varepsilon$.
4.  **Solve the System:** With $N$ unknowns, you will need $N$ independent equations derived from the steps above to solve for the currents.

## Example Application: The Two-Loop Circuit

Consider a circuit with two batteries and three resistors arranged such that there is a shared central branch. We define the current through the left loop as $I_1$ and the right loop as $I_2$. The current through the shared middle branch is $(I_1 + I_2)$ or $(I_1 - I_2)$, depending on direction choices.

Applying the loop rule to the left loop with EMF $\varepsilon_1$ and resistors $R_1$ and $R_{shared}$:

$$\varepsilon_1 - I_1 R_1 - (I_1 + I_2)R_{shared} = 0$$

Applying the loop rule to the right loop with EMF $\varepsilon_2$ and resistors $R_2$ and $R_{shared}$:

$$\varepsilon_2 - I_2 R_2 - (I_1 + I_2)R_{shared} = 0$$

By solving these simultaneous equations, one can determine the precise current flowing through every component in the compound circuit.

## Summary of Key Relationships

To fully analyze these circuits, ensure you are comfortable with:
*   [[Resistance, Resistivity, and Ohms Law]] for component-level behavior.
*   [[Electric Power]] to calculate energy dissipation in resistors.
*   [[Simple Circuits]] for identifying basic series/parallel patterns before attempting complex loop analysis.