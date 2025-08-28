# [[AP Stats Home]]
# Selecting an Experimental Design

Choosing the appropriate experimental design is crucial for drawing valid conclusions about cause-and-effect relationships. This page builds upon the [[Introduction to Experimental Design]] by delving into specific design structures and their applications.

## Key Principles of Experimental Design

Effective experimental designs adhere to three fundamental principles:

1.  **[[Control (Experimental Design)]]**:
    *   Researchers must control for lurking variables that could affect the response. This often involves keeping conditions as similar as possible for all experimental units, except for the treatments being compared.
    *   A **control group** receives an inactive treatment (placebo) or the standard treatment, serving as a baseline for comparison.
    *   **Placebo effect**: A response to a dummy treatment, which highlights the need for a control group and blinding.

2.  **[[Randomization (Experimental Design)]]**:
    *   Randomly assigning experimental units to treatment groups helps create groups that are roughly equivalent in all respects before the treatments are applied.
    *   This balances the effects of unmeasured or unknown lurking variables among the treatment groups.
    *   Randomization ensures that any observed differences in the response are more likely due to the treatments rather than pre-existing differences between groups.

3.  **[[Replication (Experimental Design)]]**:
    *   Applying each treatment to multiple experimental units (or repeating the experiment multiple times) helps reduce the impact of chance variation on the results.
    *   The more experimental units in each treatment group, the more precisely we can estimate the effects of the treatments.
    *   Replication allows us to determine if observed effects are consistent and not just random fluctuations.

## Types of Experimental Designs

### 1. Completely Randomized Design (CRD)

In a CRD, experimental units are randomly assigned to treatment groups without any other considerations.

**Steps:**

1.  Identify a group of homogeneous experimental units.
2.  Randomly assign these units to one of the treatment groups (including a control group, if applicable).
3.  Apply treatments.
4.  Measure the response variable.

**Diagram:**

```
Experimental Units
      |
      V
  Random Assignment
  /             \
 Treatment 1   Treatment 2
   (n units)     (n units)
      |             |
      V             V
 Measure Response  Measure Response
```

**When to use:** When experimental units are relatively homogeneous and there are no obvious factors to block on.

### 2. Randomized Block Design (RBD)

A randomized block design is used when there are known sources of variability among the experimental units that could affect the response. Units are first grouped into "blocks" based on a characteristic they share that is expected to influence the response, and then treatments are randomly assigned within each block.

**Steps:**

1.  Group experimental units into **blocks** based on a characteristic that is known or suspected to affect the response. (e.g., age, gender, location).
2.  Within each block, randomly assign experimental units to the treatments. Every treatment must appear in every block.
3.  Apply treatments.
4.  Measure the response variable.

**Diagram:**

```
Experimental Units
      |
      V
    Block 1 ---------> Random Assignment ---------> Treatment 1, Treatment 2
      |                                              (within Block 1)
    Block 2 ---------> Random Assignment ---------> Treatment 1, Treatment 2
      |                                              (within Block 2)
    Block ... --------> Random Assignment ---------> Treatment 1, Treatment 2
                                                     (within Block ...)
```

**Benefits:** Blocking reduces variability within treatment groups, making it easier to detect treatment effects. It accounts for known sources of variation.

### 3. Matched Pairs Design

A matched pairs design is a special case of a randomized block design where the blocks consist of two experimental units (or one unit receiving both treatments).

**Two main scenarios:**

*   **Pairs of similar units:** Two units that are as similar as possible are matched. One unit receives Treatment A, and the other receives Treatment B, with the assignment often randomized (e.g., flipping a coin).
*   **Single unit receiving both treatments:** Each experimental unit receives both treatments in a random order. This is common when comparing two conditions for the same individual (e.g., a "before" and "after" measurement, or left vs. right arm).

**Advantages:** This design controls for individual differences exceptionally well, as the comparison is made within the pair or within the same individual. This significantly reduces lurking variables and improves the power to detect treatment effects.

**Example:**
To compare two different sunscreens, each person applies sunscreen A to one arm and sunscreen B to the other arm (randomizing which arm gets which). The response is then compared for each person. Here, each person acts as their own block.

## Blinding

To prevent bias, experimenters often employ blinding:

*   **Single-blind**: The experimental units do not know which treatment they are receiving.
*   **Double-blind**: Neither the experimental units nor the researchers directly involved with the subjects know which treatment each unit is receiving. This is ideal to prevent conscious or subconscious bias from both the subjects and the experimenters.

Blinding helps to minimize the [[Placebo Effect]] and experimenter bias, strengthening the validity of the conclusions.

## Ethical Considerations

Ethical guidelines must always be followed in experimental design, particularly when involving human subjects or animals. This includes informed consent, protection of privacy, and minimizing harm.

By carefully considering these principles and design types, researchers can select an experimental design that effectively answers their research questions and provides reliable conclusions, setting the stage for [[Inference and Experiments]].