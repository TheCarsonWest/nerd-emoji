# [[Acids and Bases]]
# pH and pOH: An AP Chemistry Rundown

This rundown covers the fundamental concepts of pH and pOH, essential for understanding acids, bases, and equilibrium in AP Chemistry.

## 1. Introduction to pH and pOH

pH and pOH are scales used to express the acidity or basicity (alkalinity) of an aqueous solution. They are logarithmic scales based on the concentration of hydrogen ions ($\text{H}^+$ or $\text{H}_3\text{O}^+$) and hydroxide ions ($\text{OH}^-$), respectively.

## 2. Defining pH and pOH

*   **pH:** The negative base-10 logarithm of the hydrogen ion concentration.

    $$\text{pH} = -\log[\text{H}^+]$$

*   **pOH:** The negative base-10 logarithm of the hydroxide ion concentration.

    $$\text{pOH} = -\log[\text{OH}^-]$$

## 3. The Ion Product of Water ($K_w$)

Water undergoes self-ionization to a very small extent, producing hydrogen and hydroxide ions:

    $$\text{H}_2\text{O}(l) \rightleftharpoons \text{H}^+(aq) + \text{OH}^-(aq)$$

The equilibrium constant for this reaction is the ion product of water, $K_w$:

    $$K_w = [\text{H}^+][\text{OH}^-]$$

At 25°C, $K_w = 1.0 \times 10^{-14}$. [[Kw and Temperature]]

Taking the negative logarithm of both sides:

    $$-\log K_w = -\log([\text{H}^+][\text{OH}^-])$$
    $$-\log K_w = -\log[\text{H}^+] - \log[\text{OH}^-]$$
    $$\text{p}K_w = \text{pH} + \text{pOH}$$

Since $K_w = 1.0 \times 10^{-14}$ at 25°C, $\text{p}K_w = 14$.  Therefore:

    $$\text{pH} + \text{pOH} = 14 \text{ (at 25°C)}$$

## 4. pH Scale and Acidity/Basicity

The pH scale typically ranges from 0 to 14.

*   **pH < 7:** Acidic solution (higher concentration of $\text{H}^+$ than $\text{OH}^-$)
*   **pH = 7:** Neutral solution (equal concentrations of $\text{H}^+$ and $\text{OH}^-$)
*   **pH > 7:** Basic (alkaline) solution (lower concentration of $\text{H}^+$ than $\text{OH}^-$)

## 5. Relating pH, pOH, $[\text{H}^+]$, and $[\text{OH}^-]$

You can convert between these values using the following relationships:

*   $[\text{H}^+] = 10^{-\text{pH}}$
*   $[\text{OH}^-] = 10^{-\text{pOH}}$
*   $\text{pH} = -\log[\text{H}^+]$
*   $\text{pOH} = -\log[\text{OH}^-]$
*   $\text{pH} + \text{pOH} = 14$ (at 25°C)
*   $[\text{H}^+][\text{OH}^-] = 1.0 \times 10^{-14}$ (at 25°C)

## 6. Strong Acids and Bases

Strong acids and bases completely dissociate in water. This simplifies pH and pOH calculations. [[Strong Acids and Bases]]

*   **Strong Acid:** For example, if $[\text{HCl}] = 0.01 \text{ M}$, then $[\text{H}^+] = 0.01 \text{ M}$.  Therefore, $\text{pH} = -\log(0.01) = 2$.

*   **Strong Base:** For example, if $[\text{NaOH}] = 0.01 \text{ M}$, then $[\text{OH}^-] = 0.01 \text{ M}$.  Therefore, $\text{pOH} = -\log(0.01) = 2$, and $\text{pH} = 14 - 2 = 12$.

## 7. Weak Acids and Bases

Weak acids and bases only partially dissociate in water.  Therefore, you must use equilibrium constants ($K_a$ for weak acids and $K_b$ for weak bases) and ICE tables to determine the $[\text{H}^+]$ or $[\text{OH}^-]$ concentration and subsequently calculate pH or pOH. [[Weak Acids and Bases]]

*   **Weak Acid:** HA(aq) + H<sub>2</sub>O(l) ⇌ H<sub>3</sub>O<sup>+</sup>(aq) + A<sup>-</sup>(aq)
 $$K_a = \frac{[H_3O^+][A^-]}{[HA]}$$

*   **Weak Base:** B(aq) + H<sub>2</sub>O(l) ⇌ BH<sup>+</sup>(aq) + OH<sup>-</sup>(aq)
    $$K_b = \frac{[BH^+][OH^-]}{[B]}$$

## 8.  Relationship between $K_a$ and $K_b$

For a conjugate acid-base pair:

    $$K_a \times K_b = K_w$$

Taking the negative logarithm:

    $$\text{p}K_a + \text{p}K_b = \text{p}K_w = 14 \text{ (at 25°C)}$$

## 9. Polyprotic Acids

Polyprotic acids have more than one ionizable proton (e.g., $\text{H}_2\text{SO}_4$, $\text{H}_3\text{PO}_4$).  They dissociate in a stepwise manner, each with its own $K_a$ value ($K_{a1}$, $K_{a2}$, etc.).  The first dissociation is typically the most significant contributor to the $[\text{H}^+]$ concentration. [[Polyprotic Acids]]
