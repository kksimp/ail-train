# hanoi_moves

Lists the optimal move sequence of the Tower of Hanoi for each request.

## Input
One request per line (blank lines ignored, lines trimmed): `N` or `N FROM TO`, where N is the number of disks (1 to 5) and FROM and TO are pegs among `A`, `B`, `C` (default `A` and `C`). Fields are separated by single spaces. All disks start on FROM, and must end on TO, moving one disk at a time and never placing a larger disk on a smaller one. Disk 1 is the smallest.

## Output
For each valid request print the header `N FROM TO: COUNT moves` and then one line per move, `move DISK FROM TO`, in the standard recursive order (move N-1 disks to the spare peg, move disk N, move N-1 disks onto it). If FROM equals TO the count is 0 and no move lines follow.
For any line that is not valid (N not an integer in 1..5, a peg not in `A B C`, or a wrong number of fields) print `invalid: TEXT` with the trimmed line.

## Example
Input:
```
2 B A
```
Output:
```
2 B A: 3 moves
move 1 B C
move 2 B A
move 1 C A
```
