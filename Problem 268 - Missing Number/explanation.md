# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/missing-number/).

## Solution 1

### Solution 1: Explanation

This solution employs a technique whereby each number is used as an index
and multiplied by -1, meaning that we can then find the number which is
still greater than 0. For instance, `[1, 2, 3]` would mean we get `[1, -2, -3]`,
as 1 and 2 would be used as an index to set the value to a negative number.
This leaves two edge cases - 0 and `len(nums)`. Let's start with the latter.
If `len(nums)` is missing, all of our numbers will be negative. The final
return statement will return `len(nums)`. If we have a zero, on the other hand,
we have to set the `zero` boolean to `True`. This is because 0 \* -1 = 0.
Therefore, we will know if the number corresponding to the zero's index is
present by whether `zero` is `True`.

### Solution 1: Space Complexity

`O(1)`. We only constant extra space.

### Solution 1: Time Complexity

`O(n)`, where `n` is the length of `nums`. This is because we have to
iterate over `nums` (twice, actually, but `O(2n)` is cancelled to
`O(n)`.

## Solution 2

### Solution 2: Explanation

This solution computes the sum of the arithmetic sequence from 1 to
`len(nums)`, and compares it to the total of nums. Essentially, an
arithmetic sequence is a bunch of numbers where the difference between
a number and the next number is the same. For example, 3, 5, 7, 9. Or
1, 2, 3, 4. These are both arithmetic sequences. The formula to get the
total for an arithmetic sequence is the first term plus the final term,
multiplied by the number of terms over two. For 1, 2, 3, 4, 5, for example,
this would be (1 + 5) \* (5 / 2), or 6 \* 2.5, or 15. You can verify this:
1 + 2 + 3 + 4 + 5 does, indeed, equal 15. Anyway, let's write this as
`(n / 2) * (a1 + an)`. Let's plug the values we have in:
`(len(nums) / 2) * (1 + len(nums))`. We can rewrite this as
`(len(nums) + len(nums) ** 2) // 2`. This is the sum of the numbers from 0 to
however long `nums` is. Now, one of these numbers is missing. We can find out
which one by subtracting the actual sum. Hence, our solution!

### Solution 2: Space Complexity

`O(1)`. We only constant extra space.

### Solution 2: Time Complexity

`O(n)`, where `n` is the length of `nums`. This is because we have to
iterate over `nums` during `sum`.
