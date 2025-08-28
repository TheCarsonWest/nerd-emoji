# [[AP Stats Home]]
# Carrying Out a Chi-Square Test for Homogeneity or Independence

This page details the mechanics of performing a Chi-Square Test for Homogeneity or Independence, building upon the foundational concepts introduced in [[Setting Up a Chi-Square Test for Homogeneity or Independence]]. These tests are used to determine if there is a statistically significant association between two categorical variables in a single population (independence) or if the distribution of a categorical variable is the same across several populations (homogeneity).

## 1. State Hypotheses

Before carrying out the test, you must have clearly stated your null ($H_0$) and alternative ($H_a$) hypotheses.
*   **For Independence**:
    *   $H_0$: There is no association between the two categorical variables in the population. (The variables are independent.)
    *   $H_a$: There is an association between the two categorical variables in the population. (The variables are not independent.)
*   **For Homogeneity**:
    *   $H_0$: The distribution of the categorical variable is the same for all populations.
    *   $H_a$: The distribution of the categorical variable is not the same for all populations.

## 2. Check Conditions

Before proceeding with calculations, ensure the conditions for a Chi-Square test are met:

1.  **Random**: The data must come from a random sample(s) or a randomized experiment. For homogeneity, samples should be independent.
2.  **10% Condition** ([[Potential Problems with Sampling]]): When sampling without replacement, the sample size(s) should be no more than 10% of the population size(s). This ensures independence of observations.
3.  **Large Expected Counts**: All expected counts must be at least 5. This condition is crucial for the $\chi^2$ distribution to be a good approximation for the sampling distribution of the test statistic. Refer to [[Expected Counts in Two-Way Tables]] for how to calculate these.

## 3. Calculate the Chi-Square Test Statistic

The Chi-Square test statistic measures how far the observed counts deviate from the expected counts, assuming the null hypothesis is true.

The formula for the Chi-Square test statistic is:

$$
\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}
$$

Where:
*   **Observed (O)**: The actual count in each cell of the two-way table.
*   **Expected (E)**: The count expected in each cell if $H_0$ were true.

You will sum this value for *every cell* in the two-way table.

## 4. Determine Degrees of Freedom (df)

The degrees of freedom for a Chi-Square test involving a two-way table with $r$ rows and $c$ columns is:

$$
df = (r-1)(c-1)
$$

Where:
*   $r$ = number of rows in the two-way table.
*   $c$ = number of columns in the two-way table.

## 5. Find the P-value

The P-value is the probability of observing a Chi-Square test statistic as extreme as, or more extreme than, the one calculated, assuming the null hypothesis is true. For Chi-Square tests, this is always a right-tailed test.

You can find the P-value using:
*   **Chi-Square Table**: Look up your calculated $\chi^2$ value in a Chi-Square distribution table using your degrees of freedom. This will give a range for the P-value.
*   **Calculator/Statistical Software**: Most graphing calculators (e.g., TI-83/84) have a `chi2cdf` function or a dedicated Chi-Square test feature that will compute the P-value directly.

A smaller P-value indicates stronger evidence against $H_0$. Refer to [[Interpreting p-Values]] for more details.

## 6. Make a Decision and Conclusion

Compare the P-value to a pre-determined significance level ($\alpha$, commonly 0.05).

*   **If P-value $\le \alpha$**: Reject the null hypothesis ($H_0$).
    *   **Conclusion**: There is convincing evidence that there is an association between the two categorical variables (for independence) OR that the distribution of the categorical variable is not the same across the populations (for homogeneity).
*   **If P-value $> \alpha$**: Fail to reject the null hypothesis ($H_0$).
    *   **Conclusion**: There is not convincing evidence that there is an association between the two categorical variables (for independence) OR that the distribution of the categorical variable is not the same across the populations (for homogeneity).

Remember to state your conclusion in the context of the problem, referencing the specific variables or populations involved.

### Example Summary Table for Carrying Out the Test

| Step                               | Description                                                                                                                                                                             |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Hypotheses**                  | State $H_0$ (no association/same distribution) and $H_a$ (association/different distribution) in context.                                                                              |
| **2. Conditions**                  | Verify Random, 10% Condition, and Large Expected Counts (all $E \ge 5$).                                                                                                              |
| **3. Calculations (Test Statistic)** | Compute $\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}$.                                                                                                 |
| **4. Degrees of Freedom (df)**     | Calculate $df = (r-1)(c-1)$.                                                                                                                                                            |
| **5. P-value**                     | Find the probability of getting a $\chi^2$ value as extreme or more extreme than the observed $\chi^2$ using the $\chi^2$ distribution with the appropriate $df$.                         |
| **6. Conclusion**                  | Compare P-value to $\alpha$. Reject or Fail to Reject $H_0$. State conclusion in context, linking back to the hypotheses and the strength of evidence.                                  |

This structured approach ensures all necessary components of a Chi-Square test for homogeneity or independence are addressed. Also, be mindful of [[Potential Errors When Performing Tests]] such as Type I or Type II errors when making your final conclusion.