## 练习 2.3：

2.3-1 使用图2-4做为模型，说明递归排序在数组A=<3,41,52,26,38,57,9,49>上的操作；

> EN

Using Figure 2.4 as a model, illustrate the operation of merge sort on the array
A=<3,41,52,26,38,57,9,49>.

> 说明

![operation](/CLRS/attach/clrs-e-2-3-1.png)

2.3-2 重写MERGE过程，使之不使用哨兵(sentinel)，而是一旦数组L或R的所有元素均被复制回A就立刻停止。然后把另一个数组的剩余部分复制回A。

> EN

Rewrite the MERGE procedure so that it does not use sentinels, instead stopping
once either array L or R has had all its elements copied back to A and then copying
the remainder of the other array back into A.

> 伪代码
```
MERGE(A, p, q, r):
    L = A[p..q]
    R = A[q + 1..r]
    n1 = q - p + 1
    n2 = r - q
    let L[1..n1] and R[1..n2] be new arrays
    // 复制数组
    for i = 1 to n1
        L[i] = A[p + i - 1]
    for j = 1 to n2
        R[j] = A[q + j]

    i = 1
    j = 1
    
    for k = p to r
        if i > n1
            // 将R剩下的拷贝到A中
            A[k] = R[j]
            j = j + 1
        else if j > n2
            // 将L剩下的拷贝到A中
            A[k] = L[i]
            i = i + 1
        else if L[i] ≤ R[j]
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
```

2.3-3 使用数学归纳法(mathematical induction)证明：当n正好是2的幂时，以下递归式的解是T(n)=nlgn。

![recurrence](/CLRS/attach/clrs-e-2-3-2.png)

> EN

Use mathematical induction to show that when n is an exact power of 2, the solution
of the recurrence

> 证明

证明：当n=2时，根据递归式T(n) = 2 = 2lg2，递归式成立；

假设：当n=2^k时，递归式成立，有T(n) = 2T(n/2)+n = nlgn = 2^klg2^k = k*2^k

证明：当n=2^(k+1)时，递归式成立：
T(2^(k+1)) = 2T((2^(k+1))/2)+2^(k+1)
         = 2T(2^k)+2^(k+1)
         = 2*(k*2^k)+2^(k+1)
         = 2^(k+1)*(k+1)
         = 2^(k+1)*lg2^(k+1)
         = nlgn

结论： 当n正好是2的幂时，递归式的解是T(n)=nlgn。

2.3-4 我们可以把插人排序表示为如下的一个递归过程。为了排序A[1..n]，我们递归地排序A[1..n-1]，然后把A[n]插人已排序的数组A[1..n-1]。为插人排序的这个递归版本的最坏情况运行时间写一个递归式。

> 伪代码
```
INSERTION-SORT-RECURSION(A)
    n = A.length
    INERTION-SORT-RECURSION(A[1..n-1])
    INSERT(A,n)

INSERT(A,n)
    key = A[n]
    i = n - 1
    while i >0 and A[i] > key
        A[i + 1] = A[i]
        i = i -1
    A[i] = key    
```

>递归式

![recurrence](/CLRS/attach/clrs-e-2-3-4.png)

2.3-5 回顾查找问题(参见练习2.1-3)，注意到，如果序列A已经排好序，就可以将该序列的中点与v进行比较。如果根据比较结果，原序列中有半就不用再做进一步的考虑了。二分查找重复这个过程，每次都将序列剩余部分的规模减半。为二分查找写出迭代或者递归的伪代码。证明：二分查找的最坏情况运行时间为Θ(lgn)。

>伪代码
```
BINARY-SEARCH(A, v, l, h)
    if l > h
        return NIL
    mid = ⌈(l + h) / 2⌉ // ceil(*(l+h)/2)
    if A[mid] == v
        return mid
    else if v > A[mid]
        return BINARY-SEARCH(A, v, mid + 1, h)
    else
        return  BINARY-SEARCH(A, v, l, mid - 1)
```

