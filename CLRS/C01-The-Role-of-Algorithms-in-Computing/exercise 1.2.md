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

## 思考题 1.2：
1-1（运行时间的比较）假设求解问题的算法需要f(n)毫秒，对下表中的每个函数f(n)和时间
t，确定可以在时间t内求解的问题的最大规模n。

|  | 1秒钟 | 1 分钟 |
| --- | --- | --- |
| $lgn$ | $2^{10^6}$ | $2^{6*10^7}$|
| $\sqrt n$ | $10^{12}$ | $3.6*10^{15}$|
| $n$ | $10^6$ | $6*10^7$ |
| $nlgn$ | $6.2*10^4$ | $2.8*10^6$ | 
| $n^2$ | $10^3$ | $7.7*10^3$ |
| $n^3$ | $10^2$ | $3.9*10^2$ |
| $2^n$ | 19 | 25 |
| $n!$ | 9 | 11 |
|  |  |  |



<br>
<br>

> 参考
- [VRP](https://en.wikipedia.org/wiki/Vehicle_routing_problem)

- [sympy-lambertw](https://docs.sympy.org/latest/modules/functions/elementary.html#lambertw)
