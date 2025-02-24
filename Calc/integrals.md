# [[Calc home]]
Integrals are the cornerstone of integral calculus, essentially the inverse operation of differentiation.  They allow us to calculate areas under curves, volumes of solids, and much more.  This rundown covers the key concepts for Calculus AB.

# 1. Indefinite Integrals

The indefinite integral, denoted by $\int f(x) \, dx$, represents the *family* of functions whose [[derivative]] is $f(x)$.  The "$dx$" indicates that we are integrating with respect to the variable $x$.  The [[constant of integration]], $C$, is crucial because the [[derivative]] of a constant is zero.

# $$\int f(x) \, dx = F(x) + C, \text{ where } F'(x) = f(x)$$

**Example:** $$\int 2x \, dx = x^2 + C$$

# [[Constant of Integration]]
# 2. Definite Integrals

The definite integral, denoted by $\int_a^b f(x) \, dx$, represents the *signed* area between the curve $y = f(x)$ and the x-axis, from $x = a$ to $x = b$.  The area above the x-axis is positive, and the area below is negative.

# [[Riemann Sums]]

The definite integral can be approximated using [[Riemann Sums]] (left, right, midpoint).  These sums divide the area into rectangles and sum their areas.  As the number of rectangles increases, the approximation becomes more accurate.

[[Fundamental Theorem of Calculus]]

The [[Fundamental Theorem of Calculus]] connects differentiation and integration.  It states:

* **Part 1:** If $F(x) = \int_a^x f(t) \, dt$, then $F'(x) = f(x)$.
* **Part 2:** $\int_a^b f(x) \, dx = F(b) - F(a)$, where $F(x)$ is an antiderivative of $f(x)$.

This theorem provides a powerful method for evaluating definite [[integrals]].


# 3. [[Techniques of Integration]]

## 4. Applications of Integrals

Integrals have numerous applications in Calculus AB, including:

* **Area between curves:**  The area between two curves $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is given by 
### $$\int_a^b |f(x) - g(x)| \, dx$$

```desmos-graph
y = x^2
y = x
```

* **Average value of a function:** The average value of $f(x)$ on the interval $[a, b]]$ is 
### $$\frac{1}{b-a} \int_a^b f(x) \, dx$$
This rundown provides a concise overview of [[integrals]] in Calculus AB.  Remember to practice extensively to master these concepts and techniques.
