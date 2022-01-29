class Solution1:

    def __init__(self, nums: list[int]):
        self.nums = nums
        prefix_array = [0]
        for n in nums:
            prefix_array.append(prefix_array[-1] + n)
        self.prefix_array = prefix_array

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_array[right + 1] - self.prefix_array[left]
