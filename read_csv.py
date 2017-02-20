import pandas as pd
import numpy as np

data = pd.read_csv('/Users/rebeccakeable/Downloads/Jumpman23/analyze_me.csv', index_col='delivery_id') 
# imports data and sets the 'delivery_id' column as the index

print data['item_category'] # prints item_category column

data['item_category'].loc[143252] 
# returns item_category for delivery_id 143252

data.loc[[143252]]
# selects observation with index 143252 as dataframe

print(data[data['vehicle_type'] == 'Bike'])
# print only observations with 'Bike' as the vehicle type

data.loc[[143252, 143253], ['item_category']]
# shows item_category for selected delivery_ids as dataframe
