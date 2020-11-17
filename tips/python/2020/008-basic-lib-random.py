# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:36:13 2020

@author: Charlot
"""

from random import *
#返回 [0.0, 1.0) 范围内的下一个随机浮点数
print(random())

print(randrange(2, 10))

print(choice(['a','b','c']))

a=['a','b','c']
shuffle(a)
print(a)
