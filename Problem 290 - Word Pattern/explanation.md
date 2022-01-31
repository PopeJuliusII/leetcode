# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/word-pattern/).

## Solution 1

### Solution 1: Explanation

This solution uses two hashmaps, i.e. dictionaries, to store the
mappings of letters to words and back. Alternative solutions would
include using [bidict](https://pypi.org/project/bidict/), which is,
as far as I am aware, unavailable on LeetCode. Another alternative,
I have seen solutions where only one dictionary is used, i.e.
`letter_word`, and the line `len(set(pattern)) != len(set(s.split()))`
is used. Basically, if you have "ab" and "foo foo", a single,
letter to word dictionary would not pick up the error. The line
above ensures that we have the same number of unique letters as
unique words. I have chosen not to include a solution like that,
as the use of `set()`, twice, uses up the same space a just using
a second hash map. With the second hash map, however, we can
exit out of the function as soon as we find an error. That
set line creates sets of both full arguments passed in.
For those unaware, `zip_longest` zips two iterables, then
feeds fillvalue for the remainder of the duration of the longest one.
For example, `zip_longest("ab", "a", fillvalue=None)` would yield
`"a", "a"`, and then `"b", None`.

### Solution 1: Space Complexity

`O(n + m)`, where `n` is the length of `pattern`, and `m` is the length
of `s`. This is due to the dictionaries. (`O(2n + 2m)` gets simplified
to `O(n + m)`.

### Solution 1: Time Complexity

`O(n + m)`, where `n` is the length of `pattern`, and `m` is the length
of `s`. We have to iterate over both.
