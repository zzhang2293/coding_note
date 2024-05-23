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


class SegmentTreeSumQueryUpdate:
    def __init__(self, arr: list):
        """
        区间查询 sum，支持重制或者加法
        :param arr: 原始数组
        """
        n = len(arr)
        self.arr = arr
        self.sum_ = [0] * (n << 2)
        self.add_ = [0] * (n << 2)
        self.change = [0] * (n << 2)
        self.update = [False] * (n << 2)
        self.build(1, n, 1)

    def __up(self, idx: int) -> None:
        """
        更新父节点，左右子节点的和
        :param idx: 父节点
        :return: None
        """
        self.sum_[idx] = self.sum_[idx << 1] + self.sum_[idx << 1 | 1]

    def __update_lazy(self, idx: int, value: int, num: int) -> None:
        """
        更新懒惰标记, 如果有重制任务，那么加法任务就不会执行
        :param idx: 需要更新的位置
        :param value: 更新的值
        :param num: 更新的数量
        :return:
        """
        self.sum_[idx] = value * num
        self.add_[idx] = 0
        self.change[idx] = value
        self.update[idx] = True

    def __add_lazy(self, idx: int, value: int, num: int) -> None:
        """
        加法任务懒惰标记
        :param idx: 需要更新的位置
        :param value: 更新的值
        :param num: 更新的数量
        :return:
        """
        self.sum_[idx] += value * num
        self.add_[idx] += value

    def __down(self, idx: int, left_num: int, right_num: int) -> None:
        """
        下传懒惰标记
        :param idx: index
        :param left_num: 左边的数有几个
        :param right_num: 右边的数有几个
        :return: None
        """
        if self.update[idx]:
            self.__update_lazy(idx << 1, self.change[idx], left_num)
            self.__update_lazy(idx << 1 | 1, self.change[idx], right_num)
            self.update[idx] = False
        if self.add_[idx] != 0:
            self.__add_lazy(idx << 1, self.add_[idx], left_num)
            self.__add_lazy(idx << 1 | 1, self.add_[idx], right_num)
            self.add_[idx] = 0

    def build(self, left: int, right: int, idx: int) -> None:
        """
        建树
        :param left: 左边界
        :param right: 右边界
        :param idx: 位置
        :return: None
        """
        if left == right:
            self.sum_[idx] = self.arr[left - 1]
        else:
            mid = (left + right) >> 1
            self.build(left, mid, idx << 1)
            self.build(mid + 1, right, idx << 1 | 1)
            self.__up(idx)
        self.add_[idx] = 0
        self.change[idx] = 0
        self.update[idx] = False

    def update_operation(self, job_left: int, job_right: int, job_value: int) -> None:
        """
        在job_left到job_right区间加上job_value
        :param job_left: 左边界
        :param job_right: 右边界
        :param job_value: 加上的值
        :return: None
        """

        def dfs(l: int, r: int, idx: int) -> None:
            if job_left <= l and r <= job_right:
                self.__update_lazy(idx, job_value, r - l + 1)
            else:
                mid = (l + r) >> 1
                self.__down(idx, mid - l + 1, r - mid)
                if job_left <= mid:
                    dfs(l, mid, idx << 1)
                if mid < job_right:
                    dfs(mid + 1, r, idx << 1 | 1)
                self.__up(idx)
            return

        dfs(1, len(self.arr), 1)

    def increment(self, job_left: int, job_right: int, job_value: int) -> None:
        """
        在job_left到job_right区间加上job_value
        :param job_left: 左边界
        :param job_right: 右边界
        :param job_value: 加上的值
        :return: None
        """

        def dfs(l: int, r: int, idx: int) -> None:
            if job_left <= l and r <= job_right:
                self.__add_lazy(idx, job_value, r - l + 1)
            else:
                mid = (l + r) >> 1
                self.__down(idx, mid - l + 1, r - mid)
                if job_left <= mid:
                    dfs(l, mid, idx << 1)
                if mid < job_right:
                    dfs(mid + 1, r, idx << 1 | 1)
                self.__up(idx)
            return

        dfs(1, len(self.arr), 1)

    def query(self, left: int, right: int) -> int:
        """
        查询区间和
        :param left: 左边界
        :param right: 右边界
        :return: 区间和
        """

        def dfs(l: int, r: int, idx: int) -> int:
            if left <= l and r <= right:
                return self.sum_[idx]
            mid = (l + r) >> 1
            self.__down(idx, mid - l + 1, r - mid)
            ans = 0
            if left <= mid:
                ans += dfs(l, mid, idx << 1)
            if mid < right:
                ans += dfs(mid + 1, r, idx << 1 | 1)
            return ans

        return dfs(1, len(self.arr), 1)


tree = SegmentTreeSumQueryUpdate([1, 2, 3, 4, 5])
print(tree.query(1, 4))
tree.increment(1, 4, 1)
print(tree.query(1, 4))
tree.update_operation(1, 4, 100)
print(tree.query(1, 1))

