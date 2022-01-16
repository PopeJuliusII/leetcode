def solution_1(n: int) -> int:
    prev = curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def solution_2(n: int, a: int = 1, b: int = 1) -> int:
    return solution_2(n - 1, b, a + b) if n > 1 else b
