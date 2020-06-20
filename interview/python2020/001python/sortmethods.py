# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:51:36 2020

@author: Charlot
"""

import random
import copy
"""
插入排序
"""
def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j>-1 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
"""
选择排序
"""
def selectinsert(arr):
    sortedarr=[]
    for i in range(0,len(arr)):
        key = i
        for j in range(i,len(arr)):
            if arr[key] > arr[j]:
                key = j
        arr[i],arr[key]=arr[key],arr[i]
      
"""
冒泡排序
"""
def bubblesort(arr):
    for i in range(0,len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
"""
快速排序
"""
def quicksort(arr):
    pass
            
if __name__=='__main__':
    arr=[1,3,4,2,5,8,3,1,9,0,0]
    
    insertarr=copy.copy(arr)
    insertionsort(insertarr)
    print(insertarr)    
    
    selectarr=copy.copy(arr)
    selectinsert(selectarr)
    print(selectarr)    

    
    bubbulearr=copy.copy(arr)
    bubblesort(bubbulearr)
    print(bubbulearr)    

