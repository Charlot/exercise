# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:15:18 2020

@author: Charlot
"""

def fib(n):
    a,b=0,1
    while a<n :
        print(a,end=' ')
        a,b=b,a+b
        
fib(100)