2.3-6 注意到2.1节中的过程INSERTION-SORT的第5~7行的while循环采用一种线性查找来（反向）扫描已排好序的子数组A[1..j-1]。我们可以使用二分查找（参见练习2.3一5)来把插人排序的最坏情况总运行时间改进到Θ(nlgn）吗？

>伪代码
```
BINARY-INSERTION-SORT(A)
    for j in 2 to A.length
        m = A[j]
        // 找到位置
        i = BINARY-SEARCH(A, m, 1, A.length - 1)
        // 移动数值
        for k in j to i:
            tmp = A[k]
            A[k] = A[k-1] 
            A[k-1] = tmp
        A[i] = m
```

> 是否可以改进
```
不可以。
查找的时间减低，但是第一个循环和交换数据的循环执行总时间最坏为：Θ(n^2)
```

2.2-7 描述一个运行时间为0(nlgn）的算法，给定n个整数的集合S和另一个整数x，该算法能确定S中是否存在两个其和刚好为x的元素。
> 可以
> 将x与S中的每个元素相减，得到新集合S1。便利S1，在S中二分查找，如果S1中的元素存在S中，即可确定。
> 且运行时间为Θ(nlgn)



## 思考题 2.3：
思考题
2-1（在归并排序中对小数组采用插入排序）虽然归并排序的最坏情况运行时间为Θ(nlgn),而插人排序的最坏情况运行时间为Θ(n^2)，但是插人排序中的常量因子可能使得它在n较小时，在许多机器上实际运行得更快。因此，在归并排序中当子问题变得足够小时，采用插入排序来使递归的叶变粗是有意义的。考虑对归并排序的一种修改，其中使用插入排序来排序长度为k的n/k个子表，然后使用标准的合并机制来合并这些子表，这里k是一个待定的值。
a. 证明：插入排序最坏情况可以在Θ(nk）时间内排序每个长度为k的n/k个子表。

b. 表明在最坏情况下如何在Θ(nlg(n/k)）时间内合并这些子表。

c. 假定修改后的算法的最坏情况运行时间为Θ(nk+nlg(n/k))，要使修改后的算法与标准的归并排序具有相同的运行时间，作为n的一个函数，借助Θ记号，k的最大值是什么？

d. 在实践中，我们应该如何选择k?

> 解答

> a

每个子列表最坏情况为Θ(k^2), n/k个为线性关系，Θ(k^2)*(n/k)=Θ(nk)

> b
 
![recursion tree](/CLRS/attach/clrs-e-2-3-p-1.png)

根据递归树分析，每层总代价为cn，最底层子表个数为n/k个，代表递归树为 lgn/k+1 层。
故总代价为 cnlg(n/k)+cn = Θ(nlg(n/k)）

> c

nk+nlg(n/k) = nlgn

k = 









2-2（冒泡排序的正确性）冒泡排序是一种流行但低效的排序算法，它的作用是反复交换相邻的未按次序排列的元素。
```
BUBBLESORT(A)
1 for i=1 to A.length-1
2  for i=A.length downto i+1
3   if A[j]＜A[j-1]
4    exchange A[j] with a[j-1]
```
a. 假设A'表示BUBBLESORT(A)的输出。为了证明BUBBLSORT正确，我们必须证明它将终止并且有：
A'[1]≤A'[2]≤....≤A'[n]       (2.3)
其中n=A.length。为了证明BUBBLESORT确实完成了排序，我们还需要证明什么？下面两部分将证明不等式(2.3)。

b. 为第2~4行的for循环精确地说明一个循环不变式，并证明该循环不变式成立。你的证明应该使用本章中给出的循环不变式证明的结构。

c. 使用（b）部分证明的循环不变式的终止条件，为第1~4行的for循环说明一个循环不变式，该不变式将使你能证明不等式(2.3)。你的证明应该使用本章中给出的循环不变式证明的结构。

d. 冒泡排序的最坏情况运行时间是多少？与插人排序的运行时间相比，其性能如何？


2-3（霍纳（Horner）规则的正确性）给定系数$a_0, a_1, \ldots, a_n$和x的值，代码片段
```
1 y = 0
2 for i = n downto 0
3    y = a[i] + x * y
```

实现了用于求值多项式
$$ \begin{aligned} P(x) & = \sum_{k = 0}^n a_k x^k \\ & = a_0 + x(a_1 + x (a_2 + \cdots + x(a_{n - 1} + x a_n) \cdots)) \end{aligned} $$
的霍纳规则。

a. 借助Θ记号，实现霍纳规则的以上代码片段的运行时间是多少？

b.编写伪代码来实现朴素的多项式求值算法，该算法从头开始计算多项式的每个项。该算法的运行时间是多少？与霍纳规则相比，其性能如何？

c. 考虑以下循环不变式：
在第2~3行for循环每次迭代的开始有
$$y = \sum_{k = 0}^{n - (i + 1)} a_{k + i + 1} x^k$$
把没有项的和式解释为等于0。遵照本章中给出的循环不变式证明的结构，使用该循环
不变式来证明终止时有 

$$y = \sum_{k = 0}^n a_k x^k$$

d．最后证明上面给出的代码片段将正确地求由系数$a_0, a_1, \ldots, a_n$刻画的多项式的值。

![correction of horner's rule](/CLRS/attach/clrs-e-2-3-p-3.png)


2-4（逆序对）假设A[1..n]是一个有n个不同数的数组。若i<j且A[i]>A[j]，则对偶(i,j）称为A的一个逆序对（inversion）。

a. 列出数组（2,3,8,6,1）的5个逆序对。

b. 由集合{1,2，…，n｝中的元素构成的什么数组具有最多的逆序对？它有多少逆序对？

c. 插人排序的运行时间与输人数组中逆序对的数量之间是什么关系？证明你的回答。

d. 给出一个确定在n个元素的任何排列中逆序对数量的算法，最坏情况需要Θ(nlgn）时间。
（提示：修改归并排序。）