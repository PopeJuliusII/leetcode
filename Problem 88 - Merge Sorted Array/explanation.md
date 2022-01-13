# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/merge-sorted-array/).

## Solution 1

### Solution 1: Explanation

This solution points to the largest value in each list, and integrates the values
into `nums1`, until all of `n` has been integrated. As `nums1` is the list to
modify, leaving `m > 0`, i.e. not making it all the way to the start is irrelevant;
as both lists are in order anyway, `nums1` would remain the same, even if we let
`m` run until `m = 0`.

### Solution 1: Space Complexity

`O(1)`. Only pointers are used. `nums1` is passed in with the additional space, and
modified in-place.

### Solution 1: Time Complexity

`O(m + n)`, where `n` and `m` correspond to their values, respectively.
