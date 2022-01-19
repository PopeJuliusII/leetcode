def solution_1(columnTitle: str) -> int:
    return sum((ord(char) - 64) * 26 ** i for i, char in enumerate(reversed(columnTitle)))
