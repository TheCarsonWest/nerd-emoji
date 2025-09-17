# [[AP Stats Home]]
# Selecting an Appropriate Inference Procedure for Categorical Data

Choosing the correct inference procedure is a critical step in any statistical analysis. For categorical variables, the decision hinges on the number of populations or groups being compared and the specific research question. This page outlines the primary inference procedures for categorical data encountered in AP Statistics.

## Key Considerations for Categorical Inference

When faced with a problem involving categorical data, ask yourself these fundamental questions:

1.  **How many populations or groups are being compared?**
    *   One population
    *   Two independent populations/groups
    *   Three or more independent populations/groups (or a single population with multiple categories for a goodness-of-fit test)
2.  **What is the goal of the inference?**
    *   Estimating a population parameter (e.g., a proportion or the difference between proportions)? Use a [[Constructing a Confidence Interval for a Population|Confidence Interval]].
    *   Testing a claim about a population parameter or a relationship between variables? Use a [[Setting Up a Test for a Population Proportion|Hypothesis Test]].
3.  **Is the data collected from a single sample with multiple categories, or multiple samples each with two categories?** This distinction is crucial for Chi-Square tests.

---

## Inference for One Population Proportion

**Goal:** To estimate or test a claim about a single population proportion ($p$).
**Procedure:**
*   **Confidence Interval:** One-sample $z$-interval for $p$.
    $$ \hat{p} \pm z^* \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} $$
*   **Hypothesis Test:** One-sample $z$-test for $p$.
    $$ z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} $$
**Conditions:**
*   **Random:** Data come from a random sample or randomized experiment.
*   **Normal (Large Counts):** The number of successes ($n\hat{p}$) and failures ($n(1-\hat{p})$) are both at least 10 (for intervals) or $np_0 \ge 10$ and $n(1-p_0) \ge 10$ (for tests).
*   **Independence (10% Condition):** The sample size $n$ is no more than 10% of the population size $N$ ($n \le 0.10N$).

**Links:** [[Constructing a Confidence Interval for a Population Proportion]], [[Setting Up a Test for a Population Proportion]]

---

## Inference for Two Population Proportions

**Goal:** To estimate or test a claim about the difference between two population proportions ($p_1 - p_2$).
**Procedure:**
*   **Confidence Interval:** Two-sample $z$-interval for $p_1 - p_2$.
    $$ (\hat{p_1} - \hat{p_2}) \pm z^* \sqrt{\frac{\hat{p_1}(1-\hat{p_1})}{n_1} + \frac{\hat{p_2}(1-\hat{p_2})}{n_2}} $$
*   **Hypothesis Test:** Two-sample $z$-test for $p_1 - p_2$.
    $$ z = \frac{(\hat{p_1} - \hat{p_2}) - 0}{\sqrt{\hat{p}_c(1-\hat{p}_c)\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}} $$
    where $\hat{p}_c = \frac{X_1 + X_2}{n_1 + n_2}$ is the pooled proportion.
**Conditions:**
*   **Random:** Two independent random samples or two groups in a randomized experiment.
*   **Normal (Large Counts):** The number of successes and failures for *each* group are both at least 10.
*   **Independence (10% Condition):** Each sample size is no more than 10% of its respective population size ($n_1 \le 0.10N_1$ and $n_2 \le 0.10N_2$).

**Links:** [[Justifying a Claim Based on a Confidence Interval for a Difference of Population Proportions]], [[Setting Up a Test for the Difference of Two Population Proportions]]

---

## Chi-Square Tests

Chi-square ($\chi^2$) tests are used when dealing with counts of categorical data, particularly when comparing three or more groups or categories, or investigating relationships between two categorical variables.

### [[Chi-Square Goodness of Fit Test]]

