import graphlab
import datetime as dt
import numpy as np
import pandas as pd

graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
graphlab.canvas.set_target('ipynb')

sales = graphlab.SFrame('/Users/rebeccakeable/Downloads/Week 2/home_data.gl')
# Load data into an SFrame

# Method 1: SFrame Logical Filter
filtered_zip1 = sales[sales['zipcode'] == '98039'] 
# Method 2: SFrame apply() function
filtered_zip2 = sales[sales.apply(lambda x: x['zipcode'] > '98039')]
# Method 3: Filter_by function
filtered_zip_alt = sales.filter_by('98039','zipcode')

# Multiple Criterion
# ----------------------------------------------------------------------------
# Using Method 1
filtered_zip3 = sales[(sales['zipcode'] == '98039') | (sales['zipcode'] == '98040') & (sales['price'] > 200000)]
# Using Method 2
filtered_zip4 = sales[sales.apply(lambda x: True if (x['zipcode'] == '98039' or x['zipcode'] == '98030' and x['price'] > 200000) else False)]

filtered_zip1['zipcode','price]
filtered_zip2['zipcode','price]
filtered_zip3['zipcode','price]
filtered_zip4['zipcode','price]             
