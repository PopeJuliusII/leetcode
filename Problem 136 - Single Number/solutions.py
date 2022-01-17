from functools import reduce


def solution_1(nums: list[int]) -> int:
    tot = 0
    for n in nums:
        tot ^= n
    return tot


def solution_2(nums: list[int]) -> int:
    return reduce(lambda a, b: a ^ b, nums)
