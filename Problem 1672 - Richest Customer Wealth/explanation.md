# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/richest-customer-wealth/).

## Solution 1

### Solution 1: Explanation

This solution just adds up the total for each account and picks the
largest number.

### Solution 1: Space Complexity

`O(1)`. Nothing is created additionally beyond the original `accounts`.
`sum` just adds up the contents of the account; `max` just checks if
the next value is bigger than the previous one thus far. I want to
emphasise that this use of `max` is as a generator, so no additional
space is used. If you use a list comprehension, i.e. `max([x for x in y])`,
you will have a space complexity of `O(n)`. Please bear that in mind!

### Solution 1: Time Complexity

`O(n * m)`, where `n` is the length of `accounts` and `m` is the length
of the longest list within `accounts`. This is because we iterate over
each list within `accounts` via the use of `sum`, i.e. `m`, and over
`accounts`, via the `max` function, i.e. `n`. Hence, `O(n * m)`.
