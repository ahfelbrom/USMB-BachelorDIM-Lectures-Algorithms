# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:15:41 2017

@author: alexis
"""

import S1_algotools as algotools

def test_average_above_zero_one_value_under_zero():
    ##function to test average_above_zero
    #used to see the aerage if there's 1 or more number under 0
    tab = [-1, 0, 1, 2, 7, 3, 4]
    assert algotools.average_above_zero(tab) == 3.4

def test_average_above_zero_all_under_or_equal_zero():
    ## function to test average_above_zero
    #used to see the aerage if there's 1 or more number under 0
    tab = [-1, -5, 0, -2, -7, -3, -4]
    assert algotools.average_above_zero(tab) == 0.0
    
def test_average_above_zero_empty_error():
    ##
    # function used to test the function average_above_zero
    # this one is for the valueError empty tab
    tab = []
    try:
        assert algotools.average_above_zero(tab)
    except ValueError :
        assert True
    
def test_average_above_zero_string_error():
    ##
    # function used to test the function average_above_zero
    # this one is for the TypeError string tab    
    tab = ["ab", "a", "cd"]
    try:
        assert algotools.average_above_zero(tab)
    except TypeError :
        assert True

def test_max_value_positive_values():
    ##function testing the finding if the maximal value
    #for all values positives
    tab = [1, 0, 1, 2, 7, 3, 4]
    assert algotools.max_value(tab) == (7,4)

def test_max_value_max_zero():
    ##function testing the finding if the maximal value
    #for zero max value
    tab = [-1, 0, -1, -2, -7, -3, -4]
    assert algotools.max_value(tab) == (0,1)

def test_max_value_negative_values():
    ##function testing the finding if the maximal value
    #for all values positives
    tab = [-1, -10, -1, -2, -7, -3, -4]
    assert algotools.max_value(tab) == (-1,0)
    
def test_max_value_empty_error():
    ##
    # function used to test the function max_value
    # this is for ValueError empty list
    tab = []
    try:
        assert algotools.max_value(tab)
    except ValueError :
        assert True
    
def test_max_value_type_error():
    ##
    # function used to test the function max_value
    # this is for typeError string list
    tab = ["ab", "a", "cd"]
    try:
        assert algotools.max_value(tab)
    except TypeError :
        assert True
    
def test_reverse_table_odd_list():
    ##function testing the reversion of a table list
    #with an odd list
    tab = [1, 2, 3, 4, 5, 6, 7]
    assert algotools.reverse_table(tab) == [7, 6, 5, 4, 3, 2, 1]
    
def test_reverse_table_even_list():
    ##function testing the reversion of a table list
    #with an even list
    tab = [1, 2, 3, 4, 5, 6]
    assert algotools.reverse_table(tab) == [6, 5, 4, 3, 2, 1]
    
def test_reverse_table_string_list():
    ##function testing the reversion of a table list
    #with string list
    tab = ["a", "f", "t", "h"]
    assert algotools.reverse_table(tab) == ["h", "t", "f", "a"]    
    
import numpy

def test_roi_bbox_functionnal():
    ##function testing the finding of a bounding box
    size_rows = 7
    size_cols = 7
    my_mat = numpy.zeros([size_rows, size_cols])    
    my_mat[1:5,2:4] = numpy.ones([4,2])
    assert numpy.alltrue(algotools.roi_bbox(my_mat) == [[1, 2],[1, 3], [4, 2], [4, 3]])

def test_roi_bbox_emptyError():
    size_rows = 7
    size_cols = 7
    my_mat = numpy.zeros([size_rows, size_cols])    
    try:
        assert numpy.alltrue(algotools.roi_bbox(my_mat) == [[1, 2],[1, 3], [4, 2], [4, 3]])
    except Exception : 
        assert True
def test_random_fill_sparse_functionnal():
    ##function testing random filling of a numpy array
    #it's testing if the result_array is not empty
    size = 5
    my_rand_mat = numpy.zeros([size, size], dtype=str)
    vfill = 10
    assert numpy.any(algotools.random_fill_sparse(my_rand_mat, vfill) != [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']])

def test_remove_whitespace_middle():
    ## function testing the removal of whitespaces in a string
    #here it tests the removal of the middle whitespace
    string = "Hello world"
    assert algotools.remove_whitespace(string) == "Helloworld"
    
def test_remove_whitespace_middle_extremities():
    ##function testing the removal of whitespaces in a string
    #here it tests the removal of the middle and the extremities whitespaces    
    string = " Hello world "
    assert algotools.remove_whitespace(string) == "Helloworld"

def test_remove_whitespace_middle_left_extremity():
    ##function testing the removal of whitespaces in a string
    #here it tests the removal of the middle and the left extremity whitespaces
    string = " Hello world"
    assert algotools.remove_whitespace(string) == "Helloworld"
    
def test_remove_whitespace_middle_right_extremity():
    ##function testing the removal of whitespaces in a string
    #here it tests the removal of the middle and the right extremity whitespaces
    string = "Hello world "
    assert algotools.remove_whitespace(string) == "Helloworld"
    
def test_remove_whitespace_right_extremity():
    ##function testing the removal of whitespaces in a string
    #here it tests the removal of the right extremity whitespace
    string = "Helloworld "
    assert algotools.remove_whitespace(string) == "Helloworld"

def test_shuffle_odd_list():
    ## function testing the shuffle of a list
    # this is testing for an odd list
    tab = [1, 2, 3, 4, 5, 6, 7]
    new_list = algotools.shuffle(tab)
    assert new_list != tab

def test_shuffle_even_list():
    ## function testing the shuffle of a list
    # this is testing for an even list
    tab = [1, 2, 3, 4, 5, 6]
    new_list = algotools.shuffle(tab)
    assert new_list != tab

def test_shuffle_string_list():
    ## function testing the shuffle of a list
    # this is testing for a string list
    tab = ["a", "b", "c", "d", "z"]
    new_list = algotools.shuffle(tab)
    assert new_list != tab

def test_sort_selective_functionnal():
    tab = [10, 15, 7, 1, 3, 3, 9]
    assert algotools.sort_selective(tab) == [1, 3, 3, 7, 9, 10, 15]
    
def test_sort_bubble_functionnal():
    tab = [9, 2, 4, 3, 1, 5, 7, 6, 8]
    assert algotools.sort_bubble(tab) == [1, 2, 3, 4, 5, 6, 7, 8, 9]    