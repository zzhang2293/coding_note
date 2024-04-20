
class UnionFind:
    def __init__(self, n: int) -> None:
        self.father = [i for i in range(n)]

    def find(self, x: int) -> int:
        """
        find father of x
        :param x: x
        :return: father of x
        """
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int) -> int:
        """
        union a and b
        :param a: num1
        :param b: num2
        :return:
        """
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fb] = fa
            return True

        return False


