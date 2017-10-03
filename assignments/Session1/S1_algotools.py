# -*- coding: utf-8 -*-
"""
@author: bouleta
@brief a set of generic functions for data management
"""

def average_above_zero(tableau):
    """function to find the average of numbers in the tableList    
    @param list of numbers
    @return the float representing the average of th numbers
    """
    if tableau == []:
        raise ValueError("le tableau est vide")
    #init critical variables    
    positive_values_sum = 0
    positive_values_count = 0
    # compute the average of positive elements of a list
    for item in tableau:
        if isinstance(item, str):
            raise ValueError("les valeurs ne doivent pas etre des strings")
        else:            
            if(item > 0):
                positive_values_sum += item
                positive_values_count += 1
            elif item == 0:
                print("this value is null : " + str(item))
            else:
                print("this vale is not positive : " + str(item))
    if positive_values_count != 0:
        average = float(positive_values_sum) / float(positive_values_count)
    else:
        average = 0
    # return the result
    return float(average)

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


def reverse_table(table):
    ##
    # basic fnction able to return the list scaned reversed without using another list
    # @param table : the input list to be scanned
    poslast = len(table)
    for i in range(int(len(table)/2)):
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


# import random functions
import random

def random_fill_sparse(table, vfill):
    ##
    # function used to fill a numpy array randomly 
    # @param a 2D matrix to be scanned
    # @param the number of cells to be filled
    # output the filled matrix
    for i in range(vfill):
        randx = random.randint(0,table.shape[0] - 1)
        randy = random.randint(0, table.shape[1] - 1)
        while table[randx, randy] == 'X':
            randx = random.randint(0,table.shape[0] - 1)
            randy = random.randint(0, table.shape[1] - 1)
        table[randx, randy] = 'X'
    return table

def remove_whitespace(string):
    length = len(string)
    i = 0
    while i < length:
        if string[i] == " ":
            string = string[0:i] + string[i+1:len(string)]
            length -= 1
        i+= 1 
    return string

def shuffle(list_in):
    list_result = []
    for i in range(len(list_in)):
        list_result.append(list_in[random.randint(0,len(list_in))-1])
    print(list_result)
    return list_result

# test with odd list
tab = [1, 2, 3, 4, 5, 6, 7]
newList = shuffle(tab)
print(newList)


# test with even list
tab = [1, 2, 3, 4, 5, 6]
newList = shuffle(tab)
print(newList)
