# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/move-zeroes/).

## Solution 1

### Solution 1: Explanation

This solution simply swaps the last non-zero with the
current number if the current number is not zero.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored; everything happens in-place.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`.

## Solution 2

### Solution 2: Explanation

This solution moves all non-zero numbers to the front, then,
subsequently, overwrites all zeroes.

### Solution 2: Space Complexity

`O(1)`. Nothing is stored; everything happens in-place.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `nums`.
