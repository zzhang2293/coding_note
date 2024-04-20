from typing import List


class PreFixSumMatrix:
    def __init__(self, mat: List[List[int]]):

        """
        二维前缀和矩阵 对于 (i, j) 来说，前缀和为 (i, j) + (i-1, j) + (i, j-1) - (i-1, j-1)
        :param mat: 二维矩阵
        """

        self.mat = mat  # 二维前缀和矩阵
        self.m, self.n = len(mat), len(mat[0])
        self.prefix = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.prefix[i + 1][j + 1] = self.prefix[i][j + 1] + \
                                            self.prefix[i + 1][j] - self.prefix[i][j] + mat[i][j]
        return

    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:

        """
        查询矩阵 (x1, y1) 到 (x2, y2) 的和
        :param x1: 左上角 x 坐标
        :param y1: 左上角 y 坐标
        :param x2: 右下角 x 坐标
        :param y2: 右下角 y 坐标
        :return: 矩阵 (x1, y1) 到 (x2, y2) 的和
        """
        assert 0 <= x1 <= x2 <= self.m - 1
        assert 0 <= y1 <= y2 <= self.n - 1
        return self.prefix[x2 + 1][y2 + 1] - self.prefix[x1][y2 + 1] - self.prefix[x2 + 1][y1] + self.prefix[x1][y1]

    @staticmethod
    def get_product_matrix_except_current(grid: List[List[int]], mod = 1) -> List[List[int]]:
        """
        生成一个矩阵，每个位置的值为除了自己以外的所有元素的乘积
        :param grid: 原始矩阵
        :param mod: 取模，默认不取模
        :return: 生成的矩阵 
        """
        m, n = len(grid), len(grid[0])
        suf = 1
        mat = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mat[i][j] = suf
                suf = (suf * grid[i][j]) % mod
        pre = 1
        for i in range(m):
            for j in range(n):
                mat[i][j] = (mat[i][j] * pre) % mod
                pre = (pre * grid[i][j]) % mod
        return mat


class DifferenceArray:
    def __init__(self):
        return

    @staticmethod
    def get_diff_array(n: int, shifts: List[int]) -> List[int]:
        """
        根据 shifts 生成差分数组
        :param n: 数组长度
        :param shifts: 差分数组 structure: [from, to, value] ...
        """
        diff = [0] * n
        for i, j, val in shifts:
            if j + 1 < n:
                diff[j + 1] -= val
            diff[i] += val
        for i in range(1, n):
            diff[i] += diff[i - 1]
        return diff

    @staticmethod
    def get_array_prefix_sum(n: int, lst: List[int]) -> List[int]:
        """ 生成前缀和数组 """
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + lst[i]
        return prefix

    @staticmethod
    def get_array_range_sum(prefix: List[int], left: int, right: int) -> int:
        """
        查询前缀和数组的区间和
        :param prefix: 前缀和数组
        :param left: 左边界 (包含)
        :param right: 右边界 (不包含)
        """
        return prefix[right] - prefix[left]


class DiffMatrix:
    def __init__(self):
        return

    @staticmethod
    def get_diff_matrix(m: int, n: int, shifts: List[List[int]]) -> List[List[int]]:
        """
        根据 shifts 生成差分矩阵
        :param m: row 的长度
        :param n: col 的长度
        :param shifts: 差分数组, structure: [x1, y1, x2, y2, val] ...
        :return: 差分矩阵
        """

        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for x1, y1, x2, y2, val in shifts:
            assert 1 <= x1 <= x2 <= m
            assert 1 <= y1 <= y2 <= n
            diff[x1][y1] += val
            diff[x1][y2 + 1] -= val
            diff[x2 + 1][y1] -= val
            diff[x2 + 1][y2 + 1] += val
        for i in range(1, m + 2):
            for j in range(1, n + 2):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        for i in range(1, m + 1):
            diff[i] = diff[i][1: n + 1]
        return diff



