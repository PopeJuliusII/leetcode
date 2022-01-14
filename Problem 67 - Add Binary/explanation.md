# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/add-binary/).

## Solution 1

### Solution 1: Explanation

This solution iterates over both numbers, and adds the
result, mod 2, to `res`. `zip_longest` zips the two numbers,
and then continues to feed the `fillvalue` in place of the shorter
string for the duration of the longer string.

### Solution 1: Space Complexity

`O(max(a, b))`, where `a` and `b` are the lengths of `a` and `b`, respectively,
and not their values. Even at their maximum, say, `a = 111` and `b = 111`,
`a + b` cannot have a longer binary representation than `max(len(a), len(b)) + 1`.
This is subsequently housed in `res`.

### Solution 1: Time Complexity

`O(a + b)`, where `a` and `b` are the lengths of `a` and `b`, respectively,
and not their values. We must iterate over both. Note that `res[::-1]` is
an `O(n)` operation, where `n` is the length of `res`.

## Solution 2

### Solution 2: Explanation

This solution iterates over both numbers with pointers, and adds the
result, mod 2, to `res`.

### Solution 2: Space Complexity

`O(max(a, b))`, where `a` and `b` are the lengths of `a` and `b`, respectively,
and not their values. Even at their maximum, say, `a = 111` and `b = 111`,
`a + b` cannot have a longer binary representation than `max(len(a), len(b)) + 1`.
This is subsequently housed in `res`.

### Solution 2: Time Complexity

`O(a + b)`, where `a` and `b` are the lengths of `a` and `b`, respectively,
and not their values. We must iterate over both. Note that `res[::-1]` is
an `O(n)` operation, where `n` is the length of `res`.
