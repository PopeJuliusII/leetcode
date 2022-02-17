# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/nim-game/).

## Solution 1

### Solution 1: Explanation

This solution is based upon the fact that if it is a player's
turn, and four, or a multiple of four, stones are left, that
player will lose. Think about it this way: if there are
four stones, and it is your turn, you may remove 1, 2, or 3.
Irrespective of how many you remove, the opponent will remove
the remainder. If it is your turn and there are more than 4 stones,
say 5, 6, or 7, you can make the opponent have 4 stones left
on the opponent's turn. However, if there are 8 stones and it
is your turn, the opponent will make you have to pull from 4 stones
when it is next your turn. Therefore, if the number of stones on
your turn is 4, you're out of luck. Otherwise, you win!
Note that `n % 4` can be 0 or not 0. 0 is interpreted as `False`.
Everything else is `True`.

### Solution 1: Space Complexity

`O(1)`. We use no additional space.

### Solution 1: Time Complexity

`O(1)`. We are only performing mathematical operations.
