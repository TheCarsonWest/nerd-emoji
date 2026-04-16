
# [[AP Physics C Home]]
# Topic 10.6: Capacitors

Capacitors are fundamental components in electronic circuits designed to store electrical potential energy in an electric field. By separating opposite charges on two conductive plates, a capacitor creates a potential difference that can be released when needed.

## Basic Principles of Capacitance

Capacitance ($C$) is defined as the measure of a capacitor's ability to store charge ($Q$) for a given potential difference ($V$). It is a geometric property of the device and does not change based on the amount of charge stored.

The defining equation for capacitance is:
$$C=\frac{Q}{V}$$

Where:
*   $C$ is capacitance in Farads (F)
*   $Q$ is the magnitude of charge on either plate in Coulombs (C)
*   $V$ is the potential difference between the plates in Volts (V)

## The Parallel-Plate Capacitor

For the most common configuration, the parallel-plate capacitor, capacitance is determined by the physical geometry of the plates and the material between them (the dielectric).

The formula for parallel-plate capacitance is:
$$C=\frac{\kappa\epsilon_0 A}{d}$$

| Symbol | Definition |
| :--- | :--- |
| $\epsilon_0$ | Permittivity of free space ($8.85 \times 10^{-12} \text{ F/m}$) |
| $A$ | Area of one plate |
| $d$ | Separation distance between plates |
| $\kappa$ | Dielectric constant of the material between plates |

[[Electric Potential]] explains how the separation distance $d$ relates to the electric field created between these plates.

## Energy Storage

Capacitors store energy within the electric field formed between the plates. This stored potential energy ($U_c$) can be calculated using the charge and potential difference:

$$U_c=\frac{1}{2}QV=\frac{1}{2}CV^2=\frac{Q^2}{2C}$$

As the capacitor charges, work is done to move charge against the existing electric field, which is why energy is stored as potential energy rather than being dissipated as heat.

## Dielectrics

A dielectric is an insulating material placed between the plates of a capacitor. Inserting a dielectric increases the capacitance by a factor of $\kappa$ (the dielectric constant). The dielectric works by becoming polarized, creating an internal electric field that opposes the external field created by the plates, effectively reducing the net electric field and allowing more charge to be stored for the same voltage.

## Combining Capacitors

When multiple capacitors are connected in a circuit, they can be simplified into an equivalent capacitance ($C_{eq}$).

### Series Circuits
In series, the charge $Q$ is the same on each capacitor, but the potential difference $V$ is divided.
$$\frac{1}{C_{eq}}=\frac{1}{C_1}+\frac{1}{C_2}+...$$

### Parallel Circuits
In parallel, the potential difference $V$ is the same across each capacitor, but the charge $Q$ is divided.
$$C_{eq}=C_1+C_2+...$$

Understanding how these combine is crucial when analyzing [[Simple Circuits]] or complex [[Resistor-Capacitor (RC) Circuits]].