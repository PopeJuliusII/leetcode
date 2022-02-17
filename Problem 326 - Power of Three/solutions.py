from math import isclose, log, log10


def solution_1(n: int) -> bool:
    while n > 1 and not n % 3:
        n //= 3
    return n == 1


def solution_2(n: int) -> bool:
    # return n > 0 and not log(n, 3) % 1 # Does not work!
    return n > 0 and not (log10(n) / log10(3)) % 1  # Does work.


def solution_3(n: int) -> bool:
    return n > 0 and isclose(val := log(n, 3), round(val), rel_tol=1e-12)


def solution_4(n: int) -> bool:
    return n > 0 == 3 ** 19 % n
