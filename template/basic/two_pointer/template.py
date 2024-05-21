from collections import Counter
from typing import List


class TwoPointer:
    @staticmethod
    def countPairs(n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        https://leetcode.cn/problems/count-pairs-of-nodes/description/
        双指针，哈希
        :param n:
        :param edges:
        :param queries:
        :return:
        """
        cnt = Counter()
        deg = [0] * (n + 1)
        for a, b in edges:
            if a > b:
                a, b = b, a
            cnt[(a, b)] += 1
            deg[a] += 1
            deg[b] += 1
        deg.sort()
        ans = []
        for q in queries:
            l, r = 1, n
            cur = 0
            while l < r:
                if deg[l] + deg[r] <= q:
                    l += 1
                else:
                    cur += r - l
                    r -= 1
            for (a, b), c in cnt.items():
                if deg[a] + deg[b] > q > deg[a] + deg[b] - c:
                    cur -= 1
            ans.append(cur)
        return ans







