## 练习 1.1：
1.1-1 给出现实生活中需要排序的一个例子或者现实生活中需要计算凸壳的一个例子。
```
排序：成绩排序、基金收益排序
凸壳：图像处理等(#TODO)
```

1.1-2 除速度外，在真实环境中还可能使用哪些其他有关效率的量度？
```
与计算机软件系统相关的
- 内存使用量
- 磁盘读写速度
```

1.1-3 选择一种你以前已知的数据结构，并讨论其优势和局限。
```
数组：
优势：读取效率高；
局限：长度不可变
```

1.1-4 前面给出的最短路径与旅行商问题有哪些相似之处？又有哪些不同？
```
最短路径问题：SPP
旅行商问题：TSP
相似点: 
- 图论路径问题，根据图边权重求其和最小值；

不同点：
- SPP访问图中某些点(或全部顶点)，TSP访问全部顶点；
- SPP不需要回到原点，TSP需要(环)；
- SPP不可重复访问图顶点，TSP可以；
- 问题复杂度：SPP vs TSP = P VS NPC
```


1.1-5 提供一个现实生活的问题，其中只有最佳解才行。然后提供一个问题，其中近似最佳的一个解也足够好。
```
最佳解：
如果我和你妈同时掉河里，你先救谁？

近似解：
这么多包包哪款好看呀？
```


<br>
<br>

> 参考
- [凸壳](https://zh.wikipedia.org/wiki/%E5%87%B8%E5%8C%85)
- [最短路径问题](https://zh.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E8%B7%AF%E9%97%AE%E9%A2%98)
- [旅行商问题](https://zh.wikipedia.org/wiki/%E6%97%85%E8%A1%8C%E6%8E%A8%E9%94%80%E5%91%98%E9%97%AE%E9%A2%98)