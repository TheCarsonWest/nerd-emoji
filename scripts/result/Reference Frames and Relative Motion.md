
# [[AP Physics C Home]]
# AP Physics C - Topic 1.4: Reference Frames and Relative Motion

In physics, understanding motion often depends on the chosen **reference frame**. A reference frame is essentially a coordinate system used by an observer to measure the position, velocity, and acceleration of an object. The choice of reference frame is crucial because the observed motion can differ significantly from one frame to another. This topic explores how observations of motion are related between different reference frames, particularly when one frame is moving relative to another.

## Types of Reference Frames

There are two primary types of reference frames critical for understanding mechanics:

### [[Inertial vs. Non-Inertial Reference Frames]]
An **inertial reference frame** is one in which Newton's first law (the law of inertia) holds true: an object at rest remains at rest, and an object in motion continues in motion with constant velocity, unless acted upon by a net external force. In such a frame, there are no "fictitious forces" or "pseudo-forces." Examples include a stationary observer on Earth (for many applications) or a spaceship moving at constant velocity in deep space.

A **non-inertial reference frame** is one that is accelerating relative to an inertial reference frame. In a non-inertial frame, objects appear to accelerate without any apparent physical force acting on them. To preserve Newton's laws in these frames, fictitious forces (like centrifugal force or Coriolis force) must be introduced. Examples include a rotating carousel, a car accelerating, or a falling elevator. For most AP Physics C problems involving relative motion, we primarily consider transformations between inertial reference frames.

## Relative Position

Consider two reference frames, A and B, and an object P.
*   $\vec{r}_{P/A}$: position vector of P as measured by an observer in frame A.
*   $\vec{r}_{P/B}$: position vector of P as measured by an observer in frame B.
*   $\vec{r}_{B/A}$: position vector of the origin of frame B as measured by an observer in frame A.

The relationship between these position vectors is given by:

$$ \vec{r}_{P/A} = \vec{r}_{P/B} + \vec{r}_{B/A} $$

This equation is a fundamental vector addition that defines how positions relate between two frames. If frame B's origin is coincident with P's position in frame A, then $ \vec{r}_{B/A} = \vec{r}_{P/A} $.

## Relative Velocity

If the reference frames are in relative motion, we can determine the relative velocity of an object. Taking the time derivative of the relative position equation, and assuming the origin of frame B moves with respect to frame A, we get the **Galilean velocity transformation**:

$$ \frac{d}{dt}(\vec{r}_{P/A}) = \frac{d}{dt}(\vec{r}_{P/B}) + \frac{d}{dt}(\vec{r}_{B/A}) $$

This simplifies to:

$$ \vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A} $$

Where:
*   $\vec{v}_{P/A}$ is the velocity of object P as observed from frame A.
*   $\vec{v}_{P/B}$ is the velocity of object P as observed from frame B.
*   $\vec{v}_{B/A}$ is the velocity of frame B relative to frame A. (This is also the velocity of an observer in B as measured by an observer in A).

**Example:**
Imagine a person (P) walking on a train (B), and the train is moving relative to the ground (A).
*   $\vec{v}_{P/B}$ = velocity of the person relative to the train.
*   $\vec{v}_{B/A}$ = velocity of the train relative to the ground.
*   $\vec{v}_{P/A}$ = velocity of the person relative to the ground.

## Relative Acceleration

Similarly, taking the time derivative of the relative velocity equation yields the **Galilean acceleration transformation**:

$$ \frac{d}{dt}(\vec{v}_{P/A}) = \frac{d}{dt}(\vec{v}_{P/B}) + \frac{d}{dt}(\vec{v}_{B/A}) $$

$$ \vec{a}_{P/A} = \vec{a}_{P/B} + \vec{a}_{B/A} $$

Where:
*   $\vec{a}_{P/A}$ is the acceleration of object P as observed from frame A.
*   $\vec{a}_{P/B}$ is the acceleration of object P as observed from frame B.
*   $\vec{a}_{B/A}$ is the acceleration of frame B relative to frame A.

**Key Point**: For [[Inertial vs. Non-Inertial Reference Frames]], if both frames A and B are inertial (meaning $\vec{v}_{B/A}$ is constant, and thus $\vec{a}_{B/A} = 0$), then the acceleration of the object is the same in both frames:

$$ \vec{a}_{P/A} = \vec{a}_{P/B} $$

This is a fundamental concept in Newtonian mechanics: forces and accelerations are invariant between inertial reference frames. This means that if Newton's laws hold in one inertial frame, they hold in all inertial frames.

## Summary Table of Relative Motion Equations

| Quantity      | Definition                                    | Equation                                      |
| :------------ | :-------------------------------------------- | :-------------------------------------------- |
| **Position**  | Position of P relative to A                   | $\vec{r}_{P/A} = \vec{r}_{P/B} + \vec{r}_{B/A}$ |
| **Velocity**  | Velocity of P relative to A                   | $\vec{v}_{P/A} = \vec{v}_{P/B} + \vec{v}_{B/A}$ |
| **Acceleration** | Acceleration of P relative to A             | $\vec{a}_{P/A} = \vec{a}_{P/B} + \vec{a}_{B/A}$ |

Understanding these transformations is crucial for solving problems involving observers in different states of motion, particularly in situations like projectile motion from moving platforms, or analyzing the motion of objects in flowing fluids. For a deeper dive into vector operations, refer to [[Scalars and Vectors]].