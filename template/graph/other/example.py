from typing import List


class Solution:
    @staticmethod
    def numberOfPaths(n: int, corridors: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/
        给定一个 n 个房间的迷宫，每个房间编号为 0 到 n - 1，迷宫中有一些门连接两个房间
        请问有几个长度为3的cycle
        :param n:
        :param corridors:
        :return:
        """
        graph = [set() for _ in range(n + 1)]
        for a, b in corridors:
            if a > b:
                a, b = b, a
            graph[a].add(b)
        ans = 0
        for a, b in corridors:
            for c in graph[a]:
                if c in graph[b]:
                    ans += 1
        return ans
