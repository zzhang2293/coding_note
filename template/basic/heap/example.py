import heapq
from typing import List


class Solution:
    @staticmethod
    def leftmostBuildingQueries(buildings: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        题目介绍：leetcode 2904
        离线处理 + 小根堆
        离线处理含义：不需要按照顺序处理 queries，可以先按自己的想法处理 queries，然后再按照顺序输出结果
        :param buildings: 建筑物高度
        :param queries: 查询的位置
        :return: 查询结果
        """

        n = len(buildings)
        group = [[] for i in range(n)]
        ans = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or buildings[a] < buildings[b]:
                ans[i] = b
            else:
                group[b].append([buildings[a], i])
        heap = []
        for i in range(n):
            for a, idx in group[i]:
                heapq.heappush(heap, [a, idx])
            while heap and heap[0][0] < buildings[i]:
                a, idx = heapq.heappop(heap)
                ans[idx] = i
        return ans
