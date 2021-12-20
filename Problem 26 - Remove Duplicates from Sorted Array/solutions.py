def solution_1(nums: list[int], target: int) -> list[int]:
    curr = 1 if nums else 0
    for n in nums:
        if n > nums[curr - 1]:
            nums[curr] = n
            curr += 1
    return curr
