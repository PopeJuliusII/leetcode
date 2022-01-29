def solution_1(s: str) -> str:
    vowel_set = {char for char in "aeiouAEIOU"}
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l] not in vowel_set:
            l += 1
        while l < r and s[r] not in vowel_set:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)


def solution_2(s: str) -> str:
    vowel_set = {char for char in "aeiouAEIOU"}
    vowel = len(s) - 1
    ans = ""
    for char in s:
        if char not in vowel_set:
            ans += char
        else:
            while s[vowel] not in vowel_set:
                vowel -= 1
            ans += s[vowel]
            vowel -= 1
    return ans
