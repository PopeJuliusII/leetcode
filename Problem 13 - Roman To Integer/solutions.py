def solution_1(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    tot, prev = 0, float("inf")
    for char in s:
        curr = values[char]
        if prev < curr:
            tot -= 2 * prev
        prev = curr
        tot += curr
    return tot


def solution_2(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    combinations = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    tot = p = 0
    while p < len(s):
        if p < len(s) - 1 and (val := combinations.get(s[p] + s[p + 1])):
            tot += val
            p += 2
        else:
            tot += values.get(s[p])
            p += 1
    return tot
