import numpy as np
from __future__ import division
# now will show decimals in division

addition = 5 + 5

subtraction = 5 - 5

multiplication = 5 * 5

division = 5 / 5

exponiation = 5**5

modulo = 5%5
# modulo is the remainder

print addition
print subtraction
print multiplication
print division
print exponiation
print modulo

test_list = [5, 3, 6, 10, 23]
np_test_list = np.array(test_list)
# now an array in numpy and can perform math across entire array

max_list = max(test_list)
# returns max value from test_list
index_6 = test_list.index(6)
# returns position of '6' in test_list
count_6 = test_list.count(6)
# counts number times '6' occurs in test_list
test_list = test_list.append(33)
# Adds 33 to list

test_string = 'rebecca'
test_string = test_string.capitalize()
# capitalizes first letter of string
test_string = test_string.replace("cc", "k")
# replaces "cc" with "k" in string

median = np.median(np_test_list)
mean = np.mean(np_test_list)
std_dev = np.std(np_test_list)


correlation = np.corrcoef(np_test_list['first_var'],np_test_list['second_var'])
