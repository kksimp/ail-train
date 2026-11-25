# Reversi move replay

Read a Reversi (Othello) position and a list of attempted moves. Apply the moves one after another with strict alternation of players, report each, and print the final position.

## Input

- Line 1: the player to move first, `B` or `W`.
- Lines 2 to 9: the 8 rows of the board from top (row 1) to bottom (row 8). Each row has exactly 8 characters: `.` empty, `B` black, `W` white. Column `a` is the leftmost character, column `h` the rightmost. A cell is named by column letter then row number, for example `d3` is the 4th character of the 3rd row.
- Lines 10 onward: one attempted move per line, a cell name. Lines that are empty after trimming are skipped.

Whitespace around every line is ignored (trim each line).

## Setup errors

Check in this order, and if one applies print only that line and stop (no moves, no board):

1. Line 1 (after trimming, a missing line counts as empty) is not exactly `B` or `W`: `invalid player`
2. There are fewer than 9 lines, or any of lines 2 to 9 is not exactly 8 characters of `.`, `B`, `W`: `invalid board`

## Rules

The player to move is the current player; the other is the opponent.

For a move at cell X, decide in this order:

1. If the text is not exactly a letter `a` to `h` followed by a digit `1` to `8`: illegal, reason `bad cell`.
2. If X is not empty: illegal, reason `occupied`.
3. Look along each of the 8 directions (horizontal, vertical, diagonal) from X. In one direction, step to the neighbouring cells: if you meet one or more opponent discs in a row immediately followed by a disc of the current player, then all those opponent discs are flipped by this move. If you meet an empty cell or leave the board before reaching a current-player disc, nothing is flipped in that direction (and an opponent run that is not followed by a current-player disc flips nothing). If the first neighbour is already a current-player disc, nothing is flipped there. If no direction flips anything: illegal, reason `no flips`.
4. Otherwise the move is legal.

A legal move puts the current player's disc on X, turns all flipped discs to the current player's colour, and then the turn passes to the other player (even if that player has no legal move; there is no pass rule). An illegal move changes nothing and the same player stays on move.

## Output

For each move line, in order, using the trimmed move text and the player who was on move:

- legal: `X P: flipped N: LIST` where `P` is `B` or `W`, `N` is the number of flipped discs and `LIST` is the flipped cell names separated by single spaces, ordered by row number ascending and, within a row, by column ascending.
- illegal: `X P: illegal (REASON)`

After all moves print the final board as 8 lines of 8 characters, then one line `B=nb W=nw next=P` with the counts of black and white discs and the player now on move.

## Example

Input:

```
B
........
........
........
...WB...
...BW...
........
........
........
d3
c3
d3
e3
a1
z9
f5
```

Output:

```
d3 B: flipped 1: d4
c3 W: flipped 1: d4
d3 B: illegal (occupied)
e3 B: illegal (no flips)
a1 B: illegal (no flips)
z9 B: illegal (bad cell)
f5 B: flipped 1: e5
........
........
..WB....
...WB...
...BBB..
........
........
........
B=5 W=2 next=W
```
