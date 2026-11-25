# Stack machine

Read a program from standard input, one instruction per line, run it on an integer stack, and report.

## Input
Each line is split into words on runs of whitespace (spaces or tabs); leading and trailing whitespace is ignored.
A line with no words is skipped (but still counts for line numbering). Lines are numbered from 1.

## Instructions
The stack starts empty and holds integers (the top is the last element pushed).

- `push N`: exactly two words; `N` must be an optional `-` followed by one or more digits `0-9` (a leading `+` is not allowed). Pushes `N`.
- `add`, `sub`, `mul`: pop `b` (top), then `a`; push `a+b`, `a-b`, `a*b` respectively.
- `swap`: exchange the top two elements.
- `dup`: push a copy of the top element.
- `pop`: remove the top element.
- `print`: print the top element (decimal, on its own line) without removing it.

Every instruction other than `push` must consist of exactly one word.

## Errors
Checks are made in this order for each line; the first failure ends the run immediately:
1. The first word is not one of the eight mnemonics (case-sensitive), or the instruction is not `push` and has more than one word: `unknown instruction`.
2. For `push`: the line does not have exactly two words, or the operand is invalid: `bad operand`.
3. The stack has fewer elements than the instruction needs (`dup`, `pop`, `print` need 1; `add`, `sub`, `mul`, `swap` need 2): `stack underflow`.

On a failure print `error: line N: MESSAGE` (N is the line number) and stop; nothing else is printed after it
(output already produced by earlier `print` instructions stays).

## Output
Each `print` produces a line as it executes. If the whole input ran without error, finally print
`stack: ` followed by the elements from bottom to top separated by single spaces, or `stack: empty` if the stack is empty.
All values fit in 64-bit signed integers.

## Example
Input:
```
push 3
push 4
add
dup
print
push 10
swap
sub
print
push -2
mul
```
Output:
```
7
3
stack: 7 -6
```
