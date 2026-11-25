# flood_it

Simulates the moves of a Flood-It game.

## Input
A grid of one or more lines of digits `0`-`9` (each digit a colour, all lines the same length), then one blank line, then one line of moves: colours separated by single spaces. The moves line may be missing or empty.

## Output
The flooded region is the set of cells connected (up/down/left/right) to the top-left cell through cells of the same colour as the top-left cell. A move recolours the whole flooded region to the given colour; any neighbouring cells of that colour then join the region. For each move print `move K colour C region R`, with K the 1-based move number and R the size of the region after the move. After all moves print `flooded` if every cell of the grid is in the region, otherwise `not flooded`.
- A colour that is not a single digit prints `invalid move K` instead of the move line and does not change the grid.
- If the grid lines differ in length, contain a non-digit, or the grid is empty, print only `invalid grid`.

## Example
Input:
```
122
112
333

2 3
```
Output:
```
move 1 colour 2 region 6
move 2 colour 3 region 9
flooded
```
