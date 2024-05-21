import bisect
import math
from collections import Counter
from functools import cache
from math import inf
from typing import List
import heapq


def find(x):
    if x != father[x]:
        father[x] = find(father[x])
    return father[x]


def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa != fb:
        father[fb] = fa
        return True
    return False


graph = []
father = []
dist = {}


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        edgeList.sort(key=lambda x: x[2])
        edge = []
        for i in range(n):
            graph.append([])
        for i in range(n):
            father.append(i)

        for a, b, v in edgeList:
            if union(a, b):
                edge.append([a, b, v])

        for a, b, v in edge:
            graph[a].append([b, v])
            graph[b].append([a, v])

        vis = set()
        for i in range(n):
            fa = find(i)
            if fa not in vis:
                vis.add(fa)
                dist[fa] = [inf] * n
                dist[fa][fa] = 0
                heap = [[fa, 0]]
                while heap:
                    node, dis = heapq.heappop(heap)
                    for nxt, d in graph[node]:
                        if d + dis < dist[fa][nxt]:
                            dist[fa][nxt] = d + dis
                            heapq.heappush(heap, [nxt, dis + d])

    def query(self, p: int, q: int, limit: int) -> bool:
        def check(node, pre, target):
            if node == target:
                return True
            for nxt, dis in graph[node]:
                if nxt != pre and check(nxt, node, target):
                    return True
            return False

        ans = inf

        def dfs(node, pre, a, b):
            nonlocal ans
            if node == a:
                if check(node, pre, b):
                    ans = min(ans, dist[roota][b] - dist[roota][a])
                return node

            if node == b:
                if check(node, pre, a):
                    ans = min(ans, dist[roota][a] - dist[roota][b])
                return node
            res = []
            for nxt, dis in graph[node]:
                if nxt != pre:
                    cur = dfs(nxt, node, a, b)
                    if cur:
                        res.append(cur)
            if len(res) == 0:
                return None
            if len(res) == 1:
                return node
            if len(res) == 2:
                ans = dist[roota][a] - dist[roota][node] + dist[roota][b] - dist[roota][node]
                return node

        roota = find(p)
        rootb = find(q)
        if p == 1 and q == 3:
            print(ans)
        if roota != rootb:
            return False
        dfs(roota, -1, p, q)

        return ans < limit

obj = DistanceLimitedPathsExist(6,[[0,2,4],[0,3,2],[1,2,3],[2,3,1],[4,5,5]])
print(obj.query(2, 0, 3))

