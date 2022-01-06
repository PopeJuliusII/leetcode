def solution_1(s: str) -> int:
    return len(s.split()[-1])


def solution_2(s: str) -> int:
    p_end = len(s) - 1
    while not s[p_end].isalpha():
        p_end -= 1
    p_start = p_end
    while p_start >= 0 and s[p_start].isalpha():
        p_start -= 1
    return p_end - p_start
