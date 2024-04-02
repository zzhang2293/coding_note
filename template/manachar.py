def build(lst: str) -> list:
    n = len(lst) * 2 + 1
    arr = []
    j = 0
    for i in range(n):
        if i & 1 == 0:
            arr.append('#')
        else:
            arr.append(lst[j])
            j += 1
    return arr


def Manacher(arr: str) -> int:
    lst = build(arr)
    n = len(lst)
    p_len = [-1] * n
    max_ = central = right = 0
    for i in range(n):
        len_ = min(p_len[2 * central - i], right - i) - 1 if right > i else 1
        # if the i is in the right, i will give a length that is at least right - i length
        # if not inclusive, then myself is a palindrome so at least 1
        while i + len_ < n and i - len_ >= 0 and lst[i + len_] == lst[i - len_]:
            len_ += 1
        if i + len_ > right:
            right = i + len_
            central = i
        max_ = max(max_, len_)
        p_len[i] = len_
    return max_ - 1


print(Manacher("acaawedfawerffffaqaaabaaawerfawefaaaaa"))


