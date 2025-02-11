## [[u-Substitution]] 
This is the most fundamental technique for simplifying [[integrals]].  It involves substituting a part of the integrand with a new variable, $u$, to make the integral easier to solve.

**Steps:**

[[1]]. Choose a suitable substitution, $u = g(x)$, where $g(x)$ is a part of the integrand.
[[2]]. Find $du = g'(x) dx$.
[[3]]. Rewrite the integral in terms of $u$ and $du$.
[[4]]. Integrate with respect to $u$.
[[5]]. Substitute back $x$ for $u$ in the result.

**Example:** $\int x(x^[[2]] + [[1]])^[[3]] dx$

Let $u = x^[[2]] + [[1]]$, then $du = 2x dx$, so $x dx = \frac{[[1]]}{[[2]]} du$.

The integral becomes: $\int u^[[3]] \frac{[[1]]}{[[2]]} du = \frac{[[1]]}{8}u^[[4]] + C = \frac{[[1]]}{8}(x^[[2]] + [[1]])^[[4]] + C$

# [[Techniques of Integration]]