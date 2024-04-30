import heapq
from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    @staticmethod
    def isEscapePossible(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        BFS + 给定障碍物能围的最大面积
        :param blocked:
        :param source:
        :param target:
        :return:
        """
        base = 131
        step = [-1, 0, 1, 0, -1]
        edge = 10 ** 6
        mx = 10 ** 5
        blocked = {x * base + y for x, y in blocked}

        def check(a, b):
            vis = set()
            lst = deque([a])
            while lst and len(vis) <= mx:
                x, y = lst.popleft()
                if x == b[0] and y == b[1]:
                    return True
                if base * x + y in vis or base * x + y in blocked:
                    continue
                vis.add(base * x + y)
                for c, d in pairwise(step):
                    i, j = x + c, y + d
                    if 0 <= i < edge and 0 <= j < edge and i * base + j not in vis and i * base + j not in blocked:
                        lst.append([i, j])
            return len(vis) > mx

        return check(source, target) and check(target, source)

    @staticmethod
    def minPushBox(grid: List[List[str]]) -> int:
        """
        最小推箱子到终点次数
        人和箱子重叠后，我知道箱子的位置，我也知道人从哪里来，我就可以知道下一步箱子会移动到哪里
        然后我判断这个位置是否合法，合法就可以移动
        :param grid:
        :return:
        """

        def get_hash(x, y):
            return x * base + y

        vis = set()
        base = 10 ** 9 + 7
        people_pos = None
        box_pos = None
        dest_pos = None
        step = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    box_pos = [i, j]
                if grid[i][j] == 'S':
                    people_pos = [i, j]
                if grid[i][j] == 'T':
                    dest_pos = [i, j]

        heap = [[0, box_pos[0], box_pos[1], people_pos[0], people_pos[1]]]
        while heap:
            dis, bx, by, px, py = heapq.heappop(heap)
            if bx == dest_pos[0] and by == dest_pos[1]:
                return dis
            if (get_hash(bx, by), get_hash(px, py)) in vis:
                continue
            vis.add((get_hash(bx, by), get_hash(px, py)))
            for a, b in pairwise(step):
                pa = px + a
                pb = py + b
                if not 0 <= pa < m or not 0 <= pb < n or grid[pa][pb] == '#':
                    continue
                if pa == bx and pb == by:
                    ba, bb = bx + a, by + b
                    if 0 <= ba < m and 0 <= bb < n and grid[ba][bb] != '#' and (get_hash(ba, bb), get_hash(pa, pb)) not in vis:
                        heapq.heappush(heap, [dis + 1, ba, bb, pa, pb])
                elif (get_hash(bx, by), get_hash(pa, pb)) not in vis:
                    heapq.heappush(heap, [dis, bx, by, pa, pb])

        return -1
