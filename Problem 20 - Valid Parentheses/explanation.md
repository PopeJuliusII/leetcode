# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/valid-parentheses/).

## Solution 1

### Solution 1: Explanation

This solution uses a stack to store the parentheses we wish to match.
It uses a `parentheses_dict` variable to maintain parentheses pairs.
If a parenthesis is opened, its opposite must close it.
Finally, we return `not stack`, as `stack` evaluating to `True`
would mean we have unclosed parentheses in our string, `s`.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `s`. `parentheses_dict` is `O(1)`,
as it is constant, irrespective of the size of `s`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `s`. We iterate over the entire string.
