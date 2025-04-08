import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import nnls

# to read in the composition of each kit, showing which parts are in which kit
KIT_Comp = pd.read_excel("./PartsCost_Updates.xlsx", sheet_name = 'Kit Composition')

# read in the new prices to a separate dataframe - this source serves as the pricing library
KIT_Pricing = pd.read_excel("./PartsCost_Updates.xlsx", sheet_name = 'Kit Prices')

# This is 1-hot encoding the composition, where the quantity indicates whether or not the manufacturer wants the part to receive a portion of the kit price. .getdummies() is another option here.
# The quantity determines the coefficient utilized in the systems of equations non-negative least squares solver. In this case, it's binary (1 or 0).
basket = KIT_Comp.groupby(['kit_ID', 'part_ID'])['Qty'].sum().unstack().reset_index().fillna(0).set_index('kit_ID')

basket.to_numpy()
A = basket

Price_List = KIT_Pricing ['Cost'].to_numpy()
Price_List = np.nan_to_num(Price_List)

B = Price_List

# utilize scipy's non-negative least squares solver, which prevents negative costs from being assigned to parts.
solution = nnls(A,B)[0]

# Creating a dictionary of new parts costs
COM_List = basket.columns.values

dict = {'part_ID': COM_List, 'Updated Cost': solution}
Updated_Parts_Costs = pd.DataFrame(dict)

# previewing this parts dictionary prior to writing it back to excel as a new sheet
print(Updated_Parts_Costs)

# writing the dataframe back into excel - this will throw an error if there's already a sheet named 'Updated_COM_Costs'. This indicates that this work has already been completed.
with pd.ExcelWriter("./PartsCost_Updates.xlsx", mode = 'a') as writer:
    Updated_Parts_Costs.to_excel(writer, sheet_name = 'Updated_Parts_Costs')

# ------------------------------------------------------------------------
#                        Enhancements to be made
# ------------------------------------------------------------------------

# Assess variances after rebuilding the kits - group by kit_ID and compare against target prices
# Sort both the kit_composition and KIT_Pricing dataframes in ascending order or else users could run the risk of assigning the wrong target price to the kit
