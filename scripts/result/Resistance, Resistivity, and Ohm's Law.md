
# [[AP Physics C Home]]
# Resistance, Resistivity, and Ohm's Law

In electrical circuits, the behavior of current depends heavily on the materials used and their physical dimensions. This section explores how we quantify the opposition to current flow.

## Resistance ($R$)

Resistance is the measure of the opposition to the flow of electric current through a material. It is defined as the ratio of the potential difference (voltage) across a device to the current flowing through it.

The unit of resistance is the Ohm ($\Omega$), named after Georg Simon Ohm, where $1 \Omega = 1 V/A$.

## Resistivity ($\rho$)

While resistance describes a specific component, **resistivity** is an intrinsic property of a material itself. It quantifies how strongly a given material opposes the flow of electric current. 

For a cylindrical conductor with length $L$ and cross-sectional area $A$, the resistance is given by:

$$R = \rho \frac{L}{A}$$

| Property | Symbol | Unit | Definition |
| :--- | :--- | :--- | :--- |
| Resistance | $R$ | $\Omega$ (Ohms) | Opposition to current flow in a specific component |
| Resistivity | $\rho$ | $\Omega \cdot m$ | Intrinsic material property hindering current |
| Length | $L$ | $m$ (meters) | Length of the conductor |
| Area | $A$ | $m^2$ (square meters) | Cross-sectional area of the conductor |

Notice that resistance is directly proportional to length and inversely proportional to the cross-sectional area. This means long, thin wires have higher resistance, while short, thick wires have lower resistance.

## Ohm's Law

Ohm’s Law states that for many materials (called "ohmic" materials), the current flowing through a conductor is directly proportional to the potential difference applied across it, provided the temperature remains constant.

The standard form of Ohm’s Law is:

$$V = IR$$

Where:
* $V$ is the potential difference (Voltage) in Volts ($V$).
* $I$ is the current in Amperes ($A$).
* $R$ is the resistance in Ohms ($\Omega$).

It is important to note that Ohm’s Law is an empirical relationship, not a fundamental law of physics like Coulomb's Law. It applies strictly to *ohmic* conductors. Materials that do not follow this linear relationship are termed *non-ohmic*.

## Temperature Dependence

The resistivity of a material changes with temperature. For many metals, resistivity increases linearly with temperature over a limited range. The formula is:

$$\rho = \rho_0 [1 + \alpha(T - T_0)]$$

Where:
* $\rho_0$ is the resistivity at a reference temperature $T_0$.
* $\alpha$ is the temperature coefficient of resistivity.
* $T$ is the current temperature.

This temperature dependency is critical when designing [[Simple Circuits]] that may be subject to extreme heat, as the resistance of components may drift from their nominal values.

## Microscopic View

To understand why these relationships exist, we must look at the movement of charge carriers. The relationship between current density ($J$) and the electric field ($E$) within a conductor is given by the microscopic form of Ohm's Law:

$$J = \sigma E$$

Where $\sigma = 1/\rho$ is the conductivity of the material. This concept relates directly to the behavior of particles discussed in [[Electric Current]].