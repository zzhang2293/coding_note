from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def maximumSum(nums: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/description/
        给定一个下标从1开始的数组，求一个子集，子集下标两两直接乘积是完全平方数，求子集和的最大值
        枚举所有数字， 然后这个数字为i，作为想要的一个下标除去一个完全平方数后剩下的数字，然后求和
        比如 2 * 3 * 3，2 * 4 * 4， 这两个数由于3 * 3，4 * 4 都是完全平方数，然后2 和 2 能够再组合成一个完全平方数
        :param nums: 输入数组
        :return: 子集和的最大值
        """
        ans = 0
        n = len(nums)
        for i in range(1, n + 1):
            s = 0
            for j in range(1, n + 1):
                if i * j * j > n:
                    break
                s += nums[i * j * j - 1]
            ans = max(s, ans)
        return ans

    @staticmethod
    def minLengthAfterRemovals(nums: List[int]) -> int:
        """
        https://leetcode.com/problems/minimum-array-length-after-pair-removals/
        :param nums:
        :return:
        """
        cnt = Counter(nums)
        n = len(nums)
        max_cnt = cnt.most_common(1)[0][1]
        return max(2 * max_cnt - n, n % 2)
