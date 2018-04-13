#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:34:10 2018

@author: lalitayang
"""

import numpy as np
import scipy as sp
import pandas as pd
from scipy.stats import ttest_1samp

#Read in data from URL using pandas
data = pd.read_table('https://ww2.amstat.org/publications/jse/datasets/normtemp.dat.txt', 
                     header=None,
                     sep="   ",
                     names=['body_temp', 'sex', 'heart_rate'],
                     engine='python')

data.describe()

#manually calculate the t-statistic
temp_mean = data['body_temp'].mean()
mu = 98.6
s = data['body_temp'].std()
n = len(data['body_temp'])
dof = len(data) - 1
t = (temp_mean - mu)/(s/np.sqrt(n))

print('sample mean: ', temp_mean)
print('t-statistic: ', t)

print('sample mean: ', temp_mean)
print('t statistic: ',  ttest_1samp(data['body_temp'], mu ))

