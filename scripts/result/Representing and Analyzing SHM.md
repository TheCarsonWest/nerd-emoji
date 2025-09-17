# [[AP Physics Home]]
# AP Physics Note Page: Representing and Analyzing SHM

Simple Harmonic Motion (SHM) is a special type of periodic motion where the restoring force is directly proportional to the displacement from equilibrium and acts in the opposite direction. Understanding how to represent and analyze SHM mathematically is crucial for predicting the behavior of oscillating systems. This page builds upon the concepts introduced in [[Defining Simple Harmonic Motion (SHM)]] and [[Frequency and Period of SHM]].

## I. Position as a Function of Time

The displacement of an object undergoing SHM from its equilibrium position can be described by a sinusoidal function. The general form typically uses either sine or cosine, depending on the initial conditions (at $t=0$). For an oscillator starting at its maximum positive displacement (amplitude) at $t=0$, the cosine function is often preferred.

$x(t) = A \cos(\omega t + \phi)$

Where:
*   $x(t)$ is the displacement from equilibrium at time $t$.
*   $A$ is the [[Amplitude of SHM]], the maximum displacement from equilibrium.
*   $\omega$ (omega) is the [[Angular Frequency in SHM]], representing how fast the oscillation occurs in radians per second. It is related to the period $T$ and frequency $f$ by $\omega = \frac{2\pi}{T} = 2\pi f$.
*   $t$ is time.
*   $\phi$ (phi) is the [[Phase Constant in SHM]], which accounts for the initial conditions of the motion (i.e., the displacement at $t=0$).

**Example:** If an object starts at its positive maximum displacement ($x=A$) at $t=0$, then $A = A \cos(\phi)$, which implies $\phi = 0$. If it starts at equilibrium moving in the positive direction ($x=0, v>0$) at $t=0$, then $0 = A \cos(\phi)$, which implies $\phi = -\frac{\pi}{2}$ (or $\frac{3\pi}{2}$).

## II. Velocity as a Function of Time

The velocity of an object in SHM can be found by taking the first derivative of the position function with respect to time.

Given $x(t) = A \cos(\omega t + \phi)$:

$v(t) = \frac{dx}{dt} = -A\omega \sin(\omega t + \phi)$

Key characteristics of velocity in SHM:
*   The **maximum speed** occurs when $\sin(\omega t + \phi) = \pm 1$. Thus, $v_{max} = A\omega$.
*   The speed is zero at the extreme positions ($x = \pm A$), where the object momentarily stops before reversing direction. This is consistent with $x=A \cos(\omega t + \phi)$ and $v=-A\omega \sin(\omega t + \phi)$ when $\cos(\omega t + \phi) = \pm 1$ then $\sin(\omega t + \phi) = 0$.
*   The speed is maximum at the equilibrium position ($x=0$).

## III. Acceleration as a Function of Time

The acceleration of an object in SHM can be found by taking the first derivative of the velocity function (or the second derivative of the position function) with respect to time.

Given $v(t) = -A\omega \sin(\omega t + \phi)$:

$a(t) = \frac{dv}{dt} = -A\omega^2 \cos(\omega t + \phi)$

By substituting $x(t) = A \cos(\omega t + \phi)$ back into the acceleration equation, we get the defining characteristic of SHM:

$a(t) = -\omega^2 x(t)$

This equation clearly shows that the acceleration is directly proportional to the negative of the displacement, which is consistent with Hooke's Law for a spring-mass system ($F = -kx$, and $F=ma \implies a = -(k/m)x$). In fact, $\omega^2 = k/m$ for a spring-mass system.

Key characteristics of acceleration in SHM:
*   The **maximum acceleration** occurs when $\cos(\omega t + \phi) = \pm 1$. Thus, $a_{max} = A\omega^2$.
*   The acceleration is zero at the equilibrium position ($x=0$).
*   The acceleration is maximum at the extreme positions ($x = \pm A$), and it always points towards the equilibrium position.

## IV. Summary of SHM Equations

| Quantity      | Equation (starting at $x=A$ at $t=0$) | Maximum Value     | Relationship to $\omega$ |
| :------------ | :------------------------------------ | :---------------- | :----------------------- |
| Position      | $x(t) = A \cos(\omega t)$             | $A$               | $x_{max} = A$            |
| Velocity      | $v(t) = -A\omega \sin(\omega t)$      | $A\omega$         | $v_{max} = A\omega$      |
| Acceleration  | $a(t) = -A\omega^2 \cos(\omega t)$    | $A\omega^2$       | $a_{max} = A\omega^2$    |

Note that the equations in the table assume $\phi = 0$. For a general case, the phase constant $\phi$ must be included as shown in the previous sections.

## V. Phase Relationships

The position, velocity, and acceleration in SHM are all sinusoidal functions but are "out of phase" with each other:
*   Velocity is $90^\circ$ (or $\pi/2$ radians) out of phase with position. When position is maximum, velocity is zero, and vice-versa.
*   Acceleration is $180^\circ$ (or $\pi$ radians) out of phase with position. When position is positive maximum, acceleration is negative maximum, and vice-versa.
*   Acceleration is $90^\circ$ (or $\pi/2$ radians) out of phase with velocity.

This phase relationship is critical for understanding the energy transformations in SHM, which is covered in [[Energy of Simple Harmonic Oscillators]].