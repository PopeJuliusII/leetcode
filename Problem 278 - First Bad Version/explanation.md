# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/first-bad-version/).

## Solution 1

### Solution 1: Explanation

This solution implements a variation of binary search.
Note two things - a bad version always exists, and `right`
always points to a bad version. The original search
space is covered by [`left`, `right`]. If `mid` is
a bad version, move `right` to it. `right` is always
bad. If `mid` is a good version, move `left` up _past_ it.
The `while` loop ends when `left` becomes corrupted
by becoming a bad version. This is why we move `left`
past `mid`, we need the first bad version. Return
when `left == right`, i.e. we have the first bad version!

### Solution 1: Space Complexity

`O(1)`. Nothing is stored.

### Solution 1: Time Complexity

`O(log(n))`, where `n` is the value of `n`.
