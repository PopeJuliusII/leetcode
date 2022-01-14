# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/remove-duplicates-from-sorted-list/).

## Solution 1

### Solution 1: Explanation

This solution removes each node which matches the value of the current node.
The `next` attribute of the current node is simply shifted to the `next` of the
`next` node. It is an iterative solution.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored in memory beyond pointers.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of the linked list.

## Solution 2

### Solution 2: Explanation

This solution removes each node which matches the value of the current node.
It does so in a recursive manner, by skipping on if `parent` matches the value
of the node in question (`head`). The base case is `head is None`, and the
original `head` is returned as soon as all duplicates are removed.

### Solution 2: Space Complexity

`O(n)`, where `n` is the length of the linked list. Unlike Solution 1,
this solution is recursive, meaning that we use auxiliary space in the call stack.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of the linked list.
