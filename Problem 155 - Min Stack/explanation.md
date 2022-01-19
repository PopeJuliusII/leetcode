# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/min-stack/).

## Solution 1

### Solution 1: Explanation

This solution uses two stacks to emulate a min stack's operations
in `O(1)` time. The concept here is that we always know the smallest number,
as it is at the top of `self.min_stack`. If we encounter it when popping
from `self.stack`, we pop it, too, meaning that we now have the previous
minimum at the top of `self.min_stack`.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `stack`. Naturally, talking about
space complexity is a bit peculiar when it comes to classes. Suffice
it to say that using the two stacks, space increases only linearly
as more values are added to our min stack.

### Solution 1: Time Complexity

`O(1)`. All operations are `O(1)` operations, as all we are doing is
popping off of stacks, or appending to them.
