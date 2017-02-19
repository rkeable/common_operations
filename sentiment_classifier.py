import graphlab
from __future__ import division
graphlab.canvas.set_target('ipynb')

products = graphlab.SFrame('/Users/rebeccakeable/Downloads/Week 3/amazon_baby.gl')

products['word_count'] = graphlab.text_analytics.count_words(products['review'])
# create dictionary of all words in reviews and how often they occurred

products['awesome_count'] = products['word_count'].apply(lambda count: count.get('awesome',0))
# creates 'awesome_count' variable that isolates number of 'awesome' from dictionary
products[:2]['word_count','awesome_count','review']
products['great_count'] = products['word_count'].apply(lambda count: count.get('great',0))
products['fantastic_count'] = products['word_count'].apply(lambda count: count.get('fantastic',0))


products = products.sort('awesome_count', ascending=False)
# Sort by awesome_count

# ignore all 3 star reviews
products = products[products['rating'] != 3]
# positive sentiment is 4 or 5 star reviews, sentiment will be the target variable in model
products['sentiment'] = products['rating'] >= 4

train_data, test_data = products.random_split(.8, seed=0)
# split data into training and test with 80% in training

selected_words_model = graphlab.logistic_classifier.create(train_data, target='sentiment', 
                                                      features=['awesome_count','great_count', 'fantastic_count'], 
                                                      validation_set=test_data)

selected_words_model['coefficients'].sort('value')
# sorts coefficients by strength of association with sentiment

selected_words_model.evaluate(test_data)
selected_words_model.show(view='Evaluation')
# shows accuracy of model and false positives and negatives

products['rating'].show(view='Categorical')
# shows distribution of ratings

minority_1 = products[products['rating'] == 1].num_rows()
minority_2 = products[products['rating'] == 2].num_rows()
majority_4 = products[products['rating'] == 4].num_rows()
majority_5 = products[products['rating'] == 5].num_rows()

print majority_5 + majority_4
print minority_1 + minority_2
print (majority_5 + majority_4) / (majority_5 + majority_4 + minority_1 + minority_2)
# shows majority class occurrence that our model should be more accurate than 

products['predicted_sentiment'] = selected_words_model.predict(products, output_type='probability')
# predicts sentiment using model
