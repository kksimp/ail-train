# Exam seating plan

Reads the room size and a list of students from standard input and prints a seating chart.

The first line is `ROWS COLS` (two integers, each at least 1). Every following non-blank line is one student name (trim
surrounding spaces; names may contain inner spaces). If the first line is not two integers of at least 1, print
`error: bad header` and stop.

Students are sorted by name (byte order). To discourage copying, seats are filled in two passes, both in row-major order
(row 0 first, left to right): first every seat whose column number is even (0, 2, 4, ...), then every seat whose column
number is odd. The k-th sorted student takes the k-th seat of that order.

If there are more students than ROWS*COLS seats, print `error: too many students (N > M)` (N students, M seats) and stop.

Chart: one line per row. Each cell is the name cut to at most 8 characters and padded on the right with spaces to 8, or
`........` for an empty seat; cells are joined with `|`.

Example (`2 3` and students Zoe, Amy, Bob):
```
Amy     |........|Bob
Zoe     |........|........
```
Sorted order is Amy, Bob, Zoe. Even columns 0 and 2 of row 0 get Amy and Bob, then Zoe takes column 0 of row 1.
