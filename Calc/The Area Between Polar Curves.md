
# [[Calc Home]]
# AP Calculus BC Notes: Topic 9.9 - The Area Between Polar Curves

## Introduction

This topic builds upon the concept of [[The Area Within a Polar Curve]] to calculate the area enclosed between two or more polar curves. Understanding how to set up and evaluate definite integrals in polar coordinates is crucial. Recall that in polar coordinates, area is swept out by a ray originating from the pole ($r=0$).

## General Formula for Area Between Polar Curves

To find the area between two polar curves, $r_1 = f(\theta)$ and $r_2 = g(\theta)$, where $r_2 \ge r_1$ (meaning $r_2$ is the "outer" curve and $r_1$ is the "inner" curve) over an interval $[\alpha, \beta]$, we subtract the area of the inner curve from the area of the outer curve.

The formula for the area $A$ between the curves is:

$$ A = \frac{1}{2} \int_{\alpha}^{\beta} (r_{outer}^2 - r_{inner}^2) \, d\theta $$

Where:
*   $r_{outer}$ is the function representing the curve farther from the pole.
*   $r_{inner}$ is the function representing the curve closer to the pole.
*   $\alpha$ and $\beta$ are the angles defining the region of interest. These are often [[Points of Intersection of Polar Curves]] or angles that complete a full loop for a curve.

## Identifying Outer and Inner Curves

Determining which curve is $r_{outer}$ and which is $r_{inner}$ is critical. This often requires:
1.  **Graphing the curves:** Sketching the polar graphs can visually clarify which curve is farther from the pole in the specified interval.
2.  **Testing points:** For a given $\theta$ within the interval, evaluate both $r_1(\theta)$ and $r_2(\theta)$. The one with the larger absolute value of $r$ will be the outer curve for that specific $\theta$. However, be careful with negative $r$ values, as $r^2$ will always be positive. The "outer" curve is simply the one with the larger radius *squared* at any given angle.

## Steps to Calculate Area Between Polar Curves

1.  **Graph the curves:** Visualize the region whose area you need to find.
2.  **Find points of intersection (if necessary):** Set $r_1(\theta) = r_2(\theta)$ to find the angles where the curves intersect. These angles often define the limits of integration. Remember that the pole ($r=0$) can be an intersection point even if $r_1(\theta) = r_2(\theta)$ doesn't yield it (e.g., if one curve passes through the pole at $\theta_1$ and another at $\theta_2$).
3.  **Determine the limits of integration ($\alpha$ and $\beta$):** These angles define the specific region whose area you are calculating. They might be intersection points or angles that complete a lobe or full curve.
4.  **Identify $r_{outer}$ and $r_{inner}$:** For the chosen interval $[\alpha, \beta]$, determine which function yields a larger radial distance (or larger $r^2$) for the region you are interested in.
5.  **Set up the integral:** Substitute $r_{outer}$ and $r_{inner}$ into the general formula.
6.  **Evaluate the integral:** Use techniques of integration to find the definite integral.

### Example Scenario

Consider finding the area inside $r = 3\sin\theta$ and outside $r = 1$.

| Step | Description |
| :--- | :--- |
| **1. Graph** | $r=3\sin\theta$ is a circle centered at $(0, 3/2)$ with radius $3/2$. $r=1$ is a circle centered at the pole with radius $1$. |
| **2. Intersections** | Set $3\sin\theta = 1 \implies \sin\theta = 1/3$. Let $\theta_0 = \arcsin(1/3)$. The intersection points are at $\theta_0$ and $\pi - \theta_0$. |
| **3. Limits** | The area starts at $\theta_0$ and ends at $\pi - \theta_0$. So $\alpha = \theta_0$ and $\beta = \pi - \theta_0$. |
| **4. Identify** | For $\theta \in [\theta_0, \pi - \theta_0]$, $3\sin\theta \ge 1$, so $r_{outer} = 3\sin\theta$ and $r_{inner} = 1$. |
| **5. Setup** | $$ A = \frac{1}{2} \int_{\theta_0}^{\pi - \theta_0} ((3\sin\theta)^2 - (1)^2) \, d\theta $$ |
| **6. Evaluate** | $$ A = \frac{1}{2} \int_{\theta_0}^{\pi - \theta_0} (9\sin^2\theta - 1) \, d\theta $$ Use the identity $\sin^2\theta = \frac{1-\cos(2\theta)}{2}$. |

## Common Pitfalls

*   **Incorrect Limits of Integration:** Make sure the limits precisely define the region whose area you want. This often involves finding all [[Points of Intersection of Polar Curves]].
*   **Switching $r_{outer}$ and $r_{inner}$:** This will result in a negative area, which is incorrect. Always ensure you subtract the inner squared radius from the outer squared radius.
*   **Overlapping Regions:** Sometimes, curves might overlap in a way that requires breaking the integral into multiple parts, or using symmetry to simplify.
*   **The Pole ($r=0$):** Be particularly careful when curves pass through the pole. An intersection at $r=0$ means $f(\theta_1)=0$ and $g(\theta_2)=0$, but $\theta_1$ and $\theta_2$ might not be equal. Visualizing the graph is key.

Understanding how to correctly apply the general formula and carefully identify the components for integration will allow you to successfully calculate areas between polar curves. This topic relies heavily on a strong foundation in [[Calculus and Polar Coordinates]] and integral evaluation skills.