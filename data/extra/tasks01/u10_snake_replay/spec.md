# snake_replay

Replays a game of snake on a small board and prints the final state.

Input, four lines: 
1. `W H`: board width and height (positive integers).
2. The snake, cells `x,y` separated by spaces, head first (at least one cell; x is the column, y the row, both counted from 0 at the top-left).
3. The food queue: cells `x,y` separated by spaces, possibly an empty line.
4. The moves: a string of `U` `D` `L` `R` (up is y-1, left is x-1). May be empty.
All numbers are valid and cells are inside the board.

Replay: for each move (steps numbered from 1) the head goes one cell in that direction.
- A move outside the board ends the game with `over wall at step K`.
- A character that is not U D L R ends the game with `over bad move at step K`.
- Otherwise, if the new head is the first cell of the food queue, the snake grows (the tail stays), the food leaves the queue and the score goes up by 1. Else the tail cell is removed first, then the move is checked: if the new head is on any remaining body cell the game ends with `over self at step K`. (Moving into the cell the tail has just left is fine.)
The state stays as it was before the fatal move.
If all moves are done the result is `alive`.

Output: `result R` (R as above), `length L score S`, then the board: `.` empty, `H` head, `o` body, `*` the first food still in the queue (if any, and the cell is not covered by the snake).

Example input:
```
4 2
1,0 0,0
2,0
RD
```
Output:
```
result alive
length 3 score 1
.oo.
..H.
```
