from itertools import pairwise


def lz(idx, cnt):
    values[idx] = cnt - values[idx]
    lazy[idx] = True
    return


def down(idx, left, right):
    if lazy[idx]:
        lz(idx * 2, left)
        lz(idx * 2 + 1, right)
        lazy[idx] = False
    return


def up(idx):
    values[idx] = values[idx * 2] + values[idx * 2 + 1]
    return


def update(left: int, right: int, l, r, idx) -> None:
    if left <= l and r <= right:
        lz(idx, r - l + 1)
        return
    mid = (l + r) // 2
    down(idx, mid - l + 1, r - mid)
    if l <= mid:
        update(left, right, l, mid, idx * 2)
    if r > mid:
        update(left, right, mid + 1, r, idx * 2 + 1)
    up(idx)
    return


def query(left, right, l, r, idx):
    if left <= l and r <= right:
        return values[idx]
    ans = 0
    mid = (l + r) // 2
    if l <= mid:
        ans += query(left, right, l, mid, idx * 2)
    if r > mid:
        ans += query(left, right, mid + 1, right, idx * 2 + 1)
    return ans


n, m = input().split()
n = int(n)
m = int(m)
ops = []
for _ in range(m):
    c, a, b = input().split()
    c = int(c)
    a = int(a)
    b = int(b)
    ops.append([c, a, b])


values = [0] * (5 * n)
lazy = [False] * (5 * n)
res = []
for c, a, b in ops:
    if c == 0:
        update(a, b, 0, n - 1, 1)
    if c == 1:
        res.append(query(a, b, 0, n - 1, 1))
for val in res:
    print(val)
