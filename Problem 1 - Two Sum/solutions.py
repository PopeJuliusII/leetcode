def solution_1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def solution_2(nums: list[int], target: int) -> list[int]:
    complement_dict = {}
    for i, n in enumerate(nums):
        if target - n in complement_dict:
            return [complement_dict[target - n], i]
        complement_dict[n] = i
