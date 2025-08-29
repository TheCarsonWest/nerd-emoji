# [[AP Stats Home]]
# Setting Up a Chi-Square Goodness of Fit Test

The Chi-Square Goodness of Fit test is a powerful statistical tool used to determine if an observed distribution of a [[Categorical Variable]] differs significantly from a hypothesized or expected distribution. Essentially, it helps us decide if a theoretical model fits the data we've collected.

## When to Use It

You should use a Chi-Square Goodness of Fit test when you have:
1.  **A single categorical variable** from a single population.
2.  **Observed counts** for each category of the variable.
3.  **A hypothesized distribution** for the proportion of observations in each category. This hypothesized distribution can come from a theory, a past study, or an assumption of equal proportions across categories.

For example, you might use this test to see if:
*   The proportion of different colored candies in a bag matches the manufacturer's stated proportions.
*   The number of accidents on different days of the week is uniformly distributed.
*   The distribution of blood types in a sample matches known population percentages.

## Hypotheses

Setting up the hypotheses is crucial for any significance test. For a Chi-Square Goodness of Fit test:

*   **Null Hypothesis ($H_0$):** The observed distribution of the categorical variable is consistent with the hypothesized distribution. (i.e., there is no significant difference between observed and expected proportions.)
    *   This is often stated as: $H_0: p_1 = \text{hypothesized } p_1, p_2 = \text{hypothesized } p_2, \ldots, p_k = \text{hypothesized } p_k$
    *   Where $p_i$ represents the true proportion for category $i$, and $k$ is the number of categories.

*   **Alternative Hypothesis ($H_a$):** The observed distribution of the categorical variable is **not** consistent with the hypothesized distribution. (i.e., there is a significant difference between observed and expected proportions for at least one category.)
    *   This is typically stated as: $H_a:$ At least one of the true proportions ($p_i$) is different from its hypothesized value.

It's important to remember that the alternative hypothesis doesn't specify *how* the distributions differ, only that they do.

## Conditions for Inference

Before carrying out the test, you must verify that the following conditions are met. If any condition is violated, the results of the test may not be valid.

1.  **Random Condition:** The data must come from a [[Random Sampling and a Collection]] or a well-designed random experiment. This ensures the sample is representative of the population.

2.  **Independence Condition:**
    *   **Within the sample:** Individual observations must be independent of each other. If sampling without replacement, the population size must be at least 10 times the sample size ($N \ge 10n$).
    *   **Between categories:** The categories of the categorical variable must be mutually exclusive (an observation cannot fall into more than one category).

3.  **Large Counts Condition:** All expected counts must be at least 5. This condition is vital because the chi-square distribution is a continuous distribution, and we are using it to approximate a discrete distribution of counts. If expected counts are too small, this approximation is not reliable.

    *   **Calculating Expected Counts:** For each category, the expected count ($E_i$) is calculated by multiplying the total sample size ($n$) by the hypothesized proportion for that category ($p_i$).
        $$E_i = n \times p_i$$
    *   For example, if you have a sample of 200 candies and hypothesize that 30% are red, the expected count for red candies would be $200 \times 0.30 = 60$.

[[Expected Counts in Chi-Square Tests]]

## Test Statistic

Once the conditions are met, the next step in setting up the test is to understand the test statistic. The Chi-Square test statistic ($\chi^2$) measures how far the observed counts deviate from the expected counts.

The formula for the Chi-Square test statistic is:

$$\chi^2 = \sum \frac{(\text{Observed Count} - \text{Expected Count})^2}{\text{Expected Count}}$$

Where:
*   $\text{Observed Count}$ is the actual number of observations in a particular category.
*   $\text{Expected Count}$ is the number of observations we would expect in that category if the null hypothesis were true.
*   The sum ($\sum$) is taken over all $k$ categories.

A larger $\chi^2$ value indicates a greater discrepancy between the observed and expected distributions, providing stronger evidence against the null hypothesis.

## Degrees of Freedom

The degrees of freedom (df) for a Chi-Square Goodness of Fit test are calculated as:

$$df = \text{number of categories} - 1$$

The degrees of freedom determine the specific shape of the chi-square distribution that will be used to calculate the p-value.

After setting up the hypotheses and checking the conditions, the next step would be [[Carrying Out a Chi-Square Test for Goodness of Fit]].