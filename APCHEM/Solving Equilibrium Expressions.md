# [[Equilibrium Constant Calculations]]
# Solving [[Equilibrium]] Expressions

This note covers solving equilibrium expressions, focusing on different scenarios and problem-solving strategies.  It assumes familiarity with writing equilibrium expressions.  If not, refer to [[Equilibrium Expressions]].

**1.  Simple [[Equilibrium Calculations]]:**

These involve solving for one unknown in the equilibrium expression, given the equilibrium concentrations of all other species.

* **Example:**  For the reaction $A \rightleftharpoons B$, with $K_c = 10$, and $[A]_{eq} = 2M$. Find $[B]_{eq}$.

   $K_c = \frac{[B]_{eq}}{[A]_{eq}} \implies 10 = \frac{[B]_{eq}}{2} \implies [B]_{eq} = 20M$


**2. [[ICE Tables (Initial, Change, Equilibrium]]):**

These are crucial when only initial concentrations and the equilibrium constant are known.

* **Method:**  Construct a table with columns for initial concentration ([I]), change in concentration ($\Delta$), and equilibrium concentration ([E]).  Use the stoichiometry of the balanced equation to relate changes in concentration.  Solve the resulting equilibrium expression.

* **Example:** For $2A \rightleftharpoons B$, $K_c = 4$, $[A]_i = 1M$, $[B]_i = 0M$. Find equilibrium concentrations.

   | Species | I     | $\Delta$   | E       |
   |---------|-------|-----------|---------|
   | A       | 1     | -2x       | 1-2x    |
   | B       | 0     | +x        | x       |

   $K_c = \frac{[B]_{eq}}{[A]_{eq}^2} = \frac{x}{(1-2x)^2} = 4$.  Solving the quadratic equation gives $x$, and thus equilibrium concentrations.  ([[Solving Quadratic Equations]])

**3. Manipulating [[Equilibrium]] Expressions:**

Sometimes, we need to manipulate the expression before solving. This might involve:

*   **Reversing the reaction:**  $K_{c,rev} = \frac{1}{K_c}$
*   **Multiplying by a factor:** $K_{c,mult} = K_c^n$ (where n is the multiplication factor)

**4.  Approximations:**

If the $K_c$ value is very small or very large, simplifying assumptions can be made to avoid solving complex equations.  This is usually valid if the initial concentration is significantly greater than the value of $K_c$.

*   **Example:**  If $1-2x \approx 1$ in the previous example (because $K_c$ is large), the equation simplifies significantly.

**5.  Complex Scenarios:**

These might involve multiple simultaneous equilibria, or situations where the reaction quotient ($Q$) is compared to $K_c$ to determine the direction the reaction will shift.

* [[Simultaneous Equilibria]]
* [[Reaction Quotient (Q)]]


**6.  Units:**

Remember that equilibrium constants are dimensionless, but the numerical value depends on the units of concentration.  Always specify the units used (e.g., $K_c$ or $K_p$).



This is a starting point – more specific examples and problem types would need to be added for comprehensive understanding.
