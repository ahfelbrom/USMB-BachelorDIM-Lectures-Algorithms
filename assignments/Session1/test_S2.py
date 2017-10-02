# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:15:41 2017

@author: alexis
"""

import S1_algotools as algotools

def test_average_above_zero_one_value_under_zero():
    """ function to test average_above_zero
    used to see the aerage if there's 1 or more number under 0
    """
    tab = [-1, 0, 1, 2, 7, 3, 4]
    assert algotools.average_above_zero(tab) == 3.4

def test_average_above_zero_all_under_or_equal_zero():
    """ function to test average_above_zero
    used to see the aerage if there's 1 or more number under 0
    """
    tab = [-1, -5, 0, -2, -7, -3, -4]
    assert algotools.average_above_zero(tab) == 0.0
    
def test_max_value_positive_values():
    """function testing the finding if the maximal value
    for all values positives
    """
    tab = [1, 0, 1, 2, 7, 3, 4]
    assert algotools.max_value(tab) == (7,4)

def test_max_value_max_zero():
    """function testing the finding if the maximal value
    for zero max value
    """
    tab = [-1, 0, -1, -2, -7, -3, -4]
    assert algotools.max_value(tab) == (0,1)

def test_max_value_negative_values():
    """function testing the finding if the maximal value
    for all values positives
    """
    tab = [-1, -10, -1, -2, -7, -3, -4]
    assert algotools.max_value(tab) == (-1,0)
    
def test_reverse_table_odd_list():
    """function testing the reversion of a table list
    with an odd list
    """
    tab = [1, 2, 3, 4, 5, 6, 7]
    assert algotools.reverse_table(tab) == [7, 6, 5, 4, 3, 2, 1]
    
def test_reverse_table_even_list():
    """function testing the reversion of a table list
    with an even list
    """
    tab = [1, 2, 3, 4, 5, 6]
    assert algotools.reverse_table(tab) == [6, 5, 4, 3, 2, 1]