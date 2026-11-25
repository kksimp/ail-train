# Sliding window maximum

Line 1 holds the window size K (digits only, surrounding spaces ignored). Line 2 holds integers separated by
spaces (negative numbers allowed).

Print the maximum of every window of K consecutive numbers, from left to right, on one line separated by single
spaces. Then, on a second line, print `overall: M` where M is the largest of those window maxima.

Special cases, each printing exactly one line instead:
- K is missing, not a positive integer, or line 2 contains a token that is not an integer: `invalid input`
- there are fewer than K numbers (including no numbers): `window too large`

Example input:
```
3
1 3 -1 -3 5 3 6 7
```
Output:
```
3 3 5 5 6 7
overall: 7
```
With K = 1 each number is its own maximum.
