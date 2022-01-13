# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/plus-one/).

## Solution 1

### Solution 1: Explanation

This solution goes right to left carrying the remainder from each addition.
If we get to the end, i.e. `p == 0` and we still have a `carry`, we append
a 1 to the left of `digits`.

### Solution 1: Space Complexity

`O(1)`. Nothing additional is stored, beyond the pointer, `p`, and one
extra digit in the list.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `digits`. Note that `[1] + digits`
is an `O(n)` operation.

## Solution 2

### Solution 2: Explanation

This solution goes right to left, adding 1 where possible without reaching 10. If the digit to be added to is a 9, it is set to 0, and 1 is added to the
next digit. If the entire number is 9s, a 1 is prepended to the `digits` list.

### Solution 2: Space Complexity

`O(1)`. Nothing additional is stored, beyond the index, `i`, and one
extra digit in the list.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `digits`. Note that `[1] + digits`
is an `O(n)` operation.
