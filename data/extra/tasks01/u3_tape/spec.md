# tape: a tiny tape machine

Reads one program from the first line of stdin (further lines are ignored). Only the characters `> < + - . [ ]` are
commands; every other character is skipped. The machine has a tape of 16 cells, all 0, and a pointer at cell 0.
- `>` / `<`: move the pointer right / left
- `+` / `-`: add / subtract 1 at the pointer, wrapping modulo 256 (255 + 1 = 0, 0 - 1 = 255)
- `.`: append the current cell's value to the output list
- `[`: if the current cell is 0, jump to just after the matching `]`
- `]`: if the current cell is not 0, jump back to just after the matching `[`

Before running, brackets are checked: if they are not properly nested and balanced, print only `error brackets`.
Every executed command (including `[` and `]`) is one step. Execution stops when the program ends, when a move would
put the pointer outside cells 0 to 15 (that command still counts as a step), or when 5000 steps have run and a command
is still left to execute.

Output, two lines. First `out:` followed by a space and a value for each output item (so `out:` alone if none).
Second: `ok steps=N`, `pointer steps=N` (for a move outside the tape) or `limit steps=5000`.

Example: `++[>+++<-]>.` prints
```
out: 6
ok steps=19
```
Empty input is an empty program: `out:` and `ok steps=0`.
