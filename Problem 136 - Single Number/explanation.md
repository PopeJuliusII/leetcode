# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/single-number/).

## Solution 1

### Solution 1: Explanation

This solution is the same as Solution 2, except that it uses a `for` loop
instead of `reduce`. It relies upon two basic properties of the XOR operator:
`A ^ A = 0` and `A ^ 0 = A`. Therefore, all numbers appearing twice
will contribute 0 to `tot`, whilst the unique element will contribute itself.

### Solution 1: Space Complexity

`O(1)`. All we use are `n` and `tot`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`.

## Solution 2

### Solution 2: Explanation

This solution is the same as Solution 1, except that it uses `reduce` instead of
a `for` loop. It relies upon two basic properties of the XOR operator:
`A ^ A = 0` and `A ^ 0 = A`. Therefore, all numbers appearing twice
will contribute 0, whilst the unique element will contribute itself.

### Solution 2: Space Complexity

`O(1)`. We only store numbers in memory.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `nums`.
