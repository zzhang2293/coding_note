def up(idx: int):
    value[idx] = value[idx * 2] + value[idx * 2 + 1]
    return


def lazy(idx: int, cnt: int, val: int):
    value[idx] += cnt * val
    lz[idx] += val
    return


def down(idx: int, l_cnt: int, r_cnt: int):
    if lz[idx]:
        lazy(idx * 2, l_cnt, lz[idx])
        lazy(idx * 2 + 1, r_cnt, lz[idx])
        lz[idx] = 0
    return


def update(left, right, l, r, idx, val):
    if left <= l and r <= right:
        lazy(idx, r - l + 1, val)
        return
    mid = (l + r) // 2
    down(idx, mid - l + 1, r - mid)
    if left <= mid:
        update(left, right, l, mid, idx * 2, val)
    if right > mid:
        update(left, right, mid + 1, r, idx * 2 + 1, val)
    up(idx)
    return


def total(left, right, l, r, idx):
    if left <= l and r <= right:
        return value[idx]
    mid = (l + r) // 2
    down(idx, mid - l + 1, r - mid)
    ans = 0
    if left <= mid:
        ans += total(left, right, l, mid, idx * 2)
    if right > mid:
        ans += total(left, right, mid + 1, r, idx * 2 + 1)
    return ans


f = open("test.txt", "r")
n, m = [int(x) for x in f.readline().split()]
ini = [int(x) for x in f.readline().split()]
query = []
for _ in range(m):
    query.append([int(x) for x in f.readline().split()])
f.close()
diff = [0] * (len(ini))
diff[0] = ini[0]
value = [0] * (4 * len(diff))
n = len(ini)
lz = [0] * (4 * len(diff))
for i in range(1, len(ini)):
    diff[i] = ini[i] - diff[i - 1]
res = []
for i, val in enumerate(ini):
    update(i, i, 0, n - 1, 1, val)
for q in query:
    if q[0] == 1:
        l, r, start, dif = q[1:]
        update(l, l, 0, n - 1, 1, start)
        update(l + 1, r, 0, n - 1, 1, dif)
        if r + 1 < n:
            update(r + 1, r + 1, 0, n - 1, 1, start + (r - l) * dif)
    else:
        i = q[1:][0]
        res.append(total(i, i, 0, n - 1, 1))
for v in res:
    print(v)
