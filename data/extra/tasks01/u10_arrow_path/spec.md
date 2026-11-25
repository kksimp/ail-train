# arrow_path

Follows arrows through a grid from the top-left cell and reports how the walk ends.

Input: non-empty lines forming a grid of equal width (empty lines are ignored). Cells are `^` `v` `<` `>` (arrows moving one cell up, down, left, right) or any other character, which is a dead end.

The walk starts in cell row 0, column 0 and repeatedly moves one cell in the direction of the arrow it stands on. It ends:
- if a move would leave the grid: `exit after N moves`, where N is the number of moves made;
- if it stands on a dead-end cell: `stuck at R,C after N moves` (rows and columns from 0; a dead-end start is stuck after 0 moves);
- if it would enter a cell it already visited: `loop of length L entered at R,C after N moves`, where R,C is the repeated cell, L the number of cells in the cycle and N the number of moves made before the repeat (the repeating move is not counted).
Empty input prints `empty`.

Example input:
```
>>v
^<<
```
Output:
```
loop of length 6 entered at 0,0 after 6 moves
```
