
class KMP:
    def __init__(self):
        return

    @classmethod
    def prefix_function(cls, s: str) -> list[int]:
        """
        KMP 算法的前缀函数
        :param s: 字符串
        :return: 前缀函数
        """
        n = len(s)
        nxt = [0] * n
        for i in range(1, n):
            j = nxt[i - 1]
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt

    @staticmethod
    def z_function(s: str) -> list[int]:
        """
        Z 函数: 对于字符串 s 的每个位置 i，Z[i] 表示 s 和 s[i:] 的最长公共前缀
        :param s: 字符串
        :return: Z 函数
        """
        n = len(s)
        z_array = [-1] * n
        z_array[0] = n
        central = right = 1
        for i in range(1, n):
            len_ = min(z_array[i - central], right - i) if right > i else 0
            # at least this long
            while i + len_ < n and s[i + len_] == s[len_]:
                len_ += 1
            if i + len_ > right:
                right = i + len_
                central = i
            z_array[i] = len_
        return z_array

    @staticmethod
    def e_function(s: str, t: str) -> list[int]:
        """
        E 函数: 对于字符串 s 和 t，E[i] 表示 s[i:] 和 t 的最长公共前缀
        :param s: 字符串 s
        :param t: 字符串 t
        :return: E 函数
        """
        m, n = len(s), len(t)
        t_z_array = KMP.z_function(t)
        central, right = 0, 0
        e_array = [0] * n

        for i in range(m):
            len_ = min(right - i, t_z_array[i - central]) if right > i else 0
            while i + len_ < m and len_ < n and s[i + len_] == t[len_]:
                len_ += 1
            if i + len_ > right:
                right = i + len_
                central = i
            e_array[i] = len_

        return e_array

    def find(self, s1: str, s2: str) -> list[int]:
        """
        找到 s1 中 s2 的位置 s2 in s1
        :param s1: 字符串1 长
        :param s2: 字符串2 短
        :return: s2 在 s1 中的位置
        """
        n, m = len(s1), len(s2)
        nxt = self.prefix_function(s2 + '#' + s1)
        ans = []
        for i in range(m + 1, m + n + 1):
            if nxt[i] == m:
                ans.append(i - m - m)
                # a b c d e # a b c x
        return ans


# TODO something have not finished

# print(KMP().find("aaaaa", "aaa"))


a = "abc" * (10 ** 9)

if "a" in a:
    print("hello")

