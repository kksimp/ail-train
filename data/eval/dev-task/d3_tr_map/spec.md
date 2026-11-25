# tr: map characters

Write a program that reads text from standard input and replaces characters, like a small `tr`.

## Input

The first line is the option line: two non-empty words `SET1` and `SET2` separated by exactly one space. Neither set contains a space. Every following line is a data line (it may be empty or contain spaces).

## Rules

- Build a mapping from the characters of SET1 to the characters of SET2, position by position: the character at position i of SET1 maps to the character at position i of SET2.
- If SET2 is shorter than SET1, every position of SET1 beyond the end of SET2 maps to the LAST character of SET2.
- If SET2 is longer, its extra characters are ignored.
- If a character occurs more than once in SET1, only its first occurrence defines its mapping.
- Matching is case-sensitive. Characters not in SET1 are left unchanged.
- Each character of a data line is replaced independently (a replaced character is never replaced again).

## Output

For each data line print the converted line. If there are no data lines (or the input is empty) print nothing.

## Example

Input:

```
abc xyz
abcabc
hello a cab

AbC
```

Output:

```
xyzxyz
hello x zxy

AyC
```
