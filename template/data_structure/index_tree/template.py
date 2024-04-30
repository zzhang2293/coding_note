from math import inf
from typing import List


class IndexTreeRangeQuerySingleUpdate:
    """
    树状数组模板 - 区间查询单点更新
    """

    def __init__(self, nums=None):
        """
        初始化树状数组
        :param nums: 原始数组
        """
        if nums is None:
            nums = []
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self.add(i + 1, nums[i])

    @staticmethod
    def lowbit(x: int) -> int:
        """
        获取 x 的最后一个 1
        :param x: 输入的 x
        :return: x 的最后一个 1
        """
        return x & -x

    def add(self, x: int, k: int):
        """
        在 x 位置加上 k
        :param x: 要加的位置
        :param k: 要加的值
        """
        while x <= self.n:
            self.tree[x] += k
            x += self.lowbit(x)

    def __sum(self, x: int) -> int:
        """
        获取前 x 项的和
        :param x: 前 x 项
        :return: 前 x 项的和
        """
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= self.lowbit(x)
        return res

    def query(self, l: int, r: int) -> int:
        """
        查询区间 [l, r] 的和
        :param l: 左端点
        :param r: 右端点
        :return: 区间 [l, r] 的和
        """
        return self.__sum(r) - self.__sum(l - 1)


class IndexTreeRangeUpdateSingleQuery:
    """
    树状数组模板 - 区间更新单点查询
    使用差分数组实现
    """

    def __init__(self, nums=None):
        """
        初始化树状数组
        :param nums: 原始数组
        """
        if nums is None:
            nums = []
        self.n = len(nums)
        self.diff = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i + 1, i + 1, nums[i])

    @staticmethod
    def lowbit(x: int) -> int:
        """
        获取 x 的最后一个 1
        :param x: 输入的 x
        :return: x 的最后一个 1
        """
        return x & -x

    def __add(self, x: int, k: int):
        """
        在 x 位置加上 k
        :param x: 要加的位置
        :param k: 要加的值
        """
        while x <= self.n:
            self.diff[x] += k
            x += self.lowbit(x)

    def query(self, x: int) -> int:
        """
        获取前 x 项的和
        :param x: 前 x 项
        :return: 前 x 项的和
        """

        res = 0
        while x > 0:
            res += self.diff[x]
            x -= self.lowbit(x)
        return res

    def update(self, l: int, r: int, k: int):
        """
        区间 [l, r) 加上 k
        :param l: 左端点
        :param r: 右端点
        :param k: 要加的值
        """
        self.__add(l, k)
        self.__add(r + 1, -k)


class IndexTreeRangeUpdateRangeQuery:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # 维护原始数组查分信息 Di
        self.diff = [0] * (self.n + 1)
        # 维护原始数组的差分加工信息
        self.diff_second = [0] * (self.n + 1)
        # [1 ~ k] 累加和公式：k * Di - (i - 1) * Di; for i in range(1, k + 1)
        for i in range(self.n):
            self.add(i + 1, i + 1, nums[i])

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def __add(self, tree: List[int], x: int, k: int) -> None:
        """
        在 x 位置加上 k
        :param tree: 是哪一棵树
        :param x: 要加的位置
        :param k: 要加的值
        :return: None
        """

        while x <= self.n:
            tree[x] += k
            x += self.lowbit(x)

    def sum(self, tree: List[int], x: int) -> int:
        """
        获取前 x 项的和
        :param tree: 是哪一棵树
        :param x: 前 x 项
        :return: 前 x 项的和
        """

        res = 0
        while x > 0:
            res += tree[x]
            x -= self.lowbit(x)
        return res

    def add(self, l: int, r: int, k: int) -> None:
        """
        区间 [l, r] 加上 k
        :param l: 左端点
        :param r: 右端点
        :param k: 要加的值
        :return: None
        """

        self.__add(self.diff, l, k)
        self.__add(self.diff, r + 1, -k)
        self.__add(self.diff_second, l, k * (l - 1))
        self.__add(self.diff_second, r + 1, -(r * k))

    def query(self, l: int, r: int) -> int:
        """
        查询区间 [l, r) 的和
        :param l: 左端点
        :param r: 右端点
        :return: 区间 [l, r] 的和
        """

        return self.sum(self.diff, r) * r - self.sum(self.diff_second, r) - \
            self.sum(self.diff, l - 1) * (l - 1) + self.sum(self.diff_second, l - 1)


class IndexTreePrefixMaximum:
    """
    树状数组模板 - 前缀最大值
    """

    def __init__(self, n: int):
        """
        初始化树状数组
        """
        self.n = n
        self.tree = [-inf] * n

    @staticmethod
    def lowbit(x: int) -> int:
        """
        获取 x 的最后一个 1
        :param x: 输入的 x
        :return: x 的最后一个 1
        """
        return x & -x

    def update(self, x: int, k: int):
        """
        在 x 位置加上 k
        :param x: 要加的位置
        :param k: 要加的值
        """
        while x <= self.n:
            self.tree[x] = max(self.tree[x], k)
            x += self.lowbit(x)

    def query(self, x: int) -> int:
        """
        获取前 x 项的最大值
        :param x: 前 x 项
        :return: 前 x 项的最大值
        """
        res = -inf
        while x > 0:
            res = max(res, self.tree[x])
            x -= self.lowbit(x)
        return res


