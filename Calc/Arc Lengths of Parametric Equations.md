
# [[Calc Home]]
# AP Calculus BC Notes: Arc Lengths of Parametric Equations

Arc length is a fundamental concept in calculus that allows us to measure the distance along a curve. For parametric equations, which describe a curve using a parameter (often $t$), the method for finding arc length is particularly elegant and extends concepts from [[Calculus and Vector-Valued Functions]].

---

## 1. Introduction to Arc Length

When a curve is defined by parametric equations $x = f(t)$ and $y = g(t)$, we can trace its path as the parameter $t$ varies over a given interval $[a, b]$. The arc length represents the total distance traveled along this curve without retracing. This concept is crucial for understanding the path length of objects in [[Motion Problems with Parametric and Vector-Valued Functions]] and for various applications in physics and engineering.

---

## 2. The Arc Length Formula for Parametric Curves

To find the arc length $L$ of a parametric curve defined by $x = f(t)$ and $y = g(t)$ from $t=a$ to $t=b$, we use the following integral formula. This formula assumes that $f'(t)$ and $g'(t)$ are continuous on $[a, b]$ and that the curve does not intersect itself on the interval (or if it does, we only measure the length of one traversal).

The arc length $L$ is given by:

$$
L = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt
$$

### Breakdown of the Formula Components:

| Component | Description | Relevance |
| :-------- | :---------- | :-------- |
| $\frac{dx}{dt}$ | Derivative of $x$ with respect to $t$ | Represents the instantaneous rate of change of the $x$-coordinate. Crucial for [[Differentiating Parametric Equations]]. |
| $\frac{dy}{dt}$ | Derivative of $y$ with respect to $t$ | Represents the instantaneous rate of change of the $y$-coordinate. Also from [[Differentiating Parametric Equations]]. |
| $\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$ | Magnitude of the velocity vector | This term, often denoted as $ds/dt$, represents the instantaneous speed along the curve. It's derived from the Pythagorean theorem on infinitesimal changes $dx$ and $dy$. |
| $\int_{a}^{b} \dots dt$ | Definite integral over $[a, b]$ | Sums up these infinitesimal speeds over the entire parameter interval to give the total length. |

---

## 3. Derivation Intuition [[Derivation of Arc Length Formula]]

The formula can be intuitively understood by considering small segments of the curve. For an infinitesimal change in $t$, say $dt$, the changes in $x$ and $y$ are $dx = \frac{dx}{dt} dt$ and $dy = \frac{dy}{dt} dt$. The length of this small segment, $ds$, can be approximated using the Pythagorean theorem:

$$(ds)^2 = (dx)^2 + (dy)^2$$
$$ds = \sqrt{(dx)^2 + (dy)^2}$$

Substituting the expressions for $dx$ and $dy$:

$$
ds = \sqrt{\left(\frac{dx}{dt} dt\right)^2 + \left(\frac{dy}{dt} dt\right)^2} = \sqrt{\left(\frac{dx}{dt}\right)^2 dt^2 + \left(\frac{dy}{dt}\right)^2 dt^2}
$$
$$
ds = \sqrt{\left[\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2\right] dt^2} = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt
$$

Integrating $ds$ from $t=a$ to $t=b$ gives the total arc length $L$.

---

## 4. Key Considerations and Tips

*   **Continuity of Derivatives:** Ensure that $\frac{dx}{dt}$ and $\frac{dy}{dt}$ are continuous on the interval $[a, b]$. If they are not, the formula may not apply directly, or the curve might have sharp corners.
*   **Smooth Curve:** The curve must be "smooth" meaning its derivatives are continuous and not simultaneously zero, which prevents cusps or corners.
*   **Non-Self-Intersecting:** For a simple arc length calculation, the curve should not intersect itself on the given interval, or you'll be calculating the length of multiple traversals. If it does, you might need to adjust the integration limits.
*   **Symmetry:** Look for symmetry to simplify calculations or to determine the correct limits of integration.
*   **Calculator Use:** Integrals involving square roots can often be complex. Be prepared to use a graphing calculator (e.g., TI-84, TI-Nspire) to evaluate the definite integral, especially if it's non-standard.

---

## 5. Example Walkthrough

**Problem:** Find the arc length of the curve defined by $x = t^2$ and $y = \frac{1}{3}t^3$ from $t=0$ to $t=\sqrt{3}$.

**Solution:**

1.  **Find the derivatives:**
    $\frac{dx}{dt} = \frac{d}{dt}(t^2) = 2t$
    $\frac{dy}{dt} = \frac{d}{dt}\left(\frac{1}{3}t^3\right) = t^2$

2.  **Square the derivatives and sum them:**
    $\left(\frac{dx}{dt}\right)^2 = (2t)^2 = 4t^2$
    $\left(\frac{dy}{dt}\right)^2 = (t^2)^2 = t^4$
    $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 4t^2 + t^4 = t^2(4 + t^2)$

3.  **Take the square root:**
    $\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = \sqrt{t^2(4 + t^2)} = |t|\sqrt{4 + t^2}$
    Since $t$ is on the interval $[0, \sqrt{3}]$, $t \ge 0$, so $|t|=t$.
    Thus, we have $t\sqrt{4 + t^2}$.

4.  **Set up and evaluate the integral:**
    $L = \int_{0}^{\sqrt{3}} t\sqrt{4 + t^2} dt$

    We can use a u-substitution: Let $u = 4 + t^2$, then $du = 2t dt$, so $t dt = \frac{1}{2} du$.
    When $t=0$, $u = 4 + 0^2 = 4$.
    When $t=\sqrt{3}$, $u = 4 + (\sqrt{3})^2 = 4 + 3 = 7$.

    $L = \int_{4}^{7} \sqrt{u} \cdot \frac{1}{2} du = \frac{1}{2} \int_{4}^{7} u^{1/2} du$
    $L = \frac{1}{2} \left[\frac{u^{3/2}}{3/2}\right]_{4}^{7} = \frac{1}{2} \cdot \frac{2}{3} \left[u^{3/2}\right]_{4}^{7} = \frac{1}{3} \left[7^{3/2} - 4^{3/2}\right]$
    $L = \frac{1}{3} \left[7\sqrt{7} - (\sqrt{4})^3\right] = \frac{1}{3} \left[7\sqrt{7} - 2^3\right] = \frac{1}{3} \left[7\sqrt{7} - 8\right]$

The arc length of the curve is $\frac{7\sqrt{7}-8}{3}$.