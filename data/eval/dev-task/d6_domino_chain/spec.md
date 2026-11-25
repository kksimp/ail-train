# Domino chains

Read lines of domino tiles and check whether each line is a valid chain laid out in the given order.

## Input

Each line is one chain: tiles separated by whitespace. A tile is written `L-R` where `L` and `R` are each a single digit from `0` to `6` (for example `3-5`). Lines that are empty after trimming are skipped. If there are no chains, print nothing.

## Rules

- A line is malformed if any tile does not have exactly the form digit, `-`, digit with both digits in `0` to `6`.
- In a well-formed chain the tiles are used exactly as written (a tile is never flipped). The chain is valid when, for every pair of neighbouring tiles, the right number of the first tile equals the left number of the next tile.
- The pip total of a chain is the sum of both numbers of every tile.

## Output

One line per chain, in input order:

- malformed line: `invalid`
- valid chain: `valid PIPS`, where PIPS is the pip total
- otherwise: `broken at N`, where N is the 1-based position of the first tile whose left number does not match the right number of the tile before it

Malformed takes priority: check every tile of the line for the form before looking at matches.

## Example

Input:

```
1-2 2-3 3-3
0-0

4-5 6-1
2-2 2-9 3-3
6-6 6-0 0-4 4-1
```

Output:

```
valid 14
valid 0
broken at 2
invalid
valid 27
```
