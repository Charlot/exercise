# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:24:17 2020

@author: Charlot
"""

import string
import datetime

#使用逗号作为千位分隔符:
print('{:,}'.format(1234567890))
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
#填充
print('{:0>5}'.format('abcd'))