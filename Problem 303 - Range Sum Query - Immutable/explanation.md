# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/range-sum-query-immutable/).

## Solution 1

### Solution 1: Explanation

This solution is uses a prefix array to determine
the sum between two points. Essentially, if
you know the sum from indices 0 to x and 0 to y,
and x < y, then you can compute the sum between
x and y using subtraction. A prefix array does
just that, storing the sum of all values up to
an index. For instance, `prefix_array[3]` might
equal `sum(array[:3])`. These prefix sums are
useful in many situations. Often, you will see
the index itself included, but I think it is
cleaner like this, i.e. starting the prefix
array with a 0.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `nums`.
In essence, the `prefix_array` duplicates
the amount stored, as it is about the same length
as `nums`.

### Solution 1: Time Complexity

`O(1)`. This applies to all `sumRange` calls.
The `__init__` is an `O(n)` operation, owing to having
to create the `prefix_array`.
