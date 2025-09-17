# [[AP Physics Home]]
# AP Physics Note Page: Energy of Simple Harmonic Oscillators

Simple Harmonic Motion (SHM) is a special type of periodic motion where the restoring force is directly proportional to the displacement and acts in the direction opposite to the displacement. This section focuses on the energy transformations within such systems.

## Energy in SHM Systems

In a system undergoing [[Defining Simple Harmonic Motion (SHM)]], such as a mass on a spring, energy continuously transforms between kinetic and potential forms. Assuming an ideal system with no damping (e.g., air resistance or friction), the total mechanical energy of the system remains constant, adhering to the principle of [[Conservation of Energy]].

### Kinetic Energy in SHM

The [[Translational Kinetic Energy]] ($KE$) of an oscillating mass $m$ at any given instant is given by:

$
KE = \frac{1}{2}mv^2
$

Where $v$ is the instantaneous velocity of the mass.
For a mass on a spring undergoing SHM, its position can be described by $x(t) = A \cos(\omega t + \phi)$, and its velocity by $v(t) = -A\omega \sin(\omega t + \phi)$.
Substituting the velocity equation into the kinetic energy formula:

$
KE(t) = \frac{1}{2}m(-A\omega \sin(\omega t + \phi))^2 = \frac{1}{2}mA^2\omega^2 \sin^2(\omega t + \phi)
$

The maximum kinetic energy occurs when the mass passes through the equilibrium position ($x=0$), where its speed is maximum ($v_{max} = A\omega$).
$
KE_{max} = \frac{1}{2}mA^2\omega^2
$

### Potential Energy in SHM

For a spring-mass system, the [[Potential Energy]] stored in the spring ($PE_s$) is given by:

$
PE_s = \frac{1}{2}kx^2
$

Where $k$ is the [[Spring Forces|spring constant]] and $x$ is the displacement from the equilibrium position.
Since $x(t) = A \cos(\omega t + \phi)$, the potential energy as a function of time is:

$
PE_s(t) = \frac{1}{2}k(A \cos(\omega t + \phi))^2 = \frac{1}{2}kA^2 \cos^2(\omega t + \phi)
$

The maximum potential energy occurs at the extreme displacements ($x = \pm A$), where the spring is maximally stretched or compressed.
$
PE_{s,max} = \frac{1}{2}kA^2
$

### Total Mechanical Energy

The total mechanical energy ($E_{total}$) of an ideal SHM system is the sum of its kinetic and potential energies:

$
E_{total} = KE + PE_s = \frac{1}{2}mA^2\omega^2 \sin^2(\omega t + \phi) + \frac{1}{2}kA^2 \cos^2(\omega t + \phi)
$

We know that for a spring-mass system, the angular frequency $\omega$ is related to $k$ and $m$ by $\omega = \sqrt{\frac{k}{m}}$, or $\omega^2 = \frac{k}{m}$.
Substituting $k = m\omega^2$ into the $PE_s$ term:

$
E_{total} = \frac{1}{2}mA^2\omega^2 \sin^2(\omega t + \phi) + \frac{1}{2}(m\omega^2)A^2 \cos^2(\omega t + \phi)
$
$
E_{total} = \frac{1}{2}mA^2\omega^2 (\sin^2(\omega t + \phi) + \cos^2(\omega t + \phi))
$
Since $\sin^2\theta + \cos^2\theta = 1$, the total energy simplifies to:

$
E_{total} = \frac{1}{2}mA^2\omega^2
$

Alternatively, using $m = \frac{k}{\omega^2}$:

$
E_{total} = \frac{1}{2}kA^2
$

This shows that the total mechanical energy in SHM is constant and proportional to the square of the amplitude ($A^2$) and either the mass and angular frequency squared, or the spring constant.

## Energy Transformation Summary

The table below summarizes the energy distribution at key points in a spring-mass SHM cycle:

| Position | Displacement (x) | Velocity (v) | Kinetic Energy ($KE$) | Potential Energy ($PE_s$) | Total Energy ($E_{total}$) |
| :------- | :--------------- | :----------- | :-------------------- | :------------------------ | :------------------------- |
| **Equilibrium** | $x=0$ | $v = \pm A\omega$ | $\frac{1}{2}mA^2\omega^2$ | $0$ | $\frac{1}{2}mA^2\omega^2$ |
| **Maximum Displacement** | $x = \pm A$ | $v = 0$ | $0$ | $\frac{1}{2}kA^2$ | $\frac{1}{2}kA^2$ |
| **General Position** | $x$ | $v$ | $\frac{1}{2}mv^2$ | $\frac{1}{2}kx^2$ | $\frac{1}{2}kA^2 = \frac{1}{2}mA^2\omega^2$ |

Since $E_{total}$ is constant, we can equate the energy at any point to the maximum potential or kinetic energy:
$
\frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kA^2 = \frac{1}{2}mA^2\omega^2
$

This equation is extremely useful for solving problems involving the velocity of the oscillating mass at a given position, or vice versa, without needing to know the exact time. For example, the velocity at any position $x$ can be found from:
$
v = \pm \omega \sqrt{A^2 - x^2}
$

[[Conservation of Energy]] is a fundamental principle for analyzing SHM systems, especially when considering the interplay between kinetic and potential energy forms. Understanding these energy transformations is crucial for comprehending the dynamics of oscillating systems.