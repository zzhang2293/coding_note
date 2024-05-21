def Hungarian(n: int, edges: list[list[int]]):
    def match(from_: int):
        for j in range(n):
            if graph[from_][j] == 1 and j not in vis:
                vis.add(j)
                if pair[j] == 0 or match(pair[j]):
                    pair[j] = from_
                    return True
        return False

    graph = [[-1] * n for _ in range(n)]  # adj matrix

    for a, b in edges:
        graph[a][b] = 1
        graph[b][a] = 1
    vis = set()
    pair = [-1] * n
    ans = 0
    for i in range(n):
        vis.clear()
        if match(i):
            ans += 1
    return ans



