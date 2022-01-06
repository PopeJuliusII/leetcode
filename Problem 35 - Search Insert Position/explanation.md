# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/search-insert-position/).

## Solution 1

### Solution 1: Explanation

This solution is a modified binary search. It is based around
ensuring that `left == right` when we get to the desired index.
This is because we move `right` down until it reaches the index, and
`left` up until it reaches `right`. If the code is still unclear, try
understanding why `left` can never be larger than `right`.
If the two are equal, the `while` loop does not run. If `left < right`,
`mid < right`, meaning that at most `mid + 1 == right`, but it
can never be bigger than `right`.

### Solution 1: Space Complexity

`O(1)`. All we use are three pointers, `left`, `mid`, and `right`.

### Solution 1: Time Complexity

`O(log(n))`, where `n` is the length of `nums`. This is because
at every loop we halve our search space. For example, if
`left = 0` and `right = 10`, `mid = 5`, so we have a new
range of 6 - 10 or 0 - 5.
