
# [[AP Physics C Home]]
# AP Physics C: Topic 1.1 - Scalars and Vectors

## 1. Introduction to Physical Quantities

In physics, understanding the nature of physical quantities is fundamental. These quantities can generally be categorized into two types: scalars and vectors, distinguished by whether they possess direction in addition to magnitude.

## 2. Scalars

A **scalar** is a physical quantity that is completely described by its magnitude (a numerical value) alone. Scalars do not have an associated direction.

*   **Characteristics:**
    *   Possess magnitude only.
    *   Follow standard arithmetic rules for addition, subtraction, multiplication, and division.
*   **Examples:**
    *   **Mass**: The amount of matter in an object (e.g., 5 kg).
    *   **Time**: The duration of an event (e.g., 10 seconds).
    *   **Temperature**: The degree of hotness or coldness (e.g., 25 °C).
    *   **Distance**: The total path length traveled (e.g., 100 meters).
    *   **Speed**: The rate at which an object covers distance (e.g., 60 km/h).
    *   **Energy**: The capacity to do work (e.g., 100 Joules).

## 3. Vectors

A **vector** is a physical quantity that is completely described by both its magnitude and its direction. Vectors are crucial for describing motion, forces, and fields in physics.

*   **Characteristics:**
    *   Possess both magnitude and direction.
    *   Require special rules for mathematical operations (vector algebra).
*   **Examples:**
    *   **Displacement**: The change in position from an initial point to a final point, including direction (e.g., 5 km East). (See: [[Displacement, Velocity, and Acceleration]])
    *   **Velocity**: The rate of change of displacement, including direction (e.g., 60 km/h North).
    *   **Acceleration**: The rate of change of velocity, including direction (e.g., $9.8 \text{ m/s}^2$ downward).
    *   **Force**: A push or pull with a specific direction (e.g., 10 N upwards). (See: [[Forces and Free-Body Diagrams]])
    *   **Momentum**: The product of mass and velocity (e.g., $50 \text{ kg} \cdot \text{m/s}$ West). (See: [[Linear Momentum]])

## 4. Vector Representation and Notation

Vectors can be represented graphically or analytically.

*   **Graphical Representation**: An arrow is used, where:
    *   The length of the arrow represents the magnitude of the vector (scaled appropriately).
    *   The direction the arrow points represents the direction of the vector.
*   **Vector Notation**:
    *   Often denoted by a boldface letter (e.g., **A**) or a letter with an arrow above it (e.g., $\vec{A}$).
    *   The magnitude of a vector $\vec{A}$ is denoted by $|\vec{A}|$ or simply $A$.

## 5. Vector Components

Any vector in a 2D or 3D coordinate system can be broken down into its perpendicular components along the axes. For a vector $\vec{A}$ in 2D, its components are $A_x$ and $A_y$.

*   If $\theta$ is the angle the vector makes with the positive x-axis:
    $$A_x = A \cos \theta$$
    $$A_y = A \sin \theta$$
*   The magnitude of the vector can be found using the Pythagorean theorem:
    $$A = \sqrt{A_x^2 + A_y^2}$$
*   The direction (angle) of the vector can be found using the inverse tangent function:
    $$\theta = \arctan\left(\frac{A_y}{A_x}\right)$$
    (Care must be taken to ensure the angle is in the correct quadrant based on the signs of $A_x$ and $A_y$).

## 6. Vector Operations

### 6.1. Vector Addition and Subtraction

*   **Graphical Method (Tip-to-Tail)**: To add vectors $\vec{A}$ and $\vec{B}$, place the tail of $\vec{B}$ at the tip of $\vec{A}$. The resultant vector $\vec{R} = \vec{A} + \vec{B}$ is drawn from the tail of $\vec{A}$ to the tip of $\vec{B}$. Subtraction $\vec{A} - \vec{B}$ is equivalent to $\vec{A} + (-\vec{B})$, where $-\vec{B}$ has the same magnitude as $\vec{B}$ but points in the opposite direction.
*   **Analytical (Component) Method**: The most common and precise method. To add (or subtract) vectors, add (or subtract) their corresponding components.
    If $\vec{A} = \langle A_x, A_y \rangle$ and $\vec{B} = \langle B_x, B_y \rangle$:
    $$\vec{A} + \vec{B} = \langle A_x + B_x, A_y + B_y \rangle$$
    $$\vec{A} - \vec{B} = \langle A_x - B_x, A_y - B_y \rangle$$

### 6.2. Scalar Multiplication of a Vector

Multiplying a vector $\vec{A}$ by a scalar $c$ changes the magnitude of the vector by a factor of $|c|$.

*   If $c$ is positive, the direction of the vector remains the same.
*   If $c$ is negative, the direction of the vector is reversed.
    $$c\vec{A} = \langle cA_x, cA_y \rangle$$

Understanding scalars and vectors is foundational for nearly all topics in AP Physics C, from [[Motion in Two or Three Dimensions]] to [[Electric Fields]] and [[Magnetic Fields]].