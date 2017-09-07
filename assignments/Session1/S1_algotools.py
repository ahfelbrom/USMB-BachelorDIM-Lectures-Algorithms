# -*- coding: utf-8 -*-
"""
@author: bouleta
@brief a set of generic functions for data management
"""
"""
# a variable
a = 1 # default type : int

# an empty list
myList = []

# a filled list
myList2 = [1, 2, 3]

# append to a list
myList.append(10)

# a buggy list
myBuggyList = [1, 'a', "Hi"]

# operators
b = a + 2
myList_sum = myList+myList2 
"""

def average_above_zero(tableau):
    #init critical variables    
    positive_values_sum = 0
    positive_values_count = 0
    # compute the average of positive elements of a list
    for item in tableau:
        if(item > 0):
            positive_values_sum += item
            positive_values_count += 1
        elif item == 0:
            print("this value is null : " + str(item))
        else:
            print("this vale is not positive : " + str(item))
    average = float(positive_values_sum) / float(positive_values_count)
    # return the result
    return float(average)
"""
tab = [-1, 0, 1, 2, 7, 3, 4]
result = average_above_zero(tab)
message = "The average of positives samples of {list_value} is {res}".format(list_value = tab,res = result)
print(message)
"""