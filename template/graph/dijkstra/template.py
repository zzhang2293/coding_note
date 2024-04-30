from collections import defaultdict, deque
from heapq import heappush, heappop

from math import inf
from sortedcontainers import SortedList


class Dijkstra:
    def __init__(self):
        return

    @staticmethod
    def get_shortest_path(graph, src: int, initial=0) -> list:
        """
        dijkstra 找到从src到其他点最短路径
        :param graph: a graph
        :param src: start node
        :param initial: 起初的距离
        :return: src到每一个点的距离， 如果到不了就是inf
        """
        n = len(graph)
        dis = [inf] * n
        heap = [(initial, src)]
        while heap:
            d, i = heappop(heap)
            if dis[i] < d:
                continue
            for nxt, w in graph[i]:
                new_dis = d + w
                if new_dis < dis[nxt]:
                    dis[nxt] = new_dis
                    heappush(heap, (new_dis, nxt))
        return dis

    @staticmethod
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
            for nxt, d in graph[node]:
                if dist[nxt] == d + dis:
                    cnt[nxt] += cnt[node]
                elif dist[nxt] > d + dis:
                    dist[nxt] = d + dis
                    cnt[nxt] = cnt[node]
                    heappush(heap, (dis + d, nxt))
        return cnt[dst]

    @staticmethod
    def get_dijkstra_result_limit(graph, src: int, limit: list, target) -> list:
        """
        最短路径，但是有一个limit限制不能走
        :param graph: 图
        :param src: 起点
        :param limit: 限制
        :param target:
        :return: 到每一个点的距离
        """
        n = len(graph)
        dis = [inf] * n

        dis[src] = 0 if src not in limit else inf
        heap = [(dis[src], src)]
        while heap and target:
            d, i = heappop(heap)
            if i in target:
                target.discard(i)
            if dis[i] < d:
                continue
            for j, w in graph[i]:
                if j not in limit:
                    dj = w + d
                    if dj < dis[j]:
                        dis[j] = dj
                        heappush(heap, (dj, j))
        return dis

    @staticmethod
    def get_shortest_path_from_src_to_dst(dct, src: int, dst: int):
        """
        最短路径 & 具体的路径情况
        :param dct: 图
        :param src: 起点
        :param dst: 终点
        :return: 路线图以及最短距离
        """
        n = len(dct)
        dis = [inf] * n
        heap = [(0, src)]
        dis[src] = 0
        father = [-1] * n
        while heap:
            d, i = heappop(heap)
            if dis[i] < d:
                continue
            if i == dst:
                break
            for j, w in dct[i]:
                dj = w + d
                if dj < dis[j]:
                    dis[j] = dj
                    father[j] = i
                    heappush(heap, (dj, j))
        if dis[dst] == inf:
            return [], inf
        # backtrack for the path
        path = []
        i = dst
        while i != -1:
            path.append(i)
            i = father[i]
        return path, dis[dst]

    @staticmethod
    def gen_maximum_product_path(graph, src, dsc):
        """
        得到最大距离乘积
        :param graph: 图
        :param src: 起点
        :param dsc: 终点
        :return: 距离
        """
        dis = defaultdict(lambda: inf)
        heap = [(-1, src)]
        dis[src] = 1
        while heap:
            d, i = heappop(heap)
            d = -d
            if dis[i] > d:
                continue
            for j in graph[i]:
                dj = graph[i][j] * d
                if dj > dis[j]:
                    dis[j] = dj
                    heappush(heap, (-dj, j))
        return dis[dsc]

    @staticmethod
    def get_second_shortest_path(graph, src: int) -> list:
        """
        得到第二短的路径
        :param graph: 图
        :param src: 起点
        :return: 距离
        """
        n = len(graph)
        dist = [[inf] * 2 for _ in range(n)]  # 0: shortest, 1: second shortest
        dist[src][0] = 0
        heap = [(0, src)]
        while heap:
            d, node = heappop(heap)
            if dist[node][1] < d:
                continue
            for nxt, w in graph[node]:
                if dist[nxt][0] > d + w:
                    dist[nxt][0], dist[nxt][1] = d + w, dist[nxt][0]
                    heappush(heap, (dist[nxt][0], nxt))
                elif dist[nxt][1] > d + w > dist[nxt][0]:  # second shortest
                    dist[nxt][1] = d + w
                    heappush(heap, (dist[nxt][1], nxt))
        return dist

    @staticmethod
    def get_cnt_of_second_shortest_path(graph, src, mod=-1):
        """
        得到第二短的路径的数量
        :param graph: 图
        :param src: 起点
        :param mod: 取模， 默认不取模
        :return: 到每一个node 的 最短距离 以及 数量
        """
        n = len(graph)
        dist = [[inf] * 2 for _ in range(n)]
        heap = [(0, src, 0)]
        cnt = [[0] * 2 for _ in range(n)]
        cnt[src][0] = 1
        while heap:
            d, i, state = heappop(heap)
            if dist[i][state] < d:  # state: 0: shortest, 1: second shortest
                continue
            pre = cnt[i][state]
            for nxt, w in graph[i]:
                dd = d + w
                if dist[nxt][0] > dd:
                    dist[nxt][0], dist[nxt][1] = dd, dist[nxt][0]
                    cnt[nxt][0], cnt[nxt][1] = pre, cnt[nxt][0]
                    heappush(heap, (dd, nxt, 0))
                elif dist[nxt][0] == dd:
                    cnt[nxt][0] += pre
                    if mod != -1:
                        cnt[nxt][0] %= mod
                elif dist[nxt][1] > dd > dist[nxt][0]:
                    dist[nxt][1] = dd
                    cnt[nxt][1] = pre
                    heappush(heap, (dd, nxt, 1))
                elif dist[nxt][1] == dd:
                    cnt[nxt][1] += pre
                    if mod != -1:
                        cnt[nxt][1] %= mod
        return dist, cnt


class UnDirectedShortestCycle:
    def __init__(self):
        return

    @staticmethod
    def find_shortest_cycle_with_node(n: int, graph) -> int:
        """
        找到最短的环，暴力枚举每一个点
        :param n: 点的数量
        :param graph: 图 邻接矩阵
        :return: 最短环的长度
        """
        ans = inf
        for i in range(n):
            dist = [inf] * n
            par = [-1] * n
            dist[i] = 0
            heap = [(0, i)]
            while heap:
                dis, node = heappop(heap)
                for nxt, d in graph[node]:
                    if dist[nxt] > ans:
                        continue
                    if dist[nxt] > d + dist[node]:
                        dist[nxt] = d + dist[node]
                        par[nxt] = node
                        heappush(heap, (dist[nxt], nxt))
                    elif par[node] != nxt and par[nxt] != node:
                        cur = dist[nxt] + d + dist[node]
                        ans = min(ans, cur)

        return ans if ans != inf else -1


print(UnDirectedShortestCycle.find_shortest_cycle_with_node(3, {0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1)], 2: [(0, 1), (1, 1)]}))
