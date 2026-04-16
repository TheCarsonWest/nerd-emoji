
# [[AP Physics C Home]]
# Topic 10.3: Electric Fields

Electric fields are a fundamental concept in electromagnetism, describing the influence a charged object exerts on the space around it. An electric field exists at a point if a test charge placed at that point experiences an electric force.

## Definition and Fundamental Equation

The electric field $\vec{E}$ at a specific point in space is defined as the force per unit charge experienced by a small positive test charge $q_0$ placed at that point.

$$ \vec{E} = \frac{\vec{F}}{q_0} $$

The units for the electric field are Newtons per Coulomb ($\text{N/C}$) or Volts per meter ($\text{V/m}$). Since force is a vector quantity, the electric field is also a vector, possessing both magnitude and direction. By convention, the direction of the electric field vector is the direction in which a *positive* test charge would accelerate if placed in the field.

## Electric Fields from Point Charges

For a single point charge $Q$, the electric field at a distance $r$ can be derived from [[Electric Charge and Electric Force]] (Coulomb's Law).

$$ E = k \frac{|Q|}{r^2} $$

Where:
*   $k$ is Coulomb's constant ($\approx 8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$).
*   $Q$ is the source charge.
*   $r$ is the distance from the source charge.

## Superposition Principle

When multiple charges are present, the total electric field at any point is the vector sum of the individual electric fields produced by each charge. This is known as the **Principle of Superposition**.

$$ \vec{E}_{total} = \vec{E}_1 + \vec{E}_2 + \dots + \vec{E}_n = \sum_{i=1}^{n} \vec{E}_i $$

## Electric Field Lines

Electric field lines (or lines of force) are a visual tool used to map the electric field. They represent the direction of the field vector at any point.

| Property | Rule |
| :--- | :--- |
| **Direction** | Lines originate on positive charges and terminate on negative charges. |
| **Density** | The density of the lines is proportional to the magnitude of the field. |
| **Crossing** | Field lines can never intersect, as the field must have a unique direction at every point. |
| **Start/End** | The number of lines leaving a positive charge or entering a negative charge is proportional to the magnitude of the charge. |

## Continuous Charge Distributions

When dealing with objects rather than point charges, we treat the charge as distributed over a line, surface, or volume. Calculating the field requires [[Calculus-Based Electric Fields]], where we integrate over the charge distribution:

$$ \vec{E} = \int \frac{k \, dq}{r^2} \hat{r} $$

This approach is necessary for shapes like charged rods, rings, or disks, where the simple point-charge formula does not apply directly.

## Relationship to Potential
The electric field is not only related to force but also to potential. It can be viewed as the negative gradient of the [[Electric Potential]]. In one dimension, this is expressed as:

$$ E_x = -\frac{dV}{dx} $$

This relationship emphasizes that the electric field points in the direction of the steepest decrease in electric potential.