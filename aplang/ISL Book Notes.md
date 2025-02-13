# [[Useful Websites and Articles]]
# [[ISL Book Notes]]

**Chapter [[1: Introduction to Statistical Learning**

* **What is Statistical Learning?**  The goal is to build a model relating a response variable $Y$ to a set of predictor variables $X_1, X_2, ..., X_p$.  We can use this model to:
    * Predict the response $Y$ for new values of $X$.
    * Understand the relationship between $Y$ and $X$.

* **Types of Statistical Learning:**
    * **Supervised Learning:** We have both $X$ and $Y$ for training data.  Examples: [[Regression]], [[Classification]].
    * **Unsupervised Learning:** We only have $X$. Examples: [[Clustering]], [[Dimensionality Reduction]].

* **Regression vs. Classification:**
    * **Regression:** $Y$ is continuous.  Examples: predicting house prices, stock prices.
    * **Classification:** $Y$ is categorical. Examples: predicting customer churn, image recognition.

* **Model Accuracy:** Measured by error rate or prediction accuracy.  We use training data to fit the model and test data to evaluate its performance.  This is to avoid [[Overfitting]].

* **Bias-Variance Tradeoff:**  A crucial concept.  [[Bias-Variance Tradeoff]].

* **Model Selection:** Choosing the best model involves balancing bias and variance.  Techniques include: [[Cross-Validation]], [[Regularization]].


**Chapter 2: Linear Regression**

* **Simple Linear Regression:**  Modeling the relationship between a single predictor variable $X$ and a continuous response variable $Y$ using a linear equation:  $Y = \beta_0 + \beta_1X + \epsilon$, where $\beta_0$ is the intercept, $\beta_1$ is the slope, and $\epsilon$ is the error term.  Estimating $\beta_0$ and $\beta_1$ using [[Least Squares Estimation]].

* **Multiple Linear Regression:** Extending simple linear regression to include multiple predictor variables: $Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_pX_p + \epsilon$.  [[Model Assumptions]].

* **Assessing Model Fit:** Using $R^2$, adjusted $R^2$, and [[Residual Plots]] to evaluate the model's goodness of fit.

* **Model Diagnostics:** Identifying and addressing potential problems such as [[Multicollinearity]] and [[Heteroscedasticity]].


**Chapter 3:  Classification**

* **Logistic Regression:** Modeling the probability of a binary outcome using a logistic function: $P(Y=[[1|X) = \frac{[[1}{[[1 + exp(-\beta_0 - \beta_1X)}$. [[Logistic Regression Details]]

* **K-Nearest Neighbors:** Classifying a new observation based on the majority class among its $k$ nearest neighbors in the feature space. [[KNN Algorithm]]

* **Linear Discriminant Analysis (LDA):** Assuming data is normally distributed and finding linear combinations of predictors that maximize the separation between classes. [[LDA Details]]

* **Quadratic Discriminant Analysis (QDA):**  Similar to LDA, but allows for different covariance matrices for each class. [[QDA Details]]


[[Regression]]
[[Classification]]
[[Clustering]]
[[Dimensionality Reduction]]
[[Overfitting]]
[[Bias-Variance Tradeoff]]
[[Cross-Validation]]
[[Regularization]]
[[Least Squares Estimation]]
[[Model Assumptions]]
[[Residual Plots]]
[[Multicollinearity]]
[[Heteroscedasticity]]
[[Logistic Regression Details]]
[[KNN Algorithm]]
[[LDA Details]]
[[QDA Details]]

