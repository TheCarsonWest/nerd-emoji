# [[ICE Tables]]
# Approximations in [[Equilibrium Calculations]]

This note covers approximations used to simplify equilibrium calculations, particularly when dealing with weak acids/bases and solubility.  The goal is to avoid using the quadratic formula.

**Key Assumption:**  The approximation relies on the assumption that the change in concentration ($x$) is negligible compared to the initial concentration.  This is valid when $K$ is small and the initial concentration is relatively large.

**1.  Percent Ionization/Dissociation:**

The percent ionization (or dissociation) is a measure of how much of a weak acid or base dissociates in solution.  It's calculated as:

$ \text{Percent ionization} = \frac{[H^+]]_{eq}}{[HA]]_i} \times 100\% $  for a weak acid $HA$

$ \text{Percent dissociation} = \frac{[A^-]]_{eq}}{[HA]]_i} \times 100\% $  for a weak acid $HA$

*A similar equation applies to weak bases.*

**2. The 5% Rule:**

The 5% rule is a common criterion for determining if the approximation is valid.  If the percent ionization (or dissociation) is less than 5%, then the approximation is considered acceptable.

**3.  Weak Acid [[Equilibrium]]:**

Consider the dissociation of a weak acid $HA$:

$$ HA(aq) \rightleftharpoons H^+(aq) + A^-(aq) $$

$K_a = \frac{[H^+]][A^-]]}{[HA]]}$

**Approximation:** If we assume that $x$ (the change in concentration) is negligible compared to $[HA]]_i$, then $[HA]]_{eq} \approx [HA]]_i$.  This simplifies the $K_a$ expression to:

$K_a \approx \frac{x^2}{[HA]]_i}$

where $x = [H^+]]=[A^-]]$.  Solving for $x$ gives:

$x \approx \sqrt{K_a[HA]]_i}$

After solving for $x$, check the 5% rule to confirm the validity of the approximation.

**4. Weak Base [[Equilibrium:**  (Weak Base Equilibrium]])

**5.  Solubility Equilibria:** ([[Solubility Equilibria]])

**6.  When the Approximation Fails:**

If the 5% rule is not met, the quadratic formula must be used to solve for $x$ exactly.

**7. Example:**

Calculate the pH of a 0.10 M solution of acetic acid ($K_a = 1.8 \times 10^{-5}$).

Using the approximation:

$x = [H^+]] \approx \sqrt{(1.8 \times 10^{-5})(0.10)} \approx 1.34 \times 10^{-3} M$

Percent ionization = $\frac{1.34 \times 10^{-3}}{0.10} \times 100\% \approx 1.34\%$

Since this is less than 5%, the approximation is valid.

$pH = -\log(1.34 \times 10^{-3}) \approx 2.87$

**8.  Further Reading:** ([[Quadratic Formula and Equilibrium]])


