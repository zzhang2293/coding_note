from typing import List


def euler(n: int) -> list:
    visit = [False for _ in range(n + 1)]
    prime = []
    for i in range(2, n + 1):
        if not visit[i]:
            prime.append(i)
        for j in range(len(prime)):
            if i * prime[j] > n:
                break
            visit[i * prime[j]] = True
            if i % prime[j] == 0:
                break
    return prime


class Solution:
    @staticmethod
    def countPaths(n: int, edges: List[List[int]]) -> int:
        """
        给一个无向树，edges是树的边，求满足以下条件的路径数量，统计一共有多少路径，使得路径上的所有节点的度数正好是一个
        这道题的关键是找到度数为质数的节点，然后对于每一个质数节点，找到它的子节点，然后对于每一个子节点，找到它的子节点
        类似洪水填充的思想
        :param n:
        :param edges: 无向树的边
        :return:
        """
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ans = 0

        def dfs(node, pre):
            if node in prime:
                return
            nodes.append(node)
            for a in graph[node]:
                if a != pre:
                    dfs(a, node)
            return

        prime = set(euler(n))
        size = [0] * (n + 1)
        ans = 0
        for i in range(1, n + 1):
            if i in prime:
                s = 0
                for nxt in graph[i]:
                    if nxt == i:
                        continue
                    if nxt in prime:
                        continue
                    if size[nxt] == 0:
                        nodes = []
                        dfs(nxt, i)
                        for j in nodes:
                            size[j] = len(nodes)
                    ans += s * size[nxt]
                    s += size[nxt]
                ans += s
        return ans
