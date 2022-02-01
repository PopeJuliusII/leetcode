# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/ugly-number/).

## Solution 1

### Solution 1: Explanation

This solution simply uses a `while` loop to ascertain whether
2, 3, and 5 are the only factors of `n`.

### Solution 1: Space Complexity

`O(1)`. All we store in memory is `divisor`.

### Solution 1: Time Complexity

`O(1)`. Nominally, all we perform are mathematical operations.
This scales in interesting ways. For instance, the numbers
1024 (2 ^ 10) and 9765625 (5 ^ 10) both require the same number
of computations.
