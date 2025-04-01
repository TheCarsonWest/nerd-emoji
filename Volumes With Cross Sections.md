# [[Calc home]]
# Volumes With Cross Sections: AP Calculus AB Rundown

This topic focuses on finding the volume of a 3D solid based on knowing the area of its cross-sections perpendicular to a given axis.

## 1. General Principle

The fundamental idea is to slice the solid into infinitesimally thin cross-sections, calculate the area of each cross-section, and then integrate the area function over the interval of the solid.

$$V = \int_{a}^{b} A(x) \, dx \quad \text{or} \quad V = \int_{c}^{d} A(y) \, dy$$

Where:
*   $V$ is the volume of the solid.
*   $A(x)$ or $A(y)$ is the area of the cross-section at position $x$ or $y$, respectively.
*   $[a, b]$ or $[c, d]$ are the intervals on the x-axis or y-axis, respectively, over which the solid extends.

## 2. Key Steps to Solve Volume with Cross Sections Problems

1.  **Sketch the Base:** Carefully sketch the region that forms the base of the solid. This will help you determine the limits of integration and the relationship between $x$ and $y$.
2.  **Determine the Axis of Integration:** Decide whether to integrate with respect to $x$ or $y$ based on the orientation of the cross-sections. If the cross-sections are perpendicular to the x-axis, integrate with respect to $x$. If they are perpendicular to the y-axis, integrate with respect to $y$.
3.  **Find the Area Function A(x) or A(y):** This is the most crucial step.  You need to express the area of the cross-section as a function of $x$ or $y$.  The specific formula for $A(x)$ or $A(y)$ depends on the shape of the cross-section. [[Area Formulas for Common Shapes]]
4.  **Determine the Limits of Integration:** Find the values of $x$ (or $y$) that define the beginning and end of the solid along the chosen axis.
5.  **Integrate:** Evaluate the definite integral of the area function over the limits of integration to find the volume.

## 3. Common Cross-Section Shapes and Their Area Formulas

Here are some common shapes you might encounter, along with their area formulas:

*   **Squares:** If the side length of the square is $s$, then $A = s^2$.
*   **Rectangles:** If the length is $l$ and the width is $w$, then $A = lw$. Usually one dimension is constant and the other is defined by the region.
*   **Semicircles:** If the diameter is $d$, then the radius is $r = d/2$, and $A = \frac{1}{2}\pi r^2 = \frac{1}{2}\pi (\frac{d}{2})^2 = \frac{\pi}{8}d^2$.
*   **Equilateral Triangles:** If the side length is $s$, then $A = \frac{\sqrt{3}}{4}s^2$.
*   **Isosceles Right Triangles:**  If the leg length is $l$, then $A = \frac{1}{2}l^2$.
*   **Right Triangles:** if the base is $b$ and height is $h$, then $A = \frac{1}{2}bh$

In all these cases, the side length, diameter, or base/height will be expressed in terms of $x$ or $y$ based on the region defining the base of the solid.

## 4. Examples

**Example 1:**

The base of a solid is the region bounded by $y = x^2$ and $y = 4$.  Cross-sections perpendicular to the x-axis are squares. Find the volume.

1.  **Sketch:** Sketch the parabola $y = x^2$ and the line $y = 4$.
2.  **Axis of Integration:** Since the cross-sections are perpendicular to the x-axis, we integrate with respect to $x$.
3.  **Area Function:** The side length of the square is the distance between the two curves: $s = 4 - x^2$. Therefore, the area of the square is $A(x) = (4 - x^2)^2$.
4.  **Limits of Integration:** Find the points of intersection: $x^2 = 4$, so $x = \pm 2$.  The limits of integration are $-2$ and $2$.
5.  **Integrate:**

    $$V = \int_{-2}^{2} (4 - x^2)^2 \, dx = \int_{-2}^{2} (16 - 8x^2 + x^4) \, dx$$

    $$V = \left[16x - \frac{8}{3}x^3 + \frac{1}{5}x^5\right]_{-2}^{2} = 2\left(32 - \frac{64}{3} + \frac{32}{5}\right) = \frac{512}{15}$$

