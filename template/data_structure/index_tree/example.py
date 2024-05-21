
from typing import List


class Solution:

    @staticmethod
    def reverse_pair(arr: List[int]):
        """
        给一个数组，求逆序对的数量
        :param arr: 输入数组
        :return: 逆序对的数量
        """

        class IndexTree:
            def __init__(self, n: int):
                self.arr = [0] * (n + 1)

            def update(self, value: int):
                n = len(self.arr)
                while value < n:
                    self.arr[value] += 1
                    value += value & -value
                return

            def check(self, value: int):

                ans = 0
                while value > 0:
                    ans += self.arr[value]
                    value -= value & -value
                return ans

        n = len(arr)
        rank = sorted(set(arr))
        ans = 0

        rank_dict = {value: i + 1 for i, value in enumerate(rank)}
        tree = IndexTree(len(rank) + 1)
        for i in range(n - 1, -1, -1):
            val = rank_dict[arr[i]]
            ans += tree.check(val - 1)
            tree.update(val)
        return ans

    @staticmethod
    def count_number_of_increasing_triple_pair(nums: List[int]):
        """
        给一个数组，求递增三元组的数量
        如果 i < j < k 并且 arr[i] < arr[j] < arr[k]，那么 (i, j, k) 是一个递增三元组
        :param nums: 输入数组
        :return: 递增三元组的数量
        """

        class IndexTree:
            def __init__(self, n):
                self.tree1 = [0] * n
                self.tree2 = [0] * n

            def check2(self, value):
                ans = 0
                while value > 0:
                    ans += self.tree2[value]
                    value -= value & -value
                return ans

            def check1(self, value):
                ans = 0
                while value > 0:
                    ans += self.tree1[value]
                    value -= value & -value
                return ans

            def add1(self, value):
                while value < len(self.tree1):
                    self.tree1[value] += 1
                    value += value & -value

            def add2(self, value):
                c = self.check1(value - 1)
                while value < len(self.tree2):
                    self.tree2[value] += c
                    value += value & -value

        rank = sorted(set(nums))
        rank_dict = {value: i + 1 for i, value in enumerate(rank)}

        tree = IndexTree(len(rank) + 1)
        res = 0
        for num in nums:
            rk = rank_dict[num]
            res += tree.check2(rk - 1)
            tree.add1(rk)
            tree.add2(rk)
        return res

    @staticmethod
    def findNumberOfLIS(nums: List[int]) -> int:
        """
        给一个数组，求最长递增子序列的数量
        用树状数组 维护 max_len: 以 i...j 结尾的最长递增子序列的长度最大值，注意i, j 是树状数组j下标管着的值
        :param nums: 输入数组
        :return: 最长递增子序列的数量
        """
        class IndexTree:
            def __init__(self, n):
                self.max_len = [0] * n
                self.cnt = [0] * n

            def check(self, value):
                lens = 0
                i = value
                c = 0
                while i > 0:
                    if self.max_len[i] > lens:
                        lens = self.max_len[i]
                        c = self.cnt[i]
                    elif self.max_len[i] == lens:
                        c += self.cnt[i]
                    i -= i & -i
                return lens, c

            def update(self, value, lens, ct):
                while value < len(self.max_len):
                    if self.max_len[value] == lens:
                        self.cnt[value] += ct
                    elif self.max_len[value] < lens:
                        self.cnt[value] = ct
                        self.max_len[value] = lens
                    value += value & -value

        lst = sorted(set(nums))
        rank = {num: idx + 1 for idx, num in enumerate(lst)}
        tree = IndexTree(len(lst) + 1)
        for num in nums:
            val = rank[num]
            l, c = tree.check(val - 1)
            tree.update(val, l + 1, max(c, 1))
        _, res = tree.check(len(lst))
        return res





