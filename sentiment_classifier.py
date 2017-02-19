import graphlab

products = graphlab.SFrame('/Users/rebeccakeable/Downloads/Week 3/amazon_baby.gl')

products['word_count'] = graphlab.text_analytics.count_words(products['review'])
# create dictionary of all words in reviews and how often they occurred
