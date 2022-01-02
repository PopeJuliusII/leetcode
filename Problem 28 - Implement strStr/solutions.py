def solution_1(haystack: str, needle: str) -> int:
    """
    NOTE: TLE - does not pass.
    """
    for h_ptr, _ in enumerate(haystack):
        n_ptr = 0
        while h_ptr < len(haystack) and n_ptr < len(needle) and haystack[h_ptr] == needle[n_ptr]:
            h_ptr += 1
            n_ptr += 1
        if n_ptr == len(needle):
            return h_ptr - len(needle)
    return -1 if needle else 0


def _prefix_suffix(string: str) -> list[str]:
    arr = [0]
    left, right = 0, 1
    while right < len(string):
        if string[left] == string[right]:
            arr.append(left + 1)
            left += 1
            right += 1
        elif left:
            left = arr[left - 1]
        else:
            arr.append(0)
            right += 1
    return arr


def solution_2(haystack: str, needle: str) -> int:
    compute_array = _prefix_suffix(needle)
    h_ptr = n_ptr = 0
    while h_ptr < len(haystack) and n_ptr < len(needle):
        if haystack[h_ptr] == needle[n_ptr]:
            n_ptr += 1
            h_ptr += 1
        elif n_ptr:
            n_ptr = compute_array[n_ptr - 1]
        else:
            h_ptr += 1
    return h_ptr - len(needle) if n_ptr == len(needle) else -1
