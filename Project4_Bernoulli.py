#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:05:33 2018

@author: lalitayang
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def bernoulli_trials(n, p):
    """Perform n Bernoilli trials with success
    probability p and return number of successes"""
    
    n_success = 0
        
    for i in range(n):
        rand_n = np.random.random()
        
        if rand_n < p:
            n_success += 1
    
    return n_success
    
n_heads = np.empty(5000)

for i in range(5000):
    n_heads[i] = bernoulli_trials(1000, 0.5)

plt.hist(n_heads)
plt.xlabel('Number of heads out of 1000 flips')
plt.ylabel('Number of trials out of 5000')
plt.show()
