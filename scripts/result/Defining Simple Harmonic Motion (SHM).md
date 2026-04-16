
# [[AP Physics C Home]]
# Defining Simple Harmonic Motion (SHM)

Simple Harmonic Motion (SHM) is a specific type of periodic motion where the restoring force is directly proportional to the displacement and acts in the direction opposite to that displacement. It is the fundamental building block for understanding oscillations in physical systems, from springs to [[Simple and Physical Pendulums]].

## The Defining Condition of SHM

For an object to undergo SHM, the net force acting on it must satisfy Hooke’s Law, which states that the force is proportional to the displacement $x$ from the equilibrium position. According to Newton’s Second Law ($F=ma$), we can define SHM mathematically as:

$$F_{net} = -kx = ma$$

Where:
*   $k$ is the force constant (or spring constant).
*   $x$ is the displacement from equilibrium.
*   $m$ is the mass of the oscillating object.
*   $a$ is the acceleration of the object.

This equation reveals the critical characteristic of SHM: the acceleration is directly proportional to the negative of the displacement:

$$a = -\frac{k}{m}x$$

## The Differential Equation of SHM

Since acceleration is the second derivative of position with respect to time ($a = \frac{d^2x}{dt^2}$), we can rewrite the equation above as a second-order linear differential equation:

$$\frac{d^2x}{dt^2} + \frac{k}{m}x = 0$$

In physics, we often define the angular frequency $\omega$ as $\omega = \sqrt{\frac{k}{m}}$. Substituting this into the differential equation gives us the standard form for SHM:

$$\frac{d^2x}{dt^2} + \omega^2x = 0$$

The solution to this differential equation describes the position of the object at any time $t$. We discuss this further in [[Representing and Analyzing SHM]].

## Key Terminology

To analyze oscillations effectively, you must be familiar with the following parameters:

| Term | Definition | Unit (SI) |
| :--- | :--- | :--- |
| **Equilibrium Position** | The point where the net force is zero ($x = 0$). | meters (m) |
| **Amplitude ($A$)** | The maximum displacement from equilibrium. | meters (m) |
| **Period ($T$)** | The time taken to complete one full cycle of oscillation. | seconds (s) |
| **Frequency ($f$)** | The number of cycles completed per unit of time. | Hertz (Hz) |
| **Angular Frequency ($\omega$)** | The rate of change of the phase of the sinusoidal waveform. | rad/s |

## Energy Perspective
SHM is fundamentally a dance between potential energy and kinetic energy. Because the force is conservative (like the force from a spring), the total mechanical energy is conserved throughout the motion. You can learn more about how energy shifts between states during oscillation in [[Energy of Simple Harmonic Oscillators]]. 

Additionally, understanding the relationship between the physical attributes of the system (mass and stiffness) and the timing of the oscillation is covered in [[Frequency and Period of SHM]].