# Digital root chains

Write a program that reads lines of text from standard input. For each line that holds a number it prints the chain
of repeated digit sums that leads down to a single digit, and the number of steps it took.

## Input

Zero or more lines. Each line is processed on its own:

- Leading and trailing whitespace on a line is removed first.
- A line that is empty after that is skipped (it prints nothing).
- Otherwise the line is a *valid number* if it consists only of the ASCII digits `0` to `9` and has between 1 and 18
  characters. Anything else (letters, a sign, a decimal point, inner spaces, 19 or more characters) is invalid.

## Rules

For a valid number `n` (leading zeros are allowed in the input; use the numeric value):

1. The chain starts with `n`.
2. While the last value in the chain is 10 or more, append the sum of its decimal digits.
3. The chain ends when its last value is a single digit (0 to 9). That last value is the digital root.
4. `steps` is the number of values appended, that is, the chain length minus one.

## Output

For each valid number print one line:

`N: V0 -> V1 -> ... -> Vk steps=K`

where `N` is the numeric value of the input (no leading zeros), `V0` is `N`, and the values are joined by ` -> `
(space, hyphen, greater-than, space). A number that is already a single digit prints just `N: N steps=0`.

For each invalid line print `TEXT: invalid` where `TEXT` is the line after whitespace removal.

Empty input prints nothing.

## Example

Input:

```
9875
7
007
12a
```

Output:

```
9875: 9875 -> 29 -> 11 -> 2 steps=3
7: 7 steps=0
7: 7 steps=0
12a: invalid
```
