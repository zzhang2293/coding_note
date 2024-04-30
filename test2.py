from heapq import heappush, heappop
from math import inf
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:

        def get_cnt_of_shortest_path(graph, src: int, dst: int):

            """
            输出最短距离的数量
            :param dst: 终点
            :param graph: 图
            :param src: 起点
            :return:
            """

            n = len(graph)
            cnt = [0] * n
            cnt[0] = 1
            dist = [inf] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                dis, node = heappop(heap)
                if dist[node] < dis:
                    continue
                for nxt, d, idx in graph[node]:
                    if dist[nxt] == d + dis:
                        cnt[nxt] += cnt[node]
                        come[nxt].append(idx)
                        come[nxt].extend(come[node])
                    elif dist[nxt] > d + dis:

                        dist[nxt] = d + dis
                        cnt[nxt] = cnt[node]
                        come[nxt] = [idx]
                        come[nxt].extend(come[node].copy())
                        heappush(heap, (dis + d, nxt))
            return cnt[dst]

        graph = {i: [] for i in range(n)}
        for i, (a, b, v) in enumerate(edges):
            graph[a].append([b, v, i])
            graph[b].append([a, v, i])

        come = {i: [] for i in range(n)}
        get_cnt_of_shortest_path(graph, 0, n - 1)
        m = len(edges)
        ans = [False] * m
        for val in come[n - 1]:
            ans[val] = True
        return ans


n = 6
print(int('0011', 2))