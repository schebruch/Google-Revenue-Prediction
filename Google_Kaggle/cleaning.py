# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:38:25 2018

@author: scheb
"""

#imports
import numpy
import pandas
import matplotlib
import json

#loading the data
train = pandas.read_csv("train.csv")
test = pandas.read_csv("test.csv")

#dropping sessionId and visitId since they have no predictive power
train.drop('sessionId', axis=1, inplace=True)
train.drop('visitId', axis = 1, inplace = True)

