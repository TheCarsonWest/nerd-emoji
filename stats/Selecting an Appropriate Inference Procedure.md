# [[AP Stats Home]]
# Selecting an Appropriate Inference Procedure

Choosing the correct inference procedure is a critical skill in AP Statistics. It ensures that your analysis appropriately addresses the research question and satisfies the underlying assumptions of the statistical method. This page outlines a systematic approach to selecting the most suitable confidence interval or hypothesis test.

## Key Questions for Procedure Selection

Before performing any inference, ask yourself the following fundamental questions:

1.  **What type of data are you working with?**
    *   **Categorical Data**: Data that can be divided into groups or categories (e.g., gender, opinion (yes/no), type of car).
    *   **Quantitative Data**: Data that represents counts or measurements (e.g., height, weight, test scores, number of items).
2.  **What is the research question or objective?**
    *   **Estimation**: Do you want to estimate an unknown population parameter (e.g., proportion, mean, difference) with a certain level of confidence? This calls for a [[Constructing a Confidence Interval for a Population]].
    *   **Hypothesis Testing**: Do you want to test a claim or make a decision about a population parameter? This calls for [[Setting Up a Test for a Population Proportion]].
    *   **Relationship**: Are you looking for an association between two categorical variables, a difference between two quantitative variables, or a linear relationship between two quantitative variables?
3.  **How many populations or groups are involved?**
    *   **One Sample**: Inference about a single population parameter (e.g., proportion of adults who vote, mean height of students).
    *   **Two Samples/Groups**: Inference about the difference between two population parameters (e.g., comparing proportions of males vs. females, comparing mean scores of two different teaching methods).
    *   **More Than Two Groups**: Often involves [[Setting Up a Chi-Square Test for Homogeneity or Independence]] for categorical data, or ANOVA (which is beyond the scope of AP Statistics but good to recognize its purpose).
    *   **Paired Data**: A special case of two samples where observations are naturally matched (e.g., before-and-after measurements on the same individuals). [[Setting Up a Test for a Population Mean]] (for the differences).

## Deciding Between Proportions and Means

Once you've identified the data type and the number of groups, you can narrow down the choices:

*   **For Categorical Data**: You will typically be working with **proportions**.
    *   One Sample: [[Constructing a Confidence Interval for a Population Proportion]] or [[Setting Up a Test for a Population Proportion]].
    *   Two Samples: [[Justifying a Claim Based on a Confidence Interval for a Difference of Population Proportions]] or [[Setting Up a Test for the Difference of Two Population Proportions]].
    *   Two or More Categorical Variables (Association/Homogeneity): [[Setting Up a Chi-Square Test for Homogeneity or Independence]] or [[Setting Up a Chi-Square Goodness of Fit Test]] (for one categorical variable distribution).
*   **For Quantitative Data**: You will typically be working with **means**.
    *   One Sample: [[Constructing a Confidence Interval for a Population Mean]] or [[Setting Up a Test for a Population Mean]]. (Remember to use t-procedures).
    *   Two Independent Samples: [[Confidence Intervals for the Difference of Two Means]] or [[Setting Up a Test for the Difference of Two Population Means]]. (Use two-sample t-procedures).
    *   Paired Data: Transform into a single sample of differences and use [[Setting Up a Test for a Population Mean]] (one-sample t-procedure on the differences).

## Regression Inference

When dealing with the relationship between two quantitative variables, the focus shifts to linear regression.

*   **Two Quantitative Variables**: If you are exploring a linear relationship and wish to make inferences about the slope of the population regression line ($$\beta$$):
    *   [[Confidence Intervals for the Slope of a Regression Model]]
    *   [[Setting Up a Test for the Slope of a Regression Model]]

## Summary Table of Common Inference Procedures

| Data Type & Number of Groups | Parameter of Interest | Estimation Procedure (CI) | Hypothesis Testing Procedure (Test) |
| :--------------------------- | :-------------------- | :------------------------ | :---------------------------------- |
| **Categorical**              |                       |                           |                                     |
| One Sample                   | Population Proportion ($$p$$) | One-Sample Z-Interval for $$p$$ | One-Sample Z-Test for $$p$$         |
| Two Independent Samples      | Difference in Proportions ($$p_1 - p_2$$) | Two-Sample Z-Interval for $$p_1 - p_2$$ | Two-Sample Z-Test for $$p_1 - p_2$$ |
| One Categorical Variable     | Distribution Fit (Expected vs. Observed) | N/A | Chi-Square Goodness-of-Fit Test |
| Two Categorical Variables    | Association/Homogeneity | N/A | Chi-Square Test for Homogeneity / Independence |
| **Quantitative**             |                       |                           |                                     |
| One Sample                   | Population Mean ($$\mu$$) | One-Sample t-Interval for $$\mu$$ | One-Sample t-Test for $$\mu$$       |
| Two Independent Samples      | Difference in Means ($$\mu_1 - \mu_2$$) | Two-Sample t-Interval for $$\mu_1 - \mu_2$$ | Two-Sample t-Test for $$\mu_1 - \mu_2$$ |
| Paired Samples               | Mean Difference ($$\mu_d$$) | Paired t-Interval for $$\mu_d$$ | Paired t-Test for $$\mu_d$$         |
| **Two Quantitative Variables** |                       |                           |                                     |
| Linear Relationship          | Slope of Regression Line ($$\beta$$) | t-Interval for Slope ($$\beta$$) | t-Test for Slope ($$\beta$$)        |

Remember, selecting the appropriate procedure is the first step. You must also verify that the [[Conditions for Inference Procedures]] are met before proceeding with calculations and conclusions. Ignoring conditions can lead to invalid results.