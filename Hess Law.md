# [[Thermodynamics]]
# Hess's Law 
Hess's Law states that the total enthalpy change for a reaction is independent of the pathway taken.  In other words, if a reaction can be carried out in a series of steps, the sum of the enthalpy changes ($\Delta H$) for the individual steps will be equal to the overall enthalpy change for the direct reaction. This is a consequence of enthalpy being a state function. [[State Functions]]

## Applying Hess's Law

Hess's Law is incredibly useful for determining the enthalpy change of reactions that are difficult or impossible to measure directly. We can manipulate known reactions and their enthalpy changes to calculate the unknown enthalpy change of a target reaction.  Here's the general process:

1. **Identify the Target Reaction:** Clearly define the reaction for which you want to determine $\Delta H$.

2. **Gather Known Reactions:** Find reactions with known $\Delta H$ values that involve the reactants and products of your target reaction.

3. **Manipulate Known Reactions:**  Adjust the known reactions so that, when combined, they produce the target reaction.  Allowed manipulations include:

    * **Reversing Reactions:** If you reverse a reaction, change the sign of $\Delta H$.  For example, if $A \rightarrow B$ has $\Delta H = +100 \text{ kJ}$, then $B \rightarrow A$ has $\Delta H = -100 \text{ kJ}$.

    * **Multiplying Reactions:** If you multiply a reaction by a coefficient, multiply $\Delta H$ by the same coefficient. For example, if $A \rightarrow B$ has $\Delta H = +100 \text{ kJ}$, then $2A \rightarrow 2B$ has $\Delta H = +200 \text{ kJ}$.

4. **Add Reactions and Enthalpies:** Add the manipulated reactions together, canceling out any species that appear on both sides of the equations.  The sum of the $\Delta H$ values for the manipulated reactions will be the $\Delta H$ for the target reaction.

## Example

Let's say we want to find the enthalpy change ($\Delta H$) for the formation of carbon dioxide from carbon monoxide:

**Target Reaction:** $CO(g) + \frac{1}{2}O_2(g) \rightarrow CO_2(g) \quad \Delta H = ?$

We are given the following reactions and their enthalpy changes:

* **Reaction 1:** $C(s) + O_2(g) \rightarrow CO_2(g) \quad \Delta H_1 = -393.5 \text{ kJ}$
* **Reaction 2:** $C(s) + \frac{1}{2}O_2(g) \rightarrow CO(g) \quad \Delta H_2 = -110.5 \text{ kJ}$

To obtain the target reaction, we need to reverse Reaction 2 and then add it to Reaction 1:

* **Reversed Reaction 2:** $CO(g) \rightarrow C(s) + \frac{1}{2}O_2(g) \quad \Delta H_2' = +110.5 \text{ kJ}$

Now, add Reaction 1 and the reversed Reaction 2:

$C(s) + O_2(g) + CO(g) \rightarrow CO_2(g) + C(s) + \frac{1}{2}O_2(g)$

Canceling out the common species ($C(s)$ and $\frac{1}{2}O_2(g)$) gives us the target reaction:

$CO(g) + \frac{1}{2}O_2(g) \rightarrow CO_2(g)$

Finally, add the enthalpy changes:

$\Delta H = \Delta H_1 + \Delta H_2' = -393.5 \text{ kJ} + 110.5 \text{ kJ} = -283.0 \text{ kJ}$

Therefore, the enthalpy change for the target reaction is -283.0 kJ.


## Connection to Standard Enthalpies of Formation

Hess's Law is closely related to [[Standard Enthalpies of Formation]].  The standard enthalpy of formation ($\Delta H_f^\circ$) of a compound is the enthalpy change for the formation of one mole of the compound from its elements in their standard states.  Hess's Law can be used to calculate the standard enthalpy change of any reaction using the standard enthalpies of formation of the reactants and products:

$\Delta H^\circ_{rxn} = \sum n\Delta H_f^\circ (\text{products}) - \sum m\Delta H_f^\circ (\text{reactants})$

where *n* and *m* are the stoichiometric coefficients of the products and reactants, respectively.


## Bond Enthalpies and Hess's Law

Hess's Law can also be applied using [[Bond Enthalpies]] to estimate reaction enthalpies.  This involves considering the energy required to break bonds in the reactants and the energy released when bonds are formed in the products.
