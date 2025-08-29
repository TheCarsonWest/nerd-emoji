# 8.9: Henderson-Hasselbalch Equation

## Introduction
The Henderson-Hasselbalch equation is a useful tool for calculating the pH of a [[Buffer Solutions]]. It provides a quick method for determining the pH of a solution containing a weak acid and its conjugate base (or a weak base and its conjugate acid).

## The Equation

The Henderson-Hasselbalch equation is given by:

$$pH = pK_a + log \frac{[A^-]}{[HA]}$$

Where:
*   $pH$ is the measure of acidity.
*   $pK_a$ is the negative logarithm of the [[Acid Dissociation Constant]] ($K_a$) of the weak acid.
    $$pK_a = -log(K_a)$$
*   $[A^-]$ is the concentration of the conjugate base.
*   $[HA]$ is the concentration of the weak acid.

Alternatively, for a weak base and its conjugate acid:

$$pOH = pK_b + log \frac{[HB^+]}{[B]}$$

Where:
*   $pOH$ is the measure of basicity.
*   $pK_b$ is the negative logarithm of the [[Base Dissociation Constant]] ($K_b$) of the weak base.
    $$pK_b = -log(K_b)$$
*   $[HB^+]$ is the concentration of the conjugate acid.
*   $[B]$ is the concentration of the weak base.

## Derivation of the Henderson-Hasselbalch Equation

The Henderson-Hasselbalch equation is derived from the acid dissociation equilibrium expression.  Consider the equilibrium for a weak acid, $HA$:

$$HA(aq) \rightleftharpoons H^+(aq) + A^-(aq)$$

The [[Acid Dissociation Constant]] ($K_a$) is:

$$K_a = \frac{[H^+][A^-]}{[HA]}$$

Taking the negative logarithm of both sides:

$$-log(K_a) = -log\left(\frac{[H^+][A^-]}{[HA]}\right)$$

$$-log(K_a) = -log[H^+] - log\left(\frac{[A^-]}{[HA]}\right)$$

Since $pK_a = -log(K_a)$ and $pH = -log[H^+]$:

$$pK_a = pH - log\left(\frac{[A^-]}{[HA]}\right)$$

Rearranging to solve for pH yields the Henderson-Hasselbalch equation:

$$pH = pK_a + log\left(\frac{[A^-]}{[HA]}\right)$$

## Using the Henderson-Hasselbalch Equation

1.  **Identify the weak acid/base and its conjugate pair.**
2.  **Determine the $K_a$ (or $K_b$) value.**  If given $K_a$, calculate $pK_a$ ($pK_a = -log(K_a)$). If given $K_b$, calculate $pK_b$ ($pK_b = -log(K_b)$).
3.  **Determine the concentrations of the weak acid/base and its conjugate.**
4.  **Plug the values into the appropriate equation and solve for pH or pOH.**
5.  **If you calculated pOH, find pH using the relationship:**
    $$pH + pOH = 14$$

## Important Considerations

*   **Validity:** The Henderson-Hasselbalch equation is most accurate when the concentrations of the acid and its conjugate base are relatively high and close to each other.  It is less accurate when either $[HA]$ or $[A^-]$ is very small compared to the other.  It is most reliable when the ratio of $[A^-]/[HA]$ is between 0.1 and 10.
*   **Approximations:** The equation assumes that the [[Equilibrium Concentrations]] of the acid and base are approximately equal to their initial concentrations. This assumption is valid when the acid is weak and the concentrations are sufficiently high.
*   **Buffer Capacity:** The Henderson-Hasselbalch equation describes the pH of a buffer, but it doesn't tell us about the buffer capacity, which is the amount of acid or base a buffer can neutralize before significant pH change occurs.

## Applications

*   **Calculating the pH of buffer solutions:** Determining the pH of a solution containing a weak acid and its conjugate base, or a weak base and its conjugate acid.
*   **Preparing buffer solutions:** Determining the amounts of acid and base needed to create a buffer with a specific pH.
*   **Estimating pH changes after adding acid or base to a buffer:**  While [[ICE Tables]] would be more accurate, the Henderson-Hasselbalch equation can provide an estimate.
