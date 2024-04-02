def matrixMultiply(mat1: list[list], mat2: list[list]) -> list[list]:
    n = len(mat1)
    m = len(mat2[0])
    k = len(mat1[0])
    ans = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for c in range(k):
                ans[i][j] += mat1[i][c] * mat2[c][j]
    return ans


def power(mat: list[list[int]], p: int) -> list[list[int]]:
    n = len(mat)
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1

    while p != 0:
        if p & 1 != 0:
            ans = matrixMultiply(ans, mat)
        mat = matrixMultiply(mat, mat)
        p >>= 1
    return ans


print(power([[1, 2], [3, 4]], 5))
