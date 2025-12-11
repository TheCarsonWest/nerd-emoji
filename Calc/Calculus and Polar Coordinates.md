
# [[Calc Home]]
# AP Calculus BC Notes: Calculus and Polar Coordinates

Polar coordinates offer an alternative way to describe points in a plane, particularly useful for curves with rotational symmetry. Instead of $(x, y)$, a point is given by $(r, \theta)$, where $r$ is the directed distance from the origin (pole) and $\theta$ is the angle from the positive x-axis.

## 1. Converting Between Polar and Cartesian Coordinates

Understanding the relationship between coordinate systems is crucial for applying calculus concepts.

**Polar to Cartesian:**
Given $(r, \theta)$ in polar coordinates, the corresponding Cartesian coordinates $(x, y)$ are:
$$
x = r \cos \theta
$$
$$
y = r \sin \theta
$$

**Cartesian to Polar:**
Given $(x, y)$ in Cartesian coordinates, the corresponding polar coordinates $(r, \theta)$ are:
$$
r^2 = x^2 + y^2 \quad \text{or} \quad r = \sqrt{x^2 + y^2}
$$
$$
\tan \theta = \frac{y}{x} \quad \text{(when } x \neq 0)
$$
*Remember to consider the quadrant of $(x, y)$ when determining $\theta$ from $\tan \theta$*.

## 2. Derivatives in Polar Coordinates

One of the primary calculus applications is finding the slope of a tangent line to a polar curve $r = f(\theta)$. We use the chain rule, treating $x$ and $y$ as functions of $\theta$.

Given $r = f(\theta)$:
1.  Express $x$ and $y$ in terms of $\theta$:
    $x = f(\theta) \cos \theta$
    $y = f(\theta) \sin \theta$
2.  Find $\frac{dx}{d\theta}$ and $\frac{dy}{d\theta}$:
    $$
    \frac{dx}{d\theta} = f'(\theta) \cos \theta - f(\theta) \sin \theta
    $$
    $$
    \frac{dy}{d\theta} = f'(\theta) \sin \theta + f(\theta) \cos \theta
    $$
3.  The slope of the tangent line $\frac{dy}{dx}$ is then:
    $$
    \frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{f'(\theta) \sin \theta + f(\theta) \cos \theta}{f'(\theta) \cos \theta - f(\theta) \sin \theta}
    $$
    This formula is valid provided $\frac{dx}{d\theta} \neq 0$.

**Special Cases:**
*   **Horizontal Tangent:** Occurs when $\frac{dy}{d\theta} = 0$ and $\frac{dx}{d\theta} \neq 0$.
*   **Vertical Tangent:** Occurs when $\frac{dx}{d\theta} = 0$ and $\frac{dy}{d\theta} \neq 0$.
*   If both $\frac{dy}{d\theta} = 0$ and $\frac{dx}{d\theta} = 0$, L'Hôpital's Rule or further analysis may be needed.

## 3. [[Arc Lengths of Polar Curves]]

The arc length $L$ of a polar curve $r = f(\theta)$ from $\theta = \alpha$ to $\theta = \beta$ is given by the formula:
$$
L = \int_{\alpha}^{\beta} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} d\theta
$$
This formula is derived from the parametric arc length formula by substituting $x = r \cos \theta$ and $y = r \sin \theta$ and finding $\frac{dx}{d\theta}$ and $\frac{dy}{d\theta}$.

## 4. [[The Area Within a Polar Curve]]

The area $A$ of the region bounded by a polar curve $r = f(\theta)$ and two rays $\theta = \alpha$ and $\theta = \beta$ is given by:
$$
A = \frac{1}{2} \int_{\alpha}^{\beta} r^2 d\theta
$$
This formula is derived from approximating the area with sectors of circles. Remember to choose the limits of integration ($\alpha$ and $\beta$) carefully to cover the desired region exactly once.

## 5. [[The Area Between Polar Curves]]

To find the area between two polar curves, $r_{outer} = f(\theta)$ and $r_{inner} = g(\theta)$, from $\theta = \alpha$ to $\theta = \beta$:
$$
A = \frac{1}{2} \int_{\alpha}^{\beta} (r_{outer}^2 - r_{inner}^2) d\theta
$$
It's crucial to correctly identify which curve is the "outer" and which is the "inner" in the specified interval. Sketching the curves is highly recommended.

## 6. Applications to Motion

Similar to [[Motion Problems with Parametric and Vector-Valued Functions]], we can analyze motion along a polar curve. If an object's position is given by $(r(t), \theta(t))$ (or $r(\theta)$ and $\theta(t)$), then its velocity and acceleration vectors can be found by converting to Cartesian coordinates or using polar basis vectors. However, for AP Calculus BC, the focus is generally on $\frac{dy}{dx}$ and arc length.

For more advanced topics in this area, you might refer to notes on [[Calculus and Vector-Valued Functions]].