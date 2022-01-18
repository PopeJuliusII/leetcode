# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/intersection-of-two-linked-lists/).

## Solution 1

### Solution 1: Explanation

This solution is based around counting the length of both lists,
ensuring that both heads, `headA` and `headB` are equidistant
from their respective tails, and moving pointers along them at the same
time. If the too equal each other, then, clearly, an intersection
has been found.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored except pointers.

### Solution 1: Time Complexity

`O(m + n)`, where `m` is the number of nodes in `headA`, whilst `n` is
the number of nodes in `headB`.

## Solution 2

### Solution 2: Explanation

This solution uses Floyd's tortoise and hare cycle-finding algorithm.
Fortunately, if you are unaware of the aforementioned, I have written a
[Medium Article](https://medium.com/@edgar-loves-python/the-tortoise-the-hare-and-the-cyclical-linked-list-1b51acab5b?source=friends_link&sk=b8505cbe79e5b73d28c87f0b6f0ec3cf),
which not only goes through this problem in detail, but also explains the
mathematics behind the algorithm. I recommend checking it out! Here, suffice
it to say that if something travelling at two steps an iteration catches
something travelling one step an iteration, we clearly have a cycle.
If however, they never meet, that is because `tortoise` and `hare`,
travelling from `headA`, never traverse the loop created by `final_node`.
Finally, the modified list is restored to its original state, irrespective
of whether an intersection is found with `final_node.next`.

### Solution 2: Space Complexity

`O(1)`. Nothing is stored except pointers.

### Solution 2: Time Complexity

`O(m + n)`, where `m` is the number of nodes in `headA`, whilst `n` is
the number of nodes in `headB`.
