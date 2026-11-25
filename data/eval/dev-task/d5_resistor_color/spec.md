# d5_resistor_color

Write a command-line program that reads four-band resistor colour codes from standard input and prints the resistance and tolerance of each.

## Input

Zero or more lines. Each line holds colour names separated by one or more spaces or tabs. A line with no words (empty or only whitespace) is ignored, but it still counts when numbering lines. Lines are numbered from 1.

## Rules

A valid line has exactly four colour names, all lower case: `band1 band2 multiplier tolerance`.

- `band1` and `band2` must be digit colours. The digit colours are: black 0, brown 1, red 2, orange 3, yellow 4, green 5, blue 6, violet 7, grey 8, white 9. `band1` and `band2` form the two-digit number `10*band1 + band2` (so it may be below 10, for example black brown is 1).
- `multiplier` is either a digit colour, meaning a factor of 10 to that power (black x1, brown x10, red x100, ... white x1000000000), or `gold` (x0.1) or `silver` (x0.01).
- `tolerance` must be one of these, with the text printed exactly as shown: brown `1`, red `2`, green `0.5`, blue `0.25`, violet `0.1`, grey `0.05`, gold `5`, silver `10`.

The resistance is the two-digit number times the multiplier, an exact value that has at most two decimals. Colours not listed for a position (for example gold as `band1`, or orange as `tolerance`), unknown words, upper-case words and a wrong number of words make the line invalid.

## Output

One line per non-blank input line, in input order:

- valid: `K: R ohm +/-T%` where K is the line number, R is the resistance in ohms written with exactly two decimals (whole part without leading zeros, for example `4700.00`, `0.50`), and T is the tolerance text.
- invalid: `K: invalid`

No input lines (or only blank lines) produce no output.

## Example

Input:

```
yellow violet red gold
brown black green silver

blue grey gold gold
orange orange orange
```

Output:

```
1: 4700.00 ohm +/-5%
2: 1000000.00 ohm +/-10%
4: 6.80 ohm +/-5%
5: invalid
```
