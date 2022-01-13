# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/climbing-stairs/).

## Solution 1

### Solution 1: Explanation

This solution is dynamic programming at its simplest.
It is an implementation of the Fibonacci Sequence.
If this confuses you, I have written a [Medium article](https://medium.com/@edgar-loves-python/dimensionality-in-dynamic-programming-ad36af3b6a61)
on this topic. Suffice it to say that each step can
be reached from 1 or 2 below it, and that all paths
from 1 below it end with a one, and all paths from 2 below it
end with a 2. Therefore, there cannot be any overlap between
the paths from 1 step below and the paths from 2 steps below.

### Solution 1: Space Complexity

`O(1)`. Only `curr` and `prev` exist in memory.

### Solution 1: Time Complexity

`O(n)`, where `n` is the value of `n`.

## Solution 2

### Solution 2: Explanation

This solution is a recursive implementation of Solution 1.
All it is doing is setting `a` to `b` and `b` to `a + b`,
much like Solution 1. The base case is `n == 1`.

### Solution 2: Space Complexity

`O(n)`. The implicit call stack caused by the function calling itself
results in this space complexity. Python has no tail recursion.
In essence, recursion uses memory by taking up space in the call stack.
This is important to remember, especially when contrasting functions which
use a list with functions which use recursion.

### Solution 2: Time Complexity

`O(n)`, where `n` is the value of `n`. The `a + b` operation happens
at every value between `n` and 2, inclusive.
