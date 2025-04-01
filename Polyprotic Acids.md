# [[Acids and Bases]]
# Polyprotic Acids: AP Chemistry Rundown

Polyprotic acids are acids that can donate more than one proton (H⁺) per molecule in solution. This means they have multiple ionization steps, each with its own equilibrium constant.

## General Concepts

*   **Definition:** Acids that can donate more than one proton (H⁺).
*   **Examples:** Sulfuric acid (H₂SO₄), carbonic acid (H₂CO₃), phosphoric acid (H₃PO₄).
*   **Ionization Steps:** Each proton donation is a separate step with its own equilibrium.

## Ionization Steps and Equilibrium Constants

A polyprotic acid with 'n' protons will have 'n' ionization steps.  Each step has an associated acid dissociation constant (Ka).

For a generic diprotic acid, H₂A:

1.  **First Ionization:**
    $$H_2A(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + HA^-(aq) \quad K_{a1} = \frac{[H_3O^+][HA^-]}{[H_2A]}$$

2.  **Second Ionization:**
    $$HA^-(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + A^{2-}(aq) \quad K_{a2} = \frac{[H_3O^+][A^{2-}]}{[HA^-]}$$

*   **Key Point:** Generally,  $K_{a1} > K_{a2} > K_{a3}...$. This is because it's easier to remove a proton from a neutral molecule than from a negatively charged ion. Removing a positively charged proton from a negatively charged species requires more energy.

## Calculating pH of Polyprotic Acid Solutions

Calculating the pH of a polyprotic acid solution requires considering the multiple ionization steps. However, due to the significant difference in $K_a$ values, we can often simplify the calculation.

*   **Simplification:** In most cases, the contribution of the second (and subsequent) ionization steps to the [H₃O⁺] concentration is negligible compared to the first ionization step.  Therefore, we can often calculate the pH by only considering the first ionization.

*   **When Simplification Fails:**  The simplification is not valid when:
    *   $K_{a1}$ and $K_{a2}$ are close in value (difference is less than 100x).
    *   The acid is very dilute.
    *   You need to calculate the concentration of the fully deprotonated species (e.g., [A²⁻] in the H₂A example).

### Example: Calculating pH of a Diprotic Acid Solution

Let's say we have a 0.1 M solution of H₂A with $K_{a1} = 1.0 \times 10^{-3}$ and $K_{a2} = 1.0 \times 10^{-7}$.

1.  **First Ionization:**  Set up an ICE table for the first ionization:

    |             | H₂A    | H₃O⁺   | HA⁻    |
    | :---------- | :----- | :----- | :----- |
    | Initial     | 0.1    | 0      | 0      |
    | Change      | -x     | +x     | +x     |
    | Equilibrium | 0.1-x  | x      | x      |

    $K_{a1} = \frac{[H_3O^+][HA^-]}{[H_2A]} = \frac{x^2}{0.1-x} = 1.0 \times 10^{-3}$

    Since $K_{a1}$ is small, we can often assume that 'x' is negligible compared to 0.1 (0.1-x ≈ 0.1). However, in this case, we should check the 5% rule.

    $x = \sqrt{(1.0 \times 10^{-3})(0.1)} = \sqrt{1.0 \times 10^{-4}} = 0.01$

    $\frac{0.01}{0.1} \times 100\% = 10\%$ This is greater than 5%, so we must use the quadratic formula:

    $x^2 + 0.001x - 0.0001 = 0$

    $x = \frac{-0.001 \pm \sqrt{0.001^2 - 4(1)(-0.0001)}}{2(1)} = \frac{-0.001 \pm \sqrt{0.000001 + 0.0004}}{2} = \frac{-0.001 \pm \sqrt{0.000401}}{2}$

    $x = \frac{-0.001 \pm 0.020025}{2}$

    We take the positive root: $x = \frac{0.019025}{2} = 0.0095125$

    $[H_3O^+] \approx 0.0095 M$

    $pH = -log(0.0095) \approx 2.02$

2.  **Second Ionization:**  Now consider the second ionization:

    |             | HA⁻       | H₃O⁺      | A²⁻    |
    | :---------- | :-------- | :-------- | :----- |
    | Initial     | 0.0095    | 0.0095    | 0      |
    | Change      | -y        | +y        | +y     |
    | Equilibrium | 0.0095-y | 0.0095+y | y      |

    $K_{a2} = \frac{[H_3O^+][A^{2-}]}{[HA^-]} = \frac{(0.0095+y)(y)}{0.0095-y} = 1.0 \times 10^{-7}$

    Since $K_{a2}$ is very small, we can assume y is negligible compared to 0.0095 (0.0095+y ≈ 0.0095 and 0.0095-y ≈ 0.0095).

    $K_{a2} = \frac{(0.0095)(y)}{0.0095} = y = 1.0 \times 10^{-7}$

    $[A^{2-}] = 1.0