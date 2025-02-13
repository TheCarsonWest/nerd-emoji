# [[Exam Prep Schedule]]
# [[Techniques of Integration]]

These notes cover various methods for evaluating indefinite and definite [[integrals]].

**I. Basic Integrals:**

*   [[Power Rule]]: $\int x^n dx = \frac{x^{n+[[1}}{n+[[1} + C$,  $n \neq -[[1$
*   Exponential Rule: $\int e^x dx = e^x + C$
*   Logarithmic Rule: $\int \frac{[[1}{x} dx = \ln|x| + C$
*   Trigonometric Integrals:  [[Trigonometric Integrals]] (This will be a separate note)


**II. Advanced Techniques:**

*   **Substitution (u-substitution):**  Let $u = g(x)$, then $du = g'(x)dx$.  $\int f(g(x))g'(x)dx = \int f(u)du$.  Example: $\int 2x \cos(x^2) dx$. Let $u = x^2$, $du = 2x dx$. Then $\int \cos(u) du = \sin(u) + C = \sin(x^2) + C$.

*   **Integration by Parts:** $\int u dv = uv - \int v du$.  Choosing appropriate $u$ and $dv$ is crucial.  [[Choosing u and dv]] (This will be a separate note focusing on strategies for selecting u and dv)


*   **Trigonometric Substitution:** Used for [[integrals]] involving $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$.  This involves substituting $x$ with a trigonometric function. [[Trigonometric Substitution Examples]] (This will be a separate note)

*   **Partial Fraction Decomposition:** Used for [[integrals]] of rational functions (where the degree of the numerator is less than the degree of the denominator).  The rational function is decomposed into simpler fractions that are easier to integrate. [[Partial Fraction Decomposition Techniques]] (This will be a separate note)


*   **Improper Integrals:** Integrals with infinite limits or discontinuous integrands. [[Improper Integrals Types and Solutions]] (This will be a separate note).  We need to consider:
    *   Type [[1: $\int_a^{\infty} f(x) dx = \lim_{t \to \infty} \int_a^t f(x) dx$
    *   Type 2: $\int_{-\infty}^b f(x) dx = \lim_{t \to -\infty} \int_t^b f(x) dx$
    *   Type 3: $\int_{-\infty}^{\infty} f(x) dx = \int_{-\infty}^c f(x) dx + \int_c^{\infty} f(x) dx$  where $c$ is any real number.


**III. Tables of Integrals:**

While we aim to master the techniques above, it's useful to have a table of [[integrals]] for quick reference.  Many textbooks and online resources provide comprehensive tables. $ \int \frac{[[1}{x^2 + a^2} dx = \frac{[[1}{a} \arctan(\frac{x}{a}) + C$ is a common example.


**IV. Numerical Integration:**

For [[integrals]] that cannot be solved analytically, numerical methods (like the [[Trapezoidal Rule]] or Simpson's Rule) can approximate the value of the definite integral. [[Numerical Integration Methods]] (This will be a separate note)

**V. Applications:**

*   Calculating areas between curves.
*   Finding volumes of solids of revolution.
*   Solving differential equations.
*   Many applications in physics and engineering.  [[Applications in Physics and Engineering]] (This will be a separate note)


This is a preliminary outline; each section will be expanded in separate notes.
