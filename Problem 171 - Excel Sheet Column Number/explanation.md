# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/excel-sheet-column-number/).

## Solution 1

### Solution 1: Explanation

This solution may seem like an overly complex one-liner, but I would
argue that in this case it is justified. All we are doing is summing up
a value for each character in `columnTitle`. What is the value?
`ord(char) - 64` multiplied by some factor. `ord(A)` is, of course,
65, meaning that we shall have values 1 to 26 returned from `ord(char) - 64`,
depending upon `char`. As for the factor, it is simply 26 to
the power of whichever reverse index we are at. So, for example, for
`ABC`, `C` would have a factor of `26 ** 0`, which is 1, `B` would have
a factor of `26 ** 1`, etc. This corresponds to how the column titles work.

### Solution 1: Space Complexity

`O(1)`. No complex data structures are used.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `columnTitle`.
