# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:10:22 2020

@author: Charlot
"""

# /'enəm/ 
from enum import Enum,unique

@unique # 禁止值相同
class Color(Enum):
    Red=1
    Blue='b'
    
print(Color.Red)
print(Color.Blue)
print(repr(Color('b')))