# [[AP Stats Home]]
# Expected Counts in Two-Way Tables

When analyzing [[Representing Two Categorical Variables]] using a two-way table, we often want to determine if there's a significant association between the two variables. This analysis typically involves comparing the observed counts in each cell of the table to what we would *expect* to see if there were no association (i.e., if the variables were independent). These "expected counts" are a crucial component for [[Setting Up a Chi-Square Test for Homogeneity or Independence]].

## What are Expected Counts?

An **expected count** for a specific cell in a two-way table is the number of observations we would anticipate in that cell if the two categorical variables were truly independent of each other within the population. In simpler terms, it's what we'd expect to see if there were no relationship or difference between the categories being compared.

## The Formula for Expected Counts

The expected count for any cell in a two-way table is calculated using the following formula:

$$
\text{Expected Count} = \frac{(\text{Row Total}) \times (\text{Column Total})}{\text{Grand Total}}
$$

Where:
*   **Row Total**: The sum of all observed counts in the row containing the cell of interest.
*   **Column Total**: The sum of all observed counts in the column containing the cell of interest.
*   **Grand Total**: The total number of observations in the entire two-way table.

## Calculating Expected Counts: An Example

Let's consider a study investigating the relationship between a student's preferred learning style (Visual, Auditory, Kinesthetic) and their performance on a recent exam (Pass, Fail).

Here are the observed counts:

| Learning Style | Pass | Fail | Total (Row) |
| :------------- | :--- | :--- | :---------- |
| Visual         | 30   | 10   | 40          |
| Auditory       | 25   | 5    | 30          |
| Kinesthetic    | 20   | 10   | 30          |
| Total (Col)    | 75   | 25   | 100         |

Now, let's calculate the expected counts for each cell:

1.  **Expected Count (Visual, Pass)**:
    Row Total (Visual) = 40
    Column Total (Pass) = 75
    Grand Total = 100
    $$
    E_{\text{Visual, Pass}} = \frac{40 \times 75}{100} = \frac{3000}{100} = 30
    $$

2.  **Expected Count (Visual, Fail)**:
    Row Total (Visual) = 40
    Column Total (Fail) = 25
    Grand Total = 100
    $$
    E_{\text{Visual, Fail}} = \frac{40 \times 25}{100} = \frac{1000}{100} = 10
    $$

3.  **Expected Count (Auditory, Pass)**:
    Row Total (Auditory) = 30
    Column Total (Pass) = 75
    Grand Total = 100
    $$
    E_{\text{Auditory, Pass}} = \frac{30 \times 75}{100} = \frac{2250}{100} = 22.5
    $$

4.  **Expected Count (Auditory, Fail)**:
    Row Total (Auditory) = 30
    Column Total (Fail) = 25
    Grand Total = 100
    $$
    E_{\text{Auditory, Fail}} = \frac{30 \times 25}{100} = \frac{750}{100} = 7.5
    $$

5.  **Expected Count (Kinesthetic, Pass)**:
    Row Total (Kinesthetic) = 30
    Column Total (Pass) = 75
    Grand Total = 100
    $$
    E_{\text{Kinesthetic, Pass}} = \frac{30 \times 75}{100} = \frac{2250}{100} = 22.5
    $$

6.  **Expected Count (Kinesthetic, Fail)**:
    Row Total (Kinesthetic) = 30
    Column Total (Fail) = 25
    Grand Total = 100
    $$
    E_{\text{Kinesthetic, Fail}} = \frac{30 \times 25}{100} = \frac{750}{100} = 7.5
    $$

## Expected Counts Table

Here is the table of expected counts for our example:

| Learning Style | Pass | Fail | Total (Row) |
| :------------- | :--- | :--- | :---------- |
| Visual         | 30   | 10   | 40          |
| Auditory       | 22.5 | 7.5  | 30          |
| Kinesthetic    | 22.5 | 7.5  | 30          |
| Total (Col)    | 75   | 25   | 100         |

Notice that expected counts do not have to be whole numbers, as they represent theoretical averages if independence holds.

## [[Conditions for Chi-Square Tests]]

A crucial condition for performing a chi-square test for homogeneity or independence is that **all expected counts must be at least 5**. If any expected count is less than 5, the assumptions for the chi-square distribution are violated, and the results of the test may not be reliable. In such cases, categories might need to be combined, or alternative statistical methods pursued.