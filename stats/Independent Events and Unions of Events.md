# [[AP Stats Home]]
# Independent Events and Unions of Events

Understanding how events relate to each other and how to calculate the probability of their combined occurrences is fundamental in AP Statistics. This page will cover the definitions, conditions, and rules for independent events and unions of events. For a general overview of probability, refer to [[Introduction to Probability]].

## Independent Events

Two events are **independent** if the occurrence of one does not affect the probability of the other occurring. This concept is distinct from [[Mutually Exclusive Events]]. While mutually exclusive events cannot happen at the same time, independent events can.

### Conditions for Independence

There are several ways to define or test for independence between two events, A and B:

1.  **Conditional Probability Definition**:
    Events A and B are independent if the probability of A occurring, given that B has already occurred, is simply the probability of A.
    $$ P(A|B) = P(A) $$
    Similarly,
    $$ P(B|A) = P(B) $$
    If these conditions hold, then A and B are independent. Otherwise, they are dependent. For more on this, see [[Conditional Probability]].

2.  **Multiplication Rule for Independent Events**:
    Events A and B are independent if and only if the probability that both A and B occur is the product of their individual probabilities.
    $$ P(A \text{ and } B) = P(A) \cdot P(B) $$
    This is often used as a test for independence. If $P(A \text{ and } B) \neq P(A) \cdot P(B)$, then the events are dependent.
    This rule can be extended to more than two independent events. For instance, for three independent events A, B, and C:
    $$ P(A \text{ and } B \text{ and } C) = P(A) \cdot P(B) \cdot P(C) $$

### Example of Independent Events

Consider rolling a fair six-sided die twice.
*   Let event A be "rolling a 4 on the first roll."
*   Let event B be "rolling an odd number on the second roll."

The outcome of the first roll does not affect the outcome of the second roll. Thus, A and B are independent.
$P(A) = 1/6$
$P(B) = 3/6 = 1/2$
The probability of both occurring is $P(A \text{ and } B) = P(A) \cdot P(B) = (1/6) \cdot (1/2) = 1/12$.

## Unions of Events

The **union of two events** A and B, denoted as $A \cup B$ (read as "A or B"), is the event that A occurs, or B occurs, or both occur.

### General Addition Rule

The probability of the union of any two events A and B is given by the General Addition Rule:
$$ P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B) $$
The term $P(A \text{ and } B)$ is subtracted because the outcomes where both A and B occur are counted twice (once in $P(A)$ and once in $P(B)$).

### Addition Rule for Mutually Exclusive Events

If events A and B are [[Mutually Exclusive Events]], they cannot occur at the same time, meaning $P(A \text{ and } B) = 0$. In this special case, the General Addition Rule simplifies to:
$$ P(A \text{ or } B) = P(A) + P(B) $$

### Example of Union of Events

Consider drawing a single card from a standard 52-card deck.
*   Let event A be "drawing a King." ($P(A) = 4/52 = 1/13$)
*   Let event B be "drawing a Spade." ($P(B) = 13/52 = 1/4$)
*   Let event ($A \text{ and } B$) be "drawing a King of Spades." ($P(A \text{ and } B) = 1/52$)

The probability of drawing a King or a Spade is:
$$ P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13} $$

## Summary Table: Independence vs. Mutually Exclusive

It is crucial to distinguish between independent and mutually exclusive events.

| Feature                 | Independent Events                        | Mutually Exclusive Events                   |
| :---------------------- | :---------------------------------------- | :------------------------------------------ |
| **Definition**          | Occurrence of one doesn't affect other.   | Cannot occur at the same time.              |
| **$P(A \text{ and } B)$** | $P(A) \cdot P(B)$                         | $0$                                         |
| **$P(A \text{ or } B)$** | $P(A) + P(B) - P(A) \cdot P(B)$           | $P(A) + P(B)$                               |
| **Can they both happen?** | Yes, if $P(A) > 0$ and $P(B) > 0$.      | No.                                         |
| **Example**             | Flipping a coin twice, getting heads both times. | Rolling a die, getting a 1 and a 6.         |
| **Formal relationship** | $P(A|B) = P(A)$                           | If $P(A) > 0$ and $P(B) > 0$, then $P(A|B) = 0$. |