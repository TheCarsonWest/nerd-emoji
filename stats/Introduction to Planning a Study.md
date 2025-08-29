# [[AP Stats Home]]
# AP Statistics: Introduction to Planning a Study

Careful planning is the cornerstone of any statistical investigation. Without a well-thought-out design, the data collected may be unreliable, biased, or unable to answer the research questions, rendering the entire effort futile. This page introduces the fundamental types of studies and key terminology essential for designing effective data collection methods.

## Why Plan a Study?

The primary goal of planning a study is to gather data that can provide valid insights into a population or phenomenon of interest. This involves making informed decisions about *what* data to collect, *how* to collect it, and *who* to collect it from, all while minimizing potential sources of error and bias.

## Types of Studies

There are three main types of studies used in statistics, each with its own purpose and limitations:

### Observational Studies

In an observational study, researchers observe individuals and measure variables of interest without attempting to influence the responses. We simply watch and record.

*   **Characteristics:** No manipulation of variables by the researcher.
*   **Purpose:** To describe a group or situation, or to explore associations between variables.
*   **Limitation:** Observational studies can show association (correlation) but **cannot establish causation**. This is because lurking variables or [[Confounding Variables]] might be responsible for the observed relationship.
*   **Example:** A study that observes the relationship between screen time and academic performance in high school students. Researchers only record existing screen time habits and grades.

### Experiments

An experiment deliberately imposes some treatment on individuals to measure their responses. The goal is to determine if the treatment causes a change in the response variable.

*   **Characteristics:** Researchers actively manipulate one or more independent variables (treatments) and observe the effect on a dependent variable (response).
*   **Purpose:** To establish a cause-and-effect relationship between variables.
*   **Advantage:** Well-designed experiments can provide strong evidence for causation due to the control over variables and the use of [[Random Sampling and a Collection]] for assignment.
*   **Example:** A study testing a new fertilizer by applying it to some plants (treatment group) and not others (control group), then measuring plant growth. For more details, see [[Introduction to Experimental Design]].

### Surveys

A survey is a specific type of observational study that collects information from a sample of individuals (often through questionnaires or interviews) to understand characteristics of a larger population.

*   **Characteristics:** Gathers data by asking questions to a group of people.
*   **Purpose:** To estimate population parameters or describe attitudes, opinions, or behaviors.
*   **Limitation:** Susceptible to various biases (e.g., response bias, non-response bias). The quality of the survey depends heavily on the sampling method and question design. See [[Potential Problems with Sampling]].
*   **Example:** A poll asking a sample of registered voters about their preferred presidential candidate.

## Key Terminology

Understanding these terms is crucial for interpreting and designing studies:

| Term          | Definition                                                                        | Example (for a study on average GPA of all AP Statistics students in the US) |
| :------------ | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Population**    | The entire group of individuals about which we want information.                   | All AP Statistics students in the US.                                       |
| **Sample**      | A subset of the population from which we actually collect data.                     | 1,000 randomly selected AP Statistics students from various schools.        |
| **Parameter**   | A numerical descriptive measure of a population. (Often unknown)                    | The true average GPA ($\mu$) of all AP Statistics students in the US.       |
| **Statistic**   | A numerical descriptive measure of a sample. (Used to estimate a parameter)        | The average GPA ($\bar{x}$) of the 1,000 sampled AP Statistics students.    |

*   **Explanatory Variable (Independent Variable):** A variable that is thought to explain or cause changes in the response variable.
*   **Response Variable (Dependent Variable):** A variable that measures an outcome of a study.

In an experiment, the explanatory variable is the treatment being applied. For example, if we are studying the effect of fertilizer (explanatory variable) on plant growth (response variable), we might have different levels of fertilizer applied.

*   **Confounding Variable:** A variable that is related to both the explanatory and response variables, making it difficult to determine if the explanatory variable truly causes the change in the response variable. This is a major concern in observational studies.
    *   Mathematically, if $X$ is the explanatory variable, $Y$ is the response variable, and $Z$ is a confounding variable, then:
        $$(X \leftarrow Z \rightarrow Y)$$
    *   Here, $Z$ affects $X$ and $Z$ affects $Y$, creating a spurious association between $X$ and $Y$.

## The Role of Randomness

Randomness plays a vital role in good study design:

*   **Random Sampling:** Essential for [[Random Sampling and a Collection]] and surveys to ensure the sample is representative of the population, allowing for generalization of results. This minimizes sampling bias.
*   **Random Assignment:** In experiments, randomly assigning subjects to different treatment groups helps to balance out the effects of potential confounding variables across the groups. This is crucial for establishing causation.

By carefully considering these foundational concepts, we can design studies that yield meaningful and trustworthy conclusions.