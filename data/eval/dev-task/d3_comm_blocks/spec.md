# comm: compare two sorted blocks

Write a program that reads two blocks of lines from standard input and prints a three-column comparison, like a small `comm`.

## Input

- Line 1 is the option line: either a single `-` (no options) or a string of the digits `1`, `2`, `3` (no repeats), naming columns to suppress (for example `12`).
- Then block A: the lines up to (not including) the first line that is exactly `---`.
- Then block B: all lines after that `---` line.
- If there is no `---` line, all lines after the option line are block A and block B is empty.

Lines may be empty or contain spaces. Blocks are intended to be sorted ascending but this is not checked; the algorithm below is applied regardless.

## Rules

Keep a position in A and a position in B, both at the start. Repeat until both blocks are used up:

1. If B is used up, or (A is not used up and the current A line is less than the current B line): the A line goes to column 1; advance A.
2. Otherwise, if A is used up, or the current B line is less than the current A line: the B line goes to column 2; advance B.
3. Otherwise (the two lines are equal): the line goes to column 3 (print the text once); advance both.

Strings are compared by their bytes (so every upper-case letter sorts before every lower-case letter).

Printing: a line in a suppressed column is not printed at all. A line in column K is printed as the line text preceded by one TAB character for each column smaller than K that is NOT suppressed. So with no suppression, column 1 has no tab, column 2 has one tab, column 3 has two tabs; with `1` suppressed, column 2 has no tab and column 3 has one.

## Output

The printed lines in the order produced by the algorithm. If nothing is printed, print nothing.

## Example

Input (the four lines of block A are `a`, `b`, `c`, `e`; block B is `b`, `d`, `e`):

```
-
a
b
c
e
---
b
d
e
```

Output (`<TAB>` stands for one tab character):

```
a
<TAB><TAB>b
c
<TAB>d
<TAB><TAB>e
```
