# [[AP Physics Home]]
# AP Physics: Topic 1.4 - Reference Frames and Relative Motion

This section explores how an object's motion is observed differently depending on the observer's own motion. Understanding reference frames is fundamental to accurately describing and analyzing physical phenomena.

## What is a Reference Frame?

A **reference frame** is a coordinate system or set of axes relative to which observations and measurements of physical quantities (like position, velocity, and acceleration) are made. It consists of an origin point and a set of directions.

*   **Inertial Reference Frame:** A reference frame that is either at rest or moving with a constant velocity. In an inertial frame, [[Newton’s First Law]] (and thus [[Newton’s Second Law]]) holds true without the need for fictitious forces.
*   **Non-Inertial Reference Frame:** A reference frame that is accelerating. In such a frame, fictitious forces (e.g., centrifugal force, Coriolis force) appear to act on objects to make Newton's laws appear to hold. For AP Physics 1, we primarily deal with inertial reference frames.

## Relative Position

The position of an object is always relative to the origin of the chosen reference frame. If you're on a train, your position relative to the train is constant, but your position relative to the ground is changing.

## Relative Velocity

Relative velocity describes how the velocity of an object is perceived from different reference frames. It's crucial for understanding how observers in motion see other objects moving.

Consider two reference frames: A and B. We want to find the velocity of an object (O) as observed from frame A ($\vec{v}_{O/A}$).

The general formula for relative velocity is:

$
\vec{v}_{O/A} = \vec{v}_{O/B} + \vec{v}_{B/A}
$

Where:
*   $\vec{v}_{O/A}$: Velocity of object O as observed from reference frame A.
*   $\vec{v}_{O/B}$: Velocity of object O as observed from reference frame B.
*   $\vec{v}_{B/A}$: Velocity of reference frame B as observed from reference frame A.

**Key Relationship:** The velocity of frame A with respect to B is the negative of the velocity of frame B with respect to A:
$
\vec{v}_{A/B} = -\vec{v}_{B/A}
$

**Example Scenario:**
Imagine a person (P) walking on a moving train (T), which itself is moving relative to the ground (G).
*   $\vec{v}_{P/T}$: Velocity of the person relative to the train (e.g., 2 m/s forward).
*   $\vec{v}_{T/G}$: Velocity of the train relative to the ground (e.g., 10 m/s forward).
*   $\vec{v}_{P/G}$: Velocity of the person relative to the ground.

Using the relative velocity formula:
$
\vec{v}_{P/G} = \vec{v}_{P/T} + \vec{v}_{T/G}
$
If both velocities are in the same direction, $\vec{v}_{P/G} = 2 \text{ m/s} + 10 \text{ m/s} = 12 \text{ m/s}$.
If the person walks opposite to the train's motion, $\vec{v}_{P/G} = -2 \text{ m/s} + 10 \text{ m/s} = 8 \text{ m/s}$.

### Components of Relative Velocity

In two dimensions, relative velocity problems often involve [[Vectors and Motion in Two Dimensions]]. You'll typically break down each velocity vector into its x and y components.

Let $\vec{v}_{O/A} = v_{O/A,x}\hat{i} + v_{O/A,y}\hat{j}$, and similarly for the other terms.
Then:
$
v_{O/A,x} = v_{O/B,x} + v_{B/A,x}
$
$
v_{O/A,y} = v_{O/B,y} + v_{B/A,y}
$

## Relative Acceleration

Similar to velocity, acceleration is also relative to the chosen reference frame. For objects moving in different inertial reference frames, the acceleration of an object remains the same if the relative velocity between the frames is constant.

If frame B is moving at a constant velocity with respect to frame A ($\vec{v}_{B/A} = \text{constant}$), then $\vec{a}_{B/A} = 0$.
In this case, the acceleration of object O observed from A ($\vec{a}_{O/A}$) is equal to the acceleration of object O observed from B ($\vec{a}_{O/B}$):

$
\vec{a}_{O/A} = \vec{a}_{O/B} + \vec{a}_{B/A}
$

If $\vec{a}_{B/A} = 0$ (i.e., B is an inertial frame relative to A), then:
$
\vec{a}_{O/A} = \vec{a}_{O/B}
$

This means that observers in different inertial frames will agree on the acceleration of an object, even if they disagree on its velocity. This principle is fundamental to [[Newton’s Second Law]] and is why inertial frames are so important.

## Common Scenarios & Problem Types

| Scenario                       | Description                                                                     | Key Application                                     |
| :----------------------------- | :------------------------------------------------------------------------------ | :-------------------------------------------------- |
| [[Boat Crossing a River]]      | A boat moving relative to water, water moving relative to the ground.             | Vector addition for determining resultant velocity. |
| Airplane in Wind               | An airplane moving relative to air, air moving relative to the ground.            | Similar to boat/river; finding ground speed/direction. |
| Two Moving Objects             | Calculating the velocity of one car/person relative to another.                 | Direct application of $\vec{v}_{A/B} = \vec{v}_{A/G} - \vec{v}_{B/G}$. |

[[Boat Crossing a River]] is a classic example of applying relative velocity concepts in two dimensions, often involving trigonometry to resolve vectors.