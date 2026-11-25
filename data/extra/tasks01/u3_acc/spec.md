# acc: an accumulator machine with labels

Reads an assembly program from stdin and runs it. There is one accumulator (starts 0) and 10 memory cells 0..9
(start 0). Each line is trimmed; blank lines and lines starting with `#` are skipped but count for line numbers.
A label line is `NAME:` where NAME starts with a lowercase letter or `_` and continues with lowercase letters, digits
or `_`; it names the next instruction. Other lines are instructions, an upper-case op then an operand, one space between:
- `LOAD n`, `ADD n`, `SUB n`, `MUL n`: n is an integer of at most 6 digits with an optional `-`; acc = n, acc + n, ...
- `STORE m`, `LOADM m`, `ADDM m`, `SUBM m`, `MULM m`: m is one digit 0-9; STORE writes acc to cell m, the others
  read cell m (LOADM sets acc to it, ADDM adds it, and so on)
- `JMP NAME`, `JZ NAME` (jump if acc is 0), `JNEG NAME` (jump if acc < 0)
- `PRINT` (output acc on its own line), `HALT`; these two take no operand

Before running: the first bad line (anything not valid above, or a label defined twice) makes the program print only
`error line K` (K is the 1-based line number). Else, if a jump names a label that is never defined, print only
`error label NAME` for the first such jump in program order.

Running starts at the first instruction and ends at HALT or after the last instruction (a label at the very end
is fine). Each executed instruction is one step. After ADD, SUB, MUL, ADDM, SUBM or MULM, if |acc| > 1000000000 the run
stops at once with `error overflow steps=N` as its last line. If 1000 steps have run and the program has not ended, it
stops with `limit acc=A steps=1000`. Otherwise the last line is `acc=A steps=N`. Printed values come before that line.

Example: `LOAD 3`, `loop:`, `PRINT`, `SUB 1`, `JZ done`, `JMP loop`, `done:`, `HALT` prints 3, 2, 1, then `acc=0 steps=13`.
