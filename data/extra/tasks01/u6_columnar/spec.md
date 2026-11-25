# columnar transposition

Reads commands from standard input, one per line, and prints one result line per command.

Command format: `MODE KEY TEXT`, fields separated by single spaces. TEXT is the rest of the line (it may contain spaces and may be empty or missing).
- MODE is `E` (encrypt) or `D` (decrypt); any other MODE, or a line with fewer than two fields, prints `bad command`.
- KEY is 2 to 10 ASCII letters (either case, compared without regard to case), else the line prints `bad key`.
- Columnar transposition: TEXT is written in rows of K characters, K being the length of KEY, so the last row may be short. Column i sits under KEY letter i. The columns are read top to bottom in the alphabetical order of their KEY letters; equal letters go left to right. `E` prints that reading. `D` reverses it (the short last row has no padding; columns on the right of a short row are one character shorter). Every character, spaces included, takes part.
- Empty lines print nothing.

Example:
```
E ZEBRAS WE ARE DISCOVERED. FLEE AT ONCE
D ZEBRAS RCDEN IRL EDEFTASEEOEO. CW V AE
```
prints
```
RCDEN IRL EDEFTASEEOEO. CW V AE
WE ARE DISCOVERED. FLEE AT ONCE
```
Empty input prints nothing.
