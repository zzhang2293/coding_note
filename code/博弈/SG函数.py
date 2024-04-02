def bash(n, m):
    sg = [0] * n
    for i in range(n + 1):
        appear = [False for _ in range(m + 1)]
        j = 1
        while i - j >= 0 and j <= m:
            appear[sg[i - j]] = True
            j += 1
        for s in range(m + 1):
            if not appear[s]:
                sg[i] = s
                break


def nim(arr: list):
    mx = 0
    for num in arr:
        mx = max(mx, num)
    sg = [0 for _ in range(mx + 1)]
    for i in range(mx + 1):
        appear = [False for _ in range(mx + 1)]
        for j in range(i):
            appear[j] = True
        for x in range(mx + 1):
            if not appear[x]:
                sg[i] = x
                break
    ans = 0
    for num in arr:
        ans ^= sg[num]
    print(ans)

# nim([2, 1])
