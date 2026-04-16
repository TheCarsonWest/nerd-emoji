
# [[AP Physics C Home]]
# AP Physics C: Rotational Kinematics

Rotational kinematics describes the motion of a rotating rigid body. Just as linear motion is described by displacement, velocity, and acceleration, rotational motion uses angular counterparts.

## Angular Variables

For an object rotating about a fixed axis, we define the following variables:

| Variable | Description | SI Unit |
| :--- | :--- | :--- |
| $\theta$ | Angular Position | radians (rad) |
| $\omega$ | Angular Velocity | rad/s |
| $\alpha$ | Angular Acceleration | rad/s² |

- **Angular Position ($\theta$):** The angle through which a point or line has been rotated in a specified sense about a specified axis.
- **Angular Velocity ($\omega$):** The rate of change of angular position. 
  $$\omega = \frac{d\theta}{dt}$$
- **Angular Acceleration ($\alpha$):** The rate of change of angular velocity.
  $$\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$$

[[Direction of Rotational Vectors]]

## Rotational Kinematic Equations

If a rigid body undergoes constant angular acceleration, we can use a set of kinematic equations analogous to those in linear kinematics. These equations apply only when $\alpha$ is constant.

| Linear Equation ($a$ = const) | Rotational Equation ($\alpha$ = const) |
| :--- | :--- |
| $v_f = v_i + at$ | $\omega_f = \omega_i + \alpha t$ |
| $\Delta x = v_it + \frac{1}{2}at^2$ | $\Delta \theta = \omega_it + \frac{1}{2}\alpha t^2$ |
| $v_f^2 = v_i^2 + 2a\Delta x$ | $\omega_f^2 = \omega_i^2 + 2\alpha \Delta \theta$ |
| $\Delta x = \frac{1}{2}(v_i + v_f)t$ | $\Delta \theta = \frac{1}{2}(\omega_i + \omega_f)t$ |

## Important Considerations

1. **Radians:** Always ensure that your calculator is in radian mode when performing calculations involving trigonometric functions or when converting between linear and angular units. The radian is a dimensionless unit, defined by the ratio of arc length to radius ($s = r\theta$).
2. **Signs:** Consistency is crucial. You must define a positive direction for rotation (usually counter-clockwise is defined as positive) and stick to it for all variables ($\theta$, $\omega$, and $\alpha$).
3. **Non-constant Acceleration:** If $\alpha$ is not constant (i.e., it is a function of time), the kinematic equations above are invalid. In such cases, you must use calculus to integrate or differentiate:
   $$\omega(t) = \omega_0 + \int_{0}^{t} \alpha(t') dt'$$
   $$\theta(t) = \theta_0 + \int_{0}^{t} \omega(t') dt'$$

For more complex rotational motion problems, it is often necessary to bridge the gap between rotational and linear motion. See the notes on [[Connecting Linear and Rotational Motion]] for details on tangential acceleration, centripetal acceleration, and how they relate to angular variables.