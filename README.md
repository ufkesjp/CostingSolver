# Costing Solver

## Problem Description
A manufacturer needs to determine the cost of individual parts that are purchased in kits.
  - The prices of the kits are updated periodically by the supplier. 
  - The prices of the individual parts are not provided by the supplier, but are necessary for the manufacturer to determine costs of production.
  - Some parts are used in more than one kit.
  - Not all parts have to be assigned a cost, and the manufacturer wants the flexibility to only assign costs to the items that are likely to have a higher replacement value.

## Objectives
1. Determine the cost of each part after receiving updated kit pricing from the supplier.
2. Minimize price variance where price variance = purchase price - cost.

## Approach
The pattern of this problem is akin to a systems of linear equations problem. By one hot encoding all of the parts in all of the kits and setting them equal to the kit price, you can get an equation that looks like the following for each kit:

#### Variables
a = part_id1
b = part_id2
c = part_id3

#### Equation 
1a + 0b + 1c = target price

The coefficients in this solver are either 1 or 0. 1 indicates that a part_id is included in the kit and 0 indicates that it is not included. By creating this equation for each kit, you can get a fairly straightforward systems of linear equations problem, just with a lot of equations and a lot of variables.

Thankfully, scipy.optimize has a solution that fits this problem well with the [non-negative least squares](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html) function. This is what has been leveraged in the [CostingSolver.py]() file.
