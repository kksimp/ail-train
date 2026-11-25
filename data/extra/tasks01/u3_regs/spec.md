# regs: a register machine

Reads a program on stdin, one instruction per line, and runs it. There are four registers `a b c d`, all starting at 0.
Blank lines and lines starting with `#` are skipped (they are not instructions but still count for line numbers).
Words are separated by single spaces. Instructions are numbered from 0 (skipped lines are not numbered).

- `set R N`: R = N (N is an integer, optional leading `-`)
- `inc R`, `dec R`: add or subtract 1 (values may go negative)
- `jnz R T`: if R is not 0, continue at instruction number T (T is a non-negative integer); otherwise go on
- `halt`: stop

Execution starts at instruction 0 and stops when `halt` runs or when the next instruction number is outside the
program (jumping past the end or running off the end). Every executed instruction counts as one step. If 200 steps
have been executed and the machine has not stopped, it stops with the limit reached.

Output, two lines: `halted steps=N` (or `limit steps=200`), then `a=A b=B c=C d=D`.
An instruction that is not valid (unknown op, wrong word count, bad register, bad number) makes the program print only
`error line K` (K = 1-based line number of the first bad line, checked before running) and stop.

Example: input `set a 3`, `dec a`, `inc b`, `jnz a 1` prints
```
halted steps=10
a=0 b=3 c=0 d=0
```
Empty input: `halted steps=0` and all registers 0.
