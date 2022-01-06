def solution_1(nums: list[int]) -> int:
    curr = max_val = float("-inf")
    for n in nums:
        curr = max(curr + n, n)
        max_val = max(max_val, curr)
    return max_val
