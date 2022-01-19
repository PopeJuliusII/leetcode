# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/implement-stack-using-queues/).

## Solution 1

### Solution 1: Explanation

This solution utilises a single queue (using `collections.deque`).
Whilst `push` has a time complexity of `O(n)`, `pop` has a time complexity of
`O(1)`. Whenever a number is added to `self.queue`, it is placed in first position,
i.e. ready to be popped, by first popping every other number in `self.queue`.

### Solution 1: Space Complexity

`O(n)`, where `n` is the length of `self.queue`.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `self.queue`. This is for the `push` operation.
All other operations are `O(1)`. `popleft` on a deque is an `O(1)` operation,
but it would be `O(n)` on a regular list.

## Solution 2

### Solution 2: Explanation

This solution utilises queues (using `collections.deque`) as nodes in a
quasi linked list. Whenever a new item is added, it becomes the "head" of a
new queue, and the former queue becomes the tail node. The result is something
akin to: `[1, [2, [3]]]`. This allows for `O(1)` operations across the board,
whilst sticking to the requirement of only using queues.

### Solution 2: Space Complexity

`O(n)`, where `n` is the length of `self.queue`, nominally. However, given
that each individual item is its own queue, the space complexity is probably
far higher.

### Solution 2: Time Complexity

`O(1)`. As I mentioned, this approach allows for all operations to be
`O(1)`, albeit at the cost of having each individual item wrapped in a queue.
