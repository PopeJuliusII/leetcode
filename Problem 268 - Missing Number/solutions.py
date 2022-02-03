def solution_1(nums: list[int]) -> list[int]:
    zero = False
    for n in nums:
        index = abs(n)
        if index < len(nums):
            nums[index] *= -1
            if not nums[index]:
                zero = True
    for i, n in enumerate(nums):
        if n > 0 or (not n and not zero):
            return i
    return len(nums)


def solution_2(nums: list[int]) -> list[int]:
    return (len(nums) + len(nums) ** 2) // 2 - sum(nums)
