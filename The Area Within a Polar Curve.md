# [[Calc home]]
# The Area Within a Polar Curve

In AP Calculus BC, we extend our understanding of area to regions defined by polar coordinates. Unlike Cartesian coordinates ($x, y$), where area is found by integrating functions of $x$ or $y$ with respect to $x$ or $y$, polar coordinates ($r, \theta$) require a different approach.

## The Area Formula for Polar Curves

When calculating the area enclosed by a polar curve $r = f(\theta)$ from $\theta = \alpha$ to $\theta = \beta$, we imagine dividing the region into an infinite number of tiny sectors. Each sector can be approximated as a triangle with a small angle $d\theta$ and radius $r$. The area of such a sector is approximately $\frac{1}{2}r^2 d\theta$. Summing these infinitesimal areas leads to the definite integral:

**Starred Block: Fundamental Area Formula**
The area $A$ of a region bounded by the polar curve $r = f(\theta)$ and radial lines $\theta = \alpha$ and $\theta = \beta$ is given by:
$$A = \int_{\alpha}^{\beta} \frac{1}{2} r^2 d\theta$$
where $r$ is expressed as a function of $\theta$.

## Key Steps for Finding Area

Finding the area of a polar region involves careful identification of the curve and its limits.

| Step | Description |
| :--- | :---------- |
| **1. Identify $r = f(\theta)$** | Ensure the polar equation is in the form $r$ as a function of $\theta$. |
| **2. Determine Limits ($\alpha, \beta$)** | This is crucial. Find the range of $\theta$ that traces the desired region exactly once. For a full loop of a curve, $\alpha$ is often $0$ and $\beta$ is $2\pi$ or a smaller interval like $0$ to $\pi$ if the curve has symmetry (e.g., a circle centered at the origin, or a rose curve with an even number of petals). For a single petal of a rose curve, you'll need to find the $\theta$ values where $r=0$. |
| **3. Set Up the Integral** | Substitute $f(\theta)$ for $r$ into the formula: $A = \int_{\alpha}^{\beta} \frac{1}{2} [f(\theta)]^2 d\theta$. |
| **4. Evaluate the Integral** | Use integration techniques (often involving trigonometric identities like $\sin^2 x = \frac{1 - \cos(2x)}{2}$ or $\cos^2 x = \frac{1 + \cos(2x)}{2}$) to solve the definite integral. |

**Starred Block: Critical Tip for Limits**
Always sketch the polar curve to determine the correct limits of integration ($\alpha$ and $\beta$). Integrating over an incorrect interval can lead to an area that is too large (tracing multiple times) or too small (missing parts of the region).

## Area Between Two Polar Curves

To find the area between two polar curves, $r_{outer} = f(\theta)$ and $r_{inner} = g(\theta)$, where $f(\theta) \ge g(\theta)$ over the interval $[\alpha, \beta]$, we subtract the area of the inner region from the area of the outer region.

**Starred Block: Area Between Curves Formula**
The area $A$ between two polar curves $r_{outer} = f(\theta)$ and $r_{inner} = g(\theta)$ from $\theta = \alpha$ to $\theta = \beta$ is:
$$A = \int_{\alpha}^{\beta} \frac{1}{2} (r_{outer}^2 - r_{inner}^2) d\theta$$
Ensure that $r_{outer}$ is always greater than or equal to $r_{inner}$ in the region of interest. Finding the intersection points of the two curves is often necessary to determine $\alpha$ and $\beta$.

## Common Pitfalls & Tips

*   **Squaring $r$**: Remember to square the entire function $f(\theta)$, not just $r$.
*   **Trigonometric Identities**: Be prepared to use identities to simplify integrands, especially for $\sin^2\theta$ and $\cos^2\theta$.
*   **Symmetry**: Utilize symmetry to simplify calculations. If a curve is symmetric about the polar axis, you might calculate the area for $0 \le \theta \le \pi$ and multiply by 2, or $0 \le \theta \le \pi/2$ and multiply by 4, depending on the curve.
*   **Intersection Points**: For areas between curves, find the $\theta$ values where $f(\theta) = g(\theta)$ to establish integration limits. These points often define the boundaries of the region.