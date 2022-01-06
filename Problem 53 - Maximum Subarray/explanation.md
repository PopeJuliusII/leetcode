# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/maximum-subarray/).

## Solution 1

### Solution 1: Explanation

This solution implements [Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Empty_subarrays_admitted).
Put simply, we ask two question for each `n` in `nums`.
Which is larger, starting afresh (`n`) or adding to our subarray (`curr + n`)?
Which is larger, the previous maximum (`max_val`) or the current value (`curr`)?

### Solution 1: Space Complexity

`O(1)`. All we store are `curr` and `max_val`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`.
