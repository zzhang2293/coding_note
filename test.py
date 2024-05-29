from collections import Counter
from typing import List


class Solution:
    def compressedString(self, word: str) -> str:
        ptr = 0
        ans = []
        n = len(word)
        while ptr < n:
            start = ptr
            c = word[ptr]
            ptr += 1
            cnt = 1
            while ptr < n and word[ptr] == word[start]:
                ptr += 1
                cnt += 1
            ans.append(f"{cnt}{c}")
        return "".join(ans)


Solution().compressedString("")