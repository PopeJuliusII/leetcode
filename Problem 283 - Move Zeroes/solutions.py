def solution_1(nums: list[int]) -> None:
    switch = 0
    for i, num in enumerate(nums):
        if num:
            nums[i], nums[switch] = nums[switch], nums[i]
            switch += 1


def solution_2(nums: list[int]) -> None:
    slow = 0
    for n in nums:
        if n:
            nums[slow] = n
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1
