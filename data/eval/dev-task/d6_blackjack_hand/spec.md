# Blackjack hand values

Read blackjack hands from standard input and print the value and status of each hand.

## Input

Each line is one hand: cards separated by whitespace. A card is a single character: `2` to `9`, `T`, `J`, `Q`, `K` or `A` (capital letters only). Lines that are empty after trimming are skipped. If there are no hands, print nothing.

## Rules

- Cards `2` to `9` count as their number. `T`, `J`, `Q`, `K` count 10. An `A` counts 11, but while the total is over 21 and some ace still counts 11, change one ace to count 1 (subtract 10), repeating until the total is 21 or less or no ace counts 11.
- A hand is invalid if any card is not one of the characters above (for example `10`, `1`, `x` or a lowercase letter).
- Status of a valid hand, where `total` is the final total:
  - `blackjack 21` if the hand has exactly 2 cards and the total is 21.
  - `bust TOTAL` if the total is over 21.
  - `TOTAL soft` if the total is 21 or less and at least one ace still counts 11.
  - `TOTAL hard` otherwise.

## Output

One line per hand, in input order: the cards joined by single spaces, then `: `, then the status. For an invalid hand the status is `invalid`.

## Example

Input:

```
A K
A 6
7  8 9
A A 9

5 5 T A
Q 10
```

Output:

```
A K: blackjack 21
A 6: 17 soft
7 8 9: bust 24
A A 9: 21 soft
5 5 T A: 21 hard
Q 10: invalid
```
