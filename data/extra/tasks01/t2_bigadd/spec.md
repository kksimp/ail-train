# bigadd

Adds non-negative integers of any length given as digit strings, without using big-number library types.

Input: each line holds two tokens `A B` separated by spaces; both must consist only of the digits 0-9 (any length up to 200 digits, leading zeros allowed). Empty lines are skipped silently.

Output: for each non-empty line, one line with the sum A+B in decimal with no leading zeros (`0` for a zero sum). If the line does not have exactly two tokens, or a token has a non-digit character, print `line K: invalid` where K is the 1-based physical line number.

At the end print `sum of sums: S` where S is the total of all printed sums (the successfully computed ones), or `sum of sums: 0` if none.

Example input:
```
999 1
0007 0003
12 x
123456789012345678901234567890 987654321098765432109876543210
```
Output:
```
1000
10
line 3: invalid
1111111110111111111011111111100
sum of sums: 1111111110111111111011111112110
```
