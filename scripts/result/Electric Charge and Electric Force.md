
# [[AP Physics C Home]]
# Topic 10.1: Electric Charge and Electric Force

## Introduction to Electric Charge
Electric charge is a fundamental property of matter that causes subatomic particles to experience a force when placed in an electromagnetic field. Charge is quantized, meaning it exists in discrete packets, with the elementary charge being that of a single electron or proton.

| Particle | Charge (C) | Mass (kg) |
| :--- | :--- | :--- |
| Proton | $+1.602 \times 10^{-19}$ | $1.673 \times 10^{-27}$ |
| Electron | $-1.602 \times 10^{-19}$ | $9.109 \times 10^{-31}$ |
| Neutron | $0$ | $1.675 \times 10^{-27}$ |

The net charge of an object is always an integer multiple of the elementary charge ($e$):
$$q = ne$$
where $n$ is an integer.

For a deeper dive into the fundamental principles of how these charges are manipulated, see [[Conservation of Electric Charge and Charging]].

## Coulomb’s Law
The electric force between two stationary point charges is described by **Coulomb’s Law**. This law states that the magnitude of the electrostatic force $F_e$ between two point charges $q_1$ and $q_2$ separated by a distance $r$ is directly proportional to the product of the magnitudes of charges and inversely proportional to the square of the distance between them.

The mathematical representation is:
$$F_e = k \frac{|q_1 q_2|}{r^2}$$

### Key Components
*   $F_e$: The magnitude of the electric force (measured in Newtons, N).
*   $k$: Coulomb’s constant, approximately $8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$.
*   $q_1, q_2$: The quantities of the two charges (measured in Coulombs, C).
*   $r$: The separation distance between the centers of the two charges (measured in meters, m).

### Vector Nature of Force
Coulomb's Law is a vector equation. Like forces are repulsive, and opposite charges are attractive. To determine the direction of the force vector $\vec{F}$, we often use unit vectors $\hat{r}$:
$$\vec{F}_{12} = k \frac{q_1 q_2}{r^2} \hat{r}$$

When dealing with multiple charges, you must use the **Principle of Superposition**. The net electric force on a specific charge is the vector sum of the individual forces exerted on it by all other charges:
$$\vec{F}_{\text{net}} = \sum \vec{F}_i = \vec{F}_1 + \vec{F}_2 + ... + \vec{F}_n$$

## Important Considerations
*   **Point Charges:** Coulomb's Law strictly applies only to point charges or spherical charge distributions where the charge is evenly distributed. 
*   **Inverse Square Law:** Note the similarity between Coulomb’s Law and Newton’s Law of Universal Gravitation. Both depend on the inverse square of the distance, though electric forces can be either attractive or repulsive, whereas gravity is strictly attractive.
*   **Action-Reaction:** By Newton’s Third Law, the force exerted by $q_1$ on $q_2$ is equal and opposite to the force exerted by $q_2$ on $q_1$.

For a more comprehensive understanding of how these forces generate vector fields in space, refer to [[Electric Fields]]. If you need to understand the relationship between electric force and potential energy, see [[Electric Potential Energy]].