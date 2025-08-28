# [[AP Stats Home]]
# Estimating Probabilities Using Simulation

Simulation is a powerful tool in statistics used to estimate probabilities for complex events or scenarios that are difficult to calculate analytically. It involves modeling a real-world process using random numbers and then repeating the process many times to observe the outcomes and estimate the likelihood of a particular event. This technique is particularly useful when the underlying probability distribution is unknown or the event's probability depends on a series of uncertain outcomes.

## Why Use Simulation?

We often turn to simulation when:
*   Theoretical calculations are too complex or impossible.
*   It's impractical or costly to perform actual experiments.
*   We want to understand the long-run behavior of a random process.

Simulation provides an approximation of the true probability, which improves with a greater number of trials.

## The Simulation Process

Estimating probabilities using simulation generally follows a structured, multi-step approach:

1.  **Identify the Component of Interest**:
    *   Clearly define the basic random event that is repeated in the situation.
    *   *Example*: Flipping a coin, rolling a die, selecting a person from a group.

2.  **Model the Component with a Random Device**:
    *   Choose a random device (e.g., coin, die, random number generator) that accurately reflects the probability of the component's outcomes.
    *   Assign numbers or outcomes from the random device to represent the actual outcomes of the component.
    *   The assignment must be proportional to the probability of each outcome.
    *   *Example*: If the probability of success is $P(\text{Success}) = 0.60$, use random digits 00-59 for success and 60-99 for failure (using two-digit numbers).

3.  **Define a Trial**:
    *   A trial is one complete repetition of the experiment or scenario being simulated.
    *   It consists of a sequence of random numbers that mimics the event until the outcome of interest is achieved or a specific condition is met.
    *   *Example*: Rolling a die until a 6 appears, or simulating 5 coin flips.

4.  **State the Response Variable**:
    *   Clearly identify what you will measure or count during each trial. This is the outcome you are interested in.
    *   *Example*: The number of rolls needed to get a 6, or the number of heads in 5 flips.

5.  **Run Multiple Trials**:
    *   Repeat the simulation process a large number of times (e.g., 50, 100, 1000 trials).
    *   More trials generally lead to a more accurate estimate due to the [[Law of Large Numbers]].

6.  **Calculate the Estimated Probability**:
    *   Count the number of trials where the event of interest occurred.
    *   The estimated probability is given by:
        $$ P(\text{Event}) \approx \frac{\text{Number of favorable outcomes}}{\text{Total number of trials}} $$

## Example: Simulating a Basketball Player's Free Throws

A basketball player has an 80% free throw percentage. We want to estimate the probability that the player makes at least 3 out of 5 free throws in a game.

**Steps:**

1.  **Component**: A single free throw.
2.  **Random Device**: Use a random number generator (RNG) or a table of random digits.
    *   Let digits 0-7 represent a made free throw (80% chance).
    *   Let digits 8-9 represent a missed free throw (20% chance).
3.  **Trial**: Generate 5 random digits, representing 5 free throws.
4.  **Response Variable**: Count the number of made free throws in each trial. We are interested if this count is 3 or more.
5.  **Run Trials**:
    Let's run 5 trials as an example (in a real simulation, we'd do many more):

    | Trial | Random Digits | Outcomes (M=Make, F=Miss) | Number of Makes | At Least 3 Makes? |
    | :---- | :------------ | :-------------------------- | :-------------- | :---------------- |
    | 1     | 4, 1, 9, 0, 7 | M, M, F, M, M               | 4               | Yes               |
    | 2     | 8, 3, 5, 2, 6 | F, M, M, M, M               | 4               | Yes               |
    | 3     | 0, 2, 0, 1, 9 | M, M, M, M, F               | 4               | Yes               |
    | 4     | 5, 9, 4, 3, 0 | M, F, M, M, M               | 4               | Yes               |
    | 5     | 7, 6, 8, 1, 2 | M, M, F, M, M               | 4               | Yes               |

6.  **Estimate Probability**: In this small example, 5 out of 5 trials resulted in at least 3 makes.
    $$ P(\text{at least 3 makes}) \approx \frac{5}{5} = 1.00 $$
    *Note*: With only 5 trials, this is a very rough estimate. A real simulation would involve hundreds or thousands of trials for a more reliable estimate.

## Connecting to Other Concepts

*   **Probability Distributions**: Simulation can help us understand and visualize [[Introduction to Random Variables and Probability Distributions]] for complex scenarios where direct calculation is hard.
*   **The Binomial Distribution**: The free throw example above could be modeled using the [[Introduction to the Binomial Distribution]] if we wanted to calculate the exact probability analytically, but simulation provides an alternative, especially if the conditions for a binomial distribution weren't perfectly met (e.g., probability of success changing).
*   **[[Sampling Distributions for Sample Proportions]]**: The results from many simulation trials can themselves form a sampling distribution, which is fundamental to inferential statistics.