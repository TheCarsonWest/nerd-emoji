# [[AP Stats Home]]
# Conditional Probability

Conditional probability is a fundamental concept in [[Introduction to Probability]] that helps us understand how the likelihood of an event changes when we know that another event has already occurred. It's about narrowing down our sample space based on new information.

## Definition

[[Conditional Probability]] measures the probability of an event (let's call it A) occurring, *given that* another event (let's call it B) has already occurred. The information that event B has occurred changes the sample space of possible outcomes, potentially altering the probability of event A.

## Notation and Formula

The conditional probability of event A given event B is denoted as $P(A|B)$.
The formula for conditional probability is:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

where:
*   $P(A|B)$ is the probability of event A occurring given that event B has occurred.
*   $P(A \cap B)$ is the probability that both event A and event B occur (their intersection).
*   $P(B)$ is the probability that event B occurs.

**Important Note**: This formula is only valid when $P(B) > 0$. If $P(B) = 0$, then event B is impossible, and we cannot condition on an impossible event.

Similarly, if we want to find the probability of B given A, the formula is:

$$
P(B|A) = \frac{P(A \cap B)}{P(A)}
$$

## Understanding the Formula

Think of it as revising your sample space. When you know event B has happened, your new "universe" of possible outcomes is just the outcomes where B occurs. Out of those outcomes, you're interested in the ones where A also occurs. Thus, $P(A \cap B)$ represents the part of B where A also happens, and you normalize it by dividing by $P(B)$ to get a probability within this new, reduced sample space.

## Multiplication Rule for Probability

The conditional probability formula can be rearranged to find the probability of the intersection of two events:

$$
P(A \cap B) = P(A|B) \cdot P(B)
$$

or

$$
P(A \cap B) = P(B|A) \cdot P(A)
$$

This is known as the **General Multiplication Rule**. It's very useful when you know a conditional probability and the probability of the conditioning event.

## Example Scenario

Let's consider a class of 100 students.
*   40 students study Math (M)
*   30 students study Physics (P)
*   10 students study both Math and Physics ($M \cap P$)

We can create a two-way table for this:

|           | Physics (P) | No Physics ($P^c$) | Total |
| :-------- | :---------- | :----------------- | :---- |
| Math (M)  | 10          | 30                 | 40    |
| No Math ($M^c$) | 20          | 40                 | 60    |
| Total     | 30          | 70                 | 100   |

From this, we can calculate probabilities:
*   $P(M) = 40/100 = 0.4$
*   $P(P) = 30/100 = 0.3$
*   $P(M \cap P) = 10/100 = 0.1$

Now, let's find the conditional probability that a student studies Math *given* that they study Physics, $P(M|P)$:

$$
P(M|P) = \frac{P(M \cap P)}{P(P)} = \frac{0.1}{0.3} = \frac{1}{3} \approx 0.333
$$

This means that among the students who study Physics (our new sample space of 30 students), 10 of them also study Math. So, $10/30 = 1/3$.

## Conditional Probability and Independence

Conditional probability plays a crucial role in understanding [[Independent Events and Unions of Events]]. Two events A and B are considered independent if the occurrence of one does not affect the probability of the other.

Mathematically, A and B are independent if:
*   $P(A|B) = P(A)$ (knowing B occurred doesn't change A's probability)
*   $P(B|A) = P(B)$ (knowing A occurred doesn't change B's probability)
*   $P(A \cap B) = P(A) \cdot P(B)$ (this is the Multiplication Rule for Independent Events)

If these conditions are not met, the events are dependent. In our example above, $P(M|P) \approx 0.333$ and $P(M) = 0.4$. Since $P(M|P) \ne P(M)$, studying Math and Physics are **dependent events**.