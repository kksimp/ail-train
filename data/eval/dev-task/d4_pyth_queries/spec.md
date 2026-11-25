# Pythagorean triple queries

Write a program that reads query commands from standard input, one per line, and answers each query about Pythagorean
triples. A *triple* is three positive integers `a < b < c` with `a*a + b*b = c*c` (so `a` and `b` are the legs and `c`
is the hypotenuse). A triple is *primitive* if `gcd(a, b) = 1`. Every triple is a primitive triple multiplied by a
positive integer `k = gcd(a, b)`, called its *scale*.

## Input

Zero or more lines. Whitespace at the start and end of each line is removed first. A line that is empty after that, or
that starts with `#`, is skipped (it prints nothing). Every other line is split into words on whitespace; the first word
is the command name. Line numbers count every line of the input (including skipped ones), starting at 1.

Commands (names are lower case and case matters):

- `primitive N` with `1 <= N <= 300`
- `perimeter P` with `1 <= P <= 1000`
- `leg A` with `1 <= A <= 500`

The argument must be the second and last word. It is acceptable if it is an optional `-` followed by one or more ASCII
digits (leading zeros allowed) and its value is in the range given for the command.

## Errors

- If the first word is not one of the three command names, print `line K: unknown command` (`K` = line number).
- If the command name is known but the arguments are wrong (missing, extra words, not an integer in the form above, or
  out of range), print `line K: bad argument`.

After an error, processing continues with the next line.

## Output of each command

All triples listed below are listed as `a b c` with two leading spaces and single spaces between the numbers.

`primitive N`: print `primitive N:` (with `N` the numeric value). Then every primitive triple with `c <= N`, in
increasing order of `c` (ties by increasing `a`), one per line. Then
`  count: primitive X, all Y` (two leading spaces) where `X` is the number of primitive triples listed and `Y` is the
number of all triples (primitive or not) with `c <= N`.

`perimeter P`: print `perimeter P:`. Then every triple with `a + b + c = P` in increasing order of `a`, each line
being `  a b c xS` where `S` is the scale `gcd(a, b)` (the line is the triple, a space, then `x` and the scale). Then
`  count: M` where `M` is the number of triples listed.

`leg A`: print `leg A:`. Then every triple in which `A` is one of the two legs, in increasing order of `c`, one per
line as `  a b c` (so `a < b`, and `A` is either of them). Then `  count: M`.

A count of 0 still prints the header and the count line, with no triple lines between them.

## Example

Input:

```
primitive 30
perimeter 60
leg 5
dance 3
leg 0
```

Output:

```
primitive 30:
  3 4 5
  5 12 13
  8 15 17
  7 24 25
  20 21 29
  count: primitive 5, all 11
perimeter 60:
  10 24 26 x2
  15 20 25 x5
  count: 2
leg 5:
  5 12 13
  count: 1
line 4: unknown command
line 5: bad argument
```
