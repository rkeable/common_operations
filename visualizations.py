import graphlab
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline # direct to plot in notebook itself

graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)

sf = graphlab.SFrame('../Downloads/people-example.csv')

# Graph Lab

graphlab.canvas.set_target('ipynb')

sf['age'].show(view='Categorical')
# Creates histogram based on age variable

sf['Country'].show()
# shows frequency of each country

sf.show(view='Scatter Plot', x='age', y='price') # Makes scatter plot

sales.show(view='BoxWhisker Plot', x='zipcode', y='price')

plt.plot(test_data['sqft_living'],test_data['price'],'.', # Plot Price & Sqft_living as .
        test_data['sqft_living'],sqft_model.predict(test_data),'-') # Plot sqft_living and prediction from model as -
