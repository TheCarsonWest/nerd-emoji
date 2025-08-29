# [[AP Stats Home]]
# Potential Errors When Performing Tests

When performing a hypothesis test, our goal is to make a decision about a population parameter based on sample data. However, since we are using sample data, there's always a chance our decision will be incorrect, regardless of how carefully we follow the procedure. These potential errors are a fundamental aspect of statistical inference.

## [[Type I Error]]

A **Type I error** occurs when we **reject a true null hypothesis** ($H_0$). This means we conclude there is a significant effect or difference when, in reality, there isn't one in the population.

*   **Probability of a Type I Error:** Denoted by $\alpha$ (alpha), which is the significance level of the test.
    *   $$P(\text{Type I Error}) = P(\text{Reject } H_0 \text{ | } H_0 \text{ is True}) = \alpha$$
*   **Consequences:** The consequences depend on the context of the problem. For example, if a company concludes a new drug is effective when it isn't, they might invest heavily in a useless product or potentially harm patients.
*   **Controlling Type I Error:** We set the $\alpha$ level (e.g., 0.05 or 0.01) before conducting the test. A smaller $\alpha$ reduces the probability of a Type I error but makes it harder to reject $H_0$. This is discussed further in [[Setting Up a Test for a Population Proportion]].

## [[Type II Error]]

A **Type II error** occurs when we **fail to reject a false null hypothesis** ($H_0$). This means we fail to detect a significant effect or difference that actually exists in the population.

*   **Probability of a Type II Error:** Denoted by $\beta$ (beta).
    *   $$P(\text{Type II Error}) = P(\text{Fail to Reject } H_0 \text{ | } H_0 \text{ is False}) = \beta$$
*   **Consequences:** Failing to detect a real effect can lead to missed opportunities. For example, a company might miss out on a truly effective new drug, or a researcher might overlook a real scientific discovery.
*   **Controlling Type II Error:** Reducing $\beta$ is often achieved by increasing the sample size or increasing the significance level $\alpha$.

## The Relationship Between Type I and Type II Errors

There is an inverse relationship between Type I and Type II errors:
*   If you **decrease $\alpha$** (making it harder to reject $H_0$), you **increase $\beta$** (making it harder to detect a real effect).
*   If you **increase $\alpha$** (making it easier to reject $H_0$), you **decrease $\beta$** (making it easier to detect a real effect).

The choice of $\alpha$ depends on which type of error is considered more serious in a particular context.

## Power of a Test

The **power** of a hypothesis test is the probability of correctly rejecting a false null hypothesis. It is the probability that the test will detect an effect when there actually is an effect.

*   **Calculation:**
    *   $$Power = 1 - \beta$$
*   **Interpretation:** A higher power means a better chance of detecting a real effect.
*   **Factors Affecting Power:**
    1.  **Sample Size:** Increasing the sample size generally increases power (and decreases $\beta$).
    2.  **Significance Level ($\alpha$):** Increasing $\alpha$ increases power (and decreases $\beta$).
    3.  **Effect Size:** The magnitude of the true difference or effect in the population. A larger effect size is easier to detect, thus increasing power.
    4.  **Standard Deviation:** A smaller population standard deviation (less variability) increases power.

## Summary of Decisions and Errors

This table summarizes the possible outcomes of a hypothesis test:

|                        | **Actual State of $H_0$ (in the Population)** |                                                                  |
| :--------------------- | :-------------------------------------------- | :--------------------------------------------------------------- |
| **Decision**           | $H_0$ is True                                 | $H_0$ is False                                                   |
| **Fail to Reject $H_0$** | Correct Decision ($1 - \alpha$)               | Type II Error ($\beta$)                                          |
| **Reject $H_0$**       | Type I Error ($\alpha$)                       | Correct Decision (Power, $1 - \beta$)                           |

Understanding these errors is crucial for interpreting the results of any hypothesis test, as discussed in [[Interpreting p-Values]] and [[Concluding a Test for a Population Proportion]].