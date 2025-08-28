# [[AP Stats Home]]
# Representing Two Categorical Variables

When we collect data on two categorical variables for the same individuals, we often want to explore the relationship between these variables. This involves organizing and displaying the data in a way that allows us to identify patterns and associations. This page focuses on how to effectively represent this type of data.

## Two-Way Tables (Contingency Tables)

The primary tool for representing the relationship between two categorical variables is a [[Two-Way Table]]. Also known as a contingency table, it displays counts (or frequencies) of observations for each combination of categories for the two variables.

*   **Structure**:
    *   One categorical variable's categories form the **rows** of the table.
    *   The other categorical variable's categories form the **columns** of the table.
    *   The entries in the cells of the table are the **counts** of individuals who fall into that specific combination of categories.
    *   **Row totals** and **column totals** provide the [[Marginal Distribution]] for each variable separately.
    *   The **grand total** (bottom right corner) is the total number of individuals in the study.

### Example: Opinion on a New Policy by Gender

Consider a survey asking students about their opinion on a new school policy (Support, Oppose, Neutral) and their gender (Male, Female).

|             | Support | Oppose | Neutral | Total |
| :---------- | :------ | :----- | :------ | :---- |
| **Male**    | 50      | 30     | 20      | 100   |
| **Female**  | 40      | 60     | 10      | 110   |
| **Total**   | 90      | 90     | 30      | 210   |

From this table, we can see, for instance, that 50 males supported the policy. There were 100 males surveyed in total, and 90 students supported the policy overall.

## Types of Relative Frequencies

While counts are useful, converting them to relative frequencies (proportions or percentages) allows for easier comparison, especially when group sizes are different.

### 1. Joint Relative Frequencies

These are the proportions of individuals that fall into specific combinations of categories relative to the **grand total**. They tell us the proportion of all individuals in the study that share two specific characteristics.

$$ \text{Joint Relative Frequency} = \frac{\text{Count in cell}}{\text{Grand Total}} $$

*   *Example*: The proportion of students who are male AND support the policy: $50 / 210 \approx 0.238$ (or 23.8%).

### 2. Marginal Relative Frequencies

These are the proportions of individuals that fall into one category of a single variable, relative to the **grand total**. They are found by dividing the row or column totals by the grand total. These represent the [[Marginal Distribution]] for each variable.

$$ \text{Marginal Relative Frequency (Row)} = \frac{\text{Row Total}}{\text{Grand Total}} $$
$$ \text{Marginal Relative Frequency (Column)} = \frac{\text{Column Total}}{\text{Grand Total}} $$

*   *Example*: The proportion of all students who are female: $110 / 210 \approx 0.524$ (or 52.4%).
*   *Example*: The proportion of all students who oppose the policy: $90 / 210 \approx 0.429$ (or 42.9%).

### 3. Conditional Relative Frequencies

[[Conditional Relative Frequencies]] tell us the proportion of individuals with a specific characteristic *within a particular subgroup*. They are crucial for investigating relationships between the two variables, as they allow us to compare distributions across different categories of one variable.

$$ \text{Conditional Relative Frequency} = \frac{\text{Count in cell}}{\text{Marginal Total of the conditioning variable}} $$

*   **Conditioning on one variable**: To see if opinion *depends* on gender, we would look at the distribution of opinion *within* each gender.
    *   *Example*: Proportion of males who support the policy: $50 / 100 = 0.50$ (or 50%).
    *   *Example*: Proportion of females who support the policy: $40 / 110 \approx 0.364$ (or 36.4%).
    *   Comparing these (50% vs. 36.4%) suggests a difference in opinion between genders.

*   **Conditioning on the other variable**: To see if gender *depends* on opinion, we would look at the distribution of gender *within* each opinion category.
    *   *Example*: Proportion of those who support the policy who are male: $50 / 90 \approx 0.556$ (or 55.6%).
    *   *Example*: Proportion of those who support the policy who are female: $40 / 90 \approx 0.444$ (or 44.4%).

By comparing these conditional distributions, we can assess whether there's an association or [[Independence (Categorical Variables)]] between the two categorical variables. If the conditional distributions are similar, there might be little to no association. If they are different, an association likely exists.

For more on analyzing these relationships, refer to [[Statistics for Two Categorical Variables]]. While not extensively covered in AP Statistics, graphical representations like segmented bar charts can visually display conditional distributions, similar to how [[Representing a Categorical Variable with Graphs]] handles single categorical variables.