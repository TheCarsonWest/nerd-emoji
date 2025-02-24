L'Hopital's Rule is a powerful tool for evaluating limits involving [[Indeterminate Forms]]. 
### L'Hopital's Rule Statement

**If the limit of a fraction as $x$ approaches $a$ results in an indeterminate form (0/0 or ∞/∞), then:**

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**provided that the limit on the right-hand side exists or is $\pm \infty$.**

**In simpler terms:**  To evaluate the limit of a fraction that results in an indeterminate form, take the [[derivative]] of both the numerator and denominator separately, and then evaluate the limit again.

### Important Notes

* ### **L'Hopital's Rule only applies to [[Indeterminate Forms]] (0/0 or ∞/∞).** Don't use it for other forms like 0/∞ or ∞/0.
* **The rule can be applied repeatedly** if the limit of the derivatives still results in an indeterminate form.
* **L'Hopital's Rule is not always the easiest method** to evaluate a limit. Sometimes, algebraic manipulation or other techniques may be more efficient.
### Example

Let's say we want to evaluate the limit:
### $$\lim_{x \to 0} \frac{\sin(x)}{x}$$
**1. Indeterminate Form:**  Substituting $x = 0$ directly gives us $\frac{\sin(0)}{0} = \frac{0}{0}$, which is an indeterminate form.

**2. Apply L'Hopital's Rule:**

*  $f(x) = \sin(x)$
*  $g(x) = x$
*  $f'(x) = \cos(x)$
*  $g'(x) = 1$

Therefore, we have:

$$\lim_{x \to 0} \frac{\sin(x)}{x} = \lim_{x \to 0} \frac{\cos(x)}{1}$$

**3. Evaluate the Limit:**

$$\lim_{x \to 0} \frac{\cos(x)}{1} = \frac{\cos(0)}{1} = 1$$

**So, $\lim_{x \to 0} \frac{\sin(x)}{x} = 1$.**
