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
=======
##
#
# @author Alexandre Benoit, LISTIC Lab, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management

"""
# a variable
a=1 # default type : int

# an empty list
mylist = []

#a filled list
mylist2=[1,2,3]

#append to a list
mylist.append(10)

# a buggy list
mybuggylist=[1,'a', "Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""


def average_above_zero(input_list):
    ##
    # compute the average of positive values
    # @input_list : the list of values to process
    # @return the average value of all the positive elements

    #init critical variable
    positive_values_sum=0
    positive_values_count=0

    first_item=input_list[0] #just a line to generate a code smell with an unused value

    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items
        if item>0:
            positive_values_sum+=item
            positive_values_count+=1
        elif item==0:
            print('This value is null:'+str(item))
        else:
            print('This value is negative:'+str(item))
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count)
    print('Positive elements average is '+str(average))
    return float(average)

"""#testing average_above_zero function:
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
                                                                          res=result)
print(message)
"""

def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init max_value and its index
    max_val=input_list[0]
    max_idx=0
    #compute the average of positive elements of a list
    """for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item
    """
    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        #select only positive items
        if max_val<input_list[idx]:
            max_val=input_list[idx]
            max_idx=idx


    #generic style : iterate over the range of list indexes
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx

    return max_val, max_idx
"""
#test max_value function
#1 basic test, expected answer=2
mylist=[-1,2,-20]
mymax, mymaxidx=max_value(mylist)
mymax_tuple=max_value(mylist)
mymax=mymax_tuple[0]
print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
#==> message : "Max value of [-1, 2, -20] is (2, 1)"

#2 error test : Exception expected
max_value([])
"""

"""
# hints to solve the roi_bbox function exercise: numpy basics

#matrix processing lib
import numpy

#create a numpy matrix with specific dimensions
size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows, size_cols], dtype=int)
#set a value in a specific cell
myMat[1,3]=1

#fil something in the matrix, the basic way (a very slow python way...)
for row in range(5,8):
    for col in range(7,9):
        myMat[row,col]=1

#get time to measure processing speed
import time
init_time=time.time()

#filling something in the matrix, a nicer way
myMat[2:4,5:9]=1 #assign a scalar to each cell of a subarray
myMat[4:7,7:9]=numpy.ones([3,2]) #copy an array in a subarray
print(myMat)

#get ellapsed time
filling_time=time.time() -init_time
print('data prefecting time='+str(filling_time))

#fake bounding box coordinates matrix
xmin=0
xmax=100
ymin=0
ymax=200
#how to fill the 4x2 bbox coordinates matrix, method 1 using 1D numpy arrays (ugly?)
bbox_coords=numpy.zeros([4, 2], dtype=int)
bbox_coords[0,:]=numpy.array([ymin, xmin])
bbox_coords[1,:]=numpy.array([ymin, xmax])
bbox_coords[2,:]=numpy.array([ymax, xmin])
bbox_coords[3,:]=numpy.array([ymax, xmax])
#how to fill the 4x2 bbox coordinates matrix, method 2 using lists (shorter way)
#->create a list of lists
coordsList=[[ymin, xmin],[ymin, xmax],[ymax, xmin],[ymax, xmax]]
#->convert to an array
coords_array=numpy.array(coordsList)
"""