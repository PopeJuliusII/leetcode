# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/merge-two-sorted-lists/).

## Solution 1

### Solution 1: Explanation

This solution is a very simple recursive implementation.
If either of the lists, or, indeed, if both list are `None`,
return the list which is not `None` or `None`. This is also
our base case for the recursion. Otherwise, make the smaller
value `list1`, and make the `next` property the merge of
`list1.next` and `list2`. This works because `list1` is
always smaller, so we essentially recurse with all nodes
but the smallest one.

### Solution 1: Space Complexity

`O(a + b)`, where `a` is the number of nodes in `list1` and
`b` is the number of nodes in `list2`. This is because of the
call stack the recursion causes.

### Solution 1: Time Complexity

`O(a + b)`, where `a` is the number of nodes in `list1` and
`b` is the number of nodes in `list2`. This is because one
may have to visit each node in each list. Inserting nodes
into a linked list, however, is an `O(1)` operation.

## Solution 2

### Solution 2: Explanation

This solution is an iterative implementation. If either of
the lists, or, indeed, if both list are `None`, return the
list which is not `None` or `None`. Otherwise, this solution
attempts to integrate all nodes from `list2` into `list1`
where `list1` is the list with the smaller initial value.
Whilst proceeding down both lists, one of four situations
may occur. If `list2` is `None`, we have succeeded in
integrating all nodes from `list2` into `list1`. Return the
`return_node`. If `list1.next` is `None`, the remainder of
`list2` should be appended to the end of `list1`. Thereafter,
return the `return_node`. If `list1.next.val` is less than
or equal to `list2.val`, move onto the next node in `list1`.
Finally, if `list2.val` is less than `list1.next.val`,
integrate the node into `list1` and continue along `list2`.
Return the `return_node` at the end.

### Solution 2: Space Complexity

`O(1)`. This is because all that is required for this solution
is pointers. No additional list is created; `list2` is simply
integrated into `list1`.

### Solution 2: Time Complexity

`O(a + b)`, where `a` is the number of nodes in `list1` and
`b` is the number of nodes in `list2`. This is because one
may have to visit each node in each list. Inserting nodes
into a linked list, however, is an `O(1)` operation.
