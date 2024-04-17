from collections import defaultdict
from typing import List, Dict, Iterable
from queue import Queue


class AhoCorasick:
    """
    只允许 a-z 的范围 obj + 无优化版本
    """

    class Node:
        def __init__(self, name: str) -> None:
            """
            前缀树的节点
            :param name: 当前节点代表的字符, 通常为单个字符 a - z
            """
            self.name = name
            self.children = {}
            self.fail = None
            self.end = []

    def __init__(self, keywords: Iterable[str] = None) -> None:
        """
        AC 自动机
        :param keywords: 关键词列表
        """
        self.root = self.Node("root")
        self.finalized = False
        if keywords is not None:
            for keyword in set(keywords):
                self.add_keyword(keyword)

        self.set_fail()

    def add_keyword(self, keyword: str) -> None:
        """
        添加关键词
        :param keyword: 关键词
        """
        if self.finalized:
            raise RuntimeError("AC 自动机已经构建完成")
        current = self.root
        for char in keyword:
            if char not in current.children:
                current.children[char] = self.Node(char)
            current = current.children[char]
        current.end.append(len(keyword))

    def contains(self, keyword: str):
        """
        判断关键词是否存在
        :param keyword: 关键词
        :return: 是否存在
        """
        node = self.root
        for char in keyword:
            if char not in node.children:
                return False
            node = node.children[char]
        return bool(node.end)

    def set_fail(self) -> None:
        """
        构建 AC 自动机
        :return: None
        """
        if self.finalized:
            raise RuntimeError("AC 自动机已经构建完成")
        queue = Queue()
        queue.put(self.root)

        while not queue.empty():
            node = queue.get()
            for char in node.children:
                child = node.children[char]
                fail_node = node.fail
                # 沿着 fail pointer 向上追溯至节点
                while fail_node is not None:
                    if char in fail_node.children:
                        fail_child = fail_node.children[char]
                        child.fail = fail_child
                        if fail_child.end:
                            child.end.extend(fail_child.end)
                        break
                    fail_node = fail_node.fail
                if fail_node is None:
                    child.fail = self.root
                queue.put(child)
            self.finalized = True
        return

    def search_in(self, text: str) -> Dict[str, List[int]]:
        """
        在一段文本中查找关键字以及其开始位置
        :param text: 文本
        :return: 字典, structure: {"key": [pos1, pos2 ...]}
        """
        result = dict()
        if not self.finalized:
            self.set_fail()
        node = self.root
        for i, char in enumerate(text):
            matched = True
            # 如果当前节点的孩子找不到该字符
            while char not in node.children:
                if node.fail is None:
                    matched = False
                    break
                node = node.fail
            if matched:
                node = node.children[char]
                if node.end:
                    for len_ in node.end:
                        start = i - len_ + 1
                        word = text[start: start + len_]
                        if word not in result:
                            result[word] = []
                        result[word].append(start)
        return result


