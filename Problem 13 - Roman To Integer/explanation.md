# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/roman-to-integer/).

## Solution 1

### Solution 1: Explanation

This solution is centered around addition.
Every character is converted and added to the total,
as long as it is not larger than the character which came
before it. Otherwise, it is subtracted from the total.
See Solution 2's explanation for the theoretical
problem with this approach.

### Solution 1: Space Complexity

`O(1)`. The `values` dictionary is of constant space,
irrespective of `s`. The same is true of both `tot` and `prev`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `s`.

### Solution 2: Explanation

This solution is centered around addition, much like
Solution 1. However, a careful reading of the problem
statement illustrates that only in some instances is
a smaller number preceding a larger one to be taken
as a subtraction. For instance, `IM`, according to
the problem statement may justifiably be read `MI`.
Therefore, a `combinations` dictionary is used for
valid combinations. Otherwise, every character is
converted and added to the total, with
`combinations` taking precedence over `values`.

### Solution 2: Space Complexity

`O(1)`. The `values` and `combinations` dictionaries
are of constant space, irrespective of `s`.
The same is true of both `tot` and `p`.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `s`.
