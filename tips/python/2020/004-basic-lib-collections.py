# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:39:53 2020

@author: Charlot
"""

from collections import deque

d=deque()
d.append(1)
d.appendleft(0)
d.append(2)
d.append(3)

for i in d:
    print(i)

print(d.pop())
print(d.popleft())

print(list(d))
print(list(reversed(d)))



from collections import Counter

c=Counter(['a','b','c','a'])
print(c['a'])
print(c['d']) # 0
print(c) # Counter({'a': 2, 'b': 1, 'c': 1})

from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
    
print(dict(d))    

