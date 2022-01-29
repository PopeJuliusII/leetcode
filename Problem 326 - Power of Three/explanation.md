# Solutions

## LeetCode Link

The problem can be found [here](https://leetcode.com/problems/power-of-three/).

## Solution 1

### Solution 1: Explanation

This solution simply uses a `while` loop to determine if
`n` is the product, exclusively, of 3s.

### Solution 1: Space Complexity

`O(1)`. Nothing is stored.

### Solution 1: Time Complexity

`O(log(n))`, where `n` is the value of `n` and the `log` is
base `3`. This is the number of steps it takes to get down
to `n == 1`.

## Solution 2

### Solution 2: Explanation

This solution simply uses `log10` to find the right answer.
Note that `log(n, 3)` does not work! I have left this in
as a commented out line so that you can see. [Here](https://bugs.python.org/issue45348)
is an explanation, but, basically, `log(n, 3)` is just
doing `log10(n) / log10(3)` under the hood anyway;
doing so explicitly, however, leads to numbers precise enough
to use `% 1` on. If you know nothing about `log`, my apologies.
In essence, `log(x, base)`, i.e. log base `base` of `x`, means how
to what power must I raise `base` to get `x`? Therefore, `log(100, 10)`
equals `2`. There's more to it than that, but `log` is outside the
scope of this explanation. And, of course, `n` must be positive.

### Solution 2: Space Complexity

`O(1)`. Nothing is stored.

### Solution 2: Time Complexity

`O(1)`. This solution is maths-based.

## Solution 3

### Solution 3: Explanation

This solution uses `log` and `isclose` to find the right answer.
As mentioned in the explanation for Solution 2, `log(n, 3)`
does not work! [This may explain why.](https://bugs.python.org/issue45348)
`isclose` returns whether the answer returned is out by less than
`1e-12`, which is 10 \*\* -12.
Try `isclose(1, 0.89999999999999999, rel_tol=0.1)` and
`isclose(1, 0.8999999999999999, rel_tol=0.1)` if you have no experience with
`isclose`. Floats are the best!

### Solution 3: Space Complexity

`O(1)`. Nothing is stored.

### Solution 3: Time Complexity

`O(1)`. This solution is maths-based.

## Solution 4

### Solution 4: Explanation

This solution is ensures two things - (1) `n` is positive
and (2) `n` is a factor of `3 ** 19`. Let's start with
number 2. This is predicated upon the fact that `x * x` is
a factor of `x * x * x`. The constraints of the question
state that the largest number we can be provided is `2 ** 31 - 1`.
The largest power of 3 less than this number is `3 ** 19`.
`n` as a power of 3, must be a factor of `3 ** 19`, as
`3 ** 19` is simply `3 * 3 * 3 ....`, whereas our power
of 3 is `3 * 3 ....`. This means that no matter what,
our power will be present. If `n` is not a power
of three, it will not be a factor, as `3` is prime. That
explanation is a bit abstract so let me give you a concrete
example. Let's say that instead of `3 ** 19`, we are using
`4 ** 5`. We want to figure out if `n` is a power of `4`.
Take 8. It would come back a false positive because
even though `2 * 2 * 2` cannot be found in `4 * 4 * 4 * 4 * 4`,
it can be found if the `4` is broken down into its
constituent primes, i.e. `2 * 2 * 2` is in `2 * 2 * 2 ....`.
I feel like I have sufficiently explained this point, so
let's put it all into place. In Python, operator can be chained.
For example, 1 < 2 < 3 or 1 < 2 == 3. That's what is happening
here. You can read it as `n > 0 and 0 == 3 ** 19 % n`.
If `n` is positive and `n` is a factor of `3 ** 19`, we have
a power of three! Mathematical, but without the imprecision
of floating points.

_Credit: This solution comes directly from [here.](https://leetcode.com/problems/power-of-three/discuss/77977/Math-1-liner-no-log-with-explanation)_

### Solution 4: Space Complexity

`O(1)`. Nothing is stored.

### Solution 4: Time Complexity

`O(1)`. This solution is maths-based.
