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

    @staticmethod
    def substringXorQueries(s: str, queries: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/substring-xor-queries/
        给一个二进制字符串s，只包含0，1，给一个queries，要求return substr，要求substr的decimal表达xor
        query[0] = query[1]，输出最短的那个substr
        思路：substr ^ x = y -> substr = y ^ x，所以只需要找到y^x.由于大小限制为10^9, 2 ^ 30 > 10 ^ 9,
        我们只需要找长度为1 - 30 的substr即可
        :param s: 二进制字符串
        :param queries: 查询
        :return: 结果
        """
        mapping = {}
        n = len(s)
        idx = s.find('0')
        if idx >= 0:
            mapping[0] = [idx, idx]
        for i in range(n):
            if s[i] == '0':
                continue
            cur = 0
            for j in range(i, min(i + 30, n)):
                cur = (cur << 1) | int(s[j])
                if cur not in mapping:
                    mapping[cur] = [i, j]
        ans = []
        for x, y in queries:
            if x ^ y in mapping:
                ans.append(mapping[x ^ y])
            else:
                ans.append([-1, -1])
        return ans

    @staticmethod
    def decode(self, encoded: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/decode-xored-permutation/
        有个未知整数数组perm，他是前n个正整数排列，n是奇数
        给一个加密后的数组encode，encode满足 encode[i] = perm[i] ^ perm[i + 1]
        输出perm
        思路：全排列，也就是perm = [a, b, c, d, e] encode = [ab, bc, cd, de]
        abcde ^ encode[2, 3] = abcde ^ bcde = a 这样第一个值就出来了 (优雅)
        :param self:
        :param encoded: 加密数组
        :return: perm
        """
        n = len(encoded) + 1
        total = 0
        for v in range(1, n + 1):
            total ^= v
        sub = 0
        for i in range(1, n - 1, 2):
            sub ^= encoded[i]
        first = total ^ sub
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans

    @staticmethod
    def minEnd(n: int, x: int) -> int:
        """
        给一个x，构建一个arr要求长度为n的递增arr，并且arr所有值and为x，请问arr[n - 1] 最小是多少
        由于我们可以选 x作为最小值，那后面不管选什么，如果后面的值在x 的bit 位上为1的位置也是1的话，结果都为x
        所以我们先把x bit位上预留出来1的位置然后按顺序把n - 1的每一个位从后往前填上去就是答案了
        :param n:
        :param x:
        :return:
        """
        n -= 1
        ans = 0
        i = 0
        while n or x:
            if x & 1:
                ans |= 1 << i
            else:
                ans |= (n & 1) << i
                n >>= 1
            i += 1
            x >>= 1
        return ans

    @staticmethod
    def subsetXORSum(nums: List[int]) -> int:
        """
        一个数组的xor总和，如果数组为空，xor总和为0. 输出所有subset的xor总和
        theorem：如果一个bit上全是0，那么这位上xor结果为0。如果至少一个1，那么0和1数量相等，都为2 ^ (n - 1)
        :param nums: arr 数组
        :return:
        """
        ans = 0
        n = len(nums)
        for num in nums:
            ans |= num
        return ans << (n - 1)

    @staticmethod
    def minOperations(n: int) -> int:
        """
        https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
        给一个正整数n，可以n 加减 2 的某个幂
        输出使 n 等于 0 所需要执行的最少操作
        连续 1 就是加上lowbit，不连续就减lowbit
        :param n:
        :return:
        """
        ans = 1
        while n & (n - 1):
            lb = n & -n
            if n & (lb << 1):
                n += lb
            else:
                n -= lb
            ans += 1
        return ans

    @staticmethod
    def minImpossibleOR(nums: List[int]) -> int:
        """
        https://leetcode.com/problems/minimum-impossible-or/
        给一个下标从0开始的整数数组，如果一个整数能由nums的某个子序列的或运算得到，那么他就是可表达的
        输出nums 不可表达的最小非0整数
        如果1在nums，2 在nums，那么3 一定能被表示出来 所以最小的数字是没有在nums 里出现的 2的幂
        :param nums:
        :return:
        """
        num = set(nums)
        i = 0
        while True:
            if 2 ** i not in num:
                return 2 ** i

    @staticmethod
    def xorGame(nums: List[int]) -> bool:
        """
        如果给定序列 xor 为 0，游戏开始，先手直接获胜
        性质1: 给定序列nums的 xor 为0，先手获胜的话，说明去掉1个数xor不为0，后手去掉一个数为0
        假设后手操作前的 xor 为 Sum 去掉一个数字xor 为0
        所以去掉一个数，等于在原来xor 的基础上 xor这个值
        具体过程：
        https://leetcode.cn/problems/chalkboard-xor-game/solutions/789745/gong-shui-san-xie-noxiang-xin-ke-xue-xi-ges7k/
        :param nums:
        :return:
        """
        total = 0
        for num in nums:
            total ^= num
        return total == 0 or len(nums) % 2 == 0

    @staticmethod
    def minimumOneBitOperations( n: int) -> int:
        """
        https://leetcode.cn/problems/minimum-one-bit-operations-to-make-integers-zero/
        格雷码：相邻两个数只有一个bit不同
        :param n:
        :return:
        """
        if n <= 1:
            return n
        pos = 0
        for i in range(n.bit_length() - 1, -1, -1):
            if (n >> i) & 1 == 1:
                pos = i
                break
        return (1 << (pos + 1)) - 1 - self.minimumOneBitOperations(n - (1 << pos))


