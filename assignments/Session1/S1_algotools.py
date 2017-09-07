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

def max_value(table):
    ##
    # basic fnction able to return the max value of a list
    # @param table : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    # first check if provised list is not empty
    if len(table) ==0:
        raise ValueError('provised list is empty')
    # init max_value
    max_value = table[0]
    max_idx = 0
    # compute to find the max value
    for idx in range(len(table)):
        if max_value < table[idx]:
            max_value = table[idx]
            max_idx = idx
    return max_value, max_idx
""" 
tab = [-1, 0, 1, 2, 7, 3, 4]
result = max_value(tab)
print(result)
"""

def reverse_table(table):
    ##
    # basic fnction able to return the list scaned reversed without using another list
    # @param table : the input list to be scanned
    poslast = len(table)
    for i in range(len(table)/2):
        # take the position of the list symmetrically from the middle
        posfirst = i
        poslast = poslast - 1
    
        # taking the values of this positions
        val_first = table[posfirst]
        val_last = table[poslast]
        
        # reverse the list
        table[posfirst] = val_last
        table[poslast] = val_first
    return table
    
# test with odd list
tab = [1, 2, 3, 4, 5, 6, 7]
newList = reverse_table(tab)
print(newList)


# test with even list
tab = [1, 2, 3, 4, 5, 6]
newList = reverse_table(tab)
print(newList)

# matrix processing library
import numpy

def roi_bbox(image):
    ##
    #function to bound an image with a binary code
    #@param a 2D matrix to be scanned
    #output coordiates matrix

    # intitiate base values
    min_y = image.shape[0]
    max_y = 0
    min_x = image.shape[1]
    max_x = 0
    index_of_y = 0
    
    # finding min and max values
    for y in image:
        index_of_x = 0
        for x in y:
            if x == 1:
                if index_of_y < min_y:
                    min_y = index_of_y
                if index_of_y > max_y:
                    max_y = index_of_y
                if index_of_x < min_x:
                    min_x = index_of_x
                if index_of_x > max_x:
                    max_x = index_of_x
            index_of_x+=1
        index_of_y+=1
    
    # creating matrix with coordinates
    bbox_coords = numpy.zeros([4,2],int)
    bbox_coords[0] = [min_y,min_x]
    bbox_coords[1] = [min_y,max_x]
    bbox_coords[2] = [max_y,min_x]
    bbox_coords[3] = [max_y,max_x]
    return bbox_coords

size_rows = 7
size_cols = 7
myMat = numpy.zeros([size_rows, size_cols])

# filling something in the matrix
#for row in range(1,5):
#    for col in range(2,4):
#        myMat[row,col] = 1

# better way to fill the matrix
myMat[1:5,2:4] = numpy.ones([4,2])
print(myMat)

result = roi_bbox(myMat)
print result