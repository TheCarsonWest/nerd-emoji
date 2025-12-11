
# [[Calc Home]]
# Differentiating Parametric Equations (Topic 9.1 AP Calculus BC)

Parametric equations define coordinates $x$ and $y$ as functions of a third parameter, usually $t$ (time). For instance, $x = f(t)$ and $y = g(t)$. While these equations describe a curve in the $xy$-plane, sometimes we need to analyze their instantaneous rate of change and concavity without eliminating the parameter. This involves differentiating with respect to $t$ and then using the chain rule to find derivatives in terms of $x$ and $y$.

## 1. The First Derivative: $\frac{dy}{dx}$

To find the slope of the tangent line to a parametric curve at a given point $(x, y)$, we need $\frac{dy}{dx}$. We achieve this by applying the chain rule. Since $y$ is a function of $t$, and $x$ is a function of $t$, we can express $\frac{dy}{dx}$ as:

$$
\frac{dy}{dx} = \frac{dy/dt}{dx/dt}
$$

**Conditions:**
*   $\frac{dx}{dt} \neq 0$ for $\frac{dy}{dx}$ to be defined.
*   If $\frac{dx}{dt} = 0$ and $\frac{dy}{dt} \neq 0$, the tangent line is vertical.
*   If $\frac{dx}{dt} = 0$ and $\frac{dy}{dt} = 0$, the derivative is indeterminate, suggesting a cusp or a point where the curve changes direction (L'Hôpital's Rule might be applicable for finding the limit of the slope).

**Example:**
Given $x = t^2$ and $y = \sin(t)$.
$\frac{dx}{dt} = 2t$
$\frac{dy}{dt} = \cos(t)$
Therefore, $\frac{dy}{dx} = \frac{\cos(t)}{2t}$.

## 2. The Second Derivative: $\frac{d^2y}{dx^2}$

The second derivative, $\frac{d^2y}{dx^2}$, tells us about the concavity of the parametric curve. It is the derivative of the first derivative with respect to $x$. This requires another application of the chain rule. We define $Y = \frac{dy}{dx}$, and then we are looking for $\frac{dY}{dx}$.

$$
\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{d(dy/dx)/dt}{dx/dt}
$$

**Important Note:** Do NOT simply take the derivative of $\frac{dy}{dx}$ with respect to $t$ and then divide by $\frac{dx}{dt}$ *again*. You must differentiate the entire expression for $\frac{dy}{dx}$ *with respect to $t$* first.

**Example (continuing from above):**
Given $\frac{dy}{dx} = \frac{\cos(t)}{2t}$.
Let $Y = \frac{\cos(t)}{2t}$.
We need $\frac{dY}{dt}$ using the quotient rule:
$\frac{dY}{dt} = \frac{-\sin(t)(2t) - \cos(t)(2)}{(2t)^2} = \frac{-2t\sin(t) - 2\cos(t)}{4t^2} = \frac{-t\sin(t) - \cos(t)}{2t^2}$
Now, combine with $\frac{dx}{dt}$:
$\frac{d^2y}{dx^2} = \frac{(-t\sin(t) - \cos(t))/(2t^2)}{2t} = \frac{-t\sin(t) - \cos(t)}{4t^3}$

## 3. Interpreting Derivatives

The derivatives derived from parametric equations are essential for understanding the motion and geometry of the curve:

*   **Tangent Lines:** The slope of the tangent line at a point $(x(t_0), y(t_0))$ is $\frac{dy}{dx}\bigg|_{t=t_0}$.
*   **Horizontal Tangent:** Occurs when $\frac{dy}{dt} = 0$ and $\frac{dx}{dt} \neq 0$.
*   **Vertical Tangent:** Occurs when $\frac{dx}{dt} = 0$ and $\frac{dy}{dt} \neq 0$.
*   **Concavity:**
    *   $\frac{d^2y}{dx^2} > 0$: Curve is concave up.
    *   $\frac{d^2y}{dx^2} < 0$: Curve is concave down.
*   **Speed and Motion:** While $\frac{dy}{dx}$ gives the slope, it does not directly represent the speed of a particle. For speed, we consider [[Calculus and Vector-Valued Functions]] and the magnitude of the velocity vector:
    $$
    \text{Speed} = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}
    $$
    This is also related to [[Arc Lengths of Parametric Equations]].

## Summary Table

| Derivative              | Formula                                   | Interpretation                      |
| :---------------------- | :---------------------------------------- | :---------------------------------- |
| First Derivative        | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$    | Slope of the tangent line           |
| Second Derivative       | $\frac{d^2y}{dx^2} = \frac{d(dy/dx)/dt}{dx/dt}$ | Concavity of the curve              |

For further applications of these derivatives in motion, refer to [[Motion Problems with Parametric and Vector-Valued Functions]].