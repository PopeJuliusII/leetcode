# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/happy-number/).

## Solution 1

### Solution 1: Explanation

This solution is predicated upon using a set to store numbers we have
previously seen. This provides us with `O(1)` lookup. Here, we are
converting the number to a string a squaring each digit to find the
next value.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of the cycle before the original number
or 1 is reached. This is because of the `visited` set.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of the cycle before the original number
or 1 is reached.

## Solution 2

### Solution 2: Explanation

This solution is predicated upon using a set to store numbers we have
previously seen. This provides us with `O(1)` lookup. Here, we are utilising
a helper function, `_helper`, to find the next value of `n`. It takes each digit
in `n`, squares it, then adds it to a temporary variable, `temp`. It is
also used by Solution 3.

### Solution 2: Space Complexity

`O(n)`, where `n` is the length of the cycle before the original number
or 1 is reached. This is because of the `visited` set.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of the cycle before the original number
or 1 is reached.

## Solution 3

### Solution 3: Explanation

This solution uses Floyd's tortoise and hare cycle-finding algorithm.
Fortunately, if you are unaware of the aforementioned, I have written a
[Medium Article](https://medium.com/@edgar-loves-python/the-tortoise-the-hare-and-the-cyclical-linked-list-1b51acab5b?source=friends_link&sk=b8505cbe79e5b73d28c87f0b6f0ec3cf),
which not only goes through similar problems in detail, but also explains the
mathematics behind the algorithm. I recommend checking it out! Here, suffice
it to say that if something travelling at two steps an iteration catches
something travelling one step an iteration, we clearly have a cycle.
Here, we are utilising a helper function, `_helper`, to find the next
value of `n`. It takes each digit in `n`, squares it, then adds it to
a temporary variable, `temp`. It is also used by Solution 2.

### Solution 3: Space Complexity

`O(1)`. Unlike Solution 1 and Solution 2, we do not need to use a set.
Using no scaling data structures means that we have a space complexity of `O(1)`.

### Solution 3: Time Complexity

`O(n)`, where `n` is the length of the cycle before the original number
or 1 is reached.
