# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:15:41 2017

@author: alexis
"""

import S1_algotools as algotools

def test_average_above_zero_one_value_under_zero():
    tab = [-1, 0, 1, 2, 7, 3, 4]
    assert algotools.average_above_zero(tab) == 3.4
