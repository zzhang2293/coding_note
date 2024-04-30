from typing import List


class Solution:
    @staticmethod
    def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
        """
        换根dp模版题
        给一棵树，求每个节点到其他节点的距离和

        :param n: node 数量
        :param edges: 边
        :return: 每个节点到其他节点的距离和
        """
        ans = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dfn = [-1] * n
        size = [1] * n
        number = 0

        def dfs1(node, pre):
            nonlocal number
            dfn[node] = number
            number += 1
            for nxt in graph[node]:
                if nxt != pre:
                    dfs1(nxt, node)
                    size[dfn[node]] += size[dfn[nxt]]
            return

        def dfs2(node, pre, dis):
            ans[0] += dis
            for nxt in graph[node]:
                if nxt != pre:
                    dfs2(nxt, node, dis + 1)
            return

        def dfs3(node, pre):
            ans[node] = ans[pre] - size[dfn[node]] + n - size[dfn[node]]
            for nxt in graph[node]:
                if nxt != pre:
                    dfs3(nxt, node)
            return

        dfs1(0, -1)
        dfs2(0, -1, 0)
        for nxt in graph[0]:
            dfs3(nxt, 0)
        return ans

    @staticmethod
    def minEdgeReversals(n: int, edges: List[List[int]]) -> List[int]:
        """
        换根dp https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
        :param n:
        :param edges:
        :return:
        """

        def dfs1(node, pre):
            ans = 0
            for nxt in graph[node]:
                if nxt != pre:
                    if (node, nxt) not in contain:
                        ans += 1
                    ans += dfs1(nxt, node)
            return ans

        def dfs2(node, pre):
            if ans[node] != -1:
                return
            if (pre, node) not in contain:
                ans[node] = ans[pre] - 1
            else:
                ans[node] = ans[pre] + 1
            for nxt in graph[node]:
                if nxt != pre:
                    dfs2(nxt, node)

        graph = [[] for _ in range(n)]
        contain = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            contain.add((a, b))

        ans = [-1] * n
        ans[0] = dfs1(0, -1)
        for nxt in graph[0]:
            dfs2(nxt, 0)
        return ans
