def solution_1(self, n: int) -> bool:
    for divisor in 2, 3, 5:
        while n and not n % divisor:
            n //= divisor
    return n == 1
