def BuildNextArray(s2, m):
    if m == 1:
        return [-1]
    nxt = [0] * m
    nxt[0] = -1
    for ptr in range(2, m):
        cur = nxt[ptr - 1]
        while cur != -1 and s2[cur] != s2[ptr - 1]:
            cur = nxt[cur]
        nxt[ptr] = cur + 1
    return nxt


def kmp(s1: list[str], s2: list[str]) -> int:
    n = len(s1)
    m = len(s2)
    x, y = 0, 0
    nxt = BuildNextArray(s2, m)
    while x < n and y < m:
        if s1[x] == s2[y]:
            x += 1
            y += 1
        elif y == 0:
            x += 1
        else:
            y = nxt[y]

    return x - y if y == m else -1



