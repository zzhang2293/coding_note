class BinarySearch:
    def __init__(self):
        return

    @staticmethod
    def find_int_left(left_boundary: int, right_boundary: int, check: callable) -> int:
        """找到最小能满足 check() 的 x 值"""

        while left_boundary <= right_boundary:
            mid = left_boundary + (right_boundary - left_boundary) // 2
            if check(mid):
                right_boundary = mid - 1
            else:
                left_boundary = mid + 1
        return right_boundary + 1

    @staticmethod
    def find_int_right(left_boundary: int, right_boundary: int, check: callable) -> int:
        """找到最大能满足 check() 的 x 值"""

        while left_boundary <= right_boundary:
            mid = left_boundary + (right_boundary - left_boundary) // 2
            if check(mid):
                left_boundary = mid + 1
            else:
                right_boundary = mid - 1
        return left_boundary - 1

    @staticmethod
    def find_float_left(left_boundary: float, right_boundary: float, check: callable, precision: float) -> float:
        """找到最小能满足 check() 的 x 值"""

        while left_boundary + precision < right_boundary:
            mid = left_boundary + (right_boundary - left_boundary) / 2
            if check(mid):
                right_boundary = mid
            else:
                left_boundary = mid
        return left_boundary if check(left_boundary) else right_boundary

    @staticmethod
    def find_float_right(left_boundary: float, right_boundary: float, check: callable, precision: float) -> float:
        """找到最大能满足 check() 的 x 值"""

        while left_boundary + precision < right_boundary:
            mid = left_boundary + (right_boundary - left_boundary) / 2
            if check(mid):
                left_boundary = mid
            else:
                right_boundary = mid
        return right_boundary if check(right_boundary) else left_boundary



