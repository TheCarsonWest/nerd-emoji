# [[AP Stats Home]]
# Inference and Experiments

In AP Statistics, "Inference" refers to the process of drawing conclusions about a population based on sample data. "Experiments" are a specific type of study design used to investigate cause-and-effect relationships. When conducted properly, experiments provide the strongest evidence for causal inference.

## The Purpose of Experiments

The primary goal of an experiment is to determine if a specific **treatment** (or intervention) causes a change in a **response variable**. Unlike observational studies, which can only establish association, well-designed experiments allow us to make claims of causation. This is achieved by manipulating one or more independent variables (treatments) and observing the effect on dependent variables (responses).

## Key Principles of Experimental Design

Effective experimental design is crucial for valid causal inference. The core principles include:

1.  **Comparison**: Experiments must compare two or more treatments. One of these treatments is often a control group or a placebo.
2.  **Random Assignment**: This is the cornerstone of establishing causation. Subjects are randomly assigned to different treatment groups.
    *   *Why it's important*: Random assignment helps to create groups that are roughly equivalent in all characteristics (both known and unknown confounding variables) before the treatment is applied. This ensures that any observed differences in the response variable between groups are likely due to the treatment, not pre-existing differences.
    *   *Distinction*: [[Random Sampling and a Collection]] is about selecting a representative sample from a population for statistical inference (generalizing to the population). Random assignment is about distributing subjects within an experiment to different treatment groups for causal inference (establishing cause-and-effect).
3.  **Replication**: Applying each treatment to multiple experimental units.
    *   *Why it's important*: Replication reduces the impact of chance variation on the results and increases the reliability of the findings. More replication means a stronger ability to detect effects if they truly exist.
4.  **Control**: Efforts to keep all other variables besides the treatment constant across groups.
    *   *Methods*: Using a [[Control Group]] (a group that receives no treatment or a placebo) is a common control method. Blinding (single or double) is also used to control for psychological biases.

For more details on setting up an experiment, refer to [[Introduction to Experimental Design]] and [[Selecting an Experimental Design]].

## Terminology in Experiments

| Term                | Definition                                                                        | Example                                                                                                  |
| :------------------ | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Experimental Unit** | The smallest unit to which a treatment is applied.                                | A single patient receiving a drug, a plot of land receiving a fertilizer.                                |
| **Treatment**       | A specific condition applied to the experimental units.                           | A specific dosage of a drug, a particular type of fertilizer.                                            |
| **Factor**          | An explanatory variable that is manipulated by the experimenter.                   | Type of drug (e.g., Drug A, Drug B), level of fertilizer (e.g., low, medium, high).                       |
| **Level**           | The specific values or settings for a factor.                                     | Drug A, Drug B are levels of the "Type of Drug" factor; Low, Medium, High are levels of "Fertilizer" factor. |
| **Response Variable** | The variable that is measured after the treatments are applied.                   | Blood pressure, crop yield.                                                                              |
| **Control Group**   | A group that receives an inactive treatment (placebo) or no treatment.            | Patients receiving a sugar pill instead of the actual drug.                                              |

## Causal Inference vs. Statistical Inference

*   **Causal Inference**: When an experiment is properly designed with random assignment, we can conclude that changes in the explanatory variable *cause* changes in the response variable. This is the unique power of experiments.
*   **Statistical Inference**: Once we have the data from an experiment, we use statistical inference procedures (e.g., [[Setting Up a Test for a Population Mean]], [[Confidence Intervals for the Difference of Two Means]]) to determine if the observed differences between treatment groups are statistically significant and unlikely to have occurred by random chance. If the experimental units were also randomly sampled from a larger population, we can then generalize our causal conclusions to that population.

## Potential Problems and Solutions

*   **Confounding Variables**: Variables that are related to both the explanatory and response variables, making it difficult to determine the true effect of the treatment. Random assignment helps to balance confounding variables across groups.
*   **Placebo Effect**: The psychological effect where subjects respond to any treatment, even an inactive one. Using a placebo control group helps to isolate the actual effect of the treatment.
*   **Blinding**:
    *   **Single-blind**: Subjects do not know which treatment they are receiving.
    *   **Double-blind**: Neither the subjects nor the researchers interacting with them know which treatment the subjects are receiving. This helps to reduce bias from both subject expectations and researcher influence.

In summary, carefully designed experiments, particularly those incorporating random assignment, are essential for drawing valid causal inferences in statistics.