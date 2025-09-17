# [[AP Stats Home]]
# Statistics for Two Categorical Variables

When we analyze two categorical variables, our goal often extends beyond just representing their relationship (as discussed in [[Representing Two Categorical Variables]]) to making inferences about whether a relationship exists in the population, or if the distribution of one variable is different across categories of another. This typically involves [[Chi-Square Tests]].

## Types of Relationships

There are two primary questions we ask when dealing with two categorical variables in an inferential context:

1.  **Association/Independence**: Is there an association between the two variables, or are they independent? This is addressed by a **Chi-Square Test for Independence**.
2.  **Homogeneity**: Is the distribution of one categorical variable the same across different populations or groups defined by the other categorical variable? This is addressed by a **Chi-Square Test for Homogeneity**.

While these tests are conceptually distinct, their calculation and interpretation are often very similar.

## Observed vs. Expected Counts

The core idea behind inferential tests for two categorical variables is comparing the observed counts in a two-way table to the counts we would expect if there were no association (i.e., if the variables were independent or the distributions were homogeneous).

*   **Observed Counts**: These are the actual frequencies obtained from the sample data, usually displayed in a [[Representing Two Categorical Variables]] (contingency table).

*   **Expected Counts**: These are the counts we would anticipate in each cell of the two-way table if the null hypothesis were true (i.e., if the variables were independent or the distributions were homogeneous).

    The formula for the expected count for a cell is:
    $$
    E = \frac{(\text{row total}) \times (\text{column total})}{\text{grand total}}
    $$
    Understanding and calculating these is crucial for [[Expected Counts in Two-Way Tables]].

## Chi-Square Test Statistic

To quantify the difference between the observed and expected counts, we use the Chi-Square ($\chi^2$) test statistic. This statistic sums up the squared differences between observed and expected counts, weighted by the expected counts, across all cells in the table.

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

Where:
*   $O$ = Observed count for a cell
*   $E$ = Expected count for a cell
*   $\sum$ denotes summing over all cells in the two-way table.

A larger $\chi^2$ value indicates a greater discrepancy between observed and expected counts, suggesting stronger evidence against the null hypothesis of independence or homogeneity.

## Degrees of Freedom

The degrees of freedom (df) for a Chi-Square test for two categorical variables are calculated based on the dimensions of the two-way table:

$$
df = (\text{number of rows} - 1) \times (\text{number of columns} - 1)
$$

The degrees of freedom, along with the calculated $\chi^2$ statistic, are used to find the p-value.

## Performing the Test

The process for conducting a Chi-Square test for homogeneity or independence generally follows the standard hypothesis testing framework:

1.  **State Hypotheses**:
    *   **Null Hypothesis ($H_0$)**: There is no association between the two categorical variables (independence), or the distribution of one variable is the same across all populations/groups (homogeneity).
    *   **Alternative Hypothesis ($H_a$)**: There is an association between the two categorical variables (dependence), or the distribution of one variable is not the same across all populations/groups (heterogeneity).

2.  **Check Conditions**:
    *   **Random Sample/Assignment**: Data must come from a random sample(s) or a randomized experiment.
    *   **Large Sample Size**: All expected counts ($E$) must be at least 5. (This is a common rule of thumb, sometimes slightly relaxed for a small number of cells).
    *   **Independence**: Observations within groups and between groups must be independent.

3.  **Calculate Test Statistic and p-value**: Compute the $\chi^2$ statistic and its corresponding p-value using the degrees of freedom.

4.  **Make a Decision and Conclude**: Compare the p-value to the significance level ($\alpha$) and interpret the results in context.

This full procedure is detailed in [[Setting Up a Chi-Square Test for Homogeneity or Independence]] and [[Carrying Out a Chi-Square Test for Homogeneity or Independence]].

## Choosing the Right Test

The choice between a Chi-Square Test for Independence and a Chi-Square Test for Homogeneity depends on the study design:

*   **Test for Independence**: Used when a single sample is taken, and two categorical variables are measured for each individual (e.g., surveying students about their major and their preferred study method).
*   **Test for Homogeneity**: Used when separate samples are taken from two or more populations/groups, and one categorical variable is measured for each individual in each sample (e.g., taking separate samples of men and women and asking them about their preferred political party).

Despite the conceptual difference in design, the calculations for the $\chi^2$ statistic, degrees of freedom, and p-value are identical for both tests. For more guidance on choosing an appropriate test, refer to [[Selecting an Appropriate Inference Procedure for Categorical]].