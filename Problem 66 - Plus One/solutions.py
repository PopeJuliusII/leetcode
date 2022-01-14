def solution_1(digits: list[int]) -> list[int]:
    p = len(digits)
    carry = 1
    while p > 0 and carry:
        p -= 1
        carry, digits[p] = divmod(digits[p] + carry, 10)
    return digits if not carry else [1] + digits


def solution_2(digits: list[int]) -> list[int]:
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            break
        digits[i] = 0
    return digits if digits[0] != 0 else [1] + digits
