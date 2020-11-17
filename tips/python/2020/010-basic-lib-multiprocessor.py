# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:37:04 2020

@author: Charlot
"""

import os
import time
from multiprocessing import Process

def run(name):
  #  while True:
  #      time.sleep(2)
  print("子进程ID:%s, run:%s"%(os.getpid(),name))
        
if __name__ == '__main__':
      # 创建子进程
    p = Process(target=run,args=('Alia',))
    p.start()
    print('父进程启动: %d'%os.getpid())
  
   # p.join()
   # while True:
   #     print("死循环")
   #     time.sleep(1)
    
    
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
        
        
        
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)        