**Goal:** To determine if the observed distribution of a single categorical variable across several categories matches an expected distribution.
**Hypotheses:**
*   $H_0$: The observed distribution matches the hypothesized distribution.
*   $H_a$: The observed distribution does not match the hypothesized distribution.
**Test Statistic:**
$$ \chi^2 = \sum \frac{(Observed - Expected)^2}{Expected} $$
**Degrees of Freedom:** $df = \text{number of categories} - 1$.
**Conditions:**
*   **Random:** Data come from a random sample.
*   **Expected Counts:** All expected counts are at least 5.
*   **Independence (10% Condition):** The sample size $n$ is no more than 10% of the population size $N$.

**Links:** [[Setting Up a Chi-Square Goodness of Fit Test]], [[Carrying Out a Chi-Square Test for Goodness of Fit]]

### [[Chi-Square Test for Homogeneity or Independence]]

These tests use the same statistic and conditions but address slightly different questions, often distinguished by how the data were collected (sampling design). Both involve analyzing [[Expected Counts in Two-Way Tables]].

**1. Chi-Square Test for Homogeneity**
**Goal:** To determine if the distribution of a categorical variable is the same across several different populations or groups. Often used when comparing multiple groups from independent samples.
**Hypotheses:**
*   $H_0$: The distribution of the categorical variable is the same for all populations/groups.
*   $H_a$: The distribution of the categorical variable is not the same for all populations/groups.

**2. Chi-Square Test for Independence**
**Goal:** To determine if there is an association or relationship between two categorical variables within a single population. Often used with data from a single random sample where two categorical variables are measured for each individual.
**Hypotheses:**
*   $H_0$: There is no association between the two categorical variables (they are independent).
*   $H_a$: There is an association between the two categorical variables (they are not independent).

**Test Statistic (for both homogeneity and independence):**
$$ \chi^2 = \sum \frac{(Observed - Expected)^2}{Expected} $$
**Degrees of Freedom:** $df = (\text{number of rows} - 1)(\text{number of columns} - 1)$.
**Conditions:**
*   **Random:** Data come from a random sample (independence) or multiple independent random samples (homogeneity).
*   **Expected Counts:** All expected counts are at least 5.
*   **Independence (10% Condition):** For an independence test, the sample size $n$ is no more than 10% of the population size $N$. For a homogeneity test, each sample size is no more than 10% of its respective population size.

**Links:** [[Setting Up a Chi-Square Test for Homogeneity or Independence]], [[Carrying Out a Chi-Square Test for Homogeneity or Independence]]

---

## Summary Table for Categorical Inference Procedures

| Number of Populations/Groups | Goal & Question Type                                      | Procedure                                          | Conditions                                                                                                                                                                                                                                                                                                    |
| :--------------------------- | :-------------------------------------------------------- | :------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **One**                      | Estimate $p$ / Test a claim about $p$                     | One-sample $z$-interval/test for $p$               | Random; Large Counts ($n\hat{p}\ge10, n(1-\hat{p})\ge10$ or $np_0\ge10, n(1-p_0)\ge10$); Independence ($n \le 0.10N$)                                                                                                                                                                                  |
| **Two (Independent)**        | Estimate $p_1 - p_2$ / Test a claim about $p_1 - p_2$     | Two-sample $z$-interval/test for $p_1 - p_2$       | Random (two independent samples/groups); Large Counts (all 4 counts $\ge 10$); Independence (each $n_i \le 0.10N_i$)                                                                                                                                                                                 |
| **One (Multiple Categories)**| Test if observed distribution fits an expected distribution | Chi-Square Goodness of Fit Test                    | Random; Expected Counts ($\ge 5$ for all categories); Independence ($n \le 0.10N$)                                                                                                                                                                                                                           |
| **Two Categorical Variables**| Test for association (independence) or similarity of distributions (homogeneity) | Chi-Square Test for Independence/Homogeneity | Random (single sample for independence, multiple for homogeneity); Expected Counts ($\ge 5$ for all cells); Independence (if from single sample, $n \le 0.10N$; if multiple samples, each $n_i \le 0.10N_i$) |

---
**Remember:** Always verify the conditions for any inference procedure before interpreting results. Failure to meet conditions can invalidate your conclusions.