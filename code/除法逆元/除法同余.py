from itertools import accumulate
from math import ceil


def DivisionModulo(a: int, b: int, mod: int) -> int:
    mod_a = a % mod
    inv_b = pow(b, mod - 2, mod)
    return mod_a * inv_b % mod


def GetSequenceInv(n: int, mod: int) -> dict:
    inv = {1: 1}
    for i in range(2, n + 1):
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
    return inv


print(GetSequenceInv(10, 101))

a = [1, 1, 1, 1]
print(list(accumulate(a, initial=0)))