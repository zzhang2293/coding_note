from typing import List, Iterable


class KruskalBase:
    def __init__(self):
        pass

    @staticmethod
    def find_shortest_path(n: int, edge: List[List[int]]) -> Iterable:
        """
        Kruskal implementation
        :param n: number of node
        :param edge: edges
        :return: minimum spanning tree
        """
        father = [i for i in range(n)]

        def find(x):
            if x != father[x]:
                father[x] = find(father[x])
            return father[x]

        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx != fy:
                father[fy] = fx
                return True
            return False

        edge.sort(key=lambda x: x[2])
        total = 0
        edge_res = []
        for a, b, v in edge:
            if union(a, b):
                total += v
                edge_res.append((a, b))

        return total, edge_res
