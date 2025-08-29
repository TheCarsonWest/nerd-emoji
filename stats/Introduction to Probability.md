# [[AP Stats Home]]
# AP Statistics: Introduction to Probability

Probability is the language of randomness. It provides a mathematical framework for quantifying the likelihood of events occurring in situations where the outcome is uncertain. In AP Statistics, we use probability to understand, describe, and make inferences about populations based on samples.

---

## What is Probability?

Probability is a numerical measure of the likelihood that an event will occur. It is always a value between 0 and 1, inclusive.
*   A probability of 0 means the event will never occur.
*   A probability of 1 means the event will always occur.
*   A probability of 0.5 means the event is equally likely to occur or not occur.

Randomness in statistics refers to a phenomenon where individual outcomes are uncertain, but there is a regular distribution of outcomes in a large number of repetitions.

---

## Key Terminology

To discuss probability effectively, we need to define some fundamental terms:

*   **Experiment (or Chance Process)**: Any activity or process that has two or more possible outcomes, where there is uncertainty about which outcome will occur.
    *   *Example*: Flipping a coin, rolling a die, drawing a card from a deck.
*   **Outcome**: A single possible result of an experiment.
    *   *Example*: Getting a "Heads" when flipping a coin, rolling a "3" on a die.
*   **Sample Space ($S$)**: The set of all possible outcomes of an experiment.
    *   *Example*: For a coin flip, $S = \{ \text{Heads, Tails} \}$. For rolling a 6-sided die, $S = \{ 1, 2, 3, 4, 5, 6 \}$.
*   **Event**: A subset of the sample space; a collection of one or more outcomes. Events are usually denoted by capital letters (A, B, C, etc.).
    *   *Example*: Event A = "getting an even number" when rolling a die. $A = \{ 2, 4, 6 \}$.

---

## Basic Rules of Probability

The following rules form the foundation for all probability calculations:

1.  **Probability Range**: For any event $A$, the probability $P(A)$ must satisfy:
    $$0 \le P(A) \le 1$$
2.  **Sum of Probabilities**: The sum of the probabilities of all possible outcomes in the sample space must be 1.
    $$ \sum_{\text{all outcomes}} P(\text{outcome}) = 1 $$
    *   For example, if $S = \{ o_1, o_2, \dots, o_n \}$, then $P(o_1) + P(o_2) + \dots + P(o_n) = 1$.
3.  **Complement Rule**: The probability that an event A does not occur (denoted as $A^c$ or $\text{A'}$) is 1 minus the probability that A does occur.
    $$ P(A^c) = 1 - P(A) $$
    *   *Example*: If the probability of rain is $P(\text{Rain}) = 0.3$, then the probability of no rain is $P(\text{No Rain}) = 1 - 0.3 = 0.7$.
4.  **Addition Rule for Mutually Exclusive Events**: If two events A and B are [[Mutually Exclusive Events]] (meaning they cannot occur at the same time, i.e., $P(A \text{ and } B) = 0$), then the probability that A or B occurs is the sum of their individual probabilities.
    $$ P(A \text{ or } B) = P(A) + P(B) $$
    *   *Example*: When rolling a die, the event "rolling a 2" and "rolling a 4" are mutually exclusive. $P(2 \text{ or } 4) = P(2) + P(4) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$.

---

## Calculating Probability

There are primarily two ways to think about calculating probabilities:

### 1. Theoretical Probability (Equally Likely Outcomes)

If all outcomes in a sample space are equally likely, the probability of an event A is given by:
$$ P(A) = \frac{\text{Number of outcomes in event A}}{\text{Total number of outcomes in the sample space}} $$
*   *Example*: What is the probability of rolling an even number on a fair 6-sided die?
    *   Sample Space $S = \{1, 2, 3, 4, 5, 6\}$, so total outcomes = 6.
    *   Event A = "even number" = $\{2, 4, 6\}$, so number of outcomes in A = 3.
    *   $P(A) = \frac{3}{6} = \frac{1}{2} = 0.5$.

### 2. Empirical Probability (Relative Frequency)

This type of probability is based on observations from an experiment or simulation.
$$ P(A) \approx \frac{\text{Number of times event A occurs}}{\text{Total number of trials}} $$
As the number of trials increases, the empirical probability approaches the theoretical probability. This concept is formalized by the [[The Law of Large Numbers]].
*   *Example*: If you flip a coin 100 times and get 53 heads, the empirical probability of heads is $53/100 = 0.53$. If you flip it 10,000 times and get 4980 heads, the empirical probability is $4980/10000 = 0.498$.

For more on using simulations to estimate probabilities, see [[Estimating Probabilities Using Simulation]].

---

## The Law of Large Numbers

[[The Law of Large Numbers]] states that as the number of repetitions of a chance process increases, the proportion of times a specific outcome occurs approaches its true probability. This is why empirical probability becomes a good estimate of theoretical probability over many trials.

---

## Visualizing Probabilities

Visual tools like Venn diagrams are helpful for understanding relationships between events.

| **Event Relationship**          | **Venn Diagram Representation** |
| :------------------------------ | :------------------------------ |
| Event A                         | Circle A                        |
| Not A ($A^c$)                   | Area outside Circle A           |
| A and B ($A \cap B$)            | Overlap of Circle A and B       |
| A or B ($A \cup B$)             | Combined area of Circle A and B |

---

This introduction lays the groundwork for understanding more complex probability concepts such as [[Conditional Probability]], [[Independent Events and Unions of Events]], and the behavior of [[Random Variables]].