# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/longest-common-prefix/).

## Solution 1

### Solution 1: Explanation

This solution applies a depth first search,
seeing how far each word in `strs` matched with
the longest word thus far. Note that `len(strs)`
is always greater than 0.

### Solution 1: Space Complexity

`O(k)`, where `k` is the length of the first
word in `strs`. A single string from `strs` and
a pointer, `p`, are stored. It is interesting
to note that the space used for `longest` is,
at most, `len(strs[0])`. Therefore, irrespective
of an increase in the length of `strs`, our space
complexity is tied to the length of the first
string in `strs`, and does not increase.

### Solution 1: Time Complexity

`O(n)`, where `n` is the combined length of
all words in `strs`. This is because we search
each word, and for each word, we check each character.

## Solution 2

### Solution 2: Explanation

This solution applies a breadth first search.
We search each string's `p`th character,
and if we see that one does not match, we
return the length up to that point. Note that
`len(strs)` is always greater than 0.

### Solution 2: Space Complexity

`O(n)`, where `n` is the length of `strs`.
This is because we take the first letter of
each word in `strs`, meaning that our space
complexity will grow proportionally to an increase
in `len(strs)`. Contrasting this with the space
complexity of Solution 1 is interesting.
Depending on how data is structured, one approach
may be preferable to the other. In short, do we have
many short words (Solution 1 is preferable), or do we
have a few, very long words (Solution 2 is preferable).

### Solution 2: Time Complexity

`O(n)`, where `n` is the combined length of
all words in `strs`. This is because we search
each word, and for each word, we check each character.
