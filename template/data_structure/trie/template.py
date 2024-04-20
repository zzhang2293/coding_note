import typing
from typing import List, Any


class BasicTrieTemplate:

    class TrieNode:
        def __init__(self):
            self.child: Any = [None] * 26
            self.end = 0
            self.pass_ = 0  # abc   ab

    def __init__(self):
        self.root = self.TrieNode()

    def add_word(self, word: str) -> None:
        """
        往 trie 里添加一个单词
        :param word: 单词
        :return: None
        """
        base = ord('a')
        cur = self.root
        cur.pass_ += 1
        for c in word:
            idx = ord(c) - base
            if cur.child[idx] is None:
                cur.child[idx] = self.TrieNode()
            cur = cur.child[idx]
            cur.pass_ += 1
        cur.end += 1
        return

    def add_words(self, words: List[str]) -> None:
        """
        往 trie 里添加一组单词
        :param words: 一组单词
        :return: None
        """

        for word in words:
            self.add_word(word)
        return

    def check_cnt(self, target: str) -> int:
        """
        check trie 里面有几个 target
        :param target:
        :return:
        """
        base = ord('a')
        cur = self.root
        for c in target:
            idx = ord(c) - base
            if cur.child[idx] is None:
                return 0
            cur = cur.child[idx]
        return cur.end

    def check_array_cnt(self, targets: List[str]) -> List[int]:
        """
        check trie 里面有几个target
        :param targets: target 数组
        :return: targets 每一个元素出现几次
        """
        n = len(targets)
        ans = [0] * n
        for i, target in enumerate(targets):
            ans[i] = self.check_cnt(target)
        return ans

    def check_target_prefix(self, target: str) -> int:
        """
        以 target 作为 prefix 的有几个
        :param target: input
        :return: 几个
        """
        base = ord('a')
        cur = self.root
        for c in target:
            idx = ord(c) - base
            if cur.child[idx] is None:
                return 0
            cur = cur.child[idx]
        return cur.pass_

    def check_target_common_prefix(self, target: str) -> int:
        """
        判断 target 和 字典里值的 最长公共前缀有多长
        :param target: input
        :return: 几个
        """
        base = ord('a')
        cur = self.root
        for i, c in enumerate(target):
            idx = ord(c) - base
            if cur.child[idx] is None:
                return i + 1
            cur = cur.child[idx]
        return len(target)

    def check_element_exist(self, target: str) -> bool:
        """
        判断 target 是否在 trie 里
        :param target: input
        :return: True if exist otherwise False
        """
        cur = self.root
        base = ord("a")
        for c in target:
            idx = ord(c) - base
            if cur.child[idx] is None:
                return False
            cur = cur.child[idx]
        return True if cur.end > 0 else False

    def delete_element_from_trie(self, target) -> None:
        """
        如果target 在trie 里面，删除一条
        :param target:
        :return: None
        """
        if not self.check_element_exist(target):
            return
        cur = self.root
        cur.pass_ -= 1
        base = ord("a")
        for c in target:
            idx = ord(c) - base
            cur.child[idx].pass_ -= 1
            if cur.child[idx].pass_ == 0:
                cur.child[idx] = None
            cur = cur.child[idx]
        cur.end -= 1
        return




