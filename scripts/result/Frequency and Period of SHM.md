
# [[AP Physics C Home]]
# Topic 7.2: Frequency and Period of SHM

Simple Harmonic Motion (SHM) is characterized by a restoring force that is directly proportional to the displacement from an equilibrium position. To understand the temporal nature of this motion—how long it takes to complete a cycle and how often it repeats—we must define the period ($T$) and frequency ($f$).

## Basic Definitions

In SHM, the object oscillates back and forth. 
*   **Period ($T$):** The time taken to complete one full cycle of motion. Measured in seconds ($s$).
*   **Frequency ($f$):** The number of cycles completed per unit time. Measured in Hertz ($Hz$, or $s^{-1}$).
*   **Angular Frequency ($\omega$):** A measure of how fast the phase of the oscillation changes, measured in radians per second ($rad/s$).

These quantities are fundamentally related:

| Relationship | Formula |
| :--- | :--- |
| Period and Frequency | $$T=\frac{1}{f}$$ |
| Angular Frequency | $$\omega=2\pi f=\frac{2\pi}{T}$$ |

## Determining Frequency for a Spring-Mass System

For an object of mass $m$ attached to an ideal spring with spring constant $k$, the motion is described by Hooke's Law: $F_s = -kx$. By applying [[Newtons Second Law in Rotational Form]] (in the linear analogy sense) or simply the standard linear dynamics, we find that the acceleration is $a = -\frac{k}{m}x$.

Comparing this to the defining differential equation for [[Defining Simple Harmonic Motion (SHM)]], $\frac{d^2x}{dt^2} = -\omega^2x$, we identify that $\omega^2 = \frac{k}{m}$.

Thus, the angular frequency for a spring-mass system is:
$$\omega = \sqrt{\frac{k}{m}}$$

Using the relationships defined in the previous table, we can derive the period and frequency:

*   **Period of a spring:** $$T=2\pi\sqrt{\frac{m}{k}}$$
*   **Frequency of a spring:** $$f=\frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

## Key Takeaways

1.  **Mass vs. Stiffness:** Notice that for a spring system, the period increases as mass increases (inertia resists change) and decreases as the spring constant $k$ increases (stiffer springs pull back faster).
2.  **Independence of Amplitude:** Crucially, for a linear oscillator, the period and frequency are independent of the amplitude ($A$). Whether you pull the spring back 1 cm or 10 cm, the time it takes to return to equilibrium is determined solely by the mass and the spring constant.
3.  **Dynamic Context:** While these equations are derived from the mechanics of the system, they are consistent with the energy conservation laws discussed in [[Energy of Simple Harmonic Oscillators]]. The constant exchange between kinetic energy and elastic potential energy ensures that the frequency remains constant regardless of the energy of the system.

If the oscillator is more complex, such as a pendulum, the frequency calculation requires accounting for gravity and length, which is explored in [[Simple and Physical Pendulums]].