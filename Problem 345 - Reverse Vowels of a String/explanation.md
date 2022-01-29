# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/reverse-vowels-of-a-string/).

## Solution 1

### Solution 1: Explanation

This solution is based upon converting the string to a list,
and then letting pointers run from both ends. Vowels are
then swapped.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `s`. This is due to the
conversion to a list, i.e. `s = list(s)`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `s`. It is important to
note that when computing time complexity, non-dominant terms
are typically dropped, and so are constants. `O(2n)`, for
example, would become `O(n)`. This is relevant, because
in this solution the conversion to the list, and back, are
both `O(n)` operation. As is the use of the two pointers.
Therefore, one might say that the time complexity is actually
`O(3n)`.

## Solution 2

### Solution 2: Explanation

This solution uses two pointers and constructs an `ans`
string by using two pointers to reverse only the vowels.

### Solution 2: Space Complexity

`O(1)`. I would argue that the time complexity is `O(1)`.
The use of the `vowel_set` is `O(1)`, as it does not increase,
irrespective of the size of `s`. I would also argue that
the return objects size should not be included. This is because,
otherwise, the space complexity would be meaningless. Contrast
this solution with Solution 1. There, we create a new list in memory
and a new string (`"".join`, last line). Here, we are only creating
a new string. As stings in Python are immutable, I would argue that
this solution should be labelled `O(1)`, but I understand why others
may state that `ans` makes it an `O(n)` solution.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `s`. This is because we have to
traverse the list once, via the `for` loop.
