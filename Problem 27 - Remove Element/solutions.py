def solution_1(nums: list[int], target: int) -> list[int]:
    left_swap, right_swap = 0, len(nums) - 1
    while left_swap <= right_swap:
        if nums[left_swap] == val:
            nums[left_swap], nums[right_swap] = nums[right_swap], nums[left_swap]
            right_swap -= 1
        else:
            left_swap += 1
    return right_swap + 1
