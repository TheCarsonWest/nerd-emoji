# [[Libraries like Pandas]]
# [[Data Cleaning in Pandas]] 
This note covers data cleaning techniques within the Pandas library.  Focus will be on practical application and common issues.

Key areas to cover:

* **Handling Missing Data:**
    * Identifying missing values (`isnull()`, `notnull()`)
    * `dropna()` - removing rows/columns with missing data.  Explore `how`, `thresh`, `subset` parameters.
    * Imputation techniques:
        * Filling with specific values (`fillna()` with constants, mean, median, forward/backward fill)
        * Using more sophisticated methods (e.g., from scikit-learn's `SimpleImputer`)  ([[Imputation Techniques]])
    * Understanding the implications of different imputation strategies and choosing appropriate methods based on the dataset and the analysis goals.

* **Dealing with Outliers:**
    * Identifying outliers using box plots, scatter plots, IQR method.
    * Techniques for handling outliers:
        * Removal (careful consideration needed!)
        * Winsorizing/Clipping (capping values at certain percentiles)
        * Transformation (e.g., logarithmic transformation)
    * Consider the domain knowledge and potential impact on analysis before choosing a method. ([[Outlier Detection and Treatment]])

* **Data Transformation:**
    * Changing data types (`astype()`)
    * String manipulation (e.g., using `str.lower()`, `str.strip()`, regular expressions)  ([[Pandas String Manipulation]])
    * Feature scaling (e.g., standardization, normalization) [[Feature Scaling in Pandas]]
    * Creating new features from existing ones (feature engineering).

* **Data Consistency:**
    * Identifying and correcting inconsistencies in categorical variables (e.g., different spellings, capitalization).
    * Using `replace()` and `map()` for value replacements.
    * Handling duplicates (`duplicated()`, `drop_duplicates()`)

* **Example Code:**

```python
import pandas as pd
import numpy as np

# Sample DataFrame with missing values and outliers
data = {'A': [[1, [[2], np.nan, [[4], [[5], 100], 
        'B': ['apple', 'banana', 'orange', 'apple', 'banana', 'Apple']}
df = pd.DataFrame(data)

# Handling missing values
df_cleaned = df.dropna() # Remove rows with NaN
df_filled = df.fillna({'A': df['A'].mean()}) # Fill NaN with mean of column A

# Handling outliers (example: removing values > 10 in column A)
df_no_outliers = df_filled[df_filled['A'] <= 10]

#String Manipulation - lowercase and remove leading/trailing whitespace
df_cleaned['B'] = df_cleaned['B'].str.lower().str.strip()

print(df)
print(df_cleaned)
print(df_filled)
print(df_no_outliers)


```


Remember to always explore and understand your data before applying any cleaning techniques.  The best approach depends heavily on the specific dataset and the intended analysis.
