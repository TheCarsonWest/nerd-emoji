### [[Local Linear Approximation]] 
The concept of [[Local Linearity]] allows us to approximate the value of a function near a point using the tangent line at that point. This is called the **local linear approximation**.

**Idea:**

If we zoom in sufficiently close to a point on the graph of a function, the graph starts to look more and more like a straight line. This straight line is the tangent line.

**Formula:**

The local linear approximation of $f(x)$ at $x=a$ is given by:

$$f(x) \approx f(a) + f'(a)(x-a)$$

**Example:**

Let's approximate the value of $\sqrt{4.1}$ using the local linear approximation of $f(x) = \sqrt{x}$ at $x=4$.

We have $f'(x) = \frac{1}{2\sqrt{x}}$, so $f'(4) = \frac{1}{4}$. 

Using the local linear approximation, we get:

$$\sqrt{4.1} \approx f(4) + f'(4)(4.1-4) = 2 + \frac{1}{4}(0.1) = 2.025$$

This approximation is quite accurate, as the actual value of $\sqrt{4.1}$ is approximately 2.0248.

# [[Local Linearity]]