from typing import List


class Bipartite:

    def __init__(self):
        pass

    @staticmethod
    def isBipartite(graph: List[List[int]]) -> bool:
        """
        判断二分图，用染色法将邻居染成不同颜色，如果没有冲突说明是二分图
        :param graph:
        :return:
        """
        n = len(graph)
        color = [-1] * n

        def dfs(node, pre):
            for nxt in graph[node]:
                if nxt != pre:
                    if color[nxt] == -1:
                        color[nxt] = color[node] ^ 1
                        dfs(nxt, node)
                    else:
                        if color[nxt] == color[node]:
                            return False
            return True

        for root, arr in enumerate(graph):
            if color[root] == -1:
                color[root] = 0
                for nt in arr:
                    if not dfs(root, -1):
                        return False
        return True


print(Bipartite.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
