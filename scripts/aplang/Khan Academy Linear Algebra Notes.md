# [[Useful Websites and Articles]]
# [[Khan Academy Linear Algebra Notes]]

**I. Vectors:**

* **Definition:** A quantity with both magnitude and direction.  Represented graphically as arrows.  Can be represented algebraically as ordered tuples (e.g., $\begin{bmatrix} 2 \\ 3 \end{bmatrix}$ in $\mathbb{R}^2$).

* **Vector Addition:**  Geometrically, the tail-to-head method. Algebraically, component-wise addition:  $\begin{bmatrix} a \\ b \end{bmatrix} + \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} a+c \\ b+d \end{bmatrix}$.

* **Scalar Multiplication:**  Scaling the magnitude of a vector by a scalar value. Algebraically, multiplying each component by the scalar: $k\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} ka \\ kb \end{bmatrix}$.

* **Linear Combinations:**  A sum of scalar multiples of vectors.  $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + ... + c_n\mathbf{v}_n$, where $c_i$ are scalars and $\mathbf{v}_i$ are vectors. [[Linear Combinations and Span]]


**II. Matrices:**

* **Definition:** A rectangular array of numbers.  Dimensions are given as $m \times n$ (rows x columns).

* **Matrix Addition:** Component-wise addition (only possible for matrices of the same dimensions).

* **Scalar Multiplication:** Multiplying each element of the matrix by the scalar.

* **Matrix Multiplication:** [[Matrix Multiplication]]


**III. Systems of Linear Equations:**

* **Row Reduction (Gaussian Elimination):**  A systematic method for solving systems of linear equations using elementary row operations (swap rows, multiply a row by a non-zero scalar, add a multiple of one row to another).  Goal is to obtain row-echelon form or reduced row-echelon form.

* **Augmented Matrix:** A matrix formed by combining the coefficient matrix and the constant vector of a system of linear equations.

* **Solutions:**  A system can have one unique solution, infinitely many solutions, or no solution. [[Systems of Linear Equations: Solutions]]


**IV. Vector Spaces:**

* **Definition:** A set of vectors that is closed under vector addition and scalar multiplication.  Must contain a zero vector.

* **Subspaces:**  A subset of a vector space that is itself a vector space.

* **Basis:** A set of linearly independent vectors that span the vector space.  [[Basis and Dimension]]


**V. Linear Transformations:**

* **Definition:** A function that maps vectors from one vector space to another, preserving vector addition and scalar multiplication.  Can be represented by a matrix. [[Linear Transformations and Matrices]]


**VI. Eigenvalues and Eigenvectors:**

* **Definition:**  An eigenvector of a matrix is a non-zero vector that, when multiplied by the matrix, only changes in scale (i.e., $A\mathbf{v} = \lambda\mathbf{v}$, where $\lambda$ is the eigenvalue and $\mathbf{v}$ is the eigenvector). [[Eigenvalues and Eigenvectors: Calculation and Applications]]


**VII.  Determinants:**

* **Definition:** A scalar value associated with a square matrix.  Used to determine invertibility, and other properties. [[Determinants and their properties]]


**VIII.  Inner Product (Dot Product):**

* Definition: A way to multiply two vectors to produce a scalar value.  $u \cdot v = \sum_{i=1}^n u_i v_i$.   Useful for finding angles between vectors and projections. [[Inner Product and Orthogonality]]


**IX. Orthogonality:**

* Definition: Two vectors are orthogonal if their dot product is zero.  [[Inner Product and Orthogonality]]


**X. Gram-Schmidt Process:**  A method to transform a set of linearly independent vectors into an orthonormal set. [[Gram-Schmidt Process]]
