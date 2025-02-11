# [[Recommended Reading List]]
# [[Bias Mitigation]] Notes

**Main Goal:** Reduce or eliminate undesirable biases in datasets and models.

**Types of Bias:**

* **Sampling Bias:**  Data doesn't accurately represent the population.  [[Sampling Bias Notes]]
* **Measurement Bias:**  Systematic error in how data is collected or measured. [[Measurement Bias Notes]]
* **Algorithmic Bias:** Bias inherent in the algorithms themselves. [[Algorithmic Bias Notes]]
* **Representation Bias:**  Inadequate representation of certain groups in the data.  Related to [[Sampling Bias Notes]]


**Mitigation Techniques:**

* **Data Preprocessing:**
    * **Re-sampling:** Oversampling minority classes, undersampling majority classes.  Requires careful consideration to avoid introducing new biases. [[Resampling Techniques]]
    * **Data Augmentation:**  Generating synthetic data to balance class distributions. [[Data Augmentation Techniques]]
    * **Data Cleaning:** Handling missing values, outliers, and inconsistencies. [[Data Cleaning Techniques]]
    * **Feature Selection:** Selecting features that are less likely to be biased. [[Feature Selection Techniques]]
* **Algorithm Selection:** Choosing algorithms less susceptible to bias.  Consider fairness-aware algorithms. [[Fairness-Aware Algorithms]]
* **Post-processing:**  Modifying model outputs to mitigate bias after training.  Examples include calibration and threshold adjustment. [[Post-processing Techniques]]
* **Adversarial Training:** Training a model to be robust against biased inputs. [[Adversarial Training Notes]]

**Evaluation Metrics:**

Need to evaluate the effectiveness of bias mitigation techniques. Metrics will vary based on the type of bias and the context.  Some examples include:

* **Accuracy/Precision/Recall:**  Standard metrics, but need to be analyzed across different demographic groups to detect disparities.
* **Fairness Metrics:**  e.g., Equal Opportunity, Demographic Parity, Predictive Rate Parity. [[Fairness Metrics Notes]]

**Mathematical Formalism (example):**

Suppose we have a binary classification problem with protected attribute $A$ (e.g., gender) and outcome $Y$.  We want to ensure that the model's predictions are fair across different values of $A$.  One metric of fairness is **Equal Opportunity**, which requires:

$P(Y = [[1]] | \hat{Y} = [[1]], A = a) = P(Y = [[1]] | \hat{Y} = [[1]], A = a')$  for all $a, a'$,

where $\hat{Y}$ represents the model's prediction.


**Further Research:**

* Causal inference and bias mitigation. [[Causal Inference and Bias]]
* Explainable AI (XAI) and bias detection. [[XAI and Bias Detection]]


**Open Questions:**

* How to define and measure fairness in a way that is both meaningful and practical?
* How to balance fairness with accuracy and other desirable model properties?
* How to adapt bias mitigation techniques to different types of data and applications?


