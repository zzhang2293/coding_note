from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def subsequenceSumOr(nums: List[int]) -> int:
        """
        给一个数组，输出 按位OR的 所有子序列的sum值
        例如：1，2，3 子序列 [1, 2]的sum值就是3
        这题从小bit到大bit枚举，看是不是每一位上都能够得到 1如果能得到1说明有某个子序列那一位上能提供1个1
        :param nums: 数组
        :return:
        """
        ans = 0
        for bit in range(60):
            s, tail = 0, (1 << (bit + 1)) - 1
            for num in nums:
                s += num & tail
            if s >= 1 << bit:
                ans |= 1 << bit
        return ans

    @staticmethod
    def wonderfulSubstrings(word: str) -> int:
        """
        给一个str，要求返回有多少substr，其中至多包含奇数个数单词1个
        解法：可以把这题单词转换成0，1，分别代表奇偶行，用bit做状态压缩，如果之前有一个前缀的状态
        等于当前状态，那么说明这两个中间的substr一定是全偶数个
        第二种情况一个奇数，对于每一位上反转，做同样操作。反转后如果前面有个前缀的状态等于这个状态，
        那么这两个状态之间的substr一定是差了一个1，也就是有一个字母为奇数
        :param word:
        :return:
        """
        cnt = Counter()
        cnt[0] = 1
        base = ord('a')
        prefix = 0
        ans = 0
        for i, v in enumerate(word):
            idx = ord(v) - base
            prefix ^= 1 << idx
            ans += cnt[prefix]
            for j in range(11):
                tmp = prefix ^ (1 << j)
                ans += cnt[tmp]
            cnt[prefix] += 1
        return ans
