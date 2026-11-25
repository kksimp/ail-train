# Scrabble placement scoring

Read a series of word placements on a 15 by 15 Scrabble-style board and score each one. Placements are applied in order, so later words can overlap earlier ones.

## Input

Each line is one placement: four fields separated by whitespace: `WORD ROW COL DIR`.

- `WORD`: capital letters `A` to `Z` only.
- `ROW` and `COL`: the square of the first letter, each 1 to 3 decimal digits with no sign (the value must be in 1 to 15 to be on the board). Row 1 is the top and column 1 the left.
- `DIR`: `H` (letters go along increasing columns) or `V` (letters go along increasing rows).

Lines that are empty after trimming are skipped. Other lines are processed in order.

## Letter values

- 1 point: A E I L N O R S T U
- 2 points: D G
- 3 points: B C M P
- 4 points: F H V W Y
- 5 points: K
- 8 points: J X
- 10 points: Q Z

## Premium squares

For a square (r, c), use the first of these rules that matches:

1. Triple word: r and c are both in {1, 8, 15}, except (8, 8).
2. Double word: r is in {2, 3, 4, 5, 8, 11, 12, 13, 14} and (r = c or r + c = 16). (So (8, 8) is a double word.)
3. Triple letter: r and c are both in {2, 6, 10, 14}.
4. Double letter: r is in {1, 8, 15} and c is 4 or 12, or c is in {1, 8, 15} and r is 4 or 12.
5. Otherwise a plain square.

## Rules

A placement is checked in this order; the first problem found rejects it and the board stays unchanged:

1. Format: not exactly four fields, or WORD has any character outside `A` to `Z`, or ROW or COL is not 1 to 3 digits, or DIR is not exactly `H` or `V`: `bad format`.
2. Bounds: the first or last letter lies outside rows 1 to 15 or columns 1 to 15: `out of bounds`.
3. Conflict: going along the word from its first letter, the first square that already holds a different letter: `conflict at R C` with that square's row and column.
4. No new tiles: every letter of the word lands on a square that already holds the same letter: `no new tiles`.

Otherwise the placement is accepted and scored:

- A letter on a square that already holds a tile scores its plain letter value, with no premium.
- A letter placed on an empty square (a new tile) scores its letter value, multiplied by 3 on a triple letter square or by 2 on a double letter square.
- Each new tile on a triple word square multiplies the whole word's score by 3, and each on a double word square by 2 (they combine by multiplication).
- The word's score is the sum of its letter scores, times the word multiplier, plus 50 if exactly 7 new tiles were placed.
- Only the placed word itself is scored (no crossing words). Then the new tiles are put on the board.

## Output

For each processed line, in order, with the fields rejoined by single spaces (`WORD ROW COL DIR`, extra whitespace removed):

- accepted: `TEXT: POINTS`
- rejected: `TEXT: rejected (REASON)` with the reason text from the rules above.

After the last line print `total=T moves=M`, where T is the sum of accepted scores and M the number of accepted placements (`total=0 moves=0` if there were none).

## Example

Input:

```
QUIZ 8 8 H
ZEBRA 8 11 V
FOX 3 4 V
JAZZ 1 1 H
```

Output:

```
QUIZ 8 8 H: 44
ZEBRA 8 11 V: 32
FOX 3 4 V: 26
JAZZ 1 1 H: 117
total=219 moves=4
```
