from typing import List


class BitOperation:
    @staticmethod
    def totalHammingDistance(nums: List[int]) -> int:
        """
        汉明距离：拆位法典题
        :param nums: 
        :return:
        """
        ans = 0
        for i in range(32):
            zero = 0
            one = 0
            for num in nums:
                if (num >> i) & 1 == 0:
                    zero += 1
                else:
                    one += 1
            ans += zero * one
        return ans