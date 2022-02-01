# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/jewels-and-stones/).

## Solution 1

### Solution 1: Explanation

This solution checks if each letter in `stones` is in `jewels`.
`True` is interpreted as 1 by `sum`; `False` as 0.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored in an additional variable.

### Solution 1: Time Complexity

`O(m * n)`, where `m` is the length of `jewels` and `n` is the
length of `stones`. This is because we iterate over each character in
`stones`, for which we have to scan through `jewels`. As `jewels` is
a string, the `in` search is an `O(n)` operation, as each letter in
`jewels` must, potentially, be compared. Hence, `O(m * n)`.

## Solution 2

### Solution 2: Explanation

This solution checks if each letter in `stones` is in `jewel_set`.
`True` is interpreted as 1 by `sum`; `False` as 0.
`jewel_set` is a set containing all the unique items in `jewels`.

### Solution 2: Space Complexity

`O(m)`, where `m` is the number of unique elements in `jewels`.
This is due to the set, `jewel_set`.

### Solution 2: Time Complexity

`O(m + n)`, where `m` is the length of `jewels` and `n` is the
length of `stones`. The `O(m)` comes from creating the set, `jewel_set`,
where we have to iterate over `jewels`. The `O(n)` comes from iterating
over `stones` in the final line. Note that this solution has better
time complexity than Solution 1, but the trade-off is the worse space
complexity.
