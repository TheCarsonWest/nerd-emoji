
# [[AP Physics C Home]]
# Topic 13.6: Circuits with Capacitors and Inductors (LC Circuits)

An LC circuit consists of an ideal capacitor with capacitance $C$ and an ideal inductor with inductance $L$ connected in a closed loop. When the capacitor is initially charged and allowed to discharge through the inductor, the circuit exhibits electromagnetic oscillations. This system is the electromagnetic analog to a mechanical mass-spring system undergoing [[Defining Simple Harmonic Motion (SHM)]].

## The Physics of LC Oscillations

In an ideal LC circuit (with no resistance), energy is conserved, constantly trading back and forth between the electric field of the capacitor and the magnetic field of the inductor.

1.  **Capacitor Discharging:** Initially, all energy is stored in the electric field: $U_E = \frac{1}{2}\frac{Q^2}{C}$. As the capacitor discharges, current $I$ begins to flow, creating a magnetic field in the inductor.
2.  **Inductor Charging:** As $I$ reaches its maximum, all energy is stored in the magnetic field of the inductor: $U_B = \frac{1}{2}LI^2$.
3.  **Cycle Repeats:** The inductor opposes the change in current (Lenz's Law), forcing current to continue until the capacitor is recharged with opposite polarity.

## Mathematical Representation

The behavior of charge $q(t)$ in an LC circuit can be described by applying the loop rule. Since the total voltage sum is zero:
$$V_C + V_L = 0 \implies \frac{q}{C} + L\frac{di}{dt} = 0$$

Since $i = \frac{dq}{dt}$ and $\frac{di}{dt} = \frac{d^2q}{dt^2}$, we derive the differential equation for SHM:
$$\frac{d^2q}{dt^2} + \frac{1}{LC}q = 0$$

### Key Formulas

| Parameter | Formula |
| :--- | :--- |
| **Angular Frequency ($\omega$)** | $$\omega = \frac{1}{\sqrt{LC}}$$ |
| **Period ($T$)** | $$T = 2\pi\sqrt{LC}$$ |
| **Charge as a Function of Time** | $$q(t) = Q_{max}\cos(\omega t + \phi)$$ |
| **Current as a Function of Time** | $$i(t) = -I_{max}\sin(\omega t + \phi)$$ |

Where $I_{max} = \omega Q_{max}$.

## Energy in LC Circuits

In an ideal circuit, the total energy is constant. Just as in a mass-spring system, the energy oscillates between two forms:

$$U_{total} = U_E + U_B = \frac{q^2}{2C} + \frac{1}{2}Li^2 = \text{Constant}$$

At any given moment, the energy stored in the capacitor is maximum when the current is zero, and the energy stored in the inductor is maximum when the charge on the capacitor is zero.

## Damped Oscillations
In reality, all circuits have some resistance $R$. If resistance is present, energy is dissipated as heat, leading to **Damped LC Oscillations**. This is analogous to a mass-spring system with friction. The amplitude of the charge oscillations will decay over time, eventually coming to rest, similar to the behavior seen in [[Resistor Capacitor (RC) Circuits]] but involving oscillatory motion.