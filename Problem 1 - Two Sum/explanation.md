# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/two-sum/).

## Solution 1

### Solution 1: Explanation

This solution is probably the one which struck you first.
It is, of course, inefficient time-wise, but scrapes past LeetCode's
limits. Notice that it is, however, more space efficient than Solution 2.
The fact that the nested `for` loop starts from `i + 1` means that
a value which is half of the target will not return `[i, j]` where `i = j`,
as `i` never equals `j`.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored.

### Solution 1: Time Complexity

`O(n^2)`, where `n` is the length of `nums`. It's a nested `for` loop.

## Solution 2

### Solution 2: Explanation

This solution is a somewhat less intuitive, but, essentially,
the `complement_dict` stores the number and index.
If the pair is found, the two are returned.

### Solution 2: Space Complexity

`O(n)`, where `n` is the length of `nums`.
The `complement_dict` stores all numbers from `nums` and their indices.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `nums`.
Essentially, one only needs to iterate over `nums` once.
