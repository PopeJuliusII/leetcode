# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array/).

## Solution 1

### Solution 1: Explanation

This solution is simply based upon swapping the positions
of duplicate numbers to position them all at the start of
the list. If a number is new, then place it in the next
available slot. If `nums` is empty, then `curr` should be
zero, and not one. It is typically set to one, as
the first number has never been encountered before.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored beyond `curr`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`. Each number
has to be processed.
