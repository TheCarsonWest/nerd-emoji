# [[AP Physics Home]]
# AP Physics Note Page: Topic 7.2 - Frequency and Period of SHM

This page delves into the fundamental concepts of frequency and period, crucial for understanding Simple Harmonic Motion (SHM). These quantities quantify how often an oscillation repeats and how long it takes for a single cycle.

## I. Defining Frequency and Period

In [[Defining Simple Harmonic Motion (SHM)]], objects oscillate back and forth about an equilibrium position. Frequency ($f$) and Period ($T$) are two key measures of this oscillatory motion.

### A. Period ($T$)
The period is the time it takes for one complete cycle of oscillation.
*   **Units**: Seconds (s)
*   **Conceptual Understanding**: If an object completes 10 oscillations in 5 seconds, its period is 0.5 seconds per oscillation.

### B. Frequency ($f$)
The frequency is the number of complete cycles of oscillation that occur per unit time.
*   **Units**: Hertz (Hz), which is equivalent to cycles per second ($s^{-1}$).
*   **Conceptual Understanding**: If an object completes 10 oscillations in 5 seconds, its frequency is 2 oscillations per second (2 Hz).

## II. Relationship Between Frequency and Period

Frequency and period are inversely related. This means if you know one, you can easily calculate the other.

$
T = \frac{1}{f}
$

$
f = \frac{1}{T}
$

$A$

**Example**: If an object oscillates with a period of 0.25 seconds, its frequency is $f = 1/0.25 = 4 \text{ Hz}$. Conversely, if the frequency is 5 Hz, the period is $T = 1/5 = 0.2 \text{ s}$.

## III. Angular Frequency ($\omega$)

In addition to linear frequency ($f$), [[Representing and Analyzing SHM]] often uses **angular frequency** ($\omega$). It represents the rate of change of the angular position (or phase) of the oscillating object, analogous to angular speed in [[Circular Motion]].

*   **Units**: Radians per second (rad/s)
*   **Relationship**: Angular frequency is directly proportional to linear frequency and inversely proportional to the period:

$
\omega = 2\pi f = \frac{2\pi}{T}
$

The factor $2\pi$ arises because one complete cycle of oscillation corresponds to $2\pi$ radians of angular displacement in the equivalent circular motion.

## IV. Formulas for Specific SHM Systems

The period and frequency of an SHM system are determined by its physical properties.

### A. Mass-Spring System

For a mass ($m$) attached to an ideal spring with spring constant ($k$), undergoing SHM horizontally or vertically:

*   **Period**:
    $
    T = 2\pi\sqrt{\frac{m}{k}}
    $
*   **Frequency**:
    $
    f = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
    $
*   **Angular Frequency**:
    $
    \omega = \sqrt{\frac{k}{m}}
    $
    **Key Insight**: The period and frequency *do not* depend on the amplitude of the oscillation. They depend only on the mass and the [[Spring Forces|spring constant]]. A stiffer spring (larger $k$) leads to a higher frequency and shorter period. A larger mass (larger $m$) leads to a lower frequency and longer period.

### B. Simple Pendulum

For a simple pendulum consisting of a point mass ($m$) suspended by a light string of length ($L$), undergoing small oscillations:

*   **Period**:
    $
    T = 2\pi\sqrt{\frac{L}{g}}
    $
*   **Frequency**:
    $
    f = \frac{1}{2\pi}\sqrt{\frac{g}{L}}
    $
*   **Angular Frequency**:
    $
    \omega = \sqrt{\frac{g}{L}}
    $
    **Key Insight**: For small angles (typically less than 15 degrees), the period and frequency *do not* depend on the mass of the bob or the amplitude of the swing. They depend only on the length of the string and the [[Gravitational Force|acceleration due to gravity]] ($g$). A longer pendulum (larger $L$) leads to a longer period and lower frequency.

### Summary Table

| Quantity        | Symbol | Units  | Definition                               | Mass-Spring Formula  | Simple Pendulum Formula (small angles) |
| :-------------- | :----- | :----- | :--------------------------------------- | :------------------- | :------------------------------------- |
| **Period**      | $T$    | s      | Time for one complete cycle              | $2\pi\sqrt{m/k}$     | $2\pi\sqrt{L/g}$                       |
| **Frequency**   | $f$    | Hz     | Cycles per second                        | $\frac{1}{2\pi}\sqrt{k/m}$ | $\frac{1}{2\pi}\sqrt{g/L}$             |
| **Angular Freq.** | $\omega$ | rad/s  | Radians per second, $2\pi f = 2\pi/T$ | $\sqrt{k/m}$         | $\sqrt{g/L}$                           |