class IndexTreeRangeUpdateSingleQueryInMatrix:
    """
    树状数组模板 - 区间更新单点查询（矩阵）
    """

    def __init__(self, matrix: List[List[int]]):
        """
        初始化树状数组
        :param matrix: 原始矩阵
        """
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.tree = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(self.n):
            for j in range(self.m):
                self.__add(i + 1, j + 1, matrix[i][j])

    @staticmethod
    def lowbit(x: int) -> int:
        """
        获取 x 的最后一个 1
        :param x: 输入的 x
        :return: x 的最后一个 1
        """
        return x & -x

    def __add(self, x: int, y: int, k: int):
        """
        在 x 行 y 列加上 k
        :param x: 要加的行
        :param y: 要加的列
        :param k: 要加的值
        """
        i = x
        while i <= self.n:
            j = y
            while j <= self.m:
                self.tree[i][j] += k
                j += self.lowbit(j)
            i += self.lowbit(i)

    def __sum(self, x: int, y: int) -> int:
        """
        获取前 x 行 y 列的和
        :param x: 前 x 行
        :param y: 前 y 列
        :return: 前 x 行 y 列的和
        """
        res = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                res += self.tree[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return res

    def update(self, x: int, y: int, k: int):
        """
        更新 x 行 y 列的值 1 indexed
        :param x: 更新的行
        :param y: 更新的列
        :param k: 更新的值
        """
        self.__add(x, y, k)

    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        查询矩阵 [x1, y1] 到 [x2, y2] 的和
        :param x1: 左上角的行
        :param y1: 左上角的列
        :param x2: 右下角的行
        :param y2: 右下角的列
        :return: 矩阵 [x1, y1] 到 [x2, y2] 的和
        """
        return self.__sum(x2, y2) - self.__sum(x1 - 1, y2) - self.__sum(x2, y1 - 1) + self.__sum(x1 - 1, y1 - 1)


class IndexTreeRangeUpdateRangeQueryInMatrix:
    """
    树状数组模板 - 区间更新区间查询（矩阵）
    """

    def __init__(self, mat: List[List[int]]):
        self.m = len(mat)
        self.n = len(mat[0])
        self.info1 = [[0] * (self.n + 1) for _ in range(self.m + 1)]  # 维护原始数组查分信息 Di
        self.info2 = [[0] * (self.n + 1) for _ in range(self.m + 1)]  # 维护d[i][j] * j
        self.info3 = [[0] * (self.n + 1) for _ in range(self.m + 1)]  # 维护d[i][j] * i
        self.info4 = [[0] * (self.n + 1) for _ in range(self.m + 1)]  # 维护d[i][j] * i * j

        for i in range(self.m):
            for j in range(self.n):
                self.update(i + 1, j + 1, i + 1, j + 1, mat[i][j])

    @staticmethod
    def lowbit(x: int) -> int:
        return x & -x

    def __add(self, x: int, y: int, k: int):
        """
        在 x 行 y 列加上 k
        :param x: x 行
        :param y: y 列
        :param k: k 值
        :return:
        """
        v1 = k
        v2 = x * k
        v3 = y * k
        v4 = x * y * k
        while x <= self.m:
            y_ = y
            while y_ <= self.n:
                self.info1[x][y_] += v1
                self.info2[x][y_] += v2
                self.info3[x][y_] += v3
                self.info4[x][y_] += v4
                y_ += self.lowbit(y_)
            x += self.lowbit(x)

    def __sum(self, x: int, y: int) -> int:
        """
        获取前 x 行 y 列的和
        :param x: x 行
        :param y: y 列
        :return: 前 x 行 y 列的和
        """
        ans = 0
        x_ = x
        while x_ > 0:
            y_ = y
            while y_ > 0:
                ans += (x + 1) * (y + 1) * self.info1[x_][y_] - (y + 1) * self.info2[x_][y_] - \
                       (x + 1) * self.info3[x_][y_] + self.info4[x_][y_]
                y_ -= self.lowbit(y_)
            x_ -= self.lowbit(x_)
        return ans

    def update(self, x1: int, y1: int, x2: int, y2: int, k: int):
        """
        更新矩阵 [x1, y1] 到 [x2, y2] 的值
        :param x1: 左上角的行
        :param y1: 左上角的列
        :param x2: 右下角的行
        :param y2: 右下角的列
        :param k: 更新的值
        """
        self.__add(x1, y1, k)
        self.__add(x2 + 1, y1, -k)
        self.__add(x1, y2 + 1, -k)
        self.__add(x2 + 1, y2 + 1, k)

    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        查询矩阵 [x1, y1] 到 [x2, y2] 的和
        :param x1: 左上角的行
        :param y1: 左上角的列
        :param x2: 右下角的行
        :param y2: 右下角的列
        :return: 矩阵 [x1, y1] 到 [x2, y2] 的和
        """
        return self.__sum(x2, y2) - self.__sum(x1 - 1, y2) - self.__sum(x2, y1 - 1) + self.__sum(x1 - 1, y1 - 1)


tree = IndexTreeRangeUpdateRangeQueryInMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(tree.query(1, 1, 2, 2))
tree.update(1, 1, 2, 2, 1)
print(tree.query(1, 1, 2, 2)) #
