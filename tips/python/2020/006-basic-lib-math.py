# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:33:34 2020

@author: Charlot
"""

import math

# 返回 x 的上限，即大于或者等于 x 的最小整数
# /siːl/ 
print(math.ceil(3.3))


# 返回 x 的向下取整，小于或等于 x 的最大整数
print(math.floor(3.3))

# 返回 x 的绝对值。浮点数
print(math.fabs(-103))

# 以一个整数返回 x 的阶乘
print(math.factorial(5))

# 返回迭代中的精确浮点值。通过跟踪多个中间部分和来避免精度损失
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) # 0.9999999999999999

# 返回非负整数 n 的整数平方根。 # python3.8
# print(math.isqrt(2.1))

#返回 x 以2为底的对数。这通常比 log(x, 2) 更准确。
print(math.log2(10))
print(math.log(10,2))

# 将返回 x 的 y 次幂。与内置的 ** 运算符不同， math.pow() 将其参数转换为 float 类型。使用 ** 或内置的 pow() 函数来计算精确的整数幂。
print(2**3) # 8
print(math.pow(2,3)) # 8.0


## 三角函数
# sin cos tan

## 常量
print(math.pi)
print(math.e)
# 浮点数正无穷
print(math.inf)
# 浮点“非数字”（NaN）值。 相当于 float('nan') 的输出。
print(math.nan)
