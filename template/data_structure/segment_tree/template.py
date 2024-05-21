class SegmentTree:
    def __init__(self, lst: list):
        n = len(lst)
        self.arr = [0] * ((n << 2) + 1)
        self.add = [0] * ((n << 2) + 1)
        self.lst = lst
        self.build(1, n, 1)

    def build(self, left: int, right: int, idx: int) -> None:
        """
        范围 l 到 r 填到 i位置上
        :param left: left range
        :param right: right range
        :param idx: position
        """
        if left == right:
            self.arr[idx] = self.lst[left - 1]
        else:
            mid = (left + right) >> 1
            self.build(left, mid, idx << 1)
            self.build(mid + 1, right, idx << 1 | 1)
            self.__up(idx)
        self.add[idx] = 0
        return

    def __up(self, idx):
        """
        更新节点
        :param idx:
        :return:
        """
        self.arr[idx] = self.arr[idx << 1] + self.arr[idx << 1 | 1]

    def __lazy(self, idx: int, value: int, num: int) -> None:
        """
        懒惰标记
        :param idx:
        :param value:
        :param num:
        :return:
        """
        self.arr[idx] += value * num
        self.add[idx] += value

    def __down(self, idx: int, left_num: int, right_num: int) -> None:
        """
        下传懒惰标记
        :param idx: index
        :param left_num: 左边的数有几个
        :param right_num: 右边的数有几个
        :return: None
        """
        if self.add[idx]:
            self.__lazy(idx << 1, self.add[idx], left_num)
            self.__lazy(idx << 1 | 1, self.add[idx], right_num)
            self.add[idx] = 0

    def update(self, job_left, job_right, job_value) -> None:
        """
        在job_left到job_right区间加上job_value
        :param job_left: 左边界
        :param job_right: 右边界
        :param job_value: 加上的值
        :return: None
        """

        def dfs(l, r, idx):
            if job_left <= l and r <= job_right:
                self.__lazy(idx, job_value, r - l + 1)
            else:
                mid = (l + r) >> 1
                self.__down(idx, mid - l + 1, r - mid)
                if job_left <= mid:
                    dfs(l, mid, idx << 1)
                if job_right > mid:
                    dfs(mid + 1, r, idx << 1 | 1)
                self.__up(idx)
        dfs(1, len(self.lst), 1)

    def query(self, left: int, right: int):
        """
        区间查询
        :param left: left bound
        :param right: right bound
        :return: sum
        """

        def dfs(l, r, idx):
            if left <= l and r <= right:
                return self.arr[idx]
            mid = (l + r) >> 1
            self.__down(idx, mid - l + 1, r - mid)
            ans = 0
            if left <= mid:
                ans += dfs(l, mid, idx << 1)
            if right > mid:
                ans += dfs(mid + 1, r, idx << 1 | 1)
            return ans

        return dfs(1, len(self.lst), 1)


tree = SegmentTree([1, 2, 3, 4, 5])
print(tree.query(1, 3))
tree.update(1, 3, 2)
print(tree.query(1, 3))

