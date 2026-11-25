# bit flags

Packs named flags into small integers and back. The eight flags and their bit values are: `READ` 1, `WRITE` 2, `EXEC` 4, `HIDDEN` 8, `SYSTEM` 16, `ARCHIVE` 32, `TEMP` 64, `LINK` 128. Flag names are case-sensitive.

Reads commands from standard input, one per line, fields separated by single spaces, and prints one result line per command:
- `pack NAME...` (zero or more names): the flags ORed together, printed as `VALUE 0xHH` with the decimal value and two lower-case hex digits. Repeated names count once. If a name is not a flag, prints `error unknown NAME` for the first such name.
- `unpack N`: prints the names of the flags set in N, in ascending bit order, separated by commas, or `none` if N is 0. N must be a decimal integer (optional leading `-`, digits only): otherwise prints `error number`; if it is outside 0 to 255 prints `error range`.
- `toggle N NAME`: prints N with the NAME bit flipped. `has N NAME`: prints `yes` or `no`. N is checked as for `unpack` and then NAME as for `pack` (`error number`, `error range`, `error unknown NAME`).
- Any other non-empty line (including a wrong number of arguments for `unpack`, `toggle` or `has`) prints `bad command`. Empty lines print nothing.

Example:
```
pack READ EXEC LINK
unpack 133
toggle 133 READ
has 133 WRITE
```
prints
```
133 0x85
READ,EXEC,LINK
132
no
```
Empty input prints nothing.
