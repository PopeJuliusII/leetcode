# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/palindrome-number/).

## Solution 1

### Solution 1: Explanation

This solution simply utilises the fact that
strings can be reversed and compared.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `x` as a string.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `x` as a string,
as reversing a string is an `O(n)` operation.

## Solution 2

### Solution 2: Explanation

This solution is predicated upon checking
if the string version of `x` is a palindrome.
It utilises two pointers, which approach each other
from opposite ends of the string.

### Solution 2: Space Complexity

`O(1)`. This is because the pointers are the only additional
usages of space.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `x` as a string.

## Solution 3

### Solution 3: Explanation

This solution is virtually identical to the previous one,
however it complies with the follow-up, which asks for the
number not to be converted into a string. The only slightly
complicated portion of this solution is how each digit is
found. Essentially, the formula `(x // 10 ** p) % 10` simply
isolates the units of `x` divided by a certain power of 10.
`log10` is used to find the limit for the right pointer.
Also, note that anything below 0 cannot be a palindrome,
as the number would start with a minus sign. 0 is palindromic.

### Solution 3: Space Complexity

`O(1)`. This is because the pointers are the only additional
usages of space.

### Solution 3: Time Complexity

`O(n)`, where `n` is the number of digits in `x`.

## Solution 4

### Solution 4: Explanation

This solution relies on making a copy of `x`, then reversing `x`,
one digit at a time. It is probably easier to understand than
Solution 3. Also, note that anything below 0 cannot be a palindrome,
as the number would start with a minus sign. 0 is palindromic.

### Solution 4: Space Complexity

`O(1)`. Contrary to Solution 1, we only store a number as the reversed
format of `x`. Therefore, this is an `O(1)`.

### Solution 4: Time Complexity

`O(n)`, where `n` is the number of digits in `x`.
