## 相邻合并 -> 连续子数组合并
题目说明了是相邻合并，可以去考虑是不是连续子数组合并问题。

## 试填法
对于位运算题目，试填法是从高位到低位构建答案

## 切比雪夫距离
曼哈顿距离往往可以转换成一个切比雪夫距离问题
`a` 到 `b` 距离 从曼哈顿距离转换为切比雪夫距离方式为：
```python
a = [1, 2]
b = [3, 4]
# 曼哈顿距离
m1 = abs(a[0] - b[0] + a[1] - b[1])
# 切比雪夫坐标
a1 = [a[1] + a[0], a[1] - a[0]]
b1 = [b[1] + b[0], b[1] - b[0]]
m2 = max(abs(a1[0] - b1[0]), abs(a1[1] - b1[1]))
```
通过这个方式可以把结果放进一个`sortedcontainers` 的 `SortedList` 里面，求出最大距离。

## Trie 树 通过 pair 打包多个信息
当一道问题需要同时处理前后缀的时候，可以考虑使用 Trie 树，通过 pair 打包多个信息。例如：
当我想查询一个字符串是否为另一个字符的前后缀时候，可以把前后缀依次打包，`abc` 可以打包成 `ac` `bb` `ca`，然后查询的时候，只需要查询是否存在即可。

## 中位数贪心
中位数贪心是一种常见的贪心策略，通过中位数来进行贪心。
货仓选址问题，可以通过中位数贪心来解决。

## 树上异或
当我想要异或树上的一个路径上的所有数字，只有首尾会被异或，中间的数字会被消掉。

## index 对称点
当我的index为`i`的时候，对称点为`n - i - 1`

## 计算子数组or的高效方式
简单来说就是去重，因为至多32个不同的值所以不需要loop `n ^ 2` 次
```python
from typing import List
def smallestSubarrays(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ors = [] # tuple: 或运算值，对应子数组最小值
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        num = nums[i]
        ors.append([0, i])
        l = 0
        for pair in ors:
            pair[0] |= num
            if ors[l][0] == pair[0]:
                ors[l][1] = pair[1]
            else:
                l += 1
                ors[l] = pair
        del ors[l + 1:]
        ans[i] = ors[0][1] - i + 1
    return ans
```
```python
from typing import List
# 只问个数的解法
def closestToTarget(self, arr: List[int], target: int) -> int:
    ans = set()
    ands = set()
    for x in arr:
        ands = {o & x for o in ands}
        ands.add(x)
        ans |= ands
    return len(ans)
```

这种方式能计算出子数组的或值，同时保留了对应的最小index，
inner for loop最多执行32次，因为每一位上or的结果只有可能从0变成1
而不会从1变成0。

## 懒删除堆
懒删除堆可以用`multiset` 或者 `SortedList` 来替代

## 给string打标记

把每个字符串转换成一个整数编号，这一步可以用字典树完成
```python
class Node:
    def __init__(self):
        self.nxt = [None] * 26
        self._id = -1
        
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]):
        root = Node()
        uid = 0
        offset = ord('a')

        def put(s: str):
            nonlocal uid
            cur = root
            for c in s:
                if not cur.nxt[ord(c) - offset]:
                    cur.nxt[ord(c) - offset] = Node()
                cur = cur.nxt[ord(c) - offset]
            if cur._id == -1:
                cur._id = uid
                uid += 1

            return cur._id
```

## 生成回文数
一种高效生成回文数字的方式，给定一个范围
```python
        # 严格按顺序从小到大生成所有回文数（不用字符串转换）
        pal = []
        base = 1
        while base <= 10000:
            # 生成奇数长度回文数
            for i in range(base, base * 10):
                x = i
                t = i // 10
                while t:
                    x = x * 10 + t % 10
                    t //= 10
                pal.append(x)
            # 生成偶数长度回文数
            if base <= 1000:
                for i in range(base, base * 10):
                    x = t = i
                    while t:
                        x = x * 10 + t % 10
                        t //= 10
                    pal.append(x)
            base *= 10
        pal.append(1_000_000_001) 
```

## 归纳法

假设某一种情况成立，然后新来一个值，想一想如何去组成新的思路

## 逆元模版

```python
mod = 10 ** 9 + 7
mx = 100_000
fac = [0] * mx
for i in range(1, mx):
    fac[i] = fac[i - 1] * i % mod
inv_fac = [0] * mx
inv_fac[mx - 1] = pow(fac[mx - 1], -1, mod)

for i in range(mx - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % mod


def comb(n, k):
    return fac[n] * inv_fac[k] % mod * inv_fac[n - k] * mod
```

## floyd tortoise

```python
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    # Initialize two pointers, slow and fast, to the head of the linked list.
    slow = head
    fast = head

    # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
    # until they either meet or the fast pointer reaches the end of the list.
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        # If the pointers meet, there is a cycle in the linked list.
        # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
        # until they meet again. The node where they meet is the starting point of the cycle.
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    # If the fast pointer reaches the end of the list without meeting the slow pointer,
    # there is no cycle in the linked list. Return None.
    return None
```

## 寻找图最小环

用bfs，然后把过去的距离存在一个dict里面，
然后如果`nxt` 已经vis过了，那么说明一定有环，就用`dict[nxt] + dict[cur] + 1`得出最小环长度

## 前缀和约束

当条件为多个条件时候，用 `pair` 的方式来存储所有条件

## 同余原理 之分解
`(a - b) % k = 0 -> a % k = b % k`

## 公式化简
如果公式 要求 求出 `target ^ 2 ...` 的一个解，尝试化简平方


## bit operation

`a & ~b` is `a - b` remove all the element in b from a 

## 欧拉回路

**欧拉路径**：
如果在一张图中，可以从一点出发遍历所有的边，
那么遍历过程中的这条路径就叫做欧拉路径。如果这条路径是闭合的，
那就称为欧拉回路

**欧拉图判定** 如果可以从一点出发到所有的边，那么过程中这个路径是欧拉路径， 如果这条路是闭合的，那么就是欧拉回路
无向图中， 如果所有的定点的degree都是偶数，则为欧拉图，如果有两个点是奇数，则为半欧拉图


