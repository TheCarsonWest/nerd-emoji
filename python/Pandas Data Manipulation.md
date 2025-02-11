# [[Libraries like Pandas]]
# [[Pandas Data Manipulation]] 
This note covers data manipulation using the Pandas library in Python.

Key functionalities:

* **Data Selection:**
    * `.loc` (label-based indexing)
    ```python
    import pandas as pd
    data = {'col1': [[1, [[2], [[3]], 'col2': [[4], [[5], [[6]]}
    df = pd.DataFrame(data)
    print(df.loc[0, 'col1'])  # Accesses value at row 0, column 'col1'
    print(df.loc[:, 'col2'])  # Accesses all rows of column 'col2'
    ```
    * `.iloc` (integer-based indexing)
    ```python
    print(df.iloc[[1, 0]) # Accesses value at row [[1, column 0
    ```
    * Boolean indexing
    ```python
    print(df[df['col1'] > [[1]) # Selects rows where 'col1' > [[1
    ```
    * [[Data Selection with Pandas]]


* **Data Cleaning:**
    * Handling missing values: `.dropna()`, `.fillna()`
    ```python
    df_with_nan = pd.DataFrame({'A': [[1, [[2], None], 'B': [[4], None, [[6]]})
    print(df_with_nan.dropna()) # Drops rows with NaN values
    print(df_with_nan.fillna(0)) # Fills NaN values with 0
    ```
    * Removing duplicates: `.drop_duplicates()`
    ```python
    df_with_duplicates = pd.DataFrame({'A': [[1, [[1, [[2], [[2]], 'B': [[4], [[4], [[5], [[5]]})
    print(df_with_duplicates.drop_duplicates())
    ```
    [[Data Cleaning Techniques]]


* **Data Transformation:**
    * Applying functions: `.apply()`, `.map()`
    ```python
    df['col1_squared'] = df['col1'].apply(lambda x: x**[[2]) #Applies a lambda function
    ```
    * Grouping and aggregation: `.groupby()`, `.agg()`
    ```python
    data = {'group': ['A', 'A', 'B', 'B'], 'value': [[1, [[2], [[3], [[4]]}
    df = pd.DataFrame(data)
    print(df.groupby('group')['value'].agg(['sum', 'mean'])) #Groups by 'group' and calculates sum and mean of 'value'
    ```
    * Pivoting and melting: `.pivot()`, `.melt()`
    ```python
    #Example requires more elaborate data, see [[Data Reshaping with Pandas]]
    ```
    [[Data Transformation Methods]]


* **Data Joining/Merging:**
    * `pd.merge()` (different types of joins)
    ```python
    # Example requires creating two dataframes first, see [[Data Merging Techniques]]
    ```
    [[Data Merging Techniques]]


* **Data Visualization (brief):**
    Pandas integrates well with Matplotlib for basic visualizations.
    ```python
    df.plot.bar(x='col1', y='col2') #Requires matplotlib to be installed
    ```
    [[Pandas Visualization]]

This is a high-level overview. Each bullet point above could be expanded into a more detailed note.  Refer to the linked notes for more in-depth explanations.
