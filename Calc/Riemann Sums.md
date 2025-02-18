# [[Calc home]]
Riemann sums are used to approximate the definite integral of a function, which represents the area under the curve.  They provide a foundational understanding of integration before moving on to more sophisticated techniques.

## Types of [[Riemann Sums]] 
There are three main types of Riemann sums, each differing in how the rectangle heights are determined:

1. Left Riemann Sum: The height of each rectangle is determined by the function's value at the *left endpoint* of the subinterval.

2. Right Riemann Sum: The height of each rectangle is determined by the function's value at the *right endpoint* of the subinterval.

3. Midpoint Riemann Sum: The height of each rectangle is determined by the function's value at the *midpoint* of the subinterval.


##  Calculating [[Riemann Sums]] 
Let's consider a function $f(x)$ on the interval $[a, b]]$. We divide this interval into $n$ subintervals of equal width, $\Delta x = \frac{b-a}{n}$.  The $i$-th subinterval is $[x_{i-1}, x_i]]$, where $x_i = a + i\Delta x$.

The general formula for a Riemann sum is:
# $$ \sum_{i=1}^{n} f(x_i^*) \Delta x $$
where $x_i^*$ is a point in the $i$-th subinterval.  The choice of $x_i^*$ determines the type of Riemann sum:
* Left Riemann Sum: 
### $$x_i^* = x_{i-1} = a + (i-1)\Delta x$$
* Right Riemann Sum: 
### $$x_i^* = x_i = a + i\Delta x$$
* Midpoint Riemann Sum: 
### $$x_i^* = \frac{x_{i-1} + x_i}{2} = a + (i - \frac{1}{2})\Delta x$$
### Example: Approximate the area under the curve $f(x) = x^2$ from $x=0$ to $x=2$ using a right Riemann sum with $n=4$ subintervals.

$\Delta x = \frac{2-0}{4} = 0.5$

The subintervals are $[0, 0.5$, $[0.5, 1$, $1, 1.5$, $1.5, 2$.

The right Riemann sum is:
$R_4 = f(0.5)(0.5) + f(1)(0.5) + f(1.5)(0.5) + f(2)(0.5) = 0.5(0.5^2 + 1^2 + 1.5^2 + 2^2) = 0.5(0.25 + 1 + 2.25 + 4) = 3.75$


```desmos-graph
y = x^2
y = 0
x = 0
x = 2
```

## [[Error Analysis]]

The error in a Riemann sum approximation is the difference between the actual value of the definite integral and the approximation. The error decreases as the number of subintervals ($n$) increases.  Generally, the error is proportional to $\frac{1}{n}$.  More sophisticated error bounds exist, but are beyond the scope of AB calculus.


##  Relationship to Definite [[integrals]]

As the number of subintervals ($n$) approaches infinity, the Riemann sum converges to the definite integral:

$\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x = \int_a^b f(x) dx$

This is the fundamental theorem of calculus, connecting the concept of Riemann sums to the process of integration.


## [[Applications of Riemann Sums]]

Riemann sums are not just theoretical tools; they have practical applications in various fields, including:

* Approximating areas of irregularly shaped regions:  When dealing with complex shapes where standard geometric formulas are not applicable.
* Calculating work done by a variable force:  The force may change over the distance it acts upon.
* Estimating the total value of a continuously changing quantity:  Such as the accumulation of rainfall over time or the growth of a population.


This rundown provides a comprehensive overview of Riemann sums for Calculus AB. Remember to practice various examples to solidify your understanding.
