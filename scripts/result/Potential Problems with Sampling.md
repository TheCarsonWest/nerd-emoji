# [[AP Stats Home]]
# Potential Problems with Sampling

Sampling is a cornerstone of statistical inference, allowing us to gather information about a large population by studying a smaller, representative subset. However, the process of selecting a sample is fraught with potential pitfalls that can lead to inaccurate conclusions about the population. Understanding these problems is crucial for designing effective studies and critically evaluating statistical claims.

## The Goal of Sampling

The primary goal of sampling is to obtain a sample that is **representative** of the population of interest. This means the sample should reflect the characteristics of the population as accurately as possible. When a sample is not representative, it introduces **bias**, which is a systematic error that favors certain outcomes.

## Types of Bias in Sampling

Bias can arise at various stages of the sampling process. Here are some common types:

### [[Sampling Bias (Undercoverage)]]
This occurs when some members of the population are less likely to be chosen or cannot be chosen at all. This systematically excludes certain groups, leading to a sample that does not fully represent the population.
*   **Example**: Conducting a phone survey during the day primarily through landlines might underrepresent people who work during the day or rely solely on cell phones. This could lead to a skewed view if those groups have different opinions on the survey topic.

### [[Voluntary Response Bias]]
This type of bias occurs when individuals choose to participate in a sample. People with strong opinions, especially negative ones, are more likely to volunteer. This often leads to a sample that is not representative of the broader population's views.
*   **Example**: Online polls where anyone can click to vote. People who feel strongly about an issue are more likely to participate, leading to extreme results that don't reflect the general population.

### [[Nonresponse Bias]]
Nonresponse bias occurs when selected individuals refuse to participate in the study or cannot be contacted. If the characteristics of non-respondents differ significantly from respondents, the sample will be biased.
*   **Example**: A mailed survey about a local government policy might have a low response rate. If those who feel strongly (either for or against) are more likely to return the survey, the results will not accurately represent the sentiment of the entire community.

### [[Response Bias]]
Response bias refers to a pattern of inaccurate responses in a survey. This can be caused by various factors, including:
*   **Wording of Questions**: Poorly worded or leading questions can influence how respondents answer.
    *   *Example*: "Do you agree that the flawed new policy should be repealed?" vs. "What is your opinion on the new policy?"
*   **Interviewer Influence**: The characteristics or behavior of the interviewer can affect responses.
    *   *Example*: A survey about sensitive topics might yield different responses depending on the interviewer's perceived age, gender, or demeanor.
*   **Social Desirability**: Respondents may give answers they believe are socially acceptable rather than their true opinions.
    *   *Example*: Overreporting charitable donations or underreporting unhealthy habits.

## Sampling Error vs. Non-sampling Error

It's important to distinguish between these two broad categories of error:

*   **Sampling Error**: This is the natural, chance variation that occurs when you take a sample instead of surveying the entire population. It's not a mistake, but rather an inherent property of sampling. It can be reduced by increasing the sample size or using more efficient sampling methods (e.g., [[Introduction to Planning a Study#Stratified Random Sampling|stratified sampling]]).
    *   The margin of error in a confidence interval (like those discussed in [[Constructing a Confidence Interval for a Population]]) quantifies sampling error.
    *   Mathematically, for a sample proportion $ \hat{p} $, the standard deviation of the sampling distribution (related to sampling error) is $ \sqrt{\frac{p(1-p)}{n}} $.

*   **Non-sampling Error**: These are errors that are not due to the act of sampling. They include all forms of bias discussed above (sampling bias, nonresponse bias, response bias, voluntary response bias), as well as mistakes in data entry, calculation errors, or flaws in the survey design. Non-sampling errors are typically more serious because they cannot be reduced simply by increasing sample size; they often require a redesign of the study.

## Consequences of Poor Sampling

The presence of significant bias invalidates any inferences drawn from the sample about the population. Statistical methods assume that samples are random and free from systematic bias. If these assumptions are violated, any conclusions, such as those made in [[Justifying a Claim Based on a Confidence Interval for a Population Proportion]] or [[Setting Up a Test for a Population Proportion]], will be unreliable and potentially misleading. Therefore, rigorous attention to proper [[Random Sampling and a Collection]] techniques is paramount.