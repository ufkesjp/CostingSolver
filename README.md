# Costing Solver

## Problem Description
A manufacturer needs to determine the cost of individual parts that are purchased in kits.
  - The prices of the kits are updated periodically by the supplier. 
  - The prices of the individual parts are not provided by the supplier, but are necessary for the manufacturer to determine costs of production.
  - Some parts are used in more than one kit.
  - Not all parts have to be assigned a cost, and the manufacturer wants the flexibility to only assign costs to the items that are likely to have a higher replacement value if something were to happen.

## Question that needs to be answered
What should the cost of each part be updated to after receiving the updated kit prices from the supplier?

## Objective
Minimize price variance, which is calculated as Purchase Price - Kit Cost.
