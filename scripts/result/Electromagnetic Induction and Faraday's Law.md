
# [[AP Physics C Home]]
# Electromagnetic Induction and Faraday's Law

Electromagnetic induction is the phenomenon where a changing magnetic environment creates an electromotive force (EMF), which can drive current in a circuit. This discovery, primarily credited to Michael Faraday, is the foundational principle behind electric generators, transformers, and inductors.

## Magnetic Flux
Before defining Faraday's Law, one must understand [[Magnetic Flux]]. Magnetic flux ($\Phi_B$) measures the amount of magnetic field passing through a specific surface area. It is defined by the dot product of the magnetic field vector and the area vector:

$$\Phi_B = \int \vec{B} \cdot d\vec{A} = B A \cos(\theta)$$

Where:
*   $B$ is the magnetic field strength.
*   $A$ is the area of the loop.
*   $\theta$ is the angle between the magnetic field vector and the vector normal (perpendicular) to the surface of the loop.

## Faraday's Law of Induction
Faraday's Law states that the magnitude of the induced EMF ($\mathcal{E}$) in a circuit is proportional to the rate of change of magnetic flux through the circuit.

$$\mathcal{E} = -N \frac{d\Phi_B}{dt}$$

*   $\mathcal{E}$: Induced Electromotive Force (Volts)
*   $N$: Number of turns in the coil
*   $\frac{d\Phi_B}{dt}$: Time rate of change of magnetic flux (Webers per second)

### Lenz's Law
The negative sign in Faraday's Law represents **Lenz's Law**. It states that the direction of the induced current is always such that it opposes the change in magnetic flux that produced it. This is a manifestation of the law of conservation of energy. If the flux is increasing, the induced current creates a magnetic field to oppose that increase; if the flux is decreasing, the induced current creates a field to support the original flux.

## Methods of Inducing EMF
Because flux depends on $B$, $A$, and $\theta$, an EMF can be induced if any of these variables change over time.

| Change Type | Physical Mechanism |
| :--- | :--- |
| Changing $B$ | Moving a magnet closer/farther from a loop or changing current in an electromagnet. |
| Changing $A$ | Changing the shape or size of the conducting loop (e.g., expanding a loop). |
| Changing $\theta$ | Rotating the loop within a magnetic field (this is how [[AC Generators]] function). |

## Motional EMF
A special case of induction occurs when a conductor moves through a constant magnetic field. This is known as **Motional EMF**. As charge carriers (electrons) move within a wire that is cutting through magnetic field lines, they experience a magnetic force $F = qvB$, causing a charge separation and an induced potential difference.

For a straight rod of length $L$ moving with velocity $v$ perpendicular to a uniform field $B$:

$$\mathcal{E} = B v L$$

If the rod is part of a larger circuit, this EMF drives a current, which is then subject to [[Magnetism and Current-Carrying Wires]], creating a magnetic force that opposes the motion of the rod.