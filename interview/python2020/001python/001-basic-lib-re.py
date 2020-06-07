# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:15:22 2020

@author: Charlot
"""

import re

ma=re.match('a', 'caba')
print(ma)


se=re.search('a', 'caba')
print(se)

sp=re.split('a','caba')
print(sp)