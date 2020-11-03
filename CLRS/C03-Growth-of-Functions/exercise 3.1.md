## 练习 3.1：

**3.1-1** 假设f(n)与g(n)都是渐进非负函数。使用Θ记号的基本定义来证明max(f(n),g(n))=Θ(f(n)+g(n))

![theta](../attach/clrs-e-3-1-1.png)

**3.1-2** 证明：对任意实常量a和b，其中b>0，有 (n+a)^b=Θ(n^b)

> 解答

(n+a)^b可以化为二项式：n^b+b*n^(b-1)a+...a^b, 舍弃低次项可得Θ(n^b)


> 参考
- [二项式展开(Binomial Expantion)](https://www.shuxuele.com/algebra/binomial-theorem.html)

- [二项式展开(Binomial Expantion)](https://studywell.com/maths/pure-maths/sequences-series/binomial-expansion/)


**3.1-3** 解释为什么“算法A的运行时间至少是O(n^2)”这一表述是无意义的。

#TODO

参考:
- https://stackoverflow.com/questions/15196004/running-time-of-algorithm-a-is-at-least-on%C2%B2-why-is-it-meaningless
