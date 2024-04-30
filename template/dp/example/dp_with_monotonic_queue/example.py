from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    @staticmethod
    def findMaximumLength(nums: List[int]) -> int:
        """
        给一个数组，可以执行任意操作，每次操作选择一个子数组，将子数组用他所包含的元素和替换，
        可以操作任意次，求可以得到的最长非递减数组长度
        :param nums: 输入数组
        :return: 最长非递减数组长度
        """
        n = len(nums)
        dp = [0] * (n + 1)
        last = [0] * (n + 1)
        prefix = list(accumulate(nums, initial=0))
        queue = deque([0])
        for i in range(1, n + 1):
            while len(queue) > 1 and prefix[queue[1]] + last[queue[1]] <= prefix[i]:
                queue.popleft()

            idx = queue[0]
            dp[i] = dp[idx] + 1
            last[i] = prefix[i] - prefix[idx]
            while queue and last[queue[-1]] + prefix[queue[-1]] >= last[i] + prefix[i]:
                queue.pop()
            queue.append(i)
        return dp[-1]

