import graphlab
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline # direct to plot in notebook itself

graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)

sf = graphlab.SFrame('../Downloads/people-example.csv')

# Graph Lab

graphlab.canvas.set_target('ipynb')

# --------- GraphLab -------------------------------
sf['age'].show(view='Categorical')
# Creates histogram based on age variable

sf['Country'].show()
# shows frequency of each country

sf.show(view='Scatter Plot', x='age', y='price') # Makes scatter plot

sales.show(view='BoxWhisker Plot', x='zipcode', y='price')

# ---------- matplotlib -------------------------------
plt.plot(test_data['sqft_living'],test_data['price'],'.', # Plot Price & Sqft_living as .
        test_data['sqft_living'],sqft_model.predict(test_data),'-') # Plot sqft_living and prediction from model as -
plt.fill_between(test_data['sqft_living', test_data['price'],0,color='green') # colors in under line 
plt.yticks([0,1,2], ["one","two","three"]) # ticks with tick labels                  

plt.scatter(test_data['sqft_living'],test_data['price'])
# plots as scatterplot
plt.xlabel('sq. feet of living space') # x axis name
plt.ylabel('price') # y axis name
plt.title('Relationship between Living Space and Price')
plt.show()
plt.clf() # cleans up so can make new one

plt.scatter(test_data['sqft_living'],test_data['price'])
plt.xscale('log')
# changes x-axis to logarithmic
plt.show()

values = [1, 1, 1, 3, 6, 3, 9, 40, 52, 43, 27, 26, 25, 25, 25, 6, 8, 2, 15, 15, 15, 15]
plt.hist(values, bins=5) # makes histogram with 5 bins that python determines
plt.yticks([5,10,15,20,25,30,35,40,45,50,55]) # adds ticks on the y-axis
plt.show()
                           
np_pop = np.array(pop)
# Double np_pop
np_pop * 2
# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop) # s=np_pop scales each scatter point to its value in np_pop, creating bubbles
plt.show()
plt.clf()                           
                           
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8) # alpha=0.8 makes bubbles translucent
plt.text(1550, 71, 'India') # Adds label 'India' to point at x=1550 y=71
plt.text(5700, 80, 'China')  
                           
                           
