# word_search

Finds words in a letter grid.

## Input
A grid of one or more lines of lowercase letters `a`-`z`, then one blank line, then one word per line (the words section may be empty). Words are lowercase letters.

## Output
For each word, in input order, print one line:
- `WORD: ROW,COL DIR` for the first match, with ROW and COL the 1-based position of the first letter and DIR one of `E SE S SW W NW N NE`.
- `WORD: not found` if it is not in the grid.

A word may run in any of the 8 directions. The first match is found by scanning start cells row by row (left to right within a row) and, for each start cell, trying directions in the order `E SE S SW W NW N NE`. A one-letter word matches with direction `E`.

If the grid lines have different lengths, or contain a character outside `a`-`z`, print only `invalid grid`. Blank lines among the words are ignored. If there is no blank line, the whole input is the grid and nothing else is printed. Empty input prints `invalid grid`.

## Example
Input:
```
cat
oxa
dgt

cat
cod
xa
c
cow
```
Output:
```
cat: 1,1 E
cod: 1,1 S
xa: 2,2 E
c: 1,1 E
cow: not found
```
