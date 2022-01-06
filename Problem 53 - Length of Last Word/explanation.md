# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/length-of-last-word/).

## Solution 1

### Solution 1: Explanation

This solution uses the `split` function to separate the words.

### Solution 1: Space Complexity

`O(n)`, where `n` is the number of words in `s`.
This is due to `split` creating a list of the aforementioned.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `s`. This, like the space complexity,
is the result of the `split` operation.

## Solution 2

### Solution 2: Explanation

This solution is just two pointers which designate the two ends of the final word.

### Solution 2: Space Complexity

`O(1)`. Two pointers are used.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `s`.
