
# [[AP Physics C Home]]
# Induced Currents and Magnetic Forces

When a conductor moves through a magnetic field, the motion of the charge carriers within the conductor creates an interaction between the magnetic field and the electric current. This interaction is the foundation of motional electromotive force (EMF) and the resulting induced currents.

## Motional EMF
Motional EMF occurs when a conductor moves through a magnetic field. For a conducting rod of length $l$ moving at a velocity $v$ perpendicular to a uniform magnetic field $B$, the magnetic force on the charge carriers creates a potential difference across the ends of the rod.

The magnetic force acting on a charge $q$ is given by $F = qvB$. This force pushes charges to the ends of the rod until an opposing electric field is established, creating a balanced electric force $F_E = qE = q(\frac{\Delta V}{l})$. By equating these forces, we derive the motional EMF:

$$\varepsilon = Blv$$

This equation assumes the velocity, magnetic field, and the length of the conductor are all mutually perpendicular. If they are not perpendicular, you must use the appropriate components.

## Lenz's Law and Energy Conservation
The induced current that arises from motional EMF creates its own magnetic field. According to [[Lenz's Law]], the direction of this induced current is such that the resulting magnetic force opposes the original motion of the conductor. 

This is a physical manifestation of the [[Conservation of Energy]]. If the induced current did not oppose the motion, the system would accelerate without any external work input, violating energy conservation laws.

## Induced Current in a Circuit
Consider a conductive loop or a sliding rod on rails forming a closed circuit with resistance $R$. The induced EMF generates an induced current ($I$) governed by [[Ohms Law]]:

$$I = \frac{\varepsilon}{R} = \frac{Blv}{R}$$

Because there is a current flowing in a magnetic field, the rod will experience a magnetic force (often called a "magnetic drag force") that opposes its motion:

$$F_B = IlB = \left(\frac{Blv}{R}\right)lB = \frac{B^2l^2v}{R}$$

### Summary of Relationships

| Variable | Symbol | Relationship to Motion |
| :--- | :--- | :--- |
| Motional EMF | $\varepsilon$ | $\varepsilon \propto v$ |
| Induced Current | $I$ | $I \propto v$ |
| Magnetic Drag Force | $F_B$ | $F_B \propto v$ |

## Power Considerations
As the magnetic force opposes the motion of the rod, an external force $F_{ext}$ must be applied to maintain a constant velocity $v$. The power delivered by the external force is equal to the rate at which energy is dissipated in the resistor.

The mechanical power input is:
$$P_{mech} = F_{ext}v = \left(\frac{B^2l^2v}{R}\right)v = \frac{B^2l^2v^2}{R}$$

The electrical power dissipated as heat in the resistor is:
$$P_{elec} = I^2R = \left(\frac{Blv}{R}\right)^2 R = \frac{B^2l^2v^2}{R}$$

As expected, $P_{mech} = P_{elec}$, confirming the principle of [[Conservation of Energy]].