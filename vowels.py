# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:54:56 2020

@author: Prerna Sharma
"""

states=['Alabama','California','Oklahoma','Florida]
str1="
list1=[]

for items in states:
    for letter in item:
        if letter not in "aeiouAEIOU":
            str1=str1+letter
    list1.append(str1)
    str1="
print(list1)