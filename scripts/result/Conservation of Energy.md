# [[AP Physics Home]]
# AP Physics 1: Topic 3.4 - Conservation of Energy

## 1. Introduction to Conservation of Energy

The principle of [[Conservation of Energy]] is one of the most fundamental concepts in physics. It states that the total energy of an isolated system remains constant; energy can neither be created nor destroyed, but it can be transformed from one form to another. In the context of mechanics, this often involves the interplay between kinetic energy and various forms of potential energy.

## 2. Mechanical Energy

Mechanical energy ($E_M$) is the sum of an object's [[Translational Kinetic Energy]] ($K$) and all forms of [[Potential Energy]] ($U$).

$ E_M = K + U $

### 2.1 Kinetic Energy ($K$)

Kinetic energy is the energy an object possesses due to its motion.
$ K = \frac{1}{2}mv^2 $
Where $m$ is the mass of the object and $v$ is its speed.

### 2.2 Potential Energy ($U$)

Potential energy is stored energy that depends on the relative positions of various components of a system.
*   **Gravitational Potential Energy ($U_g$)**: Energy stored due to an object's position within a gravitational field.
    $ U_g = mgh $
    Where $m$ is mass, $g$ is the acceleration due to gravity, and $h$ is the height above a chosen reference level.
*   **Elastic Potential Energy ($U_s$)**: Energy stored in an elastic object, like a spring, when it is stretched or compressed from its equilibrium position.
    $ U_s = \frac{1}{2}kx^2 $
    Where $k$ is the [[Spring Forces|spring constant]] and $x$ is the displacement from equilibrium.

## 3. The Principle of Conservation of Mechanical Energy

When only conservative forces (like gravity and spring forces) do [[Work]] within a system, the total mechanical energy of the system remains constant.

$ E_{Mi} = E_{Mf} $
$ K_i + U_i = K_f + U_f $

Where the subscripts 'i' and 'f' refer to the initial and final states of the system, respectively. This equation is incredibly powerful for solving problems involving motion without directly using Newton's Laws and kinematics equations.

### Examples of Conservative Forces
*   Gravitational Force
*   Spring Force

### Examples of Non-Conservative Forces
*   Friction
*   Air Resistance
*   Applied Force (from an external agent)

## 4. Work Done by Non-Conservative Forces

If non-conservative forces (like friction or air resistance) are present and do work, then the total mechanical energy of the system is *not* conserved. Instead, the change in mechanical energy is equal to the work done by these non-conservative forces ($W_{nc}$).

$ W_{nc} = \Delta E_M = (K_f + U_f) - (K_i + U_i) $

This equation is sometimes referred to as the **Generalized Work-Energy Theorem** or the **Extended Conservation of Energy**. When $W_{nc}$ is negative (e.g., due to friction), mechanical energy is lost, often dissipated as thermal energy. If $W_{nc}$ is positive (e.g., an external force doing positive work), mechanical energy is added to the system.

## 5. Problem-Solving Strategy

1.  **Define the System**: Clearly identify what is included in your system (e.g., object, Earth, spring).
2.  **Identify Initial and Final States**: Determine the relevant positions and velocities at the beginning and end of the motion.
3.  **Choose a Reference Level**: For gravitational potential energy, select a height ($h=0$) for your calculations. This choice does not affect the change in potential energy, only its absolute value.
4.  **Identify Forces**: Determine if any non-conservative forces are doing work.
5.  **Apply the Appropriate Equation**:
    *   If only conservative forces do work: $K_i + U_i = K_f + U_f$
    *   If non-conservative forces do work: $W_{nc} = \Delta E_M$
6.  **Solve for the Unknown**: Use algebraic manipulation to find the desired quantity.

## 6. Energy Transformations Table

| Energy Type       | Initial State ($E_i$)              | Final State ($E_f$)                | Change in Energy ($\Delta E$) |
| :---------------- | :--------------------------------- | :--------------------------------- | :---------------------------- |
| **Kinetic ($K$)** | $\frac{1}{2}mv_i^2$                | $\frac{1}{2}mv_f^2$                | $\Delta K$                    |
| **Gravitational ($U_g$)** | $mgh_i$                            | $mgh_f$                            | $\Delta U_g$                  |
| **Elastic ($U_s$)** | $\frac{1}{2}kx_i^2$                | $\frac{1}{2}kx_f^2$                | $\Delta U_s$                  |
| **Mechanical ($E_M$)** | $K_i + U_{g,i} + U_{s,i}$ | $K_f + U_{g,f} + U_{s,f}$ | $\Delta E_M$                  |

**Note**: In an isolated system with only conservative forces, $\Delta E_M = 0$. Otherwise, $\Delta E_M = W_{nc}$.