def solution_1(n: int) -> bool:
    visited = set()
    while n not in visited:
        visited.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def _helper(n: int, steps: int = 1) -> int:
    for _ in range(steps):
        temp = 0
        while n:
            n, remainder = divmod(n, 10)
            temp += remainder ** 2
        n = temp
    return n


def solution_2(n: int) -> bool:
    visited = set()
    while n not in visited:
        visited.add(n)
        n = _helper(n)
    return n == 1


def solution_3(n: int) -> bool:
    tortoise, hare = _helper(n, 1), _helper(n, 2)
    while tortoise != hare:
        tortoise, hare = _helper(tortoise, 1), _helper(hare, 2)
    return tortoise == 1
