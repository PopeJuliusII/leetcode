def solution_1(jewels: str, stones: str) -> int:
    return sum(stone in jewels for stone in stones)


def solution_2(jewels: str, stones: str) -> int:
    jewel_set = set(jewels)
    return sum(stone in jewel_set for stone in stones)
