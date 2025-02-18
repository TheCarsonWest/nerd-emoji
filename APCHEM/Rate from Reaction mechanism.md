Make a AP Chemistry rundown on determining [[Rate from Reaction mechanism]]  in markdown format(make use of headings), use the LaTeX equation library format when writing equations. For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]], make sure they are just short titles for seperate notes)

# Rate Law from Reaction Mechanism (AP Chemistry Rundown)

Determining the rate law from a proposed reaction mechanism is a key skill in chemical kinetics.  The rate law derived from a mechanism must agree with the experimentally determined rate law for the mechanism to be considered valid. The overall rate of a reaction is determined by the **slowest elementary step**, also known as the **rate-determining step (RDS)**.

## Elementary Reactions

Elementary reactions describe what happens at the molecular level. They are single steps in a mechanism and have no intermediates. The rate law of an elementary reaction can be written directly from its stoichiometry. For example:

*   A → Products: Rate = $k[A]]$
*   2A → Products: Rate = $k[A]]^2$
*   A + B → Products: Rate = $k[A]][B]]$

## Multi-Step Mechanisms

Most reactions proceed through multiple elementary steps.  The overall rate law for these reactions is determined by the rate-determining step.

### Case 1:  RDS is the First Step

If the slowest step is the first step, the rate law for the overall reaction is simply the rate law of that elementary step.  For example:

Step 1 (slow):  $A + B \rightarrow C$
Step 2 (fast): $C + D \rightarrow E$

Overall Reaction: $A + B + D \rightarrow E$

Rate Law: Rate = $k[A]][B]]$

### Case 2: RDS is Not the First Step

If the slowest step is *not* the first step, the rate law can be more complicated.  Intermediates formed in earlier, faster steps must be expressed in terms of reactants. This is done by assuming a fast equilibrium for the steps preceding the RDS.

**Example:**

Step 1 (fast, reversible): $A \rightleftharpoons B + C$
Step 2 (slow): $B + D \rightarrow E$

Overall Reaction: $A + D \rightarrow C + E$

1.  **Rate Law for the RDS:** Rate = $k[B]][D]]$

2.  **Express Intermediates in Terms of Reactants:** Since step 1 is fast and reversible, we can assume it is at equilibrium:

    $K_{eq} = \frac{[B]][C]]}{[A]]}$  where $K_{eq}$ is the equilibrium constant.

    Therefore, $[B]] = \frac{K_{eq}[A]]}{[C]]}$

3.  **Substitute into the RDS Rate Law:**

    Rate = $k\frac{K_{eq}[A]]}{[C]]}[D]] = k'[A]][D]][C]]^{-1}$ where $k' = kK_{eq}$

    [[Equilibrium Constant]]
    [[Steady-State Approximation]]

This final rate law includes a reactant ($A$ and $D$) and a product from the first step ($C$).  This can happen when the RDS is not the first step. In some cases, you might need to use the steady-state approximation if equilibrium cannot be assumed.

## Steady-State Approximation

[[Steady-State Approximation]]

When the intermediate is highly reactive, the steady-state approximation can be used. This approximation assumes that the rate of formation of the intermediate is equal to its rate of consumption, so its concentration remains relatively constant.


## Catalyst

[[Catalyst]]

Catalysts affect the rate of reaction by providing an alternative reaction pathway with a lower [[Activation Energy]]. They are not consumed in the overall reaction. The presence of a catalyst can change the rate law.


## Summary

1.  Identify the rate-determining step (RDS).
2.  Write the rate law for the RDS based on its stoichiometry.
3.  If the RDS involves intermediates, express their concentrations in terms of reactants using prior fast equilibrium steps or the steady-state approximation.
4.  The resulting rate law should only contain reactants and possibly catalysts.  It should agree with the experimentally determined rate law.
