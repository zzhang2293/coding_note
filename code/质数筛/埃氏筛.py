def ehrlich(n: int) -> int:
    # 埃氏筛
    visit = [False for _ in range(n)]
    cur = 2
    while cur * cur <= n:
        if not visit[cur]:
            j = cur ** 2
            while j <= n:
                visit[j] = True
                j += cur
        cnt = 0
        for i in range(2, n + 1):
            if not visit[i]:
                cnt += 1
        return cnt



