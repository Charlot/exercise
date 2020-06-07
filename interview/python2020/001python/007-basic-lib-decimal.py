# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:53:05 2020

@author: Charlot
"""

from decimal import *

print(Decimal('-7')%Decimal(4))


# 返回活动线程的当前上下文。
print(getcontext()) # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])



#返回一个上下文管理器，它将在进入 with 语句时将活动线程的当前上下文设为 ctx 的一个副本并在退出 with 语句时恢复之前的上下文。 如果未指定上下文，则会使用当前上下文的一个副本。
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 42   # Perform a high precision calculation
    s = calculate_something()
s = +s  # Round the final result back to the default precision