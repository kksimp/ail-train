# vigenere

Reads commands from standard input, one per line, and prints one result line per command.

Command format: `MODE KEY TEXT`, fields separated by single spaces. TEXT is the rest of the line (it may contain spaces and may be missing, meaning empty).
- MODE is `E` (encrypt) or `D` (decrypt). Any other MODE, or a line with fewer than two fields, prints `bad command`.
- KEY must be one or more ASCII letters (either case; case does not matter), else the line prints `bad key`.
- Vigenere cipher: each ASCII letter of TEXT is shifted by the next key letter (A=0 .. Z=25), forward for `E`, backward for `D`, wrapping around the alphabet. Letter case of TEXT is kept. Characters that are not ASCII letters are copied unchanged and do not use up a key letter; the key repeats from its start when exhausted.
- Empty lines print nothing.

Example:
```
E LEMON Attack at dawn!
D LEMON Lxfopv ef rnhr!
```
prints
```
Lxfopv ef rnhr!
Attack at dawn!
```
Empty input prints nothing.
