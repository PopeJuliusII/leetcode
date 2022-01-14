from itertools import zip_longest


def solution_1(a: str, b: str) -> str:
    res = ""
    carry = 0
    for i, j in zip_longest(reversed(a), reversed(b), fillvalue="0"):
        carry, digit = divmod(int(i) + int(j) + carry, 2)
        res += str(digit)
    if carry:
        res += "1"
    return res[::-1]


def solution_2(a: str, b: str) -> str:
    res = ""
    carry = 0
    pa = len(a) - 1
    pb = len(b) - 1
    while pa >= 0 or pb >= 0 or carry:
        a_val = int(a[pa]) if pa > -1 else 0
        b_val = int(b[pb]) if pb > -1 else 0
        carry, digit = divmod(a_val + b_val + carry, 2)
        res += str(digit)
        pa -= 1
        pb -= 1
    return res[::-1]
