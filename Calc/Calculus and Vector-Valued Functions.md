
# [[Calc Home]]
# AP Calculus BC Notes: 9.4 Calculus and Vector-Valued Functions

Vector-valued functions are crucial in describing motion and curves in 2D and 3D space. They assign a vector to each real number (parameter, often time $t$). Calculus extend;s naturally to these functions, allowing us to analyze properties like limits, continuity, rates of change (velocity, acceleration), and displacement.

## Defining a Vector-Valued Function

A vector-valued function $\mathbf{r}(t)$ is typically defined by its component functions:

For 2D: $$\mathbf{r}(t) = \langle x(t), y(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j}$$
For 3D: $$\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$$

Where $x(t)$, $y(t)$, and $z(t)$ are real-valued functions of the parameter $t$. The domain of $\mathbf{r}(t)$ is the intersection of the domains of its component functions.

## Limits of Vector-Valued Functions

The limit of a vector-valued function is found by taking the limit of each component function separately, provided each limit exists.

If $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$, then:
$$ \lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} x(t), \lim_{t \to a} y(t), \lim_{t \to a} z(t) \right\rangle $$
A vector-valued function $\mathbf{r}(t)$ is **continuous** at $t=a$ if $\lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)$, which implies that all component functions are continuous at $t=a$.

## Derivatives of Vector-Valued Functions

The derivative of a vector-valued function is found by differentiating each component function with respect to $t$. This derivative, $\mathbf{r}'(t)$, represents a tangent vector to the curve at $t$.

If $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$, then:
$$ \mathbf{r}'(t) = \frac{d}{dt}\mathbf{r}(t) = \left\langle x'(t), y'(t), z'(t) \right\rangle $$
The derivative $\mathbf{r}'(t)$ gives the instantaneous direction and magnitude of change along the curve. For motion problems, this is the [[Motion Problems with Parametric and Vector-Valued Functions#Velocity and Acceleration|velocity vector]]. The second derivative, $\mathbf{r}''(t)$, gives the [[Motion Problems with Parametric and Vector-Valued Functions#Velocity and Acceleration|acceleration vector]].

### Differentiation Rules

Differentiation rules for vector-valued functions are similar to those for real-valued functions, extended to vectors. Let $\mathbf{u}(t)$ and $\mathbf{v}(t)$ be differentiable vector functions, $c$ a scalar, and $f(t)$ a differentiable scalar function.

| Rule                     | Formula                                                                               |
| :----------------------- | :------------------------------------------------------------------------------------ |
| Scalar Multiple          | $\frac{d}{dt}[c\mathbf{u}(t)] = c\mathbf{u}'(t)$                                      |
| Sum/Difference           | $\frac{d}{dt}[\mathbf{u}(t) \pm \mathbf{v}(t)] = \mathbf{u}'(t) \pm \mathbf{v}'(t)$   |
| Scalar Function Product  | $\frac{d}{dt}[f(t)\mathbf{u}(t)] = f'(t)\mathbf{u}(t) + f(t)\mathbf{u}'(t)$          |
| Dot Product              | $\frac{d}{dt}[\mathbf{u}(t) \cdot \mathbf{v}(t)] = \mathbf{u}'(t) \cdot \mathbf{v}(t) + \mathbf{u}(t) \cdot \mathbf{v}'(t)$ |
| Cross Product (3D only)  | $\frac{d}{dt}[\mathbf{u}(t) \times \mathbf{v}(t)] = \mathbf{u}'(t) \times \mathbf{v}(t) + \mathbf{u}(t) \times \mathbf{v}'(t)$ |
| Chain Rule               | $\frac{d}{dt}[\mathbf{u}(f(t))] = \mathbf{u}'(f(t))f'(t)$                             |

**Key Property**: If $|\mathbf{r}(t)| = c$ (constant magnitude), then $\mathbf{r}(t) \cdot \mathbf{r}'(t) = 0$. This means $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal. This is particularly useful for circular motion.

## Integrals of Vector-Valued Functions

Integration of a vector-valued function is also performed component by component. This applies to both indefinite and definite integrals.

If $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$, then:
### Indefinite Integral
$$ \int \mathbf{r}(t) \,dt = \left\langle \int x(t) \,dt, \int y(t) \,dt, \int z(t) \,dt \right\rangle + \mathbf{C} $$
Where $\mathbf{C} = \langle C_1, C_2, C_3 \rangle$ is a constant vector of integration.

### Definite Integral
$$ \int_a^b \mathbf{r}(t) \,dt = \left\langle \int_a^b x(t) \,dt, \int_a^b y(t) \,dt, \int_a^b z(t) \,dt \right\rangle $$
The definite integral of a velocity vector over an interval gives the [[Motion Problems with Parametric and Vector-Valued Functions#Displacement and Total Distance|displacement vector]] during that interval.

## Arc Length of a Vector-Valued Curve

The [[Arc Lengths of Parametric Equations|arc length]] $L$ of a smooth curve defined by $\mathbf{r}(t)$ from $t=a$ to $t=b$ is given by:
$$ L = \int_a^b |\mathbf{r}'(t)| \,dt = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} \,dt $$
For a 2D curve, simply omit the $z$ component. This is the total distance traveled by an object whose position is given by $\mathbf{r}(t)$.