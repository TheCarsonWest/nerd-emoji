
# [[AP Physics C Home]]
# 7.4: Energy of Simple Harmonic Oscillators

In a system undergoing Simple Harmonic Motion (SHM), the total mechanical energy is conserved, assuming no non-conservative forces (like friction or air resistance) are acting on the system. This means that energy continuously oscillates between kinetic and potential forms.

## Components of Energy in SHM

For a mass-spring system, the energy is stored in two forms: kinetic energy ($K$) and elastic potential energy ($U_s$).

### Kinetic Energy
The kinetic energy of the oscillator is defined by the mass and its velocity. Since the velocity in SHM is a function of time, so is the kinetic energy.
$$K = \frac{1}{2}mv^2$$
Using the kinematic relationships established in [[Defining Simple Harmonic Motion (SHM)]], specifically $v(t) = -A\omega\sin(\omega t + \phi)$, we can express kinetic energy as:
$$K(t) = \frac{1}{2}m(A\omega)^2\sin^2(\omega t + \phi)$$

### Elastic Potential Energy
The potential energy is stored in the spring as it stretches or compresses. Using Hooke's Law and the position function $x(t) = A\cos(\omega t + \phi)$:
$$U_s = \frac{1}{2}kx^2$$
$$U_s(t) = \frac{1}{2}kA^2\cos^2(\omega t + \phi)$$

## Total Mechanical Energy
The total energy ($E_{total}$) is the sum of kinetic and potential energies. A key property of the simple harmonic oscillator is that the total energy is constant and depends only on the amplitude ($A$) and the spring constant ($k$).

$$E_{total} = K + U_s = \frac{1}{2}kA^2$$

Since $\omega^2 = \frac{k}{m}$, we can also express total energy in terms of the angular frequency and mass:
$$E_{total} = \frac{1}{2}m\omega^2A^2$$

## Energy Transformation Table

The energy fluctuates throughout the cycle of motion, but the sum remains invariant. The following table summarizes the energy distribution at specific points in the cycle:

| Position | Velocity | Kinetic Energy ($K$) | Potential Energy ($U_s$) | Total Energy ($E$) |
| :--- | :--- | :--- | :--- | :--- |
| Equilibrium ($x=0$) | Maximum ($v_{max}$) | $\frac{1}{2}kA^2$ | $0$ | $\frac{1}{2}kA^2$ |
| Amplitude ($x=A$) | $0$ | $0$ | $\frac{1}{2}kA^2$ | $\frac{1}{2}kA^2$ |
| Between $0$ and $A$ | Intermediate | $\frac{1}{2}k(A^2-x^2)$ | $\frac{1}{2}kx^2$ | $\frac{1}{2}kA^2$ |

## Key Takeaways
1.  **Conservation:** Because energy is conserved, the system obeys the principles discussed in [[Conservation of Energy]].
2.  **Amplitude Dependence:** Note that the total energy is proportional to the square of the amplitude ($E \propto A^2$). If you double the amplitude of an oscillation, you quadruple the energy of the system.
3.  **Frequency:** The total energy is independent of the frequency of the oscillator; it is strictly a function of the spring constant and the amplitude.
4.  **Work:** If an external force is applied to change the amplitude, the work done on the system corresponds to the change in the total mechanical energy, as detailed in [[Work]].