from typing import List


class Implementation:
    def __init__(self):
        pass

    @staticmethod
    def matrix_rotate(matrix: List[List[int]]):

        """ 90度顺时针旋转矩阵 """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                a, b, c, d = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = a, b, c, d

        """ 90 度逆时针旋转矩阵 """
        n - len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                a, b, c, d = matrix[j][n - i - 1], matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1]
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = a, b, c, d
        return matrix


class SpiralMatrix:
    def __init__(self):
        return

    @staticmethod
    def joseph_circle(n, m) -> int:
        """
        约瑟夫环问题
        每次移除m-th，输出最后剩下的结果
        TODO
        :param n: 起初一共有多少人
        :param m: 每次移除的人的位置
        :return: 最后剩下的人
        """
        f = 0
        for x in range(2, n + 1):
            f = (m + f) % x
        return f

    @staticmethod
    def num_to_loc(m, n, num) -> int:
        """
        把一个数字转换成在矩阵中的位置
        :param m: row len
        :param n: col len
        :param num: 数字
        :return: 具体矩阵中的位置
        """
        m += 1
        return [num // m, num % n]

    @staticmethod
    def loc_to_num(row, col, m, n) -> int:
        """
        把一个位置转换成具体一个数字
        :param row: row
        :param col: col
        :param m: row len
        :param n: col len
        :return: 具体数字 unique
        """

        return row * m + col

    @staticmethod
    def get_spiral_matrix_num(m, n, r, c) -> int:
        """
        clockwise spiral num at pos [r, c] start from 1
        :param m: row len
        :param n: col len
        :param r: start row pos
        :param c: start col pos
        :return:
        """
        assert 1 <= r <= m and 1 <= c <= n
        num = 1
        while r not in [1, m] and c not in [1, n]:
            num += 2 * m + 2 * n - 4
            r -= 1
            c -= 1
            n -= 2
            m -= 2
        x = y = 1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        while [x, y] != [r, c]:
            a, b = directions[d]
            if not (1 <= x + a <= m and 1 <= y + b <= n):
                d += 1
                a, b = directions[d]
                x += a
                y += b
                num += 1
        return num

