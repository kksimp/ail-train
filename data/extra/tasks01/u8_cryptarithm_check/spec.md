# cryptarithm_check

Checks proposed digit assignments for addition puzzles such as SEND+MORE=MONEY.

## Input
One check per line (blank lines ignored, lines trimmed): `A+B=C ASSIGNMENT`, where A, B and C are words of uppercase letters and ASSIGNMENT is a space-separated list of `L=D` items (L an uppercase letter, D one digit 0-9), separated from the puzzle by a single space.

## Output
One verdict line per check, using the first rule that applies:
1. `malformed` if the line does not have that shape (puzzle without exactly one `+` and one `=`, empty or non-uppercase words, an item that is not `L=D`, no assignment at all).
2. `conflict L` if a letter is assigned twice (first such letter in the assignment list).
3. `missing L` for the first letter of A+B=C, scanned in the order A, B, C, that has no digit.
4. `duplicate digit D` if two different letters share a digit (the smallest such digit).
5. `leading zero W` for the first word of A, B, C (in that order) of length above 1 that starts with a letter assigned 0.
6. `ok` if the numeric sum A + B equals C, otherwise `wrong X + Y != Z` showing the three numbers.
Letters in the assignment that do not occur in the puzzle count for rules 2 and 4 as well.

## Example
Input:
```
SEND+MORE=MONEY S=9 E=5 N=6 D=7 M=1 O=0 R=8 Y=2
AB+C=D A=1 B=2 C=3 D=5
```
Output:
```
ok
wrong 12 + 3 != 5
```
