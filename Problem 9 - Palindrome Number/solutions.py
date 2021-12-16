from math import floor, log10


def solution_1(x: int) -> bool:
    return str(x) == str(x)[::-1]


def solution_2(x: int) -> bool:
    x = str(x)
    p_left, p_right = 0, len(x) - 1
    while p_left < p_right:
        if x[p_left] != x[p_right]:
            return False
        p_left += 1
        p_right -= 1
    return True


def solution_3(x: int) -> bool:
    if x <= 0:
        return x == 0
    pl, pr = 0, floor(log10(x))
    while pl < pr:
        if (x // 10 ** pl) % 10 != (x // 10 ** pr) % 10:
            return False
        pl += 1
        pr -= 1
    return True


def solution_4(x: int) -> bool:
    if x <= 0:
        return x == 0
    x_copy, x_backwards = x, 0
    while x:
        x_backwards *= 10
        x_backwards += x % 10
        x //= 10
    return x_copy == x_backwards
