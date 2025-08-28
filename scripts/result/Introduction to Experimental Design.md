# [[AP Stats Home]]
# Introduction to Experimental Design

In AP Statistics, understanding how to design an effective study is crucial for drawing valid conclusions. We've previously discussed [[Introduction to Planning a Study]] and the importance of [[Random Sampling and a Collection]] for gathering data. While observational studies observe individuals and measure variables of interest without influencing responses, experiments deliberately impose some [[Treatment]] on individuals to observe their responses. The primary goal of an experiment is to establish cause-and-effect relationships.

## Key Terminology

Before diving into design principles, let's define some essential terms:

| Term               | Definition                                                                  | Example                                                                          |
| :----------------- | :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **Experimental Units** | The individuals on which the experiment is performed. If human, they are **subjects**. | Patients in a drug trial, plots of land receiving fertilizer.                     |
| **Explanatory Variables (Factors)** | The independent variables whose effects we want to study.                     | Type of fertilizer, dosage of a drug.                                            |
| **Levels**         | The specific values or versions of the factors.                             | Fertilizer A, Fertilizer B; 5mg drug, 10mg drug.                                 |
| **Treatments**     | A specific condition applied to the experimental units. It's a combination of specific levels of all factors. | Fertilizer A on Plot 1, 10mg drug to Patient X.                                  |
| **Response Variables** | The dependent variables that are measured to determine the effect of the treatments. | Plant growth, blood pressure reduction.                                          |
| **Control Group**  | A group that receives no treatment or a placebo treatment. Used as a baseline for comparison. | Patients receiving a sugar pill instead of the actual drug.                       |

## Core Principles of Experimental Design

A well-designed experiment adheres to three core principles:

1.  **[[Control]]**: We want to minimize the effects of lurking variables on the response variable. This is often done by comparing two or more treatments. A control group serves as a baseline, helping to account for unknown factors that might influence the response. Without control, it's impossible to isolate the effect of the treatment.
    *   **Placebo Effect**: A common issue in experiments, especially with human subjects, where subjects improve simply because they believe they are receiving a treatment, even if it's inactive (a placebo).
    *   **Blinding**:
        *   **Single-blind**: The subjects do not know which treatment they are receiving.
        *   **Double-blind**: Neither the subjects nor the researchers who interact with them know which treatment a subject is receiving. This helps prevent bias from both sides.

2.  **[[Random Assignment]]**: This is the most important principle for establishing cause and effect. Experimental units are assigned to treatments using a chance process (e.g., flipping a coin, using a random number generator).
    *   **Purpose**: Random assignment helps create roughly equivalent groups before treatments are applied. It balances out the effects of unmeasured lurking variables among the treatment groups. If the groups are randomly assigned, any observed differences in the response variable can be attributed to the treatments rather than to pre-existing differences between the groups.
    *   **Distinction from Random Sampling**: Random sampling (from [[Random Sampling and a Collection]]) helps make results generalizable to a larger population. Random assignment helps establish causation within the scope of the experiment.

3.  **[[Replication]]**: Applying each treatment to many experimental units.
    *   **Purpose**: Using enough experimental units in each group reduces the chance variation in the results. If the observed effect of a treatment is consistent across many units, we can be more confident that it's due to the treatment and not just random chance or individual variability. Larger sample sizes in each treatment group lead to more precise estimates of treatment effects.

## Why Experiments are Powerful

The careful implementation of control, random assignment, and replication allows experiments to draw conclusions about **causation**. Unlike observational studies where [[Potential Problems with Sampling]] and confounding variables make it difficult to establish cause and effect, a well-designed experiment can provide strong evidence that changes in the explanatory variable *cause* changes in the response variable.

$$ \text{Treatment Effect} = \text{Observed Response}_{\text{Treatment Group}} - \text{Observed Response}_{\text{Control Group}} $$

This simple equation highlights the goal: to isolate and measure the impact of the treatment.