def solution_1(strs: list[str]) -> str:
    longest = strs[0]
    for word in strs:
        p = 0
        while p < len(word) and p < len(longest) and word[p] == longest[p]:
            p += 1
        longest = word[:p]
    return longest


def solution_2(strs: list[str]) -> str:
    p = 0
    for letters in zip(*strs):
        if all(char == letters[0] for char in letters):
            p += 1
        else:
            break
    return strs[0][:p]
