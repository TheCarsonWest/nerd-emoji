# [[AP Stats Home]]
# Setting Up a Test for a Population Proportion

When we want to make a claim or decision about the true proportion of a certain characteristic within a population, we often use a [[Hypothesis Test]]. This process allows us to assess the evidence against a null hypothesis in favor of an alternative hypothesis. This note page focuses on the crucial initial steps of setting up such a test for a population proportion.

---

## The Four-Step Process (Introduction)

A hypothesis test generally follows a four-step process, often remembered by mnemonics like "PHANTOMS" or "PANDA" (though specific steps vary slightly). The setup involves the first three parts:
1.  **P**arameters: Define the population parameter of interest.
2.  **H**ypotheses: State the null and alternative hypotheses.
3.  **A**ssumptions/Conditions: Check the conditions required for the test.
4.  **N**ame the test and **T**est statistic: Identify the appropriate test and calculate its statistic (covered in [[Carrying Out a Test for a Population Proportion]]).
5.  **O**btain p-value: Determine the probability of observing our data (or more extreme) if the null hypothesis were true (covered in [[Interpreting p-Values]]).
6.  **M**ake a decision and **S**tate a conclusion: Compare the p-value to the significance level and draw a conclusion in context (covered in [[Concluding a Test for a Population Proportion]]).

---

## 1. Defining the Parameter (P)

First, clearly define the population parameter you are interested in. For a test about a population proportion, this is usually denoted by $p$.

*   Let $p$ = the true proportion of [contextual event/group] in the [defined population].

**Example:**
*   Let $p$ = the true proportion of U.S. adults who support a new healthcare policy.

---

## 2. Stating Hypotheses (H)

This is a critical step where you articulate the claim you are testing. Every hypothesis test involves two competing statements: the null hypothesis ($H_0$) and the alternative hypothesis ($H_a$).

### Null Hypothesis ($H_0$)
The null hypothesis represents the status quo, a statement of no effect, no difference, or no change. It always includes an equality sign.

*   $H_0: p = p_0$
    *   where $p_0$ is a specific hypothesized value for the population proportion.

### Alternative Hypothesis ($H_a$)
The alternative hypothesis is the statement we are trying to find evidence for. It reflects the claim or suspicion that something has changed or is different. It can be one-sided (greater than or less than) or two-sided (not equal to).

**Types of Alternative Hypotheses:**

| Type         | Notation        | Description                                                                                             |
| :----------- | :-------------- | :------------------------------------------------------------------------------------------------------ |
| **Two-Sided** | $H_a: p \ne p_0$ | Used when we are interested in whether the true proportion is simply *different* from $p_0$.           |
| **One-Sided** | $H_a: p > p_0$  | Used when we are interested in whether the true proportion is *greater than* $p_0$.                    |
| **One-Sided** | $H_a: p < p_0$  | Used when we are interested in whether the true proportion is *less than* $p_0$.                       |

**Choosing the Alternative:** The choice of $H_a$ depends on the specific question being asked or the claim being investigated.

**Example:**
*   A company claims that 80% of its customers are satisfied. A consumer group suspects this percentage is lower.
    *   $H_0: p = 0.80$
    *   $H_a: p < 0.80$

---

## 3. Checking Conditions (A)

Before performing a hypothesis test for a population proportion, three key conditions must be met to ensure the sampling distribution of the sample proportion ($\hat{p}$) is approximately normal. These are often referred to as the "Random, Normal, Independent" conditions. This builds upon concepts from [[Sampling Distributions for Sample Proportions]].

### a. Random Condition
The data must come from a [[Random Sampling and a Collection]] or a [[Randomized Experiment]]. This ensures the sample is representative of the population.

*   **Check:** Was the sample obtained using a simple random sample (SRS) or a well-designed random process? If it's an experiment, were subjects randomly assigned?

### b. Normal Condition (Large Counts Condition)
The sampling distribution of $\hat{p}$ is approximately normal if the expected number of successes and failures are both at least 10. *Crucially, we use the hypothesized population proportion ($p_0$) from $H_0$ for this check, not the sample proportion ($\hat{p}$).*

*   $np_0 \ge 10$
*   $n(1 - p_0) \ge 10$

Where:
*   $n$ = sample size
*   $p_0$ = hypothesized population proportion from $H_0$

### c. Independent Condition (10% Condition)
When sampling without replacement, the observations must be independent. This is ensured if the sample size is no more than 10% of the population size.

*   $n \le 0.10N$
    *   Where $N$ = population size.
*   **Check:** Is the sample size ($n$) less than 10% of the total population size? If we assume the population is very large relative to the sample (e.g., millions of people), this condition is usually met.

---

Once these three steps are completed, you have successfully set up your hypothesis test for a population proportion and are ready to proceed with calculating the test statistic and p-value.