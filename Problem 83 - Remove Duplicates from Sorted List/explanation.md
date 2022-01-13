# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/remove-duplicates-from-sorted-list/).

## Solution 1

### Solution 1: Explanation

This solution removes each node which matches the value of the current node.
The `next` attribute of the current node is simply shifted to the `next` of the
`next` node.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored in memory beyond pointers.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of the linked list.
