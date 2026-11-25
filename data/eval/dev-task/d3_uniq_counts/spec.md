# uniq: collapse adjacent duplicate lines

Write a program that reads text from standard input and collapses runs of equal adjacent lines, like a small `uniq`.

## Input

The first line is the option line: either a single `-` (no options) or a string of option letters from `c`, `d`, `u`, `i` in any order without repeats (for example `ci`). Every following line is a data line (it may be empty or contain spaces; spaces are significant).

## Rules

- Split the data lines into groups: a group is a maximal run of consecutive data lines that are equal. Only ADJACENT equal lines are grouped; the same text appearing again later starts a new group.
- With option `i`, two lines are equal when they are equal after converting all letters to lower case (ASCII letters). Without `i`, lines must be identical.
- A group has a count (the number of lines in the run) and a text (the FIRST line of the run, exactly as written).
- Option `d`: keep only groups with count 2 or more.
- Option `u`: keep only groups with count exactly 1.
- If both `d` and `u` are given, no group can be kept.
- Option `c`: print each kept group as its count right-aligned in a field of width 4 (padded with spaces on the left; counts never exceed 9999), then ONE space, then the group's text. Without `c`, print just the text.

## Output

Kept groups in input order, one per line. If there are no data lines, or the input is empty, print nothing.

## Example

Input:

```
c
apple
apple
banana
apple
apple
apple
```

Output:

```
   2 apple
   1 banana
   3 apple
```
