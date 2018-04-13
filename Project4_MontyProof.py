#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:02:11 2018

@author: lalitayang
"""

#starting point: each door is 1/3 probability containing car
p_door_1 = 1/3          #P(1)
p_door_2 = 1/3          #P(2)
p_door_3 = 1/3          #P(3)

#assume player chooses door 1
#given that player close door 1, what is the probability Monty chooses door 3
#conditional on where the prize is

p_door3_carIn1 = 1/2    #P(3|1)
p_door3_carIn2 = 1      #P(3|2)
p_door3_carIn3 = 0      #P(3|3)

#Bayes Theorem
# P(A|B) = (P(B|A) * P(A)) / P(B)
#Substitute for P(B) = P(3|1)*P(1) + P(3|2)*P(2) + P(3|3)*3


##Probability that car is in door 2 if Monty opens door 3 after player chooses door 1

#Substitute and solve P(2|3) 
#(P(3|2) * P(2)) / (P(3|1)*P(1) + P(3|2)*P(2) + P(3|3)*3)

carInDoor2_ifOpen3 = (p_door3_carIn2*p_door_2) / (p_door3_carIn1*p_door_1 + p_door3_carIn2*p_door_2 + p_door3_carIn3*p_door_3 ) 
print('Probability of winning if switch doors: ', carInDoor2_ifOpen3)

##Probability that car is in door 1 if Monty opens door 3 after player chooses door 1
#Substitute and solve P(1|3) 
#(P(3|1) * P(1)) / (P(3|1)*P(1) + P(3|2)*P(2) + P(3|3)*3)

carInDoor1_ifOpen3 = (p_door3_carIn1*p_door_1) / (p_door3_carIn1*p_door_1 + p_door3_carIn2*p_door_2 + p_door3_carIn3*p_door_3 ) 
print('Probability of winning if same door: ', carInDoor1_ifOpen3)

print('Switching doors has a higher probability of winning')
