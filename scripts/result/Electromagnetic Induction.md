
# [[AP Physics C Home]]
# Topic 13.2: Electromagnetic Induction

Electromagnetic induction is the phenomenon where a changing magnetic field induces an electromotive force (EMF) and, consequently, an electric current in a conductor. This is the fundamental principle behind electric generators, transformers, and induction cooktops.

## Faraday's Law of Induction

Faraday’s Law states that the magnitude of the induced EMF ($\mathcal{E}$) in a circuit is directly proportional to the rate of change of magnetic flux ($\Phi_B$) through the circuit.

The mathematical formulation is given by:

$$\mathcal{E} = -N \frac{d\Phi_B}{dt}$$

Where:
*   $\mathcal{E}$ is the induced EMF (measured in Volts).
*   $N$ is the number of turns in the coil.
*   $\Phi_B$ is the [[Magnetic Flux]].
*   The negative sign represents Lenz’s Law.

## Lenz's Law

Lenz’s Law is a consequence of the law of conservation of energy. It dictates the *direction* of the induced current. It states that the induced current will create a magnetic field that opposes the change in the magnetic flux that produced it.

*   If the flux through a loop is increasing, the induced current will create a magnetic field in the opposite direction to the existing field to try to reduce the flux.
*   If the flux through a loop is decreasing, the induced current will create a magnetic field in the same direction to try to maintain the flux.

## Motional EMF

When a conductor moves through a constant magnetic field, a force acts on the charge carriers within the conductor. This force separates the charges, creating a potential difference across the ends of the conductor. This is known as motional EMF.

For a straight conductor of length $L$ moving with velocity $v$ perpendicular to a magnetic field $B$:

$$\mathcal{E} = B L v$$

### Summary of Induced EMF Scenarios

| Scenario | Physical Mechanism | Governing Equation |
| :--- | :--- | :--- |
| Changing $B$-field | Time-varying magnetic field within a stationary loop | $\mathcal{E} = -N \frac{d\Phi_B}{dt}$ |
| Changing Area | Loop changing size or shape in a constant $B$-field | $\mathcal{E} = -B \frac{dA}{dt}$ |
| Changing Angle | Loop rotating within a constant $B$-field | $\mathcal{E} = -N \frac{d(BA \cos\theta)}{dt}$ |
| Motional EMF | Conductor moving through a $B$-field | $\mathcal{E} = B L v$ |

## Applications and Considerations

The study of electromagnetic induction is crucial for understanding how mechanical energy is converted into electrical energy. When a coil rotates in a magnetic field, the angle $\theta$ changes over time (usually $\theta = \omega t$), which results in a sinusoidal induced EMF. This is the basis for AC generators.

Furthermore, this topic bridges the gap to understanding [[Inductance]], where a changing current in one circuit induces an EMF in the same or a nearby circuit due to its own magnetic field. 

One must also be careful to distinguish between these effects and the [[Magnetic Fields of Current-Carrying Wires and the Biot-Savart Law]], as induction relies on the *change* of fields, rather than the existence of static fields alone.