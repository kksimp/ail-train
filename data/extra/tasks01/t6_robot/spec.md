# Robot on a grid following commands

Standard input:
- line 1: `W H`, the grid size (columns x, rows y; valid cells are 0 <= x < W and 0 <= y < H, y grows towards north);
- line 2: `X Y D`, the robot's start cell and facing D (one of `N E S W`);
- line 3: `K`, the number of obstacle cells; the next K lines are `X Y`, each an obstacle cell;
- all remaining lines are command lines made of the letters `F` (one cell forward), `B` (one cell back), `L` and `R` (turn 90 degrees left or right in place).

A move into a wall (outside the grid) or into an obstacle does not happen; the robot stays and that is a bump. North is y+1, East is x+1.
If the first K+3 lines are not valid (W, H >= 1; the start inside the grid and not on an obstacle; K a non-negative integer; every obstacle an `X Y` pair of integers), print only `bad input`.

For each command line print `X Y D bumps=B`: the robot's cell and facing after the line and the number of bumps during that line.
A command line containing any other character (an empty line is fine, it does nothing) prints `bad command` and is not executed at all.
After all command lines print `final X Y D`.

Example:
    input:  4 3
            0 0 N
            1
            1 1
            FFFRF
            FFFF
    output: 1 2 E bumps=1
            3 2 E bumps=2
            final 3 2 E
