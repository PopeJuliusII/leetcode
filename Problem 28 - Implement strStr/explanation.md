# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/implement-strstr/).

## Solution 1

### Solution 1: Explanation

This solution does not pass, it times out. Nonetheless, I felt it worth discussing,
as it provides the starting point for Solution 2. This is probably the most efficient
solution one can come up with off the top of one's head. The premise is simply
to check each character, one by one, from each starting index in `haystack`.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored.

### Solution 1: Time Complexity

`O(n * m)`, where `n` is the length of `haystack` and `m` is the length of `needle`.

## Solution 2

### Solution 2: Explanation

This solution does pass. The concept undergirding Solution 1 is simple. At every
character in `haystack`, we check whether `needle` exists, and we keep checking
until we find a disparity betwixt the two strings. The problem with this approach
is that it is too slow. If one were to check at every index of `haystack`, one would
be pursuing a check potentially along most of `needle` at every index. A more
efficient way of solving this problem is the KMP algorithm. KMP, i.e. Knuth-Morris-Pratt,
is a string search algorithm which runs much faster. Going into much more detail
would be redundant, as I have already written a detailed [medium article](https://www.medium.com)
on the subject. Feel free to check it out if the code is unclear. The basic premise
if simply that for `haystack` `abcabcabd` and `needle` `abcabd`, when comparing
one would inevitably find no match at the final character of needle the first time,
i.e. `haystack[5] != needle[5]`. In Solution 1, we would then start again at
`needle[0]`. However, using KMP, one can recognise that one can continue from
using an `abc` which matches the first `abc` of needle. If that sentence confused
you, please do check out the [medium post](https://www.medium.com).

### Solution 2: Space Complexity

`O(m)`, where `m` is the length of `needle`. This is because of the prefix list.

### Solution 3: Time Complexity

`O(n + m)`, where `n` is the length of `haystack` and `m` is the length of `needle`.
The `O(m)` comes from the preprocessing; the `O(n)` from the matching.
