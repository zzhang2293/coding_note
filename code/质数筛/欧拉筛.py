def euler(n: int) -> list:
    visit = [False for _ in range(n + 1)]
    prime = []
    cnt = 0
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


print(euler(20))


