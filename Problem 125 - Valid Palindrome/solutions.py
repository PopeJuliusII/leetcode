def solution_1(s: str) -> bool:
    p = len(s) - 1
    for i, char in enumerate(s):
        if i >= p:
            return True
        if not char.isalnum():
            continue
        while not s[p].isalnum() and i < p:
            p -= 1
        if s[p].lower() != char.lower():
            return False
        p -= 1
    return True


def solution_2(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
