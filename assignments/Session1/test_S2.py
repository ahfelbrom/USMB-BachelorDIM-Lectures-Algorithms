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