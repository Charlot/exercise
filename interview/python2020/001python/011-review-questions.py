# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:49:04 2020

@author: Charlot
"""
# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

print(list(filter(lambda x:x>10,map(lambda x:x*x,[1,2,3,6,6,8]))))

import numpy as np

print(np.random.randn(5))


import re

s = '<div class="nam">中国</div>'
print(re.findall(r'<div class=".*">(.*)</div>',s))

a = "not 404 found 张三 99 深圳"

# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"a,d,f,j,l"
print(','.join( sorted( set( "ajldjlajfdljfddd"))))

# 用lambda函数实现两个数相乘
print((lambda x,y:x*y)(10,3))

#24、字典根据键从小到大排序

dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

print(sorted(dic.items(),key=lambda d:d[0]))

print(list(zip([1,2,3],[4,5,6])))
a=[[1,2],[3,4],[5,6]]
print([j for i  in a for j in i])
import numpy as np
print(np.array([1,2]).flatten().tolist())

print('abc'.join('dff'))

import re
print(re.sub(r'\d+','100','张明 98分'))

print(list({'1':1}.items()))


print([ '%s*%s=%s'%(x,y,x*y)   for x in range(1,10) for y in range(x,10)])