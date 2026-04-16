
# [[AP Physics C Home]]
# Resistance, Resistivity, and Ohm's Law

## Overview
In the study of electrodynamics, understanding how materials impede the flow of charge is fundamental to circuit analysis. This topic defines the relationship between the physical properties of a material, its geometry, and the resulting electrical behavior when subjected to a potential difference.

## Resistance ($R$)
Resistance is a measure of the opposition to current flow in an electrical circuit. For an ohmic material, the resistance is defined by the ratio of the potential difference across a conductor to the current flowing through it.

The unit of resistance is the Ohm ($\Omega$), where $1 \Omega = 1 V/A$.

### Ohm's Law
Ohm's Law states that for many materials, the current $I$ is directly proportional to the potential difference $V$ across the material, assuming the temperature remains constant.

$$V = IR$$

Where:
*   $V$ is potential difference (Volts)
*   $I$ is current (Amperes)
*   $R$ is resistance ($\Omega$)

[[Electric Current]] and [[Simple Circuits]] provide further context on how this equation applies to broader circuit analysis.

## Resistivity ($\rho$)
While resistance is a property of a specific object, **resistivity** is an intrinsic property of a material itself, independent of the object's shape or size. It quantifies how strongly a given material opposes the flow of electric current.

The resistance of a conductor is determined by its material resistivity, length, and cross-sectional area:

$$R = \rho \frac{L}{A}$$

Where:
*   $R$ is resistance ($\Omega$)
*   $\rho$ is resistivity ($\Omega \cdot m$)
*   $L$ is the length of the conductor ($m$)
*   $A$ is the cross-sectional area ($m^2$)

### Temperature Dependence
The resistivity of materials is temperature-dependent. For metals, resistivity generally increases as temperature increases, because increased thermal agitation of the atoms impedes the flow of electrons. This is approximated by the linear relationship:

$$\rho = \rho_0 [1 + \alpha(T - T_0)]$$

| Material Type | Resistivity Characteristics |
| :--- | :--- |
| **Conductors** | Low $\rho$ (e.g., Copper: $\approx 1.7 \times 10^{-8} \Omega \cdot m$) |
| **Semiconductors** | Intermediate $\rho$ (Highly temperature dependent) |
| **Insulators** | Very High $\rho$ (e.g., Rubber: $\approx 10^{13} \Omega \cdot m$) |

## Microscopic View of Ohm's Law
To understand Ohm's Law at a microscopic level, we look at the current density ($J$) and the electric field ($E$). The microscopic form of Ohm's Law is:

$$J = \sigma E$$

Where:
*   $J$ is current density ($A/m^2$)
*   $\sigma$ is conductivity ($1/\rho$), the reciprocal of resistivity.
*   $E$ is the electric field magnitude ($V/m$)

This relates the electric field driving the charges to the resulting current density inside the conductor.