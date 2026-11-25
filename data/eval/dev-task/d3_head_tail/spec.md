# head/tail: select lines by range

Write a program that reads text from standard input and prints only the lines selected by a list of ranges.

## Input

The first line is the option line: a comma-separated list of one or more selectors (no spaces). Every following line is a data line (it may be empty). Data lines are numbered from 1, not counting the option line. Let N be the number of data lines.

A selector is one of:

- `A-B`: lines A through B inclusive (A and B are non-negative integers)
- `A-`: lines A through N
- `-B`: lines 1 through B
- `K`: only line K
- `tK`: the last K lines (lines with number greater than N minus K; if K is at least N, all lines)

A selector may name lines beyond N or a reversed range such as `5-2`; such a range simply selects nothing.

## Rules

A data line is printed if at least one selector selects it. Each line is printed at most once, and lines are printed in their original order, whatever the order of the selectors.

## Output

The selected lines, each unchanged, one per line. If nothing is selected, or there are no data lines, or the input is empty, print nothing.

## Example

Input:

```
1,3-4,t1
a
b
c
d
e
f
```

Output:

```
a
c
d
f
```
