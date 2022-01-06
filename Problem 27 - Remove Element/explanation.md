# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/remove-element/).

## Solution 1

### Solution 1: Explanation

This solution simply examines `nums`, traversing it
from both ends. `right_swap` is the final position which
has not been swapped with a number of value `val`.
Once the two pointers meet, we can be certain that all
numbers which are equal to `val` are to the right
of `right_swap`. Note that as we are dealing with indices,
we need to add one to `right_swap` at the end.

### Solution 1: Space Complexity

`O(1)`. This solution only uses pointers to keep track of
which indices to swap.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`. The pointers
start at opposing ends, and the function ends when they
meet.

## Solution 2

### Solution 2: Explanation

This solution iterates over `nums` and stores each number
which is not equal to `val` at the start of the `list`,
as designated by `idx`. Whilst this approach is cleaner
than Solution 1, quite often it is important to maintain
all elements in the `list`, and Solution 1 achieves this,
whilst Solution 2 overwrites all indices which house `val`
and are less than the number of non-`val` values in `nums`.

### Solution 2: Space Complexity

`O(1)`. This solution only uses a single pointer to keep
track of which index to overwrite.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `nums`.
