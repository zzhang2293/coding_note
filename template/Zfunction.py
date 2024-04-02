def Zfunction(string: str, n: int) -> list:
    z_array = [-1] * n
    z_array[0] = n
    central = right = 1
    for i in range(1, n):
        len_ = min(z_array[i - central], right - i) if right > i else 0
        # at least this long
        while i + len_ < n and string[i + len_] == string[len_]:
            len_ += 1
        if i + len_ > right:
            right = i + len_
            central = i
        z_array[i] = len_
    return z_array


def Efunction(string1: str, string2: str) -> list:
    m, n = len(string1), len(string2)
    string2_z_array = Zfunction(string2, n)
    central, right = 0, 0
    e_array = [0] * n
    for i in range(m):
        len_ = min(right - i, string2_z_array[i - central]) if r > i else 0
        while i + len_ < m and len_ < n and string1[i + len_] == string2[len_]:
            len_ += 1
        if i + len_ > right:
            right = i + len_
            central = i
        e_array[i] = len_
    return e_array
