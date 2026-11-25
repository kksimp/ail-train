# cut: select delimited fields

Write a program that reads text from standard input and prints selected fields of each line, like a small `cut`.

## Input

The first line is the option line. It has exactly this shape: the two characters `d=`, then ONE delimiter character (any character, possibly a space), then a space, then `f=`, then a field list. So the delimiter is the 3rd character of the line and the field list is everything from the 7th character on.

The field list is one or more items separated by commas. Each item is either a positive integer `N` (field N, counting from 1) or a range `A-B` (fields A through B inclusive, with 1 <= A <= B). The option line is always well formed.

Every following line is a data line (it may be empty).

## Rules

- For each data line, if the line does not contain the delimiter character at all, print the line unchanged.
- Otherwise split the line at every occurrence of the delimiter (so `a,,b` has the three fields `a`, empty, `b`, and `,a` has two fields, the first empty).
- Expand the field list into a sequence of field numbers, in the order written; a range expands to its numbers in increasing order. Numbers may repeat and need not be increasing; the output follows the sequence exactly.
- Output the field with each number in the sequence, in sequence order, joined with the delimiter character. A number larger than the count of fields of that line gives an empty field (still joined by the delimiter).

## Output

One output line per data line. If there are no data lines (or the input is empty) print nothing.

## Example

Input:

```
d=, f=1,3
alice,30,paris
bob,25
solo
```

Output:

```
alice,paris
bob,
solo
```
