# [[Calc home]]
# [[Unit 7 Applications of Integrals]]
# Volumes of Revolutions: AP Calculus AB Rundown

This document provides a concise overview of volumes of revolution, a key topic in AP Calculus AB. We will cover the main methods: the Disk Method, the Washer Method, and briefly touch on the Shell Method (though it's less common on the AB exam).

## 1. Introduction

Volumes of revolution involve calculating the volume of a 3D solid formed by rotating a 2D region around a line (the axis of revolution).  The key is to slice the solid into infinitesimally thin shapes (disks or washers) and integrate their volumes.

## 2. The Disk Method

The Disk Method is used when the region being revolved is *adjacent* to the axis of revolution. This means the cross-sections perpendicular to the axis of revolution are solid disks.

**Procedure:**

1.  **Sketch the region:** Draw the region you're revolving and the axis of revolution.
2.  **Identify the radius:** Determine the radius, *r*, of a representative disk.  The radius will be a function of either *x* or *y*, depending on the axis of revolution. [[Radius Identification]]
3.  **Set up the integral:** The volume is found by integrating the area of the disk, $$A = \pi r^2$$, along the axis of revolution.

**Formulas:**

*   **Revolution about the x-axis:**
    $$V = \pi \int_a^b [f(x)]^2 \, dx$$
    where *f(x)* is the function defining the curve, and *a* and *b* are the limits of integration along the x-axis.

*   **Revolution about the y-axis:**
    $$V = \pi \int_c^d [g(y)]^2 \, dy$$
    where *g(y)* is the function defining the curve (solved for *x* in terms of *y*), and *c* and *d* are the limits of integration along the y-axis.

**Example:**

Find the volume of the solid formed by revolving the region bounded by $$y = \sqrt{x}$$, $$x = 4$$, and $$y = 0$$ about the x-axis.

$$V = \pi \int_0^4 (\sqrt{x})^2 \, dx = \pi \int_0^4 x \, dx = \pi \left[ \frac{1}{2}x^2 \right]_0^4 = \pi \left( \frac{1}{2}(4)^2 - 0 \right) = 8\pi$$

## 3. The Washer Method

The Washer Method is used when the region being revolved is *not adjacent* to the axis of revolution. This creates a "hole" in the center of the solid, resulting in washer-shaped cross-sections.

**Procedure:**

1.  **Sketch the region:** Draw the region you're revolving and the axis of revolution.
2.  **Identify the outer and inner radii:** Determine the outer radius, *R*, and the inner radius, *r*, of a representative washer. Both radii will be functions of either *x* or *y*. [[Radii Identification]]
3.  **Set up the integral:** The volume is found by integrating the area of the washer, $$A = \pi (R^2 - r^2)$$, along the axis of revolution.

**Formulas:**

*   **Revolution about the x-axis:**
    $$V = \pi \int_a^b ([f(x)]^2 - [g(x)]^2) \, dx$$
    where *f(x)* is the outer function (further from the axis) and *g(x)* is the inner function (closer to the axis), and *a* and *b* are the limits of integration along the x-axis.

*   **Revolution about the y-axis:**
    $$V = \pi \int_c^d ([F(y)]^2 - [G(y)]^2) \, dy$$
    where *F(y)* is the outer function (further from the axis) and *G(y)* is the inner function (closer to the axis), and *c* and *d* are the limits of integration along the y-axis.

**Example:**

Find the volume of the solid formed by revolving the region bounded by $$y = x^2$$ and $$y = x$$ about the x-axis.

First, find the intersection points: $$x^2 = x  \Rightarrow x^2 - x = 0 \Rightarrow x(x-1) = 0 \Rightarrow x = 0, 1$$.

$$V = \pi \int_0^1 (x^2 - (x^2)^2) \, dx = \pi \int_0^1 (x^2 - x^4) \, dx = \pi \left[ \frac{1}{3}x^3 - \frac{1}{5}x^5 \right]_0^1 = \pi \left( \frac{1}{3} - \frac{1}{5} \right) = \frac{2\pi}{15}$$

