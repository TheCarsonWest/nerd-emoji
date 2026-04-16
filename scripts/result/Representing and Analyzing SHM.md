
# [[AP Physics C Home]]
# Representing and Analyzing Simple Harmonic Motion (SHM)

Simple Harmonic Motion (SHM) is defined by oscillatory motion where the restoring force is directly proportional to the displacement from equilibrium and directed toward it. Analyzing SHM requires understanding how position, velocity, and acceleration behave as functions of time.

## Mathematical Representation
The position $x(t)$ of an object undergoing SHM can be modeled using sinusoidal functions. The general equation is:

$$x(t) = A \cos(\omega t + \phi)$$

Where:
*   $A$: The amplitude (maximum displacement from equilibrium).
*   $\omega$: The angular frequency ($\omega = 2\pi f = \frac{2\pi}{T}$).
*   $\phi$: The phase constant (determines the initial position at $t=0$).

### Relationship between Kinematic Variables
Using [[Calculus]], specifically differentiation with respect to time, we can derive the velocity and acceleration functions from the position function.

| Kinematic Variable | Equation |
| :--- | :--- |
| **Position** $x(t)$ | $$x(t) = A \cos(\omega t + \phi)$$ |
| **Velocity** $v(t)$ | $$v(t) = \frac{dx}{dt} = -A\omega \sin(\omega t + \phi)$$ |
| **Acceleration** $a(t)$ | $$a(t) = \frac{dv}{dt} = -A\omega^2 \cos(\omega t + \phi)$$ |

Note that the acceleration is directly proportional to the negative of the position, consistent with Hooke's Law and Newton’s Second Law:
$$a(t) = -\omega^2 x(t)$$

## Analyzing Graphical Representations
Graphs of $x(t)$, $v(t)$, and $a(t)$ are vital for visualizing the phase relationships between these quantities.

*   **Position vs. Time:** A cosine wave with amplitude $A$.
*   **Velocity vs. Time:** A sine wave with amplitude $A\omega$. Velocity is $90^\circ$ ($\pi/2$ radians) out of phase with position. When position is at a maximum ($x=A$), velocity is zero. When position is at equilibrium ($x=0$), velocity is at its maximum magnitude.
*   **Acceleration vs. Time:** A cosine wave with amplitude $A\omega^2$, inverted relative to the position graph. Acceleration is $180^\circ$ ($\pi$ radians) out of phase with position.

## Energy in SHM
Analyzing SHM also involves understanding the energy transformations. Since SHM is a conservative system (assuming no friction or air resistance), the total mechanical energy is constant.

*   **Potential Energy:** The potential energy stored in a spring is defined by $U = \frac{1}{2}kx^2$. Using our substitution, we can relate this to the amplitude.
*   **Kinetic Energy:** The kinetic energy of the oscillating mass is $K = \frac{1}{2}mv^2$.

The total energy of the system is the sum of these, which remains constant throughout the cycle:
$$E_{total} = K + U = \frac{1}{2}kA^2 = \frac{1}{2}mv_{max}^2$$

For a deeper dive into the conservation laws governing these oscillations, refer to the notes on [[Energy of Simple Harmonic Oscillators]]. To understand the timing and duration of these cycles, see [[Frequency and Period of SHM]].