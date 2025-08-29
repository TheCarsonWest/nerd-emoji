# [[AP Stats Home]]
# Mutually Exclusive Events

## Introduction to Mutually Exclusive Events

In [[Introduction to Probability]], we learned about events and their probabilities. Mutually exclusive events, also known as disjoint events, are a fundamental concept in probability theory. Two events are considered mutually exclusive if they cannot occur at the same time. This means that if one event happens, the other simply cannot.

### Definition
Two events, $A$ and $B$, are **mutually exclusive** (or **disjoint**) if they have no outcomes in common. That is, the occurrence of one event precludes the occurrence of the other.

## Key Characteristics

*   **No Overlap**: Mutually exclusive events never share any common outcomes in the sample space.
*   **Simultaneous Occurrence Impossible**: It is impossible for both events to happen at the same time in a single trial or observation.
*   **Intersection is Empty**: The intersection of two mutually exclusive events is an empty set ($\emptyset$).

### Visualizing Mutually Exclusive Events

Venn diagrams are excellent tools for visualizing relationships between events. For mutually exclusive events, their circles in a Venn diagram will not overlap.

```mermaid
graph TD
    subgraph Sample Space (S)
        A -- (No overlap) --> B
    end
    style A fill:#ADD8E6,stroke:#333,stroke-width:2px
    style B fill:#FFB6C1,stroke:#333,stroke-width:2px
```

*In this diagram, the circles representing Event A and Event B are separate, indicating no common outcomes.*

## Probability of Mutually Exclusive Events

When two events $A$ and $B$ are mutually exclusive, the probability that *both* events occur is 0. This is expressed as:

$$P(A \text{ and } B) = P(A \cap B) = 0$$

### The Addition Rule for Mutually Exclusive Events

For any two events $A$ and $B$, the general addition rule for the probability of their union (the probability that $A$ occurs *or* $B$ occurs *or* both occur) is:

$$P(A \text{ or } B) = P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

However, if $A$ and $B$ are mutually exclusive, we know that $P(A \cap B) = 0$. Therefore, the addition rule simplifies considerably for mutually exclusive events:

$$P(A \text{ or } B) = P(A) + P(B)$$

This simplified rule states that the probability of one or the other mutually exclusive event occurring is simply the sum of their individual probabilities.

**Example:**
Consider rolling a standard six-sided die.
Let event $A$ be rolling an even number {2, 4, 6}. $P(A) = 3/6 = 1/2$.
Let event $B$ be rolling an odd number {1, 3, 5}. $P(B) = 3/6 = 1/2$.

Are $A$ and $B$ mutually exclusive? Yes, you cannot roll a number that is both even and odd simultaneously. The intersection $A \cap B = \emptyset$.
The probability of rolling an even OR an odd number is:
$P(A \text{ or } B) = P(A) + P(B) = 1/2 + 1/2 = 1$. This makes sense, as all outcomes are either even or odd.

## [[Mutually Exclusive vs. Independent Events]]

It is crucial to understand the difference between mutually exclusive events and [[Independent Events and Unions of Events]]. These two concepts are often confused but are almost opposite of each other.

| Feature             | Mutually Exclusive Events                               | Independent Events                                    |
| :------------------ | :------------------------------------------------------ | :---------------------------------------------------- |
| **Definition**      | Cannot occur at the same time ($P(A \cap B) = 0$)       | Occurrence of one does not affect the other ($P(A \cap B) = P(A) \cdot P(B)$) |
| **Overlap in Venn** | No overlap (disjoint)                                   | May or may not overlap, but their relationship is defined by their probabilities |
| **$P(A \cap B)$**   | $0$ (if $A$ and $B$ are not impossible events)           | $P(A) \cdot P(B)$                                     |
| **Can both happen?**| No                                                      | Yes                                                   |

**Key Takeaway**: If two events are mutually exclusive and have non-zero probabilities, they cannot be independent. If $P(A) > 0$ and $P(B) > 0$, and they are mutually exclusive, then $P(A \cap B) = 0$. However, if they were independent, $P(A \cap B)$ would be $P(A) \cdot P(B)$, which would be greater than 0. Since $0 \ne P(A) \cdot P(B)$ (unless one event has a probability of 0), they cannot be both.

The only case where two events can be both mutually exclusive and independent is if at least one of them is an impossible event (i.e., has a probability of 0). This is usually not relevant for typical AP Statistics problems.

## Examples in AP Statistics Context

1.  **Card Deck**:
    *   Event $A$: Drawing a red card.
    *   Event $B$: Drawing a black card.
    *   Are $A$ and $B$ mutually exclusive? Yes, a card cannot be both red and black. $P(A \text{ or } B) = P(A) + P(B) = 26/52 + 26/52 = 1$.
2.  **Survey Data**:
    *   Event $C$: A randomly selected person is a high school student.
    *   Event $D$: A randomly selected person is a college graduate.
    *   Are $C$ and $D$ mutually exclusive? Yes, assuming a person cannot be both at the same time for the purpose of the survey (e.g., they are not simultaneously enrolled in both).

Understanding mutually exclusive events is fundamental for correctly applying the addition rule and for distinguishing between different types of event relationships in probability calculations.