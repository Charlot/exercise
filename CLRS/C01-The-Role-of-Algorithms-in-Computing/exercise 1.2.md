## 练习 1.2：
1.2-1 给出在应用层需要算法内容的应用的一个例子，并讨论涉及的算法的功能。
```
例子：车辆路径规划, Vehicle Routing Problem, VRP
算法：#TODO
```

1.2-2 假设我们正比较插人排序与归并排序在相同机器上的实现。对规模为n的输人，插人排序运行$8n^2$步，而归并排序运行$64nlgn$步。问对哪些n值，插人排序优于归并排序？

> 求解过程

$8n^2<64nlgn$

$n<-8lgn$

$lg2^n<lgn^8$

$2^n<n^8$

得出 n < 44的正整数

```
from sympy import *
x = symbols('x')
print(solve(2**x-x**8, x)[1].n())

# => 43.5592604368817
```


1.2-3 n的最小值为何值时，运行时间为$100n^2$的一个算法在相同机器上快于运行时间为$2^n$的另一个算法？
```
15

解法同上
(#=>14.3247278369982)
```

<br>
<br>

> 参考
- [VRP](https://en.wikipedia.org/wiki/Vehicle_routing_problem)

- [sympy-lambertw](https://docs.sympy.org/latest/modules/functions/elementary.html#lambertw)
