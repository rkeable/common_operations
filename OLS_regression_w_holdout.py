import graphlab
import matplotlib.pyplot as plt
%matplotlib inline

sales = graphlab.SFrame('/Users/rebeccakeable/Downloads/Week 2/home_data.gl')
# Upload data into an SFrame

graphlab.canvas.set_target('ipynb') # show in notebook not new tab
sales.show(view='Scatter Plot', x='sqft_living', y='price') # Makes scatter plot

train_data, test_data = sales.random_split(.8, seed=0) 
# Splits data into training (80%) and test validation (20%) to enable testing model for overfitting
# seed=0 ensures that everyone running notebook gets same split groups (can omit if want random)


##### --------------Model 1________________________________________________________________________
sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'])
# Uses training data. Target is our dependent variable and features are our independent variables

print test_data['price'].mean()
print sqft_model.evaluate(test_data)
# Max Error of Model & Root Mean Square Error - average error

plt.plot(test_data['sqft_living'], test_data['price'], '.', test_data['sqft_living'], sqft_model.predict(test_data), '-')
# Plots actual data as blue '.' and predictions as green '-'

sqft_model.get('coefficients')
# Shows model coefficients & std. deviation


##### --------------Model 2________________________________________________________________________
holistic_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']

holistic_model = graphlab.linear_regression.create(train_data, target='price', features=holistic_features)

print test_data['price'].mean()
print holistic_model.evaluate(test_data)

holistic_model.get('coefficients')


### Prediction time!
# Using both models to predict price of hypothetical home
house1 = {'bedrooms':[8], 
              'bathrooms':[25], 
              'sqft_living':[50000], 
              'sqft_lot':[225000],
              'floors':[4], 
              'zipcode':['98039'], 
              'condition':[10], 
              'grade':[10],
              'waterfront':[1],
              'view':[4],
              'sqft_above':[37500],
              'sqft_basement':[12500],
              'yr_built':[1994],
              'yr_renovated':[2010],
              'lat':[47.627606],
              'long':[-122.242054],
              'sqft_living15':[5000],
              'sqft_lot15':[40000]}

print holistic_model.predict(graphlab.SFrame(house1))

print sqft_model.predict(graphlab.SFrame(house1))
