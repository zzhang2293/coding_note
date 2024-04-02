class TrieNode:
    def __init__(self):
        self.nxt = [None] * 26
        self.pass_ = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def build(self, string: str):
        n = len(string)
        cur: TrieNode = self.root
        for i in range(n):
            ind = 0    # TODO depends on different question
            if not cur.nxt[ind]:
                cur.nxt[ind] = TrieNode()
            cur = cur.nxt[ind]

    def find(self, string):
        n = len(string)
        ans = 0
        cur = self.root
        for i in range(n):
            c = int(string[i])
            if cur.nxt[c]:
                cur = cur.nxt[c]
                ans += 1
            else:
                break
        return ans
