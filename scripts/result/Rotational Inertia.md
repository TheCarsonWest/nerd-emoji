
# [[AP Physics C Home]]
# 5.4 Rotational Inertia

Rotational inertia, also known as the moment of inertia ($I$), is the rotational analog of mass. It represents an object’s resistance to changes in its angular velocity. While mass tells us how hard it is to change an object's linear motion, rotational inertia tells us how hard it is to change an object's rotation about a specific axis.

## Definition and Formula

For a point mass $m$ rotating at a distance $r$ from an axis of rotation, rotational inertia is defined as:

$$I=mr^2$$

For a system of multiple point masses, the total rotational inertia is simply the sum of the individual moments of inertia:

$$I_{total}=\sum m_i r_i^2$$

For continuous rigid bodies, we calculate the rotational inertia using calculus by integrating over the mass distribution:

$$I=\int r^2 dm$$

[[Calculating Rotational Inertia via Integration]]

## Moments of Inertia for Common Objects

The rotational inertia of an object depends not just on its mass, but on how that mass is distributed relative to the axis of rotation. Objects with mass concentrated further from the axis of rotation have larger rotational inertia.

| Object | Axis of Rotation | Moment of Inertia ($I$) |
| :--- | :--- | :--- |
| Hoop (thin ring) | Central axis | $I=MR^2$ |
| Solid Cylinder/Disk | Central axis | $I=\frac{1}{2}MR^2$ |
| Solid Sphere | Center | $I=\frac{2}{5}MR^2$ |
| Thin Rod | Center of mass | $I=\frac{1}{12}ML^2$ |
| Thin Rod | End | $I=\frac{1}{3}ML^2$ |

## The Parallel Axis Theorem

If you know the rotational inertia of an object about its center of mass ($I_{cm}$), you can find its rotational inertia about any parallel axis displaced by a distance $d$ using the **Parallel Axis Theorem**:

$$I=I_{cm}+Md^2$$

This theorem is incredibly useful for solving complex rotational problems where the axis of rotation is not located at the object's center of mass.

## Significance in Rotational Motion

Rotational inertia appears as a critical term in the dynamic equations of rotational motion. It is the factor that relates torque to angular acceleration, a relationship analogous to Newton’s Second Law ($F=ma$):

$$\tau_{net}=I\alpha$$

[[Newtons Second Law in Rotational Form]]

Furthermore, rotational inertia determines the amount of energy stored in a rotating object:

$$K_{rot}=\frac{1}{2}I\omega^2$$

[[Rotational Kinetic Energy]]

Understanding how rotational inertia changes (for instance, a figure skater pulling in their arms) is essential for grasping concepts like the [[Conservation of Angular Momentum]]. By decreasing their effective radius ($r$), they decrease their rotational inertia ($I$), which forces an increase in angular velocity ($\omega$) to conserve angular momentum.