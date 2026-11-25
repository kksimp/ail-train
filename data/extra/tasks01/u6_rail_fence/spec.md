# rail fence

Reads commands from standard input, one per line, and prints one result line per command.

Command format: `MODE N TEXT`, fields separated by single spaces. TEXT is the rest of the line (it may contain spaces and may be empty or missing).
- MODE is `E` (encrypt) or `D` (decrypt); any other MODE, or a line with fewer than two fields, prints `bad command`.
- N is the number of rails and must be an integer from 2 to 10, else the line prints `bad rails`.
- Rail fence (zigzag) cipher: the characters of TEXT are written on N rails going down 0, 1, ..., N-1 then back up N-2, ..., 1, then down again, and so on. `E` prints the rails read from rail 0 to rail N-1, each from left to right. `D` reverses that. Every character, spaces included, takes part.
- Empty lines print nothing.

Example:
```
E 3 WEAREDISCOVERED
D 3 WECRERDSOEEAIVD
```
prints
```
WECRERDSOEEAIVD
WEAREDISCOVERED
```
Empty input prints nothing.
