# [[integrals]]

The constant of integration is a crucial concept in integral calculus.  It arises because the derivative of a constant is always zero.  This means that when we find an antiderivative (also called an indefinite integral), we can't uniquely determine the original function.  There's always a family of functions that could have yielded the same derivative.

## Understanding the Problem

Let's consider a simple example.  The derivative of $f(x) = x^2 + 5$ is $f'(x) = 2x$.  Similarly, the derivative of $g(x) = x^2 + 10$ is also $g'(x) = 2x$.  In fact, the derivative of $h(x) = x^2 + C$, where $C$ is any constant, is $h'(x) = 2x$.

This illustrates that many functions can share the same derivative.  When we find the antiderivative of $2x$, we are essentially trying to reverse the differentiation process.  Since we lose information about the constant during differentiation, we need to account for this lost information when we integrate.

## The [[Constant of Integration]]: $C$

To represent this ambiguity, we introduce the constant of integration, denoted by $C$.  When we find the indefinite integral of a function, we always add this constant.

For example, the indefinite integral of $2x$ is given by:

$\int 2x \, dx = x^2 + C$

This expression represents the entire family of functions whose derivative is $2x$.  Each value of $C$ yields a different function in this family.

[[integrals]]

## Determining the [[Constant of Integration]]

The constant of integration, $C$, is an arbitrary constant.  Its value can only be determined if we have additional information about the original function. This additional information usually comes in the form of an initial condition, which specifies the value of the function at a particular point.

For example, if we know that the function passes through the point $([[1, 6)$, and we have found the antiderivative to be $x^2 + C$, we can solve for $C$:

$6 = ([[1)^2 + C$
$C = 5$

So, the specific function is $f(x) = x^2 + 5$.


## Visualizing the Family of Functions

```desmos-graph
y = x^2 + [[1
y = x^2 + 2
y = x^2 + 3
y = x^2
y = x^2 -[[1
y = x^2 -2
```

The graph above shows several functions of the family $y = x^2 + C$ for different values of $C$.  They are all parallel curves, differing only by a vertical shift.


[[Initial Value Problems]]

## Importance of the [[Constant of Integration]]

While seemingly minor, forgetting the constant of integration can lead to significant errors in solving differential equations and other applications of calculus.  It's a crucial detail that ensures we capture the complete solution and not just a specific case.  Always remember to include the $+C$ when finding indefinite [[integrals]].




# [[Constant of Integration]]
## 2. Definite Integrals

The definite integral, denoted by $\int_a^b f(x) \, dx$, represents the *signed* area between the curve $y = f(x)$ and the x-axis, from $x = a$ to $x = b$.  The area above the x-axis is positive, and the area below is negative.

## [[Riemann Sums]]

The definite integral can be approximated using [[Riemann Sums]] (left, right, midpoint).  These sums divide the area into rectangles and sum their areas.  As the number of rectangles increases, the approximation becomes more accurate.

[[Fundamental Theorem of Calculus]]

The [[Fundamental Theorem of Calculus]] connects differentiation and integration.  It states:

* **Part [[1:** If $F(x) = \int_a^x f(t) \, dt$, then $F'(x) = f(x)$.
* **Part 2:** $\int_a^b f(x) \, dx = F(b) - F(a)$, where $F(x)$ is an antiderivative of $f(x)$.

This theorem provides a powerful method for evaluating definite [[integrals]].


## 3. [[Techniques of Integration]] 
Calculus AB primarily focuses on these basic integration techniques:

* **[[Power Rule]]:** $\int x^n \, dx = \frac{x^{n+[[1}}{n+[[1} + C$  (for $n \neq -[[1$)
* **Constant Multiple Rule:** $\int kf(x) \, dx = k \int f(x) \, dx$
* **Sum/Difference Rule:** $\int [f(x) \pm g(x)]] \, dx = \int f(x) \, dx \pm \int g(x) \, dx$
* **Integration by Substitution (u-substitution):** A technique for simplifying [[integrals]] by substituting a new variable, $u$, for a part of the integrand.


**Example (u-substitution):**

To evaluate $\int 2x(x^2 + [[1)^3 \, dx$, let $u = x^2 + [[1$, so $du = 2x \, dx$.  Then the integral becomes $\int u^3 \, du = \frac{u^4}{4} + C = \frac{(x^2 + [[1)^4}{4} + C$.


## 4. Applications of Integrals

Integrals have numerous applications in Calculus AB, including:

* **Area between curves:**  The area between two curves $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is given by 
### $$\int_a^b |f(x) - g(x)| \, dx$$

```desmos-graph
y = x^2
y = x
```

* **Average value of a function:** The average value of $f(x)$ on the interval $[a, b]]$ is 
### $$\frac{[[1}{b-a} \int_a^b f(x) \, dx$$
This rundown provides a concise overview of [[integrals]] in Calculus AB.  Remember to practice extensively to master these concepts and techniques.

# [[integrals]]