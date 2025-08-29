# [[AP Stats Home]]
# Setting Up a Chi-Square Test for Homogeneity or Independence

Chi-square tests for homogeneity or independence are powerful tools used to analyze relationships between two categorical variables. While similar in their calculations, they differ fundamentally in their experimental design and the conclusions they allow us to draw.

## [[Chi-Square Test for Homogeneity vs. Independence]]

The distinction between a test for homogeneity and a test for independence lies in the sampling method:

*   **Test for Homogeneity:** Used when you have **two or more independent random samples**, each taken from a different population or treatment group, and you want to see if the distribution of a single categorical variable is the same across those populations/groups.
    *   **Example:** Comparing the distribution of preferred social media platforms (categorical variable) among college students (Population 1) vs. high school students (Population 2). Here, we sample independently from two pre-defined populations.
*   **Test for Independence:** Used when you have **a single random sample** from a population, and you want to assess if there's an association or relationship between two categorical variables within that population.
    *   **Example:** Taking a single random sample of adults and asking them about their education level (Categorical Variable 1) and their political affiliation (Categorical Variable 2). We want to see if these two variables are associated.

Despite their different purposes, the mechanics of setting up and carrying out the test (hypotheses, conditions, calculations) are largely identical once the data is organized into a two-way table.

## Hypotheses

For both tests, the null and alternative hypotheses are stated as follows:

*   **Null Hypothesis ($H_0$):**
    *   **For Homogeneity:** There is no difference in the distribution of the categorical variable across the populations/groups. (i.e., The distributions are homogeneous.)
    *   **For Independence:** The two categorical variables are independent in the population. (i.e., There is no association between them.)
*   **Alternative Hypothesis ($H_a$):**
    *   **For Homogeneity:** There is a difference in the distribution of the categorical variable across the populations/groups. (i.e., The distributions are not homogeneous.)
    *   **For Independence:** The two categorical variables are not independent in the population. (i.e., There is an association between them.)

Note: The alternative hypothesis is always non-directional. We are simply testing for *any* difference or association.

## Conditions for Inference

Before performing a chi-square test, certain conditions must be met:

1.  **Random Condition:**
    *   **For Homogeneity:** The data must come from two or more independent random samples or randomized experiments.
    *   **For Independence:** The data must come from a single random sample.
2.  **Large Counts (Expected Counts) Condition:** All expected counts must be at least 5. This condition ensures that the chi-square distribution is a good approximation for the sampling distribution of the test statistic.
3.  **Independent Observations Condition:**
    *   When sampling without replacement, the sample size(s) should be less than 10% of the population size(s) (i.e., $n \le 0.10N$). This ensures that individual observations are independent.

## Observed and Expected Counts

Data for these tests are organized into a [[Two-Way Table]] of **observed counts**. The core idea of the chi-square test is to compare these observed counts to the **expected counts** – what we would expect to see if the null hypothesis were true.

The formula for calculating an expected count in any cell of a two-way table is:

$$
\text{Expected Count} = \frac{(\text{Row Total}) \times (\text{Column Total})}{\text{Grand Total}}
$$

Let's illustrate with an example:

|             | Category 1 | Category 2 | Total |
| :---------- | :--------- | :--------- | :---- |
| Group A     | 25         | 75         | 100   |
| Group B     | 30         | 70         | 100   |
| **Total**   | **55**     | **145**    | **200** |

To find the expected count for Group A and Category 1:
$$
E_{\text{Group A, Cat 1}} = \frac{(\text{Row Total for Group A}) \times (\text{Column Total for Cat 1})}{\text{Grand Total}} = \frac{100 \times 55}{200} = 27.5
$$

[[Expected Counts in Two-Way Tables]] are crucial for calculating the chi-square test statistic.

## The Chi-Square Test Statistic

The chi-square test statistic ($\chi^2$) measures the overall difference between the observed and expected counts. A larger $\chi^2$ value indicates greater discrepancy and stronger evidence against the null hypothesis.

The formula is:

$$
\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}
$$

Where the sum is taken over all cells in the two-way table.

## Degrees of Freedom

The degrees of freedom (df) for a chi-square test for homogeneity or independence are calculated as:

$$
df = (\text{number of rows} - 1) \times (\text{number of columns} - 1)
$$

These degrees of freedom are used to determine the shape of the chi-square distribution and ultimately to find the p-value.

Once these steps are completed, you would proceed to [[Carrying Out a Chi-Square Test for Homogeneity or Independence]] to calculate the p-value and draw a conclusion.