# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/linked-list-cycle/).

## Solution 1

### Solution 1: Explanation

This solution uses a set to store nodes. If we have previously encountered a node,
then, clearly, a cycle must exist.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of the linked list. This is because of the set,
`node_set`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of the linked list, as we traverse the entire list.

## Solution 2

### Solution 2: Explanation

This solution uses Floyd's tortoise and hare cycle-finding algorithm.
Fortunately, if you are unaware of the aforementioned, I have written a
[Medium Article](https://medium.com/@edgar-loves-python/the-tortoise-the-hare-and-the-cyclical-linked-list-1b51acab5b?source=friends_link&sk=b8505cbe79e5b73d28c87f0b6f0ec3cf),
which not only goes through this problem in detail, but also explains the
mathematics behind the algorithm. I recommend checking it out! Here, suffice
it to say that if something travelling at two steps an iteration catches
something travelling at one step an iteration, we clearly have a cycle.

### Solution 2: Space Complexity

`O(1)`. All we use are two pointers.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of the linked list, as we traverse the entire list.
