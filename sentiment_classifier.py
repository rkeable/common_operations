import graphlab

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
