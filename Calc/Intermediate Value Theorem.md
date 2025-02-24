[[Calc home]]
## [[Intermediate Value Theorem]] (IVT)

The [[Intermediate Value Theorem]] (IVT) is a fundamental theorem in calculus that helps us understand the behavior of continuous functions. It essentially states that if a continuous function takes on two values, then it must also take on all the values in between.

# Statement of the IVT

Let $f$ be a continuous function on the closed interval $[a,b]]$. If $f(a) \neq f(b)$, then for any value $k$ between $f(a)$ and $f(b)$, there exists a value $c$ in the interval $(a,b)$ such that $f(c) = k$.

### Visualizing the IVT

Imagine a continuous curve representing the function $f(x)$ on the interval $[a,b]]$.  The IVT says that if the curve starts at a point with a certain y-value and ends at a point with a different y-value, then it must pass through every y-value in between those two points.

**Example:** Consider the function $f(x) = x^2$ on the interval $[0,2$.  $f(0) = 0$ and $f(2) = 4$.  Since $f(x)$ is continuous, the IVT tells us that for any value $k$ between 0 and 4, there exists a value $c$ in the interval $(0,2)$ such that $f(c) = k$.

# [Desmos Exploration]](https://www.desmos.com/calculator/qrkkua0100)

### Key Points

* **[[Continuity]] is crucial:** The IVT only applies to continuous functions. If a function has a jump, hole, or vertical asymptote within the interval, the theorem may not hold.
* **Closed interval:** The IVT requires the interval to be closed, meaning it includes both endpoints.
* **Intermediate value:** The theorem guarantees the existence of a value $c$ where $f(c) = k$, but it doesn't tell us how to find that value.

### Applications of the IVT

The IVT has numerous applications in calculus and other areas of mathematics. Some common uses include:

* **Finding roots:** The IVT can be used to prove that a function has a root (a value where the function equals zero) within a given interval.
* **Solving equations:** The IVT can help us determine if an equation has a solution within a specific interval.
* **Proving inequalities:** The IVT can be used to prove inequalities by showing that a function takes on a specific value within an interval.

### Example: Proving the Existence of a Root

Let $f(x) = x^3 - 2x - 5$. We want to prove that $f(x)$ has a root in the interval $2,3$.

1. **[[Continuity]]:**  $f(x)$ is a polynomial function, which is continuous everywhere.
2. **Interval:** We are considering the closed interval $2,3$.
3. **Values at endpoints:**  $f(2) = 8 - 4 - 5 = -1$ and $f(3) = 27 - 6 - 5 = 16$.
4. **Intermediate value:** Since $f(2)$ is negative and $f(3)$ is positive, the IVT guarantees that there exists a value $c$ in the interval $(2,3)$ such that $f(c) = 0$. 

Therefore, we have proven that $f(x) = x^3 - 2x - 5$ has a root in the interval $2,3$.

**Note:** The IVT only proves the existence of a root, not its exact value. To find the root, we would need to use numerical methods like the Bisection Method.

