def solution_1(s: list[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


def solution_2(s: list[str]) -> None:
    s.reverse()
