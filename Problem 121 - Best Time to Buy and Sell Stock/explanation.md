# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

## Solution 1

### Solution 1: Explanation

This solution relies upon the knowledge that the best one
can possibly do is purchasing at the trough and selling at the peak.
Assume every value you encounter is the peak, and compare it to the lowest value
up to that point. All we need is to store the lowest up to that point,
which we do with `low`, and compare it to the current value we are on.

### Solution 1: Space Complexity

`O(1)`. All we use are pointers.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`.
