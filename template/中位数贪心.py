from typing import List


def minOperations(prefix: List[int], l: int, r: int, target: int, pos: int) -> int:
    """
    中位数贪心，货仓选址问题
    :param prefix: the prefix sum of the array
    :param l: start point of nums
    :param r: end point of nums
    :param target: target num
    :param pos: the position of the target num
    :return: the sum of all nums bounded by [l, r) reach the target value
    """

    left = target * (pos - l) - (prefix[pos] - prefix[l])
    right = (prefix[r] - prefix[pos]) - target * (r - pos)

    return left + right





