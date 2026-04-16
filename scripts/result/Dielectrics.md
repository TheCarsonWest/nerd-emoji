
# [[AP Physics C Home]]
# AP Physics C: Dielectrics

## Overview
A dielectric is a non-conducting material (an insulator) placed between the plates of a capacitor. When inserted, dielectrics increase the capacitance of the capacitor, allowing it to store more charge at a given potential difference. This is a fundamental concept in [[Capacitors]].

## Molecular Basis of Dielectrics
When a dielectric is placed in an external electric field $E_0$ (created by the capacitor plates), the molecules within the dielectric become polarized. 

1.  **Polar Molecules:** Molecules with a permanent dipole moment align with the field.
2.  **Non-Polar Molecules:** The field induces a dipole moment by slightly shifting the electron clouds relative to the nuclei.

This polarization creates an internal "induced" electric field ($E_{induced}$) that points in the opposite direction of the external field. The net electric field ($E_{net}$) inside the dielectric is reduced:
$$E_{net} = E_0 - E_{induced}$$

## The Dielectric Constant ($\kappa$)
The dielectric constant, denoted by $\kappa$ (kappa), is a dimensionless property of the material that quantifies how much the material reduces the electric field. It is always greater than or equal to 1. For a vacuum, $\kappa = 1$.

The relationship between the initial field ($E_0$) and the net field ($E_{net}$) is:
$$E_{net} = \frac{E_0}{\kappa}$$

Similarly, the potential difference ($V$) across a capacitor with a dielectric, compared to the original potential ($V_0$) without one, is:
$$V = \frac{V_0}{\kappa}$$

## Impact on Capacitance
Since capacitance is defined as $C = Q/V$, if the potential difference $V$ decreases while the charge $Q$ remains constant (assuming the capacitor is disconnected from the battery), the capacitance must increase:
$$C = \frac{Q}{V} = \frac{Q}{V_0/\kappa} = \kappa \left(\frac{Q}{V_0}\right) = \kappa C_0$$

Thus, for a parallel plate capacitor, the new capacitance is:
$$C = \frac{\kappa \epsilon_0 A}{d}$$

### Summary of Effects
Assuming the capacitor is disconnected from the charging source, the charge $Q$ remains constant. Here is how the physical quantities change when a dielectric is inserted:

| Quantity | Change with Dielectric | Formula |
| :--- | :--- | :--- |
| **Capacitance** | Increases | $C = \kappa C_0$ |
| **Electric Field** | Decreases | $E = E_0 / \kappa$ |
| **Voltage** | Decreases | $V = V_0 / \kappa$ |
| **Charge** | Remains Constant | $Q = Q_0$ |
| **Stored Energy** | Decreases | $U = U_0 / \kappa$ |

*Note: If the capacitor remains connected to a battery, the Voltage ($V$) stays constant, meaning the Charge ($Q$) must increase to accommodate the higher capacitance.*

## Energy Storage
Dielectrics also impact the energy stored in the electric field of the capacitor. Since $U = \frac{1}{2}QV$ or $U = \frac{Q^2}{2C}$, inserting a dielectric when the battery is disconnected reduces the potential energy stored in the system, as the work done by the field on the dielectric is external energy removed from the capacitor. This relates back to the concepts discussed in [[Electric Potential Energy]].