# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/excel-sheet-column-title/).

## Solution 1

### Solution 1: Explanation

This solution divides `columnNumber - 1` repeatedly by 26 until
it is equal to 1. The remainder is added to 65, as `chr(65)` is "A".
As the remainder, `char_index` can range from 0 to 25, we can can add
anything from `chr(65 + 0)` (A) to `chr(65 + 25)` (Z). We prepend this
value to `row_name`. Finally, `row_name` is returned.

### Solution 1: Space Complexity

`O(1)`. No complex data structures are used.

### Solution 1: Time Complexity

`O(log(columnNumber))`, where `columnNumber` is the value of `columnNumber`,
and the log is base 26.
